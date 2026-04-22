---
name: ecom-channel-attribution-split
description: |
  渠道归因拆分: 自然搜索/付费/内容/达人/私域 的 GMV 贡献 + 互动触达 + 首次归因 + 末次归因。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [渠道归因, 归因, GMV 来源]
ecom: { domain: 06-data-analytics, role: 运营, frequency: weekly }
---

# channel-attribution-split



## Step 1: 加载基础设施
```bash
source /home/user/AI/.claude/skills/_ecom/lib/browser-setup.sh
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
source /home/user/AI/.claude/skills/_ecom/lib/experience.sh
```

## Step 2: 执行核心动作
(见 description, 具体做什么)

## Step 3: 输出
Write 到 `~/.zhongtai/artifacts/ecom-channel-attribution-split/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "channel-attribution-split" "$REPORT"
exp_record "ecom-channel-attribution-split" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/channel-attribution-split/SKILL.md (v0 spec, 如有)
