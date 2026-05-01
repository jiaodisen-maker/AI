"""Integration test：mock LLM clients，跑 A2 → A3 全链，验 DB 写入。

跳过条件：无可用 DATABASE_URL（conftest.py 处理）。

不跑 Temporal — 直接 await activity coroutine（A2/A3 都用了 _safe_workflow_id 兜底）。
"""
import asyncio
import json
from unittest.mock import patch

import pytest
from sqlalchemy import text

from worker.agents import a2_decomposition, a3_compliance
from worker.db import session_scope

_FAKE_DECOMP = {
    "segments": [
        {"segment_type": s, "start_sec": i * 3, "end_sec": (i + 1) * 3, "summary": f"段落 {s}"}
        for i, s in enumerate([
            "hook", "pain", "product_intro", "ingredient_backing",
            "mechanism", "social_proof", "use_scenario", "offer", "cta",
        ])
    ],
    "atoms": [
        {"atom_type": "hook", "content": "数字反差吸引：3 秒抓你眼球", "source_segment_index": 0},
        {"atom_type": "hook", "content": "身份共鸣开场", "source_segment_index": 0},
        {"atom_type": "pain", "content": "凌晨惊醒的焦虑", "source_segment_index": 1},
        {"atom_type": "pain", "content": "下楼膝盖咔咔响的无奈", "source_segment_index": 1},
        {"atom_type": "trust", "content": "成分背书 + 第三方检测", "source_segment_index": 3},
        {"atom_type": "trust", "content": "真实用户使用见证", "source_segment_index": 5},
        {"atom_type": "cta", "content": "限时优惠引导下单", "source_segment_index": 8},
        {"atom_type": "cta", "content": "评论区扣 1 抽奖", "source_segment_index": 8},
        {"atom_type": "hook", "content": "悬念问句开场", "source_segment_index": 0},
        {"atom_type": "trust", "content": "权威机构合作", "source_segment_index": 4},
    ],
}


@pytest.fixture
def fresh_case_input():
    return {
        "url": "https://www.douyin.com/video/test-integration",
        "data_lineage": "manual",
        "platform": "douyin",
        "brand": "TEST_BRAND",
        "sku": "TEST_SKU",
        "category": "氨糖软骨素",
        "manual_payload": {
            "asr_text": "我妈膝盖咔咔响 / 三盒下来跳舞没问题 / 限时五折",
            "ocr_text": "限时五折 / 跳舞无忧",
            "visual_desc": "中年女性手持产品",
            "duration_sec": 60.0,
        },
    }


def test_a2_a3_end_to_end_with_mocked_llm(fresh_case_input):
    """A2 拆解 + A3 合规扫描，全程 mock LLM，验 DB 写入。"""
    with patch("worker.agents.a2_decomposition.call_deepseek") as a2_mock, \
         patch("worker.agents.a3_compliance.call_deepseek") as a3_mock:

        a2_mock.return_value = json.dumps(_FAKE_DECOMP, ensure_ascii=False)
        a3_mock.return_value = json.dumps({"hits": [], "overall": "green"})

        case_id = asyncio.run(a2_decomposition.decompose(fresh_case_input))
        assert case_id

        a3_result = asyncio.run(a3_compliance.scan_compliance(case_id))

    with session_scope() as s:
        case_row = s.execute(
            text("SELECT id, brand, data_lineage FROM cases WHERE id = :id"),
            {"id": case_id},
        ).first()
        assert case_row is not None
        assert case_row.brand == "TEST_BRAND"
        assert case_row.data_lineage == "manual"

        seg_count = s.execute(
            text("SELECT COUNT(*) FROM case_segments WHERE case_id = :id"),
            {"id": case_id},
        ).scalar_one()
        assert seg_count == 9

        atom_count = s.execute(
            text("SELECT COUNT(*) FROM atoms WHERE source_case_id = :id"),
            {"id": case_id},
        ).scalar_one()
        assert atom_count >= 10

        cv = s.execute(
            text("SELECT verdict FROM cross_validations WHERE case_id = :id AND agent = 'a3_compliance'"),
            {"id": case_id},
        ).first()
        assert cv is not None

    assert "verdict" in a3_result


def test_poc_isolation_trigger_blocks_disallowed_insert(fresh_case_input):
    """直接构造 INSERT 触碰 PoC 隔离 trigger，确认 RAISE EXCEPTION。"""
    fresh_case_input["data_lineage"] = "poc_crawled"

    with patch("worker.agents.a2_decomposition.call_deepseek") as a2_mock:
        a2_mock.return_value = json.dumps(_FAKE_DECOMP, ensure_ascii=False)
        case_id = asyncio.run(a2_decomposition.decompose(fresh_case_input))

    # 拿一个 poc_crawled atom
    with session_scope() as s:
        atom_id = s.execute(
            text("SELECT id FROM atoms WHERE source_case_id = :cid LIMIT 1"),
            {"cid": case_id},
        ).scalar_one()

        # 找一个 active microtype（make seed 提供）
        mt_id = s.execute(
            text("SELECT id FROM microtypes WHERE status = 'active' LIMIT 1")
        ).scalar()

        if mt_id is None:
            pytest.skip("no active microtype seeded; run scripts/seed_microtypes.py first")

        # 故意在 for_internal_research_only=false 时插入 — 应被 trigger 阻止
        with pytest.raises(Exception, match="PoC isolation violation"):
            s.execute(
                text(
                    """
                    INSERT INTO generated_scripts (
                        microtype_id, atom_ids, prompt_version, output, llm_model,
                        for_internal_research_only
                    )
                    VALUES (:mt, ARRAY[CAST(:a AS UUID)], 'default', 'test', 'deepseek-chat', false)
                    """
                ),
                {"mt": str(mt_id), "a": str(atom_id)},
            )
