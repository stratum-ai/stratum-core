# Trino Catalog Configuration

Configure Trino to connect to warehouse and relational sources.

## File Locations
- Trino container mounts `./trino/etc` to `/etc/trino`
- Catalog files live in `/etc/trino/catalog/*.properties`

## Postgres Catalog Example (`/etc/trino/catalog/postgres.properties`)
```properties
connector.name=postgresql
connection-url=jdbc:postgresql://postgres:5432/warehouse
connection-user=stratum
connection-password=stratum
case-insensitive-name-matching=true
include-system-tables=false
```

## Snowflake Catalog Example (`/etc/trino/catalog/snowflake.properties`)
```properties
connector.name=snowflake
connection-url=jdbc:snowflake://<account>.snowflakecomputing.com
user=<USER>
password=<PASSWORD>
warehouse=<WAREHOUSE>
role=<ROLE>
```

## MySQL Catalog Example (`/etc/trino/catalog/mysql.properties`)
```properties
connector.name=mysql
connection-url=jdbc:mysql://mysql:3306/oltp
connection-user=stratum
connection-password=stratum
```

## Verify Catalogs
```bash
# list catalogs
curl http://localhost:8080/v1/catalog

# query with catalog prefix
curl -X POST http://localhost:8080/v1/statement \
  -H 'X-Trino-User: dev' \
  -H 'X-Trino-Catalog: postgres' \
  -H 'X-Trino-Schema: public' \
  -d 'SELECT * FROM information_schema.tables LIMIT 5'
```

## Best Practices
- Use read-only DB users for all catalogs
- Restrict schemas via Trino config and Stratum policies
- Monitor catalog health; alert on connection failures
