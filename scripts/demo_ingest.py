"""端到端 demo: POST /ingest with manual_payload (媒体管道旁路).

启动 stack 后跑：
    make up
    make migrate
    # 一个终端
    make worker
    # 另一个终端
    make api
    # 第三个终端
    python scripts/demo_ingest.py
"""
import asyncio
import os
import sys

import httpx

API = os.getenv("API_URL", "http://localhost:8000")

# 一个虚构的抖音爆款 — 9 段式 + 多种合规命中（demo 用）
DEMO_PAYLOAD = {
    "url": "https://www.douyin.com/video/demo-7000000000000000000",
    "data_lineage": "manual",
    "platform": "douyin",
    "brand": "DEMO_BRAND",
    "sku": "DEMO_GLUCOSAMINE",
    "category": "氨糖软骨素",
    "manual_payload": {
        "asr_text": (
            "姐妹们我跟你们说，我妈以前每次上下楼膝盖都咔咔响，"
            "三盒下来现在跳广场舞都没问题了，根治了多年的老毛病。"
            "这款氨糖加了硫酸软骨素，专利配方，全国销量第一，"
            "30 天见效不见效全额退款，孕妇糖尿病人也能放心用，"
            "三甲医院推荐，今晚 8 点直播间限时五折，赶紧点小黄车。"
        ),
        "ocr_text": "限时五折 / 销量第一 / 30 天见效",
        "visual_desc": (
            "中年女性出镜，背景为厨房，手持产品包装；"
            "中段切到一位老人下蹲起立的镜头；尾段切到直播间倒计时画面。"
        ),
        "duration_sec": 56.0,
    },
}


async def main() -> int:
    async with httpx.AsyncClient(timeout=30.0) as client:
        # health
        h = await client.get(f"{API}/health")
        print("HEALTH:", h.json())

        # ingest
        r = await client.post(f"{API}/ingest", json=DEMO_PAYLOAD)
        print("INGEST:", r.status_code, r.json())
        if r.status_code != 202:
            return 1

        wf_id = r.json()["workflow_id"]

        # 等待 workflow 完成（简单 polling — 真实场景应该用 Temporal client.get_workflow_handle）
        print(f"Workflow {wf_id} started. 在 Temporal UI (http://localhost:8233) 看进度。")
        print("等 30s 后查 cases 列表 + 详情...")
        await asyncio.sleep(30)

        # 列表
        cases = await client.get(f"{API}/cases?limit=5")
        print("\nLATEST CASES:")
        for c in cases.json():
            print(f"  {c['id']}  lineage={c['data_lineage']}  brand={c.get('brand')}")

        if not cases.json():
            print("⚠️  没有新 case 入库 — 检查 worker 日志")
            return 1

        # 详情
        first_id = cases.json()[0]["id"]
        detail = await client.get(f"{API}/cases/{first_id}")
        d = detail.json()
        print(f"\nCASE {first_id} DETAIL:")
        print(f"  segments: {len(d['segments'])}")
        print(f"  atoms:    {len(d['atoms'])}")
        print("  cross_validations:")
        for cv in d["cross_validations"]:
            print(f"    [{cv['agent']}] verdict={cv['verdict']} confidence={cv['confidence']}")

        # generated scripts (W3)
        scripts = await client.get(f"{API}/scripts?limit=10")
        print(f"\nGENERATED_SCRIPTS: {len(scripts.json())}")
        for sc in scripts.json()[:3]:
            print(
                f"  {sc['id']} prompt={sc['prompt_version']} "
                f"internal_only={sc['for_internal_research_only']}"
            )
            if scripts.json():
                detail = await client.get(f"{API}/scripts/{sc['id']}")
                cs = detail.json()["critic_scores"]
                print(f"    critic_scores ({len(cs)}):")
                for c in cs:
                    print(
                        f"      [{c['evaluator_model']}] "
                        f"avg={_avg_score(c['scores'])} conf={c['confidence']}"
                    )

        # alerts (HITL inbox)
        alerts = await client.get(f"{API}/alerts?status=open&limit=10")
        print(f"\nOPEN ALERTS: {len(alerts.json())}")
        for al in alerts.json()[:5]:
            print(f"  [{al['alert_type']}] {al['created_at']}")

        # prompt versions (DSPy 自优化历史)
        pv = await client.get(f"{API}/prompt-versions?limit=5")
        print(f"\nPROMPT_VERSIONS: {len(pv.json())}")
        for v in pv.json():
            print(f"  agent={v['agent']} version={v['version']} created={v['created_at']}")

        return 0


def _avg_score(scores: dict | None) -> str:
    if not scores or not isinstance(scores, dict):
        return "—"
    vals = [v for v in scores.values() if isinstance(v, int | float)]
    if not vals:
        return "—"
    return f"{sum(vals) / len(vals):.1f}"


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
