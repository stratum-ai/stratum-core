# PRD — Stratum Core MVP

## Problem
Agents can't reliably query enterprise data due to missing schema context and safe NL→SQL execution.

## Users
- Data/AI engineers (primary)
- Analysts building early copilots (secondary)

## Goals (MVP)
- One backend (DuckDB/Postgres)
- 3 APIs: /describe, /find, /ask
- Qdrant retrieval
- ≥70% NL→SQL on golden set

## Non-Goals
- RBAC, SSO, federated joins

## Acceptance Criteria
- Local deploy \<30m
- Demo answers 10 curated questions
- OpenAPI published; docs live

## Open Questions
- Pick Snowflake **or** Databricks first for enterprise connector?
