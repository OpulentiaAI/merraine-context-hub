---
type: gtm.automation
tldr: Bump or breakup on the cadence
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-follow-up module, stood up as a Disabled Opulent automation"
slug: merraine-follow-up
uses:
  - "[[gmail]]"
  - "[[spear]]"
  - "[[gojiberry]]"
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
producesArtifact: "follow-up-<date>.md"
loopGuard: "If a follow-up file for today already exists, stop."
---

# Merraine follow-up cadence

# Overview
Propose one bump or one breakup for threads that went quiet. Never as a first touch.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine follow-up cadence".

Trigger: Weekdays at 8:30 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a follow-up file for today already exists, stop.

1. Read merraine/playbooks/follow-up.
2. Include only warm / question / ooo / stalled threads past the wait.
3. One purpose per note. New value in a bump.
4. Write follow-up-<date>.md with wait_until on every row.
5. Do not send.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
