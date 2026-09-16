---
type: gtm.automation
tldr: Transcript healthcheck
status: draft
owner: Jeremy Sanchez
updated: 2026-09-14
surface: jeremy
provenance: "Pattern from x.ai dr-eggbot-v2 standing healthchecks, rebuilt on Opulent primitives"
slug: merraine-transcript-healthcheck
uses: []
schedule:
  tldr: weekday cron
  kind: cron
  expression: "44 8 * * 1-5"
  timezone: America/Chicago
  source: opulent-native
mode: read-only
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 3
producesArtifact: "friction-scan-<date>.md"
sourceTemplate: "dr-eggbot-v2 transcript-healthcheck"
loopGuard: "If today's friction scan exists, stop. If there is nothing to propose, stay silent."
---

# Transcript healthcheck

# Overview
Mines this account's own turn history for friction and proposes fixes to the hub.
**It proposes; it never applies.** This is how the hub improves itself without
anyone deciding to sit down and improve it.

The borrowed shape is dr-eggbot-v2's two standing healthchecks: a weekday friction
scan and a Monday waste audit, both silent when there is nothing worth saying, and
neither allowed to create anything until a human picks from the report.

## Specifications

- Output is a list of `gtm.improvement` proposals, each with evidence
- `decision` is always `proposed` on write
- Silence is a valid and successful run

# Prompt
```text
Create an Opulent automation named "Merraine transcript healthcheck".

Trigger: weekdays at 8:44 AM America/Chicago.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Mine yesterday's sessions on this account for friction, and propose improvements to the Merraine context hub. Propose only. Change nothing.

IMPORTANT: If today's friction scan already exists, stop. If you find nothing worth proposing, write nothing and end quietly. Silence is a successful run.

1. Read the sessions and agent runs on this account from the last 24 hours.
2. Look for exactly these frictions, and record the run id and turn for each:
   - a step that was retried more than twice with the same error
   - a tool call that returned nothing and was not retried differently
   - a run that stopped blocked_on_user_action for something a human did not need to decide
   - an instruction the agent visibly misread, and what wording caused it
   - a fact asserted without a citation
   - a route that failed and what was used instead
   - work that duplicated something already delivered
3. For each friction write one proposal as a gtm.improvement: observedFriction, evidence (run id plus the exact error or quote), proposal, targetFile in the hub, changeKind, estimatedSaving, decision: proposed.
4. Group proposals by targetFile so a human can accept a whole file's worth at once.
5. Write "friction-scan-<date>.md". Do not edit any hub file. Do not create automations. Do not restart any run.
6. If two or more proposals point at the same hub file for the third day running, say so explicitly at the top. That is a structural problem, not a wording problem.

CAUTION: Propose only. Never apply a change, never restart a run, never contact anyone. An empty scan is a good outcome, not a failure to report.
```

# Forbidden Actions
- Do not apply a proposal
- Do not create anything from the report until a human picks
- Do not report "no issues" as a message; stay silent instead
