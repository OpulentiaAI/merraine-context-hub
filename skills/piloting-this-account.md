---
type: hub.skill
name: piloting-this-account
description: "Pilot, audit, or change Jeremy Sanchez's Opulent account through Convex prod. Use when checking account state, connector status, balance, threads, or when installing and mounting hub context. Triggers: audit the account, check his balance, is X connected, mount the hub, what runs on his account."
triggers: [audit, balance, connector, mount, install hub, convex, prod, account state]
readWhen: "Before any claim about what is true on the account"
doNotUseFor: ["Sending anything", "Changing billing", "Anything requiring a signed-in browser session"]
---

# Piloting this account

Read [[convex-pilot]]. The short version:

- `./scripts/audit.sh` first, every session. Claims come from the evidence bundle,
  not from memory.
- Reads are free. Writes need `CONFIRM=send`, which represents a human decision.
- A deploy key is not a session. Identity-scoped functions (`mcpConnectors:list`)
  will reject you; use the `*Internal` sibling or read it in the browser.
- `mounted_context: 0` in the audit summary means this hub is not installed.
