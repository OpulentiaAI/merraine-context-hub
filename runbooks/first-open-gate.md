---
type: gtm.runbook
tldr: First-open gate
status: active
owner: Opulent
updated: 2026-09-14
provenance: "OpulentiaAI/gtm-agent-automations agents/PLAYBOOK.md and agents/gtm/README.md"
trigger: "Before enabling any automation in this hub"
audience: opulent
escalateWhen:
  - "An automation cannot produce a checkable first output"
  - "A write happened without the confirm word"
relatedAutomations: []
---

# First-open gate

No automation in this hub gets a running clock until it has produced one output a
human opened. This is the single most important procedure here.

## Procedure

1. Open the automation file. Write down **Uses**, **schedule**, and **mode** before
   touching anything.
2. Connect **only** the connectors on the `uses` line, at least privilege. Read-only
   where the mode is `read-only` or `draft-then-wait`. Send scopes stay off.
3. Copy the full prompt from the **Prompt** section, including the `Create an
   Opulent automation` line and the `Trigger` line. Replace names to match the
   environment. **Leave the job, the loop guard, and the CAUTION line intact.**
4. Create it **Disabled**.
5. Run one manual tick.
6. Check the output against the job:
   - exactly one artifact, or justified silence
   - **open every cited source yourself.** A row whose URL does not resolve fails
     the run
   - no send, no write, no publish
   - spend within `costCeilingUsd`
7. Set `firstOpenChecked: yes` in the automation file, with the artifact name.
8. Only now Enable the clock.
9. Validate the next live fire the same way. Pause if auth fails twice, or if any
   write happened without the confirm word.

## Verification

An automation is Enabled legitimately only if its file shows `firstOpenChecked: yes`
and an evidence row naming the artifact you checked. Anything else is an ungated
clock, and should be paused on sight.

## Failure branches

| Symptom | Do this |
|---|---|
| Two artifacts from one tick | Loop guard failed. Fix the guard before re-running. |
| A cited URL does not resolve | Fail the run. Tell the automation to drop uncited rows and re-tick. |
| Output is right but spend is over ceiling | Do not Enable. Bound the tool calls first. |
| Silence on the first tick | Legitimate only if the sources genuinely had nothing. Prove it by checking one source by hand. |
