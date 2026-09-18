#!/usr/bin/env bash
set -euo pipefail
: "${OPERATOR_ACCOUNT_ID:?Set OPERATOR_ACCOUNT_ID in private environment}"
: "${OPERATOR_EMAIL:?Set OPERATOR_EMAIL in private environment}"
: "${OPERATOR_DEPLOYMENT:?Set OPERATOR_DEPLOYMENT in private environment}"
echo 'Audit bindings supplied from private environment; do not record results in this public repository.'
