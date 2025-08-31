# Security Interfaces (Pluggable)

These provider contracts enable OSS defaults and Enterprise integrations without code forks.

## AuthProvider
Responsibilities:
- Authenticate requests (API key or JWT)
- Produce `Principal` with tenant, user, roles, scopes

Suggested interface (Python, conceptual):
```python
class Principal(TypedDict):
    tenant_id: str
    user_id: str
    roles: list[str]
    scopes: set[str]
    claims: dict

class AuthProvider(Protocol):
    def authenticate(self, headers: dict[str, str]) -> Principal: ...
```

Implementations:
- Core: ApiKeyAuthProvider, HsJwtAuthProvider, JwksAuthProvider
- Enterprise: OidcAuthProvider (Auth0/Okta/Azure AD), SamlAuthProvider, ScimSyncService

## PolicyProvider
Responsibilities:
- Resolve effective policies for a principal/tenant
- Evaluate table/schema access, column masks, row filters, limits

Suggested interface:
```python
class TableAccess(TypedDict):
    allowed: bool
    reason: str | None

class PolicyProvider(Protocol):
    def get_policies(self, tenant_id: str, user_id: str) -> dict: ...
    def can_access_table(self, fqtn: str, principal: Principal) -> TableAccess: ...
    def column_mask(self, fqcn: str, principal: Principal) -> str | None: ...
    def row_filter(self, fqtn: str, principal: Principal) -> str | None: ...
    def limits(self, principal: Principal) -> dict: ...  # time_ms, row_cap, rate
```

Implementations:
- Core: PostgresPolicyProvider (tables: roles, policies, masks, filters)
- Enterprise: OpaPolicyProvider (Rego), RangerPolicyProvider

## SecretProvider
Responsibilities:
- Store/retrieve connection credentials
- Rotate and audit access

Suggested interface:
```python
class SecretProvider(Protocol):
    def get(self, key: str) -> str: ...
    def set(self, key: str, value: str) -> None: ...
    def rotate(self, key: str) -> None: ...
```

Implementations:
- Core: DbSecretProvider (encrypted values in Postgres)
- Enterprise: VaultSecretProvider, AwsSecretsManagerProvider, AzureKeyVaultProvider

## Integration Points in Request Lifecycle
1. AuthProvider.authenticate → principal/tenant
2. PolicyProvider.get_policies → planning context
3. Verifier uses PolicyProvider to apply masks/filters and enforce limits
4. SecretProvider supplies Trino catalog creds at connection time

## Identity Mapping for RBAC
- OIDC/SAML providers must emit stable `sub`/`user_id`
- Map provider groups/roles to Core roles via configuration
- Store role bindings per tenant in Postgres (Core)

## Configuration
```yaml
security:
  auth_provider: jwks  # api_key | hs_jwt | jwks | oidc | saml
  policy_provider: postgres  # opa | ranger
  secret_provider: db  # vault | aws_secrets_manager | azure_key_vault
  scopes: [describe, find, ask, admin:*]
```

With these contracts, Core ships safe defaults; Enterprise adds integrations by swapping providers.
