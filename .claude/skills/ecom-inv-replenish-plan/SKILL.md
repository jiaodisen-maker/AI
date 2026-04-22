---
name: ecom-inv-replenish-plan
description: |
  补货计划生成。基于销量预测 + 在途库存 + 安全库存 + 供应商 lead time，
  算各 SKU 应补数量，生成采购单草稿。Use when 算补货 / 补货计划 / 生成采购单.
allowed-tools: [Bash, Read, Write]
triggers: [算补货, 补货计划, 生成采购单]
ecom: { domain: 09-supply-chain, platform: all, role: 采购, frequency: weekly }
---

# 补货计划

## Step 1: 销量预测 (近 30 天 MA / 季节性调整)
```python
import pandas as pd
sales = pd.read_csv("/path/to/sales.csv", parse_dates=["date"])
forecast = sales.groupby("sku")["qty"].rolling(7).mean().iloc[-1]
```

## Step 2: 计算补货量
`补货量 = (日均销量 × (lead_time + 审批周期)) + 安全库存 - 当前可用 - 在途`

## Step 3: 输出采购单
写 CSV 到 `~/.zhongtai/purchase-orders/<YYYYMMDD>.csv`: SKU, 供应商, 数量, 期望到货日, 单价, 总额, 备注 (如"临期清仓期间减半")

## Step 4: 推送飞书让采购主管审批
```bash
feishu_card "补货计划 YYYY-MM-DD" "$SUMMARY (总金额 ¥X, 共 X 个 SKU) 链接: ..."
```
