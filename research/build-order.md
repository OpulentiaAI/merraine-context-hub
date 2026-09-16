---
type: gtm.tactic
tldr: Build order - data layer before agents
status: active
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "Field Theory bookmark 2059254933539451104, @lukepierceops"
source: "@lukepierceops"
sourceUrl: "https://x.com/lukepierceops/status/2059254933539451104"
category: architecture
appliesTo: []
claimedResult: "Author's basis: systems built for 85+ companies"
adoptionState: adopted
---

# Build order - data layer before agents

# The play
> "The order you build in matters more than what you build."

1. **Data layer** — one place where truth lives. Everything reads from and writes to it.
2. **Intake** — standardised fields, validated inputs, deduplication. 80% of
   automation problems trace back to dirty intake.
3. **Routing** — where data goes next, under what conditions.
4. **Notifications and handoffs** — the connective tissue between humans and system.
5. **Automations** — the actual time-savers.
6. **Agents** — intelligence on top of workflows that already exist.
7. **Dashboards** — the view layer.

> "People start at step 6 because agents are sexy and they don't want to tell the
> client no. Then they wonder why nothing holds up at scale."

# How we apply it for Merraine
This hub **is** step 1, and that is the whole reason it exists rather than a folder
of prompts. The typed graph is the data layer; `merraine/types` is the schema.

Where the engagement actually sits:

- Step 1 data layer — this repo, plus the Spear extraction already delivered
- Step 2 intake — [[email-communications-extraction]], blocked on [[gmail]]
- Step 3 routing — [[merraine-pipeline]] stages
- Step 5 automations — the automation dictionary, none Enabled yet
- Step 6 agents — the Gojiberry desks, deliberately last

The temptation with Jeremy Sanchez will be to jump to step 6 and show him thirteen
agents on day one. Resist it. Connect Gmail, land the extraction, and the agents
have something true to stand on.
