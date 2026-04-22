---
name: ecom-rfm-segment
description: |
  RFM 8 段分层 (R×F×M 三维). 输出每段人群规模 + 行动建议 (VIP 专员 / 沉睡召回 / 新客激活)。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [RFM 分层, 用户分层, 8 段人群]
ecom: { domain: 06-data-analytics, role: 运营, frequency: monthly }
---

# rfm-segment



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
Write 到 `~/.zhongtai/artifacts/ecom-rfm-segment/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "rfm-segment" "$REPORT"
exp_record "ecom-rfm-segment" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/rfm-segment/SKILL.md (v0 spec, 如有)
