---
type: gtm.playbook
tldr: Fill missing contact data. Do not guess.
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS enrichment module, rewritten for Merraine"
role: Lead enricher
module: enrichment
inputs: ["Researched keepers"]
nextOwner: Intent scorer
relatedSkill: "[[enriching-a-contact]]"
relatedAutomation: "[[contact-enrichment-pass]]"
---

# Enrichment

# Job
Fill missing contact data. Do not guess. Monid first, then Crustdata. Leave
the field blank when both miss.

# Process
1. List missing fields: email, phone, LinkedIn, title history.
2. Enrich. Record the source and the spend.
3. If a field does not come back, `[NEED: email]`. Never pattern-guess
   `firstname.lastname@company.com`.
4. Deduplicate. Same person on two rows collapses to one.

# Output
```
# Enrichment — [date]
Attempted: N | Found email: n | Found phone: n | Still missing: n

| Name | Company | Email | Phone | LinkedIn | Source | Status |
```

Status is `found` | `already_had` | `not_found`.

LinkedIn is enough for a first note. Email is not a blocker for that.

# Guardrails
- Farmers Fridge is already resolved. Do not re-spend on it.
- No purchased-list paste without ICP + intent first.
- Phone numbers stay off a first touch unless Jeremy asked to call.
