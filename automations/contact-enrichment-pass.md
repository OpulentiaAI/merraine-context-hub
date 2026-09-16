---
type: gtm.automation
tldr: Fill missing contact fields on last night's keepers
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS enrichment module, stood up as a Disabled Opulent automation"
slug: merraine-contact-enrichment
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
costCeilingUsd: 4
producesArtifact: "enrichment-<date>.md"
loopGuard: "If an enrichment file for today already exists, stop."
---

# Merraine contact-enrichment pass

# Overview
Fill missing emails, phones, and LinkedIn URLs on researched keepers.
Leave a field blank when the tool misses. Never invent an address.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine contact-enrichment pass".

Trigger: Weekdays at 7:10 AM America/Chicago, after account research exists.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an enrichment file for today already exists, stop.

1. Read merraine/playbooks/enrichment and the latest account-research artifact.
2. If that artifact does not exist, stop and say so.
3. For each keeper, list missing email, phone, LinkedIn, title history.
4. Enrich from connected tools only. Record source and spend per field.
5. If a field does not come back, write [NEED: email] (or the missing field). Never pattern-guess firstname.lastname@company.com.
6. Collapse duplicate people to one row.
7. Write enrichment-<date>.md. Do not score. Do not write copy.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not invent an email, phone, or LinkedIn URL
