#!/usr/bin/env bash
# _ecom/lib/experience.sh
# 经验沉淀: 每次 skill 执行后把 input/output/human_edit diff 追加到 JSONL

EXP_DIR="${ECOM_EXP_DIR:-$HOME/.zhongtai/experience}"
mkdir -p "$EXP_DIR"

# exp_record <skill_name> <json_payload>
exp_record() {
  local skill="$1"
  local payload="$2"
  local ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  local user_id="${ECOM_USER_ID:-$USER}"
  printf '{"ts":"%s","skill":"%s","user":"%s",%s}\n' \
    "$ts" "$skill" "$user_id" "${payload#\{}" \
    >> "$EXP_DIR/${skill}.jsonl"
}

# exp_inject <skill_name>  → 读取高置信度 pattern 拼成 system prompt fragment
exp_inject() {
  local skill="$1"
  local file="$EXP_DIR/${skill}.jsonl"
  [ -f "$file" ] || return 0
  # 简化版: 最近 30 天 human_edit 不为空的 top 5 pattern
  # 实际需要 Python/Node 脚本做聚类 + 置信度, 这里先占位
  tail -n 100 "$file" | grep -o '"pattern":"[^"]*"' | sort -u | head -5
}
