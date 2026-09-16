---
type: gtm.playbook
tldr: Read replies. Identify interest. Do not close.
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS replies module, rewritten for Merraine"
role: Reply agent
module: replies
inputs: ["Open threads"]
nextOwner: Follow-up or meeting qualifier
relatedSkill: "[[triaging-replies]]"
relatedAutomation: "[[unibox-triage]]"
---

# Replies

# Job
Read replies. Identify who is interested. Do not close the search here.

# Process
Classify each open thread:

| Label | Meaning | Next |
|---|---|---|
| interested | wants a call, asks how a search works | [[qualifying-a-meeting]] |
| question | real question, not buying yet | [[following-up]] |
| warm | polite, not now, "send info" | [[following-up]] |
| objection | timing, already have a firm | one pass, then stop |
| ooo | out of office | wait for the return date |
| negative | stop, unsubscribe, hostile | log, do not message |
| noise | auto-note, "thanks" | ignore |

Quote the prospect. Never paraphrase interest into a meeting they did not
ask for.

# Output
```
# Triage — [date]
Open threads: n
## Interested (n)
## Questions (n)
## Warm (n)
## Negative / stop (n)
```

# Guardrails
- Speed matters more than poetry. Interested people go to qualification
  the same turn.
- Do not continue a thread that said stop.
- Baur's rule applies: the moment someone replies, automation stops.
  See [[baur-exit-on-reply]].
