---
type: gtm.signal
tldr: Federal contract award
status: active
owner: Opulent
updated: 2026-09-14
provenance: "@scaling_shields: public databases get 5-12% reply vs Apollo's 0.5%"
rank: 6
sourceSystems: [USASpending.gov]
query: "Award of $500k+ to an ICP-sector company within 90 days"
citationRequirement: "USASpending award record URL with award date and value"
decayDays: 90
falsePositives: ["Renewals of existing ceilings counted as new", "Prime vs sub confusion"]
openerAngle: "Confirmed budget with a delivery deadline, which means hiring against the contract"
evidence: []
---

# Federal contract award

## How to detect

Filter USASpending by ICP-relevant NAICS and award date. Capture company, award value, service type, award date.

## How to disqualify

Drop option-year exercises presented as new awards. Confirm the awardee entity matches the company you intend to contact.
