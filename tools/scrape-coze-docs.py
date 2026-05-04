"""把 Coze / Volcengine / CloudWeGo 上跟 Coze 相关的整站文档爬下来转成 markdown。

在 *你自己的电脑* 上跑（不是沙箱）——沙箱被防火墙挡了。
不需要任何 token，所有目标都是公开文档。

用法:
    pip install httpx beautifulsoup4 html2text lxml
    python tools/scrape-coze-docs.py                  # 全部站点
    python tools/scrape-coze-docs.py --site coze_cn   # 只爬 docs.coze.cn
    python tools/scrape-coze-docs.py --resume         # 断点续爬

输出:
    docs/coze-knowledge-base/raw/<site>/<path>.md
    docs/coze-knowledge-base/raw/_index.json          url → 文件 + 哈希
    docs/coze-knowledge-base/raw/_failures.json       抓失败的清单
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import html2text
import httpx
from bs4 import BeautifulSoup

# ---- 配置 ---------------------------------------------------------

SITES = {
    "coze_cn": {
        "seeds": [
            "https://docs.coze.cn/",
            "https://docs.coze.cn/cozespace/coze_billing_overview",
            "https://www.coze.cn/open/docs/guides",
            "https://www.coze.cn/open/docs/coze_pro",
        ],
        "allowed_hosts": ["docs.coze.cn", "www.coze.cn", "coze.cn"],
        "path_prefix_filter": ["/docs", "/open/docs", "/cozespace"],
    },
    "volcengine_coze": {
        "seeds": [
            "https://www.volcengine.com/docs/84458",
            "https://www.volcengine.com/product/coze-pro",
        ],
        "allowed_hosts": ["www.volcengine.com", "developer.volcengine.com"],
        "path_prefix_filter": ["/docs/84458", "/product/coze", "/articles"],
    },
    "cloudwego_eino": {
        "seeds": [
            "https://www.cloudwego.io/docs/eino/",
            "https://www.cloudwego.cn/docs/eino/",
        ],
        "allowed_hosts": ["www.cloudwego.io", "www.cloudwego.cn"],
        "path_prefix_filter": ["/docs/eino"],
    },
    "github_coze": {
        # 这俩 repo 的 wiki。只留 /wiki 路径避免抓 issues / PRs / 源码 viewer。
        "seeds": [
            "https://github.com/coze-dev/coze-studio/wiki",
            "https://github.com/coze-dev/coze-loop/wiki",
        ],
        "allowed_hosts": ["github.com", "raw.githubusercontent.com"],
        "path_prefix_filter": [
            "/coze-dev/coze-studio/wiki",
            "/coze-dev/coze-loop/wiki",
        ],
    },
}

OUTPUT_ROOT = Path(__file__).resolve().parent.parent / "docs" / "coze-knowledge-base" / "raw"

# 抓取参数
TIMEOUT = 15
DELAY = 0.3                  # 礼貌间隔，每页 300ms
MAX_PAGES_PER_SITE = 800     # 单站点上限，防失控
USER_AGENT = "coze-docs-scraper/1.0 (+local research; respects robots.txt)"

# ---- 工具函数 -----------------------------------------------------

def url_to_path(url: str, site: str) -> Path:
    p = urlparse(url)
    raw = p.path or "/"
    if raw.endswith("/"):
        raw += "index"
    raw = raw.lstrip("/")
    safe = re.sub(r"[^\w\-./]+", "_", raw)
    return OUTPUT_ROOT / site / (safe + ".md")


def html_to_md(html: str, base_url: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")

    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    elif soup.h1:
        title = soup.h1.get_text(strip=True)

    # 去除导航 / 页脚 / 脚本 / 样式 / 隐藏块
    for sel in ["nav", "header", "footer", "script", "style", "aside",
                "[role=navigation]", ".sidebar", ".toc", ".header", ".footer"]:
        for el in soup.select(sel):
            el.decompose()

    # 优先取 main / article 主体
    main = (soup.find("main") or soup.find("article")
            or soup.find("div", id="content") or soup.body)
    if main is None:
        return title, ""

    # 处理相对链接
    for a in main.find_all("a", href=True):
        a["href"] = urljoin(base_url, a["href"])
    for img in main.find_all("img", src=True):
        img["src"] = urljoin(base_url, img["src"])

    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False
    h.protect_links = True
    h.unicode_snob = True
    md = h.handle(str(main))
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return title, md


def extract_links(html: str, base_url: str, allowed_hosts: list[str],
                  path_filters: list[str]) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    out = []
    for a in soup.find_all("a", href=True):
        u = urljoin(base_url, a["href"])
        u, _ = urldefrag(u)
        p = urlparse(u)
        if p.scheme not in ("http", "https"):
            continue
        if p.netloc not in allowed_hosts:
            continue
        if path_filters and not any(p.path.startswith(pf) for pf in path_filters):
            continue
        # 过滤明显的非文档资源
        if any(p.path.lower().endswith(ext) for ext in
               (".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf",
                ".zip", ".tar", ".gz", ".mp4", ".mp3")):
            continue
        out.append(u)
    return out


# ---- 主爬虫逻辑 ---------------------------------------------------

def crawl_site(site: str, cfg: dict, index: dict, failures: dict,
               resume: bool, seen_init: set | None = None) -> None:
    seen: set[str] = set(seen_init or [])
    queue: deque[str] = deque()

    for s in cfg["seeds"]:
        if s not in seen:
            queue.append(s)

    cli = httpx.Client(timeout=TIMEOUT, follow_redirects=True,
                       headers={"User-Agent": USER_AGENT})
    n_done = 0

    while queue and n_done < MAX_PAGES_PER_SITE:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        try:
            r = cli.get(url)
            ct = r.headers.get("content-type", "")
            if r.status_code != 200 or "html" not in ct:
                failures[url] = f"{r.status_code} {ct}"
                continue
        except Exception as e:
            failures[url] = f"network: {e!r}"
            continue

        title, md = html_to_md(r.text, url)
        if not md or len(md) < 50:
            failures[url] = f"empty/short body ({len(md)} chars)"
            continue

        path = url_to_path(url, site)
        path.parent.mkdir(parents=True, exist_ok=True)

        header = (
            f"---\n"
            f"source_url: {url}\n"
            f"title: {title!r}\n"
            f"site: {site}\n"
            f"scraped_at: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n"
            f"---\n\n# {title}\n\n"
        )
        path.write_text(header + md, encoding="utf-8")

        index[url] = {
            "site": site,
            "path": str(path.relative_to(OUTPUT_ROOT.parent.parent.parent)),
            "title": title,
            "sha256": hashlib.sha256(md.encode()).hexdigest()[:16],
            "bytes": len(md),
        }

        # 提取站内链接继续爬
        for nu in extract_links(r.text, url, cfg["allowed_hosts"],
                                cfg["path_prefix_filter"]):
            if nu not in seen:
                queue.append(nu)

        n_done += 1
        if n_done % 10 == 0:
            print(f"  [{site}] {n_done} pages, queue={len(queue)}", flush=True)
        time.sleep(DELAY)

    cli.close()
    print(f"[{site}] done: {n_done} pages, {len(failures)} failures so far",
          flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", action="append",
                    choices=list(SITES.keys()) + ["all"],
                    help="只爬某个站点；可重复；默认全部")
    ap.add_argument("--resume", action="store_true",
                    help="继续上次中断的（按 _index.json 跳过已抓的）")
    args = ap.parse_args()

    targets = (list(SITES.keys()) if (not args.site or "all" in args.site)
               else args.site)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    idx_file = OUTPUT_ROOT / "_index.json"
    fail_file = OUTPUT_ROOT / "_failures.json"

    # 总是合并已有 index/failures，避免不同站点之间的运行互相覆盖。
    # --resume 只决定"是否把已抓的 URL 加入 seen 集合（跳过重抓）"。
    existing_idx = json.loads(idx_file.read_text()) if idx_file.exists() else {}
    existing_fail = json.loads(fail_file.read_text()) if fail_file.exists() else {}
    index = dict(existing_idx)
    failures = dict(existing_fail)
    if args.resume:
        seen_seed = set(existing_idx.keys())
    else:
        seen_seed = set()

    print(f"将爬取站点: {targets}")
    print(f"输出目录: {OUTPUT_ROOT}")
    print(f"已有页数 (resume): {len(index)}\n")

    for site in targets:
        try:
            crawl_site(site, SITES[site], index, failures, args.resume,
                       seen_init=seen_seed)
        except KeyboardInterrupt:
            print("\n中断，已存当前状态")
            break

        idx_file.write_text(json.dumps(index, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        fail_file.write_text(json.dumps(failures, ensure_ascii=False, indent=2),
                             encoding="utf-8")

    print(f"\n完成。共 {len(index)} 页成功，{len(failures)} 页失败。")
    print(f"  index:    {idx_file}")
    print(f"  failures: {fail_file}")
    print(f"\n下一步:")
    print(f"  git add docs/coze-knowledge-base/raw/")
    print(f"  git commit -m 'scrape: coze docs sites'")
    print(f"  git push")


if __name__ == "__main__":
    sys.exit(main())
