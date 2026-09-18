# Worker A Jev receipts

These receipts use synthetic, public-safe design descriptions only. Jev judged
evidence quality and fixture safety; it did not authorize contact, override
`doNotContact`, or make any approval decision.

- `worker-a-warm-path-contract.json` evaluates whether a URL alone or a URL
  plus observation date is the minimum public evidence contract. It selected
  `url_plus_observed_at` (0.54, although confidence was only 0.08). I changed
  `gtm.warm-path` to require `observedAt`, updated the organization-map
  runbook, and added the missing-date negative fixture. The low confidence
  means a date is a freshness floor, not proof that a route remains legitimate;
  `pathKind`, source reopening, and human approval remain separate controls.
- `worker-a-citation-gate.json` tests the universal-search rule that an
  unresolvable cited source cannot be used as a factual finding. It returned
  0.03 for usability, passing the at-most-0.10 deterministic gate. The result
  confirms the existing drop-on-unresolvable-source runbook rule; no weaker
  exception was added.
- `worker-a-negative-fixtures.json` independently evaluates all eight bad
  synthetic fixture categories as unsafe. Every unsafe probability cleared the
  0.60 gate (0.83–0.97), including missing warm-path evidence and date,
  suppression bypass, malformed evidence, duplicate observations, approval
  bypass, an unverifiable hash, and an invalid award conflict.
- `worker-a-negative-control.json` is the labeled negative control: a design
  where a favorable model score authorizes contact despite possible suppression.
  Its 0.24 safety probability fails the conservative at-most-0.10 gate, so the
  receipt's deterministic outcome is `fail`: the bad design is rejected. The
  same receipt gives the separate human/code authority control 0.95. No
  approval field was added to `gtm.warm-path`; approval and suppression remain
  human/code decisions outside Jev.
