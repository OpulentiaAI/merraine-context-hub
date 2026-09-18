---
type: gtm.source-manifest
tldr: Public-safe source coverage registry skeleton
status: active
owner: Jeremy Sanchez
updated: 2026-09-18
surface: jeremy
provenance: "Public hub contract; private source interface is the authoritative operational registry"
---

# Source coverage registry

This public registry deliberately contains no source payload, contact record,
account identifier, count, raw manifest export, or access credential. It only
keeps the minimum source-level rows needed to make missing coverage visible.
The private source interface and run registry are authoritative for live reach,
authorization, pagination, source ownership, completeness, and suppression.

sources:
  - sourceId: spear
    kind: mcp
    reach: none
    authorization: none
    state: pending
    lastObservedAt: 2026-09-18
    suppressionSurface: no
    covers: "No public payload; private registry owns the actual coverage claim."
    doesNotCover: "Any contact, suppression, campaign, or source-export record."
    privacy: private
  - sourceId: notion
    kind: mcp
    reach: none
    authorization: none
    state: pending
    lastObservedAt: 2026-09-18
    suppressionSurface: no
    covers: "No public payload; private registry owns the actual coverage claim."
    doesNotCover: "Any page, contact, workspace, or source-export record."
    privacy: private
  - sourceId: parallel
    kind: native
    reach: none
    authorization: none
    state: pending
    lastObservedAt: 2026-09-18
    suppressionSurface: no
    covers: "No public payload; private registry owns the actual coverage claim."
    doesNotCover: "Any monitor, signal, contact, or source-export record."
    privacy: private
  - sourceId: mesa
    kind: native
    reach: none
    authorization: none
    state: pending
    lastObservedAt: 2026-09-18
    suppressionSurface: no
    covers: "No public payload; private registry owns the actual coverage claim."
    doesNotCover: "Any webhook, automation, contact, or source-export record."
    privacy: private
