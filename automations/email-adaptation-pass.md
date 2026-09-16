---
type: gtm.automation
tldr: Rework today's pack for the inbox
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published marketing-team agent playbook. Claimed numbers stay the author's."
slug: merraine-email-adapt
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
costCeilingUsd: 2
producesArtifact: "email-adapt-<date>.md"
loopGuard: "If an email-adapt file for today already exists, stop."
---

# Merraine email-adaptation pass

# Overview
Take the copy pack and fill [[email-components]] for each keeper whose channel is email. Do not send.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine email-adaptation pass".

Trigger: Weekdays at 7:40 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an email-adapt file for today already exists, stop.

1. If copy-pack for today does not exist, stop and say so.
2. Read merraine/playbooks/email and merraine/entities/email-components.
3. For each keeper on email, decide pointer or whole thing, then fill every component or leave [NEED].
4. Write subject and preview last, as a pair. Write plain text by hand.
5. Note what was cut on purpose. Do not harden a hedge.
6. Write email-adapt-<date>.md. sendReady stays no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
- Do not claim Gmail can send
