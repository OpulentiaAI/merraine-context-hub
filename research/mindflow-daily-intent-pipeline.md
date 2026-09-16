---
type: gtm.tactic
tldr: A daily intent pull, then a hard filter
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from the published case study. Claimed numbers stay the author's."
source: "Mindflow / Gojiberry case study"
sourceUrl: "https://gojiberry.ai/case-study-mindflow"
category: architecture
claimedResult: "Mindflow claims a 31–35% reply rate and 21% of replies to MQL. Their number, not ours."
adoptionState: adapted
---

# A daily intent pull, then a hard filter

# The play
Pull fresh intent every day. Filter by company type, title, geo, and
size before anyone writes a line. Adapt the campaign to the signal that
fired. They sell a long enterprise cycle; one deal funded the tool.

# How we apply it for Merraine
[[signal-triggered-outbound]] is the daily pull. [[icp]] is the hard
filter. Title list and geos already live on [[icp-context]]. Do not skip
the filter because the signal was exciting.
