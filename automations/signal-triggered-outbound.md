---
type: gtm.automation
tldr: Merraine signal-triggered outbound
status: draft
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "Adapted from OpulentiaAI/gtm-agent-automations agents/gtm/outbound/signal-triggered-outbound.md"
slug: merraine-signal-outbound
uses:
  - "[[spear]]"
  - "[[parallel]]"
  - "[[gmail]]"
  - "[[notion]]"
schedule:
  tldr: weekday cron
  kind: cron
  expression: "30 6 * * 1-5"
  timezone: America/Chicago
  source: opulent-native
mode: draft-then-wait
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 5
producesArtifact: "signal-digest-<date>.md"
sourceTemplate: "gtm/outbound/signal-triggered-outbound.md"
loopGuard: "If a digest for today already exists in the workspace, stop."
---

# Merraine signal-triggered outbound

# Overview
The core of Jeremy Sanchez's ask. Every weekday morning, find who became a buyer
overnight and have a cited opener waiting.

## What's Needed From User

- [[spear]] connected (done, 131 tools)
- [[gmail]] connected — **currently blocking**, needed for voice and suppression
- [[merraine-icp]] reviewed and its `[NEED: x]` gaps filled
- Destination for the digest: workspace artifact, or a Notion page he names

# Procedure
1. Stand up per [[first-open-gate]]. Create **Disabled**.
2. Run one manual tick.
3. Open every cited URL yourself before Enabling.

## Specifications

- Postcondition: one digest artifact, every row citable, zero sends
- Mode holds: draft-then-wait, human approval before send, fail closed
- Empty search is `UNVERIFIED`, never an invented zero

# Prompt
```text
Create an Opulent automation named "Merraine signal-triggered outbound".

Trigger: weekdays at 6:30 AM America/Chicago.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Find who became a buyer for an executive search overnight, and leave a cited opener waiting for approval.

IMPORTANT: If a signal digest for today already exists in this workspace, stop. Do not create a second one. A second artifact can retrigger this run.

1. Read merraine/entities/merraine-icp and every file under merraine/signals. Those define what counts as intent and what only looks like it.
2. Load the named-account seed list from the Spear prospect extraction already in this workspace (FILE-INDEX -> personal-context-hub). Do not re-extract Spear.
3. For the past 24 hours, gather signals from connected tools only:
   - senior job postings aged past 30 days, or 3+ senior reqs open at one org
   - funding rounds closed in the last 60 days
   - executive arrivals and departures in the last 90 days
   - Parallel monitor events that fired against a merraine/signals watch
4. Drop any signal you cannot cite with a resolvable URL, filing, or platform event id. No signal, no row. An empty result is UNVERIFIED, not zero.
5. Score each row using the rank in its signal file. Keep the top 15.
6. Record the signal in the source's own words plus its date. Never paraphrase a quote into something stronger.
7. Enrich the likely buyer (CEO, COO, CHRO, VP People) with Monid first, Crustdata only where Monid returns nothing. Leave fields blank when both miss. Record actual spend.
8. Apply hard filters: anyone contacted in the last 90 days, anyone in an open Merraine search, anyone on the suppression list, and every disqualifier in the ICP file.
9. For each surviving row write one opener under 80 words that: quotes the cited event in its first sentence, says in one sentence what Merraine sees at that moment, asks one question, and closes giving them permission to pass. Use merraine/research/voice-profile if it exists; otherwise use the ICP voice fields.
10. Run merraine/research/slop-patterns against every draft. Two trips means rewrite.
11. Create the sequence in Spear as a PAUSED campaign. Do not enable send.
12. Write the artifact "signal-digest-<date>.md" with columns: account, signal, source URL, signal date, enrichment status, draft, approval checkbox. Mark every draft send_ready: false.
13. Log: rows found, rows kept, rows dropped with reasons, spend, artifact hash.

CAUTION: Never auto-send outbound. Never invent a signal, an email, a headcount, or a quote. If a tool returns nothing, say nothing was found.
```

# Forbidden Actions
- Do not send, enroll, or enable a campaign
- Do not re-extract Spear
- Do not infer an industry focus from a company's website styling
- Do not Enable the clock before a first-open you personally checked
