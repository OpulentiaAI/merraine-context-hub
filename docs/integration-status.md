# Integration status

## Implemented controls

- Source manifests, duplicate-source checks, owner separation, and suppression
  validation fail closed.
- Six workflow axes are bound in the private catalog: search, warm paths,
  sequencing and replies, enrichment, signals, and awards.
- Missing CRM records are review-only observations. Nothing creates CRM records
  automatically.
- Jev receipts use synthetic/redacted inputs, preserve reproducibility, and
  record unavailable outcomes honestly. They never authorize contact or sends.
- Public automations are disabled non-runnable drafts. A future dispatcher must
  enforce an authorized per-run budget before it can activate one.
- Public account bindings and audit payloads are removed from the current
  branch. Historical repository exposure is a separate owner decision.

## Data coverage

The private canonical archive validates the authorized Spear extraction scope
and its owner boundary. It does not establish account-wide coverage. Connected
application reads are inventory-only or partial where their authorized tools do
not expose meaningful content, and several sources remain unavailable or lack
credentials.

## Activation gates

No automation, outreach, deployment, or merge is authorized by this status.
Activation remains blocked until source owners complete the remaining allowed
reads, an external cost-authorizing dispatcher exists, and a named human grants
the required approval.
