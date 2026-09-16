---
type: gtm.runbook
tldr: First-session init. Extract, contacts, voice, clocks.
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Same pattern as [[spear-tool-extraction]]. One init, then receipts."
trigger: "First session on this hub, or whenever init-receipt.json is missing"
audience: jeremy-sanchez
escalateWhen:
  - "A connector needs Jeremy's login"
  - "Mounting the hub needs the confirm word"
  - "An extraction would write back to a live system"
  - "A person would be contacted"
relatedAutomations:
  - "[[signal-triggered-outbound]]"
  - "[[awards-recognition-monitor]]"
  - "[[connector-health-check]]"
  - "[[routine-healthcheck]]"
  - "[[transcript-healthcheck]]"
  - "[[unibox-triage]]"
  - "[[sales-motion-board]]"
  - "[[hub-self-extension]]"
---

# Hub init

This is the first session. Treat the workspace as a personal context hub
and fill it. Do not stop after a status report. Do not wait for a second
ask to extract a tool that is already connected.

Spear already ran this pattern. Every other live service gets the same
treatment. Mail, once connected, becomes contacts and voice. Clocks are
created Disabled and gated.

# Procedure

## 0. Ground
1. Fresh-read [[workspace-now]] and [[connection-inventory]]. Do not
   reason from memory.
2. List every connected MCP and native integration with a live tool
   count. Save `connector-surface-<date>.json`.
3. Read `FILE-INDEX` and any `extraction-receipt.json`. A hash plus a
   nonzero count means that tool is done.
4. Do not remount leftover knowledge notes. Do not resume a Spear
   rerun thread. See [[spear-tool-extraction]].

## 1. Mount
1. `python3 scripts/validate.py`. Fix owned errors before anything
   installs.
2. Dry-run `python3 scripts/materialize.py`. Show Jeremy the file list.
3. Mount only when he types the confirm word:
   `CONFIRM=send python3 scripts/materialize.py --apply`.
4. Attach the Jeremy-facing files to Default Workspace. Operator files
   under `ops/` stay off the workspace.

## 2. Extract every connected service
For each connected tool with no receipt, run [[connected-tool-extraction]]
the way Spear was pulled: discover the real tool names, inventory
counts, pull in bounded pages, normalise, reconcile, write `<tool>.md`,
write the receipt. Coordinator plus worker. Routes named explicitly.

Default order on this account:

| Tool | State | What to pull |
|---|---|---|
| [[spear]] | Done | Skip. 57 Drive files and `personal-context-hub.zip` already exist. |
| [[notion]] | Connected, not extracted | People, companies, notes, databases in Shepherd Search Group / Merraine. |
| [[parallel]] | Connected, not extracted | Monitors, watches, recent events. |
| [[mesa]] | Connected, not extracted | Workspace revisions and webhook jobs. |
| Any other live connector | If the count is > 0 | Same pattern. |

Native integrations ([[parallel]], [[mesa]]) may show MCP tool count 0
and still be on. Extract through their native list/watch/job APIs, not
by waiting for an MCP catalog.

Cap $15 per tool with no artifact. `completed` is not proof. Proof is a
file count, artifact rows, and a hash you recomputed.

## 3. Populate contacts
1. Index the existing Spear export into hub people and orgs. Do not
   call Spear again. Your profile: 1,314 prospects. Reid's: 1,639.
   Write `contacts-from-spear.json` plus a FILE-INDEX row.
2. If [[gmail]] is off, ask for that one click now. Keep extracting
   everything else while it is pending. The moment it reads connected,
   run [[email-communications-extraction]] in the same session.
3. From mail: `relationship-graph.json` (every human correspondent,
   warmth from reply latency), `suppression-list.json`, and
   `reconstructed-pipeline.json`. Read-only. Nothing is sent, filed,
   or labelled.
4. Merge Spear + mailbox into `contacts-index.json`. Same person
   across sources is one row. Suppression wins.
