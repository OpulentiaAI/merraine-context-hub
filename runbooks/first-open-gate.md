---
type: gtm.runbook
tldr: First-open gate
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "OpulentiaAI/gtm-agent-automations agents/PLAYBOOK.md and agents/gtm/README.md"
trigger: "Before enabling any automation in this hub"
audience: jeremy-sanchez
escalateWhen:
  - "An automation cannot produce a checkable first output"
  - "A write happened without the confirm word"
relatedAutomations: []
---

# First-open gate

No automation gets a running clock until it has produced one output Jeremy
opened.

# Procedure
1. Open the automation file. Write down **Uses**, **schedule**, and **mode**
   before touching anything.
2. Connect only the connectors on the `uses` line, least privilege. Read-only
   where the mode is `read-only` or `draft-then-wait`. Send scopes stay off.
3. Copy the full prompt from the **Prompt** section, including the
   `Create an Opulent automation` line and the `Trigger` line. Leave the job,
   the loop guard, and the CAUTION line intact.
4. Create it **Disabled**.
5. Run one manual tick.
6. Check the output:
   - exactly one artifact, or justified silence
   - open every cited source. A row whose URL does not resolve fails the run
   - no send, no write, no publish
   - spend within `costCeilingUsd`
7. Set `firstOpenChecked: yes` in the automation file, with the artifact name.
8. Only now Enable the clock.
9. Validate the next live fire the same way. Pause if auth fails twice, or if
   any write happened without the confirm word.

# Verification
This repository has no cost-authorizing dispatcher. Every automation is a
**disabled, non-runnable draft** here, regardless of `costCeilingUsd`; that
field is planning metadata, not a dollar or token cap. Activation requires an
external executor that rejects dispatch before any provider call when a named
cost authorizer and enforceable per-run budget are absent.

An automation is eligible for a future external executor only if its file shows `firstOpenChecked: yes` and
an evidence row naming the artifact that was opened. Anything else is an
ungated clock. Pause it.

# Failure branches
| Symptom | Do this |
|---|---|
| Two artifacts from one tick | Loop guard failed. Fix it before re-running. |
| A cited URL does not resolve | Fail the run. Drop uncited rows and re-tick. |
| Output is right but spend is over ceiling | Do not Enable. Bound the tool calls first. |
| Silence on the first tick | Legitimate only if the sources had nothing. Check one source by hand. |
