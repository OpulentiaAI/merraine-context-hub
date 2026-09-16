---
type: gtm.automation
tldr: Draft held social versions of today's claim
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-social-queue
uses:
  - "[[notion]]"
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
producesArtifact: "queue-pack-<date>.md"
loopGuard: "If a queue-pack file for today already exists, stop."
---

# Merraine social-queue draft

# Overview
Read what is connected. Draft for the default surfaces. Propose a time. Do not set it.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine social-queue draft".

Trigger: Weekdays at 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a queue-pack file for today already exists, stop.

1. Read merraine/playbooks/social-queue and merraine/entities/jeremy-writing-prefs.
2. List connected surfaces. If none, say so and still write LinkedIn plus email drafts.
3. Adapt the same claim per surface. Do not invent handles or stats.
4. Write queue-pack-<date>.md with a proposed time. sendReady stays no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
- Do not schedule or publish
