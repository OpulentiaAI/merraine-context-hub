---
type: gtm.automation
tldr: Merraine awards and recognition monitor
status: draft
owner: Opulent
updated: 2026-09-14
provenance: "Jeremy Sanchez ask item 6, 2026-09-11"
slug: merraine-awards-monitor
uses:
  - [[parallel]]
  - [[gmail]]
schedule:
  kind: cron
  expression: "0 7 * * 1"
  timezone: America/Chicago
  source: parallel-monitor
mode: draft-then-wait
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 5
producesArtifact: "recognition-digest-<date>.md"
sourceTemplate: "none - authored for this engagement"
loopGuard: "If this week's recognition digest already exists, stop."
---

# Merraine awards and recognition monitor

## Overview

His words: *"Award winners are warm intros waiting to happen."* A named
congratulations is the only cold opener that is genuinely welcome.

## What's Needed From User

- [[parallel]] (already installed, scope `monitor.event.detected`)
- Confirmation of which regional journals matter beyond Chicago and New York

## Procedure

Stand up per [[first-open-gate]]. Prefer Parallel monitors over polling — see
[[parallel-monitor-scheduling]].

## Specifications

- Every honoree traces to a publisher URL with a publication date
- Social posts are never a source
- Zero sends

## Prompt

```text
Create an Opulent automation named "Merraine awards and recognition monitor".

Trigger: weekly, Monday 7:00 AM America/Chicago.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Find newly announced award and list recognitions for companies and executives in Merraine's ICP, and leave a congratulations opener waiting for approval.

IMPORTANT: If this week's recognition digest already exists in this workspace, stop.

1. Read merraine/entities/merraine-icp and merraine/signals/award-recognition.
2. Cover the past 7 days across these publishers only: Forbes lists, Crain's Chicago Business (40 Under 40, Fast 50, Notable lists, Best Places to Work), Crain's New York Business, Chicago Business Journal, New York Business Journal, Inc. 5000, and any industry list named in the ICP file.
3. Keep only honorees whose company matches ICP geography and size.
4. Record: honoree name, company, list name, publisher URL, publication date.
5. Drop anything without a resolvable publisher URL. Never infer an award from a social post or a congratulatory comment.
6. Verify the honoree still works where the list says. List pages lag job changes. If the listing and their current role disagree, keep the row and mark it conflict; do not resolve it by guessing.
7. Enrich the honoree, or the company's CEO or CHRO, with Monid first and Crustdata as fallback. Leave blanks when both miss. Record spend.
8. Draft one opener per row, under 60 words: congratulate on the specific recognition by name, one sentence on what Merraine notices about companies at that moment, one question, and permission to pass.
9. Run merraine/research/slop-patterns on every draft. Rewrite on two trips.
10. Write "recognition-digest-<date>.md" with every draft send_ready: false and a per-row approval checkbox. Log counts, spend, and the artifact hash.

CAUTION: Never send. Never invent an award, an honoree, or a quote. A quiet week is UNVERIFIED, not "no awards".
```

## Forbidden Actions

- Do not treat a pay-to-play award as a signal
- Do not congratulate someone on a prior-year list re-run
- Do not send
