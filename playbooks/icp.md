---
type: gtm.playbook
tldr: Decide who we target, then brake before outreach
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS icp module, rewritten for Merraine"
role: Head of sales + ICP analyst
module: icp
inputs: ["[[icp-context]]", "[[merraine-icp]]"]
nextOwner: Account researcher
relatedSkill: "[[evolving-the-icp]]"
relatedAutomation: "[[icp-evolution-review]]"
---

# ICP

# Job
Decide the battlefield, then filter. Do not hunt leads in this module. False
positives cost more than missed logos.

# Process
**Who to target**

1. State the offer in one sentence a CEO would recognise. Today that lives
   on [[merraine-icp]]. Gaps stay `[NEED]`.
2. Name the economic buyer, the user, and the champion. They are often
   different (CEO / CHRO / Head of Talent).
3. Must-have vs nice-to-have vs never. Never wins.
4. Pick 1–3 buying triggers that imply budget and timing. Vanity signals
   stay off the hunt list.
5. Name the anti-ICP: staffing firms, pre-seed, large public enterprises
   Jeremy did not name, anyone inside an open search.

**Filter before outreach**

For every prospect: company match, title match, disqualifiers, signal still
true. Decision: Keep / Maybe / Drop, with one sentence. Maybe does not go
to outreach.

# Output
```
# Targeting brief — [date]
## Who
## Why now
## Must-have
## Never
## Triggers we will hunt
## Triggers we will ignore
## First list to build
## What I couldn't determine
```

Filter columns: `company_fit` · `title_fit` · `signal_fresh` · `decision` · `why`.

# Guardrails
- Do not enrich here. Do not write copy.
- Do not "keep them anyway, the message can be generic".
- Drop silently is forbidden. Every drop gets a why so [[reading-the-pipeline]]
  can see if we over-filtered.
- The living file is [[icp-context]]. Review it on the clock in
  [[icp-evolution-review]]. Do not invent a value to make a draft easier.
