from __future__ import annotations

import threading
from typing import Dict, List, TypedDict

from .trino_utils import get_trino_connection


class TableEntry(TypedDict, total=False):
    kind: str
    catalog: str
    table: str  # schema.table
    score: float


class ColumnEntry(TypedDict, total=False):
    kind: str
    catalog: str
    table: str  # schema.table
    name: str   # column name
    score: float


class SchemaCache:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._tables: List[TableEntry] = []
        self._columns: List[ColumnEntry] = []
        self._warmed = False

    def warm(self) -> None:
        with self._lock:
            if self._warmed:
                return
            conn = get_trino_connection()
            try:
                cur = conn.cursor()
                # Fetch tables
                cur.execute(
                    "SELECT table_catalog, table_schema, table_name FROM system.jdbc.tables"
                )
                for cat, sch, tbl in cur.fetchall():
                    self._tables.append(
                        {
                            "kind": "table",
                            "catalog": cat,
                            "table": f"{sch}.{tbl}",
                        }
                    )
                # Fetch columns (limit rows for safety in large catalogs)
                cur.execute(
                    "SELECT table_catalog, table_schema, table_name, column_name "
                    "FROM system.jdbc.columns LIMIT 100000"
                )
                for cat, sch, tbl, col in cur.fetchall():
                    self._columns.append(
                        {
                            "kind": "column",
                            "catalog": cat,
                            "table": f"{sch}.{tbl}",
                            "name": col,
                        }
                    )
                self._warmed = True
            finally:
                try:
                    conn.close()
                except Exception:
                    pass

    def search(self, query: str, limit: int = 20) -> List[Dict]:
        if not self._warmed:
            self.warm()
        q = query.lower()
        matches: List[Dict] = []
        # simple substring matching
        for t in self._tables:
            if q in t["table"].lower():
                matches.append({**t, "score": 1.0})
                if len(matches) >= limit:
                    return matches
        for c in self._columns:
            if q in c["name"].lower() or q in c["table"].lower():
                matches.append({**c, "score": 0.9})
                if len(matches) >= limit:
                    return matches
        return matches


cache = SchemaCache()


