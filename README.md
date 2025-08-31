# Stratum Core

Stratum Core is an agent‑native, cloud‑neutral semantic execution layer for heterogeneous enterprise data.

## Quickstart (Local)

1) Create a Python venv and install deps
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```

2) Or start full stack with Docker Compose
```bash
docker compose up -d
```
- API: http://localhost:8000/health
- Trino: http://localhost:8080
- Qdrant: http://localhost:6333
- Postgres: localhost:5432

3) Configure Trino catalogs in `trino/etc/catalog/`

For development details, see `docs/engineering/guides/dev-environment.md` and Reference → API.

## Installing GNU Make (for Makefile commands)

The repository includes a Makefile to streamline common tasks (venv, running the API, Docker Compose). Install GNU Make as follows:

macOS:
```bash
brew install make
# invoke as "make" (or gmake if Homebrew installs it under that name)
```

Ubuntu/Debian:
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
- Alternatively, use WSL (Ubuntu) and follow the Linux instructions; `make` will work out of the box after `apt install make`.

**Docs:** https://stratum-ai.github.io/stratum-core/

**Design partners:** We're onboarding a small group of teams running Snowflake + Databricks.
👉 Apply here: [Design Partner Application](https://example.com/design-partner)

## Quickstart (docs-first)
1) Browse the docs: `docs/intro.md`
2) MVP scope: `docs/mvp-scope.md`
3) API contract: `openapi/semantic.yaml` + `docs/api.md`

## License
Apache-2.0 (see `LICENSE`)
