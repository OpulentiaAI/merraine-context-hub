---
type: gtm.playbook
tldr: Draft freely. Schedule only on confirm.
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
role: Social queue operator
module: social-queue
inputs: ["A settled message", "[[jeremy-writing-prefs]]"]
nextOwner: Jeremy Sanchez
relatedSkill: "[[running-the-social-queue]]"
relatedAutomation: "[[social-queue-draft]]"
---

# Social queue

# Job
Read the real accounts and drafts, then write platform-native versions
into a held queue. Publishing and deletes wait for the confirm word.

# Process
1. Read [[jeremy-writing-prefs]]. Default surfaces are LinkedIn and email.
2. List what is actually connected and what drafts already exist. Never
   invent a handle, a draft id, or a statistic.
3. Adapt the same claim per surface via [[channels]]. One announcement,
   many voices. See [[one-claim-many-voices]].
4. Lint each version with [[keeping-prose-clean]] and the matching
   channel guide. Then [[review]].
5. Propose a time. Do not set it. `sendReady: no`.
6. If a fact is missing, [[verifying-a-public-claim]] first.

# Output
```
# Queue pack — [date]
Surfaces: [from prefs]
| Surface | Draft | Fold | Lint | Review | Schedule proposed |
```

# Guardrails
- No social queue is connected today. Say so. Still write the drafts.
- Do not fabricate analytics. The Monday digest skips rather than guesses.
- Deletes are permanent. Only when Jeremy asks.
