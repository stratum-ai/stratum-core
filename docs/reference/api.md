# API Documentation

Base URL: `/api/v1`

## GET /describe/\{table\}
Return schema, profile, and natural language description for a table.

**Path Parameters:**
- `table` (string): Table name, optionally with catalog prefix (e.g., `warehouse.sales.orders`)

**Response:**
```json
{
  "table": "warehouse.sales.orders",
  "catalog": "warehouse",
  "columns": [
    {
      "name": "order_id", 
      "type": "bigint", 
      "nullable": false,
      "description": "Unique order identifier"
    },
    {
      "name": "customer_id", 
      "type": "bigint", 
      "nullable": false,
      "description": "Foreign key to customers table"
    },
    {
      "name": "total_amount", 
      "type": "decimal(10,2)", 
      "nullable": true,
      "description": "Order total in USD"
    }
  ],
  "profile": {
    "row_count": 128934, 
    "last_updated": "2024-12-01T10:30:00Z",
    "null_percentages": {"total_amount": 0.02}
  },
  "sample_rows": [
    {"order_id": 1, "customer_id": 100, "total_amount": 42.50},
    {"order_id": 2, "customer_id": 101, "total_amount": 15.99}
  ],
  "nl_description": "Customer order transactions with line items and totals"
}
```

## GET /find
Discover relevant tables and columns using semantic and keyword search.

**Query Parameters:**
- `q` (string, required): Search query (e.g., "customer email addresses")
- `limit` (int, optional): Maximum results to return (default: 20)
- `catalogs` (string[], optional): Restrict search to specific catalogs

**Response:**
```json
{
  "query": "customer email addresses",
  "matches": [
    {
      "kind": "column",
      "catalog": "warehouse", 
      "table": "crm.customers",
      "name": "email_address",
      "score": 0.87,
      "description": "Primary email contact for customer"
    },
    {
      "kind": "table",
      "catalog": "warehouse",
      "table": "marketing.email_events", 
      "score": 0.72,
      "description": "Email campaign engagement tracking"
    },
    {
      "kind": "column",
      "catalog": "transactional",
      "table": "users", 
      "name": "email",
      "score": 0.65,
      "description": "User login email"
    }
  ],
  "total_results": 3,
  "search_time_ms": 45
}
```

## POST /ask
Convert natural language to SQL, verify safety, and execute; optionally return document passages and multiple frames.

**Request Body:**
```json
{
  "query": "Top 5 customers by total spend in the last 90 days",
  "max_rows": 100,
  "catalogs": ["warehouse"],  // optional: restrict to specific catalogs
  "explain_only": false       // optional: return SQL without executing
}
```

**Success Response (structured + passages):**
```json
{
  "sql": "SELECT c.customer_id, c.customer_name, SUM(o.total_amount) AS total_spend\nFROM warehouse.sales.orders o\nJOIN warehouse.crm.customers c ON o.customer_id = c.customer_id\nWHERE o.order_date >= CURRENT_DATE - INTERVAL '90' DAY\nGROUP BY c.customer_id, c.customer_name\nORDER BY total_spend DESC\nLIMIT 5",
  "rows": [
    {"customer_id": 42, "customer_name": "Acme Corp", "total_spend": 12345.67},
    {"customer_id": 17, "customer_name": "TechStart Inc", "total_spend": 9876.54}
  ],
  "metadata": {
    "engine": "trino",
    "catalog": "warehouse",
    "routed_reason": "table_resolved", 
    "execution_time_ms": 1247,
    "row_count": 5,
    "bytes_scanned": 1048576,
    "query_cost": 0.023
  },
  "passages": [
    {"doc_id": "s3://bucket/policies/hr.pdf", "page": 12, "snippet": "... refund window is 90 days ...", "score": 0.83}
  ],
  "provenance": {
    "tables": ["warehouse.sales.orders", "warehouse.crm.customers"],
    "columns": ["customer_id", "customer_name", "total_amount", "order_date"],
    "documents": ["s3://bucket/policies/hr.pdf#page=12"],
    "query_id": "trino-20241201-123456-789"
  }
}
```

**Success Response (stitching with frames):**
```json
{
  "frames": [
    {
      "name": "orders",
      "rows": [{"customer_id": 42, "total_spend": 12345.67}],
      "provenance": {"tables": ["snowflake.sales.orders"]}
    },
    {
      "name": "customers",
      "rows": [{"customer_id": 42, "segment": "enterprise"}],
      "provenance": {"tables": ["postgres.crm.customers"]}
    }
  ]
}
```

## Error Responses

All endpoints use consistent error format with appropriate HTTP status codes.

### Error Response Schema
```json
{
  "error": {
    "code": "error_type",
    "message": "Human-readable error description",
    "details": {
      // Additional context specific to error type
    }
  },
  "metadata": {
    "engine": "trino",
    "routed_reason": "routing_failed",
    "request_id": "req-abc123"
  }
}
```

### Common Error Types

**400 Bad Request - Invalid Query**
```json
{
  "error": {
    "code": "invalid_sql",
    "message": "Generated SQL failed validation",
    "details": {
      "sql": "SELECT * FROM nonexistent_table",
      "parse_error": "Table 'nonexistent_table' not found"
    }
  }
}
```

**403 Forbidden - Policy Violation**
```json
{
  "error": {
    "code": "policy_violation", 
    "message": "Query blocked by governance policy",
    "details": {
      "blocked_tables": ["hr.salaries"],
      "policy": "pii_access_restricted"
    }
  }
}
```

**404 Not Found - Resource Missing**
```json
{
  "error": {
    "code": "table_not_found",
    "message": "Table 'unknown_table' not found in any catalog",
    "details": {
      "searched_catalogs": ["warehouse", "transactional"],
      "suggestion": "Check table name or contact admin to add catalog"
    }
  }
}
```

**429 Too Many Requests - Rate Limited**
```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Query rate limit exceeded for tenant",
    "details": {
      "current_rate": "15 queries/minute",
      "limit": "10 queries/minute", 
      "retry_after_seconds": 45
    }
  }
}
```

**500 Internal Server Error - Execution Failed**
```json
{
  "error": {
    "code": "execution_failed",
    "message": "Query execution failed on backend",
    "details": {
      "engine": "trino",
      "engine_error": "Connection timeout to catalog 'warehouse'",
      "query_id": "trino-20241201-123456-789"
    }
  }
}
```

Full schema: see `openapi/semantic.yaml`.
