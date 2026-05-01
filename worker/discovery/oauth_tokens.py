"""OAuth token 持久化 + 自动刷新（抖音 / 千川）。

DB 表 oauth_tokens（迁移 002）：
- (provider, account_id) UNIQUE
- access_token / refresh_token / expires_at / advertiser_id

策略：
- get_token(provider, account_id) → 若 expires_at 还有 >5min 直接返回；否则刷新
- save_token(...) → upsert
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

import httpx
from sqlalchemy import text

from ..db import session_scope

log = logging.getLogger(__name__)

DOUYIN_TOKEN_URL = "https://open.douyin.com/oauth/access_token/"
DOUYIN_REFRESH_URL = "https://open.douyin.com/oauth/refresh_token/"
QIANCHUAN_TOKEN_URL = "https://ad.oceanengine.com/open_api/oauth2/access_token/"
QIANCHUAN_REFRESH_URL = "https://ad.oceanengine.com/open_api/oauth2/refresh_token/"

REFRESH_MARGIN = timedelta(minutes=5)


@dataclass
class OAuthToken:
    provider: str
    account_id: str
    access_token: str
    refresh_token: str | None
    expires_at: datetime | None
    advertiser_id: str | None
    scope: str | None


def _row_to_token(r) -> OAuthToken:
    return OAuthToken(
        provider=r.provider,
        account_id=r.account_id,
        access_token=r.access_token,
        refresh_token=r.refresh_token,
        expires_at=r.expires_at,
        advertiser_id=r.advertiser_id,
        scope=r.scope,
    )


def save_token(
    provider: str,
    account_id: str,
    access_token: str,
    *,
    refresh_token: str | None = None,
    expires_in: int | None = None,
    scope: str | None = None,
    advertiser_id: str | None = None,
) -> None:
    expires_at = (
        datetime.now(UTC) + timedelta(seconds=expires_in) if expires_in else None
    )
    with session_scope() as s:
        s.execute(
            text(
                """
                INSERT INTO oauth_tokens (
                    provider, account_id, access_token, refresh_token,
                    expires_at, scope, advertiser_id
                )
                VALUES (:p, :a, :t, :r, :e, :s, :ad)
                ON CONFLICT (provider, account_id) DO UPDATE SET
                    access_token = EXCLUDED.access_token,
                    refresh_token = COALESCE(EXCLUDED.refresh_token, oauth_tokens.refresh_token),
                    expires_at = EXCLUDED.expires_at,
                    scope = COALESCE(EXCLUDED.scope, oauth_tokens.scope),
                    advertiser_id = COALESCE(EXCLUDED.advertiser_id, oauth_tokens.advertiser_id),
                    updated_at = now()
                """
            ),
            {
                "p": provider,
                "a": account_id,
                "t": access_token,
                "r": refresh_token,
                "e": expires_at,
                "s": scope,
                "ad": advertiser_id,
            },
        )


def _refresh_douyin(refresh_token: str) -> dict:
    client_key = os.environ["DOUYIN_OAUTH_CLIENT_ID"]
    payload = {
        "client_key": client_key,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }
    with httpx.Client(timeout=10.0) as c:
        r = c.post(DOUYIN_REFRESH_URL, params=payload)
        r.raise_for_status()
        return r.json().get("data", {})


def _refresh_qianchuan(refresh_token: str) -> dict:
    payload = {
        "app_id": os.environ["QIANCHUAN_APP_ID"],
        "secret": os.environ["QIANCHUAN_SECRET"],
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }
    with httpx.Client(timeout=10.0) as c:
        r = c.post(QIANCHUAN_REFRESH_URL, json=payload)
        r.raise_for_status()
        return r.json().get("data", {})


def get_token(provider: str, account_id: str) -> OAuthToken | None:
    with session_scope() as s:
        row = s.execute(
            text(
                """
                SELECT provider, account_id, access_token, refresh_token,
                       expires_at, scope, advertiser_id
                FROM oauth_tokens
                WHERE provider = :p AND account_id = :a
                """
            ),
            {"p": provider, "a": account_id},
        ).first()
    if row is None:
        return None

    tok = _row_to_token(row)
    if tok.expires_at and tok.expires_at - datetime.now(UTC) > REFRESH_MARGIN:
        return tok
    if tok.refresh_token is None:
        log.warning("token expired but no refresh_token; provider=%s account=%s", provider, account_id)
        return tok

    try:
        data = (
            _refresh_douyin(tok.refresh_token)
            if provider == "douyin"
            else _refresh_qianchuan(tok.refresh_token)
        )
    except Exception as e:
        log.warning("refresh failed provider=%s: %s", provider, e)
        return tok

    save_token(
        provider,
        account_id,
        data.get("access_token", tok.access_token),
        refresh_token=data.get("refresh_token", tok.refresh_token),
        expires_in=data.get("expires_in"),
    )
    return get_token(provider, account_id)


def exchange_douyin_code(code: str) -> dict:
    """OAuth 授权回调：code → tokens。完成后由调用方 save_token。"""
    payload = {
        "client_key": os.environ["DOUYIN_OAUTH_CLIENT_ID"],
        "client_secret": os.environ["DOUYIN_OAUTH_CLIENT_SECRET"],
        "code": code,
        "grant_type": "authorization_code",
    }
    with httpx.Client(timeout=10.0) as c:
        r = c.post(DOUYIN_TOKEN_URL, params=payload)
        r.raise_for_status()
        return r.json().get("data", {})
