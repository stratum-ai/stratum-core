#!/usr/bin/env bash
set -euo pipefail

API_URL=${API_URL:-http://localhost:8000}
API_KEY=${API_KEY:-devkey}

echo "[smoke] /api/v1/find?q=orders"
resp=$(curl -sS "${API_URL}/api/v1/find?q=orders" -H "x-api-key: ${API_KEY}")
echo "$resp"
matches=$(echo "$resp" | sed -n 's/.*"matches" *: *\[\(.*\)\].*/\1/p')
if [[ -z "$matches" ]]; then
  echo "Find returned no matches" >&2
  exit 1
fi
echo "[smoke] find returned matches"


