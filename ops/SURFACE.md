# Product surface

Jeremy's Opulent workspace may only receive files this hub marks as Jeremy-facing.

## Rule

- Files under `entities/`, `signals/`, `pipelines/`, `playbooks/`, `automations/`,
  `extractions/`, `runbooks/`, `catalogs/`, `research/`, `skills/`, and `inject/`
  are the product surface. `scripts/materialize.py` installs only those directories.
- `ops/` is operator-only. It is never materialized. It holds identity traps,
  Convex function catalogs, and leftover-knowledge hygiene.
- `evidence/` is an audit ledger, not context. Do not attach it to the workspace.
- A file that names an internal owner, a deploy key, or another product's memory
  taxonomy does not belong on the product surface.

`scripts/validate.py` fails the build if a product-surface file contains the
forbidden phrases listed there.

## How to add a file

1. If Jeremy or his agent should see it in Opulent, put it in a product directory
   and set `surface: jeremy`.
2. If only a hub operator needs it, put it in `ops/` and set `surface: operator`.
3. Run `python3 scripts/validate.py` before committing.
