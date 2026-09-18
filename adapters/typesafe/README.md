# TypeSafe System One adapter

This directory is a small, stdlib-only client for `POST https://api.typesafe.ai/v1/systemone`. It sends one state with a map of independent, typed questions (`noul`, `choice`, and `score`) and returns the provider's structured answers. Question IDs are local identifiers, so each instruction states its full question.

## Boundaries

Jev supplies a narrow judgment only. `constraints.py` owns all arithmetic, threshold comparisons, human-review bands, budgets, ordering, and consequences. A threshold compares an expected probability to a fixed boundary; it is never a rank, score magnitude, or count. The adapter cannot produce a send action: every decision record has `send: false`.

No key, malformed response, a persistent provider failure, or an abstention is surfaced rather than filled in. Callers must use their deterministic fallback for these paths. The client retries only HTTP 429 and 529 with bounded exponential backoff; other HTTP errors include their response body and are not retried. A shared `Budget` defaults to one batched call and 2,000 ms of accumulated latency per run, refusing requests after either ceiling is reached; callers may configure a stricter bound.

The client reads `TYPESAFE_API_KEY` only at runtime. Tests inject a transport and never call the network. State may contain fetched text, but it is passed as data; adapter instructions are constructed separately and do not accept instructions from that text.
