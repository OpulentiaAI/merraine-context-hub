---
type: gtm.runbook
tldr: Operator Convex seam for Jeremy Sanchez's Opulent account
status: active
owner: operator
updated: 2026-09-16
surface: operator
provenance: "Functions below were called live against prod:confident-sheep-333 on 2026-09-14 and re-read 2026-09-16."
trigger: "Any time an operator needs ground truth about the account, or needs to install hub context"
audience: operator
escalateWhen:
  - "A write would change billing"
  - "A write would send, publish, or contact a human"
  - "The deployment guard in pilot.sh trips"
relatedAutomations: []
---

# Operator Convex seam

Operator-only. Never materialize this file onto Jeremy's workspace.
Identity lives in [[account-identity]]. Leftover notes live in
[[live-knowledge-hygiene]].

Opulent's backend is Convex. This account lives on `prod:confident-sheep-333`.
Everything goes through `scripts/pilot.sh`: reads are free, writes are gated,
every call lands in an evidence ledger.

## Overview

```bash
./scripts/pilot.sh whoami
./scripts/audit.sh
python3 scripts/materialize.py
CONFIRM=send python3 scripts/materialize.py --apply
```

Credentials come from `heavy-production/frontend/.env.deploy`
(`CONVEX_DEPLOY_KEY`, `CONVEX_DEPLOYMENT`). Never print them, never copy them
into this repo, never pass them to a worker.

## Access classes

A deploy key is not a session.

| Class | Reachable with deploy key | Example |
|---|---|---|
| Internal (`internalQuery` / `internalMutation`) | yes | `userIdentityLinks:resolveOwnershipCandidatesInternal` |
| Public, unauthenticated | yes | `creditTracking:getCreditBalance` |
| Public, identity-scoped | no | `mcpConnectors:list` |

Pilot through internal functions and admin actions. When a public query rejects
you, find the `*Internal` sibling. Do not forge a session.

Identity-scoped functions that take no `userId` (`v.object({})`) derive the user
from the session. Read the validator in the error.

## Verified function catalog

| Function | Args | Use |
|---|---|---|
| `actions/authAdmin:checkAccountDetails` | `{email}` | Resolve account, balance, plan |
| `creditTracking:getCreditBalance` | `{userId}` | Balance and plan |
| `creditTracking:getRecentUsageEvents` | `{userId}` | Spend trail |
| `userIdentityLinks:resolveOwnershipCandidatesInternal` | `{email}` | Linked-owner set |
| `workspaceEntities:listForAgentInternal` | `{userId}` | Workspaces and mounted context |
| `workspaceEntities:attachContextForAgentInternal` | `{userId, workspaceId, attached*Ids}` | Mount this hub |
| `knowledgeRunbooks:listKnowledge` | `{userId, limit?}` | What notes exist |
| `knowledgeRunbooks:getKnowledge` | `{userId, noteId}` | Full note |
| `knowledgeRunbooks:createKnowledge` | `{userId, name, content, folder?}` | Install a hub file |
| `knowledgeRunbooks:listRunbooks` | `{userId, limit?}` | What procedures exist |
| `knowledgeRunbooks:getRunbook` | `{userId, runbookId}` | Full runbook |
| `mcpConnectors:listInstalledCapabilitiesInternal` | `{userId}` | Live connector inventory |
| `triggers:listAutomationsInternal` | `{userId}` | Saved automations |
| `drive:listByUserInternal` | `{userId}` | Drive artifacts |
| `memoryBlocks:listForUser` | `{userId}` | Durable memory blocks |
| `threads:getByThreadIdInternal` | `{threadId}` | Thread title and status |
| `agentRuns:getByThreadInternal` | `{threadId}` | Run history |

## Live facts 2026-09-16

```
account    : jeremysanchez@opulentia.ai
plan       : Heavy
balance    : $140.12
workspace  : Default Workspace, mesa=ready, mounted_context=0
automations: 0
```

# Procedure

1. `./scripts/audit.sh`. If `mounted_context` is 0, the hub is not installed.
2. Compare the audit against what you believed. Any difference is the real state.
3. Dry-run first. Every script here defaults to dry.
4. Writes need `CONFIRM=send`. That word is a human decision.
5. Re-run `audit.sh` afterwards and diff.

# Verification

- `evidence/pilot-log-<date>.jsonl` has one line per call.
- `evidence/audit-<date>/SUMMARY.md` is the redacted bundle. Raw note bodies
  that contain secrets stay off git.

# Failure branches

| Symptom | Do this |
|---|---|
| `UNAUTHORIZED / SIGN_IN_REQUIRED` | Find the `*Internal` sibling or read it in the browser. |
| `ArgumentValidationError` | Read the printed validator. |
| Deployment guard trips | Stop. Do not override the guard. |
| A write returns nothing | Re-read. Do not assume. |
