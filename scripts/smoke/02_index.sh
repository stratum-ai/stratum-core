#!/usr/bin/env bash
set -euo pipefail

API_URL=${API_URL:-http://localhost:8000}
API_KEY=${API_KEY:-devkey}

echo "[smoke] /api/v1/index/schema"
resp=$(curl -sS -X POST ${API_URL}/api/v1/index/schema \
  -H "x-api-key: ${API_KEY}" \
  -H 'content-type: application/json' \
  -d '{"limit_tables": 10}')
echo "$resp"
indexed=$(echo "$resp" | sed -n 's/.*"indexed" *: *\([0-9][0-9]*\).*/\1/p')
if [[ -z "$indexed" ]]; then
  echo "Indexing failed" >&2
  exit 1
fi
echo "[smoke] indexed $indexed objects"


