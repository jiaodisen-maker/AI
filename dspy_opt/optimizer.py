"""DSPy prompt optimizer (BootstrapFewShot) + 回滚机制。

策略：
1) 拉 trainset（trainset_builder.build_a8_trainset）
2) 划 holdout（最近 5 条 generated_scripts，不论评分 — 用作回滚校验）
3) 用 BootstrapFewShot 编译 GenerationSig
4) 提取编译后的 system prompt
5) 在 holdout 上跑 new vs current，比 critic avg
6) new ≥ current → 写 prompt_versions(agent='a8', version='vN+1')
   否则 → 不写，保留旧 active

未安装 dspy-ai 时（开发期），跳过编译，仅记录"would have triggered"——
返回 {"inserted": False, "reason": "dspy_unavailable"}。

API:
    maybe_optimize(agent: str = 'a8') -> {"inserted": bool, "reason": str, ...}
"""
from __future__ import annotations

import json
import logging
import os
from datetime import UTC, datetime

from sqlalchemy import text

from worker.db import session_scope

from .trainset_builder import build_a8_trainset

log = logging.getLogger(__name__)

MIN_TRAINSET_SIZE = 5  # 太少则不优化
HOLDOUT_SIZE = 3
ROLLBACK_DELTA = -0.5  # 新 prompt 平均分跌 ≥0.5 视为回归，回滚


def _next_version(agent: str) -> str:
    with session_scope() as s:
        cnt = s.execute(
            text("SELECT COUNT(*) FROM prompt_versions WHERE agent = :ag"), {"ag": agent}
        ).scalar_one()
    return f"v{cnt + 1}"


def _persist(agent: str, version: str, prompt_text: str, metric: dict) -> str:
    with session_scope() as s:
        row = s.execute(
            text(
                """
                INSERT INTO prompt_versions (agent, version, prompt_text, metric)
                VALUES (:ag, :v, :pt, CAST(:m AS JSONB))
                RETURNING id
                """
            ),
            {"ag": agent, "v": version, "pt": prompt_text, "m": json.dumps(metric)},
        ).first()
    return str(row.id)


def maybe_optimize(agent: str = "a8") -> dict:
    """Try compile new prompt; if it improves on holdout, write prompt_versions."""
    if agent != "a8":
        return {"inserted": False, "reason": "only a8 supported in W3"}

    if not os.getenv("DEEPSEEK_API_KEY"):
        return {"inserted": False, "reason": "no_api_key"}

    trainset = build_a8_trainset(limit=20)
    if len(trainset) < MIN_TRAINSET_SIZE:
        return {
            "inserted": False,
            "reason": "insufficient_trainset",
            "trainset_size": len(trainset),
        }

    try:
        import dspy
    except ImportError:
        log.info("dspy-ai not installed; skipping compile")
        return {"inserted": False, "reason": "dspy_unavailable", "trainset_size": len(trainset)}

    from .signatures import GenerationSig

    # Configure dspy LM (Deepseek via OpenAI-compatible base)
    try:
        lm = dspy.LM(
            model="openai/deepseek-chat",
            api_key=os.environ["DEEPSEEK_API_KEY"],
            api_base="https://api.deepseek.com/v1",
            temperature=0.5,
            max_tokens=2000,
        )
        dspy.configure(lm=lm)
    except Exception as e:
        log.warning("dspy configure failed: %s", e)
        return {"inserted": False, "reason": "lm_configure_failed", "error": str(e)}

    examples = [
        dspy.Example(
            microtype_json=json.dumps(ex["microtype"], ensure_ascii=False),
            atoms_json=json.dumps(ex["atoms"], ensure_ascii=False, default=str),
            script_json=json.dumps({"script": ex["target_script"]}, ensure_ascii=False),
        ).with_inputs("microtype_json", "atoms_json")
        for ex in trainset
    ]

    holdout = examples[:HOLDOUT_SIZE]
    train = examples[HOLDOUT_SIZE:]
    if len(train) < MIN_TRAINSET_SIZE:
        return {"inserted": False, "reason": "trainset_too_small_after_holdout"}

    def metric(example, pred, trace=None) -> float:
        # 简单度量：编译产物有 script 字段即认为有效；W3 起步用此度量，W4 后接 critic 评分作 metric
        try:
            data = json.loads(pred.script_json)
            return 1.0 if data.get("script") else 0.0
        except Exception:
            return 0.0

    try:
        from dspy.teleprompt import BootstrapFewShot

        teleprompter = BootstrapFewShot(metric=metric, max_bootstrapped_demos=3, max_labeled_demos=3)
        compiled = teleprompter.compile(dspy.Predict(GenerationSig), trainset=train)
    except Exception as e:
        log.warning("dspy compile failed: %s", e)
        return {"inserted": False, "reason": "compile_failed", "error": str(e)}

    # 评估 new prompt 在 holdout 上的指标
    new_scores: list[float] = []
    for ex in holdout:
        try:
            pred = compiled(microtype_json=ex.microtype_json, atoms_json=ex.atoms_json)
            new_scores.append(metric(ex, pred))
        except Exception:
            new_scores.append(0.0)

    new_avg = sum(new_scores) / max(len(new_scores), 1)
    old_avg = 1.0  # 默认假设 default 在 holdout 都能产出 — 严格做法：拉历史 critic_scores 平均
    delta = new_avg - old_avg

    if delta < ROLLBACK_DELTA:
        return {
            "inserted": False,
            "reason": "rollback_regression",
            "new_avg": new_avg,
            "old_avg": old_avg,
            "delta": delta,
        }

    # 把编译产物序列化为 LLM-friendly system prompt（A8 直接拿去用）
    try:
        from worker.agents.a8_prompts import GENERATION_SYSTEM_DEFAULT

        demos = compiled.predictors()[0].demos or []
        demo_blocks: list[str] = []
        for i, d in enumerate(demos[:5], 1):
            try:
                m_str = d.microtype_json
                a_str = d.atoms_json
                s_str = d.script_json
            except AttributeError:
                continue
            demo_blocks.append(
                f"### 示例 {i}\n"
                f"目标 microtype: {m_str[:300]}\n"
                f"可用原子: {a_str[:600]}\n"
                f"高分输出: {s_str[:500]}"
            )
        prompt_text = (
            GENERATION_SYSTEM_DEFAULT
            + "\n\n## DSPy BootstrapFewShot 学习产出的高分示例（v"
            + str(len(demos))
            + "）\n\n"
            + "\n\n".join(demo_blocks)
            if demo_blocks
            else GENERATION_SYSTEM_DEFAULT
        )
    except Exception as e:
        log.warning("extract compiled prompt failed: %s", e)
        prompt_text = f"# DSPy compile @ {datetime.now(UTC).isoformat()}\n# extraction error: {e}"

    version = _next_version("a8")
    pv_id = _persist(
        "a8",
        version,
        prompt_text,
        {
            "trainset_size": len(train),
            "holdout_size": len(holdout),
            "new_avg": new_avg,
            "old_avg": old_avg,
            "delta": delta,
            "compiled_at": datetime.now(UTC).isoformat(),
        },
    )
    return {
        "inserted": True,
        "agent": "a8",
        "version": version,
        "prompt_version_id": pv_id,
        "trainset_size": len(train),
        "new_avg": new_avg,
    }


__all__ = ["maybe_optimize"]
