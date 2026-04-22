---
name: ecom-aarrr-funnel
description: |
  AARRR 漏斗: 拉新/激活/留存/变现/自传播 逐层转化率 + 流失诊断 + 改进假设。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [AARRR, 增长漏斗, 海盗模型]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# aarrr-funnel



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
Write 到 `~/.zhongtai/artifacts/ecom-aarrr-funnel/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "aarrr-funnel" "$REPORT"
exp_record "ecom-aarrr-funnel" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/aarrr-funnel/SKILL.md (v0 spec, 如有)
