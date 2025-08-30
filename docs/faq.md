# FAQ

## What data systems does Stratum support?
Structured via Trino catalogs (e.g., Snowflake, Databricks, Postgres) and unstructured documents via Qdrant.

## Do I need to move data?
No. Stratum executes read-only SQL via Trino and retrieves document passages from your sources; data stays where it is.

## How do agents integrate?
Use the `/ask` API (or SDKs). You can also publish an Agent Spec for governance. No external agent runtime is required.

## What’s returned by `/ask`?
Rows (tabular), verified SQL, metadata (engine, timing), provenance (tables/documents), and optionally document passages and frames for stitching.

## Is there a UI?
Core includes a minimal playground; Enterprise adds a visual builder and admin console.

## How is security handled?
API keys/JWT; roles/scopes; policy enforcement; audit & provenance. Enterprise adds turnkey SSO/SCIM, secret managers, and external policy engines.
