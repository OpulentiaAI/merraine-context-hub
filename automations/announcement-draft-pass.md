---
type: gtm.automation
tldr: Draft the public note for a real change
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
slug: merraine-announcement-draft
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
producesArtifact: "announcement-<date>.md"
loopGuard: "If an announcement file for this change already exists, stop."
---

# Merraine announcement draft pass

# Overview
Write the public note for a change that actually happened. Hold it. Do not publish.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine announcement draft pass".

Trigger: Weekdays at 8:20 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an announcement file for this change already exists, stop.

1. Read merraine/playbooks/announcement and merraine/entities/channel-announcement.
2. If there is no real change, stop and say so. Do not fill a slot.
3. Public note: what changed, who it affects, what to do, where to read more.
4. Versioned record: newest first, dated, Breaking / New / Improved / Fixed only.
5. Leave unnamed placements as [NEED]. Write announcement-<date>.md. sendReady stays no.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
- Do not invent a change to fill a slot