5. Enrich keepers that pass [[icp-context]] through Crustdata. Leave
   blanks. Do not invent a phone or an email.

## 4. Train writing style
1. Load [[jeremy-voice]] and [[jeremy-writing-prefs]] now. Drafts may
   use them before the mailbox lands.
2. Once mail is in, sample 15–30 **sent messages that received a
   reply**. Write `voice-profile.md` with sentence length, greeting,
   sign-off, how he asks for a meeting, and quoted message ids.
3. Fold only durable rules into [[jeremy-writing-prefs]]. One-offs die
   with the draft. See [[holding-writing-prefs]].
4. Proof: rewrite one real sent mail through [[style]] and
   [[keeping-prose-clean]]. The rewrite must still sound like him.
   Save `style-proof-<date>.md`. `sendReady: no`.

## 5. Triggers and automations
Create from [[automation-dictionary]]. Every one starts **Disabled**.
No clock until [[first-open-gate]] passes.

Create immediately, this session:

| Automation | Why it is day-one |
|---|---|
| [[signal-triggered-outbound]] | Who became a buyer overnight, cited opener waiting. |
| [[awards-recognition-monitor]] | Named congratulations for a real honoree. |
| [[connector-health-check]] | What is still connected. |
| [[sales-motion-board]] | The day's run plan. |
| [[routine-healthcheck]] | Friction in session history. Proposes only. |
| [[transcript-healthcheck]] | Waste in transcripts. Proposes only. |
| [[hub-self-extension]] | Turns an accepted proposal into a reviewable patch. |
| [[unibox-triage]] | Only after Gmail is on. |

Stand Parallel monitors, not crons, for detection. See
[[parallel-monitor-scheduling]]. Point each at one file in
[[signal-catalog]]: senior role, funding, exec move, award. One
synthetic fire before the monitor is trusted.

First-open **signal outbound** and **awards** on one manual tick each.
Enable those two clocks only after Jeremy has opened the artifact.
Leave the rest Disabled.

Do not invent a clock for [[daily-hiring-scan]] unless he asks.
Content and social queues stay created-Disabled until he names extra
surfaces on [[jeremy-writing-prefs]].

## 6. Receipt
Write `init-receipt.json` in the same session:

```
connected: [name, toolCount]
extracted: [tool, fileCount, hash, skippedReason]
contacts: {spear, mailbox, merged, suppressed}
voice: {source, sampleIds, prefsUpdated}
automationsCreated: [slug, enabled]
monitors: [signal, monitorId, proven]
blockedOn: [click or confirm still needed]
```

A later session that sees this receipt does not re-init. It resumes
only the `blockedOn` rows.

# Verification
- Spear was not pulled again.
- Every connected tool with count > 0 has a receipt or a written skip.
- `contacts-index.json` exists. Suppression rows have a source.
- Voice is either the live mailbox sample or an explicit "mailbox
  pending" note pointing at [[jeremy-voice]].
- Day-one automations exist as Disabled rows. At most the two
  first-opened clocks are Enabled.
- `init-receipt.json` is present and the hashes recompute.
- No send, no label, no publish, no live write-back.

# Failure branches
| Symptom | Do this |
|---|---|
| An MCP connector count is 0 after a settings page said on | Trust the live count. Record it. Do not extract. |
| A native integration (Parallel, Mesa) shows MCP count 0 | Still extract. Use the native list/watch/job surface. |
| Gmail click is still pending | Finish Notion, Parallel, Mesa, Spear index, and Disabled clocks. Resume mail the moment it connects. |
| Notion or Mesa pull fails twice the same way | Write the error on the receipt. Do not loop. Continue the other tools. |
| Materialize has no confirm word | Keep extracting to artifacts. Do not mount. |
| First-open tick invents a row or a URL | Fail the tick. Do not Enable. |
| A rerun thread for Spear is offered | Leave it. The export already exists. |
