---
type: gtm.runbook
tldr: Daily CFO and leadership hiring scan
status: active
owner: Jeremy Sanchez
updated: 2026-09-16
surface: jeremy
provenance: "Durable memory block cfo-leadership-hiring-scan, last written 2026-09-10, read live 2026-09-16"
trigger: "When Jeremy asks for the daily hiring scan, or when standing the scan up as an automation"
audience: jeremy-sanchez
escalateWhen:
  - "A prospect would be contacted"
  - "A name, title, or email would have to be invented"
  - "Email to Jeremy's work inbox fails"
relatedAutomations: []
---

# Daily CFO and leadership hiring scan

The recurring scan you already run. There is **no saved automation** for it
yet. When you say "run the scan" or "adjust the prompt," deliver the report
or the revised prompt in the thread. Do not invent a clock.

# Procedure
1. Search Indeed, LinkedIn, Crain's Chicago Business, local publications, and
   general news for CFO / VP+ hiring at growth-stage VC or PE-backed companies.
   Titles: VP Finance, VP Ops, Controller, VP Accounting, CAO, VP Sales, CRO,
   COO, CFO. Exclude large public enterprises and pre-seed startups.
2. Two groups only: **Open postings** (still live on an employer source) and
   **New hires** (announced or started in the last few days, with dates).
3. Priority geos first, and flag them: Chicago, Boston, New York, Ohio, Florida.
   Other US markets only when the signal is standout.
4. If a group has nothing fresh and verified, say so. Do not pad with stale rows.
   Yesterday's baseline is on [[active-accounts]].
5. Per finding: company, location, funding or growth context you can cite,
   title and signal, one recruiting line, source links for the signal and the
   funding.
6. Each opening gets three named outreach contacts, ranked:
   1. Confirmed hiring manager if you can see them, else the relevant functional
      leader
   2. Senior sponsor (CFO, COO, CRO, CEO, relevant VP)
   3. Another decision-maker (department exec, Head of TA, CPO)
   Each contact: full name, current title, LinkedIn or company-bio link, why
   they matter. Mark confirmed vs inferred. Never invent a name, title,
   reporting line, profile URL, or email. List gaps. **Do not contact them.**
7. Confirm openings on the employer ATS or careers page, not on a search snippet.
   LinkedIn job pages alone are not enough. Built In "removed" and Lever 404
   mean the seat is gone.
8. Deliver the full report in the thread **and** email Jeremy's work inbox
   with subject `Daily CFO/Leadership Hiring Scan — [today's date]`. Not Slack.
   If the email cannot send, still post the report and say so. That email is
   delivery to you, not outbound to a prospect.

# Verification
- Every open posting still loads on an employer-owned page.
- Every new hire has a date.
- No contact on the list was invented.
- The 10 September baseline rows were not re-reported as new.

# Failure branches
| Symptom | Do this |
|---|---|
| A source URL does not resolve | Drop the row. |
| Email to Jeremy's work inbox fails | Keep the thread report. Name the blocker. |
| Someone asks to "just send a few notes" | No. The list is for your outreach. |
| You want this on a weekday clock | Stand it up Disabled through [[first-open-gate]]. |
