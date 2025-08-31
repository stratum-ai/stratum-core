# Developer Environment

## Python venv (recommended)

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

## Environment variables
Copy `ENV.example` to `.env` (or export variables) and adjust as needed.

## Docker Compose (infra + API)

```bash
docker compose up -d
# API at http://localhost:8000/health
# Trino at http://localhost:8080
# Qdrant at http://localhost:6333
# Postgres at localhost:5432
```

To rebuild the API image after code changes:

```bash
docker compose build api && docker compose up -d api
```
