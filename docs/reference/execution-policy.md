# Execution Policy

## Routing Rules

### Default Execution
- **Primary Engine**: All queries route to Trino by default
- **Catalog Resolution**: Tables resolved via configured Trino catalogs
- **Fallback**: No fallback engines - if Trino can't handle it, return error

### Source Configuration
```yaml
# Example catalog configuration
catalogs:
  warehouse:
    type: snowflake
    connection: ${SNOWFLAKE_URL}
    schema_discovery: true
  
  transactional: 
    type: postgres
    connection: ${POSTGRES_URL}
    schema_discovery: true
    
  analytics:
    type: databricks
    connection: ${DATABRICKS_URL}
    schema_discovery: false  # Manual schema only
```

### Query Routing Logic
1. **Table Resolution**: Look up table in catalog metadata
2. **Catalog Assignment**: Route to appropriate Trino catalog
3. **Execution**: Submit SQL to Trino with catalog prefix
4. **Response**: Return results with routing metadata

## Response Metadata

### Required Fields
Every `/ask` response MUST include:

```json
{
  "sql": "SELECT ...",
  "rows": [...],
  "metadata": {
    "engine": "trino",
    "catalog": "warehouse", 
    "routed_reason": "table_resolved",
    "execution_time_ms": 1247,
    "row_count": 42,
    "bytes_scanned": 1048576
  },
  "provenance": {
    "tables": ["warehouse.sales.orders", "warehouse.crm.customers"],
    "columns": ["order_id", "customer_name", "total_amount"],
    "documents": ["s3://bucket/doc.pdf#page=12"],
    "query_id": "trino-20241201-123456-789"
  }
}
```

### Routing Reasons
- `table_resolved` - Table found in catalog, routed to appropriate source
- `cross_catalog` - Query spans multiple catalogs (Phase 3+)
- `policy_override` - Special routing due to governance policy
- `manual_catalog` - Explicit catalog specified in query

### Error Responses
```json
{
  "error": {
    "code": "table_not_found",
    "message": "Table 'unknown_table' not found in any catalog",
    "details": {
      "searched_catalogs": ["warehouse", "transactional"],
      "suggestion": "Check table name or contact admin to add catalog"
    }
  },
  "metadata": {
    "engine": "trino",
    "routed_reason": "routing_failed"
  }
}
```

## Safety Policies

### Query Validation (Pre-Execution)
1. **SQL Parsing**: Use SQLGlot to parse and validate syntax
2. **Read-Only Check**: Reject DML/DDL statements (INSERT, UPDATE, DELETE, CREATE, etc.)
3. **Schema Validation**: Verify all referenced tables/columns exist in catalogs
4. **Limit Injection**: Automatically append `LIMIT 1000` if no LIMIT specified

### Runtime Policies  
1. **Execution Timeout**: 30s default, configurable per tenant
2. **Memory Limits**: Enforce via Trino query limits
3. **Row Limits**: Hard cap at 10,000 rows per query
4. **Cost Tracking**: Tag queries with tenant/user for cost attribution

### Governance Integration
```sql
-- Example: Row-level security applied at plan time
-- Original: SELECT * FROM customers  
-- Applied:  SELECT * FROM customers WHERE region = 'us-west'

-- Example: Column masking applied at plan time  
-- Original: SELECT email FROM customers
-- Applied:  SELECT CASE WHEN has_permission('pii') THEN email ELSE '***masked***' END FROM customers
```

## Catalog Management

### Auto-Discovery
- **Schema Crawling**: Periodic jobs discover new tables/columns
- **Metadata Sync**: Keep control plane in sync with source schemas
- **Change Detection**: Alert on schema changes that might break queries

### Manual Override
```yaml
# Override auto-discovered metadata
tables:
  warehouse.sales.orders:
    description: "Customer order transactions with line items"
    columns:
      order_date:
        semantic_type: "timestamp"
        description: "When the order was placed"
      customer_id:
        semantic_type: "foreign_key"
        references: "warehouse.crm.customers.id"
```

### Exclusion Rules
```yaml
# Don't expose certain schemas/tables
exclusions:
  schemas:
    - "warehouse.internal.*"
    - "*.audit_*"
  tables:
    - "warehouse.hr.salaries"  # PII sensitive
  columns:
    - "*.ssn"
    - "*.credit_card_number"
```

## Future Extensions

### Phase 2: Multi-Catalog Queries
- Support queries spanning multiple Trino catalogs
- Cross-catalog join optimization
- Federated result stitching

### Phase 3: External Engines  
- Route specific query types to specialized engines
- Vector database queries for similarity search
- Time-series databases for temporal analytics

### Phase 4: Cost Optimization
- Query cost prediction before execution
- Automatic materialization recommendations  
- Cache-aware routing for repeated queries
