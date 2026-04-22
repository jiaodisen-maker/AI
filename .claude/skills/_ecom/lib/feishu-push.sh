#!/usr/bin/env bash
# _ecom/lib/feishu-push.sh
# 飞书机器人推送 (webhook 从 credentials 读)

source "$(dirname "${BASH_SOURCE[0]}")/credentials.sh"

# feishu_text <text>
feishu_text() {
  local text="$1"
  local webhook_file="$CRED_DIR/feishu-bot-webhook.env"
  [ -f "$webhook_file" ] || { echo "SKIP: no feishu webhook configured"; return 0; }
  # shellcheck disable=SC1090
  source "$webhook_file"
  [ -z "$FEISHU_WEBHOOK" ] && { echo "SKIP: FEISHU_WEBHOOK empty"; return 0; }
  curl -s -X POST -H "Content-Type: application/json" \
    -d "{\"msg_type\":\"text\",\"content\":{\"text\":$(printf '%s' "$text" | python3 -c 'import json,sys;print(json.dumps(sys.stdin.read()))')}}" \
    "$FEISHU_WEBHOOK" >/dev/null
  echo "FEISHU_SENT"
}

# feishu_card <title> <markdown_body>
feishu_card() {
  local title="$1"
  local body="$2"
  local webhook_file="$CRED_DIR/feishu-bot-webhook.env"
  [ -f "$webhook_file" ] || { echo "SKIP"; return 0; }
  # shellcheck disable=SC1090
  source "$webhook_file"
  local payload
  payload=$(python3 <<PY
import json,sys
title = """$title"""
body = """$body"""
print(json.dumps({
  "msg_type": "interactive",
  "card": {
    "header": {"title": {"tag": "plain_text", "content": title}},
    "elements": [{"tag": "markdown", "content": body}]
  }
}))
PY
)
  curl -s -X POST -H "Content-Type: application/json" -d "$payload" "$FEISHU_WEBHOOK" >/dev/null
  echo "FEISHU_CARD_SENT"
}
