---
type: gtm.automation
tldr: Routine healthcheck
status: draft
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "Pattern from x.ai dr-eggbot-v2; cost lens from Clay's 350m-agents-a-month talk"
slug: merraine-routine-healthcheck
uses: []
schedule:
  kind: cron
  expression: "49 8 * * 1"
  timezone: America/Chicago
  source: opulent-native
mode: read-only
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 3
producesArtifact: "routine-audit-<date>.md"
sourceTemplate: "dr-eggbot-v2 routine-healthcheck"
loopGuard: "If this week's audit exists, stop. Silent when nothing to propose."
---

# Routine healthcheck

## Overview

Weekly waste audit over every automation on the account. Catches the automation that
fires daily and finds nothing, the one whose tool calls doubled, and the one nobody
has read the output of in three weeks.

## Prompt

```text
Create an Opulent automation named "Merraine routine healthcheck".

Trigger: weekly, Monday 8:49 AM America/Chicago.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Audit every automation on this account for cost and waste. Propose changes. Apply nothing.

IMPORTANT: If this week's routine audit already exists, stop. If nothing is worth proposing, end quietly.

1. List every automation on this account with its schedule, last 7 fires, and spend per fire.
2. For each, compute: fires, fires that produced an artifact, fires that produced nothing, total spend, spend per produced artifact.
3. Flag, with numbers attached:
   - automations whose empty-fire rate is above 70 percent - these should be event-triggered via Parallel, not scheduled
   - automations whose spend per artifact rose more than 50 percent week over week
   - automations whose artifacts nobody opened
   - two automations producing overlapping artifacts
   - any automation still enabled: no after 7 days, which means a first-open never passed
4. For each flag write a gtm.improvement with decision: proposed. Prefer rerouting to an event trigger over deleting.
5. Check tool-call counts per run. Bounding tool calls improves quality as well as cost; an unbounded loop is a correctness risk, not just a bill.
6. Write "routine-audit-<date>.md". Change no schedule, pause nothing, delete nothing.

CAUTION: Propose only. Never pause, enable, or delete an automation. Never claim a saving you did not compute from real spend numbers.
```

## Forbidden Actions

- Do not pause or delete any automation
- Do not change a schedule
- Do not estimate savings without real spend figures
