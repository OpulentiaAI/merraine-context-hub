---
type: gtm.signal
tldr: Senior role posting open >30 days
status: active
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "@Kazanjy 'job postings = hiring pain'; @scaling_shields public-database sourcing"
rank: 1
sourceSystems: [LinkedIn Jobs, Indeed, company careers page, Parallel Monitor]
query: "Senior titles (CEO, COO, CHRO, VP, Head of) posted >30 days ago, OR 3+ senior reqs open at once at one org"
citationRequirement: "A resolvable job posting URL with a visible post date"
decayDays: 45
falsePositives: ["Junior or IC reqs", "Evergreen reqs that never close", "Agency-posted duplicates of the same role"]
openerAngle: "They have been carrying the seat for over a month, which is the moment a search firm stops being optional"
evidence: []
---

# Senior role posting open >30 days

# How to detect
Pull postings for ICP titles. Age each one. Flag orgs where a senior seat has stayed open past 30 days, or where three or more senior seats are open simultaneously. Record the posting URL and post date verbatim.

# How to disqualify
Drop evergreen reqs (same title reposted continuously for a year), agency reposts of a role already counted, and anything below director level. If the org is a staffing firm, drop it as a competitor.
