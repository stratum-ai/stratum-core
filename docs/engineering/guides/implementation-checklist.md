# Implementation Checklist

Copy these checklists into GitHub issues to track implementation progress.

## 📋 Phase 1: Core Surface (Weeks 1-4)

### Sprint 1: Foundation (Week 1)
- [ ] **Repository Setup**
  - [ ] Python project structure with Poetry/pyproject.toml
  - [ ] Docker Compose with FastAPI, Trino, Qdrant, Postgres
  - [ ] CI/CD pipeline (GitHub Actions) with tests, linting, Docker build
  - [ ] Pre-commit hooks: black, isort, mypy, pytest

- [ ] **Core Dependencies**  
  - [ ] FastAPI + Uvicorn server with health check endpoint
  - [ ] Pydantic models for API request/response schemas
  - [ ] SQLAlchemy models for Postgres control plane
  - [ ] Trino Python client (trino-python-client)
  - [ ] Qdrant Python client + embedding utilities

### Sprint 2: API Skeleton (Week 2)
- [ ] **API Endpoints (Basic)**
  - [ ] `GET /health` - service health check
  - [ ] `GET /describe/{table}` - table schema endpoint (stub)
  - [ ] `GET /find?q=...` - semantic search endpoint (stub)
  - [ ] `POST /ask` - NL→SQL endpoint (stub)
  - [ ] OpenAPI schema generation and /docs endpoint

- [ ] **Authentication & Control Plane**
  - [ ] API key middleware and tenant resolution
  - [ ] Postgres schemas for tenants, catalogs, policies, audit
  - [ ] Basic tenant management (create, list, delete)

### Sprint 3: Semantic Retrieval (Week 3)
- [ ] **Qdrant Integration**
  - [ ] Collection setup for table/column metadata
  - [ ] Embedding generation pipeline (OpenAI text-embedding-ada-002)
  - [ ] Hybrid search: keyword (BM25) + vector (cosine similarity)
  - [ ] Result ranking and relevance scoring

- [ ] **Catalog Discovery**
  - [ ] Trino catalog introspection (list tables, describe columns)
  - [ ] Metadata enhancement with NL descriptions via LLM
  - [ ] Control plane sync: store catalog metadata in Postgres

### Sprint 4: Query Planning & Execution (Week 4)
- [ ] **NL→SQL Planning**
  - [ ] OpenAI GPT-4 integration with prompt templates
  - [ ] Context injection: relevant tables/columns from semantic search
  - [ ] Catalog-aware SQL generation (prefix with catalog.schema)

- [ ] **Safety & Verification**
  - [ ] SQLGlot integration for SQL parsing and validation
  - [ ] Read-only enforcement (block DML/DDL statements)
  - [ ] Automatic LIMIT injection if not specified
  - [ ] Schema validation against Trino catalogs

- [ ] **Execution & Response**
  - [ ] Trino query execution with error handling
  - [ ] Response formatting with metadata and provenance
  - [ ] Query logging and audit trail in Postgres

### Phase 1 Acceptance Tests
- [ ] **Functional Tests**
  - [ ] 15 curated NL questions execute successfully
  - [ ] 2 real data sources connected (e.g., sample Postgres + CSV files)
  - [ ] All responses include `engine="trino"`, provenance, routed_reason

- [ ] **Performance Tests**
  - [ ] p95 `/find` latency \<150ms
  - [ ] p95 `/ask` latency \<5s
  - [ ] 10+ concurrent requests handled successfully

---

## 🔌 Phase 2: Enterprise Readiness (Weeks 5-8)

### Sprint 5: Source Connectors (Week 5)
- [ ] **Trino Catalog Configuration**
  - [ ] Snowflake catalog setup and connection testing
  - [ ] Postgres/MySQL catalog configuration  
  - [ ] Catalog health monitoring and error handling
  - [ ] Multi-catalog query support

- [ ] **Schema Management**
  - [ ] Automated schema discovery jobs
  - [ ] Change detection and notification
  - [ ] Manual metadata override capabilities

