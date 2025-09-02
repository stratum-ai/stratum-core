# Local Development Setup

This guide sets up Stratum Core locally with Docker Compose using:
- FastAPI (API)
- Trino (execution)
- Postgres (control plane)
- Qdrant (semantic retrieval)

## Prerequisites
- Docker Desktop (or Docker Engine)
- Node.js 18+ for docs (optional)
- Python 3.9+ (for API dev later)

## Quick Start

```bash
# Clone repo
git clone <repo>
cd stratum-core

# One-step setup (Ubuntu/WSL): installs Docker and creates Python venv
make setup

# Launch services
docker compose up -d

# Verify services
curl http://localhost:8080/v1/info        # Trino
curl http://localhost:6333/cluster/status  # Qdrant
```

## Ports
- Trino: 8080
- Qdrant: 6333
- Postgres: 5432
- API (later): 8000

## Compose Template (example)
```yaml
services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: stratum
      POSTGRES_PASSWORD: stratum
      POSTGRES_DB: stratum
    ports: ['5432:5432']

  qdrant:
    image: qdrant/qdrant:latest
    ports: ['6333:6333']

  trino:
    image: trinodb/trino:latest
    ports: ['8080:8080']
    volumes:
      - ./trino/etc:/etc/trino

  api:
    build: .
    environment:
      STRATUM_DB_URL: postgresql://stratum:stratum@postgres:5432/stratum
      QDRANT_URL: http://qdrant:6333
      TRINO_URL: http://trino:8080
      STRATUM_API_KEYS: dev=devkey
    ports: ['8000:8000']
    depends_on: [postgres, qdrant, trino]
```

## Next Steps
- Configure Trino catalogs: see `docs/engineering/trino-catalogs.md`
- Authenticate to API:
  ```bash
  curl -X POST http://localhost:8000/api/v1/index/schema -H 'x-api-key: devkey' -H 'content-type: application/json' -d '{"limit_tables":50}'
  curl 'http://localhost:8000/api/v1/find?q=orders' -H 'x-api-key: devkey'
  ```
