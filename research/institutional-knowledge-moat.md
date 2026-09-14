---
type: gtm.tactic
tldr: Encoded institutional knowledge is the moat
status: active
owner: Opulent
updated: 2026-09-14
provenance: "Field Theory bookmark 2080716441041465427, @ParthGujare_ on Ramp Revenue"
source: "@ParthGujare_ (Ramp)"
sourceUrl: "https://x.com/ParthGujare_/status/2080716441041465427"
category: architecture
appliesTo: []
claimedResult: "Ramp Revenue used by >90% of Ramp's GTM teams"
adoptionState: adopted
---

# Encoded institutional knowledge is the moat

## The play

> "Automating repeatable tasks isn't the point. The real unlock is that we're
> encoding institutional GTM knowledge that used to live in reps' heads — playbooks,
> account memory, what worked for which segment, why a deal moved — and making it
> computable. Every run compounds it. Every human correction teaches the system.
> The org's rate of learning becomes the moat, not any single agent."

Three things the author says made it work:

- **A composable context layer.** Give the agent a live shared view of the account
  and let it write back what it learns. Generic models do not know your customers.
- **A real harness.** Short episodes, memory, triggers, evals, human approval points.
  Shipping an agent is easy; real work at an acceptable quality bar is hard.
- **Playbooks as the orchestration layer.** Who qualifies, why now, the message, the
  channel — agents turn that into the work.

## How we apply it for Merraine

This is the argument for the whole hub, and the thing to say to Jeremy Sanchez when
he asks why we did not just buy six tools.

Six tools give him six context-free surfaces. What Merraine actually owns that no
vendor can sell them is twenty-five years of knowing which companies hire, which
executives move, and who returns a call. That currently lives in Jeremy Sanchez's
head and his mailbox.

The mapping is direct:
- composable context layer -> this hub, mounted on his workspace
- write back what it learns -> [[hub-self-extension]]
- human correction teaches the system -> [[transcript-healthcheck]]
- playbooks as orchestration -> the automation dictionary
