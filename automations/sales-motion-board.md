---
type: gtm.automation
tldr: Daily motion board
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-motion-board module, stood up as a Disabled Opulent automation"
slug: merraine-motion-board
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
costCeilingUsd: 1
producesArtifact: "motion-board-<date>.md"
loopGuard: "If a motion-board file for today already exists, stop."
---

# Merraine sales-motion board

# Overview
Write the day's board and the next three actions. Do not do the specialist work in this job.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine sales-motion board".

Trigger: Weekdays at 6:15 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a motion-board file for today already exists, stop.

1. Read merraine/playbooks/routing and merraine/entities/icp-context.
2. Count rows in each stage from artifacts that already exist. Do not invent counts.
3. Name the next three actions and who owns each.
4. Write motion-board-<date>.md.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
