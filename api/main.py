from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Stratum Core API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/v1/describe/{table}")
def describe(table: str):
    return JSONResponse({"table": table, "columns": [], "profile": {}, "sample_rows": [], "nl_description": ""})

@app.get("/api/v1/find")
def find(q: str):
    return JSONResponse({"query": q, "matches": []})

@app.post("/api/v1/ask")
def ask(payload: dict):
    return JSONResponse({
        "sql": "",
        "verified": False,
        "engine": "trino",
        "rows": [],
        "metadata": {"engine": "trino"},
        "provenance": {"tables": [], "documents": []}
    })
