---
type: gtm.pipeline
tldr: Merraine search pipeline
status: draft
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Provisional. Real stage durations come from [[email-communications-extraction]], which is blocked on Gmail."
systemOfRecord: "UNVERIFIED - Merraine has no CRM we can write to yet. Notion is the candidate."
writeBackPolicy: "Nothing writes back to a Merraine system until Jeremy Sanchez names one and grants scope."
stages:
  - tldr: Signal
    order: 1
    name: Signal
    entryCriteria: "A cited gtm.observation exists against an ICP org"
    exitCriteria: "Buyer identified and enriched"
    ownerRole: automation
    slaDays: 1
  - tldr: Opener held
    order: 2
    name: Opener held
    entryCriteria: "Draft written and slop-checked"
    exitCriteria: "Jeremy Sanchez approves or rejects"
    ownerRole: jeremy-sanchez
    slaDays: 2
  - tldr: Conversation
    order: 3
    name: Conversation
    entryCriteria: "Reply received"
    exitCriteria: "Scoping call booked"
    ownerRole: jeremy-sanchez
    slaDays: 7
  - tldr: Scoping
    order: 4
    name: Scoping
    entryCriteria: "Call held"
    exitCriteria: "Search mandate agreed"
    ownerRole: jeremy-sanchez
    slaDays: 14
  - tldr: Search
    order: 5
    name: Search
    entryCriteria: "Mandate signed"
    exitCriteria: "Shortlist delivered"
    ownerRole: merraine
    slaDays: 30
  - tldr: Placement
    order: 6
    name: Placement
    entryCriteria: "Client interviews begin"
    exitCriteria: "Candidate placed and invoiced"
    ownerRole: merraine
    slaDays: 60
---

# Merraine search pipeline

# Flow
Signal -> filter -> research -> score -> opener held -> conversation ->
scoping -> search -> placement.

The specialist modules for the first five steps live in [[playbook-catalog]].
[[routing]] owns the board.

Only stages 1 and 2 are automated. Everything from stage 3 is Jeremy's. The
hub prepares: a brief before every call, a reminder when a thread goes quiet,
a record of what was said.

# Guardrails
- **Stage 2 is a hard stop.** Nothing advances from held to sent without him.
- The `slaDays` above are **placeholders**, not measurements. They are replaced by
  real medians from `reconstructed-pipeline.json` once the mailbox extraction runs.
  Until then, never present them as data.
- No stage writes to a Merraine system. This hub reads and drafts; it does not
  mutate his systems of record.
