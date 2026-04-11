"""JWT token creation and validation."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from app.config import settings

ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24


def create_token(
    user_id: str,
    role: str = "user",
    extra: dict[str, Any] | None = None,
    expire_hours: int = TOKEN_EXPIRE_HOURS,
) -> str:
    """Create a signed JWT token."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "role": role,
        "iat": now,
        "exp": now + timedelta(hours=expire_hours),
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT token. Raises jwt.InvalidTokenError on failure."""
    return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
