"""TTL Purge — 清理 30 天前的 poc_crawled 数据 + MinIO 媒体对象。

职责（与 §14.9 风险护栏 + §14.0 PoC 隔离一致）：
1) 删除 cases.data_lineage='poc_crawled' AND poc_purge_at < now()
2) FK ON DELETE CASCADE 自动连带删 case_segments / cross_validations
3) atoms.source_case_id ON DELETE SET NULL — atoms (embedding/content) 保留供 DSPy 训练
4) MinIO 中 workflow_id 前缀的 raw 视频 / ASR / OCR 中间产物全删
5) 任何对象删除失败 → 写 hitl_alert(poc_purge_failed)
6) 清理日志归档（追加到 storage/poc_purge.log）

运行：
- 一次性：python scripts/poc_purge.py
- 定时：cron 每天 03:00 跑（或 Temporal Schedule）
"""
import json
import logging
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import text

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from worker.db import session_scope  # noqa: E402

LOG_PATH = Path(os.getenv("POC_PURGE_LOG", "storage/poc_purge.log"))
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("poc_purge")


def _purge_minio(workflow_ids: list[str]) -> tuple[int, list[str]]:
    """返回 (deleted_count, failed_keys)"""
    deleted = 0
    failed: list[str] = []
    if not workflow_ids:
        return 0, []
    try:
        from worker.storage import get_minio_client
    except Exception as e:
        log.warning("MinIO client import failed: %s", e)
        return 0, [f"<import error: {e}>"]

    bucket = os.getenv("MINIO_BUCKET", "cases-media")
    client = get_minio_client()
    if not client.bucket_exists(bucket):
        log.info("Bucket %s does not exist; skip", bucket)
        return 0, []

    for wf_id in workflow_ids:
        try:
            objects = list(client.list_objects(bucket, prefix=f"{wf_id}/", recursive=True))
            for obj in objects:
                try:
                    client.remove_object(bucket, obj.object_name)
                    deleted += 1
                except Exception as e:
                    log.warning("delete %s failed: %s", obj.object_name, e)
                    failed.append(obj.object_name)
        except Exception as e:
            log.warning("list bucket prefix %s failed: %s", wf_id, e)
            failed.append(f"<list error wf={wf_id}: {e}>")
    return deleted, failed


def _write_audit(stats: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {"ts": datetime.now(UTC).isoformat(), "event": "poc_purge", "stats": stats}
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")


def main() -> int:
    log.info("PoC purge starting")

    with session_scope() as s:
        rows = s.execute(
            text(
                """
                SELECT id, workflow_id, ingested_at, poc_purge_at
                FROM cases
                WHERE data_lineage = 'poc_crawled'
                  AND poc_purge_at IS NOT NULL
                  AND poc_purge_at < now()
                """
            )
        ).all()
        candidates = [{"case_id": str(r.id), "workflow_id": r.workflow_id} for r in rows]

    log.info("Found %d candidate poc_crawled cases past TTL", len(candidates))
    if not candidates:
        _write_audit({"deleted_cases": 0, "deleted_objects": 0, "failed_objects": []})
        return 0

    # 1) 先删 MinIO 对象（失败可重跑，DB 还在）
    workflow_ids = [c["workflow_id"] for c in candidates if c["workflow_id"]]
    obj_deleted, failed = _purge_minio(workflow_ids)
    log.info("MinIO: deleted=%d failed=%d", obj_deleted, len(failed))

    # 2) 删 DB cases — FK CASCADE 连带 segments / cross_validations；atoms.source_case_id SET NULL
    case_ids = [c["case_id"] for c in candidates]
    with session_scope() as s:
        # 把 atoms 中可能引用的 source_segment_id 也置 NULL（FK already does this）
        s.execute(
            text(
                """
                DELETE FROM cases
                WHERE id = ANY(CAST(:ids AS UUID[]))
                """
            ),
            {"ids": "{" + ",".join(case_ids) + "}"},
        )
        if failed:
            s.execute(
                text(
                    """
                    INSERT INTO hitl_alerts (alert_type, payload)
                    VALUES ('poc_purge_failed', CAST(:p AS JSONB))
                    """
                ),
                {
                    "p": json.dumps(
                        {
                            "failed_objects": failed,
                            "case_ids": case_ids,
                            "ts": datetime.now(UTC).isoformat(),
                        },
                        ensure_ascii=False,
                    )
                },
            )

    stats = {
        "deleted_cases": len(case_ids),
        "deleted_objects": obj_deleted,
        "failed_objects": failed,
        "case_ids": case_ids,
    }
    _write_audit(stats)
    log.info("PoC purge done: %s", stats)
    return 0 if not failed else 2


if __name__ == "__main__":
    sys.exit(main())
