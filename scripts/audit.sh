#!/usr/bin/env bash
# audit.sh — read-only state capture for Jeremy Sanchez's Opulent account.
#
# Run this FIRST, every session, before deciding anything. It writes a dated
# evidence bundle so later claims can be checked against what was actually true.
#
# Usage: ./scripts/audit.sh [outdir]
#
set -euo pipefail

HUB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PILOT="$HUB_ROOT/scripts/pilot.sh"
UID_S="k57apryqpfeg6h33ybxfynarx58e1dwa"
EMAIL="jeremysanchez@opulentia.ai"
OUT="${1:-$HUB_ROOT/evidence/audit-$(date +%F)}"

mkdir -p "$OUT"
echo "audit -> $OUT"

cap() { # name function args
  local name="$1" fn="$2" args="$3"
  echo "  - $name"
  if "$PILOT" read "$fn" "$args" > "$OUT/$name.json" 2> "$OUT/$name.err"; then
    rm -f "$OUT/$name.err"
  else
    echo "    FAILED (see $name.err)"
  fi
}

cap account          actions/authAdmin:checkAccountDetails            "{\"email\":\"$EMAIL\"}"
cap balance          creditTracking:getCreditBalance                  "{\"userId\":\"$UID_S\"}"
cap owner-set        userIdentityLinks:resolveOwnershipCandidatesInternal "{\"email\":\"$EMAIL\"}"
cap workspaces       workspaceEntities:listForAgentInternal           "{\"userId\":\"$UID_S\"}"
cap knowledge        knowledgeRunbooks:listKnowledge                  "{\"userId\":\"$UID_S\",\"limit\":200}"
cap runbooks         knowledgeRunbooks:listRunbooks                   "{\"userId\":\"$UID_S\",\"limit\":200}"
cap usage            creditTracking:getRecentUsageEvents              "{\"userId\":\"$UID_S\"}"

echo
echo "== summary =="
python3 - "$OUT" <<'PY'
import json, sys, os
out = sys.argv[1]
def load(n):
    p = os.path.join(out, n + ".json")
    if not os.path.exists(p): return None
    try: return json.load(open(p))
    except Exception: return None

acct = load("account") or {}
bal  = load("balance") or {}
ws   = load("workspaces") or {}
kn   = load("knowledge")
rb   = load("runbooks")

u = acct.get("user") or {}
print(f"account    : {u.get('email','?')}  id={u.get('_id','?')}")
print(f"plan       : {bal.get('planName','?')}  balance=${bal.get('balanceCents',0)/100:.2f}")

wss = ws.get("workspaces") or []
print(f"workspaces : {len(wss)}")
for w in wss:
    mounted = sum(len(w.get(k) or []) for k in
                  ["attachedSkillIds","attachedRunbookIds","attachedKnowledgeIds",
                   "attachedWorkflowIds","attachedDriveFileIds","attachedMemoryBlockIds"])
    print(f"  - {w.get('workspaceId')}  '{w.get('name')}'  mesa={w.get('mesaProvisioningStatus')}  mounted_context={mounted}")

def count(x):
    if x is None: return "n/a"
    if isinstance(x, list): return len(x)
    for k in ("items","knowledge","runbooks","results"):
        if isinstance(x, dict) and isinstance(x.get(k), list): return len(x[k])
    return "?"
print(f"knowledge  : {count(kn)}")
print(f"runbooks   : {count(rb)}")
print()
print("Mounted context of 0 means this hub is not installed yet. Run materialize.sh.")
PY
