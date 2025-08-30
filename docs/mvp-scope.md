# MVP Scope (60–90 days)

## Problem
Agents/LLMs fail on enterprise data because they lack schema context and a reliable NL→SQL bridge.

## Goals
- Trino execution plane with 2 catalogs (warehouse + relational)
- APIs: `/describe`, `/find`, `/ask`
- Vector retrieval (Qdrant) for schema/table/column search
- ≥70% pass on curated NL→SQL set (Phase 3 target ≥90%)
- Local deploy in \<30 minutes (Docker Compose)

## Non-Goals
- Federated/semantic joins
- RBAC/SSO/governance
- Multi-backend routing

## Success Criteria
- Demo answers 10 curated questions correctly
- Docs site live with "Apply as design partner" CTA
