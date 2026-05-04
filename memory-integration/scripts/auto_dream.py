"""autoDream 守护进程：Hindsight ↔ GBrain 的睡眠时凝固。

调度方式：
  python auto_dream.py --once          # 跑一次 scope=recent
  python auto_dream.py --cron          # 内置每小时调度
  python auto_dream.py --scope all     # 全量整合（建议每周日凌晨）
"""
from __future__ import annotations

import argparse
import asyncio
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta

import yaml
from pathlib import Path

from .adapters import gbrain, hindsight, notify

CFG = yaml.safe_load(Path(__file__).parent.parent.joinpath("config.yaml").read_text())
THRESH = CFG["consolidation"]


@dataclass
class Conflict:
    path: str
    old: str
    new: str
    hindsight_id: str


async def consolidate(scope: str = "recent", dry_run: bool = False) -> dict:
    report = {
        "consolidated_entities": 0,
        "appended_beliefs": 0,
        "indexed_docs": 0,
        "conflicts": [],
    }

    # ① 凝固：稳定 Entity → markdown
    entities = await hindsight.stable_entities(
        min_age_hours=THRESH["min_age_hours"],
        min_confidence=THRESH["min_confidence"],
        min_observations=THRESH["min_observation_count"],
        scope=scope,
    )
    for e in entities:
        path = f"brain/people/{e.slug}.md" if e.kind == "person" \
               else f"brain/{e.kind}/{e.slug}.md"
        existing = await gbrain.read(path)
        if existing and _conflicts(existing, e.to_markdown()):
            report["conflicts"].append(Conflict(path, existing, e.to_markdown(), e.id))
            continue
        if not dry_run:
            await gbrain.upsert_markdown(path, e.to_markdown())
            await hindsight.mark_archived(e.id, gbrain_path=path)
        report["consolidated_entities"] += 1

    # ② 信念追加：高置信 belief → 档案 ## 观察 段
    beliefs = await hindsight.stable_beliefs(min_confidence=THRESH["min_confidence"])
    for b in beliefs:
        if not b.subject_ref:
            continue
        if not dry_run:
            await gbrain.append_section(b.subject_ref, "观察", b.to_markdown())
            await hindsight.mark_archived(b.id, gbrain_path=b.subject_ref)
        report["appended_beliefs"] += 1

    # ③ 反向同步：GBrain 新文档 → Hindsight World Facts
    since = datetime.utcnow() - timedelta(hours=24 if scope == "recent" else 24 * 30)
    for doc in await gbrain.changed_since(since):
        if not dry_run:
            await hindsight.retain(
                doc.summary,
                meta={"network": "world_facts", "gbrain_ref": doc.path},
            )
        report["indexed_docs"] += 1

    # ④ 冲突推审核
    if THRESH["conflict_strategy"] == "human_review":
        for c in report["conflicts"]:
            await notify.send_review(c)

    report["conflicts"] = [c.__dict__ for c in report["conflicts"]]
    return report


def _conflicts(old_md: str, new_md: str) -> bool:
    # 极简：如果新版本删除了旧版本超过 30% 内容就算冲突
    old_lines = set(filter(None, old_md.splitlines()))
    new_lines = set(filter(None, new_md.splitlines()))
    if not old_lines:
        return False
    removed = (old_lines - new_lines)
    return len(removed) / len(old_lines) > 0.3


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--cron", action="store_true")
    ap.add_argument("--scope", default="recent", choices=["recent", "all"])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.once or not args.cron:
        report = await consolidate(args.scope, args.dry_run)
        print(report)
        return

    while True:
        try:
            report = await consolidate("recent", False)
            print(f"[{datetime.utcnow().isoformat()}] {report}")
        except Exception as e:
            print(f"consolidate failed: {e}", file=sys.stderr)
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
