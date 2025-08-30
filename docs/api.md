# API (MVP)

Base URL: `/api/v1`

## GET /describe/\{table\}
Return schema, simple profile, and NL description.
```json
{
  "table": "orders",
  "columns": [
    {"name": "order_id", "type": "int", "description": "Unique order identifier"},
    {"name": "customer_id", "type": "int", "description": "FK to customers"},
    {"name": "total_amount", "type": "decimal", "description": "Order total"}
  ],
  "profile": {"row_count": 128934, "null_pct": {"total_amount": 0.2}},
  "sample_rows": [{"order_id": 1, "customer_id": 100, "total_amount": 42.50}],
  "nl_description": "Orders placed by customers with totals and keys."
}
```

## GET /find?q=...

Return ranked tables/columns by semantic & keyword match.

```json
{
  "query": "customer email",
  "matches": [
    {"kind": "column", "table": "customers", "name": "email", "score": 0.87},
    {"kind": "table", "table": "email_events", "score": 0.72}
  ]
}
```

## POST /ask

Generate and execute SQL safely.

```json
// Request
{
  "query": "Top 5 customers by total spend last 90 days",
  "max_rows": 100
}

// Response
{
  "sql": "SELECT c.customer_id, SUM(o.total_amount) AS spend\n          FROM orders o JOIN customers c USING (customer_id)\n          WHERE o.order_date >= CURRENT_DATE - INTERVAL '90 days'\n          GROUP BY 1 ORDER BY spend DESC LIMIT 5",
  "verified": true,
  "engine": "duckdb",
  "rows": [
    {"customer_id": 42, "spend": 12345.67}
  ],
  "stats": {"duration_ms": 812, "row_count": 5},
  "provenance": {"tables": ["orders","customers"]}
}
```

Full schema: see `openapi/semantic.yaml`.
