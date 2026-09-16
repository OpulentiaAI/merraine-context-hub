---
type: mcp.skill::au-mcp-sdk
name: standing-up-an-automation
description: "Create, enable, schedule, or troubleshoot an automation on this account. Use when adding a recurring job, wiring a Parallel monitor or webhook, or when an automation misfires. Triggers: create an automation, schedule it, set up a monitor, enable the clock, why did it fire twice."
---

# Standing up an automation

Read [[first-open-gate]] and follow it exactly. Nothing gets a clock before one
checked output. On first session, [[hub-init]] creates the day-one set
Disabled and first-opens signal outbound and awards.

Choose the trigger honestly, per [[parallel-monitor-scheduling]]: detection is
an event, aggregation is a cron. An automation that fires daily and finds
nothing should be a Parallel monitor instead.

Every automation file needs `costCeilingUsd`, a `loopGuard`, and a CAUTION line
in its prompt. Bounding tool calls improves quality, not just cost — see
[[agent-economics]].

The daily hiring scan already has a procedure ([[daily-hiring-scan]]) and is
not on a clock. Do not invent a schedule for it unless Jeremy asks.
