---
type: gtm.playbook
tldr: Find people showing real buying intent
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Sales OS signals module, rewritten for Merraine leadership search"
role: Signal hunter
module: signals
inputs: ["[[icp-context]]", "[[merraine-icp]]", "[[signal-catalog]]"]
nextOwner: ICP analyst
relatedSkill: "[[hunting-signals]]"
relatedAutomation: "[[signal-triggered-outbound]]"
relatedSignals: ["[[senior-role-posting-open]]", "[[funding-round-closed]]", "[[executive-move]]", "[[category-conversation]]", "[[posted-hiring-pain]]", "[[social-warmth]]", "[[lookalike-won]]"]
---

# Signals

# Job
Find people showing **real buying intent**, not people who merely exist. Hand
a cited list to the ICP filter. Do not enrich. Do not write messages.

# Process
1. Read [[icp-context]] and [[merraine-icp]].
2. Hunt only the ranked triggers on those files and on [[signal-catalog]].
   Strongest first: a senior seat open past 30 days, a raise that funds a
   bench, an executive move, someone already talking about the category,
   a public post naming the hiring pain, social warmth, a lookalike of a
   search already won.
3. Record the signal in their words or in platform data, plus the date.
   No signal, no row.
4. Cap the list (default 25). Quality over a dump.

Does not count: title match alone, "works at a growth-stage company", a like
on a motivational quote.

# Output
```
# Signal list — [query] — [date]
Source: [tool / page]
Count: N

| Name | Title | Company | Signal (quote or event) | Date | Source | Suggested next |
```

# Guardrails
- If the search returns nobody, say nobody. Then offer to widen one variable
  (title or geo or signal), not all three.
- Never invent a signal to make a row look warm.
- This is the play Wispra named: stop targeting profiles, start targeting
  conversations. Their claim is theirs. See [[wispra-conversation-targeting]].
