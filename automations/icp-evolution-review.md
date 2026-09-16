---
type: gtm.automation
tldr: Weekly living-ICP review
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-icp-evolution module, stood up as a Disabled Opulent automation"
slug: merraine-icp-evolution
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
producesArtifact: "icp-evolution-<date>.md"
loopGuard: "If an icp-evolution file for this week already exists, stop."
---

# Merraine ICP evolution review

# Overview
Once a week, open [[icp-context]] against what actually happened and propose fills for `[NEED]` lines. Propose. Never apply.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine ICP evolution review".

Trigger: Mondays at 7:00 AM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If an icp-evolution file for this week already exists, stop.

1. Read merraine/entities/icp-context and merraine/entities/merraine-icp.
2. Read the last seven days of signal-digest and pipeline-report artifacts if they exist.
3. List every [NEED] that a cited artifact can now fill. Quote the artifact.
4. List every Keep row that later proved anti-ICP, with the why.
5. List triggers that converted with n>=30, and triggers that only looked busy.
6. Write icp-evolution-<date>.md with proposed line edits (old → new → reason). Do not edit icp-context.md.
7. Stop. Wait for Jeremy.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
