---
type: gtm.runbook
title: Gojiberry autonomous setup and MCP wiring
status: active
owner: Opulent
updated: 2026-09-14
provenance: "github.com/OpulentiaAI/gojiberryai-sales-os README; Opulent MCP connector UI verified 2026-09-08"
trigger: "Jeremy asks for Gojiberry, or an automation needs a 13-desk outbound department"
audience: opulent
escalateWhen:
  - "Signup requires a paid plan or a card"
  - "LinkedIn connection requires Jeremy Sanchez's own credentials"
  - "A CAPTCHA or identity document is presented"
relatedAutomations: []
---

# Gojiberry autonomous setup and MCP wiring

**Goal: Jeremy says "wire up Gojiberry" and nothing else is required of him until
the LinkedIn auth step.** Everything before that is yours to do.

## Overview

Gojiberry is a 13-agent outbound department (Signal Hunter, ICP Analyst, Account
Researcher, Lead Enricher, Intent Scorer, LinkedIn Copywriter, Outreach Operator,
Reply Agent, Follow-up Agent, Meeting Qualifier, Pipeline Analyst, Sales Manager,
Head of Sales) sitting over a hosted MCP. It is markdown plus an MCP URL — there is
no code to review. Its default mode is **propose, don't send**, which matches this
hub's send policy exactly.

## Procedure

### 1. Create the account

Open `https://gojiberry.ai/` and sign up. Use the Aside password manager to
generate and store the credential at creation time — **persist it the instant it is
visible**, before clicking through. Do not defer the vault write.

Registration identity: use an operator-controlled mailbox, not `paul@opulent.ai`-style
aliases that are Opulent identities rather than real mailboxes. If no real mailbox
is available for this signup, that is an escalation, not a workaround.

**Stop and escalate if a card is required.** Do not pay or upgrade without asking.

### 2. Teach it the ICP

Add Merraine's website so it learns the ICP, then override the inferred profile with
ours. Copy `[[merraine-icp]]` into its ICP context. Keep `[NEED: x]` markers intact —
an honest gap beats a confident guess.

### 3. Get the MCP URL

Settings -> Connect MCP. If the workspace issues a **unique** MCP URL, use that one.
Otherwise the default is `https://mcp.gojiberry.ai/mcp`.

### 4. Wire it into Jeremy's Opulent account

The connector UI is at `platform.opulentia.ai/dashboard/settings/credentials`,
under the **MCP servers** tab. (`/dashboard/settings/connections` 404s — do not
send him there.)

Use **Add custom MCP**:

| Field | Value |
|---|---|
| Name | `gojiberry` |
| Server URL | the workspace MCP URL from step 3 |
| Transport | HTTP (fall back to SSE only if HTTP discovery fails) |
| Custom Headers JSON | auth header if the workspace issued a key, else empty |

Discovery runs **synchronously on submit**, so the new row's status label *is* the
probe result. A row that says connected with a tool count is your proof. A row that
errors is a real failure — read the label, do not retry blindly.

### 5. Verify before declaring success

- Fresh read-only connector discovery shows `gojiberry` connected with tool count > 0.
- Ask it one read-only question: *"Show me my Gojiberry workspace — campaigns, lists,
  and intent breakdown. Don't change anything."* A real answer proves the wiring.
- Update `[[gojiberry]]` in this hub: `connected: yes`, real `toolCount`, and an
  evidence row citing the discovery read.

### 6. Hand it the desks

Copy `skills/sales-os/` from `OpulentiaAI/gojiberryai-sales-os` into the account's
skill surface, or point Opulent at the repo. Then register the five commands as hub
workflows: `/sales-os:outbound`, `:find-leads`, `:research`, `:replies`, `:pipeline`.

## Verification

Done means: connector row green with a tool count, one read-only query answered from
real workspace data, `[[gojiberry]]` updated with evidence, and **no campaign created
and no message sent**.

## Failure branches

| Symptom | Do this |
|---|---|
| Signup wants a card | Escalate to Jeremy. Do not pay. |
| MCP row errors on submit | Read the probe label verbatim. Try SSE once. If it still fails, capture the exact error into `[[gojiberry]]` `blockerNote` and move on — do not block the rest of setup. |
| LinkedIn connect needs Sanchez's own login | Escalate. This is a credential, one of the three things that reach a human. |
| Tool count is 0 but row says connected | Treat as failed. A connector with no tools is not wired. |
