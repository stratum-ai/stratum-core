from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Tuple
from urllib.parse import urlparse

import trino


@dataclass
class FullyQualifiedTableName:
    catalog: str
    schema: str
    table: str


def parse_fqtn(table_str: str, default_catalog: str = "postgres") -> FullyQualifiedTableName:
    parts = table_str.split(".")
    if len(parts) == 3:
        catalog, schema, table = parts
    elif len(parts) == 2:
        catalog = default_catalog
        schema, table = parts
    else:
        raise ValueError("table must be 'schema.table' or 'catalog.schema.table'")
    return FullyQualifiedTableName(catalog=catalog, schema=schema, table=table)


def _parse_trino_env() -> Tuple[str, int, str, str]:
    url = os.getenv("TRINO_URL", "http://localhost:8080")
    user = os.getenv("TRINO_USER", "stratum")
    parsed = urlparse(url)
    host = parsed.hostname or "localhost"
    port = int(parsed.port or 8080)
    scheme = parsed.scheme or "http"
    return host, port, scheme, user


def get_trino_connection(catalog: str | None = None, schema: str | None = None):
    host, port, scheme, user = _parse_trino_env()
    # catalog/schema optional; queries will use fully-qualified names
    conn = trino.dbapi.connect(
        host=host,
        port=port,
        user=user,
        http_scheme=scheme,
        catalog=catalog,
        schema=schema,
    )
    return conn


def describe_table(fqtn: FullyQualifiedTableName) -> List[dict]:
    query = (
        f"SELECT column_name, data_type, is_nullable "
        f"FROM {fqtn.catalog}.information_schema.columns "
        f"WHERE table_schema = ? AND table_name = ? "
        f"ORDER BY ordinal_position"
    )
    conn = get_trino_connection()
    try:
        cur = conn.cursor()
        cur.execute(query, (fqtn.schema, fqtn.table))
        rows = cur.fetchall()
    finally:
        try:
            conn.close()
        except Exception:
            pass
    columns = [
        {
            "name": r[0],
            "type": r[1],
            # nullable omitted from public schema for OSS response alignment
        }
        for r in rows
    ]
    return columns


