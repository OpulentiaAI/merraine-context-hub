---
type: gtm.brief
tldr: What is already in this workspace
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "drive:listByUserInternal, knowledgeRunbooks:listKnowledge, triggers:listAutomationsInternal, memoryBlocks:listForUser, 2026-09-16"
kind: workspace
---

# What is already here

## Done

- **Spear export.** 57 Drive files including `personal-context-hub.zip`,
  FILE-INDEX, prospect JSON, trigger JSON, campaign JSON. The authorized
  owner export is already in Drive. Do not extract Spear again.
- **Spear, Notion, Parallel, Mesa** are connected. See [[connection-inventory]].
- **Crustdata enrichment** has already resolved Farmers Fridge.
- **A daily CFO / VP+ hiring scan** already has a written procedure and a
  10 September baseline. It is not on a clock yet. See [[daily-hiring-scan]].
- **Boston week is this week.** HubSpot UNBOUND and Startup Boston Week.
  Remaining days: [[boston-week-2026]].

## Not done

- This hub is **not mounted** on Default Workspace yet. Sessions will not
  see these files until `scripts/materialize.py` is applied.
- **Init has not run.** There is no `init-receipt.json`. First session
  runs [[hub-init]].
- **Notion, Parallel, and Mesa are connected and not extracted.** Pull
  them the same way Spear was pulled. Do not re-extract Spear.
- **Contacts are not indexed.** The Spear export is in Drive. Mail has
  not been swept.
- **Voice is the standing file only.** [[jeremy-voice]] is in force until
  Gmail lands 15–30 replied-to sent mails.
- **No saved automations.** Signal outbound and the awards monitor are
  written here and still Disabled.
- **Gmail is not connected.** Mailbox extraction is waiting on that click.
- The ICP still has open questions only you can answer. See [[merraine-icp]].

## Threads that already ran

From recent usage on this account:

| Thread | What happened |
|---|---|
| Search the web (Indeed, LinkedIn, Crain's) | Two Gmail logins timed out. One later run completed. |
| Spear MCP context hub extraction (luna fast) | Completed. This is the export in Drive. |
| Earlier Spear extraction reruns | Stopped. Do not resume them. |
| Earlier routing and model tests | Not Merraine work. Leave them. |

If a thread is a retry of the finished Spear export, or a model test, leave
it alone.
