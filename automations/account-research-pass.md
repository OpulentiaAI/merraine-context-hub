---
type: gtm.automation
tldr: One angle per Keep row
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-account-research module, stood up as a Disabled Opulent automation"
slug: merraine-account-research
uses:
  - "[[spear]]"
  - "[[parallel]]"
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
producesArtifact: "account-research-<date>.md"
loopGuard: "If an account-research file for today already exists, stop."
---

# Merraine account-research pass

# Overview
Research today's Keep rows. One angle each. No copy.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine account-research pass".

Trigger: Weekdays at 7:00 AM America/Chicago, after the ICP filter on the digest.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an account-research file for today already exists, stop.

1. Take only Keep rows from today's digest. Skip Drops and Maybes.
2. For each, follow merraine/playbooks/research. Primary sources only.
3. Run the delete-the-name test on every angle.
4. Write account-research-<date>.md. Do not draft outreach here.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
