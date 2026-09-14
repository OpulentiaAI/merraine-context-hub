---
type: mcp.skill::au-mcp-sdk
name: running-an-extraction
description: "Pull a connected tool's full dataset, or a mailbox's communications and relationships, into this hub. Use when a new connector is authorised, when asked to extract or mine a tool, or when asked what data we already have. Triggers: extract, pull the data, mine his email, what's in Spear, ingest, import."
---

# Running an extraction

Read [[connected-tool-extraction]] for the generic pattern and
[[spear-tool-extraction]] for the proven reference.

Three rules that have already cost this account real money when ignored:

1. **`completed` is not proof.** Proof is a file count, artifact rows, and a hash
   you recomputed.
2. **Check for a prior delivery first.** Spear has three duplicate extraction
   threads with zero tool executions. Resuming one re-extracts what exists.
3. **A failed retry seconds after a success is a programmatic retry**, not
   unfinished work. Do not treat it as a resume candidate.

For the mailbox, read [[email-communications-extraction]]. It is blocked on
[[gmail]] and unlocks the most valuable asset Merraine has.
