---
name: ecom-inv-multi-warehouse-alloc
description: |
  多仓调拨。按各仓 SKU 库存 + 销量地域分布，算最优调拨方案，生成调拨单。
  Use when 仓间调拨 / 多仓调拨 / 调货.
allowed-tools: [Bash, Read, Write]
triggers: [仓间调拨, 多仓调拨, 调货]
ecom: { domain: 09-supply-chain, platform: all, role: 仓储, frequency: weekly }
---

# 多仓调拨

## Step 1: 拉各仓库存 + 地域订单分布
```bash
# ERP API 拉仓位库存 + 订单收货省份汇总
```

## Step 2: 计算最优调拨
```python
# 简化: 从多库存仓 调 到 少库存仓 (基于就近发货效率)
# 考虑: 调拨运费 vs 发货时效收益
```

## Step 3: 生成调拨单
Write CSV: 来源仓, 目标仓, SKU, 数量, 预计到货。

## Step 4: 触发 WMS 执行
调 WMS API 或导出给仓储主管。
