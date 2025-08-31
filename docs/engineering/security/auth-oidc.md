# OIDC Authentication Setup

Enable SSO for the Admin/API using OIDC (OpenID Connect).

## Overview
- Identity Provider (IdP): Any OIDC provider (Auth0, Okta, Azure AD, etc.)
- Flow: Authorization Code with PKCE for UI; client credentials for service-to-service
- Tokens: JWT access tokens with tenant and scopes

## Required Environment Variables (example)
```bash
OIDC_ISSUER_URL=https://YOUR_IDP/.well-known/openid-configuration
OIDC_CLIENT_ID=your_client_id
OIDC_CLIENT_SECRET=your_client_secret
OIDC_REDIRECT_URI=https://your-host/admin/callback
OIDC_SCOPES=openid profile email offline_access
```

## Token Claims
- `sub`: user id
- `email`: user email (optional)
- `tid`: tenant id (custom claim)
- `scp`: scopes (e.g., `admin`, `read:queries`, `manage:policies`)

## API Protection
- Verify JWT signature and `aud`, `iss`
- Validate token expiry
- Map `tid` to tenant context
- Enforce scopes per endpoint

## Example Middleware (pseudocode)
```python
from fastapi import Request, HTTPException

async def auth_middleware(request: Request, call_next):
    token = extract_bearer_token(request.headers)
    claims = verify_jwt(token, issuer=ISSUER, audience=CLIENT_ID)
    request.state.tenant_id = claims.get('tid')
    request.state.scopes = set(claims.get('scp', []))
    return await call_next(request)
```

## Scope Model (suggested)
- `read:catalog` – list tables/columns
- `read:queries` – view query logs
- `exec:ask` – execute `/ask`
- `manage:connections` – add/remove catalogs
- `manage:policies` – CRUD row/column policies

## Local Testing
- Use a test IdP (Auth0/Okta dev tenant)
- Create application, set redirect URI, configure scopes
- Obtain token via device code or client credentials

## References
- OIDC spec: `https://openid.net/specs/openid-connect-core-1_0.html`
- Authlib (Python): `https://docs.authlib.org/`
