#!/usr/bin/env bash
# pilot.sh — the governed Convex prod seam for Jeremy Sanchez's Opulent account.
#
# Every call this hub makes against production goes through here so that:
#   - reads are free, writes are gated behind an explicit confirm word
#   - every call is appended to an evidence ledger
#   - the deployment is pinned, never inferred
#
# Usage:
#   ./scripts/pilot.sh read  <function> '<json args>'
#   ./scripts/pilot.sh write <function> '<json args>'     # needs CONFIRM=send
#   ./scripts/pilot.sh whoami
#   ./scripts/pilot.sh catalog
#
set -euo pipefail

HUB_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FRONTEND="${OPULENT_FRONTEND:-$HOME/Desktop/heavy-production/frontend}"
EXPECTED_DEPLOYMENT="prod:confident-sheep-333"
SANCHEZ_USER_ID="k57apryqpfeg6h33ybxfynarx58e1dwa"
SANCHEZ_EMAIL="jeremysanchez@opulentia.ai"
SANCHEZ_WORKSPACE="ws_6b932257a9014a51a2ec5d42bb"
LEDGER="$HUB_ROOT/evidence/pilot-log-$(date +%F).jsonl"

die() { echo "pilot: $*" >&2; exit 1; }

[ -d "$FRONTEND" ] || die "frontend not found at $FRONTEND (set OPULENT_FRONTEND)"
[ -f "$FRONTEND/.env.deploy" ] || die "no .env.deploy in $FRONTEND"

cd "$FRONTEND"
set -a; . ./.env.deploy; set +a

# Pin the deployment. Never let a stray env var repoint a write at the wrong backend.
[ "${CONVEX_DEPLOYMENT:-}" = "$EXPECTED_DEPLOYMENT" ] \
  || die "CONVEX_DEPLOYMENT is '${CONVEX_DEPLOYMENT:-unset}', expected $EXPECTED_DEPLOYMENT"

mkdir -p "$HUB_ROOT/evidence"

log() { # mode fn args exitcode
  printf '{"ts":"%s","mode":"%s","fn":"%s","args":%s,"exit":%s,"deployment":"%s"}\n' \
    "$(date -u +%FT%TZ)" "$1" "$2" "${3:-null}" "$4" "$EXPECTED_DEPLOYMENT" >> "$LEDGER"
}

invoke() {
  local mode="$1" fn="$2" args="${3:-{\}}"
  local out rc
  set +e
  out="$(npx --yes convex run "$fn" "$args" --prod 2>&1)"
  rc=$?
  set -e
  # strip CLI noise that is not part of the payload
  printf '%s\n' "$out" | grep -v 'ExperimentalWarning\|trace-warnings\|Ignoring `--prod`'
  log "$mode" "$fn" "$args" "$rc"
  return $rc
}

cmd="${1:-}"; shift || true

case "$cmd" in
  read)
    [ $# -ge 1 ] || die "usage: pilot.sh read <function> '<json>'"
    invoke read "$1" "${2:-{\}}"
    ;;

  write)
    [ $# -ge 1 ] || die "usage: pilot.sh write <function> '<json>'"
    [ "${CONFIRM:-}" = "send" ] \
      || die "refusing a production write. Re-run with CONFIRM=send if a human decided this."
    echo "pilot: WRITE $1 on $EXPECTED_DEPLOYMENT" >&2
    invoke write "$1" "${2:-{\}}"
    ;;

  whoami)
    echo "deployment : $EXPECTED_DEPLOYMENT"
    echo "account    : $SANCHEZ_EMAIL"
    echo "userId     : $SANCHEZ_USER_ID"
    echo "workspace  : $SANCHEZ_WORKSPACE"
    echo "ledger     : $LEDGER"
    invoke read creditTracking:getCreditBalance "{\"userId\":\"$SANCHEZ_USER_ID\"}"
    ;;

  catalog)
    sed -n '/^| /p' "$HUB_ROOT/runbooks/convex-pilot.md"
    ;;

  *)
    sed -n '2,16p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 1
    ;;
esac
