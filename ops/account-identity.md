---
type: gtm.account
tldr: Operator identity map for Jeremy Sanchez's Opulent account
status: active
owner: operator
updated: 2026-09-16
surface: operator
provenance: "Live Convex read 2026-09-16 via actions/authAdmin:checkAccountDetails and userIdentityLinks:resolveOwnershipCandidatesInternal"
email: jeremysanchez@opulentia.ai
opulentUserId: k57apryqpfeg6h33ybxfynarx58e1dwa
plan: Heavy
deployment: "prod:confident-sheep-333"
balanceCents: 14012
workspaceId: ws_6b932257a9014a51a2ec5d42bb
isolated: "yes"
evidence:
  - claim: "user k57apryqpfeg6h33ybxfynarx58e1dwa, Heavy, balance 14012 cents, one linked owner id"
    tldr: "Verified live 2026-09-16"
    origin: "convex:prod:confident-sheep-333/actions/authAdmin:checkAccountDetails"
    observedAt: 2026-09-16
    method: cli
    verifiedBy: parent
    confidence: verified
---

# Operator identity map

This file must never be materialized onto Jeremy's workspace.

## Address trap

The live account is `jeremysanchez@opulentia.ai`.
`jeremysanchez@opulent.ai` does not exist — `checkAccountDetails` returns
*User not found*.

Out of scope, never pilot: `jeremy@merraine.com` as an Opulent login,
`sanchez@opulentia.ai`. The linked-owner set is exactly one id.

## Standing IDs

```
deployment : prod:confident-sheep-333
account    : jeremysanchez@opulentia.ai
userId     : k57apryqpfeg6h33ybxfynarx58e1dwa
workspace  : ws_6b932257a9014a51a2ec5d42bb  "Default Workspace"
mesa repo  : workspace-ws_6b932257a9014a51a2ec5d42bb (ready)
```

## Live state 2026-09-16

Mounted context is still 0. Knowledge and runbooks exist on the account from
earlier sessions, but none are attached to the workspace. See
`live-knowledge-hygiene.md` before installing this hub.
