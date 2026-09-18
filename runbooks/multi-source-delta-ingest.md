---
type: gtm.runbook
tldr: Pull every connected source in, and prove what landed
status: active
owner: Jeremy Sanchez
updated: 2026-09-18
surface: jeremy
provenance: "Completeness guardrail: coverage is manifest-based, not extraction-based"
trigger: "A new source is connected, an extraction is requested, or the manifest shows a pending row"
audience: jeremy-sanchez
escalateWhen:
  - "A source needs an auth click or a paid seat"
  - "A hash does not match after download"
  - "The manifest and live discovery disagree"
relatedAutomations:
  - "[[source-manifest-review]]"
---

# Multi-source delta ingest

Pull every connected source into this hub, and prove what landed. Generic: it
makes no assumption about which tool a source is, only that the manifest knows
it and a runbook exists or can be authored for it.

This is the procedure behind the completeness rule in
`docs/completeness-and-source-coverage.md`. Read that first.

# Procedure

1. **Discover live.** Read what is actually connected right now. Do not reason
   from memory, from a settings page, or from the previous manifest. A stale
   manifest is how a source goes missing without anyone noticing.
2. **Diff against the manifest.** For each connected source, find its
   `sourceId` row. Three outcomes:
   - no row — add one with `state: pending` before doing anything else
   - `state: extracted` — skip, unless the user asked for a refresh
   - `state: pending | unavailable | blocked` — this is the work queue
3. **Order the queue cheapest-first.** A source with an existing runbook and no
   auth click goes before one that needs a human to authorize something.
   Never block the whole ingest on one click; extract what is reachable and say
   what is waiting.
4. **For each source, pick the scope.**
   - `full` — first run, or the user asked for a rebuild
   - `delta` — a prior run exists and the source supports reading only what is
     new. A delta run never closes a source.
5. **Extract through the source's runbook** ([[connected-tool-extraction]] is
   the reference pattern). Route explicitly. Put bulk pulls on a worker and
   keep the coordinator's context for orchestration.
6. **Land the material privately.** Artifacts go to the account's storage, not
   into this repository and not into a chat message.
7. **Prove it.** File count you can list, artifact row count, and a hash you
   recomputed after download. `completed` is never proof.
8. **Record a `gtm.extraction-run`** — scope, counts, artifact ref by name,
   hash, outcome, and every count you could not get.
9. **Update the manifest row last.** `extracted` only on a `full` run that
   proved out. Set `lastObservedAt` to the date observed. Write what the source
   does not cover before you move on, while you still remember.
10. **Report the queue, not just the successes.** Sources still `pending`, still
    `unavailable`, and their blockers are part of the result.

# Verification

- Every connected source has a manifest row. No exceptions, including the ones
  that look obviously empty.
- Every `extracted` row names the run that produced it and the date observed.
- Every artifact ref carries a recomputed hash.
- Every `unavailable` or `blocked` row carries a verbatim blocker note.
- The sum of `recordCount` across runs equals what the manifest implies. If it
  does not, the difference is named, not rounded away.
- No extracted content appears anywhere in this repository.

# Failure branches

| Symptom | Do this |
|---|---|
| A source is connected but has no runbook | Author one under `gtm.extraction` first. Do not improvise a one-off pull. |
| An auth click is required | Mark the row `unavailable` with the click named. Keep extracting the rest. Never forge a session to get past it. |
| A hash does not match after download | Treat the run as `failed`. Do not record it as delivered. |
| Counts are missing | `outcome: partial`, `missing:` names what is unknown. An unknown count is not a zero. |
| A source returns nothing | That is a real result: `recordCount: 0`, `outcome: ok`. Say so plainly and keep the empty result. |
| The manifest and live discovery disagree | Live discovery wins. Fix the manifest and say what drifted. |
| Someone says one big extraction means the account is done | No. Completeness is the manifest, and the manifest is row by row. |
