#!/usr/bin/env bash
# _ecom/lib/browser-setup.sh
# 加载 gstack browse 二进制到 $B
# 用法: source 本文件, 之后用 $B <command>

_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
B=""
[ -n "$_ROOT" ] && [ -x "$_ROOT/.claude/skills/gstack/browse/dist/browse" ] \
  && B="$_ROOT/.claude/skills/gstack/browse/dist/browse"
[ -z "$B" ] && [ -x "$HOME/.claude/skills/gstack/browse/dist/browse" ] \
  && B="$HOME/.claude/skills/gstack/browse/dist/browse"

if [ -z "$B" ] || [ ! -x "$B" ]; then
  echo "ERROR: gstack browse not found. Run /home/user/AI/.claude/skills/gstack/setup first."
  return 1 2>/dev/null || exit 1
fi

export B
echo "BROWSE_READY: $B"
