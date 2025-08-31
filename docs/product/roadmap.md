# Roadmap

## 🧱 Phase 1 — Core Surface (Weeks 1–4)

**Goal**: One coherent API that works end-to-end with production-grade building blocks.

### Deliverables
- [x] Public API service exposing `/describe/{table}`, `/find?q=...`, `/ask`
- [ ] Planner & Verifier with SQL safety layer
- [ ] Catalog & Retrieval with semantic + keyword search  
- [ ] Control plane with tenants, connections, policies, API keys, audit
- [ ] Trino execution engine with multi-catalog support
 - [ ] Unstructured retrieval (documents) MVP: ingest + search + passages

### Acceptance Criteria
- [ ] 15 curated questions execute successfully against 2 real data sources
- [ ] p95 `/ask` \<5s on those questions
- [ ] 100% responses include `engine="trino"`, provenance, and routed_reason

---

## 🔌 Phase 2 — Connectors & Governance (Weeks 5–8)

**Goal**: Credible enterprise pilots.

### Deliverables
- [ ] Source connectors via Trino (Snowflake + Postgres/MySQL catalogs)
- [ ] Policy/Guardrails (org/role policies, blocked schemas, column masks, row filters)
- [ ] Observability (structured logs, metrics, latency tracking)
- [ ] Security (OIDC SSO, secrets management, read-only source creds)
 - [ ] Unstructured connectors: S3/GCS/Azure; ACL-aware retrieval

### Acceptance Criteria
- [ ] Pilot environment runs with 2+ distinct enterprise sources
- [ ] Policy tests: masked columns never leak, blocked schemas rejected, limits enforced
- [ ] Basic admin view for connections/policies/query logs operational

---

## 🧠 Phase 3 — Accuracy, Reliability & Outcomes (Weeks 9–12)

**Goal**: Make it trustworthy and impressive.

### Deliverables
- [ ] Evaluation harness with golden NL→SQL test suite
- [ ] Planner improvements (better joins, time filters, semantic synonyms)
- [ ] Stitching (lite) - multiple result frames for one question
 - [ ] Unified responses: rows + document passages + provenance
- [ ] Design-partner readiness (pilot playbook, runbooks, support process)

### Acceptance Criteria
- [ ] ≥90% execution accuracy on golden NL→SQL test suite
- [ ] Retrieval recall@k baseline established for table/column discovery
- [ ] 1+ public reference case study completed

---

## 💵 Phase 4 — Commercialization (Weeks 13+)

**Goal**: Sustainable business model and growth.

### Deliverables
- [ ] Design Partner Pilot program (90 days, fixed fee, 2-3 sources, 20 questions)
- [ ] Enterprise offering (annual subscriptions, premium governance & support)
- [ ] Additional catalogs (BigQuery, MongoDB, time-series databases)
- [ ] Reference agent kits (LangGraph/CrewAI integration examples)

### Commercial Artifacts
- [ ] Docs site CTA "Apply as Design Partner" → intake form
- [ ] One-pager PDF + reference demo script + buyer FAQ
- [ ] Pricing model for Design Partner vs Enterprise tiers
