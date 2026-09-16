---
type: gtm.automation
tldr: Book, ask, or pass
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-meeting-qual module, stood up as a Disabled Opulent automation"
slug: merraine-meeting-qual
uses:
  - "[[gmail]]"
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
producesArtifact: "qualification-<date>.md"
loopGuard: "If a qualification file for today already exists for the same threads, stop."
---

# Merraine meeting qualification

# Overview
On interested threads, fill problem / role / timing / fit and hold a brief for Jeremy.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine meeting qualification".

Trigger: When an interested row lands, and weekdays at 9:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a qualification file for today already exists for the same threads, stop.

1. Read merraine/playbooks/qualification.
2. Take only interested threads from today's triage.
3. Status book, ask, or pass. Quote the problem.
4. Write qualification-<date>.md. Do not put a time on Jeremy's calendar.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
