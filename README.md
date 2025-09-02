# Stratum Core

Stratum Core is an agent‑native, cloud‑neutral semantic execution layer for heterogeneous enterprise data.

## Quickstart (Local)

1) Create a Python venv and install deps
```bash
# macOS/Linux/WSL
python -m venv .venv  # or: python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1  # after creating the venv with 'py -m venv .venv'
```

2) Or one-step setup with Make (installs Docker on Ubuntu/WSL, creates venv)
```bash
make setup
```

3) Start full stack with Docker Compose
```bash
docker compose up -d
```
- API: http://localhost:8000/health
- Trino: http://localhost:8080
- Qdrant: http://localhost:6333
- Postgres: localhost:5432

4) Authenticate to API

The stack sets `STRATUM_API_KEYS=dev=devkey` for local development.

```bash
# Health is open (no auth)
curl http://localhost:8000/health

# Index schema (requires API key)
curl -X POST http://localhost:8000/api/v1/index/schema \
  -H 'x-api-key: devkey' \
  -H 'content-type: application/json' \
  -d '{"limit_tables": 50}'

# Find (requires API key)
curl 'http://localhost:8000/api/v1/find?q=orders' -H 'x-api-key: devkey'
```

5) Configure Trino catalogs in `trino/etc/catalog/`

For development details, see `docs/engineering/setup/local-dev-setup.md` and Reference → API.

## Installing GNU Make (for Makefile commands)

The repository includes a Makefile to streamline common tasks (venv, running the API, Docker Compose). Install GNU Make as follows:

macOS:
```bash
brew install make
# invoke as "make" (or gmake if Homebrew installs it under that name)
```

Ubuntu/Debian/WSL:
```bash
sudo apt-get update && sudo apt-get install -y make
```

RHEL/CentOS/Amazon Linux:
```bash
sudo yum install -y make
```

Windows (PowerShell):
```powershell
# Option 1: Chocolatey
choco install make -y

# Option 2: Scoop
scoop install make

# Option 3: MSYS2 (provides a Unix-like shell)
winget install -e --id MSYS2.MSYS2
# Then from MSYS2 shell:
pacman -Sy --noconfirm make
```

Notes for Windows:
- Ensure the installed `make` is on your PATH (close/reopen the terminal after install).
- From PowerShell or CMD, you can run `make help`, `make venv-win`, `make run-win`, etc.
- Alternatively, use WSL (Ubuntu) and follow the Linux instructions; `make` works after `apt install make`.

### WSL notes

- Use the Linux instructions inside WSL. `make venv-unix` auto-detects `python` vs `python3`.
- Install base tooling:
  ```bash
  sudo apt-get update && sudo apt-get install -y make python3-venv python3-pip
  ```
- For Docker: either
  - Use Docker Desktop with WSL integration enabled, or
  - Install `docker` in WSL and ensure the service/daemon is reachable. Verify with `docker info`.
- File system performance: prefer cloning the repo under your Linux home (e.g., `/home/<user>/...`) rather than the Windows-mounted drive.
- Line endings: ensure Git is set to avoid CRLF conversions inside WSL: `git config --global core.autocrlf input`.

**Docs:** https://stratum-ai.github.io/stratum-core/

**Design partners:** We're onboarding a small group of teams running Snowflake + Databricks.
👉 Apply here: [Design Partner Application](https://example.com/design-partner)

## Quickstart (docs-first)
1) Browse the docs: `docs/intro.md`
2) MVP scope: `docs/mvp-scope.md`
3) API contract: `openapi/semantic.yaml` + `docs/api.md`

## License
Apache-2.0 (see `LICENSE`)
