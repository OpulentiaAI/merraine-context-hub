---
type: gtm.runbook
tldr: Piloting the account through Convex prod
status: active
owner: Jeremy Alston
updated: 2026-09-14
provenance: "Every function below was called live against prod:confident-sheep-333 on 2026-09-14. Access classes are observed, not assumed."
trigger: "Any time you need ground truth about the account, or need to install/change hub context on it"
audience: operator
escalateWhen:
  - "A write would change billing"
  - "A write would send, publish, or contact a human"
  - "The deployment guard in pilot.sh trips"
relatedAutomations: []
---

# Piloting the account through Convex prod

The control plane for this hub. Opulent's backend is Convex; the account lives on
`prod:confident-sheep-333`. Everything goes through `scripts/pilot.sh` so reads are
free, writes are gated, and every call lands in an evidence ledger.

## Overview

```bash
./scripts/whoami                      # identity + balance, pinned deployment
./scripts/audit.sh                    # full read-only state capture -> evidence/
python3 scripts/materialize.py        # dry run the hub install
CONFIRM=send python3 scripts/materialize.py --apply
```

Credentials come from `heavy-production/frontend/.env.deploy`
(`CONVEX_DEPLOY_KEY`, `CONVEX_DEPLOYMENT`). Never print them, never copy them into
this repo, never pass them to a worker.

## The access rule that matters most

**A deploy key is not a session.** Convex functions on this backend fall into three
classes and only two are reachable from the CLI:

| Class | Reachable with deploy key | Example | Why |
|---|---|---|---|
| Internal (`internalQuery` / `internalMutation`) | **yes** | `userIdentityLinks:resolveOwnershipCandidatesInternal` | No identity check; admin-key callable |
| Public, unauthenticated | **yes** | `creditTracking:getCreditBalance` | Takes `userId` as an argument |
| Public, identity-scoped | **no** | `mcpConnectors:list` | Calls `requireCanonicalIdentity`; fails `UNAUTHORIZED / SIGN_IN_REQUIRED` |

So: **pilot through internal functions and admin actions.** When a public query
rejects you, do not try to forge a session — find the `*Internal` sibling. If there
is none, that state must be read in the browser as the signed-in user, and that is
a different task with a different owner.

A second trap: several identity-scoped functions take **no** `userId` argument at
all (`agentRuns:listAwaitingAuthForUser` validates `v.object({})`). Passing one
returns an `ArgumentValidationError`, which reads like a bad call but is really a
signal that the function derives the user from the session. Read the validator in
the error; it tells you the exact shape.

## Verified function catalog

Called live 2026-09-14. Args are the validated shapes.

| Function | Args | Class | Use |
|---|---|---|---|
| `actions/authAdmin:checkAccountDetails` | `{email}` | action | Resolve an account, balance, plan. Start here. |
| `creditTracking:getCreditBalance` | `{userId}` | public | Balance and plan only |
| `creditTracking:getRecentUsageEvents` | `{userId}` | public | Spend trail |
| `creditTracking:assertSufficientCredits` | `{userId, estimatedCostCents}` | mutation | Admission check before a run |
| `userIdentityLinks:resolveOwnershipCandidatesInternal` | `{email}` or `{authUserId}` | internal | Full linked-owner set. Run before touching anything. |
| `workspaceEntities:listForAgentInternal` | `{userId}` | internal | Workspaces, Mesa repo state, mounted context |
| `workspaceEntities:attachContextForAgentInternal` | `{userId, workspaceId, attached*Ids}` | internal | **Mounts this hub onto the account** |
| `workspaceEntities:listThreads` | `{workspaceId, limit?}` | public | Threads in a workspace |
| `knowledgeRunbooks:listKnowledge` | `{userId, search?, folder?, limit?}` | internal | What reference material exists |
| `knowledgeRunbooks:createKnowledge` | `{userId, name, content, folder?, source?, status?}` | internal | Install a reference file |
| `knowledgeRunbooks:listRunbooks` | `{userId, search?, limit?}` | internal | What procedures exist |
| `knowledgeRunbooks:createRunbook` | `{userId, title, content, macro?, mode?, source?}` | internal | Install a procedure |
| `agentRuns:getByThread` | `{threadId}` | public | Run history for a thread |
| `agentRuns:respondToToolApproval` | approval id + decision | mutation | Deny a credential-printing command |
| `mcpConnectors:list` | session | **blocked** | Read connector state in the browser instead |

## Account facts, verified

```
deployment : prod:confident-sheep-333
account    : jeremysanchez@opulentia.ai
userId     : k57apryqpfeg6h33ybxfynarx58e1dwa   (auth = canonical = legacy, one id)
plan       : Heavy
balance    : 14012 cents
workspace  : ws_6b932257a9014a51a2ec5d42bb  "Default Workspace"
mesa repo  : workspace-ws_6b932257a9014a51a2ec5d42bb  (01M21F5VQWGXPPZZF3Z1HMESXD, ready)
```

At first audit all six `attached*Ids` arrays were **empty** — the account had no
mounted context at all. That is the hole this hub fills.

## Procedure

1. `./scripts/audit.sh`. Read the summary. If `mounted_context` is 0, the hub is
   not installed.
2. Compare the audit against what you believed. Any difference is the real state.
3. For a change, dry-run first. Every script here defaults to dry.
4. Writes need `CONFIRM=send` in the environment. That word is a human decision,
   not a default you set in a script.
5. Re-run `audit.sh` afterwards and diff. A write you cannot see in a fresh read
   did not happen.

## Verification

- `evidence/pilot-log-<date>.jsonl` has one line per call with function, args, exit.
- `evidence/audit-<date>/` holds the raw JSON for every capture.
- Claims in any report trace to a file in that directory.

## Failure branches

| Symptom | Do this |
|---|---|
| `UNAUTHORIZED / SIGN_IN_REQUIRED` | Identity-scoped function. Find the `*Internal` sibling or move the read to the browser. |
| `ArgumentValidationError` | Read the printed validator. It is the authoritative signature. |
| `CONVEX_DEPLOYMENT is ... expected prod:confident-sheep-333` | Something repointed the backend. Stop. Do not override the guard. |
| A write returns nothing | Convex mutations often return a bare id or null. Verify by re-reading, never by assuming. |
| Balance moved unexpectedly | Stop all automations, capture `getRecentUsageEvents`, and escalate. |
