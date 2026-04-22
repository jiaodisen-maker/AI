#!/usr/bin/env bash
# 平台常量与通用工具。所有 ecom-* skill 共用。

set -euo pipefail

ZT_PLATFORMS_ALL="tmall jd douyin kuaishou xiaohongshu pdd shipinghao qiwei"

# 日期工具 (默认 T-1)
zt_date_yesterday() { date -u -d 'yesterday' +%Y-%m-%d 2>/dev/null || date -u -v-1d +%Y-%m-%d; }
zt_date_today()     { date -u +%Y-%m-%d; }
zt_date_7d_ago()    { date -u -d '7 days ago' +%Y-%m-%d 2>/dev/null || date -u -v-7d +%Y-%m-%d; }
zt_date_30d_ago()   { date -u -d '30 days ago' +%Y-%m-%d 2>/dev/null || date -u -v-30d +%Y-%m-%d; }

# 金额格式化
zt_fmt_gmv() {
  python3 -c "v=float('${1:-0}')
print(f'{v/1e8:.2f}亿' if v>=1e8 else f'{v/1e4:.1f}万' if v>=1e4 else f'{v:.0f}')"
}

# JSONL 追加 (给 data/ 下的数据集用)
zt_jsonl_append() {
  local file="$1" json_line="$2"
  mkdir -p "$(dirname "$file")"
  echo "$json_line" >> "$file"
}

# 从 JSONL 读最新 N 行
zt_jsonl_tail() {
  local file="$1" n="${2:-10}"
  [ -f "$file" ] || return 0
  tail -n "$n" "$file"
}
