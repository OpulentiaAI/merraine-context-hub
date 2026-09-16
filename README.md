# merraine-context-hub

Jeremy Sanchez's working context for **Merraine Group** — leadership search —
running on Opulent.

Built on [arsumbris](https://arsumbris.ai): folders of markdown and YAML that
an engine reads as one typed, queryable graph. A field that should hold a
citation cannot quietly hold a guess.

**New here?** Open [ONBOARDING.md](ONBOARDING.md). One paste block, then the
auth clicks that are actually yours.

If you are mounting this in Ars Umbris, see [docs/open-in-au-host.md](docs/open-in-au-host.md).
On Linux, [docs/running-on-linux.md](docs/running-on-linux.md).

## What it holds

| Directory | What is in it |
|---|---|
| `type/` | The ontology. Orgs, people, signals, automations, extractions, briefs. |
| `entities/` | Merraine, Jeremy, the workspace, connectors, accounts in motion. |
| `signals/` | Seven ranked buying triggers. |
| `extractions/` | How to pull a tool or a mailbox into the hub. |
| `automations/` | Paste-ready prompts. All Disabled until a first output is opened. |
| `runbooks/` | How the work actually runs, including the daily hiring scan. |
| `research/` | Voice, Spear vocabulary, and outside plays we adopted. |
| `skills/`, `inject/`, `profiles/` | What a session sees. |
| `scripts/` | `audit.sh`, `materialize.py`, `validate.py`. |

## Status

As of 16 September 2026, read live from the workspace:

- Spear, Notion, Parallel, and Mesa are connected.
- Spear is already extracted. Do not run that job again.
- Gmail is not connected. That is the unlock for mailbox extraction.
- No automation is Enabled. The validator fails the build if one is.

## The loop

```
scripts/audit.sh                 read the workspace, write an evidence bundle
python3 scripts/materialize.py   dry-run the hub install
python3 scripts/validate.py      type check, link check, surface check
```

Reads are free. Writes require `CONFIRM=send`.
