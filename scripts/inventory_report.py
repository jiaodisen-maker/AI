"""
Agent 库存报告

输出：
- Agent 总数 / 按框架分布 / 按团队分布 / 按成熟度分布
- 重复能力检测（同 trigger）
- 使用量 Top 10
- 成本 Top 10

用法：
    python scripts/inventory_report.py
    python scripts/inventory_report.py --format markdown > report.md
"""
from __future__ import annotations

import argparse
import asyncio
import os
from collections import Counter, defaultdict

import httpx

ROUTER_URL = os.getenv("AGENT_ROUTER_URL", "http://localhost:8000")


async def fetch_data():
    async with httpx.AsyncClient(timeout=30) as client:
        agents_resp = await client.get(f"{ROUTER_URL}/agents")
        agents_resp.raise_for_status()
        agents = agents_resp.json()["agents"]

        try:
            stats_resp = await client.get(f"{ROUTER_URL}/stats")
            stats = stats_resp.json() if stats_resp.status_code == 200 else {}
        except Exception:
            stats = {}

    return agents, stats


def analyze(agents: list[dict], stats: dict):
    total = len(agents)
    by_framework = Counter(a["framework"] for a in agents)
    by_team = Counter(a.get("owner_team", "unknown") for a in agents)
    by_maturity = Counter(a.get("maturity", "unknown") for a in agents)

    # 重复能力（同 trigger）
    trigger_to_agents = defaultdict(list)
    for a in agents:
        triggers = a.get("skill", {}).get("triggers", []) or []
        for t in triggers:
            trigger_to_agents[t].append(a["name"])
    duplicates = {
        t: names for t, names in trigger_to_agents.items() if len(names) > 1
    }

    # 使用量 / 成本 Top
    usage_list = []
    for name, s in stats.items():
        if isinstance(s, dict):
            usage_list.append((name, s.get("total_calls", 0), s.get("total_cost", 0.0)))
    usage_list.sort(key=lambda x: x[1], reverse=True)
    cost_list = sorted(usage_list, key=lambda x: x[2], reverse=True)

    return {
        "total": total,
        "by_framework": dict(by_framework),
        "by_team": dict(by_team),
        "by_maturity": dict(by_maturity),
        "duplicates": duplicates,
        "top_usage": usage_list[:10],
        "top_cost": cost_list[:10],
    }


def render_text(report: dict) -> str:
    lines = [
        "=" * 60,
        f"Agent 库存报告（共 {report['total']} 个）",
        "=" * 60,
        "",
        "按框架分布：",
    ]
    for fw, n in sorted(report["by_framework"].items(), key=lambda x: -x[1]):
        lines.append(f"  {fw:20s} {n:4d}")
    lines.append("")
    lines.append("按团队分布：")
    for team, n in sorted(report["by_team"].items(), key=lambda x: -x[1]):
        lines.append(f"  {team:20s} {n:4d}")
    lines.append("")
    lines.append("按成熟度分布：")
    for m, n in sorted(report["by_maturity"].items(), key=lambda x: -x[1]):
        lines.append(f"  {m:20s} {n:4d}")
    lines.append("")
    lines.append(f"重复触发词检测（{len(report['duplicates'])} 个重复）：")
    for trigger, names in report["duplicates"].items():
        lines.append(f"  '{trigger}' → {', '.join(names)}")
    lines.append("")
    lines.append("使用量 Top 10：")
    for name, calls, cost in report["top_usage"]:
        lines.append(f"  {name:30s} {calls:6d} 次  ¥{cost:.2f}")
    lines.append("")
    lines.append("成本 Top 10：")
    for name, calls, cost in report["top_cost"]:
        lines.append(f"  {name:30s} ¥{cost:8.2f}  ({calls} 次)")
    return "\n".join(lines)


def render_markdown(report: dict) -> str:
    md = [f"# Agent 库存报告", f"\n**总数：{report['total']}**\n"]

    md.append("## 按框架分布\n")
    md.append("| 框架 | 数量 |")
    md.append("|---|---|")
    for fw, n in sorted(report["by_framework"].items(), key=lambda x: -x[1]):
        md.append(f"| {fw} | {n} |")

    md.append("\n## 按团队分布\n")
    md.append("| 团队 | 数量 |")
    md.append("|---|---|")
    for team, n in sorted(report["by_team"].items(), key=lambda x: -x[1]):
        md.append(f"| {team} | {n} |")

    md.append("\n## 按成熟度分布\n")
    md.append("| 成熟度 | 数量 |")
    md.append("|---|---|")
    for m, n in sorted(report["by_maturity"].items(), key=lambda x: -x[1]):
        md.append(f"| {m} | {n} |")

    if report["duplicates"]:
        md.append(f"\n## ⚠️ 重复触发词（{len(report['duplicates'])} 个）\n")
        md.append("| 触发词 | 涉及 Agent |")
        md.append("|---|---|")
        for trigger, names in report["duplicates"].items():
            md.append(f"| `{trigger}` | {', '.join(names)} |")

    md.append("\n## 使用量 Top 10\n")
    md.append("| Agent | 调用次数 | 总成本 |")
    md.append("|---|---|---|")
    for name, calls, cost in report["top_usage"]:
        md.append(f"| {name} | {calls} | ¥{cost:.2f} |")

    md.append("\n## 成本 Top 10\n")
    md.append("| Agent | 总成本 | 调用次数 |")
    md.append("|---|---|---|")
    for name, calls, cost in report["top_cost"]:
        md.append(f"| {name} | ¥{cost:.2f} | {calls} |")

    return "\n".join(md)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["text", "markdown"], default="text")
    args = parser.parse_args()

    agents, stats = await fetch_data()
    report = analyze(agents, stats)

    if args.format == "markdown":
        print(render_markdown(report))
    else:
        print(render_text(report))


if __name__ == "__main__":
    asyncio.run(main())
