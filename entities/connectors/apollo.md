---
type: gtm.connector
tldr: Apollo
status: blocked
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "mcpConnectors:listInstalledCapabilitiesInternal 2026-09-16; earlier note that app.apollo.io redirects to trial-expired upgrade"
slug: apollo
kind: mcp
connected: error
toolCount: 0
scopes: []
authOwner: Jeremy Sanchez
blockerNote: "Trial expired. Not connected."
evidence:
  - claim: "Apollo MCP present and disconnected"
    tldr: "Apollo MCP present and disconnected"
    origin: "convex:mcpConnectors:listInstalledCapabilitiesInternal"
    observedAt: 2026-09-16
    method: cli
    verifiedBy: parent
    confidence: verified
---

# Apollo

Enrichment cross-check only. The Apollo trial is expired, so this connector
does nothing right now.

If turning it back on means a paid plan, say so and we drop it. Enrichment
already runs Monid first, then Crustdata. Farmers Fridge has already been
resolved that way.
