---
type: mcp.skill::au-mcp-sdk
name: calling-connected-tools
description: "Call a live connected tool by its real name. Use when asked which tools are on, to call Gojiberry, or whether a connector is ready. Triggers: is Gojiberry connected, list tools, call the connector, MCP health."
---

# Calling connected tools

Read [[mcp]] and [[connection-inventory]]. Live names win.

If a connector is off, say so and stop. Do not create it. Do not fire
OAuth. Prefer reads.
