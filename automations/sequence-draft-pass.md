---
type: gtm.automation
tldr: Draft a three-step paused sequence
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published marketing-team agent playbook. Claimed numbers stay the author's."
slug: merraine-sequence-draft
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
producesArtifact: "sequence-<date>.md"
loopGuard: "If a sequence file for this pack already exists, stop."
---

# Merraine sequence-draft pass

# Overview
Write the last note first, then the two steps that earn it. Create nothing live.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine sequence-draft pass".

Trigger: Weekdays at 7:40 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a sequence file for this pack already exists, stop.

1. If intent-ranking for today does not exist, stop and say so.
2. Read merraine/playbooks/sequencing.
3. For keepers at or above the cut, write a two- or three-step run. Last note first.
4. Each step: one job, one action, one exit.
5. Write sequence-<date>.md. Campaign stays paused. sendReady stays no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
- Do not enable a Spear campaign
