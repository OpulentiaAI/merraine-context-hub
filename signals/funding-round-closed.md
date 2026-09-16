---
type: gtm.signal
tldr: Funding round closed in last 60 days
status: active
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "@scaling_shields 'a company that raised $5m last week has $5m to deploy'"
rank: 2
sourceSystems: [Crunchbase, PitchBook, Parallel Monitor, SEC EDGAR]
query: "Any priced round closed within 60 days at an ICP-sized company"
citationRequirement: "Press release, filing, or database record with a close date"
decayDays: 60
falsePositives: ["Rumored or unannounced rounds", "Extensions counted twice", "Rounds older than 60 days"]
openerAngle: "New capital converts directly into senior hires, and the hiring plan is written in the first quarter after close"
evidence: []
---

# Funding round closed in last 60 days

## How to detect

Watch funding feeds for ICP-sized companies. Record amount, stage, close date, and the source URL. Cross-reference against open senior reqs to raise the score.

## How to disqualify

Drop anything you cannot cite to a filing or an official announcement. Never infer a round from a congratulatory social post.
