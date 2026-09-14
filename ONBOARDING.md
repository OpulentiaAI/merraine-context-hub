# Start here

**Jeremy — paste the block below into a new Opulent session. That is the whole setup.**

Everything after that is auth clicks. The agent drives the rest.

---

## The paste block

```text
Read this repository as your operating context: merraine-context-hub.

You are running Jeremy Sanchez's Opulent account (jeremysanchez@opulentia.ai, Merraine Group,
executive search). Mount this hub, then work the day-one order in ONBOARDING.md.

Start by reading, in this order:
  injects/hub-inject.md          - your standing rules
  runbooks/convex-pilot.md       - how to see the truth about this account
  catalogs/automation-dictionary.md - what you can stand up
  entities/merraine-icp.md       - who we sell to, and what is still unknown

Then run scripts/audit.sh and tell me the account's real state before doing anything else.

Standing rules, non-negotiable:
- Nothing sends, pays, publishes, or contacts a human unless I type "send" in that moment.
- Every claim carries a resolvable source. Empty results are UNVERIFIED, never zero.
- "completed" is not proof. Open the artifact.
- Three things come to me: a secret, a payment, a send. Decide everything else yourself.
```

---

## What you will be asked to authorise

Four clicks, in this order. The agent handles everything between them.

| # | What | Where | Why it matters |
|---|---|---|---|
| 1 | **Gmail** | `platform.opulentia.ai/dashboard/settings/credentials` → Connectors | Unlocks the mailbox extraction — relationships, voice, and your real pipeline. This is the big one. |
| 2 | **Sales Navigator seat** | LinkedIn, ~$99/mo | Not a build. Five filters do the work; see `research/sales-navigator-filters.md` |
| 3 | **Apollo** (optional) | Connectors tab | Currently `error: account inactive`. If it needs a paid plan, say so and we drop it. |
| 4 | **Gojiberry** (on request) | Nothing — say "wire up Gojiberry" | The agent creates the account and wires the MCP itself. Only the LinkedIn connect needs you. |

Already connected and working: **Spear** (131 tools), **Notion** (42 tools),
**Parallel Monitor**, **Mesa**.

---

## Day one, in order

The agent follows this. It is here so you can see where it is.

**1. Audit.** `scripts/audit.sh`. Ground truth before opinions. You will see plan,
balance, workspace, and whether the hub is mounted.

**2. Mount the hub.** `CONFIRM=send python3 scripts/materialize.py --apply`.
Installs every file here as Opulent knowledge and runbooks, then attaches them to
your workspace so every future session starts with this context. At last check your
workspace had **zero** mounted context; this fills it.

**3. Gmail, then extract.** Once Gmail is connected,
`extractions/email-communications-extraction.md` runs. It produces:

- `relationship-graph.json` — everyone you know, how warm, by reply latency
- `voice-profile.md` — how you actually write, from 15-30 of your own replied-to mails
- `reconstructed-pipeline.json` — your real pipeline, rebuilt from threads
- `suppression-list.json` — who must never be contacted

Read-only. Nothing is sent, filed, or labelled.

**4. Extract the rest.** Every connected tool, in turn, using the pattern already
proven on Spear. Spear itself is **done** — 57 files and a context bundle are
already in your account. It will not be re-run.

**5. Stand up two automations.** Both created Disabled, both checked on one manual
run before any clock starts:

- **Signal-triggered outbound** — weekday 6:30am. Who became a buyer overnight,
  with a cited opener waiting.
- **Awards and recognition monitor** — Monday 7am. Forbes, Crain's Chicago, Crain's
  New York, the business journals. A named congratulations per honoree.

**6. Turn on the self-improvement loop.** Two quiet healthchecks that mine your own
session history for friction and waste and propose fixes. They propose; they never
apply.

---

## Your six asks, and where each one landed

| Your ask | Where it lives | State |
|---|---|---|
| Universal search across LinkedIn, Google, company sites | `automations/signal-triggered-outbound.md` + Browserbase research | Needs Gmail |
| LinkedIn Sales Navigator | `research/sales-navigator-filters.md` | **Buy the seat** — don't build it |
| Spear for sequencing, replies, auto-prospecting | Already connected, data already extracted | **Ready now** |
| Enrichment: name → email, phone, title history | Monid → Crustdata cascade, proven and costed | Ready |
| Market signals: raises, exec moves, job postings | `signals/` + `automations/signal-triggered-outbound.md` | **Build this first** |
| Awards tracker: Forbes, Crain's, regional journals | `automations/awards-recognition-monitor.md` | Ready to stand up |

You asked for six tools. You wrote "one stack" in the subject line and asked for the
fastest path to pilot **one** of them this month. The answer is the fifth row: market
signals is the engine, and the other five are its inputs and outputs.

---

## What this repo is

A typed knowledge graph, not a folder of prompts. Built on
[arsumbris](https://arsumbris.ai) — markdown and YAML that an engine reads as one
queryable graph, so a field that should be a citation cannot quietly become a guess.

```
types/        the ontology - 23 types. Everything here is typed against one of them.
entities/     Merraine, you, the account, every connector
signals/      7 ranked buying triggers, each with how to detect and how to disqualify
extractions/  how to pull a tool, a mailbox, a relationship graph into the hub
automations/  the automation dictionary - paste-ready prompts with schedules
runbooks/     operating procedures, including how the account is piloted
research/     outside tactics we adopted, every one attributed
catalogs/     generated indexes
skills/       triggered guidance for the agent
scripts/      the governed Convex seam: audit, materialize, validate
evidence/     dated audit bundles and a call ledger
```

`python3 scripts/validate.py` checks the whole graph: types resolve, links resolve,
no automation is enabled without a checked first run, nothing is pre-approved to send.

---

## What is deliberately not filled in

These are marked `[NEED: x]` in `entities/merraine-icp.md` and will stay blank until
you answer. A guess here poisons every downstream draft.

- **Which industries Merraine actually focuses on.** We can derive a first pass from
  your Spear data, but you should confirm it.
- **Three named placements or clients** we may cite as proof.
- **Fee and capacity** — what a search costs and how many you can run at once.
- **Your suppression list** — who is already inside an open search.
