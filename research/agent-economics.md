---
type: gtm.tactic
tldr: Production agent economics
status: active
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "Field Theory bookmark 2069769261778686044, LangChain on Clay's Head of AI"
source: "Clay via @LangChain"
sourceUrl: "https://x.com/LangChain/status/2069769261778686044"
category: ops
appliesTo: []
claimedResult: "Observed running 350m GTM agents a month"
adoptionState: adopted
---

# Production agent economics

# The play
From running roughly 350 million GTM agents a month:

- Caching can cut LLM costs up to 70%.
- **Bounding tool calls often improves quality, not just cost.**
- Fairness queues matter once you have real multi-tenant load.

# How we apply it for Merraine
The middle point is the one that changes our instructions. An unbounded research
loop is not merely expensive, it is *less accurate* — it wanders, accumulates weakly
related context, and starts asserting things it half-saw.

So every automation here carries a `costCeilingUsd`, every extraction caps tool
calls per entity class, and [[routine-healthcheck]] treats a rising tool-call count
as a correctness regression rather than a billing item.

The same discipline appears in the Browserbase research skills as hard per-entity
caps: one call for ICP triage, five for deep research, four per person. Cap first,
then let the agent argue for more.
