---
name: ecom-weekly-report-generate
description: |
  自动生成周报: WoW + 同期去年 + 归因分析 + 下周行动项。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [出周报, 周报, 周度复盘]
ecom: { domain: 06-data-analytics, role: 运营, frequency: weekly }
---

# weekly-report-generate



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
Write 到 `~/.zhongtai/artifacts/ecom-weekly-report-generate/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "weekly-report-generate" "$REPORT"
exp_record "ecom-weekly-report-generate" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/weekly-report-generate/SKILL.md (v0 spec, 如有)
