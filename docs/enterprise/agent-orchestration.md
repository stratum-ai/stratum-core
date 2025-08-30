# Enterprise Agent Orchestration (Visual Builder)

## Graph Editor
- Drag-and-drop nodes: Retrieve → Plan → Verify → Execute → Tools → Post-process
- Node configs: catalogs, limits, prompts, retries, timeouts
- Policy simulation: evaluate masks/filters before deploy

## Managed Runtime
- Temporal-based orchestration, retries/backoff, circuit breakers
- Human-in-the-loop review steps
- Deploy, canary, rollback; versioned graphs

## Integration
- Import/export to LangGraph/CrewAI code
- Bind secrets and catalogs via UI; role-scoped publishing

## Monitoring & Evals
- Per-node traces, latency/cost dashboards
- Golden-set evals and A/B testing

This is an Enterprise capability; Core remains API/SDK-first with a minimal Playground.
