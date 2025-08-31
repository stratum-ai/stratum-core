# Unstructured Data Support

Goal: let agents ask questions that may require facts from documents, logs, or pages—under the same policy and provenance model.

## Scope
- Document sources: S3/GCS/Azure Blob, SharePoint/Drive, Confluence/Wiki, Websites
- Formats: PDF, DOCX, HTML/MD, TXT, JSON/Logs
- Index: chunking + embeddings (Qdrant); optional keyword store

## Ingestion (Pipeline)
1. Connectors pull documents and metadata (path, owner, timestamps, ACLs)
2. Parse & chunk (e.g., 1–2k tokens) with overlap; normalize text
3. Generate NL summaries and embeddings; store in Qdrant with metadata
4. Store source metadata in control plane (for provenance and policy)

## Retrieval
- Hybrid search over chunks (semantic + keyword)
- Ranking and deduplication; diversity by document/source
- Return passages with document IDs and anchors (page/section)

## Planning with Structured Data
- Use retrieved passages as context alongside table/column context
- If question is purely unstructured, answer from passages
- If mixed, proceed with plan → verify → execute on Trino, then enrich answer with passages

## Response & Provenance
```json
{
  "rows": [...],
  "passages": [
    {
      "doc_id": "s3://bucket/policies/hr.pdf",
      "page": 12,
      "snippet": "... masking requirements ...",
      "score": 0.83
    }
  ],
  "provenance": {
    "tables": ["snowflake.sales.orders"],
    "documents": ["s3://bucket/policies/hr.pdf#page=12"]
  }
}
```

## Governance & Security
- Respect source ACLs during retrieval (filter by tenant/role/labels)
- PII masking in passages; redact before return
- Per-connector allowlists/denylists; domain and path scoping

## Connectors (roadmap)
- S3/GCS/Azure Blob (Core)
- SharePoint/Drive, Confluence/Jira (Enterprise)
- Crawler for internal sites (Enterprise)

## Costs & Performance
- Batch ingestion; incremental updates by mtime/etag
- Embedding cache; adaptive chunk sizes; passage result caps

## Developer Notes
- Use existing Qdrant; add a `documents` collection
- Add `documents` to `/find` results with `kind: "document"`
- Extend `/ask` to optionally return `passages` when relevant
