"""Playwright 渲染版：抓 SPA 文档站（如 docs.coze.cn）。

跟 scrape-coze-docs.py 同样的输出格式，但用真浏览器渲染。
慢一些（每页 3-5 秒），但能拿到 SPA 的实际内容。

安装一次:
    pip install playwright beautifulsoup4 html2text lxml
    playwright install chromium

用法:
    python tools\\scrape-coze-docs-rendered.py                      # 只爬 SPA 站点（coze_cn）
    python tools\\scrape-coze-docs-rendered.py --site coze_cn       # 显式指定
    python tools\\scrape-coze-docs-rendered.py --resume             # 接着抓
    python tools\\scrape-coze-docs-rendered.py --concurrency 3      # 调高并发
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import sys
import time
from collections import deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse
from xml.etree import ElementTree as ET

import html2text
import httpx
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


SITES = {
    "coze_cn": {
        "seeds": [
            # cozespace（用户给的 9 条 + billing）
            "https://docs.coze.cn/cozespace",
            "https://docs.coze.cn/cozespace/overview",
            "https://docs.coze.cn/cozespace/session",
            "https://docs.coze.cn/cozespace/job",
            "https://docs.coze.cn/cozespace/files",
            "https://docs.coze.cn/cozespace/collaction",
            "https://docs.coze.cn/cozespace/memory",
            "https://docs.coze.cn/cozespace/mail",
            "https://docs.coze.cn/cozespace/device",
            "https://docs.coze.cn/cozespace/coze_billing_overview",
            # developer_guides（截图确认）
            "https://docs.coze.cn/developer_guides/coze_cli",
            "https://docs.coze.cn/developer_guides/coze_cli_quickstart",
            "https://docs.coze.cn/developer_guides/changelog",
            # 兜底入口（让 BFS 从根扩散）
            "https://docs.coze.cn/",
            "https://docs.coze.cn/api",
            "https://docs.coze.cn/customers",
        ],
        "allowed_hosts": ["docs.coze.cn"],
        # 完全放开 path filter——docs.coze.cn 整站都是文档，不挑路径
        "path_prefix_filter": ["/"],
        "wait_selector": "[class*='sidebar'], [class*='nav'], [class*='menu'], "
                          "[class*='catalog'], [class*='toc']",
        "expand_sidebar_js": """
            // 反复点开所有折叠的侧边栏项，直到没有新项出现
            const wait = ms => new Promise(r => setTimeout(r, ms));
            for (let i = 0; i < 8; i++) {
                const before = document.querySelectorAll('a[href]').length;
                document.querySelectorAll(
                    '[class*="arrow"], [class*="caret"], [class*="chevron"], '
                    + '[class*="expand"], [aria-expanded="false"], '
                    + '[class*="catalog"] svg, [class*="sidebar"] svg, '
                    + '[class*="menu"] svg'
                ).forEach(el => { try { el.click(); } catch(e){} });
                await wait(400);
                const after = document.querySelectorAll('a[href]').length;
                if (after === before) break;
            }
            return document.querySelectorAll('a[href]').length;
        """,
        "sitemap_urls": [],   # docs.coze.cn 的 sitemap.xml 是 SPA 假的
    },
    "volcengine_coze": {
        "seeds": [
            "https://www.volcengine.com/docs/84458",
            "https://www.volcengine.com/product/coze-pro",
        ],
        "allowed_hosts": ["www.volcengine.com", "developer.volcengine.com"],
        "path_prefix_filter": ["/docs/84458", "/product/coze", "/articles"],
        "wait_selector": "main, article, .markdown-body, .doc-content, "
                          ".content, [class*='content']",
        "expand_sidebar_js": "",
        "sitemap_urls": [],
    },
}

OUTPUT_ROOT = (Path(__file__).resolve().parent.parent
               / "docs" / "coze-knowledge-base" / "raw")

PAGE_TIMEOUT_MS = 25000
WAIT_AFTER_LOAD_MS = 800
DELAY_BETWEEN_S = 0.4
MAX_PAGES_PER_SITE = 1500
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/126.0.0.0 Safari/537.36")


# ---- 辅助 -----------------------------------------------------------

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

    for sel in ["nav", "header", "footer", "script", "style", "aside",
                "[role=navigation]", ".sidebar", ".toc", ".header", ".footer",
                ".doc-header", ".doc-sidebar", ".doc-toc"]:
        for el in soup.select(sel):
            el.decompose()

    main = (soup.find("main") or soup.find("article")
            or soup.select_one(".doc-content")
            or soup.select_one(".markdown-body")
            or soup.select_one("#content")
            or soup.select_one("[class*='content']")
            or soup.body)
    if main is None:
        return title, ""

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
        if any(p.path.lower().endswith(ext) for ext in
               (".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf",
                ".zip", ".tar", ".gz", ".mp4", ".mp3", ".js", ".css")):
            continue
        out.append(u)
    return out


async def try_sitemap(urls: list[str]) -> list[str]:
    """如果有 sitemap.xml，返回里头所有 <loc>。"""
    out = []
    async with httpx.AsyncClient(timeout=10,
                                 headers={"User-Agent": USER_AGENT}) as cli:
        for u in urls:
            try:
                r = await cli.get(u)
                if r.status_code != 200:
                    continue
                root = ET.fromstring(r.text)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                for loc in root.findall(".//sm:loc", ns):
                    if loc.text:
                        out.append(loc.text.strip())
                if out:
                    print(f"  sitemap {u} → {len(out)} URLs", flush=True)
                    return out
            except Exception as e:
                print(f"  sitemap {u} skipped: {e}", flush=True)
    return out


# ---- Playwright 渲染抓取 -----------------------------------------

async def render_one(page, url: str, wait_selector: str | None,
                     expand_js: str | None) -> str | None:
    try:
        await page.goto(url, wait_until="networkidle",
                        timeout=PAGE_TIMEOUT_MS)
        if wait_selector:
            try:
                await page.wait_for_selector(wait_selector,
                                             timeout=PAGE_TIMEOUT_MS // 3)
            except Exception:
                pass
        # React 多一点时间渲染
        await page.wait_for_timeout(WAIT_AFTER_LOAD_MS)
        # 展开侧边栏，让所有 <a href> 都出现
        if expand_js:
            try:
                count = await page.evaluate(f"async () => {{ {expand_js} }}")
                # 静默 — 不打印，避免日志噪音
            except Exception:
                pass
            await page.wait_for_timeout(500)
        return await page.content()
    except Exception as e:
        print(f"    render fail {url}: {e}", flush=True)
        return None


async def worker(name: str, queue: asyncio.Queue, browser, cfg: dict,
                 site: str, index: dict, failures: dict, seen: set,
                 stats: dict):
    ctx = await browser.new_context(user_agent=USER_AGENT,
                                    viewport={"width": 1280, "height": 900})
    page = await ctx.new_page()

    while True:
        try:
            url = await asyncio.wait_for(queue.get(), timeout=5)
        except asyncio.TimeoutError:
            break

        if url in seen:
            queue.task_done()
            continue
        seen.add(url)

        if stats["done"] >= MAX_PAGES_PER_SITE:
            queue.task_done()
            continue

        html = await render_one(page, url, cfg.get("wait_selector"),
                                cfg.get("expand_sidebar_js"))
        if html is None:
            failures[url] = "render timeout / network"
            queue.task_done()
            await asyncio.sleep(DELAY_BETWEEN_S)
            continue

        title, md = html_to_md(html, url)
        if not md or len(md) < 80:
            failures[url] = f"empty after render ({len(md)} chars)"
            queue.task_done()
            await asyncio.sleep(DELAY_BETWEEN_S)
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

        for nu in extract_links(html, url, cfg["allowed_hosts"],
                                cfg["path_prefix_filter"]):
            if nu not in seen:
                await queue.put(nu)

        stats["done"] += 1
        if stats["done"] % 5 == 0:
            print(f"  [{name}] {stats['done']} pages, "
                  f"queue≈{queue.qsize()}, "
                  f"failures={len(failures)}",
                  flush=True)

        queue.task_done()
        await asyncio.sleep(DELAY_BETWEEN_S)

    await ctx.close()


async def crawl_site(site: str, cfg: dict, index: dict, failures: dict,
                     seen_init: set, concurrency: int):
    seen = set(seen_init)
    queue: asyncio.Queue = asyncio.Queue()

    # 1) 试 sitemap
    sm_urls = await try_sitemap(cfg.get("sitemap_urls", []))
    if sm_urls:
        for u in sm_urls:
            p = urlparse(u)
            if p.netloc not in cfg["allowed_hosts"]:
                continue
            if cfg["path_prefix_filter"] and not any(
                p.path.startswith(pf) for pf in cfg["path_prefix_filter"]
            ):
                continue
            if u not in seen:
                await queue.put(u)
        print(f"  [{site}] sitemap 提供 {queue.qsize()} 个 URL")

    # 2) seed 兜底
    for s in cfg["seeds"]:
        if s not in seen:
            await queue.put(s)

    print(f"  [{site}] 初始队列: {queue.qsize()}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        stats = {"done": 0}
        workers = [
            asyncio.create_task(
                worker(f"{site}#{i}", queue, browser, cfg, site,
                       index, failures, seen, stats))
            for i in range(concurrency)
        ]
        await asyncio.gather(*workers, return_exceptions=True)
        await browser.close()

    print(f"[{site}] 完成: {stats['done']} 页成功, "
          f"{len(failures)} 累计失败", flush=True)


# ---- main ---------------------------------------------------------

async def main_async():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", action="append",
                    choices=list(SITES.keys()) + ["all"],
                    help="只爬某个站点；可重复")
    ap.add_argument("--resume", action="store_true",
                    help="把已有 _index.json 中的 URL 加入 seen，避免重抓")
    ap.add_argument("--concurrency", type=int, default=2,
                    help="并发浏览器页数（建议 2-3）")
    args = ap.parse_args()

    targets = (list(SITES.keys()) if (not args.site or "all" in args.site)
               else args.site)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    idx_file = OUTPUT_ROOT / "_index.json"
    fail_file = OUTPUT_ROOT / "_failures.json"

    existing_idx = json.loads(idx_file.read_text()) if idx_file.exists() else {}
    existing_fail = json.loads(fail_file.read_text()) if fail_file.exists() else {}
    index = dict(existing_idx)
    failures = dict(existing_fail)
    seen_init = set(existing_idx.keys()) if args.resume else set()

    print(f"将爬取站点: {targets}")
    print(f"输出目录: {OUTPUT_ROOT}")
    print(f"并发: {args.concurrency}")
    print(f"已抓页数 (resume): {len(existing_idx)}\n")

    for site in targets:
        try:
            await crawl_site(site, SITES[site], index, failures,
                             seen_init, args.concurrency)
        except KeyboardInterrupt:
            print("\n中断，存当前状态")
            break

        idx_file.write_text(json.dumps(index, ensure_ascii=False, indent=2))
        fail_file.write_text(json.dumps(failures, ensure_ascii=False, indent=2))

    print(f"\n全部完成。共 {len(index)} 页成功，{len(failures)} 页失败。")
    print(f"  index:    {idx_file}")
    print(f"  failures: {fail_file}")


def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
