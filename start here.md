---
type: map::au-base-types
tldr: Entry point for the Merraine GTM context hub.
---

# Merraine context hub

You are in **Jeremy Sanchez's** GTM workspace (Merraine Group, executive search).

## Read first

- [[hub-inject]] — the standing rules. They apply to every session.
- [[convex-pilot]] — how to see the truth about the Opulent account.
- [[merraine-icp]] — who we sell to, and what is still unknown.
- [[automation-dictionary]] — everything we can stand up.

## The shape of the graph

- **Who** — [[merraine-group]], [[jeremy-sanchez]], [[sanchez-opulent-account]]
- **What we watch** — [[signal-catalog]], seven ranked buying triggers
- **What we pull in** — [[runbook-catalog]], the extraction runbooks
- **What runs** — [[automation-dictionary]]
- **Why we do it this way** — [[tactic-catalog]]

## Before you act

Run `scripts/audit.sh`. Ground truth about the account comes from production,
never from memory. Then `python3 scripts/validate.py` — the graph must be clean
before you add to it.

## The rule that matters most

Nothing sends, pays, publishes, or contacts a human unless a human types the
confirm word in that moment. Every draft carries `sendReady: no`.
