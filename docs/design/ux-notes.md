# UX Notes — Playground & Admin (MVP)

## Playground
- Single input box → shows:
  - Generated SQL (read-only)
  - Result table
  - Provenance (tables used)
- Error states:
  - Verification failure (unknown column/table)
  - Timeout/row limit exceeded
- Instrumentation:
  - Latency, token usage (if using an LLM), row count

## Admin (later)
- Data sources list
- Index status (collections, vectors)
- Query logs (PII-safe)
