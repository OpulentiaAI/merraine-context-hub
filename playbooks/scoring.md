---
type: gtm.playbook
tldr: Rank likelihood to buy a search now
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS scoring module, rewritten for Merraine"
role: Intent scorer
module: scoring
inputs: ["Researched keepers", "[[intent-score]]"]
nextOwner: Copywriter
relatedSkill: "[[scoring-intent]]"
relatedAutomation: "[[intent-score-pass]]"
---

# Scoring

# Job
Rank by likelihood they will open a search **now**. Fit without timing is a
nurture row, not a first-touch.

# Process
1. Take researched keepers.
2. Score each with the four parts on [[intent-score]] visible (not a naked 73).
3. Sort descending. Default cut: first-touch ≥ 65.
4. Flag collisions: already in a campaign, already messaged, already a client.

# Output
```
# Intent ranking — [date]
Cut line: 65
Basis: heuristic

| Rank | Name | Company | Total | ICP/30 | Title/20 | Signal/35 | Angle/15 | Cut | Note |
```

Hand ≥ cut to [[drafting-outreach]]. Hand below cut to a named nurture list.
Do not delete. Do not message.

# Guardrails
- Do not average a 12-person sample into "this ICP converts".
- Do not boost a score because we already wrote a clever line.
