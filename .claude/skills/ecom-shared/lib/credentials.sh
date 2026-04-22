#!/usr/bin/env bash
# 自愈登录库。所有 ecom-* skill 通过 with_cred <platform> <cmd> 来访问平台,
# 本库保证: 未登录→引导登录 / 过期→提示重登 / 都失败→降级并告警。

set -euo pipefail

SCRIPT_DIR_CRED="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=dataroot.sh
source "$SCRIPT_DIR_CRED/dataroot.sh"

# 支持的平台列表。登录 URL / 主页 URL / 登录后验证选择器
zt_platform_config() {
  local platform="$1"
  case "$platform" in
    tmall)
      echo "login_url=https://login.taobao.com/"
      echo "home_url=https://myseller.taobao.com/home.htm"
      echo "verify_selector=.user-name,#J_SiteNavLogin"
      echo "check_url=https://sycm.taobao.com/"
      echo "display_name=天猫/淘宝 (千牛+生意参谋)"
      ;;
    jd)
      echo "login_url=https://passport.jd.com/new/login.aspx"
      echo "home_url=https://shop.jd.com/"
      echo "verify_selector=.user-name,#ttbar-login"
      echo "check_url=https://shop.jd.com/"
      echo "display_name=京东 (京麦+京东商智)"
      ;;
    douyin)
      echo "login_url=https://fxg.jinritemai.com/"
      echo "home_url=https://fxg.jinritemai.com/ffa/mshop/homepage/index"
      echo "verify_selector=.user-info,.shop-name"
      echo "check_url=https://compass.jinritemai.com/"
      echo "display_name=抖店 (抖店+罗盘)"
      ;;
    kuaishou)
      echo "login_url=https://cp.kwaixiaodian.com/"
      echo "home_url=https://cp.kwaixiaodian.com/cp/index"
      echo "verify_selector=.user-area,.shop-name"
      echo "check_url=https://cp.kwaixiaodian.com/"
      echo "display_name=快手小店 (磁力金牛)"
      ;;
    xiaohongshu)
      echo "login_url=https://ark.xiaohongshu.com/login"
      echo "home_url=https://ark.xiaohongshu.com/"
      echo "verify_selector=.user-name,.shop-info"
      echo "check_url=https://ark.xiaohongshu.com/"
      echo "display_name=小红书 (千帆+聚光+蒲公英)"
      ;;
    pdd)
      echo "login_url=https://mms.pinduoduo.com/login"
      echo "home_url=https://mms.pinduoduo.com/home"
      echo "verify_selector=.mall-name,.user-info"
      echo "check_url=https://mms.pinduoduo.com/"
      echo "display_name=拼多多 (多多工作台)"
      ;;
    shipinghao)
      echo "login_url=https://channels.weixin.qq.com/"
      echo "home_url=https://channels.weixin.qq.com/shop/"
      echo "verify_selector=.finder-info,.shop-info"
      echo "check_url=https://channels.weixin.qq.com/shop/"
      echo "display_name=视频号小店"
      ;;
    qiwei)
      echo "login_url=https://work.weixin.qq.com/wework_admin/loginpage_wx"
      echo "home_url=https://work.weixin.qq.com/wework_admin/frame"
      echo "verify_selector=.js_user_name,.ww_userInfo"
      echo "check_url=https://work.weixin.qq.com/"
      echo "display_name=企业微信 (SCRM)"
      ;;
    *)
      echo "# unknown platform: $platform" >&2
      return 1
      ;;
  esac
}

_zt_browse_bin() {
  local root
  root=$(git rev-parse --show-toplevel 2>/dev/null || true)
  if [ -n "$root" ] && [ -x "$root/.claude/skills/gstack/browse/dist/browse" ]; then
    echo "$root/.claude/skills/gstack/browse/dist/browse"
  else
    echo "$HOME/.claude/skills/gstack/browse/dist/browse"
  fi
}

# 检查凭证是否存在
cred_exists() {
  local platform="$1"
  [ -s "$(zt_cred_file "$platform")" ]
}

