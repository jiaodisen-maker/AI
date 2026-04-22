---
name: ecom-inv-ship-sla-monitor
description: |
  发货时效监控。每小时扫未发货订单，24h/48h 达成率计算，滞留订单按快递公司
  分类告警。Use when 发货监控 / 发货时效 / SLA 监控.
allowed-tools: [Bash, Read, Write]
triggers: [发货监控, 发货时效, SLA 监控]
ecom: { domain: 09-supply-chain, platform: all, role: 仓储, frequency: hourly }
---

# 发货时效监控

## Step 1: 拉未发货订单
```bash
# 各平台订单 API / ERP 待发货
```

## Step 2: 计算滞留时长
每单: `滞留小时 = 当前时间 - 下单时间 (排除夜间)`。
- **> 24 h**: 🟠 警告
- **> 48 h**: 🔴 严重 (平台扣分)

## Step 3: 按快递公司/仓分组告警
```bash
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
feishu_card "发货告警" "超时订单: $COUNT 单; Top 快递: ..."
```

## Step 4: 触发下游
- 自动推送仓储主管
- 严重 > 100 单 → 老板
