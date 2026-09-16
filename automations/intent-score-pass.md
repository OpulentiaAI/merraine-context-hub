---
type: gtm.automation
tldr: Score last night's keepers
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-intent-score module, stood up as a Disabled Opulent automation"
slug: merraine-intent-score
uses:
  - "[[spear]]"
  - "[[parallel]]"
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
producesArtifact: "intent-ranking-<date>.md"
loopGuard: "If an intent-ranking file for today already exists, stop."
---

# Merraine intent-score pass

# Overview
Score researched keepers against [[intent-score]] and hold the cut list.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine intent-score pass".

Trigger: Weekdays at 7:00 AM America/Chicago, after the signal digest exists.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an intent-ranking file for today already exists, stop.

1. If signal-digest for today does not exist, stop and say so.
2. Read merraine/entities/intent-score and merraine/playbooks/scoring.
3. Score each keeper with ICP/30, Title/20, Signal/35, Angle/15 visible.
4. Apply the cut (default 65). Flag collisions (already touched, open search, suppression).
5. Write intent-ranking-<date>.md. Do not write copy in this job.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
