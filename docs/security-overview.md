# Security Overview

Stratum Core is secure by default and vendor-neutral.

- Authentication: API keys; JWT/JWKS support
- Authorization: roles/scopes; policy enforcement in verifier
- Safety: read-only, LIMIT/timeouts, schema validation
- Provenance: tables/documents + query metadata
- Audit: structured logs (tenant, principal, query_id, timing)

For detailed engineering docs, see:
- `engineering/security-strategy.md`
- `engineering/security-interfaces.md`

Enterprise adds turnkey SSO/SCIM, secret managers, external policy engines, and compliance reporting.
