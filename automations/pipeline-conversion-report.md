---
type: gtm.automation
tldr: What converted, with enough n
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS merraine-pipeline-report module, stood up as a Disabled Opulent automation"
slug: merraine-pipeline-report
uses:
  - "[[spear]]"
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
producesArtifact: "pipeline-report-<date>.md"
loopGuard: "If a pipeline-report file for this week already exists, stop."
---

# Merraine pipeline conversion report

# Overview
Weekly honesty pass on which signals and notes converted. Directional below n=30.

Stand up per [[first-open-gate]]. Create Disabled. One manual tick before
any clock.

# Prompt
```text
Create an Opulent automation named "Merraine pipeline conversion report".

Trigger: Fridays at 4:00 PM America/Chicago.

When the automation runs, start a session with the prompt below.

IMPORTANT: If a pipeline-report file for this week already exists, stop.

1. Read merraine/playbooks/pipeline and merraine/pipelines/merraine-pipeline.
2. Use volume that exists. Say when n is too small to pick a winner.
3. Rank slices by interested/contacted, not by contacted volume.
4. Write pipeline-report-<date>.md. Propose targeting changes. Do not apply them.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a quote, or a score part. If a tool returns nothing, say nothing was found. sendReady stays no.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not Enable the clock before a first-open Jeremy opened
- Do not fill a `[NEED]` with a guess
