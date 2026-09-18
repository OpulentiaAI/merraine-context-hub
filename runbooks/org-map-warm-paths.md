---
type: gtm.runbook
tldr: Build organization maps and retain only public, evidenced warm paths
status: active
owner: Opulent
updated: 2026-09-18
surface: jeremy
provenance: "Operational procedure authored for the context hub; Sales Navigator guidance is cited in research/sales-navigator-filters.md"
trigger: "When a target organization needs a map of legitimate introduction routes"
audience: operator
escalateWhen:
  - "A requested route lacks public evidence but someone wants to use it"
  - "Sales Navigator access is unavailable and the map cannot be completed"
  - "A user asks to guess an email, personal contact, or relationship"
relatedAutomations: []
---

# Organization map and warm paths

Use a purchased LinkedIn Sales Navigator seat to map accounts and identify
publicly evidenced routes. Do not build a scraper or bypass access controls.
Silence and no evidence are valid results.

# Procedure
1. Define the target organization, buyer roles, exclusions, and the map date.
   Open Sales Navigator with the account list and filters appropriate to the
   question, including role, geography, seniority, recent job changes, and
   recent activity when relevant.
2. Build an organization map from visible, public profile and company context:
   target people, current roles, and any public relationship route. Record only
   facts supported by the profile or another public source.
3. For each potential introducer, find the public page that shows the route to
   the target: a shared network, former employer, investor, advisor, customer,
   partner, or community connection. Record its URL exactly as `evidenceUrl`.
4. Create `gtm.warm-path` only when `evidenceUrl` is present. Set `pathKind`
   and `strength` no stronger than the evidence supports, and set `verified` to
   `yes` only after reopening the cited page. A missing URL means drop the path.
5. Keep the map separate from outreach. Do not infer email addresses, personal
   contacts, reporting lines, or permission to introduce. Respect
   `doNotContact: yes` on every person.
6. Report verified routes, unverified but evidenced routes, and gaps separately.
   If no path has evidence, report no legitimate warm path rather than filling
   the map with guesses.

# Verification
- Sales Navigator is used as a purchased product, not reproduced with a scraper.
- Every retained `gtm.warm-path` has a non-empty public `evidenceUrl`.
- The cited page was reopened before `verified: yes` was assigned.
- `strength` reflects the cited connection and does not turn a shared employer
  or community into a direct relationship.
- No route includes guessed contact details or bypasses a do-not-contact flag.

# Failure branches
| Symptom | Do this |
|---|---|
| Sales Navigator is unavailable | Do not scrape it. Record the gap and escalate for seat access or defer the map. |
| A colleague says they know the target but supplies no public evidence | Drop the path; it is not usable in this hub. |
| The only apparent route is an email guess or personal contact | Do not use it. Record no legitimate warm path. |
| A cited page no longer shows the connection | Set `verified: no` or drop the path; do not retain it as usable. |
| Target or introducer has `doNotContact: yes` | Exclude them from the path and do not initiate contact. |