### Sprint 6: Governance & Policies (Week 6)
- [ ] **Policy Engine**
  - [ ] Row-level security rules (WHERE clause injection)
  - [ ] Column masking policies (SELECT clause transformation)
  - [ ] Schema/table blocklist enforcement
  - [ ] Rate limiting per tenant/user

- [ ] **Policy Management**
  - [ ] Policy CRUD APIs for admin interface
  - [ ] Policy validation and testing framework
  - [ ] Policy audit log and violation tracking

### Sprint 7: Security & Auth (Week 7)
- [ ] **Authentication**
  - [ ] OIDC/OAuth2 integration for SSO
  - [ ] JWT token validation and user context
  - [ ] Role-based access control (RBAC)

- [ ] **Secrets Management**
  - [ ] Secure storage of data source credentials
  - [ ] Credential rotation and management
  - [ ] Read-only database user enforcement

### Sprint 8: Observability (Week 8)
- [ ] **Logging & Metrics**
  - [ ] Structured logging with correlation IDs
  - [ ] Prometheus metrics (latency, errors, throughput)
  - [ ] Query execution tracking and profiling

- [ ] **Admin Interface**
  - [ ] Connection management UI
  - [ ] Policy management dashboard
  - [ ] Query logs and audit trail viewer

### Phase 2 Acceptance Tests
- [ ] **Enterprise Integration**
  - [ ] 2+ production data sources connected
  - [ ] Policy enforcement: 0 data leakage incidents
  - [ ] Admin interface operational for day-to-day management

---

## 🧠 Phase 3: Quality & Reliability (Weeks 9-12)

### Sprint 9: Evaluation Framework (Week 9)
- [ ] **Golden Test Suite**
  - [ ] 50+ curated NL→SQL question pairs
  - [ ] Automated execution and accuracy measurement
  - [ ] Regression testing on schema changes

- [ ] **Retrieval Evaluation**
  - [ ] Recall@k measurement framework
  - [ ] Semantic relevance scoring
  - [ ] Benchmark dataset creation

### Sprint 10: Planner Improvements (Week 10)
- [ ] **Advanced SQL Features**
  - [ ] Multi-table join inference
  - [ ] Time window/date filter normalization
  - [ ] Aggregation and grouping logic
  - [ ] Semantic synonym handling

- [ ] **Query Optimization**
  - [ ] Query plan analysis and optimization
  - [ ] Predicate pushdown recommendations
  - [ ] Index utilization hints

### Sprint 11: Result Stitching (Week 11)
- [ ] **Multi-Frame Responses**
  - [ ] Support for multiple result sets per query
  - [ ] Cross-catalog query coordination
  - [ ] Result correlation and metadata

- [ ] **Performance Optimization**
  - [ ] Query result caching (Redis)
  - [ ] Parallel execution for independent subqueries
  - [ ] Connection pooling and resource management

### Sprint 12: Design Partner Readiness (Week 12)
- [ ] **Pilot Program**
  - [ ] Onboarding playbook and documentation
  - [ ] Support process and escalation procedures
  - [ ] Success metrics tracking and reporting

- [ ] **Case Study Development**
  - [ ] Reference implementation with anonymized data
  - [ ] Performance benchmarks and accuracy metrics
  - [ ] Customer testimonial and use case documentation

### Phase 3 Acceptance Tests
- [ ] **Quality Metrics**
  - [ ] ≥90% execution accuracy on golden test suite
  - [ ] Retrieval recall@k baseline established
  - [ ] Performance targets met under load

- [ ] **Commercial Readiness**
  - [ ] 1+ public case study completed
  - [ ] Design partner satisfaction ≥4/5
  - [ ] Sales collateral and demo materials ready

---

## 🚀 Ready to Begin?

**Next immediate actions:**
1. Create GitHub repository with these checklists as issues
2. Set up development environment (Docker Compose)
3. Begin Sprint 1: Foundation work

**Track progress**: Update checkboxes as tasks complete and maintain momentum through the 12-week plan!
