---
type: gtm.automation
tldr: Keep the source manifest honest against live discovery
status: draft
owner: Jeremy Sanchez
updated: 2026-09-18
surface: jeremy
provenance: "Completeness guardrail: one extraction is not source coverage"
slug: merraine-source-manifest-review
uses:
  - "[[mesa]]"
schedule:
  tldr: weekly cron
  kind: cron
  expression: "0 8 * * 1"
  timezone: America/Chicago
  source: opulent-native
mode: read-only
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 1
producesArtifact: "source-manifest-review-<date>.md"
sourceTemplate: "none - authored for this engagement"
loopGuard: "If a source manifest review for this date already exists, stop."
---

# Source manifest review

# Overview
The manifest is the coverage ledger. A manifest that has drifted from live
discovery is worse than no manifest, because it reads as complete.

This job re-reads live state, compares it to the source manifest, and reports
the difference. It repairs nothing and extracts nothing: a manifest that edits
itself is a manifest nobody checked.

# What's Needed From User
- Nothing. Read-only. It never extracts, sends, or spends past its ceiling.

# Procedure
1. Read `entities/source-manifest.md` and the live connection inventory.
2. Diff the two in both directions.
3. Report and stop. Repairs are a human decision, made in the thread.

# Prompt
```text
Create an Opulent automation named "Merraine source manifest review".

Trigger: weekly, Monday 8:00 AM America/Chicago.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Check whether the source manifest still matches what is actually connected.

IMPORTANT: If a source manifest review for this date already exists in this workspace, stop.

1. Read merraine/entities/source-manifest and merraine/entities/connection-inventory.
2. Read live connected capabilities for this account. Do not reason from memory.
3. Report two diffs, both needed:
   - connected now but absent from the manifest, or whose row state disagrees
   - manifest rows marked extracted, unavailable or blocked that live state contradicts
4. For every row still pending, unavailable, or blocked, quote its blocker note verbatim. If a row has no note, that is the finding.
5. For every row marked extracted, check that it names a run, a date observed, and a recomputed hash. A row missing any of the three is reported as unproved.
6. Write "source-manifest-review-<date>.md": one row per source with sourceId, manifest state, live state, and the drift or "agrees". End with a coverage line: how many connected sources are covered, and which are not.
7. Log: rows compared, drifts found, rows still unproved.

CAUTION: Never extract, never materialize, never enable an automation, never send. Never mark a source covered on the strength of a different source's extraction. If live discovery fails, say so and report nothing as agreeing.
```

# Forbidden Actions
- Do not extract, re-extract, or re-auth any source
- Do not edit the manifest; report the drift and stop
- Do not treat one source's presence as coverage of another
- Do not Enable this clock before a first open Jeremy checked
