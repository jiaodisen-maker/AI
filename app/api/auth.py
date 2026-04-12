"""Authentication API endpoints: Feishu SSO login."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.auth.feishu_sso import FeishuSSO
from app.auth.jwt import create_token
from app.auth.middleware import require_auth

router = APIRouter(prefix="/auth", tags=["auth"])

_sso = FeishuSSO()


class LoginRequest(BaseModel):
    code: str
    redirect_uri: str


class LocalLoginRequest(BaseModel):
    """For development: login with username only."""
    username: str
    role: str = "employee"


@router.get("/feishu/url")
async def feishu_authorize_url(redirect_uri: str, state: str = ""):
    """Get the Feishu OAuth authorize URL."""
    url = _sso.get_authorize_url(redirect_uri, state)
    return {"authorize_url": url}


@router.post("/feishu/callback")
async def feishu_callback(req: LoginRequest):
    """Exchange Feishu OAuth code for JWT token."""
    result = await _sso.login_with_code(req.code, req.redirect_uri)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result


@router.post("/login")
async def local_login(req: LocalLoginRequest):
    """Local login for development (no Feishu required)."""
    from app.config import settings
    if not settings.debug:
        raise HTTPException(
            status_code=403, detail="Local login disabled in production"
        )

    token = create_token(
        user_id=req.username,
        role=req.role,
        extra={"name": req.username, "via": "local"},
    )
    return {
        "token": token,
        "user": {"user_id": req.username, "role": req.role},
    }


@router.get("/me")
async def get_current_user(user: dict = Depends(require_auth)):
    """Get current user info from JWT."""
    return user


@router.get("/permissions")
async def get_permissions(user: dict = Depends(require_auth)):
    """Get current user's RBAC permissions from ontology."""
    from app.auth.rbac import RBACEngine
    from app.main import get_app_state

    state = get_app_state()
    rbac = RBACEngine(ontology_service=state.ontology_service)
    return rbac.get_user_permissions(user.get("role", "employee"))
