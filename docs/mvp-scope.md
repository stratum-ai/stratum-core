# MVP Scope (60–90 days)

## Problem
Agents/LLMs fail on enterprise data because they lack schema context and a reliable NL→SQL bridge.

## Goals
- One backend (DuckDB or Postgres)
- APIs: `/describe`, `/find`, `/ask`
- Vector retrieval (Qdrant) for schema/table/column search
- ≥70% pass on golden NL→SQL set
- Local deploy in \<30 minutes

## Non-Goals
- Federated/semantic joins
- RBAC/SSO/governance
- Multi-backend routing

## Success Criteria
- Demo answers 10 curated questions correctly
- Docs site live with "Apply as design partner" CTA
