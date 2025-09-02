import os
import socket
from urllib.parse import urlparse

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .models import (
    AskRequest,
    AskResponse,
    DescribeResponse,
    FindResponse,
)
from .trino_utils import describe_table, parse_fqtn
from .schema_cache import cache
from .sql_utils import ensure_limit, verify_select_only
from .qdrant_utils import ensure_schema_collection, list_collections
from .indexer import index_schema_objects
from .security import authenticate
from .db import init_db, session_scope, Tenant

app = FastAPI(title="Stratum Core API", version="0.1.0")


@app.on_event("startup")
def _on_startup():
    try:
        init_db()
    except Exception:
        pass

def _check_tcp(host: str, port: int, timeout: float = 1.0) -> tuple[bool, str]:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True, "ok"
    except Exception as e:  # noqa: BLE001
        return False, str(e)


async def _check_http_get(url: str, timeout: float = 1.5) -> tuple[bool, str]:
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url)
            if 200 <= resp.status_code < 300:
                return True, f"{resp.status_code}"
            return False, f"status={resp.status_code}"
    except Exception as e:  # noqa: BLE001
        return False, str(e)


@app.get("/health")
async def health():
    db_url = os.getenv("STRATUM_DB_URL", "postgresql://stratum:stratum@localhost:5432/stratum")
    trino_url = os.getenv("TRINO_URL", "http://localhost:8080")
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")

    # Postgres: TCP ping
    parsed = urlparse(db_url)
    pg_host = parsed.hostname or "localhost"
    pg_port = int(parsed.port or 5432)
    pg_ok, pg_detail = _check_tcp(pg_host, pg_port)

    # Trino: HTTP /v1/info
    trino_info = trino_url.rstrip("/") + "/v1/info"
    trino_ok, trino_detail = await _check_http_get(trino_info)

    # Qdrant: HTTP /healthz
    qdrant_health = qdrant_url.rstrip("/") + "/healthz"
    q_ok, q_detail = await _check_http_get(qdrant_health)

    # Qdrant ensure collection (best-effort)
    try:
        ensure_schema_collection()
        q_collections = await _check_http_get(qdrant_url.rstrip("/") + "/collections")
    except Exception:
        q_collections = (q_ok, q_detail)

    services = {
        "postgres": {"status": "ok" if pg_ok else "down", "detail": pg_detail},
        "trino": {"status": "ok" if trino_ok else "down", "detail": trino_detail},
        "qdrant": {"status": "ok" if q_ok else "down", "detail": q_detail},
    }
    overall_ok = pg_ok and trino_ok and q_ok
    return {"status": "ok" if overall_ok else "degraded", "services": services}


@app.get("/api/v1/collections")
def collections(request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        names = list_collections()
        return {"collections": names}
    except Exception as e:  # noqa: BLE001
        return JSONResponse({"error": str(e)}, status_code=503)


@app.post("/api/v1/index/schema")
def index_schema(limit_tables: int | None = 50, request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    # Preflight service checks so errors are clear
    trino_url = os.getenv("TRINO_URL", "http://localhost:8080").rstrip("/")
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333").rstrip("/")
    try:
        t_resp = httpx.get(trino_url + "/v1/info", timeout=1.5)
        q_resp = httpx.get(qdrant_url + "/collections", timeout=1.5)
    except Exception as e:  # noqa: BLE001
        return JSONResponse({
            "error": "dependencies_unavailable",
            "detail": str(e),
            "hint": "Start dependencies: docker compose up -d (postgres, qdrant, trino)",
        }, status_code=503)
    if t_resp.status_code >= 300 or q_resp.status_code >= 300:
        return JSONResponse({
            "error": "dependencies_unavailable",
            "trino_status": t_resp.status_code,
            "qdrant_status": q_resp.status_code,
            "hint": "Start dependencies: docker compose up -d (postgres, qdrant, trino)",
        }, status_code=503)
    try:
        count = index_schema_objects(limit_tables=limit_tables)
        return {"indexed": count, "collection": "schema_objects"}
    except Exception as e:  # noqa: BLE001
        return JSONResponse({"error": str(e)}, status_code=500)


@app.post("/api/v1/admin/tenants")
def create_tenant(slug: str, name: str, request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    with session_scope() as s:
        t = Tenant(slug=slug, name=name)
        s.add(t)
        s.commit()
        s.refresh(t)
        return {"id": t.id, "slug": t.slug, "name": t.name}


@app.get("/api/v1/admin/tenants")
def list_tenants(request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    with session_scope() as s:
        rows = s.query(Tenant).all()
        return {"tenants": [{"id": t.id, "slug": t.slug, "name": t.name} for t in rows]}

@app.get("/api/v1/describe/{table}", response_model=DescribeResponse)
def describe(table: str, request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        fqtn = parse_fqtn(table)
        columns = describe_table(fqtn)
        return DescribeResponse(
            table=f"{fqtn.catalog}.{fqtn.schema}.{fqtn.table}",
            columns=columns,
            profile={},
            sample_rows=[],
            nl_description="",
        )
    except ValueError as e:
        return JSONResponse({"error": str(e)}, status_code=400)

@app.get("/api/v1/find", response_model=FindResponse)
def find(q: str, limit: int = 20, request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    raw_matches = cache.search(q, limit=limit)
    return FindResponse(query=q, matches=raw_matches)

@app.post("/api/v1/ask", response_model=AskResponse)
def ask(payload: AskRequest, request: Request):
    principal = authenticate(dict(request.headers))
    if not principal:
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    # Placeholder NL->SQL (to be implemented). For now, echo a baseline SELECT.
    base_sql = "SELECT 1 AS example"
    ok, detail = verify_select_only(base_sql)
    if not ok:
        return JSONResponse({"error": detail or "invalid_sql"}, status_code=400)
    final_sql = ensure_limit(base_sql, max_rows=payload.max_rows or 100)
    if payload.explain_only:
        return AskResponse(sql=final_sql, verified=True, engine="trino", rows=[])
    # Execute against Trino minimal example
    try:
        from .trino_utils import get_trino_connection

        conn = get_trino_connection()
        cur = conn.cursor()
        cur.execute(final_sql)
        rows = cur.fetchall()
    except Exception:
        rows = []
    finally:
        try:
            conn.close()  # type: ignore[has-type]
        except Exception:
            pass
    return AskResponse(sql=final_sql, verified=True, engine="trino", rows=[{"example": r[0]} for r in rows])
