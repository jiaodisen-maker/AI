"""客服 / 私域日志 → userpain_clusters 灌库 (PIPL §28 合规)。

输入：CSV with column 'text'（每行一条客服对话或评价）
脱敏规则（命中即替换为 token）：
- 手机号 → [PHONE]
- 邮箱 → [EMAIL]
- 身份证号 → [IDCARD]
- 订单号（10+ 位数字串）→ [ORDER_ID]
- 中文姓名（"张三""李小明" 等）→ [NAME]  (启发式，可能漏)
- IP 地址 → [IP]
- 银行卡 → [CARD]

聚类策略（W5 起步用启发式；W6 后接 BERTopic / KMeans on embeddings）：
- 按 source_count 聚合相同前缀子串
- 每 cluster 取 ≤5 条 representative_quotes（脱敏后）
- 嵌入 cluster_label 用 DashScope text-embedding-v3

用法：
    python scripts/import_userpain.py --csv input.csv [--label "睡眠焦虑"]
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from sqlalchemy import text  # noqa: E402

from worker.db import session_scope  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("import_userpain")

# 脱敏规则（PIPL §28 + GBT 35273 个人信息分类）
# 顺序敏感：specific-first（先精确匹配 IDCARD/CARD，再 PHONE，最后 ORDER_ID 兜底）
SCRUB_PATTERNS: list[tuple[re.Pattern, str]] = [
    # IP 优先（含点的特殊形态）
    (re.compile(r"(?<!\d)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?!\d)"), "[IP]"),
    # Email
    (re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"), "[EMAIL]"),
    # 身份证 18 位（最后位可能为 X/x）
    (re.compile(r"(?<!\d)\d{17}[\dXx](?!\w)"), "[IDCARD]"),
    # 银行卡 16-19 位
    (re.compile(r"(?<!\d)\d{16,19}(?!\d)"), "[CARD]"),
    # 手机号 11 位
    (re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"), "[PHONE]"),
    # 订单号兜底 10-15 位
    (re.compile(r"(?<!\d)\d{10,15}(?!\d)"), "[ORDER_ID]"),
    # 中文姓名启发式：常见姓 + 1-2 字
    (
        re.compile(
            r"(?:王|李|张|刘|陈|杨|赵|黄|周|吴|徐|孙|胡|朱|高|林|何|郭|马|罗|梁|宋|郑|谢|韩|唐|冯|于|董|萧|程)"
            r"[一-龥]{1,2}(?=先生|女士|同学|老师|说|表示|反馈)"
        ),
        "[NAME]",
    ),
]


def scrub(text_in: str) -> str:
    out = text_in
    for pat, token in SCRUB_PATTERNS:
        out = pat.sub(token, out)
    return out


def cluster_heuristic(rows: list[str], label: str | None) -> list[dict]:
    """启发式聚类：按文本前 12 字相同前缀分组。

    生产应替换为 BERTopic / KMeans on bge embeddings。
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        key = r.strip()[:12] or "其它"
        groups[key].append(r)

    clusters: list[dict] = []
    for prefix, samples in groups.items():
        cluster_label = label or prefix
        clusters.append(
            {
                "cluster_label": cluster_label,
                "representative_quotes": samples[:5],
                "source_count": len(samples),
            }
        )
    return clusters


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True, help="CSV with 'text' column")
    p.add_argument("--label", default=None, help="Optional cluster label override")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        log.error("CSV not found: %s", csv_path)
        return 1

    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "text" not in (reader.fieldnames or []):
            log.error("CSV must have 'text' column")
            return 1
        raw_rows = [r["text"] for r in reader if r.get("text")]

    log.info("Loaded %d rows", len(raw_rows))
    scrubbed = [scrub(r) for r in raw_rows]
    log.info("Scrubbed PII (PIPL §28)")

    clusters = cluster_heuristic(scrubbed, args.label)
    log.info("Built %d clusters", len(clusters))

    if args.dry_run:
        for c in clusters[:5]:
            sample = c["representative_quotes"][0][:80]
            log.info("  [%s] count=%d sample=%s", c["cluster_label"], c["source_count"], sample)
        return 0

    try:
        from worker.embeddings import embed_text
    except Exception as e:
        log.error("embedding import failed (need QWEN_API_KEY?): %s", e)
        return 2

    inserted = 0
    with session_scope() as s:
        for c in clusters:
            try:
                vec = embed_text(c["cluster_label"])
            except Exception as e:
                log.warning("embed failed for cluster %s: %s", c["cluster_label"], e)
                continue
            s.execute(
                text(
                    """
                    INSERT INTO userpain_clusters (
                        cluster_label, representative_quotes, embedding, source_count
                    )
                    VALUES (:l, :q, CAST(:v AS vector), :n)
                    """
                ),
                {
                    "l": c["cluster_label"],
                    "q": c["representative_quotes"],
                    "v": json.dumps(vec),
                    "n": c["source_count"],
                },
            )
            inserted += 1

    log.info("Inserted %d userpain_clusters", inserted)
    return 0


if __name__ == "__main__":
    sys.exit(main())
