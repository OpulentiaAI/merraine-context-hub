---
type: gtm.automation
tldr: Rewrite any waiting draft that trips slop
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS slop-patterns module, stood up as a Disabled Opulent automation"
slug: merraine-slop-rewrite
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
costCeilingUsd: 1
producesArtifact: "slop-pass-<date>.md"
loopGuard: "If a slop-pass file for this pack already exists, stop."
---

# Merraine slop-rewrite pass

# Overview
Run [[slop-patterns]] on every draft in today's copy pack. Two trips means
rewrite. Fail closed.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine slop-rewrite pass".

Trigger: Weekdays at 7:30 AM America/Chicago, after the copy pack exists.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a slop-pass file for this pack already exists, stop.

1. If copy-pack for today does not exist, stop and say so.
2. Read merraine/playbooks/slop and merraine/research/slop-patterns.
3. For each note, mark instant fails and soft fails.
4. Rewrite any note with two or more trips until it sounds like Jeremy, not a sequence.
5. Write slop-pass-<date>.md with pass / fail / rewritten, and the trips named.
6. Do not mark sendReady yes. Do not send.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not pass a draft that still trips twice
