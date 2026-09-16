---
type: gtm.automation
tldr: Show the pack, wait for send
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-outreach-gate module, stood up as a Disabled Opulent automation"
slug: merraine-outreach-gate
uses:
  - "[[spear]]"
schedule:
  tldr: weekday cron
  kind: cron
  expression: "0 7 * * 1-5"
  timezone: America/Chicago
  source: opulent-native
mode: draft-then-wait
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 3
producesArtifact: "outreach-action-<date>.md"
loopGuard: "If an outreach-action file for this pack already exists, stop."
---

# Merraine outreach launch gate

# Overview
When a copy pack is ready, show who / why / which paused campaign, and wait.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine outreach launch gate".

Trigger: When a copy pack artifact lands, and not on a clock until the first-open passes.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an outreach-action file for this pack already exists, stop.

1. Read merraine/playbooks/outreach.
2. Show the pack. Confirm none are below the cut, on suppression, or in an open search.
3. Create or reuse a paused Spear campaign. Do not enable it.
4. Write outreach-action-<date>.md. Wait for the confirm word.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
