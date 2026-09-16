---
type: gtm.automation
tldr: Fresh-eyes verdict on today's pack
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-fresh-review
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
producesArtifact: "review-<date>.md"
loopGuard: "If a review file for this pack already exists, stop."
---

# Merraine fresh-review pass

# Overview
Judge the finished drafts. Verdict only. Do not rewrite.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine fresh-review pass".

Trigger: Weekdays at 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a review file for this pack already exists, stop.

1. If copy-pack or queue-pack for today does not exist, stop and say so.
2. Read merraine/playbooks/review.
3. For each draft, verdict ready or revise with quote, rule, and fix.
4. Write review-<date>.md. When torn, choose revise.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
