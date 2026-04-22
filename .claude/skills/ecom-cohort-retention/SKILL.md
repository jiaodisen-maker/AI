---
name: ecom-cohort-retention
description: |
  按获客渠道/月份拆的留存曲线, 新老客留存差异, 异常低点根因。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [留存曲线, cohort 留存, 留存分析]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# cohort-retention



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
Write 到 `~/.zhongtai/artifacts/ecom-cohort-retention/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "cohort-retention" "$REPORT"
exp_record "ecom-cohort-retention" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/cohort-retention/SKILL.md (v0 spec, 如有)
