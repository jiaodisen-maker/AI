"""遍历 docs/coze-knowledge-base/raw/<site>/ 下所有 .md 文件，
读取每个文件顶部的 frontmatter（source_url / title），
重建 _index.json。

适用场景：脚本运行中途崩溃但 .md 文件已落盘，索引文件丢失。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = (Path(__file__).resolve().parent.parent
        / "docs" / "coze-knowledge-base" / "raw")

FRONTMATTER_RE = re.compile(
    r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
SOURCE_URL_RE = re.compile(r"^source_url:\s*(.+?)\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^title:\s*'(.+?)'\s*$", re.MULTILINE)
SITE_RE = re.compile(r"^site:\s*(.+?)\s*$", re.MULTILINE)


def parse(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")

    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm, body = m.group(1), m.group(2)

    url_m = SOURCE_URL_RE.search(fm)
    title_m = TITLE_RE.search(fm)
    site_m = SITE_RE.search(fm)
    if not url_m:
        return None

    return {
        "url": url_m.group(1).strip(),
        "site": site_m.group(1).strip() if site_m else "unknown",
        "path": str(path.relative_to(ROOT.parent.parent.parent)),
        "title": title_m.group(1).strip() if title_m else "",
        "sha256": hashlib.sha256(body.encode()).hexdigest()[:16],
        "bytes": len(body),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="只打印统计，不写文件")
    args = ap.parse_args()

    if not ROOT.exists():
        print(f"raw 目录不存在: {ROOT}")
        return

    n_total = 0
    n_ok = 0
    n_skip = 0
    index: dict[str, dict] = {}
    by_site: dict[str, int] = {}

    for md in ROOT.rglob("*.md"):
        n_total += 1
        rec = parse(md)
        if rec is None:
            n_skip += 1
            continue
        url = rec.pop("url")
        index[url] = rec
        by_site[rec["site"]] = by_site.get(rec["site"], 0) + 1
        n_ok += 1

    print(f"扫描 {n_total} 个 .md 文件，重建索引: {n_ok} 个，跳过 {n_skip} 个")
    for site, count in sorted(by_site.items()):
        print(f"  [{site}] {count}")

    if args.dry_run:
        print("\n--dry-run，未写入。")
        return

    idx_file = ROOT / "_index.json"
    idx_file.write_text(json.dumps(index, ensure_ascii=False, indent=2),
                        encoding="utf-8")
    print(f"\n写入: {idx_file}")
    print(f"现在可以 git add docs/coze-knowledge-base/raw/ 并提交")


if __name__ == "__main__":
    main()
