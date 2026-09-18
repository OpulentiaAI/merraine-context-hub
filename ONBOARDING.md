# Start here

**Jeremy — paste the block below into a new Opulent session. That is init.**

The agent fills the hub the way Spear was pulled: every live service,
then contacts, then voice, then clocks. You only do the auth clicks.

---

## The paste block

```text
Read this repository as your operating context: merraine-context-hub.

You are running Jeremy Sanchez's Opulent account ([OPERATOR_EMAIL: private configuration],
Merraine Group, leadership search). Mount this hub, then immediately run
runbooks/hub-init.md. Do not stop after reporting state.

Start by reading, in this order:
  inject/hub-inject.md
  runbooks/hub-init.md
  entities/workspace-now.md
  entities/connection-inventory.md
  catalogs/automation-dictionary.md
  catalogs/playbook-catalog.md
  entities/icp-context.md
  entities/jeremy-writing-prefs.md

Then init, this session, in this order:
  1. Fresh-read what is actually connected. Do not guess.
  2. Validate, then mount when I type send
     (CONFIRM=send python3 scripts/materialize.py --apply).
  3. Extract every connected service that has no receipt.
     Spear is already done — do not pull it again.
     Notion, Parallel, and Mesa are connected and not extracted. Pull them
     the same way Spear was pulled (codemode + MCP, coordinator + worker,
     FILE-INDEX, hash).
  4. Populate contacts from the Spear export now. When Gmail is on, run
     extractions/email-communications-extraction.md in the same session
     and merge the relationship graph.
  5. Train writing style from 15–30 of my sent mails that got a reply.
     Until Gmail is on, use research/jeremy-voice.md and
     entities/jeremy-writing-prefs.md.
  6. Create the day-one automations as Disabled drafts. This repository
     has no executor or cost-authorizing dispatcher, so do not Enable
     a clock from here. First-open is a future external-executor gate.
  7. Write init-receipt.json. Resume only what is still blockedOn.

Standing rules, non-negotiable:
- Nothing sends, pays, publishes, or contacts a person unless I type "send"
  in that moment.
- Emailing the daily hiring scan to my work inbox is delivery to me,
  not outbound. Do not store that address in this public hub.
- Every claim carries a resolvable source. Empty results are UNVERIFIED,
  never zero.
- "completed" is not proof. Open the artifact.
- Three things come to me: a secret, a payment, a send. Decide everything
  else yourself.
```

---

## What init does in the first session

| Step | What lands | You do |
|---|---|---|
| Mount | This hub attached to Default Workspace | Type `send` once |
| Extract live services | Notion, Parallel, Mesa (and any other connected tool) as artifacts + receipts | Nothing if already connected |
| Skip Spear | 57 Drive files and `personal-context-hub.zip` stay the source of record | Nothing. Do not re-run it. |
| Contacts | `contacts-from-spear.json`, then `relationship-graph.json` from mail, merged to `contacts-index.json` | Gmail click, if it is still off |
| Voice | `voice-profile.md` from replied-to sent mail, standing rules on `jeremy-writing-prefs` | Nothing. One-offs are not saved. |
| Triggers | Parallel monitor procedures exist. Live monitors need an extracted Parallel surface and an external executor. | Nothing |
| Automations | Day-one jobs written here as **Disabled, non-runnable drafts**. This repo cannot Enable a clock. | Nothing until an external dispatcher exists |

The procedure is [[hub-init]]. The extraction pattern is
[[connected-tool-extraction]]. Mail is
[[email-communications-extraction]]. Clocks go through
[[first-open-gate]].

---

## What you will be asked to authorise

Clicks only. The agent keeps extracting everything else while a click
is pending, then uses the new connector in the same session.

| # | What | Where | What it unblocks |
|---|---|---|---|
| 1 | **Gmail** | Settings → Connectors | Contacts from mail, voice from sent mail, suppression list, unibox. Two earlier logins timed out. |
| 2 | **Sales Navigator seat** | LinkedIn, about $99/mo | Not a build. Five filters. See `research/sales-navigator-filters.md` |
| 3 | **Apollo** (optional) | Connectors | Trial expired. If it needs a paid plan, drop it. |
| 4 | **Gojiberry** (on request) | Say "wire up Gojiberry" | The agent creates the account. Only the LinkedIn connect needs you. |

Already connected, and init must extract them now (except Spear):

- **Spear** — 131 tools. Export already in Drive. Skip the pull. Index the prospects.
- **Notion** — 42 tools. Shepherd Search Group / Merraine. Pull it.
- **Parallel Monitor** — watches. Pull the monitors, then register the day-one ones.
- **Mesa** — workspace versions and webhook jobs. Pull it.

---

## Day-one clocks

Written in this repository as Disabled drafts. They are not runnable
here. `runbooks/first-open-gate.md` is the future external-executor
gate; this repo has no dispatcher.

**Drafts that would be first-open candidates later**

- **Signal-triggered outbound** — weekday morning. Who became a buyer overnight, with a cited opener waiting.
- **Awards and recognition monitor** — Monday. Forbes, Crain's Chicago, Crain's New York, the business journals. A named congratulations per honoree.

**Drafts that stay off until you ask, and stay off here regardless**

- Connector health, sales motion board, routine + transcript healthchecks, hub self-extension.
- Unibox triage — only after Gmail is on.
- Email / style / sequence / social / newsletter jobs — written, off.

The daily CFO / VP+ hiring scan already has a procedure
(`runbooks/daily-hiring-scan.md`). It is not on a clock. It is not an
executor. Say when you want it scheduled outside this repo.

Detection is specified as Parallel events, not a daily poll that finds
nothing. See `runbooks/parallel-monitor-scheduling.md`. Parallel is
connected and not extracted.

---

## Your six asks, and where each one landed

This public hub holds **typed knowledge, procedures, and disabled
automation drafts**. It does not run them. There is no executor or
cost-authorizing dispatcher in this repository. Several sources remain
authorization-blocked. See `docs/integration-status.md` and
`runbooks/first-open-gate.md`. Recording the six asks is not acceptance
that they are live.

| Your ask | Where it lives | State |
|---|---|---|
| Universal search across LinkedIn, Google, company sites | `runbooks/universal-search.md`, `runbooks/daily-hiring-scan.md`, typed `gtm.search-run` fixtures | Procedure and synthetic fixtures. No live search executor. Gmail is not connected. |
| LinkedIn Sales Navigator | `research/sales-navigator-filters.md` | Procedure only. Buy the seat — do not build it. |
| Spear for sequencing, replies, auto-prospecting | `entities/connectors/spear.md`, `playbooks/sequencing.md`, `playbooks/replies.md` | Typed connector note and procedures. Extracted payloads are not in this public repo. Automations are disabled drafts. |
| Enrichment: name → email, phone, title history | `playbooks/enrichment.md`, `automations/contact-enrichment-pass.md` | Procedure and a disabled draft. Not executable here. |
| Market signals: raises, exec moves, job postings | `signals/`, `automations/signal-triggered-outbound.md` | Typed signal catalog and a disabled draft. Parallel is connected and not extracted. No dispatcher. |
| Awards tracker: Forbes, Crain's, regional journals | `automations/awards-recognition-monitor.md`, `signals/award-recognition.md` | Typed signal and a disabled draft. Not standing, not runnable here. |

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
runbooks/     how the work actually runs, including hub-init
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
