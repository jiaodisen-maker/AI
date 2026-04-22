#!/usr/bin/env bash
# 飞书推送。所有 skill 推送报表/告警都走这里。
# webhook 存在 ~/.zhongtai/config.json 的 feishu_webhook 字段。

set -euo pipefail

SCRIPT_DIR_FS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=dataroot.sh
source "$SCRIPT_DIR_FS/dataroot.sh"

_fs_webhook() {
  zt_config_get feishu_webhook ""
}

_fs_alert_webhook() {
  zt_config_get feishu_alert_webhook "$(_fs_webhook)"
}

# feishu_send_text <channel> <text>
#   channel: default | alert (alert 用独立的告警群)
feishu_send_text() {
  local channel="${1:-default}" text="$2" hook
  case "$channel" in
    alert) hook=$(_fs_alert_webhook) ;;
    *)     hook=$(_fs_webhook) ;;
  esac
  [ -n "$hook" ] || { zt_log crawls "FEISHU_SKIP_NO_WEBHOOK channel=$channel"; return 0; }

  local payload
  payload=$(python3 -c "import json,sys; print(json.dumps({'msg_type':'text','content':{'text':sys.argv[1]}},ensure_ascii=False))" "$text")
  curl -fsS -X POST "$hook" \
    -H 'Content-Type: application/json' \
    -d "$payload" >/dev/null 2>&1 || zt_log crawls "FEISHU_FAIL channel=$channel"
}

# feishu_send_card <channel> <markdown-file>
feishu_send_card() {
  local channel="${1:-default}" md_file="$2" hook
  [ -f "$md_file" ] || { echo "md not found: $md_file" >&2; return 1; }
  case "$channel" in
    alert) hook=$(_fs_alert_webhook) ;;
    *)     hook=$(_fs_webhook) ;;
  esac
  [ -n "$hook" ] || { zt_log crawls "FEISHU_SKIP_NO_WEBHOOK"; return 0; }

  python3 - "$hook" "$md_file" <<'PY' || zt_log crawls "FEISHU_CARD_FAIL"
import sys, json, urllib.request
hook, md_path = sys.argv[1], sys.argv[2]
md = open(md_path, encoding='utf-8').read()
card = {
  "msg_type": "interactive",
  "card": {
    "header": {"title": {"tag": "plain_text", "content": md.split('\n', 1)[0].lstrip('# ').strip() or "中台报告"}},
    "elements": [{"tag": "markdown", "content": md}]
  }
}
req = urllib.request.Request(hook,
    data=json.dumps(card, ensure_ascii=False).encode('utf-8'),
    headers={'Content-Type': 'application/json'})
urllib.request.urlopen(req, timeout=10).read()
PY
}

feishu_alert() {
  local title="$1" body="$2"
  feishu_send_text alert "[告警] ${title}
${body}

来自: $(basename "${PWD}")
时间: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
