# Technology Stack

## Core Architecture

### Execution Plane
- **Query Engine**: Trino (primary execution for all sources)
- **Catalogs**: Snowflake, Postgres, MySQL, etc. connected via Trino connectors
- **Routing**: Default to Trino; external sources via catalog configuration
- **Data Formats**: Arrow/Parquet for efficient data exchange

### Control Plane  
- **Database**: Postgres (tenants, connections, policies, API keys, audit)
- **Configuration**: Pydantic models for settings management
- **Orchestration**: Temporal (roadmap - workflow orchestration)

### Semantic Retrieval
- **Vector Store**: Qdrant (semantic similarity search)
- **Embeddings**: OpenAI text-embedding-ada-002 (configurable)
- **Hybrid Search**: Keyword (BM25) + Vector (cosine similarity)
- **Indexing**: Table/column metadata with NL descriptions

### Unstructured Search (Docs)
- **Sources**: S3/GCS/Azure, SharePoint/Drive, Confluence (roadmap)
- **Parsing**: PDF/DOCX/HTML/TXT; chunking + overlap
- **Collections**: `schema_objects` (tables/columns), `documents` (passages)

### API & Planning
- **Web Framework**: FastAPI (Python 3.9+)
- **SQL Processing**: SQLGlot for parsing/validation/safety
- **LLM Provider**: OpenAI GPT-4 (configurable for other providers)
- **Verification**: Read-only enforcement, LIMIT injection, schema validation

### Development & Deployment
- **Language**: Python 3.9+
- **Package Management**: Poetry or pip-tools
- **Testing**: pytest + FastAPI TestClient
- **Containerization**: Docker (Alpine-based)
- **Local Development**: docker-compose or uvicorn

### Future Premium Connectors
- **Snowflake**: snowflake-connector-python
- **Databricks**: databricks-sql-connector
- **BigQuery**: google-cloud-bigquery
- **Authentication**: OAuth2/OIDC via authlib

## Architecture Decisions

### Why Trino as Execution Plane?
- **Universal SQL**: Single query engine for 20+ data source types
- **Production Scale**: Handles petabyte-scale analytics workloads
- **Vendor Neutral**: No lock-in to specific cloud/warehouse vendors
- **Rich Ecosystem**: Active connector development for new sources

### Why Postgres for Control Plane?
- **Transactional**: ACID guarantees for tenant/policy management
- **Mature Ecosystem**: Rich tooling, monitoring, backup solutions  
- **SQL Interface**: Easy admin queries and reporting
- **Deployment Flexibility**: Cloud managed or self-hosted

### Why Qdrant for Retrieval?
- **Purpose-Built**: Optimized for vector similarity search
- **Metadata Filtering**: Combine semantic + structured filters
- **Self-Hostable**: Aligns with vendor neutrality principle
- **Developer Experience**: Good Python SDK and REST API

### Why SQLGlot for Safety?
- **Multi-Dialect**: Parses/validates SQL across 20+ dialects
- **AST Manipulation**: Inject LIMIT, strip DML, validate schemas
- **Lightweight**: Pure Python, no external dependencies
- **Active Development**: Rapidly evolving SQL parser ecosystem

## Performance Targets (MVP)
- `/find` endpoint: \<150ms p95
- `/ask` endpoint: \<5s p95 (including LLM call)
- Concurrent requests: 10+ simultaneous queries
- Memory usage: \<2GB for typical enterprise schemas
