---
type: gtm.automation
tldr: Fill gaps in today's drafts from the open web
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-public-facts
uses:
  - "[[parallel]]"
  - "[[notion]]"
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
producesArtifact: "facts-<date>.md"
loopGuard: "If a facts file for this pack already exists, stop."
---

# Merraine public-fact check

# Overview
Answer only the questions the drafts marked [NEED] that a public source can fill.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine public-fact check".

Trigger: Weekdays at 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a facts file for this pack already exists, stop.

1. Read today's drafts for [NEED] lines that a public page could fill.
2. Read merraine/playbooks/facts.
3. For each question, search, read the page, and cite the URL. Unverified goes in Gaps.
4. Write facts-<date>.md. Do not edit the drafts.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
