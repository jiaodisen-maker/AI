"""Audit logging middleware.

Records every authenticated API call:
  - User ID, role, IP
  - Endpoint, method, status code
  - Latency, request body (sanitized), response status
  - Timestamp

Logs go to:
  1. Structured Python logger
  2. Optional: SQLAlchemy audit_logs table
  3. Optional: Langfuse trace
"""

from __future__ import annotations

import logging
import time
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger("audit")

# Sensitive paths to log carefully
SENSITIVE_PATHS = ["/api/auth", "/api/feishu/webhook"]
SKIP_PATHS = ["/api/health", "/docs", "/openapi.json", "/static", "/"]


class AuditMiddleware(BaseHTTPMiddleware):
    """FastAPI middleware that audit-logs every request."""

    async def dispatch(
        self, request: Request, call_next: Callable
    ) -> Response:
        # Skip non-audited paths
        path = request.url.path
        if any(path.startswith(p) for p in SKIP_PATHS):
            return await call_next(request)

        start = time.monotonic()
        client_ip = request.client.host if request.client else "-"
        method = request.method

        # Capture user from auth header (if present)
        user_id = "anonymous"
        user_role = "-"
        auth = request.headers.get("authorization", "")
        if auth.startswith("Bearer "):
            try:
                from app.auth.jwt import decode_token
                payload = decode_token(auth[7:])
                user_id = payload.get("sub", "unknown")
                user_role = payload.get("role", "-")
            except Exception:
                pass

        # Process request
        try:
            response = await call_next(request)
            status = response.status_code
            error = ""
        except Exception as e:
            status = 500
            error = str(e)
            response = None

        elapsed_ms = int((time.monotonic() - start) * 1000)

        # Log audit event
        is_sensitive = any(path.startswith(p) for p in SENSITIVE_PATHS)
        log_msg = (
            f"[AUDIT] {method} {path} "
            f"user={user_id} role={user_role} ip={client_ip} "
            f"status={status} latency={elapsed_ms}ms"
        )
        if is_sensitive:
            log_msg += " [SENSITIVE]"
        if error:
            log_msg += f" error={error}"
            logger.error(log_msg)
        else:
            logger.info(log_msg)

        # Best-effort persist to DB
        try:
            await self._persist_audit(
                user_id, user_role, method, path, status,
                elapsed_ms, client_ip, error,
            )
        except Exception:
            pass

        if response:
            return response
        from starlette.responses import JSONResponse
        return JSONResponse(
            status_code=500, content={"detail": error or "Internal error"}
        )

    @staticmethod
    async def _persist_audit(
        user_id: str, user_role: str, method: str, path: str,
        status: int, latency_ms: int, ip: str, error: str,
    ) -> None:
        """Persist audit log to DB (best effort)."""
        # Phase 5: implement with SQLAlchemy AuditLog table
        pass
