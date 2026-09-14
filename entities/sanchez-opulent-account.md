---
type: gtm.account
title: Sanchez Opulent account
status: active
owner: Jeremy Alston
updated: 2026-09-14
provenance: "Live read: npx convex run actions/authAdmin:checkAccountDetails --prod"
email: jeremysanchez@opulentia.ai
opulentUserId: k57apryqpfeg6h33ybxfynarx58e1dwa
plan: Heavy
deployment: "prod:confident-sheep-333"
balanceCents: 14012
workspaceId: ""
isolated: "yes"
evidence:
  - claim: "user k57apryqpfeg6h33ybxfynarx58e1dwa, Heavy, balance 14012 cents"
    sourceUrl: "convex:prod:confident-sheep-333/actions/authAdmin:checkAccountDetails"
    observedAt: 2026-09-14
    method: cli
    verifiedBy: parent
    confidence: verified
---

# Sanchez Opulent account

## Address trap

Jeremy Alston refers to this account as `jeremysanchez@opulent.ai`. **That address
does not exist** — `checkAccountDetails` returns *User not found*. The real account
is `@opulentia.ai`.

Out of scope, never pilot: `jeremy@merraine.com`, `sanchez@opulentia.ai`.
The linked-owner set for this account is exactly one id.

## Standing state as of the last audit (2026-09-10)

38 threads, 31 runs, all terminal (11 completed / 16 failed / 4 stopped).
Zero active, zero awaiting-auth, zero queued, zero blocked approvals.
Intentional user stops: 0. Surviving autonomous resume candidates: **zero**.
