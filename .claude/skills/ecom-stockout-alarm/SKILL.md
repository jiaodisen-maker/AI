---
name: ecom-stockout-alarm
description: |
  缺货预测预警 (与 09-supply-chain/inv-stockout-alert 联动, 补齐数据视角)。
allowed-tools: [Bash, Read, Write, WebFetch]
triggers: [缺货预测, 库存告警]
ecom: { domain: 06-data-analytics, role: 运营, frequency: hourly }
---

# stockout-alarm



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
Write 到 `~/.zhongtai/artifacts/ecom-stockout-alarm/YYYYMMDD/`

## Step 4: 推送飞书 + 经验沉淀
```bash
feishu_card "stockout-alarm" "$REPORT"
exp_record "ecom-stockout-alarm" '"status":"done"'
```

## 参考规范
/home/user/AI/skills/06-data-analytics/stockout-alarm/SKILL.md (v0 spec, 如有)
