---
type: gtm.playbook
tldr: How to call Gojiberry when it is connected
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS mcp module. Live tool names win over this map."
role: Connector
module: mcp
inputs: ["[[gojiberry]] connected"]
nextOwner: The specialist who asked
relatedSkill: "[[calling-connected-tools]]"
relatedAutomation: "[[connector-health-check]]"
---

# Gojiberry tools

# Job
A map, not a contract. If the live server lists a different name, use the
live name. [[gojiberry]] is not created until Jeremy says to wire it.

# Process
1. Confirm the connector is on. If it is not, research and draft only.
2. Session start: who is connected, then stop guessing.
3. Prefer reads in propose mode. Batch them.
4. After a write, read the row back and report ids.
5. On auth errors: stop. Say reconnect. Do not retry a send loop.

# Output
The tool result, or a named blocker.

# Guardrails
- Never log raw tokens.
- Propose mode never fires a connection request, a message, or a campaign
  mutation.
- ChargeMate's shape: the agent finds, Jeremy reviews, the tool sequences.
  See [[chargemate-human-review]].
