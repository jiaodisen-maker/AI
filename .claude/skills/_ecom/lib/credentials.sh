#!/usr/bin/env bash
# _ecom/lib/credentials.sh
# 统一凭证读取与登录检查

CRED_DIR="${ECOM_CRED_DIR:-$HOME/.zhongtai/credentials}"
mkdir -p "$CRED_DIR"

# cred_exists <platform>  → 0 if exists, 1 otherwise
cred_exists() {
  local platform="$1"
  [ -f "$CRED_DIR/${platform}-cookies.json" ] || \
  [ -f "$CRED_DIR/${platform}-token.env" ] || \
  [ -f "$CRED_DIR/${platform}.env" ]
}

# cred_path <platform> [cookies|token|env]  → print path
cred_path() {
  local platform="$1"
  local type="${2:-cookies}"
  echo "$CRED_DIR/${platform}-${type}.json"
}

# ensure_login <platform>  → if no cred, echo NEEDS_LOGIN:<platform>
# Caller (Claude) should AskUserQuestion and then run:
#   $B cookie-import-browser <browser> --domain .<platform>.com
#   cp ~/.gstack/cookies.json "$(cred_path <platform>)"
ensure_login() {
  local platform="$1"
  if cred_exists "$platform"; then
    echo "LOGGED_IN: $platform"
    return 0
  fi
  echo "NEEDS_LOGIN: $platform"
  return 1
}

# verify_login <platform> <verify_url> <selector>  → test via gstack browse
# After login, caller should verify the cred still works.
verify_login() {
  local platform="$1"
  local url="$2"
  local ok_selector="$3"
  local cred="$(cred_path "$platform")"
  [ -f "$cred" ] || return 1
  "$B" cookie-import "$cred" >/dev/null 2>&1
  "$B" goto "$url" >/dev/null 2>&1
  "$B" wait --networkidle >/dev/null 2>&1
  if "$B" is visible "$ok_selector" 2>&1 | grep -q "true"; then
    echo "VERIFIED: $platform"
    return 0
  fi
  echo "STALE: $platform - cred expired, needs re-login"
  return 1
}
