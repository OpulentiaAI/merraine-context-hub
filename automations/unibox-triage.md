---
type: gtm.automation
tldr: Classify overnight replies
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-unibox-triage module, stood up as a Disabled Opulent automation"
slug: merraine-unibox-triage
uses:
  - "[[gmail]]"
  - "[[gojiberry]]"
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
producesArtifact: "unibox-triage-<date>.md"
loopGuard: "If a unibox-triage file for today already exists, stop."
---

# Merraine reply triage

# Overview
Read overnight threads. Classify. Draft. Do not send. Exit on reply — the human owns the conversation from the first response.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine reply triage".

Trigger: Weekdays at 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a unibox-triage file for today already exists, stop.

1. If Gmail is not connected and Gojiberry is not connected, stop and name the blocker.
2. Read merraine/playbooks/replies.
3. Classify each open thread. Quote the prospect.
4. Draft replies only for interested, question, and objection.
5. Write unibox-triage-<date>.md. Interested rows go to qualification the same morning.
6. Do not continue a thread that said stop.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
