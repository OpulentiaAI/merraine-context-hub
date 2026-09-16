---
type: gtm.signal
tldr: Executive departure or arrival in last 90 days
status: active
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "@draprints 'changed jobs in past 90 days - new VPs have budget and points to prove'; @chrispisarski 'track every champion who changes jobs and route them as a new account'"
rank: 3
sourceSystems: [LinkedIn, Parallel Monitor, company press, news APIs]
query: "C-level or VP-level departure, arrival, or promotion at an ICP org within 90 days"
citationRequirement: "A LinkedIn profile change, press release, or news article with a date"
decayDays: 90
falsePositives: ["Lateral moves inside the same company with no new mandate", "Board observer seats", "Advisor titles"]
openerAngle: "New leaders rebuild their team in the first two quarters, and a departure leaves a seat somebody has to fill"
evidence: []
---

# Executive departure or arrival in last 90 days

# How to detect
Track arrivals and departures for ICP titles. An arrival is a buyer with a mandate. A departure is an open seat. Both are routable; score the departure higher when no successor is named.

# How to disqualify
Drop title inflation with no role change. Drop moves older than 90 days. If a successor was announced simultaneously, the seat is filled - downgrade to relationship-building.
