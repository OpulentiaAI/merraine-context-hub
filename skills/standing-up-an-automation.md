---
type: hub.skill
name: standing-up-an-automation
description: "Create, enable, schedule, or troubleshoot an automation on this account. Use when adding a recurring job, wiring a Parallel monitor or webhook, or when an automation misfires. Triggers: create an automation, schedule it, set up a monitor, enable the clock, why did it fire twice."
triggers: [automation, schedule, cron, monitor, webhook, enable, trigger]
readWhen: "Before creating or enabling anything that runs on its own"
doNotUseFor: ["One-off tasks", "Anything that would send without approval"]
---

# Standing up an automation

Read [[first-open-gate]] and follow it exactly. Nothing gets a clock before one
checked output.

Choose the trigger honestly, per [[parallel-monitor-scheduling]]: detection is an
event, aggregation is a cron. An automation that fires daily and finds nothing
should be a Parallel monitor instead, and [[routine-healthcheck]] will flag it if
it is not.

Every automation file needs `costCeilingUsd`, a `loopGuard`, and a CAUTION line in
its prompt. Bounding tool calls improves quality, not just cost — see
[[agent-economics]].
