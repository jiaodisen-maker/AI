---
name: ecom-inv-safety-stock-calc
description: |
  安全库存计算。按公式: 安全库存 = 日均销量 × 补货周期 + 安全系数 × 标准差。
  每 SKU 各平台分仓算。Use when 算安全库存 / 补货周期 / 安全系数.
allowed-tools: [Bash, Read, Write]
triggers: [算安全库存, 安全库存]
ecom: { domain: 09-supply-chain, platform: all, role: 库存, frequency: weekly }
---

# 安全库存计算

## Step 1: 拉近 30 天销售 + 补货周期
```bash
# ERP 销售数据 + 供应商 lead time
```

## Step 2: Python 计算
```python
import statistics, math
daily_sales = [...]  # 每日销量列表
avg = statistics.mean(daily_sales)
std = statistics.stdev(daily_sales)
z = 1.65  # 95% 服务水平
lead_time = 7  # 天
safety_stock = round(avg * lead_time + z * std * math.sqrt(lead_time))
```

## Step 3: 写回 ERP + 告警当前低于安全线的 SKU
```bash
source /home/user/AI/.claude/skills/_ecom/lib/feishu-push.sh
feishu_text "⚠️ 低于安全库存的 SKU: ..."
```
