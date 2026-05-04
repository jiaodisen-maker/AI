"""tenant_access_token 守护进程。

飞书的 tenant_access_token 2 小时过期。提前 10 分钟续，存 Redis 共享。
所有需要调飞书 API 的进程（worker / backfill）通过 current_token() 拿。
"""
from __future__ import annotations

import argparse
import asyncio
import os
import time

import httpx
import yaml
import redis.asyncio as redis

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
APP_ID = os.path.expandvars(CFG["feishu"]["app_id"])
APP_SECRET = os.path.expandvars(CFG["feishu"]["app_secret"])
_r = redis.from_url(CFG["queue"]["url"])
KEY = "feishu:tenant_access_token"
SAFETY_MARGIN_S = 600


async def fetch_new() -> tuple[str, int]:
    async with httpx.AsyncClient() as cli:
        r = await cli.post(
            "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
            json={"app_id": APP_ID, "app_secret": APP_SECRET}, timeout=10)
        r.raise_for_status()
        d = r.json()
        return d["tenant_access_token"], int(d["expire"])


async def current_token() -> str:
    val = await _r.get(KEY)
    if val:
        return val.decode()
    # 兜底：进程没等到 refresher 就启动了
    tok, expire = await fetch_new()
    await _r.set(KEY, tok, ex=max(expire - SAFETY_MARGIN_S, 60))
    return tok


async def loop():
    print("[token_refresher] started", flush=True)
    while True:
        try:
            tok, expire = await fetch_new()
            ttl = max(expire - SAFETY_MARGIN_S, 60)
            await _r.set(KEY, tok, ex=ttl)
            print(f"[token_refresher] refreshed, ttl={ttl}s", flush=True)
            await asyncio.sleep(ttl - 30)
        except Exception as e:
            print(f"[token_refresher] err={e}, retry in 30s", flush=True)
            await asyncio.sleep(30)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cron", action="store_true")
    args = ap.parse_args()
    if args.cron:
        asyncio.run(loop())
    else:
        asyncio.run(fetch_new())


if __name__ == "__main__":
    main()
