#!/usr/bin/env bash
set -euo pipefail

HOST=${1:?host}
PORT=${2:?port}
TIMEOUT=${3:-60}
LABEL=${4:-target}

echo "[wait-for] Waiting for ${LABEL} at ${HOST}:${PORT} (timeout ${TIMEOUT}s)"
SECS=0
while ! (echo > /dev/tcp/${HOST}/${PORT}) 2>/dev/null; do
  sleep 1
  SECS=$((SECS+1))
  if [ ${SECS} -ge ${TIMEOUT} ]; then
    echo "[wait-for] Timeout waiting for ${LABEL} at ${HOST}:${PORT}" >&2
    exit 1
  fi
done
echo "[wait-for] ${LABEL} is reachable"


