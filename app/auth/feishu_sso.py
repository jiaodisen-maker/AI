"""Feishu SSO authentication flow.

Allows employees to log in using their Feishu account.
Flow:
  1. User clicks "Login with Feishu"
  2. Redirect to Feishu OAuth authorize URL
  3. Feishu redirects back with code
  4. Exchange code for user info
  5. Issue JWT token with user identity
"""

from __future__ import annotations

import logging
from typing import Any
from urllib.parse import urlencode

import httpx

from app.config import settings

logger = logging.getLogger(__name__)

FEISHU_AUTHORIZE_URL = "https://open.feishu.cn/open-apis/authen/v1/authorize"
FEISHU_ACCESS_TOKEN_URL = "https://open.feishu.cn/open-apis/authen/v2/oauth/token"
FEISHU_USER_INFO_URL = "https://open.feishu.cn/open-apis/authen/v1/user_info"


class FeishuSSO:
    """Feishu OAuth2 SSO handler."""

    def __init__(self) -> None:
        self._http = httpx.AsyncClient(timeout=10)

    def get_authorize_url(self, redirect_uri: str, state: str = "") -> str:
        """Build the Feishu OAuth authorize URL."""
        params = {
            "app_id": settings.feishu_app_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "state": state or "default",
        }
        return f"{FEISHU_AUTHORIZE_URL}?{urlencode(params)}"

    async def exchange_code_for_token(
        self, code: str, redirect_uri: str
    ) -> dict[str, Any]:
        """Exchange authorization code for user access token."""
        if not settings.feishu_app_id:
            return {"error": "Feishu SSO 未配置"}

        try:
            resp = await self._http.post(
                FEISHU_ACCESS_TOKEN_URL,
                json={
                    "grant_type": "authorization_code",
                    "client_id": settings.feishu_app_id,
                    "client_secret": settings.feishu_app_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                },
            )
            data = resp.json()
            return data
        except Exception as e:
            logger.error("Feishu SSO token exchange failed: %s", e)
            return {"error": str(e)}

    async def get_user_info(self, user_access_token: str) -> dict[str, Any]:
        """Get user info from Feishu using user access token."""
        try:
            resp = await self._http.get(
                FEISHU_USER_INFO_URL,
                headers={"Authorization": f"Bearer {user_access_token}"},
            )
            return resp.json()
        except Exception as e:
            logger.error("Feishu user info failed: %s", e)
            return {"error": str(e)}

    async def login_with_code(
        self, code: str, redirect_uri: str
    ) -> dict[str, Any]:
        """Complete login flow: code → token → user info → JWT.

        Returns: {"token": jwt_token, "user": user_info}
        """
        token_data = await self.exchange_code_for_token(code, redirect_uri)
        if "error" in token_data:
            return token_data

        access_token = token_data.get("access_token")
        if not access_token:
            return {"error": "未获取到 access_token"}

        user_data = await self.get_user_info(access_token)
        if "error" in user_data:
            return user_data

        user_info = user_data.get("data", {})
        from app.auth.jwt import create_token

        jwt_token = create_token(
            user_id=user_info.get("user_id", "unknown"),
            role="employee",
            extra={
                "name": user_info.get("name", ""),
                "email": user_info.get("email", ""),
                "department": user_info.get("department", ""),
                "open_id": user_info.get("open_id", ""),
            },
        )

        return {"token": jwt_token, "user": user_info}

    async def close(self) -> None:
        await self._http.aclose()
