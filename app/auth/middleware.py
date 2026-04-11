"""FastAPI authentication middleware and dependencies."""

from __future__ import annotations

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer

from app.auth.jwt import decode_token
from app.config import settings

bearer_scheme = HTTPBearer(auto_error=False)
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def require_auth(
    bearer: HTTPAuthorizationCredentials | None = Security(bearer_scheme),
    api_key: str | None = Security(api_key_header),
) -> dict:
    """Authenticate via JWT Bearer token or API key.

    Usage: @router.get("/protected", dependencies=[Depends(require_auth)])
    Or:    user = Depends(require_auth)
    """
    # Skip auth in debug mode
    if settings.debug:
        return {"sub": "debug-user", "role": "admin"}

    # Try Bearer JWT
    if bearer and bearer.credentials:
        try:
            return decode_token(bearer.credentials)
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

    # Try API key
    if api_key and api_key == settings.secret_key:
        return {"sub": "api-key-user", "role": "admin"}

    raise HTTPException(status_code=401, detail="Authentication required")
