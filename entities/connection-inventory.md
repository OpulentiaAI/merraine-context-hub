---
type: gtm.brief
tldr: Live connections on this workspace
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "mcpConnectors:listInstalledCapabilitiesInternal 2026-09-16"
kind: inventory
---

# Connections

Read from your workspace on 16 September 2026. This is what is actually on,
not what a settings page used to display.

## On

| Name | Kind | What you get |
|---|---|---|
| [[spear]] | MCP | 131 tools. Export already in Drive. |
| [[notion]] | MCP | 42 tools. Shepherd Search Group / Merraine. |
| [[parallel]] | Native | Watches for hiring and market events. |
| [[mesa]] | Native | Workspace versioning, webhook jobs. |

Crustdata is available as enrichment (secret already stored). It is not an
MCP row. Farmers Fridge has already been resolved through it.

## Off, and why it matters

| Name | State | What it blocks |
|---|---|---|
| [[gmail]] | Not connected | Mailbox extraction, voice from sent mail, suppression list |
| [[apollo]] | Trial expired | Optional enrichment cross-check |
| Slack | Not connected | Daily hiring scan already moved to email for this reason |
| HubSpot, ZoomInfo, Fireflies | Not connected | Displayed as connected in an older audit; live tools are zero |
| Similarweb, Outreach, Atlassian, Clay, Monday, Close | Not connected | Waiting on your login if you want them |
| [[gojiberry]] | Not created | Only if you ask |

Sales Navigator is not a connector. It is a LinkedIn seat. See
[[sales-navigator-filters]].
