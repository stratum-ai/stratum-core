# SDKs & CLI (Core)

## SDKs
- Python: helper for `/describe`, `/find`, `/ask`, retry/backoff, provenance parsing
- TypeScript: browser/server usage for the same

### Python Example
```python
from stratum import Client

c = Client(base_url="http://localhost:8000/api/v1", api_key="...")

result = c.ask(
  query="Top 5 customers by spend last quarter",
  catalogs=["warehouse"],
  max_rows=100
)
print(result.rows)
print(result.metadata.engine, result.provenance.tables)
```

## CLI
- `stratum agents validate spec.yaml`
- `stratum agents publish spec.yaml --tenant acme --version 0.1.0`
- `stratum agents list --tenant acme`

## Integration with Frameworks
- LangGraph/CrewAI starter kits
- Hooks to inject Stratum retrieval context into your tools or nodes

## Observability
- Correlation IDs propagated; optional OTEL export in client
- Cost and latency surfaced via client middleware
