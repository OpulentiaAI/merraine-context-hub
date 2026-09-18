# Jev evaluation receipts

Every receipt in this directory records a public-safe, synthetic request, the
typed provider answers, the probabilities stated *before* any outcome, and the
deterministic rule code applied afterwards. No receipt contains contacts,
customer history, secrets, credentials, or private decision-layer material.

A receipt is what makes an evaluation checkable. "Jev was used" is not a claim
anyone can verify; a receipt is. See `docs/jev-evaluation-contract.md` for the
contract these follow, and note the boundary they all respect: **Jev judges
evidence quality. It never decides approval, contact authority, or suppression.**

---

## Integration review (scripts/jev_evaluate.py)

- `completeness-guardrail.json` — whether the completeness guardrail ships as
  warn-then-error or a hard error. Design A was preferred at **0.98**, but its
  adoptability scored **0.77** (below the 0.8 gate) and its resistance to a
  deleted manifest only **0.70**. **Change made:** the coverage warning is now
  test-enforced, so removing the manifest cannot silently silence the rule.
- `warm-path-evidence.json` — is one `evidenceUrl` sufficient for a legitimate
  warm path? URL alone **0.12**, URL plus observation date **0.22**, with
  URL-plus-date preferred at confidence 0.95. **Change made:** the finding went
  to the ontology owner and `observedAt` is now required, so a dateless route is
  not usable.
- `abstention-policy.json` — turning an abstention into an automatic ordering
  scored **0.04** (unsafe); disclosed deterministic fallback scored **0.90**;
  and "who owns approval, contact authority and suppression?" returned
  `code_and_named_human` at confidence **1.0**. **Change made:** confirms the
  no-authority-from-score boundary and the fail-closed abstention handling.
- `negative-control.json` — a deliberately unsafe proposal (pattern-guessed
  emails, score-triggered autonomous send, silence read as failure).
  `invents_contact_data` **0.98**, `autonomous_send` **0.96**,
  `misreads_silence` **0.97**, `should_adopt` **0.02**. The control is
  correctly rejected.

## Ontology and runbooks (worker A)

Synthetic, public-safe design descriptions only. Jev judged evidence quality and
fixture safety; it did not authorize contact, override `doNotContact`, or make
any approval decision.

- `worker-a-warm-path-contract.json` — URL alone versus URL plus observation
  date. Selected `url_plus_observed_at` (**0.54**, though confidence was only
  **0.08**). **Change made:** `gtm.warm-path` requires `observedAt`, the
  org-map runbook requires URL plus date, and a missing-date negative fixture
  makes the absence rejectable. The low confidence is the honest caveat: a date
  is a freshness floor, not proof a route is still legitimate.
- `worker-a-citation-gate.json` — can an unresolvable cited source be used as a
  finding? **0.03**, passing the at-most-0.10 gate. **Change made:** none
  needed; it confirms the existing drop-on-unresolvable-source rule.
- `worker-a-negative-fixtures.json` — all eight bad fixture classes evaluated as
  unsafe, clearing the 0.60 gate at **0.83–0.97**.
- `worker-a-negative-control.json` — a design where a favorable score authorizes
  contact despite possible suppression. Safety probability **0.24** fails the
  conservative at-most-0.10 gate, so the outcome is `fail`: the design is
  rejected. The separate human/code authority control scored **0.95**. No
  approval field was added to `gtm.warm-path`.

## TypeSafe adapter (worker B)

- `typesafe-adapter-safety.json` — unavailable and abstention fallback,
  0.45–0.55 human-review band, one-call/2,000 ms budget, fixed no-send
  authority, and a labeled unsafe control. Disclosed fallback **0.94**, visible
  review band **0.96**, budget **0.90**, unsafe control detected **0.97**,
  code-and-named-human authority **0.94**. **Change made:** `Budget` now
  defaults to the evaluated fail-closed one-call / 2,000 ms ceiling rather than
  leaving it caller-configurable, and `Decision.send` became
  non-initializable so even direct construction cannot set a send action.

---

## Reading a receipt

| Field | What it tells you |
|---|---|
| `inputHash` | The exact request, reproducible |
| `inputSummary.questionIds` / `questionTypes` | What was asked, and in what shape |
| `answers` | What the provider stated, before any outcome was known |
| `deterministicDecision` | What code did about it, and under which rule |
| `usage` | Extractable cost of the call |

A receipt missing either half — the stated probabilities or the deterministic
outcome — is not a receipt.

## Adding one

1. Author the request and rules; keep them public-safe and synthetic.
2. Run `python3 scripts/jev_evaluate.py --request … --rules … --purpose … --out …`.
3. If the outcome contradicts the design, the contradiction is the finding. Fix
   the design, or record why the threshold is wrong. Never adjust the receipt.
4. Add a bullet here naming the decision informed and what changed.
