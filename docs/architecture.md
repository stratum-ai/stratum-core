# Architecture (MVP)

## Components
- **Catalog Crawler & Profiler**: enumerate tables/columns, sample values, stats
- **Explainer & Indexer**: NL descriptions + embeddings → VectorStore
- **Retriever**: hybrid (keyword + vector) returns relevant tables/columns
- **Planner**: NL→SQL using schema context
- **Verifier**: EXPLAIN/dry-run, safe guards (SELECT-only, LIMIT)
- **Executor**: run plan on DuckDB/Postgres; return Arrow/Parquet-friendly frames
- **API Layer**: FastAPI exposing `/describe`, `/find`, `/ask`

## Sequence (MVP)

```mermaid
sequenceDiagram
  participant U as User/Agent
  participant API as Stratum API
  participant C as Catalog
  participant V as VectorStore (Qdrant)
  participant DB as Backend (DuckDB/Postgres)

  U->>API: POST /ask {"query": "..."}
  API->>C: load schema + samples
  API->>V: retrieve relevant tables/columns
  API->>API: plan SQL with context
  API->>DB: EXPLAIN (verify schema)
  DB-->>API: plan ok / error
  API->>DB: RUN SELECT (LIMIT N, timeout)
  DB-->>API: rows + stats
  API-->>U: answer + SQL + provenance
```
