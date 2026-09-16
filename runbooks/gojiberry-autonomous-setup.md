---
type: gtm.runbook
tldr: Gojiberry setup and MCP wiring
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "github.com/OpulentiaAI/gojiberryai-sales-os README; connector UI verified 2026-09-08"
trigger: "Jeremy says wire up Gojiberry"
audience: jeremy-sanchez
escalateWhen:
  - "Signup requires a paid plan or a card"
  - "LinkedIn connection needs Jeremy's own login"
  - "A CAPTCHA or identity document is presented"
relatedAutomations: []
---

# Gojiberry setup and MCP wiring

Jeremy says **wire up Gojiberry**. Everything before LinkedIn is the agent's job.

## Overview

Gojiberry is a 13-desk outbound department sitting over a hosted connector. It
proposes. It does not send. That matches this hub.

## Procedure

### 1. Create the account

Open `https://gojiberry.ai/` and sign up. Store the credential in Opulent
Secrets the instant it is visible. Do not defer that write.

Use a real mailbox Jeremy names. If none is available, stop and ask.

**Stop if a card is required.** Do not pay or upgrade without asking.

### 2. Teach it the ICP

Add Merraine's website, then override the inferred profile with
[[merraine-icp]]. Keep `[NEED: x]` markers intact.

### 3. Get the MCP URL

Settings → Connect MCP. If the workspace issues a unique URL, use that.
Otherwise the default is `https://mcp.gojiberry.ai/mcp`.

### 4. Wire it into this Opulent account

Settings → Connectors → MCP servers. Use **Add custom MCP**:

| Field | Value |
|---|---|
| Name | `gojiberry` |
| Server URL | the workspace MCP URL from step 3 |
| Transport | HTTP (SSE only if HTTP discovery fails) |
| Custom Headers JSON | auth header if the workspace issued a key, else empty |

Discovery runs on submit. A row that says connected with a tool count is
proof. A row that errors is a real failure — read the label.

### 5. Verify before calling it done

- A fresh read shows `gojiberry` connected with tool count > 0.
- One read-only question: *"Show me my Gojiberry workspace — campaigns, lists,
  and intent breakdown. Don't change anything."*
- Update [[gojiberry]]: `connected: yes`, real `toolCount`, evidence row.

## Verification

Done means: connector row green with a tool count, one read-only query
answered from real workspace data, [[gojiberry]] updated, and **no campaign
created and no message sent**.

## Failure branches

| Symptom | Do this |
|---|---|
| Signup wants a card | Ask Jeremy. Do not pay. |
| MCP row errors on submit | Read the probe label. Try SSE once. Then write the error on [[gojiberry]] and move on. |
| LinkedIn connect needs Jeremy's login | Stop. That click is his. |
| Tool count is 0 but the row says connected | Treat as failed. |
