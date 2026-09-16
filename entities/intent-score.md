---
type: gtm.score-model
tldr: First-touch vs nurture score
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS scoring rubric, weights unchanged, language adapted for a search"
scaleMin: 0
scaleMax: 100
firstTouchCut: 65
icpWeight: 30
titleWeight: 20
signalWeight: 35
angleWeight: 15
---

# Intent score

# Rubric
| Band | Score | Meaning |
|---|---|---|
| In-market, ICP, fresh trigger, right title | 80–100 | First-touch this week |
| ICP + real trigger, title is champion not buyer | 65–79 | First-touch, CTA is a question or an intro |
| ICP, weak or stale signal | 45–64 | Nurture. Do not burn the first note. |
| Off-ICP or no signal | 0–44 | Do not contact |

Parts: ICP fit 30, title buying power 20, signal strength + freshness 35,
angle quality 15.

# Process
Read [[scoring]] and [[icp-context]]. Score the four parts in the open.
Recommend the cut (default 65). Flag anyone already touched. The weekday
job is [[intent-score-pass]].

# Guardrails
All scores are heuristics unless a connected tool supplied its own number.
Say which. Do not boost a score because the copy is clever.
