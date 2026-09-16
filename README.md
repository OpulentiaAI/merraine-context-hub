---
type: au.engine.readme::au-engine
tldr: "Jeremy Sanchez's Merraine GTM hub. Open ONBOARDING.md, then start here.md. Extend it by adding typed notes under type/ and the matching folder."
---

# Repo Overview

Typed working context for Jeremy Sanchez at **Merraine Group** — leadership
search — running on Opulent. Built on [arsumbris](https://arsumbris.ai):
folders of markdown and YAML that an engine reads as one typed, queryable
graph. A field that should hold a citation cannot quietly hold a guess.

## What this is

A go-to-market graph for Merraine: living ICP, ranked signals, specialist
playbooks, skills, automations, extractions, and the voice that drafts must
match. The product surface is Jeremy's. Operator Convex notes stay under
`ops/` and never materialize onto the workspace.

| Directory | What is in it |
|---|---|
| `type/` | The ontology. Orgs, people, signals, automations, extractions, briefs. |
| `entities/` | Merraine, Jeremy, the workspace, connectors, accounts in motion. |
| `signals/` | Ranked buying triggers, including category conversations. |
| `playbooks/` | Specialist modules — signals, ICP, score, replies, and the rest. |
| `extractions/` | How to pull a tool or a mailbox into the hub. |
| `automations/` | Paste-ready prompts. All Disabled until a first output is opened. |
| `runbooks/` | How the work actually runs, including the daily hiring scan. |
| `research/` | Voice, Spear vocabulary, and outside plays we adopted. |
| `skills/`, `inject/`, `profiles/` | What a session sees. |
| `scripts/` | `audit.sh`, `materialize.py`, `validate.py`. |

As of 16 September 2026, read live from the workspace:

- Spear, Notion, Parallel, and Mesa are connected.
- Spear is already extracted. Do not run that job again.
- Notion, Parallel, and Mesa are connected and not extracted. Init pulls them.
- Gmail is not connected. That is the unlock for mailbox contacts and voice.
- No automation is Enabled. The validator fails the build if one is.

## How to use this

**New here?** Open [ONBOARDING.md](ONBOARDING.md). One paste block starts
[[hub-init]]: extract every live service, populate contacts, train voice,
stand up day-one clocks. The auth clicks that are actually yours happen
inside that session. Then open [start here.md](start%20here.md).

If you are mounting this in Ars Umbris, see [docs/open-in-au-host.md](docs/open-in-au-host.md).
On Linux, [docs/running-on-linux.md](docs/running-on-linux.md).

```
scripts/audit.sh                 read the workspace, write an evidence bundle
python3 scripts/materialize.py   dry-run the hub install
python3 scripts/validate.py      type check, link check, surface check
```

Reads are free. Writes require `CONFIRM=send`. Nothing sends, pays,
publishes, or contacts a person unless Jeremy types that word in the moment.

## How to extend this

Add a type under `type/` that extends `idea::au-base-types` plus `gtm.managed`
when the note is owned. Put instances in the matching folder (`signals/`,
`playbooks/`, `automations/`, …). Required body sections are H1 headings
matching the type. Quote YAML `[[wikilinks]]`. Then:

```
python3 scripts/validate.py --catalog
```

That rewrites the catalogs from what actually exists. Downstream repos
import these types as `gtm.<name>::merraine-context-hub`.
