---
name: ecom-shared
description: Shared bash library for all ecom-* skills. Not invoked directly. Provides dataroot management, self-healing credentials, Feishu push, platform constants. 所有 ecom-* skill 共用的 bash 库, 不直接调用。
---

# ecom-shared: 共享库

不是用户调用的 skill，而是所有 `ecom-*` skill 在脚本开头 `source` 的库。

## 用法

每个 ecom-* skill 的 Step 1 都应该加：

```bash
LIB="$HOME/AI/.claude/skills/ecom-shared/lib"
[ -d "$LIB" ] || LIB="$(git rev-parse --show-toplevel)/.claude/skills/ecom-shared/lib"
# shellcheck disable=SC1091
source "$LIB/dataroot.sh"
source "$LIB/credentials.sh"
source "$LIB/feishu.sh"
source "$LIB/platform.sh"
zt_init_dirs

# 冷启动守卫: 未初始化就拒绝运行，让用户先跑 ecom-bootstrap
if ! zt_is_initialized; then
  echo "ZHONGTAI_NOT_INITIALIZED"
  echo "请先跑 /ecom-bootstrap 做冷启动初始化。"
  exit 2
fi
```

## API 速查

### dataroot.sh — 目录管理
- `zt_init_dirs` — 建好 `~/.zhongtai/{credentials,data,artifacts,logs,cache,seed}`
- `zt_is_initialized` / `zt_mark_initialized` — 初始化标记
- `zt_path <rel>` — 绝对路径解析
- `zt_cred_file <platform>` — 返回凭证 JSON 路径
- `zt_artifact <category> <name>` — 返回带时间戳的产物路径
- `zt_log <cat> <msg>` — 写日志
- `zt_config_get <k> [default]` / `zt_config_set <k> <v>` — 读写配置

### credentials.sh — 自愈登录
- `cred_exists <platform>` — 凭证是否存在
- `load_cred <platform>` — 把凭证注入当前 browse 上下文
- `verify_login <platform>` — 访问主页检查登录态
- `login_interactive <platform>` — 真浏览器引导登录 + 导出 cookie
- `ensure_login <platform>` — **核心入口**。保证调用后处于已登录态；失败返回 1
- `with_cred <platform> <cmd> [args...]` — 包装器；自动 ensure_login 再跑 cmd

支持的 platform：`tmall jd douyin kuaishou xiaohongshu pdd shipinghao qiwei`

### feishu.sh — 飞书推送
- `feishu_send_text <channel> <text>` — 纯文本（channel: default / alert）
- `feishu_send_card <channel> <md_file>` — 富文本卡片
- `feishu_alert <title> <body>` — 告警（走 alert channel）

webhook 从 `~/.zhongtai/config.json` 读 `feishu_webhook` / `feishu_alert_webhook`。

### platform.sh — 通用工具
- `ZT_PLATFORMS_ALL` — 全平台列表
- `zt_date_yesterday` / `zt_date_7d_ago` / `zt_date_30d_ago` — 常用日期
- `zt_fmt_gmv <amount>` — GMV 金额中文格式化 (1.2亿 / 35.8万)
- `zt_jsonl_append <file> <line>` / `zt_jsonl_tail <file> [n]` — JSONL 读写

## 设计原则

1. **单一事实来源**：所有持久化状态集中在 `~/.zhongtai/`，用户可审计、可备份、可版本化（.zhongtai 自己可以是个 git repo）
2. **自愈**：登录态失效不报错退出，而是 AskUserQuestion 引导重登 → retry
3. **降级**：3 次重登失败 → 走 `feishu_alert` 告警 + 用缓存数据继续
4. **权限最小**：`~/.zhongtai/credentials/` chmod 700，凭证文件 chmod 600
5. **可移植**：`ZHONGTAI_HOME` 环境变量可覆盖默认路径（给多员工共享数据场景留口子）
