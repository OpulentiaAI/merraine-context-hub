---
type: gtm.automation
tldr: Report only real social numbers
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-social-digest
uses:
  - "[[notion]]"
  - "[[spear]]"
schedule:
  tldr: monday cron
  kind: cron
  expression: "0 8 * * 1"
  timezone: America/Chicago
  source: opulent-native
mode: read-only
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 2
producesArtifact: "social-digest-<date>.md"
loopGuard: "If a social-digest file for this week already exists, stop."
---

# Merraine weekly social digest

# Overview
Pull follower and post numbers that a connected tool actually returns. Skip the report rather than guess.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine weekly social digest".

Trigger: Mondays at 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a social-digest file for this week already exists, stop.

1. Read merraine/playbooks/social-queue.
2. If no analytics source is connected, write that and stop. Skip rather than guess.
3. Report only returned rows in two tables: followers with change, and per-post engagement with links.
4. Write social-digest-<date>.md. Do not fabricate a number.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
- Do not invent a follower count or an engagement rate
