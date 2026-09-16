---
type: gtm.extraction
tldr: Spear tool extraction
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Already executed. Confirmed again 2026-09-16: personal-context-hub.zip and 57 Drive files still present. Do not repeat."
sourceSystem: Spear
accessPath: mcp
requiresAuth: "no"
authOwner: already connected
method: "codemode + mcp access"
coordinatorRoute: "luna-fast"
workerRoute: "deepseek worker"
outputs:
  - "57 drive files"
  - "personal-context-hub.zip"
  - "FILE-INDEX artifact rows"
idempotency: "If personal-context-hub.zip exists and is 'ready', this has run. Do not repeat."
evidence:
  - claim: "57 drive files + personal-context-hub.zip + FILE-INDEX, from completed luna-fast + deepseek worker runs 22:18-22:34"
    tldr: "57 drive files + personal-context-hub.zip + FILE-INDEX, from completed..."
    origin: "capy:jam_WJH16K8HT2KG346Z09FH84GJM4/pre-resume-verification.md"
    observedAt: 2026-09-14
    method: read
    verifiedBy: parent
    confidence: verified
---

# Spear tool extraction

**This is the reference pattern for pulling any connected tool's full dataset into
the hub.** It is already done for Spear. Read it before extracting anything else.

# Preconditions
- The tool is connected as an MCP connector on the account, with a non-zero tool count.
- You have confirmed the tool count with a read-only connector discovery first.
- No prior extraction artifact exists (see **Do not repeat if**).

# Procedure
1. Read the connector's tool surface. Do not guess tool names.
2. Run the extraction through **codemode + MCP access**, not UI scraping. The
   operative instruction that worked verbatim was:
   *"extract all of our data on prospects and triggers from spear mcp using codemode and mcp access."*
3. Topology: a **coordinator** on a fast route with a **worker** doing the pulls.
   Pass both routes explicitly. Do not let `continueThread` pick a default.
4. Write outputs as **durable artifacts** into the account's context hub, not as
   chat text. Produce a `FILE-INDEX` so later runs can tell what landed.
5. Zip the corpus into a single retrievable bundle.
6. Record file count, artifact row count, and the bundle hash.

# Proof of delivery
`completed` status is **not** proof. Proof is:

- A file count you can list.
- Artifact rows in the account's storage.
- A bundle whose hash you recomputed after download.

For Spear that is: 57 drive files, `personal-context-hub.zip` in `ready` state,
and FILE-INDEX artifacts.

# Do not repeat if
Three threads on this account carry duplicate Spear-extraction instructions created
**after** delivery, all with zero tool executions:

- `m5703g57agq4` — Workflow: Untitled Workflow, started 23:01, `toolExecutionRollup.total = 0`
- `m57503x9f1pf` — API: Extract Spear MCP prospects/triggers, zero runs
- `m57daagyajat`, `m57eyzess12p` — stopped rerun threads, no provenance

Resuming any of them re-extracts what already exists. The standing decision is
**do not re-extract Spear.**
