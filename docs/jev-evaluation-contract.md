# Jev evaluation contract

How this repository uses [TypeSafe](https://typesafe.ai) Jev, and what a claim of
"we evaluated this" has to carry to be checkable.

## The rule

**Jev judges. Code decides.** The model returns typed judgments with
probabilities. Thresholds, ordering, counts, consequences and routing are code.
Any design in which the model produces the final ordering, number, or action is
wrong by construction.

**A decision is only evidence when it carries a receipt.** "We used Jev" is not
a claim anyone can check. A receipt records the request that produced the answer,
the probabilities that were stated *before* the outcome, and the deterministic
rule code applied afterwards.

**Never claim all work was evaluated without receipts.** No receipt means the
evaluation did not happen as far as this repository is concerned. Missing or
failed evaluations are recorded as `unavailable` — never silently skipped, never
rendered as a pass.

## What Jev may and may not decide

| Jev may judge | Jev may never decide |
|---|---|
| How well evidence supports a claim | Whether we may contact a person |
| Which of several designs is stronger | Whether approval was given |
| Whether a signal is admissible as evidence | Whether suppression or do-not-contact is lifted |
| How confident a categorization is | Anything irreversible: a send, a payment, a publish |

Authority, approval and suppression belong to deterministic code plus an explicit
named human. This is not a preference. An evaluation of exactly this question —
"who must own approval, contact authority and suppression?" — returned
`code_and_named_human` at confidence 1.0, and the control question "is it safe to
convert an abstention into an automatic ordering and proceed?" returned 0.04.

## Running an evaluation

```bash
python3 scripts/jev_evaluate.py \
  --request req.json \
  --rules rules.json \
  --purpose "the decision this resolves" \
  --out evidence/jev-receipts/<name>.json
```

`request.json`:

```json
{
  "questionSetVersion": "merraine.<area>.<name>.v1",
  "state": { "named": "fields only, filtered to what the questions need" },
  "questions": {
    "is_supported": { "type": "noul", "instructions": "…", "criteria": {"true": "…", "false": "…"} },
    "best_design":  { "type": "choice", "instructions": "…", "criteria": {"a": "…", "b": "…"} },
    "strength":     { "type": "score", "instructions": "…", "criteria": ["level 0", "level 1", "level 2"] }
  },
  "model": "jev-latest"
}
```

`rules.json` maps a question id to the deterministic gate applied to its answer:

```json
{ "is_supported": { "threshold": 0.8, "direction": "at_least", "review_band": [0.4, 0.6] } }
```

Auth is the `TYPESAFE_API_KEY` environment variable, read at runtime. It is never
printed, written to a receipt, or committed.

### Writing good questions

The question id is **not** sent to the model, so `instructions` must carry the
full meaning. One dimension per question — never "is this good overall". Score
levels are the rubric, written as concrete observable conditions. Batch
independent questions over one state into a single request; they run in parallel
and cannot see each other's answers. Do not ask the model to count, subtract, or
compare dates — that is code.

### Reading an answer

- `noul` is the probability a condition holds. A value near 0.5 means uncertain,
  not medium intensity.
- `score` and `choice` carry a probability distribution and a confidence.
  Confidence measures how concentrated the distribution is, not correctness.
- The **expected value** (`sum(p × points)`) is for comparing against a threshold
  only. It is never interpolated into a magnitude.

## Abstention, unavailability, and the review band

| Situation | Handling |
|---|---|
| Provider abstains | Fall back to the deterministic rubric, keep the probability as weak signal, route to a human. **Never re-read an abstention as an ordering.** |
| Provider unavailable / no key | Mark the affected rows `unavailable`, let the deterministic rubric answer, and say so in the output. Never fabricate a judgment. Never silently drop a gate. |
| Probability inside the review band (default 0.4–0.6) | Route to human review with the underlying probability still visible. This is an escalation, not a verdict. |

Rate limits (`429`, `529`) are retried with bounded exponential backoff. Other
non-2xx statuses carry the provider's error body; read it, do not retry blindly.

## Privacy

- Send the **minimum redacted operational context**. Synthetic or scrubbed state
  only.
- Never send conversation prose, contact records, or any customer payload to the
  evaluator.
- Never copy question sets, thresholds, or decision records out of a private
  repository. Author your own.
- Receipts live under `evidence/jev-receipts/` and carry a **synthetic or redacted**
  request, deterministic rules, provider response, input hash, question ids and
  types, answers, and deterministic outcome. They carry **no keys and no private
  payload prose** — a public receipt is reproducible because its input is safe to publish.

## Receipt shape

```json
{
  "schemaVersion": "1.0",
  "purpose": "the decision this resolves",
  "model": "jev-1.13.0",
  "inputHash": "sha256:…",
  "inputSummary": { "questionIds": ["…"], "questionTypes": { "…": "noul" },
                    "stateKeys": ["…"], "questionSetVersion": "…" },
  "request": { "synthetic": "public-safe input" },
  "rules": { "is_supported": { "threshold": 0.8, "direction": "at_least" } },
  "response": { "synthetic": "provider response" },
  "answers": [ { "question_id": "…", "type": "noul", "value": 0.9 } ],
  "deterministicDecision": { "outcome": "pass", "components": [ … ] },
  "usage": { "input_tokens": 0, "output_tokens": 0 }
}
```

`request` plus `inputHash` makes the input reproducible. `rules` and `response`
make the deterministic result reviewable. `answers` records what was stated.
`deterministicDecision` records what code did about it. An unavailable receipt
uses `response: null`, preserves the request and rules, and records `unavailable`;
a receipt missing any of those contract fields is not a receipt.

## Negative controls

Every question set that gates something carries a labeled negative control: a
deliberately bad input with an expected verdict. A gate nobody has watched
reject a known-bad input is a gate nobody should trust. Re-run the control after
any change to the gate or its thresholds.

## Adding a receipt

1. Write the request and rules as files next to the receipt.
2. Run the harness. Read the deterministic outcome it prints.
3. If the outcome contradicts your design, **the contradiction is the finding** —
   fix the design, or record why the threshold is wrong. Do not adjust the
   receipt.
4. Commit the receipt and a one-line entry in `evidence/jev-receipts/README.md`
   naming the decision it informed and what changed as a result.
