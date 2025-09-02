#!/usr/bin/env bash
set -euo pipefail

API_URL=${API_URL:-http://localhost:8000}

echo "[smoke] /health"
resp=$(curl -sS ${API_URL}/health)
echo "$resp"
status=$(echo "$resp" | sed -n 's/.*"status" *: *"\([a-z]*\)".*/\1/p')
if [[ "$status" != "ok" && "$status" != "degraded" ]]; then
  echo "Health check failed" >&2
  exit 1
fi
echo "[smoke] health OK"


