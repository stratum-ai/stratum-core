# Agent Spec (Core)

A minimal, declarative spec to bind agents to Stratum capabilities safely.

## Example (YAML)
```yaml
agent:
  name: revenue-qa
  description: Answer revenue questions across catalogs
  version: 0.1.0

capabilities:
  catalogs: [warehouse, transactional]
  max_rows: 1000
  timeouts_ms: 5000
  use_retrieval: semantic+keyword

policies:
  allow_tables:
    - warehouse.sales.*
    - warehouse.crm.customers
  block_tables:
    - warehouse.hr.*
  column_masks:
    email: "***masked***"
  row_filters:
    warehouse.sales.orders: "region = 'us-west'"

scopes: [describe, find, ask]

observability:
  correlation_tags: [team:analytics, env:dev]
```

## Lifecycle
- Validate: CLI checks schema and policy references
- Publish: store in control plane with version
- Bind: agent user/service gets roles/scopes derived from spec

## Runtime
- The spec informs planner/verifier context and enforcement
- Changes require a version bump and re-publish

See also: `sdk-cli.md` for validation and publish commands.
