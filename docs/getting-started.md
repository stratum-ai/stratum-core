# Getting Started with Stratum Core

## Quick Overview

Stratum Core is an **agent-native semantic layer** that makes enterprise data accessible to AI agents through natural language. Think of it as a universal translator between agents and databases.

**In 30 seconds:**
- Agents send natural language queries to `/ask`
- Stratum finds relevant tables via vector search
- Converts NL → verified SQL → executes safely
- Returns structured results + provenance

## Understanding the Mission

👉 **Start here**: [Mission](./mission-statement.md)

**The Problem**: AI agents can't effectively query enterprise data because it's fragmented across multiple systems (Snowflake, Postgres, Databricks, etc.) with different schemas and access patterns.

**Our Solution**: A neutral semantic layer that lets agents discover, understand, and safely query any data source through simple APIs.

## Key Documents by Role

### For Product Managers
1. [Mission Statement](./mission-statement.md) - Why we exist
2. [Vision & Principles](./vision.md) - Where we're going  
3. [MVP Scope](./mvp-scope.md) - What we're building first
4. PRD and product design docs are available to maintainers in the private `design/` workspace.

### For Engineers  
1. [Implementation Plan](./implementation-plan.md) - 16-week roadmap with checkboxes
2. [Technology Stack](./tech-stack.md) - All technologies and decisions
3. [Architecture](./architecture.md) - System design and data flow
4. [API Documentation](./api.md) - Contract specifications

### For Business
1. [Roadmap](./roadmap.md) - 4-phase release plan
2. Metrics & KPIs are tracked in the private `design/` workspace.
3. Internal UX notes are available to maintainers in the private `design/` workspace.

## Next Actions by Priority

### Immediate (This Week)
1. ✅ **Documentation complete** - You are here!
2. 📋 **Set up development environment** - Follow [Implementation Plan Week 1](./implementation-plan.md#week-1-2-project-setup)
3. 🏗️ **Create Python project structure** - Poetry + FastAPI skeleton

### Week 1-2: Foundation
- [ ] Repository setup (CI/CD, Docker, pre-commit)
- [ ] FastAPI server with basic health checks
- [ ] Database connection (DuckDB for MVP)
- [ ] OpenAPI schema generation

### Week 3-4: Core Features
- [ ] Schema discovery and profiling
- [ ] Vector store integration (Qdrant)
- [ ] Basic `/describe` endpoint

## Technology Decisions Made

Based on the documentation, here are the key technology choices:

### ✅ **Confirmed Stack**
- **Backend**: FastAPI (Python 3.9+)
- **Database**: DuckDB (MVP) → Postgres (production)  
- **Vector Store**: Qdrant
- **SQL Processing**: SQLGlot
- **LLM Provider**: OpenAI GPT-4 (configurable)
- **Data Formats**: Arrow/Parquet
- **Deployment**: Docker + docker-compose

### ❓ **Still to Decide**
- Package management: Poetry vs pip-tools
- Caching layer: Redis vs in-memory
- Monitoring: Which observability stack?
- Testing data: Sample datasets for golden test suite

## Quick Start Commands

Once implementation begins:

```bash
# Clone and setup
git clone <repo>
cd stratum-core
pip install poetry
poetry install

# Local development
docker-compose up -d  # Start Qdrant + Postgres
poetry run uvicorn app.main:app --reload

# Test the APIs
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/describe/users
```

## Questions to Resolve

1. **Design Partner Strategy**: How to find and onboard first 3-5 design partners?
2. **LLM Costs**: Budget for OpenAI API calls during development/testing?
3. **Sample Data**: What datasets to use for golden NL→SQL test suite?
4. **Enterprise Connector Priority**: Snowflake or Databricks first?

---

**Ready to start building?** Head to the [Implementation Plan](./implementation-plan.md) for your detailed 16-week roadmap with checkboxes for every task.
