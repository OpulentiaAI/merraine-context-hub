# merraine-context-hub

A typed, agent-native context hub for **Merraine Group** GTM, piloted end to end by
Opulent.

Built on [arsumbris](https://arsumbris.ai): folders of markdown and YAML that an
engine reads as one typed, queryable graph. Knowledge, types, skills and workflows
live together, so a field that should hold a citation cannot quietly hold a guess.

> **Running Ars Umbris?** [docs/open-in-au-host.md](docs/open-in-au-host.md) mounts this as a workspace.
> **New here? Read [ONBOARDING.md](ONBOARDING.md).** It is one paste block and four
> auth clicks.

## What it holds

| Directory | What is in it |
|---|---|
| `type/` | The ontology, subtyped off `au-base-types`. 23 types covering orgs, people, signals, sequences, automations, extractions, evidence. |
| `entities/` | Merraine, Jeremy Sanchez, the Opulent account, and every connector with its live state. |
| `signals/` | Seven ranked buying triggers. Each says how to detect it, how to disqualify it, and what it looks like when it lies. |
| `extractions/` | Runbooks for pulling a tool, a mailbox, or a relationship graph into the hub. |
| `automations/` | The automation dictionary: paste-ready Opulent prompts with triggers, cost ceilings and loop guards. |
| `runbooks/` | Operating procedures, including how this account is piloted through Convex prod. |
| `research/` | Outside tactics we adopted, each attributed, with the author's claims kept as the author's. |
| `skills/`, `inject/`, `profiles/` | What an Opulent session sees: triggered guidance, standing context, and agent profiles. |
| `scripts/` | The governed seam: `audit.sh`, `materialize.py`, `validate.py`, `pilot.sh`. |
| `evidence/` | Dated audit bundles and a per-call ledger. |

## The pilot loop

```
scripts/audit.sh          read production, write an evidence bundle
scripts/materialize.py    install the hub as Opulent knowledge + runbooks, mount it
scripts/validate.py       type check, link check, send-safety check
scripts/pilot.sh          the governed Convex seam every write goes through
```

Reads are free. Writes require `CONFIRM=send`. Every call is logged. The deployment
is pinned to `prod:confident-sheep-333` and the scripts refuse to run against
anything else.

## How it improves itself

Three automations close the loop:

- **`transcript-healthcheck`** — weekday scan of the account's own session history
  for friction: repeated retries, uncited claims, misread instructions. Proposes fixes.
- **`routine-healthcheck`** — weekly waste audit. Flags automations that fire and find
  nothing, spend that rose, artifacts nobody opened.
- **`hub-self-extension`** — turns accepted proposals and new extraction output into a
  reviewable patch against this repo.

All three propose. None apply. A human picks.

## Status

Nothing is Enabled. Every automation ships `enabled: no` and `firstOpenChecked: no`
by design — see `runbooks/first-open-gate.md`. The validator fails the build if that
invariant is ever broken.
