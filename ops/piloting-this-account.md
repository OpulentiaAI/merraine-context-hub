---
type: mcp.skill::au-mcp-sdk
name: piloting-this-account
description: "Operator-only. Audit or change Jeremy Sanchez's Opulent account through Convex. Never mount this skill on his workspace."
surface: operator
---

# Piloting this account

Operator-only. Read [[convex-pilot]] and [[account-identity]].

- `./scripts/audit.sh` first. Claims come from the evidence bundle.
- Reads are free. Writes need `CONFIRM=send`.
- A deploy key is not a session.
- `mounted_context: 0` means this hub is not installed.
- Do not attach leftover notes listed in [[live-knowledge-hygiene]].
