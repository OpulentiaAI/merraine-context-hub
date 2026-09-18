---
type: gtm.automation
tldr: Resolve open experiments against what actually happened
status: draft
owner: Jeremy Sanchez
updated: 2026-09-18
surface: jeremy
provenance: "Measurable-experiment loop: state the threshold before the run, record the outcome after"
slug: merraine-experiment-outcome-review
uses:
  - "[[spear]]"
schedule:
  tldr: weekly cron
  kind: cron
  expression: "30 8 * * 1"
  timezone: America/Chicago
  source: opulent-native
mode: read-only
confirmWord: send
firstOpenChecked: "no"
enabled: "no"
costCeilingUsd: 1
producesArtifact: "experiment-review-<date>.md"
sourceTemplate: "none - authored for this engagement"
loopGuard: "If an experiment review for this date already exists, stop."
---

# Experiment outcome review

# Overview
An experiment that is never scored is a habit, not a test. This job reads every
open `gtm.experiment`, measures the ones whose window has closed, and records
the result — including the result "not enough observations to decide".

Nothing is promoted. Moving a supported experiment into code or policy is a
human decision, and the type refuses to let an automation record it.

# What's Needed From User
- Nothing. Read-only.

# Procedure
1. Read every `gtm.experiment` whose state is `running` or `proposed`.
2. Measure only what the experiment's own `measure` names, in code.
3. Record the outcome. Leave promotion alone.

# Prompt
```text
Create an Opulent automation named "Merraine experiment outcome review".

Trigger: weekly, Monday 8:30 AM America/Chicago, after the source manifest review.

When the automation runs, start a session with the prompt below. Everything after this line is the session prompt.

Score every open experiment against what actually happened.

IMPORTANT: If an experiment review for this date already exists, stop.

1. Read merraine/experiments and every gtm.experiment with state proposed or running.
2. If there are none, write a one-line artifact saying so and stop. Do not invent an experiment to fill the file.
3. For each one whose window has closed, compute the measure it names, in code, from the named observations. Count observations; never estimate a count.
4. Compare the value to the threshold using the experiment's own direction. Record supported only when the threshold was cleared, refuted only when it was missed.
5. If the sample is below what the experiment needs, record insufficient and write the number of observations. Small n is reported, never hidden, and insufficient is not a failure.
6. If the numbers moved for a reason that is not attributable to the change, record inconclusive and name the confound.
7. Unresolved means the window is still open. Say that. Silence is not a refutation and an experiment with no result is not a failed experiment.
8. Write "experiment-review-<date>.md": one row per experiment with state, measure, threshold, observed value, sample size, and the decision taken. Every promotion is left blank for a human.
9. Log: experiments read, resolved, still open, insufficient.

CAUTION: Never promote an experiment result into code, policy, a threshold or a live automation. Never set promotedBy. Never send, never enable a clock, never spend. If data is missing, record insufficient and leave the value blank rather than writing a zero.
```

# Forbidden Actions
- Do not promote a result; `promotedBy` is human-only
- Do not treat a silent or unmeasured experiment as refuted
- Do not fabricate an observed value or a sample size
- Do not Enable this clock before a first open Jeremy checked
