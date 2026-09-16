---
type: gtm.playbook
tldr: One angle per prospect — why them, why now
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS research module, rewritten for Merraine"
role: Account researcher
module: research
inputs: ["ICP Keep rows"]
nextOwner: Lead enricher
relatedSkill: "[[researching-an-account]]"
relatedAutomation: "[[account-research-pass]]"
---

# Research

# Job
Find the angle: why this company, why this person, why now. One angle per
prospect. Two is indecision.

# Process
1. Take only ICP **Keep** rows.
2. Company: what they sell, size, a recent public event. Primary sources
   only — site, LinkedIn company, filing, blog.
3. Person: role scope, time in seat, a public post that names a problem.
4. Fit to a search: the problem in **their** language.
5. Angle test: if you deleted the company name, would the opener still make
   sense? If yes, the research failed.
6. Risk flags: already a client, just raised and is being spammed, already
   inside an open Merraine search.

# Output
```
company:
person:
why_them:
why_now:          # event + date, or "no fresh trigger — say so"
angle:            # one sentence
proof_we_can_use: # only real proof from [[icp-context]]
do_not_mention:
confidence: H/M/L
gaps:             # [NEED: x]
```

Hand the angle, not the binder, to [[drafting-outreach]].

# Guardrails
- No invented funding rounds, headcount, or "I saw you posted".
- A thin angle, labelled thin, is honest. It produces a shorter note.
