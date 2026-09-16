---
type: gtm.automation
tldr: List live connectors and stop on a guess
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS mcp module, stood up as a Disabled Opulent automation"
slug: merraine-connector-health
uses:
  - "[[spear]]"
  - "[[notion]]"
  - "[[parallel]]"
  - "[[gojiberry]]"
schedule:
  tldr: weekday cron
  kind: cron
  expression: "0 7 * * 1-5"
  timezone: America/Chicago
  source: opulent-native
mode: read-only
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 1
producesArtifact: "connector-health-<date>.md"
loopGuard: "If a connector-health file for today already exists, stop."
---

# Merraine connector-health check

# Overview
Read which connectors are actually on. Live tool names win over the map
in [[mcp]]. Do not fire a connection request.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine connector-health check".

Trigger: Weekdays at 6:05 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a connector-health file for today already exists, stop.

1. Read merraine/playbooks/mcp and merraine/entities/connection-inventory.
2. List each connector: connected / not / error, and the live tool names if the server answers.
3. If a live name differs from the map, prefer the live name and say so.
4. If Gojiberry is not connected, say so. Do not create it.
5. Write connector-health-<date>.md. No writes. No reconnect loops.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not create a connector or fire an OAuth request
- Do not log raw tokens
