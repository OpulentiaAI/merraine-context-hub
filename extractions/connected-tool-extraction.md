---
type: gtm.extraction
tldr: Pull a newly connected tool into this hub
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Same pattern as [[spear-tool-extraction]], which already delivered"
sourceSystem: "any connected MCP or native integration"
accessPath: mcp
requiresAuth: "yes"
authOwner: Jeremy Sanchez
method: "codemode + mcp access, coordinator + worker"
coordinatorRoute: "luna-fast"
workerRoute: "gemini-3.8-flash"
outputs: ["<tool>-export/ directory", "<tool>.md context file", "FILE-INDEX row", "extraction-receipt.json"]
idempotency: "Check FILE-INDEX for a <tool> entry before starting. If present with a hash, stop."
evidence: []
---

# Connected tool extraction

Run this for every tool you authorise, in connector order. Same pattern as
Spear, with the tool name as the only change. [[hub-init]] runs this for
every connected service that has no receipt. Spear is the exception: skip it.

# Preconditions
- Connector reads `connected: yes` with a tool count > 0 in a fresh discovery.
- `FILE-INDEX` has no completed entry for this tool.
- Budget ceiling set. Stop at $15 per tool with no artifact.

# Procedure
1. **Discover.** List the connector's tools and their input schemas. Save as
   `<tool>-tool-surface.json`. Never invent a tool name.
2. **Inventory.** Call the tool's list/search endpoints with the widest safe filter
   to learn total record counts *before* pulling. Save `<tool>-inventory.json`.
3. **Pull in bounded pages.** Cap tool calls per entity class. Bounding tool calls
   improves quality, not just cost — see [[agent-economics]].
4. **Normalise** into the hub ontology: records that are companies become
   `gtm.org`, people become `gtm.person`, triggers become `gtm.observation`
   pointing at an existing `gtm.signal`. Anything that does not map stays raw in
   `<tool>-export/`.
5. **Reconcile.** Compare every normalised row field-by-field against the raw
   response. Report: missing, extra, and field differences. Zero of each is the bar.
6. **Write** `<tool>.md` — a context file describing what this tool holds, what it
   is authoritative for, and what it must never be trusted for.
7. **Receipt.** `extraction-receipt.json`: record counts, tool calls used, spend,
   bundle hash, and the reconciliation result.

# Proof of delivery
A reconciliation showing **0 missing, 0 extra, 0 field differences** against the
raw source responses, plus a hash you recomputed after download. The Spear
export already in Drive met this bar. Every later tool has to meet it too.

# Do not repeat if
`FILE-INDEX` already has a `<tool>` entry with a hash and a nonzero record count.
A failed retry that started seconds after a successful run is a **programmatic
retry, not a new request** — do not treat it as unfinished work.
