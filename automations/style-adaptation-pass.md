---
type: gtm.automation
tldr: Restyle today's pack without changing claims
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published marketing-team agent playbook. Claimed numbers stay the author's."
slug: merraine-style-adapt
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
producesArtifact: "style-pass-<date>.md"
loopGuard: "If a style-pass file for this pack already exists, stop."
---

# Merraine style-adaptation pass

# Overview
Restyle the copy pack in Jeremy's voice. Keep every claim. Show before and after.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine style-adaptation pass".

Trigger: Weekdays at 7:40 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a style-pass file for this pack already exists, stop.

1. If copy-pack for today does not exist, stop and say so.
2. Read merraine/playbooks/style, merraine/research/jeremy-voice, and merraine/research/slop-patterns.
3. Restyle each note for its channel. Do not add a fact.
4. Run the slop test. Two trips means rewrite.
5. Write style-pass-<date>.md with before → after for lines that moved.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
