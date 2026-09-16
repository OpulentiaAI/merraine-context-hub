---
type: gtm.runbook
tldr: Leftover notes already on Jeremy's account that must not be remounted
status: active
owner: operator
updated: 2026-09-16
surface: operator
provenance: "knowledgeRunbooks:listKnowledge + getKnowledge on 2026-09-16"
trigger: "Before materializing this hub or attaching existing knowledge ids"
audience: operator
escalateWhen:
  - "A write would archive a note Jeremy still uses"
  - "A note contains a secret and is about to be copied into this repo"
---

# Leftover knowledge hygiene

Jeremy's account already has 13 knowledge notes and 3 runbooks. They are
searchable. They are **not** attached to the workspace (`mounted_context: 0`).
Do not attach the leftover rows. Integrate the useful facts into this hub
instead, then mount the hub files.

## Keep using the facts, do not remount the row

| Name | Why the facts matter | Why the row stays unmounted |
|---|---|---|
| Jeremy Sanchez Profile (canonical) | Role, team, voice, clients | Written as a third-party dossier |
| Spear Site Notes | Trigger thesis, keyword set, profile id | Browser-quirk commentary |
| Boston September 2026 Travel & Events Guide | This week's calendar | Fine as a source; the hub has a cleaned brief |
| Session Log Sep 8 2026 (episodic) | First-sign-in history | Contains credential-handling narrative |

## Do not remount, do not copy verbatim

| Name | Why |
|---|---|
| Marketing & Channel Skills Index | Imported Vercel marketing-agent template. Not Merraine's voice. |
| Aside Memory Taxonomy & Write Rules | Another product's memory layout. |
| Aside Operating Defaults | Same. |
| Aside User Briefing (Jeremy Sanchez) | Short pointer into the other product's paths. |
| Opulent OS Platform Notes | Login-page and autofill diagnostics. |
| Workspace Connected Tools & MCP Audit | Internal connector diagnostics. |
| Spear AI MCP Integration & OAuth Quirks | Implementation defect notes. |
| Parallel Monitor Integration & Diagnostics | Secret names and routing-bug notes. |
| Crustdata API Configuration & Enrichment | Contains a live API key. Never copy that file into git. |
| Durable Memory Write Rules (runbook) | Migrated leftover. |
| Aside Operating Defaults (runbook) | Migrated leftover. |
| Working with Jeremy Sanchez (runbook) | Written as if Jeremy were the subject, not the user. |

## Procedure

1. Run `scripts/audit.sh`. Confirm `mounted_context` is still 0, or that only
   `merraine/*` names are attached.
2. Dry-run `python3 scripts/materialize.py`. It must list only product-surface
   files from this repo.
3. Do not pass leftover note ids into
   `workspaceEntities:attachContextForAgentInternal`.
4. If a leftover note must be archived later, that is a separate confirmed write.
   This file does not authorize it.

## Verification

- `scripts/validate.py` fails if product-surface files contain leftover-product
  names or internal commentary.
- A fresh audit after materialize shows only `merraine/` knowledge and runbook
  titles attached.
