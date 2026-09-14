---
type: gtm.signal
title: Headcount growth 20%+ year over year
status: active
owner: Opulent
updated: 2026-09-14
provenance: "@draprints 'growing companies = hiring = budget'; @Kazanjy signal reading"
rank: 5
sourceSystems: [LinkedIn, Crustdata, Monid, Parallel Monitor]
query: "Employee count up 20% or more over trailing twelve months at an ICP org"
citationRequirement: "A dated headcount series from a provider, not a single snapshot"
decayDays: 120
falsePositives: ["Growth from an acquisition rather than hiring", "Provider miscounts from a domain merge", "Contractor surges"]
openerAngle: "Sustained growth means the org chart is outrunning its leadership layer"
evidence: []
---

# Headcount growth 20%+ year over year

## How to detect

Compare trailing-twelve-month headcount from a provider that returns a dated series. Flag 20%+ increases.

## How to disqualify

Drop growth explained by an acquisition. Drop single-snapshot claims - one number is not a trend. Treat provider disagreement as a conflict to record, not resolve by guessing.
