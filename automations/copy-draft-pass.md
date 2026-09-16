---
type: gtm.automation
tldr: Draft A/B notes for keepers who cleared the cut
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS copy module, stood up as a Disabled Opulent automation"
slug: merraine-copy-draft
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
costCeilingUsd: 3
producesArtifact: "copy-pack-<date>.md"
loopGuard: "If a copy-pack file for today already exists, stop."
---

# Merraine copy-draft pass

# Overview
Write one cited note per keeper who cleared the cut. Then run
[[slop-patterns]]. Do not send.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine copy-draft pass".

Trigger: Weekdays at 7:20 AM America/Chicago, after the intent ranking exists.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a copy-pack file for today already exists, stop.

1. If intent-ranking for today does not exist, stop and say so.
2. Read merraine/playbooks/copy, merraine/research/jeremy-voice, and merraine/research/slop-patterns.
3. For each keeper at or above the cut, write Draft A and a sharper Draft B from the same facts.
4. First sentence quotes the cited event. One question. Permission to pass.
5. 80 words for a signal opener, 60 for congratulations. Label a note role-only when it cannot be personalised without inventing.
6. Run the slop test. Two trips means rewrite before the pack is written.
7. Write copy-pack-<date>.md. Every note carries sendReady: no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not invent a post, a quote, or a personal detail
