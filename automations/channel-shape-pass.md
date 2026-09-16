---
type: gtm.automation
tldr: Rewrite today's pack for each channel fold
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published marketing-team agent playbook. Claimed numbers stay the author's."
slug: merraine-channel-shape
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
producesArtifact: "channel-shape-<date>.md"
loopGuard: "If a channel-shape file for today already exists, stop."
---

# Merraine channel-shape pass

# Overview
Rewrite each settled note for the channel it will travel. Claim stays.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine channel-shape pass".

Trigger: Weekdays at 7:40 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a channel-shape file for today already exists, stop.

1. If copy-pack for today does not exist, stop and say so.
2. Read merraine/playbooks/channels, merraine/entities/channel-email, and merraine/entities/channel-linkedin.
3. For each keeper, rewrite to that channel's first fold.
4. If the channel is not connected, say so and leave the row blocked.
5. Write channel-shape-<date>.md. sendReady stays no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
