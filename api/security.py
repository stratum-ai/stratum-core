from __future__ import annotations

import os
from typing import Dict, Optional, TypedDict


class Principal(TypedDict, total=False):
    tenant_id: str
    user_id: str
    roles: list[str]
    scopes: list[str]
    claims: dict


def _parse_api_keys_env() -> Dict[str, str]:
    """
    Parse STRATUM_API_KEYS env var into mapping of api_key -> tenant_id.
    Format examples:
      STRATUM_API_KEYS="tenantA=keyA,tenantB=keyB"
    Whitespace is ignored around separators.
    """
    raw = os.getenv("STRATUM_API_KEYS", "")
    mapping: Dict[str, str] = {}
    for pair in filter(None, [p.strip() for p in raw.split(",")]):
        if "=" not in pair:
            continue
        tenant, key = pair.split("=", 1)
        tenant = tenant.strip()
        key = key.strip()
        if tenant and key:
            mapping[key] = tenant
    return mapping


def resolve_api_key_from_headers(headers: dict[str, str]) -> Optional[str]:
    api_key = headers.get("x-api-key") or headers.get("X-API-Key")
    if api_key:
        return api_key.strip()
    auth = headers.get("authorization") or headers.get("Authorization")
    if auth and auth.lower().startswith("bearer "):
        return auth.split(" ", 1)[1].strip()
    return None


def authenticate(headers: dict[str, str]) -> Optional[Principal]:
    api_key = resolve_api_key_from_headers(headers)
    if not api_key:
        return None
    mapping = _parse_api_keys_env()
    tenant = mapping.get(api_key)
    if not tenant:
        return None
    principal: Principal = {
        "tenant_id": tenant,
        "user_id": "api-key",
        "roles": ["default"],
        "scopes": ["describe", "find", "ask"],
        "claims": {},
    }
    return principal


