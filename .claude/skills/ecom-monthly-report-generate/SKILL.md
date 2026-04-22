---
name: ecom-monthly-report-generate
description: |
  自动生成月报: 类目结构 + 新品贡献 + 渠道 mix + MoM 环比。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [出月报, 月报, 月度复盘]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# monthly-report-generate



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
Write 到 `~/.zhongtai/artifacts/ecom-monthly-report-generate/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "monthly-report-generate" "$REPORT"
exp_record "ecom-monthly-report-generate" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/monthly-report-generate/SKILL.md (v0 spec, 如有)
