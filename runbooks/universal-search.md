---
type: gtm.runbook
tldr: Repeatable cited search across LinkedIn, Google, and company sites
status: active
owner: Opulent
updated: 2026-09-18
surface: jeremy
provenance: "Operational procedure authored for the context hub; source results are recorded per run"
trigger: "When a defined research question needs a reproducible, cited result set"
audience: operator
escalateWhen:
  - "A result would be used for outreach or a decision without a reopened source"
  - "A source requires credentials or permission the operator does not have"
  - "The captured artifact cannot be hashed or stored"
relatedAutomations: []
---

# Universal search

Search is a repeatable evidence-gathering operation, not a list-making exercise.
Run it against LinkedIn, Google, and employer-owned company sites; retain only
claims that can be cited from the source itself.

# Procedure
1. State the question and the inclusion, exclusion, geography, date, and title
   constraints before opening a source. Record that exact text as `query`.
2. Search LinkedIn for people and company context, Google for discovery, and the
   company site for confirmation. Prefer a company-owned careers, leadership,
   newsroom, or filing page over a snippet, aggregation, or repost.
3. For each retained row, capture the source URL, the source's own words that
   support the claim, the observation date, and the method used. Create a
   `gtm.evidence` row for each supported factual claim; do not strengthen a
   title, relationship, date, or role by paraphrase.
4. Save the complete raw result set, including dropped rows and source URLs, at
   a repository-relative `artifactPath`. Count only retained rows in
   `resultCount`; a search with no retained evidence is `unverified`, never a
   zero-result claim.
5. Compute SHA-256 from the saved artifact after it is final. Record the
   digest as `artifactSha256`, the capture date as `capturedAt`, every searched
   system in `sources`, and the evidence rows in a `gtm.search-run` instance.
6. Reopen every cited URL before using a row. Mark the run `verified` only when
   its retained evidence is present and reopenable; otherwise mark it
   `unverified`, `incomplete`, or `discarded` and say why.

# Verification
- The artifact exists at `artifactPath`, and a fresh SHA-256 computation equals
  `artifactSha256`.
- Every retained factual claim has a `gtm.evidence` row with claim, observedAt,
  and method.
- Every job posting used as an open role still loads on an employer-owned page;
  search snippets and LinkedIn job pages alone do not confirm it.
- LinkedIn, Google, and company-site coverage is recorded explicitly, including
  a source that returned no usable evidence.
- A run without evidence rows is marked `unverified`; it is not represented as
  an evidenced empty result set.

# Failure branches
| Symptom | Do this |
|---|---|
| A URL does not resolve or no longer supports the claim | Drop the row and retain the failed lookup only in the artifact. |
| Google finds a claim but the company source does not confirm it | Treat Google as discovery, not proof; leave the row unverified or drop it. |
| LinkedIn or a company site requires access you do not have | Do not bypass access controls. Record the coverage gap and escalate if the question cannot wait. |
| No source produces evidence | Save the artifact, set `resultCount` to 0, and set the run disposition to `unverified`. |
| The artifact changes after hashing | Recompute the SHA-256 and update the search-run before it is used. |
