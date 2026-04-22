---
name: ecom-feishu-multidim-sync
description: |
  飞书多维表格数据同步。各数据源 → 飞书多维表格, 供老板看, 支持多视图。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [飞书多维表, 同步飞书]
ecom: { domain: 06-data-analytics, role: 运营, frequency: daily }
---

# feishu-multidim-sync



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
Write 到 `~/.zhongtai/artifacts/ecom-feishu-multidim-sync/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "feishu-multidim-sync" "$REPORT"
exp_record "ecom-feishu-multidim-sync" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/feishu-multidim-sync/SKILL.md (v0 spec, 如有)
