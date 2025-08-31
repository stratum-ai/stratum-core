# Stratum Announces Stratum Core and New Capabilities for Agentic Data Access

- Stratum Core provides a single `/ask` API that lets AI agents safely query heterogeneous enterprise data
- New governance features make it easier to enforce least‑privilege access, document policy, and audit provenance throughout the lifecycle
- Unified retrieval and execution bring together semantic search over tables/documents with verified SQL on Trino
- Developer experience improvements accelerate going from prompt to production with SDKs, specs, and a minimal playground
- Enterprise options add turnkey SSO/SCIM, secret managers, external policy engines, admin UX, and visual orchestration

SEATTLE—(BUSINESS WIRE)—Stratum today announced Stratum Core, an agent‑native, vendor‑neutral semantic execution layer that helps teams safely build and scale AI experiences on top of their existing data systems. With a single `/ask` API, Stratum retrieves context, plans and verifies SQL, executes on Trino, and returns governed results with full provenance. Customers can adopt AI on Snowflake, Databricks, Postgres, and object storage—without data movement or vendor lock‑in.

“Enterprises shouldn’t have to re‑platform or pick a single vendor to make AI useful,” said the Stratum team. “Stratum Core is a neutral substrate: it gives agents governed access to the data you already have—safely, consistently, and without lock‑in.”

## New governance capabilities in Stratum Core

As the number of models, agents, and users grows, organizations need stronger controls and visibility across the lifecycle.

- Role‑ and scope‑based access: least‑privilege controls for `/describe`, `/find`, and `/ask`
- Policy enforcement in the verifier: read‑only, LIMIT/timeouts, schema validation, column masking, row filters, rate/row/time caps
- Provenance & audit: tables/documents, query metadata, timing, bytes scanned, and routed reason for every response

## Unified retrieval and execution

- Hybrid retrieval: semantic + keyword over schema objects (tables/columns) and document passages (optional)
- Catalog‑aware planning: generate SQL with `catalog.schema.table` context
- Verified execution: SQLGlot guards and Trino execution with catalog routing; optional multi‑catalog stitching returns multiple result frames
- Unstructured support: return relevant passages with ACL‑aware filters and redaction; unified provenance includes `documents`

## Developer experience: faster from prompt to production

- SDKs & tools: Python/TypeScript clients; Agent Spec to declare capabilities/policies; CLI to validate/publish
- Minimal playground: test prompts and inspect SQL/provenance
- Reference templates: plan → verify → execute graphs and examples for LangGraph/CrewAI integration

## Enterprise options (design partner)

- Identity & secrets: OIDC/SAML SSO, SCIM provisioning, Vault/AWS/Azure secret managers
- Governance & compliance: external policy engines (OPA/Ranger), immutable audit, SIEM exports, retention
- Admin UX & orchestration: policy console, query logs, dashboards, and visual agent orchestration with versioning and promotion

## Customer benefits

- Faster time to value: first answers in minutes on existing estates
- Neutral foundation: avoid lock‑in to any single warehouse or framework
- Governed by design: policies applied before execution; full lineage and audit
- Scalable architecture: Trino for execution, vector retrieval for recall, and clear SLOs for latency

## Availability

- Stratum Core (open source) is available today.
- Enterprise features are available via the design partner program.

## Learn more

- Product → Getting Started
- Reference → API
- Engineering → Guides

To inquire about the design partner program, reach out to the team and include a brief description of your data estate (e.g., Snowflake + Databricks + Postgres) and target AI use cases.
