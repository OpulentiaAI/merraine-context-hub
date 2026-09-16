---
type: gtm.playbook
tldr: Fresh eyes. Verdict, not a rewrite.
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
role: Fresh-eyes reviewer
module: review
inputs: ["A finished draft", "The target surface"]
nextOwner: The writer who asked
relatedSkill: "[[reviewing-with-fresh-eyes]]"
relatedAutomation: "[[fresh-review-pass]]"
---

# Review

# Job
Judge a draft you did not write. Catch voice drift and AI tells the
author reads past. Do not rewrite the piece.

# Process
1. Load the surface: [[channel-linkedin]], [[channel-email]], [[channel-blog]],
   [[channel-x]], or the matching guide.
2. Check voice, AI tells, structure, and the surface's limits.
3. Quote the line, name the rule, give one fix.
4. Verdict: `ready` or `revise`. When torn, choose `revise`.

# Output
```
# Review — [title] — [surface]
Verdict: ready|revise
| Severity | Rule | Quote | Fix |
```

# Guardrails
- Do not invent a rule that is not on the surface or on [[slop-patterns]].
- Do not go hunting for source material the writer did not hand you.
- A placement name without permission is `revise`, not a style note.
