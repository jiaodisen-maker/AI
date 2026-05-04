"""Coze.cn 只读快照：拉 workspaces / bots / workflows / KBs 写成 YAML。

PAT 只从 COZE_PAT 环境变量读。任何文件里都不应出现 token。
"""
from __future__ import annotations

import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import yaml

PAT = os.environ.get("COZE_PAT")
BASE = os.environ.get("COZE_API_BASE", "https://api.coze.cn")
WORKSPACE_FILTER = os.environ.get("COZE_WORKSPACE_ID")  # 可选：只拉某一个

if not PAT:
    print("missing COZE_PAT env var", file=sys.stderr)
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent


def req(path: str, params: dict | None = None, method: str = "GET",
        body: dict | None = None) -> dict:
    url = BASE.rstrip("/") + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body else None
    headers = {
        "Authorization": f"Bearer {PAT}",
        "Content-Type": "application/json",
    }
    r = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        raise RuntimeError(f"HTTP {e.code} {url}\n{body}") from None


def write_yaml(path: pathlib.Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False))


def list_workspaces() -> list[dict]:
    r = req("/v1/workspaces", {"page_num": 1, "page_size": 50})
    if r.get("code", 0) != 0 and "data" not in r:
        raise RuntimeError(f"workspaces failed: {r}")
    return r.get("data", {}).get("workspaces", [])


def list_bots(space_id: str) -> list[dict]:
    out, page = [], 1
    while True:
        r = req("/v1/space/published_bots_list",
                {"space_id": space_id, "page_size": 20, "page_index": page})
        if r.get("code", 0) != 0:
            print(f"  bots api code={r.get('code')} msg={r.get('msg')}",
                  file=sys.stderr)
            break
        d = r.get("data", {})
        items = d.get("space_bots") or d.get("items") or []
        out.extend(items)
        total = d.get("total")
        if not items or (total is not None and len(out) >= total):
            break
        page += 1
        time.sleep(0.1)
    return out


def get_bot_detail(bot_id: str) -> dict | None:
    try:
        r = req("/v1/bot/get_online_info", {"bot_id": bot_id})
        return r.get("data", r)
    except RuntimeError as e:
        print(f"  bot {bot_id} failed: {e}", file=sys.stderr)
        return None


def list_kbs(space_id: str) -> list[dict]:
    try:
        r = req("/open_api/v2/dataset", {"space_id": space_id, "page": 1, "size": 50})
        if r.get("code", 0) == 0:
            return r.get("data", {}).get("dataset_list", []) \
                or r.get("data", {}).get("items", [])
        print(f"  kb api code={r.get('code')} msg={r.get('msg')}", file=sys.stderr)
    except RuntimeError as e:
        print(f"  kb listing failed: {e}", file=sys.stderr)
    return []


def main():
    summary = {"started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "api_base": BASE, "workspaces": []}

    workspaces = list_workspaces()
    if WORKSPACE_FILTER:
        workspaces = [w for w in workspaces if w.get("id") == WORKSPACE_FILTER]
    print(f"workspaces: {len(workspaces)}")
    write_yaml(ROOT / "_workspaces.yaml", {"items": workspaces})

    for sp in workspaces:
        sid = sp.get("id") or sp.get("workspace_id")
        sname = sp.get("name", sid)
        if not sid:
            continue
        bots = list_bots(sid)
        write_yaml(ROOT / "bots" / f"_index_{sid}.yaml",
                   {"workspace": sp, "bots": bots})
        kbs = list_kbs(sid)
        write_yaml(ROOT / "knowledge" / f"_index_{sid}.yaml",
                   {"workspace_id": sid, "datasets": kbs})

        # bot 详情，限速
        details_ok = 0
        for b in bots:
            bid = b.get("bot_id") or b.get("id")
            if not bid:
                continue
            d = get_bot_detail(bid)
            if d is not None:
                write_yaml(ROOT / "bots" / f"{sid}_{bid}.yaml", d)
                details_ok += 1
            time.sleep(0.2)

        summary["workspaces"].append({
            "id": sid, "name": sname,
            "bots": len(bots), "bot_details_ok": details_ok,
            "knowledge_bases": len(kbs),
        })
        print(f"  [{sname}] bots={len(bots)} details_ok={details_ok} kbs={len(kbs)}")

    write_yaml(ROOT / "_pull_summary.yaml", summary)
    print("done. summary written to coze-control/_pull_summary.yaml")


if __name__ == "__main__":
    main()
