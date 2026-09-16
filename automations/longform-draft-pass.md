---
type: gtm.automation
tldr: Draft the long version of today's claim
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-longform-draft
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
producesArtifact: "longform-<date>.md"
loopGuard: "If a longform file for today already exists, stop."
---

# Merraine long-form draft pass

# Overview
Write the page a thread can be cut from. Hold it. Do not publish.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine long-form draft pass".

Trigger: Weekdays at 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a longform file for today already exists, stop.

1. Read merraine/playbooks/longform and merraine/entities/jeremy-writing-prefs.
2. If no settled claim exists in today's copy pack, stop and say so.
3. Write hook, stakes, payoff, one next step. Leave uncited proof as [NEED].
4. Run slop. Write longform-<date>.md. sendReady stays no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
