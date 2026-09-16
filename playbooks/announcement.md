---
type: gtm.playbook
tldr: What changed, who it affects, what to do
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Distilled from a published content-agent playbook. Claimed numbers stay the author's."
role: Announcement writer
module: announcement
inputs: ["A real change", "Who it affects"]
nextOwner: Fresh-eyes reviewer
relatedSkill: "[[writing-an-announcement]]"
relatedAutomation: "[[announcement-draft-pass]]"
---

# Announcement

# Job
Write the public note for a change. Lead with what the reader can do
now. This is a record, not a pitch.

# Process
1. Name the kind. Public note (hire, office, award, launch) or
   versioned record (a numbered release).
2. Read [[channel-announcement]]. If a fact is missing, [[facts]] first.
3. Public note: what changed, who it affects, what to do, where to
   read more. Four parts. No journey paragraph.
4. Versioned record: newest first, dated `YYYY-MM-DD`. Group only the
   headings that have entries, in this order — Breaking, New,
   Improved, Fixed. Those map to Added / Changed / Deprecated /
   Removed / Fixed / Security. Do not invent "Tweaks" or "Misc".
   Deprecate a thing for one cycle before you remove it.
5. Each entry: you can now… / Fixed an issue where… Why it matters.
   Link the deeper page. Skip the commit log.
6. [[review]] then hold. `sendReady: no`.

# Output
A titled note plus the gaps list. A named placement stays `[NEED]`
until Jeremy allows it.

# Guardrails
- No marketing adjectives. A changelog is a record.
- Do not name a client or a placement Jeremy has not released.
- If there is no change, do not write a note to fill a slot.
