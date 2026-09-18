# Completeness and source coverage

**Completeness is manifest-based.** A claim that this hub covers Jeremy's account
must name the `gtm.source-manifest` row that supports it. A source that is
connected but has no row is an explicit gap. It is never an implicit zero.

This document exists because the most dangerous state of this hub is a hub that
looks complete. Early on, one source was extracted successfully and the word
"done" started doing work it had not earned.

## The rule

1. **One row per source of truth** in the manifest, keyed by `sourceId`.
2. **`state` is honest.** `pending` is the default and is not a failure:
   it means reachable and not yet pulled. `unavailable` and `blocked` carry a
   verbatim `blockerNote`. Silence is never used to mean "nothing there".
3. **`doesNotCover` is required and is the important half.** A prospect corpus
   does not cover a mailbox, a voice, or a history. Writing that down is what
   stops one source from standing in for the account.
4. **A completed extraction is proof of that source only.** A finished run —
   even a large one, even one whose artifact is present and hashed — is not
   evidence about any other source, and is not evidence that the account is
   covered.
5. **Coverage never regresses silently.** A source whose row says `extracted`
   and whose material is gone becomes `pending` with a blocker note, not an
   assumption that it is still there.
6. **Delta runs never close a source.** A `delta` scope run records what arrived
   since the previous run. Only a `full` run may move `state` to `extracted`.

## Do not re-extract is not the same as done

The hub carries standing decisions not to repeat an extraction — re-running one
duplicates material and burns spend. That decision is about **not wasting a run**.
It is not a statement that the account is covered.

| Phrase | What it actually means |
|---|---|
| "Do not extract X again" | X already landed. Re-running it is waste. |
| "X is extracted" | The manifest row for X says `extracted`. |
| "The account is covered" | **Only** claimable when every connected source has a row that is not `pending`, or names its blocker. |

## Privacy split

The manifest row is public. The extracted material is not.

| Class | May be committed here | Example |
|---|---|---|
| Manifest row | yes | `sourceId`, `state`, `covers`, `doesNotCover`, `artifactRef` by name |
| Artifact reference | yes — **name and hash only** | `personal-context-hub.zip`, `artifactSha256` |
| Extracted content | **no** | prospects, contacts, mail, transcripts, identifiers |

A `privacy: private` row means everything the row produced stays out of this
repository. Names and hashes may appear; content never does. No raw mailbox, no
contact list, no chat history, no transcript text.

## How to add a source

1. Read live state. Do not reason from memory about what is connected.
2. Add the manifest row before extracting anything. `state: pending` is correct
   and honest at this point.
3. Extract through the source's runbook, or author one under `gtm.extraction`.
4. Record a `gtm.extraction-run` with counts and a recomputed hash.
5. Only then move `state` to `extracted`, with `lastObservedAt` set to the date
   you actually observed it.

Run `python3 scripts/validate.py` before committing. It enforces that every
connected source has a manifest row, that a terminal state carries the fields
that state requires, and that a `non-ok` run names its gap.
