---
name: ecom-bi-dashboard-build
description: |
  BI 看板搭建 (Tableau / Quick BI / FineBI / Metabase). 根据 ask 自动建看板。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [BI 看板, 数据看板, Tableau]
ecom: { domain: 06-data-analytics, role: 运营, frequency: on-demand }
---

# bi-dashboard-build



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
Write 到 `~/.zhongtai/artifacts/ecom-bi-dashboard-build/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "bi-dashboard-build" "$REPORT"
exp_record "ecom-bi-dashboard-build" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/bi-dashboard-build/SKILL.md (v0 spec, 如有)
