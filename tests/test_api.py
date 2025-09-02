import os

import types
import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("STRATUM_API_KEYS", "dev=devkey")

from api.main import app  # noqa: E402


@pytest.fixture()
def client():
    return TestClient(app)


def auth_headers():
    return {"x-api-key": "devkey"}


def test_health_open(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] in ("ok", "degraded")


def test_auth_required(client):
    r = client.get("/api/v1/find", params={"q": "orders"})
    assert r.status_code == 401


def test_find_with_auth_monkeypatched(client, monkeypatch):
    from api import schema_cache

    def fake_search(q: str, limit: int = 20):
        return [
            {"kind": "table", "catalog": "postgres", "table": "public.orders", "score": 1.0},
            {"kind": "column", "catalog": "postgres", "table": "public.orders", "name": "order_id", "score": 0.9},
        ]

    monkeypatch.setattr(schema_cache.cache, "search", fake_search)
    r = client.get("/api/v1/find", params={"q": "orders"}, headers=auth_headers())
    assert r.status_code == 200
    data = r.json()
    assert data["query"] == "orders"
    assert len(data["matches"]) >= 2


def test_describe_with_auth_monkeypatched(client, monkeypatch):
    import api.main as main_mod

    def fake_parse(s: str):
        class FQTN:
            catalog = "postgres"
            schema = "public"
            table = "orders"

        return FQTN()

    def fake_describe(fqtn):
        return [{"name": "order_id", "type": "bigint"}]

    monkeypatch.setattr(main_mod, "parse_fqtn", fake_parse)
    monkeypatch.setattr(main_mod, "describe_table", fake_describe)
    r = client.get("/api/v1/describe/public.orders", headers=auth_headers())
    assert r.status_code == 200
    data = r.json()
    assert data["table"].endswith("public.orders")
    assert data["columns"][0]["name"] == "order_id"


def test_ask_explain_only(client):
    r = client.post("/api/v1/ask", json={"query": "x", "explain_only": True}, headers=auth_headers())
    assert r.status_code == 200
    data = r.json()
    assert data["verified"] is True
    assert "SELECT" in data["sql"].upper()


