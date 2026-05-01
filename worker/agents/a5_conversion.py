"""A5 Conversion Agent — 千川 / 巨量算数 OAuth 拉取转化数据。

策略（与 v6 §11 + §14.0 数据合规边界一致）：
- 仅自家账号（data_lineage='oauth' 或 'manual' 且属于自家品牌）走真 API
- poc_crawled / public_api（非自家）→ verdict='no_data'，因为：
  1) 没有合法的方式拿到第三方账号的转化数据
  2) 即使有，也不能用作 PoC 数据混入对外通路（PoC 隔离）
- 缺凭据时 verdict='no_creds'，避免 W2 端到端 demo 卡死

W2 实装范围：
- API 调用 shape 完整（千川 Marketing API v1.0 + 巨量算数 OpenAPI）
- 凭据缺失时优雅降级
- 真实 OAuth flow 在 W4 接 §14.4 决策门后启用
"""
from __future__ import annotations

import json
import logging
import os

from sqlalchemy import text
from temporalio import activity

from ..db import session_scope

log = logging.getLogger(__name__)

# 端点常量已迁移到 worker/discovery/qianchuan_client.py


def _has_creds() -> bool:
    """V7 起改用 oauth_tokens 表存的凭据；环境变量只看 ACCOUNT_ID 路由。"""
    return bool(os.getenv("QIANCHUAN_ACCOUNT_ID"))


def _fetch_qianchuan_video_metrics(item_id: str) -> dict:
    """走 oauth_tokens 持久化的 token + advertiser_id（worker/discovery/qianchuan_client.py）。"""
    from ..discovery.qianchuan_client import fetch_metrics

    account_id = os.environ["QIANCHUAN_ACCOUNT_ID"]
    metrics = fetch_metrics(account_id, item_id)
    if metrics is None:
        raise RuntimeError("qianchuan metrics fetch returned None")
    # 把 v3.0 报表的第一行扁平化
    rows = metrics.get("report", {}).get("rows") or []
    flat = rows[0].get("metrics", {}) if rows else {}
    flat["info"] = metrics.get("info", {})
    return flat


def _classify_verdict(metrics: dict) -> str:
    """高赞 ≠ 真带货——用 CTR + cvr + GMV 给一个粗粒度评级。"""
    ctr = float(metrics.get("ctr", 0))
    cvr = float(metrics.get("cvr", 0))
    gmv = float(metrics.get("total_pay_amount", 0))

    if gmv > 50000 and cvr > 0.02:
        return "effective"  # 真有效
    if gmv < 1000 and ctr > 0.05:
        return "virtual"  # 高互动低转化（虚火）
    if ctr > 0.20 and cvr < 0.005:
        return "suspicious"  # 数据可疑（疑刷）
    return "uncertain"


@activity.defn
async def fetch_conversion(case_id: str) -> dict:
    activity.logger.info("A5 Conversion case_id=%s", case_id)

    with session_scope() as s:
        case_row = s.execute(
            text("SELECT data_lineage, url, raw_meta FROM cases WHERE id = :id"),
            {"id": case_id},
        ).first()

        if case_row is None:
            return {"verdict": "case_not_found"}

        lineage = case_row.data_lineage

        if lineage in ("poc_crawled", "public_api"):
            verdict = "no_data"
            confidence = 0.0
            raw = {"reason": "third-party data unavailable under data_lineage policy"}
        elif not _has_creds():
            verdict = "no_creds"
            confidence = 0.0
            raw = {"reason": "QIANCHUAN_API_KEY / DOUYIN_OAUTH_CLIENT_ID not set in env"}
        else:
            try:
                # 从 url 解析 item_id（抖音视频 ID）
                item_id = case_row.url.rstrip("/").split("/")[-1]
                metrics = _fetch_qianchuan_video_metrics(item_id)
                verdict = _classify_verdict(metrics)
                confidence = 0.8 if verdict != "uncertain" else 0.4
                raw = {"metrics": metrics, "item_id": item_id}
            except Exception as e:
                log.warning("A5 Qianchuan API failed: %s", e)
                verdict = "api_error"
                confidence = 0.0
                raw = {"error": str(e)}

        s.execute(
            text(
                """
                INSERT INTO cross_validations (case_id, agent, verdict, confidence, raw_data)
                VALUES (:cid, 'a5_conversion', :v, :c, CAST(:p AS JSONB))
                """
            ),
            {
                "cid": case_id,
                "v": verdict,
                "c": confidence,
                "p": json.dumps(raw, ensure_ascii=False, default=str),
            },
        )

    activity.logger.info("A5 Conversion done case_id=%s verdict=%s", case_id, verdict)
    return {"verdict": verdict, "confidence": confidence}
