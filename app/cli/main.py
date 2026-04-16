"""zhongtai CLI — management interface for the AI middleware platform.

Usage:
    zhongtai health          # Health check
    zhongtai skill list      # List all skills
    zhongtai ontology list   # List ontology dimensions
    zhongtai patrol list     # List patrol tasks
"""

from __future__ import annotations

import json
import sys

import httpx

BASE_URL = "http://localhost:8080/api"


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) < 2:
        _print_help()
        return

    command = sys.argv[1]
    subcommand = sys.argv[2] if len(sys.argv) > 2 else ""

    handlers = {
        "health": _health,
        "skill": _skill,
        "ontology": _ontology,
        "patrol": _patrol,
    }

    handler = handlers.get(command)
    if handler:
        handler(subcommand)
    else:
        print(f"Unknown command: {command}")
        _print_help()


def _print_help() -> None:
    print("zhongtai — AI 中台管理工具")
    print()
    print("Commands:")
    print("  health              健康检查")
    print("  skill list          列出所有技能")
    print("  skill exec <id>     执行技能")
    print("  ontology list       列出本体维度")
    print("  ontology validate   验证本体文件")
    print("  patrol list         列出巡逻任务")
    print("  patrol run <id>     手动触发巡逻")


def _health(sub: str) -> None:
    try:
        resp = httpx.get(f"{BASE_URL}/health", timeout=5)
        data = resp.json()
        print(f"Status: {data.get('status', 'unknown')}")
        print(f"Version: {data.get('version', 'unknown')}")
    except httpx.ConnectError:
        print("Error: Cannot connect to AI 中台 server")
        print(f"  Make sure it's running at {BASE_URL}")


def _skill(sub: str) -> None:
    if sub == "list":
        try:
            resp = httpx.get(f"{BASE_URL}/skills", timeout=5)
            data = resp.json()
            print(f"Skills ({data.get('count', 0)}):")
            for s in data.get("skills", []):
                print(f"  {s['id']:20s} {s['name']:15s} {s.get('description', '')[:50]}")
        except httpx.ConnectError:
            print("Error: Cannot connect to server")
    elif sub == "exec" and len(sys.argv) > 3:
        skill_id = sys.argv[3]
        message = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else "测试执行"
        try:
            resp = httpx.post(
                f"{BASE_URL}/skills/{skill_id}/execute",
                json={"message": message},
                timeout=30,
            )
            data = resp.json()
            if data.get("success"):
                print(data.get("content", ""))
            else:
                print(f"Error: {data.get('error', 'unknown')}")
        except httpx.ConnectError:
            print("Error: Cannot connect to server")
    else:
        print("Usage: zhongtai skill [list|exec <id> <message>]")


def _ontology(sub: str) -> None:
    if sub == "list":
        from app.ontology.loader import OntologyLoader
        loader = OntologyLoader()
        loader.load_all()
        print(f"Ontology dimensions ({len(loader.dimensions)}):")
        for dim in loader.dimensions:
            data = loader.get(dim)
            keys = len(data) if isinstance(data, dict) else 0
            print(f"  {dim:30s} ({keys} top-level keys)")
    elif sub == "validate":
        from app.ontology.loader import OntologyLoader
        loader = OntologyLoader()
        data = loader.load_all()
        errors = 0
        for dim in loader.dimensions:
            content = loader.get(dim)
            if not content:
                print(f"  WARNING: {dim} is empty")
                errors += 1
            else:
                print(f"  OK: {dim}")
        if errors:
            print(f"\n{errors} warning(s) found")
        else:
            print("\nAll ontology files valid")
    else:
        print("Usage: zhongtai ontology [list|validate]")


def _patrol(sub: str) -> None:
    if sub == "list":
        try:
            resp = httpx.get(f"{BASE_URL}/patrol/tasks", timeout=5)
            data = resp.json()
            tasks = data.get("tasks", [])
            if not tasks:
                print("No patrol tasks registered")
            for t in tasks:
                status = "enabled" if t.get("enabled") else "disabled"
                print(f"  {t['task_id']:20s} {t['name']:20s} cron={t['cron']} [{status}]")
        except httpx.ConnectError:
            print("Error: Cannot connect to server")
    elif sub == "run" and len(sys.argv) > 3:
        task_id = sys.argv[3]
        try:
            resp = httpx.post(f"{BASE_URL}/patrol/tasks/{task_id}/run", timeout=30)
            print(json.dumps(resp.json(), ensure_ascii=False, indent=2))
        except httpx.ConnectError:
            print("Error: Cannot connect to server")
    else:
        print("Usage: zhongtai patrol [list|run <id>]")


if __name__ == "__main__":
    main()
