#!/usr/bin/env bash
# 中台数据根目录管理。所有 ecom-* skill 的持久化状态都写在这里。
# 设计原则：一处可见、用户可审计、可跨 skill 共享、可纳入备份。

set -euo pipefail

: "${ZHONGTAI_HOME:=$HOME/.zhongtai}"

zt_init_dirs() {
  mkdir -p "$ZHONGTAI_HOME"/{credentials,data,artifacts,logs,cache,seed}
  mkdir -p "$ZHONGTAI_HOME/data"/{products,competitors,orders,inventory,users,campaigns,regulations}
  mkdir -p "$ZHONGTAI_HOME/artifacts"/{daily,weekly,monthly,ad-hoc}
  mkdir -p "$ZHONGTAI_HOME/logs"/{skill-runs,crawls,compliance-hits}
  mkdir -p "$ZHONGTAI_HOME/credentials/platforms"
  chmod 700 "$ZHONGTAI_HOME/credentials"
}

zt_is_initialized() {
  [ -f "$ZHONGTAI_HOME/.initialized" ]
}

zt_mark_initialized() {
  date -u +%Y-%m-%dT%H:%M:%SZ > "$ZHONGTAI_HOME/.initialized"
}

zt_path() {
  echo "$ZHONGTAI_HOME/$1"
}

zt_cred_file() {
  local platform="$1"
  echo "$ZHONGTAI_HOME/credentials/platforms/${platform}.json"
}

zt_artifact() {
  local category="$1" name="$2"
  local stamp=$(date +%Y%m%d-%H%M%S)
  echo "$ZHONGTAI_HOME/artifacts/${category}/${stamp}-${name}"
}

zt_log() {
  local category="$1" msg="$2"
  local f="$ZHONGTAI_HOME/logs/${category}.log"
  mkdir -p "$(dirname "$f")"
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $msg" >> "$f"
}

zt_config_get() {
  local key="$1" default="${2:-}"
  local f="$ZHONGTAI_HOME/config.json"
  [ -f "$f" ] || { echo "$default"; return; }
  python3 -c "import json,sys
try:
  d=json.load(open('$f'))
  print(d.get('$key','$default'))
except: print('$default')" 2>/dev/null || echo "$default"
}

zt_config_set() {
  local key="$1" value="$2"
  local f="$ZHONGTAI_HOME/config.json"
  [ -f "$f" ] || echo '{}' > "$f"
  python3 -c "import json
d=json.load(open('$f'))
d['$key']='$value'
json.dump(d,open('$f','w'),ensure_ascii=False,indent=2)"
}
