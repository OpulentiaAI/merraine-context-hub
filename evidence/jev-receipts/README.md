# Jev evaluation receipts

Every committed receipt is a public-safe synthetic evaluation. It contains the
exact request, deterministic rules, provider response, canonical input hash,
normalized answers, and deterministic outcome, so a reviewer can reproduce the
record without seeing a contact, customer payload, credential, or private Jev
material. A receipt is evidence of judgment quality only: it never authorizes a
send, overrides suppression, or replaces named-human approval.

## Integration review

- `receipt-reproducibility.json` — live Jev (`jev-1.13.0`) reviewed the design
  choice between a hash-only claim and a complete synthetic receipt. The
  deterministic result is `pass`: the receipt records request/rules/response
  plus hash and preserves unavailable outcomes. The authority question was
  independently gated, so this evidence cannot grant contact or send authority.

## Reading a receipt

| Field | What it proves |
| --- | --- |
| `request` and `inputHash` | The exact synthetic input and its canonical SHA-256 digest. |
| `rules` | The deterministic gate configuration. |
| `response` and `answers` | What the provider returned before code selected an outcome. |
| `deterministicDecision` | What code did with the response or unavailability. |

Unavailable receipts retain the request and rules, set `response` to `null`, and
record `outcome: unavailable`. They are honest failed evaluations, never a pass.

See `docs/jev-evaluation-contract.md` for the full safety and privacy contract.
