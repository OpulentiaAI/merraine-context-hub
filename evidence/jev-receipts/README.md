# Jev evaluation receipts

Every receipt in this directory records a public-safe, synthetic request, typed provider answers, probabilities before the deterministic outcome, and the rule outcome. It contains no contacts, customer history, secrets, or private decision-layer material.

- `typesafe-adapter-safety.json` evaluates the TypeSafe adapter's unavailable and abstention fallback, 0.45–0.55 human-review band, one-call/2,000 ms default budget, fixed no-send authority, and a labeled unsafe negative control. The receipt informed an adapter change: `Budget` now defaults to the evaluated one-call and 2,000 ms ceiling. The unsafe control was detected at 0.97 and is rejected by the documented policy; it is not an adapter behavior.
