---
type: gtm.automation
title: Hub self-extension
status: draft
owner: Opulent
updated: 2026-09-14
provenance: "Requested: autonomous additions to the hub as new knowledge arrives"
slug: merraine-hub-self-extension
uses: []
schedule:
  kind: event
  expression: "accepted gtm.improvement, or a completed extraction"
  timezone: America/Chicago
  source: opulent-native
mode: draft-then-wait
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 5
producesArtifact: "hub-patch-<date>.md"
sourceTemplate: "none"
loopGuard: "Never triggered by its own patch artifact."
---

# Hub self-extension

## Overview

Closes the loop. When a healthcheck proposal is **accepted**, or an extraction lands
new entities, this turns that into an actual hub change — as a reviewable patch,
never a silent edit.

This is the difference between an automation library and a system that learns. The
argument for it, from Ramp's GTM Coworker: *"the real unlock is encoding
institutional knowledge that used to live in reps' heads and making it computable.
Every run compounds it. Every human correction teaches the system."*

## Prompt

```text
Create an Opulent automation named "Merraine hub self-extension".

Trigger: when a gtm.improvement is marked accepted, or an extraction receipt is written.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Turn accepted improvements and new extraction output into a reviewable patch against the Merraine context hub.

IMPORTANT: Never trigger on your own patch artifact. If the only new input is a hub-patch file, stop.

1. Collect every gtm.improvement with decision: accepted that has not been applied, and every extraction receipt written since the last patch.
2. For each, write the exact change: the target file, the current text, and the replacement text. Whole-file rewrites are not a patch; show the specific edit.
3. New entities from an extraction become new instance files typed against merraine/types. Fill every required field or mark it [NEED: x]. Never invent a field value to satisfy a type.
4. Respect the ontology. A company is gtm.org, a person is gtm.person, an observed trigger is gtm.observation pointing at an existing gtm.signal. If something does not fit an existing type, propose the new type rather than forcing the shape.
5. Every new factual claim carries a gtm.evidence row with a resolvable source. Claims without one are written as UNVERIFIED, not dropped and not asserted.
6. Write "hub-patch-<date>.md" containing the full diff and a one-line rationale per change. Mark each gtm.improvement applied only after a human confirms the patch landed.
7. Do not edit hub files directly. The patch is the deliverable.

CAUTION: Propose the patch, do not apply it. Never invent a field value. Never widen a type to make bad data fit.
```

## Forbidden Actions

- Do not edit hub files in place
- Do not mark an improvement applied before the patch is confirmed
- Do not create a type to accommodate data you have not verified
