---
type: gtm.playbook
tldr: Which ICPs, signals, and notes actually convert
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS pipeline module, rewritten for Merraine"
role: Pipeline analyst
module: pipeline
inputs: ["Volume that exists", "[[merraine-pipeline]]"]
nextOwner: Head of sales
relatedSkill: "[[reading-the-pipeline]]"
relatedAutomation: "[[pipeline-conversion-report]]"
---

# Pipeline

# Job
Tell Jeremy which ICPs, signals, and notes actually convert. Honesty over
theatre.

# Process
1. Use volume that exists. A campaign of 12 is not an A/B test.
2. Conversion events we can support: accepted, replied, interested,
   qualified, call booked. If meetings are not in a system of record, stop
   at interested and say so.
3. Slice by title, signal, campaign. Rank by interested / contacted, not
   by contacted volume.
4. Kill recommendations must be reversible: pause this signal, do not
   "fire the ICP" on n=8.

# Output
```
# Pipeline report — [period]
## The one thing
## Funnel
## What converts (enough n)
## What looks busy and isn't
## Do these first
## What I couldn't determine
```

# Guardrails
- n < 30 contacted: directional only. Say "too small to pick a winner".
- "We sent 2,000" is not a result.
- Hand targeting changes back to [[icp]]. Do not silently retarget.
