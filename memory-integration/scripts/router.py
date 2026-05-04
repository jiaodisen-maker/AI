"""MemoryRouter: 写入路由 + 检索融合。

被 mcp_server.py 调用，是 OpenClaw 看不到的底层。
所有写/读必须经过这里，禁止直接操作 GBrain 文件或 Hindsight API。
"""
from __future__ import annotations

import asyncio
import yaml
from dataclasses import dataclass
from pathlib import Path

from .adapters import gbrain, hindsight  # 薄封装，见 adapters/

CONFIG = yaml.safe_load(Path(__file__).parent.parent.joinpath("config.yaml").read_text())


@dataclass
class WriteResult:
    target: str          # "gbrain" | "hindsight" | "both"
    gbrain_path: str | None = None
    hindsight_id: str | None = None


@dataclass
class RecallHit:
    id: str
    text: str
    score: float
    source: str          # "KB" | "MEM"
    ref: str
    ts: str


class MemoryRouter:
    def __init__(self, cfg: dict = CONFIG):
        self.cfg = cfg

    async def write(self, content: str, hints: dict | None = None) -> WriteResult:
        hints = hints or {}
        target = self._classify(content, hints)

        if target == "gbrain":
            path = await gbrain.write_markdown(content, hints)
            return WriteResult("gbrain", gbrain_path=path)

        if target == "hindsight":
            mid = await hindsight.retain(content, hints)
            return WriteResult("hindsight", hindsight_id=mid)

        # both: 双写 + 双向引用
        path = await gbrain.write_markdown(content, hints)
        mid = await hindsight.retain(content, hints | {"gbrain_ref": path})
        await gbrain.append_frontmatter(path, "hindsight_ids", [mid])
        return WriteResult("both", gbrain_path=path, hindsight_id=mid)

    async def recall(self, query: str, k: int = 5) -> list[RecallHit]:
        timeout = self.cfg["recall"]["parallel_timeout_ms"] / 1000
        kk = max(k * 2, 10)

        gb_task = asyncio.create_task(gbrain.hybrid_search(query, k=kk))
        hs_task = asyncio.create_task(hindsight.recall(query, k=kk))

        results: list[RecallHit] = []
        done, pending = await asyncio.wait(
            {gb_task, hs_task}, timeout=timeout
        )
        for t in pending:
            t.cancel()

        for t in done:
            for hit in t.result() or []:
                src = "KB" if t is gb_task else "MEM"
                results.append(RecallHit(
                    id=hit["id"], text=hit["text"], score=hit["score"],
                    source=src, ref=hit.get("ref", hit["id"]),
                    ts=hit.get("ts", ""),
                ))

        return self._rrf_fuse(results, k)

    def _classify(self, content: str, hints: dict) -> str:
        for rule in self.cfg["routing_rules"]:
            if self._match(rule["match"], hints):
                tgt = rule["target"]
                if tgt == "llm_classify":
                    return self._llm_classify(content, hints)
                return tgt
        return "hindsight"  # 安全兜底

    @staticmethod
    def _match(pattern: dict, hints: dict) -> bool:
        if not pattern:
            return True
        for key, allowed in pattern.items():
            v = hints.get(key)
            if isinstance(allowed, list):
                if v not in allowed:
                    return False
            else:
                if v != allowed:
                    return False
        return True

    def _rrf_fuse(self, hits: list[RecallHit], k: int) -> list[RecallHit]:
        k_rrf = self.cfg["recall"]["rrf_k"]
        ranked: dict[str, float] = {}
        by_id: dict[str, RecallHit] = {}
        for source in ("KB", "MEM"):
            same = sorted([h for h in hits if h.source == source],
                          key=lambda h: -h.score)
            for i, h in enumerate(same):
                ranked[h.id] = ranked.get(h.id, 0.0) + 1.0 / (k_rrf + i + 1)
                by_id[h.id] = h
        ordered_ids = sorted(ranked, key=lambda i: -ranked[i])
        return [by_id[i] for i in ordered_ids[:k]]

    def _llm_classify(self, content: str, hints: dict) -> str:
        # 留 stub，接你 gstack 的 brain 层 LLM
        # 简单启发：长文本 → gbrain，短主观 → hindsight
        return "gbrain" if len(content) > 400 else "hindsight"
