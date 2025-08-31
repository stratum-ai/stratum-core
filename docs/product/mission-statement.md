# Mission

## North Star

**Deliver a self-contained, vendor-neutral semantic layer that lets agents ask questions across heterogeneous data via a single `/ask` API, with Trino as the primary execution plane, Qdrant for semantic retrieval, and Postgres for control-plane state.**

## The Problem We Solve

**Enterprise data is fragmented across heterogeneous systems, and AI agents can't navigate it effectively.**

Today's reality:
- Companies use 5+ data systems (Snowflake, Databricks, Postgres, MongoDB, etc.)
- Each has different dialects, access patterns, and query interfaces
- LLMs/agents fail because they lack schema context and safe query execution
- Existing semantic layers are built for humans/BI tools, not programmatic agent access
- Data teams spend 60%+ of time on "plumbing" instead of insights

## Our Mission

**Make enterprise data universally accessible to AI agents through a single, vendor-neutral API.**

Stratum Core provides agents with a unified interface to discover, understand, and safely query data across any source—without vendor lock-in, data movement, or learning system-specific query languages.

## Value Delivered

### For AI/Data Engineers
- **Single API**: One `/ask` endpoint works across Snowflake, Postgres, Databricks, etc.
- **Fast Setup**: Deploy with Trino + Qdrant + Postgres in \<30 minutes
- **Production Ready**: Built-in safety, governance, and observability

### For AI Agent Builders  
- **Semantic Discovery**: `/find` endpoint for table/column discovery via natural language
- **Safe Execution**: Automatic query verification, limits, and read-only enforcement
- **Rich Metadata**: Every response includes provenance, engine info, and execution stats

### For Enterprises
- **Vendor Neutral**: Works with any data source via Trino connectors
- **Governance**: Row/column policies, rate limits, audit trails
- **Cost Transparent**: Query cost tags and resource attribution

> For engineering metrics, acceptance criteria, and delivery targets, see the private `design/` workspace and `docs/roadmap.md`.

## Core Principles

1. **Neutrality First**: Never lock customers into specific vendors or clouds
2. **Agent Native**: APIs designed for LLM/agent consumption, not human UIs  
3. **Security by Default**: Read-only access, query verification, audit trails
4. **Open Core**: Community-driven development with premium enterprise features

## Why Now?

The convergence of three trends makes this the perfect moment:
1. **AI Agents**: Every company is building LLM-powered data applications
2. **Multi-Cloud Data**: Enterprises run 5+ heterogeneous data systems
3. **Semantic Layer Revival**: Modern tools (dbt, Cube) prove the value, but miss agent use cases

Stratum Core bridges this gap by being the first semantic layer built from the ground up for agents, not humans.
