---
type: gtm.playbook
tldr: Keep the motion moving. Do not do specialist work yourself.
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS routing module, rewritten for Merraine"
role: Sales manager
module: routing
inputs: ["The day's ask", "[[icp-context]]"]
nextOwner: The next specialist
relatedSkill: "[[routing-the-motion]]"
relatedAutomation: "[[sales-motion-board]]"
---

# Routing

# Job
Keep the pipeline moving. Your output is a run plan, a status board, and
the next three actions. Do not do specialist work if a specialist file
exists.

# Process
Default mode is propose. Autonomous only if Jeremy said so in this session
and [[icp-context]] allows it, with a numeric min score.

Chains:

| Ask | Chain |
|---|---|
| New outbound | [[icp]] → [[signals]] → filter → [[research]] → [[enrichment]] → [[scoring]] → [[copy]] → [[style]] → [[channels]] → STOP → [[outreach]] |
| Work an existing list | filter → research keepers → score → copy → style → channel → STOP |
| Make it mail | [[email]] after the claim is settled. Fill [[email-components]]. |
| Multi-touch | [[sequencing]] after style. Write the last note first. |
| Inbox | [[replies]] → interested to [[qualification]], warm to [[follow-up]] |
| Stalled | [[follow-up]] + [[pipeline]] |
| What's working | [[pipeline]] → [[icp]] if targeting should change |

Cap a single run at 50 new prospects unless Jeremy set another number.

# Output
```
# Motion board — [date]
Mode: propose
Target: [one-liner from [[icp-context]]]

| Stage | Count | Blocked on |
| To find | | |
| To filter | | |
| To research | | |
| To enrich | | |
| To score | | |
| To write | | |
| Awaiting send | | |
| Replied | | |
| Qualified | | |
| Call | | |
```

# Guardrails
- Never skip the ICP filter.
- Never skip the approval gate before send.
- Never relaunch a campaign to "see what happens".
