---
type: gtm.automation
tldr: Draft one newsletter issue from cited items
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-newsletter-issue
uses:
  - "[[notion]]"
  - "[[spear]]"
schedule:
  tldr: monday cron
  kind: cron
  expression: "0 9 * * 1"
  timezone: America/Chicago
  source: opulent-native
mode: draft-then-wait
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 2
producesArtifact: "newsletter-<date>.md"
loopGuard: "If a newsletter file for this week already exists, stop."
---

# Merraine newsletter-issue pass

# Overview
One spine. One action. Skip the week if there is nothing to say.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine newsletter-issue pass".

Trigger: Mondays at 9:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a newsletter file for this week already exists, stop.

1. Read merraine/playbooks/newsletter and merraine/entities/email-components.
2. If there is no cited spine, stop and say skip the week.
3. Fill subject, preview, first line, body, one action, plain text.
4. Write newsletter-<date>.md. Do not send. Gmail is not connected.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
- Do not rewrite the daily hiring scan as a newsletter
