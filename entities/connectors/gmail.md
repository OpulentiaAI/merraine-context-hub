---
type: gtm.connector
tldr: Gmail
status: blocked
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Live capabilities 2026-09-16 show no Gmail install; thread 'Search the web' has two runs failed with authentication not completed within 10 minutes"
slug: gmail
kind: composio
connected: no
toolCount: 0
scopes: []
authOwner: Jeremy Sanchez
blockerNote: "Not connected. Two login attempts on 2026-09-10 timed out after 10 minutes."
evidence:
  - claim: "Gmail is not in the live capability inventory; Search the web thread has two auth timeouts"
    tldr: "Gmail still disconnected"
    origin: "convex:mcpConnectors:listInstalledCapabilitiesInternal + agentRuns:getByThreadInternal"
    observedAt: 2026-09-16
    method: cli
    verifiedBy: parent
    confidence: verified
---

# Gmail

The highest-value unlock. Gmail is what lets us rebuild your relationships,
your voice from mail you actually sent, and the suppression list.

Connect it in Settings → Connectors. Two earlier login attempts on the
"Search the web" thread timed out after ten minutes. Nothing here can finish
that click for you.

Once it is connected, [[email-communications-extraction]] runs read-only.
Nothing is sent, filed, or labelled.
