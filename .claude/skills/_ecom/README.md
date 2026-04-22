# _ecom/ — 保健品 AI 中台电商 skill 共用基础设施

所有 `ecom-*` skill 都会读取本目录的共用资源。

## 目录结构

```
_ecom/
├── README.md
├── lib/
│   ├── browser-setup.sh      # 加载 gstack browse 二进制 $B
│   ├── credentials.sh        # 读取 ~/.zhongtai/credentials/<platform>.json
│   ├── experience.sh         # 追加经验沉淀 JSONL
│   ├── feishu-push.sh        # 飞书机器人推送
│   └── compliance-filter.sh  # 调用违禁词扫描
└── data/
    ├── forbidden-words.json  # 三类违禁词库 (极限/医疗/暗示)
    ├── 27-functions.json     # 蓝帽子 27 项功能
    ├── replacement-dict.json # 合规替代词库
    └── blue-cap-registry.json # 本公司产品备案 (运行时填充)
```

## 共用约定

### 凭证位置
所有平台登录态/token/API key 统一放 `~/.zhongtai/credentials/`：

```
~/.zhongtai/credentials/
├── tmall-cookies.json        # 从浏览器导入 (gstack cookie-import-browser)
├── douyin-cookies.json
├── jd-cookies.json
├── xiaohongshu-cookies.json
├── wechat-work-token.env     # 企微 API token
├── feishu-bot-webhook.env    # 飞书机器人 webhook
├── openai-compatible.env     # LLM API
└── ...
```

首次调用某 skill 发现没凭证时：
1. 用 `AskUserQuestion` 询问是否现在授权
2. 若用户选择，`gstack browse cookie-import-browser <browser>` 拉取登录态
3. 保存到对应 JSON

### 经验沉淀位置
`~/.zhongtai/experience/<skill-name>.jsonl`
每行一条 JSON: `{ts, inputs, ai_output, human_edited_output, diff, user_id}`

### 输出产物位置
`~/.zhongtai/artifacts/<skill-name>/<YYYYMMDD>/<run_id>.{md,json,csv}`

## 使用

每个 skill 的 SKILL.md 会这样引用：

```bash
source "$CLAUDE_SKILL_DIR/../_ecom/lib/browser-setup.sh"    # 加载 $B
source "$CLAUDE_SKILL_DIR/../_ecom/lib/credentials.sh"      # 加载 cred_get()
source "$CLAUDE_SKILL_DIR/../_ecom/lib/compliance-filter.sh" # scan_forbidden()
```

## 中台路由元数据

每个 SKILL.md frontmatter 的 `ecom:` 字段被 AI 中台 runtime 消费：
- `domain` — 12 大领域分类
- `platform` — 适用平台
- `role` — 典型执行岗位
- `frequency` — daily / weekly / on-demand / campaign
- `human_review_required` — 是否需要人工最终审批
- `compliance_filter` — 是否在输出前走违禁词过滤

Claude Code 本身不认识这些字段，会静默忽略 — 不影响 slash command 调用。

中台 Agent SDK 启动时扫全部 `.claude/skills/ecom-*/SKILL.md`，建路由索引。
