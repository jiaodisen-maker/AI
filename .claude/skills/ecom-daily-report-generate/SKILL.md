---
name: ecom-daily-report-generate
description: |
  自动生成日报: 昨日 GMV/UV/CVR/订单/Top SKU/异常 + 环比同比 + 行动建议, 早上 8:30 推飞书。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [出日报, 日报, 昨天咋样]
ecom: { domain: 06-data-analytics, role: 运营, frequency: daily }
---

# daily-report-generate



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
Write 到 `~/.zhongtai/artifacts/ecom-daily-report-generate/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "daily-report-generate" "$REPORT"
exp_record "ecom-daily-report-generate" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/daily-report-generate/SKILL.md (v0 spec, 如有)
