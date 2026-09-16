---
type: gtm.extraction
tldr: Email, communications and relationship extraction
status: blocked
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Designed for this engagement. Blocked on [[gmail]] until OAuth completes."
sourceSystem: "Jeremy Sanchez's connected mailbox"
accessPath: mcp
requiresAuth: "yes"
authOwner: Jeremy Sanchez
method: "read-only mailbox sweep, then graph construction"
coordinatorRoute: "ai-gateway/openai/gpt-6-astra"
workerRoute: "gemini-3.8-flash"
outputs:
  - "relationship-graph.json"
  - "communication-patterns.md"
  - "reconstructed-pipeline.json"
  - "voice-profile.md"
  - "suppression-list.json"
idempotency: "Keyed on mailbox message id high-water mark in extraction-receipt.json. Re-runs are incremental."
evidence: []
---

# Email, communications and relationship extraction

The single richest source Merraine has, and it is entirely unexploited. **Blocked
until [[gmail]] is connected** — that is one user click and it unlocks this whole file.

## Preconditions

- `gmail` connector reads `isConnected: true` with scopes listed.
- **Read-only.** This extraction never sends, replies, archives, or labels.
- Jeremy Sanchez has confirmed the mailbox is his business mailbox.

## Procedure

### 1. Relationship graph

Sweep sent and received mail. For every human correspondent build a `gtm.person`
with: first contact date, last contact date, total threads, reply latency both
directions, and who initiated. Derive `relationshipStrength`:

- **client** — an active thread inside a paid engagement
- **active** — exchanged mail both ways in the last 90 days
- **warm** — he wrote, they replied, ever
- **aware** — he wrote, no reply
- **cold** — inbound only, or a single touch

Reply latency is the honest strength signal. Someone who answers him in an hour is
a different asset than someone who answers in nine days.

### 2. Communication patterns

Extract, do not invent:

- Subject-line shapes that actually got replies, with reply rate per shape.
- Median length of his emails that got a reply vs those that did not.
- Opening and closing lines he genuinely uses.
- Time-of-day and day-of-week send distribution against reply rate.
- Threads that died, and the last message before they died.

### 3. Voice profile

Sample **15-30 sent messages that received replies**. Write `voice-profile.md`
capturing his actual sentence length, contraction use, greeting, sign-off, and how
he asks for a meeting. Every future draft is generated against this file and then
checked with [[slop-patterns]]. Never synthesise a voice from a persona description.

### 4. Pipeline reconstruction

Merraine's real pipeline is in his mailbox, not in a CRM. Identify threads that
progressed through recognisable states — intro, scoping, shortlist, interview,
placement, invoice — and rebuild them into `gtm.pipeline` stages with real median
durations. That produces `reconstructed-pipeline.json`, which becomes the baseline
the automations write against.

### 5. Suppression list

Anyone in an open search, anyone who asked not to be contacted, anyone mid-negotiation.
This file is a **hard filter** on every automation in this hub.

## Proof of delivery

- `relationship-graph.json` row count equals the distinct-correspondent count you
  can reproduce from a second independent sweep.
- Every `relationshipStrength` above `aware` traces to at least one message id.
- `voice-profile.md` quotes at least 15 real sent messages by id.
- No message was sent, modified, or labelled. Prove it from the tool log.

## Do not repeat if

An `extraction-receipt.json` exists with a message-id high-water mark. Re-runs are
incremental from that mark, never a full re-sweep.
