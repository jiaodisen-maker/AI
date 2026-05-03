"""
批量导入 Agent 到 Registry

输入：YAML 文件，定义多个 Agent
输出：Registry 中注册的 Agent 数量

用法：
    python scripts/bulk_import_agents.py agents.yaml
    python scripts/bulk_import_agents.py agents.yaml --dry-run

YAML 格式（agents.yaml）见 agents.example.yaml
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

import httpx
import yaml

ROUTER_URL = os.getenv("AGENT_ROUTER_URL", "http://localhost:8000")


REQUIRED_FIELDS = {"name", "display_name", "description", "framework", "endpoint", "skill"}


def validate_agent(idx: int, agent: dict) -> list[str]:
    """返回错误列表，空 = 合法"""
    errors = []
    missing = REQUIRED_FIELDS - set(agent.keys())
    if missing:
        errors.append(f"agent[{idx}] missing fields: {missing}")
    skill = agent.get("skill")
    if isinstance(skill, dict):
        if not skill.get("name"):
            errors.append(f"agent[{idx}].skill.name 缺失")
        if not skill.get("description"):
            errors.append(f"agent[{idx}].skill.description 缺失")
    else:
        errors.append(f"agent[{idx}].skill 必须是 object")
    return errors


async def import_agents(yaml_path: Path, dry_run: bool = False):
    if not yaml_path.exists():
        print(f"❌ File not found: {yaml_path}")
        sys.exit(1)

    with open(yaml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict) or "agents" not in data:
        print("❌ YAML 必须包含顶层 `agents` 列表")
        sys.exit(1)

    agents = data["agents"]
    if not isinstance(agents, list):
        print("❌ `agents` 必须是列表")
        sys.exit(1)

    # 校验所有 agent
    all_errors = []
    for idx, agent in enumerate(agents):
        errors = validate_agent(idx, agent)
        all_errors.extend(errors)

    if all_errors:
        print(f"❌ 发现 {len(all_errors)} 个错误：")
        for e in all_errors:
            print(f"   - {e}")
        sys.exit(1)

    print(f"✓ 校验通过：{len(agents)} 个 Agent")

    if dry_run:
        print("\n[DRY RUN] 将注册以下 Agent：")
        for a in agents:
            print(f"  - {a['name']:30s} [{a['framework']}] [{a.get('owner_team', '?')}]")
        return

    # 实际导入
    success = 0
    failed = []
    async with httpx.AsyncClient(timeout=15) as client:
        for agent in agents:
            try:
                # 先尝试创建
                response = await client.post(f"{ROUTER_URL}/agents", json=agent)
                if response.status_code == 201:
                    print(f"  ✓ Created: {agent['name']}")
                    success += 1
                else:
                    # 已存在 → update
                    response = await client.put(
                        f"{ROUTER_URL}/agents/{agent['name']}", json=agent
                    )
                    if response.status_code == 200:
                        print(f"  ↻ Updated: {agent['name']}")
                        success += 1
                    else:
                        print(f"  ✗ {agent['name']}: HTTP {response.status_code}: {response.text[:100]}")
                        failed.append(agent["name"])
            except Exception as e:
                print(f"  ✗ {agent['name']}: {e}")
                failed.append(agent["name"])

    print(f"\n总计: {success} 成功 / {len(failed)} 失败")
    if failed:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="批量导入 Agent")
    parser.add_argument("yaml_file", help="Agent 定义 YAML 文件路径")
    parser.add_argument("--dry-run", action="store_true", help="只校验不写入")
    args = parser.parse_args()

    asyncio.run(import_agents(Path(args.yaml_file), dry_run=args.dry_run))


if __name__ == "__main__":
    main()
