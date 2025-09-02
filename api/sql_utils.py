from __future__ import annotations

from typing import Tuple

import sqlglot


def verify_select_only(sql: str) -> Tuple[bool, str | None]:
    try:
        expr = sqlglot.parse_one(sql)
    except Exception as e:  # noqa: BLE001
        return False, f"parse_error: {e}"
    if not isinstance(expr, sqlglot.exp.Select):
        return False, "only SELECT statements are allowed"
    return True, None


def ensure_limit(sql: str, max_rows: int = 100) -> str:
    try:
        expr = sqlglot.parse_one(sql)
        if isinstance(expr, sqlglot.exp.Select):
            if not expr.args.get("limit"):
                expr.set("limit", sqlglot.exp.Limit(this=sqlglot.exp.Literal.number(max_rows)))
            return expr.sql(dialect="trino")
    except Exception:
        pass
    # Fallback: append LIMIT cautiously
    return f"{sql.rstrip(';')} LIMIT {max_rows}"


