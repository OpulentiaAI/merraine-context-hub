---
type: gtm.signal
tldr: Reviewed a competing service
status: active
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "@scaling_shields: reviewers have budget, are comparing, and are reachable"
rank: 7
sourceSystems: [G2, Capterra]
query: "Left a review of a staffing, search, or HR-tech product within 90 days"
citationRequirement: "Review URL with reviewer profile and date"
decayDays: 90
falsePositives: ["Reviews left by vendors themselves", "Anonymous reviews with no attributable identity"]
openerAngle: "They bought something in this category, which proves budget and an active evaluation"
evidence: []
---

# Reviewed a competing service

# How to detect
Pull reviewers of competing search and HR platforms. Match reviewer identity to ICP titles.

# How to disqualify
Drop anonymous reviews. Drop anyone whose employer is a competitor. Confirm the reviewer still works where the review says.
