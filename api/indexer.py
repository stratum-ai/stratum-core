from __future__ import annotations

import hashlib
import json
from typing import Iterable, List

from qdrant_client.http import models as qmodels

from .qdrant_utils import SCHEMA_COLLECTION, get_qdrant_client, ensure_schema_collection
from .trino_utils import get_trino_connection


def _fake_embed(text: str, size: int = 1536) -> List[float]:
    # Placeholder deterministic embedding for dev to avoid real provider usage
    h = hashlib.sha256(text.encode("utf-8")).digest()
    # Repeat hash to fill vector
    vals = list(h) * ((size // len(h)) + 1)
    vec = [float(v) / 255.0 for v in vals[:size]]
    return vec


def iter_schema_objects(limit_tables: int | None = None) -> Iterable[dict]:
    conn = get_trino_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT table_catalog, table_schema, table_name FROM system.jdbc.tables"
        )
        count = 0
        for cat, sch, tbl in cur.fetchall():
            yield {
                "kind": "table",
                "catalog": cat,
                "table": f"{sch}.{tbl}",
                "text": f"table {cat}.{sch}.{tbl}",
            }
            if limit_tables is not None:
                count += 1
                if count >= limit_tables:
                    break
        # columns
        cur.execute(
            "SELECT table_catalog, table_schema, table_name, column_name "
            "FROM system.jdbc.columns"
        )
        for cat, sch, tbl, col in cur.fetchall():
            yield {
                "kind": "column",
                "catalog": cat,
                "table": f"{sch}.{tbl}",
                "name": col,
                "text": f"column {cat}.{sch}.{tbl}.{col}",
            }
    finally:
        try:
            conn.close()
        except Exception:
            pass


def index_schema_objects(limit_tables: int | None = None) -> int:
    ensure_schema_collection()
    client = get_qdrant_client()
    points: List[qmodels.PointStruct] = []
    count = 0
    for obj in iter_schema_objects(limit_tables=limit_tables):
        payload = {k: v for k, v in obj.items() if k != "text"}
        text = obj.get("text", json.dumps(payload))
        vec = _fake_embed(text, size=1536)
        # stable id by hash
        pid = int(hashlib.md5(text.encode("utf-8")).hexdigest()[:16], 16)
        points.append(qmodels.PointStruct(id=pid, vector=vec, payload=payload))
        if len(points) >= 256:
            client.upsert(collection_name=SCHEMA_COLLECTION, points=points)
            count += len(points)
            points.clear()
    if points:
        client.upsert(collection_name=SCHEMA_COLLECTION, points=points)
        count += len(points)
    return count


