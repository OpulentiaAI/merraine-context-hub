# Start here

**Jeremy — paste the block below into a new Opulent session. That is the whole setup.**

Everything after that is auth clicks. The agent drives the rest.

---

## The paste block

```text
Read this repository as your operating context: merraine-context-hub.

You are running Jeremy Sanchez's Opulent account (jeremysanchez@opulentia.ai, Merraine Group,
leadership search). Mount this hub, then work the day-one order in ONBOARDING.md.

Start by reading, in this order:
  inject/hub-inject.md              - standing rules
  entities/workspace-now.md         - what is already in this workspace
  entities/connection-inventory.md  - what is actually connected
  catalogs/automation-dictionary.md - what we can stand up
  catalogs/playbook-catalog.md      - specialist modules in the motion
  entities/icp-context.md           - living ICP. Empty fields stay empty.
  entities/merraine-icp.md          - who we sell to, and what is still unknown

Then tell me the workspace's real state before doing anything else.

Standing rules, non-negotiable:
- Nothing sends, pays, publishes, or contacts a person unless I type "send" in that moment.
- Emailing the daily hiring scan to jeremy@merraine.com is delivery to me, not outbound.
- Every claim carries a resolvable source. Empty results are UNVERIFIED, never zero.
- "completed" is not proof. Open the artifact.
- Three things come to me: a secret, a payment, a send. Decide everything else yourself.
```

---

## What you will be asked to authorise

Four clicks, in this order. The agent handles everything between them.

| # | What | Where | Why it matters |
|---|---|---|---|
| 1 | **Gmail** | Settings → Connectors | Unlocks mailbox extraction — relationships, voice, and the real pipeline. This is the big one. Two earlier logins timed out. |
| 2 | **Sales Navigator seat** | LinkedIn, about $99/mo | Not a build. Five filters do the work. See `research/sales-navigator-filters.md` |
| 3 | **Apollo** (optional) | Connectors | Trial expired. If it needs a paid plan, say so and we drop it. |
| 4 | **Gojiberry** (on request) | Say "wire up Gojiberry" | The agent creates the account. Only the LinkedIn connect needs you. |

Already connected: **Spear** (131 tools, export already in Drive), **Notion**
(42 tools, Shepherd Search Group / Merraine), **Parallel Monitor**, **Mesa**.

---

## Day one, in order

**1. Ground truth.** Read `entities/workspace-now.md` and
`entities/connection-inventory.md`. As of 16 September 2026 the hub is not
mounted yet, Spear is already extracted, and no automation is on a clock.

**2. Mount the hub.** `CONFIRM=send python3 scripts/materialize.py --apply`.
Installs the Jeremy-facing files as knowledge and runbooks, then attaches them
to Default Workspace so every later session starts with this context.

**3. Gmail, then extract.** Once Gmail is connected,
`extractions/email-communications-extraction.md` runs. It produces:

- `relationship-graph.json` — everyone you know, how warm, by reply latency
- `voice-profile.md` — how you actually write, from 15–30 of your own replied-to mails
- `reconstructed-pipeline.json` — the real pipeline, rebuilt from threads
- `suppression-list.json` — who must never be contacted

Read-only. Nothing is sent, filed, or labelled.

**4. Do not re-extract Spear.** 57 Drive files and `personal-context-hub.zip`
are already there. 1,314 prospects on your profile, 1,639 on Reid's.

**5. Stand up two automations first.** Both created Disabled, both checked on
one manual run before any clock starts. The rest of the motion
(`catalogs/automation-dictionary.md`) stays off until those two open clean.

- **Signal-triggered outbound** — weekday 6:30am. Who became a buyer overnight,
  with a cited opener waiting.
- **Awards and recognition monitor** — Monday 7am. Forbes, Crain's Chicago,
  Crain's New York, the business journals. A named congratulations per honoree.

The daily CFO / VP+ hiring scan already has a written procedure
(`runbooks/daily-hiring-scan.md`). It is not on a clock. Say when you want it
scheduled.

**6. Turn on the self-improvement loop.** Two quiet healthchecks that mine
session history for friction and waste and propose fixes. They propose. They
never apply.

---

## Your six asks, and where each one landed

| Your ask | Where it lives | State |
|---|---|---|
| Universal search across LinkedIn, Google, company sites | `automations/signal-triggered-outbound.md` + `runbooks/daily-hiring-scan.md` | Needs Gmail for the mailbox side. The daily scan already runs on request. |
| LinkedIn Sales Navigator | `research/sales-navigator-filters.md` | Buy the seat — do not build it |
| Spear for sequencing, replies, auto-prospecting | Already connected, data already extracted | Ready now |
| Enrichment: name → email, phone, title history | Monid → Crustdata. Farmers Fridge already resolved. | Ready |
| Market signals: raises, exec moves, job postings | `signals/` + `automations/signal-triggered-outbound.md` | Build this first |
| Awards tracker: Forbes, Crain's, regional journals | `automations/awards-recognition-monitor.md` | Ready to stand up |

You asked for six tools. You wrote "one stack" and asked for the fastest path
to pilot **one** of them this month. The answer is the fifth row: market
signals is the engine. The other five are its inputs and outputs.

---

## What this repo is

A typed knowledge graph, not a folder of prompts. Built on
[arsumbris](https://arsumbris.ai) — markdown and YAML that an engine reads as
one queryable graph, so a field that should be a citation cannot quietly
become a guess.

```
type/         the ontology
entities/     Merraine, you, the workspace, living ICP, score model, connectors
signals/      ranked buying triggers
playbooks/    specialist modules — hunt, filter, score, reply, email, sequence
extractions/  how to pull a tool or a mailbox into the hub
automations/  paste-ready prompts with schedules — all Disabled
runbooks/     how the work actually runs
research/     voice, case-study plays, Spear vocabulary
catalogs/     generated indexes
skills/       triggered guidance
scripts/      audit, materialize, validate
```

`python3 scripts/validate.py` checks the whole graph: types resolve, links
resolve, no automation is enabled without a checked first run, nothing is
pre-approved to send, and operator notes cannot land on this workspace.

---

## What is deliberately not filled in

These are marked `[NEED: x]` in `entities/merraine-icp.md` and stay blank
until you answer.

- Which industries Merraine actually focuses on
- Three named placements or clients we may cite as proof
- Fee and capacity — what a search costs and how many you can run at once
- Your suppression list — who is already inside an open search
