# Implementation Plan

## Phase 1: MVP Foundation (Weeks 1-8)

### Week 1-2: Project Setup
- [ ] **Repository & DevOps**
  - [x] Documentation site (Docusaurus)
  - [ ] Python project structure (Poetry/pyproject.toml)
  - [ ] Docker setup (Dockerfile, docker-compose.yml)
  - [ ] CI/CD pipeline (GitHub Actions)
  - [ ] Pre-commit hooks (black, isort, mypy)

- [ ] **Core Dependencies**
  - [ ] FastAPI + Uvicorn server setup
  - [ ] Pydantic models for API contracts
  - [ ] SQLGlot for SQL parsing/validation
  - [ ] DuckDB connector implementation

### Week 3-4: Catalog System
- [ ] **Schema Discovery**
  - [ ] Database introspection (tables, columns, types)
  - [ ] Basic column profiling (nulls, cardinality, samples)
  - [ ] Metadata storage (SQLite or DuckDB)

- [ ] **NL Description Generation**
  - [ ] OpenAI integration for schema descriptions
  - [ ] Prompt templates for table/column descriptions
  - [ ] Embedding generation and storage

### Week 5-6: Vector Retrieval
- [ ] **Qdrant Integration**
  - [ ] Docker setup for local Qdrant instance
  - [ ] Python client configuration
  - [ ] Collection management (create, index, search)

- [ ] **Hybrid Search**
  - [ ] Keyword search (simple text matching)
  - [ ] Vector similarity search
  - [ ] Result ranking and combination

### Week 7-8: Core APIs
- [ ] **API Implementation**
  - [ ] `/describe/{table}` endpoint
  - [ ] `/find?q=...` endpoint  
  - [ ] `/ask` endpoint (basic NL→SQL)

- [ ] **Query Planning**
  - [ ] LLM integration for SQL generation
  - [ ] Context injection (relevant schemas)
  - [ ] Basic verification (SQLGlot parsing)

## Phase 2: Production Readiness (Weeks 9-12)

### Week 9-10: Verification & Safety
- [ ] **Enhanced Verification**
  - [ ] EXPLAIN query validation
  - [ ] SELECT-only enforcement
  - [ ] Row/time limits
  - [ ] Dangerous operation detection

- [ ] **Error Handling**
  - [ ] Graceful LLM API failures
  - [ ] Database connection issues
  - [ ] Invalid SQL recovery

### Week 11-12: Testing & Documentation
- [ ] **Comprehensive Testing**
  - [ ] Unit tests (pytest, 80%+ coverage)
  - [ ] Integration tests (real databases)
  - [ ] Golden NL→SQL test suite (10 questions)

- [ ] **Production Setup**
  - [ ] Environment configuration
  - [ ] Logging and observability
  - [ ] Health check endpoints
  - [ ] Docker optimization

## Phase 3: Enhancement (Weeks 13-16)

### Week 13-14: Advanced Features
- [ ] **Query Optimization**
  - [ ] Caching layer (Redis)
  - [ ] Prompt optimization
  - [ ] Parallel processing

- [ ] **Extended Connectors**
  - [ ] Postgres production connector
  - [ ] CSV/Parquet file support
  - [ ] Connection pooling

### Week 15-16: UX & Demo
- [ ] **Demo Interface**
  - [ ] Simple web playground
  - [ ] Query result visualization
  - [ ] SQL explanation/provenance

- [ ] **Design Partner Readiness**
  - [ ] Installation automation
  - [ ] Configuration templates
  - [ ] Usage analytics

## Success Metrics by Phase

### Phase 1 Targets
- [ ] All 3 APIs functional (`/describe`, `/find`, `/ask`)
- [ ] \<30 minute local setup time
- [ ] Basic NL→SQL on 5+ question types

### Phase 2 Targets  
- [ ] 70%+ accuracy on golden NL→SQL set
- [ ] Zero SQL injection vulnerabilities
- [ ] \<5s p95 latency for `/ask`

### Phase 3 Targets
- [ ] Demo answers 10 curated questions correctly
- [ ] First design partner onboarded
- [ ] Documentation site live with CTA

## Technical Debt & Future Work

### Post-MVP Priorities
- [ ] Multi-database query stitching
- [ ] Advanced query optimization
- [ ] Streaming result support
- [ ] Plugin architecture for connectors

### Enterprise Features (Future)
- [ ] RBAC and SSO integration
- [ ] Query audit logging
- [ ] Cost tracking and limits
- [ ] Governance policies
