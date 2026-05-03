"""
启动脚本：注册示例 Agent 到 Registry

跑法:
    python scripts/seed_agents.py

或者通过 Docker:
    docker compose exec agent-router python -m scripts.seed_agents
"""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

# 让脚本可以从项目根目录跑
sys.path.insert(0, str(Path(__file__).parent.parent / "services" / "agent-router"))

import httpx

ROUTER_URL = os.getenv("AGENT_ROUTER_URL", "http://localhost:8000")


SAMPLE_AGENTS = [
    {
        "name": "compliant-copywriter",
        "display_name": "合规文案助手",
        "description": "为保健品生成符合中国法规和平台规则的营销文案",
        "framework": "mock",  # 先用 mock 验证流程
        "endpoint": "http://mock-not-used",
        "skill": {
            "name": "compliant-copy",
            "description": "为保健品生成符合中国法规和平台规则的营销文案",
            "instructions": "## 禁词清单\n- 治疗、治愈、根治\n- 100% 有效、立竿见影\n",
            "triggers": ["写文案", "合规文案", "营销文案", "小红书", "抖音"],
        },
        "owner_team": "marketing",
        "maturity": "production",
        "cost_per_call": 0.05,
    },
    {
        "name": "data-analyst",
        "display_name": "数据查询助手",
        "description": "通过自然语言查询销售/库存/会员数据",
        "framework": "mock",
        "endpoint": "http://mock-not-used",
        "skill": {
            "name": "data-query",
            "description": "通过自然语言查询销售/库存/会员数据",
            "triggers": ["查数据", "销售", "库存", "会员", "报表"],
        },
        "owner_team": "operation",
        "maturity": "production",
        "cost_per_call": 0.02,
    },
    {
        "name": "compliance-reviewer",
        "display_name": "合规审查助手",
        "description": "对已有文案进行合规审查，检查禁词、平台规则、行业法规",
        "framework": "mock",
        "endpoint": "http://mock-not-used",
        "skill": {
            "name": "compliance-review",
            "description": "对已有文案进行合规审查",
            "triggers": ["合规审查", "审核文案", "检查文案", "禁词"],
        },
        "owner_team": "legal",
        "maturity": "beta",
        "cost_per_call": 0.03,
    },
]


async def seed():
    async with httpx.AsyncClient(timeout=10) as client:
        for agent in SAMPLE_AGENTS:
            try:
                response = await client.post(f"{ROUTER_URL}/agents", json=agent)
                if response.status_code == 201:
                    print(f"✓ Registered: {agent['name']}")
                else:
                    # 已存在 → update
                    response = await client.put(
                        f"{ROUTER_URL}/agents/{agent['name']}", json=agent
                    )
                    print(f"↻ Updated: {agent['name']}")
            except Exception as e:
                print(f"✗ Failed: {agent['name']}: {e}")

        # 列出所有
        response = await client.get(f"{ROUTER_URL}/agents")
        data = response.json()
        print(f"\n总计 {data['count']} 个 Agent 已注册：")
        for a in data["agents"]:
            print(f"  - {a['name']:30s} [{a['framework']}] [{a['maturity']}]")


if __name__ == "__main__":
    asyncio.run(seed())
