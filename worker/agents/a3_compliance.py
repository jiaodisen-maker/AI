"""A3 Compliance Agent — 14 类违禁词扫描 + LLM 双验。

策略（与 v6 §14.0 / §14.9 一致）：
1) yaml 词库是 source of truth — 正则命中即权威判定
2) LLM 双验只能补充（写 hitl_alert(compliance_edge)），不能否决正则
3) 命中按 severity 写 atoms.compliance_grade（red→R, yellow→Y）
4) 每个 case 总会写一行 cross_validations.agent='a3_compliance'，verdict ∈ {green, yellow, red}
"""
from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml
from sqlalchemy import text
from temporalio import activity

from ..db import session_scope
from ..llm import call_deepseek

log = logging.getLogger(__name__)

RULES_PATH = Path(__file__).resolve().parents[2] / "rules" / "banned_terms_14categories.yaml"


@dataclass(frozen=True)
class CompiledCategory:
    id: str
    name_cn: str
    severity: str
    patterns: tuple[re.Pattern, ...]


@lru_cache(maxsize=1)
def _load_rules() -> list[CompiledCategory]:
    raw = yaml.safe_load(RULES_PATH.read_text(encoding="utf-8"))
    out: list[CompiledCategory] = []
    for cat in raw["categories"]:
        compiled = tuple(re.compile(p) for p in (cat.get("patterns") or []))
        out.append(
            CompiledCategory(
                id=cat["id"],
                name_cn=cat["name_cn"],
                severity=cat.get("severity", "yellow"),
                patterns=compiled,
            )
        )
    return out


def _scan_text(text_in: str) -> list[dict]:
    """Return list of hits: {category_id, name_cn, severity, matched_term, context}."""
    if not text_in:
        return []
    hits: list[dict] = []
    for cat in _load_rules():
        for pat in cat.patterns:
            for m in pat.finditer(text_in):
                start, end = m.span()
                ctx = text_in[max(0, start - 20) : min(len(text_in), end + 20)]
                hits.append(
                    {
                        "category_id": cat.id,
                        "name_cn": cat.name_cn,
                        "severity": cat.severity,
                        "matched_term": m.group(0),
                        "context": ctx,
                    }
                )
    return hits


def _verdict_from_hits(hits: list[dict]) -> str:
    if any(h["severity"] == "red" for h in hits):
        return "red"
    if any(h["severity"] == "yellow" for h in hits):
        return "yellow"
    return "green"


def _grade_from_severity(severity: str) -> str:
    return {"red": "R", "yellow": "Y"}.get(severity, "G")


_LLM_DOUBLE_CHECK_SYSTEM = """你是保健品广告合规专家。给定一段文本，判断是否触犯如下 14 类违禁规则中任一类。

14 类（仅列出名称，请按编号回答）：
01_efficacy 疗效宣称 / 02_promise 效果承诺 / 03_absolute 绝对化用语 / 04_comparison 同行贬损
05_medical_device 医疗器械混淆 / 06_extreme_words 极限词 / 07_celebrity_endorsement 明星患者代言
08_tcm_efficacy 中医功效话术 / 09_age_discrimination 年龄歧视 / 10_gender_discrimination 性别歧视
11_data_fabrication 数据造假 / 12_pseudoscience 伪科学 / 13_medical_institution 医院医保背书
14_special_groups 特殊人群

输出严格 JSON（不要 markdown，仅输出 JSON 对象）：
{"hits": [{"category_id": "01_efficacy", "evidence": "..."}, ...], "overall": "red|yellow|green"}"""


def _llm_double_check(text_in: str) -> dict:
    if not text_in.strip():
        return {"hits": [], "overall": "green"}
    try:
        out = call_deepseek(
            _LLM_DOUBLE_CHECK_SYSTEM,
            text_in,
            temperature=0.0,
            response_format_json=True,
        )
        return json.loads(out)
    except Exception as e:
        log.warning("A3 LLM double-check failed (non-fatal): %s", e)
        return {"hits": [], "overall": "green", "error": str(e)}


@activity.defn
async def scan_compliance(case_id: str) -> dict:
    activity.logger.info("A3 Compliance scanning case_id=%s", case_id)

    with session_scope() as s:
        rows = s.execute(
            text(
                """
                SELECT id, segment_type, asr_text, ocr_text
                FROM case_segments WHERE case_id = :cid
                """
            ),
            {"cid": case_id},
        ).all()

        all_hits: list[dict] = []
        for seg in rows:
            text_combined = " ".join(filter(None, [seg.asr_text, seg.ocr_text]))
            hits = _scan_text(text_combined)
            for h in hits:
                h["segment_id"] = str(seg.id)
                h["segment_type"] = seg.segment_type
            all_hits.extend(hits)

            llm_view = _llm_double_check(text_combined)
            regex_cats = {h["category_id"] for h in hits}
            llm_extra = [
                e for e in llm_view.get("hits", []) if e.get("category_id") not in regex_cats
            ]
            if llm_extra:
                s.execute(
                    text(
                        """
                        INSERT INTO hitl_alerts (alert_type, payload)
                        VALUES ('compliance_edge', CAST(:p AS JSONB))
                        """
                    ),
                    {
                        "p": json.dumps(
                            {
                                "case_id": case_id,
                                "segment_id": str(seg.id),
                                "regex_hits": hits,
                                "llm_extra": llm_extra,
                            },
                            ensure_ascii=False,
                        )
                    },
                )

        verdict = _verdict_from_hits(all_hits)

        # 写 atoms.compliance_grade — 把命中 segment 涉及到的 atoms 升级
        for h in all_hits:
            grade = _grade_from_severity(h["severity"])
            s.execute(
                text(
                    """
                    UPDATE atoms
                    SET compliance_grade = :g
                    WHERE source_segment_id = :sid
                      AND (compliance_grade IS NULL
                           OR (:g = 'R')
                           OR (:g = 'Y' AND compliance_grade = 'G'))
                    """
                ),
                {"g": grade, "sid": h["segment_id"]},
            )

        # 没命中的 atoms 默认绿色
        s.execute(
            text(
                """
                UPDATE atoms SET compliance_grade = 'G'
                WHERE source_case_id = :cid AND compliance_grade IS NULL
                """
            ),
            {"cid": case_id},
        )

        s.execute(
            text(
                """
                INSERT INTO cross_validations (case_id, agent, verdict, confidence, raw_data)
                VALUES (:cid, 'a3_compliance', :v, :c, CAST(:p AS JSONB))
                """
            ),
            {
                "cid": case_id,
                "v": verdict,
                "c": 1.0,  # regex-driven decision is deterministic
                "p": json.dumps({"hits": all_hits}, ensure_ascii=False),
            },
        )

    activity.logger.info("A3 Compliance done case_id=%s verdict=%s hits=%d", case_id, verdict, len(all_hits))
    return {"verdict": verdict, "hit_count": len(all_hits)}