# 加载凭证到当前浏览器上下文。返回 0 = 加载成功，1 = 凭证不存在/过期
load_cred() {
  local platform="$1"
  local cred_file
  cred_file=$(zt_cred_file "$platform")
  local B
  B=$(_zt_browse_bin)

  [ -s "$cred_file" ] || return 1
  [ -x "$B" ] || { echo "gstack browse 未编译，请先跑 ~/.claude/skills/gstack/setup" >&2; return 2; }

  "$B" cookie-import "$cred_file" >/dev/null 2>&1 || return 1
  return 0
}

# 验证凭证有效性。访问 home_url 检查 verify_selector 是否出现
verify_login() {
  local platform="$1"
  local B cfg home_url selector
  B=$(_zt_browse_bin)
  cfg=$(zt_platform_config "$platform") || return 1
  home_url=$(echo "$cfg" | grep ^home_url= | cut -d= -f2-)
  selector=$(echo "$cfg" | grep ^verify_selector= | cut -d= -f2-)

  load_cred "$platform" || return 1
  "$B" goto "$home_url" >/dev/null 2>&1 || return 1
  sleep 2

  # 任一选择器匹配就算登录
  local IFS=','
  for s in $selector; do
    if "$B" is visible "$s" 2>/dev/null | grep -q true; then
      zt_log crawls "VERIFY_OK $platform"
      return 0
    fi
  done

  zt_log crawls "VERIFY_STALE $platform"
  return 1
}

# 互动式登录（由 skill 发起，在 AskUserQuestion 确认后调用）
# 打开真浏览器让用户扫码/输入密码 → 用户回来按 resume → 从浏览器导出 cookie
login_interactive() {
  local platform="$1"
  local B cfg login_url
  B=$(_zt_browse_bin)
  cfg=$(zt_platform_config "$platform") || return 1
  login_url=$(echo "$cfg" | grep ^login_url= | cut -d= -f2-)

  echo "==> 启动真浏览器，打开 $platform 登录页..."
  "$B" connect >/dev/null 2>&1 || true
  "$B" goto "$login_url"
  "$B" handoff "请在浏览器里完成 $platform 登录（扫码或密码）。完成后回到这里敲 enter。"
  echo "按 enter 继续..."
  # 在脚本里通常是 skill 自己用 AskUserQuestion 卡住，这里留一个 read 兜底
  read -r _ 2>/dev/null || true

  "$B" resume >/dev/null 2>&1 || true
  # 把当前域的 cookie 导出
  local out
  out=$(zt_cred_file "$platform")
  "$B" cookies > "$out.tmp" 2>/dev/null || return 1
  mv "$out.tmp" "$out"
  chmod 600 "$out"
  zt_log crawls "LOGIN_SAVED $platform -> $out"
  echo "==> 凭证已保存: $out"
}

# 核心入口: ensure_login <platform>
# 语义: 保证调用完毕时, 当前 browse 上下文已经带上该平台的有效登录态
# 返回:
#   0  已登录 (可能是冷缓存, 可能是刚刚重登)
#   1  需要人工介入 (调用方必须走 AskUserQuestion → 然后再次 retry)
#   2  无法自愈 (降级处理, 比如跳过本次跑, 发飞书告警)
ensure_login() {
  local platform="$1"
  local max_try="${2:-2}"

  for i in $(seq 1 "$max_try"); do
    if cred_exists "$platform" && verify_login "$platform"; then
      return 0
    fi
    zt_log crawls "ENSURE_LOGIN_MISS $platform attempt=$i"
    [ "$i" -lt "$max_try" ] && sleep 1
  done

  # 到这里说明 cookie 失效或不存在
  echo "NEEDS_LOGIN $platform"
  return 1
}

# 调用方封装: with_cred <platform> <cmd> [args...]
# 自动 ensure_login → 执行命令 → 记录日志
with_cred() {
  local platform="$1"; shift
  ensure_login "$platform" || return $?
  "$@"
}
