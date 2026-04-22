---
name: ecom-ps-seasonality-curve
description: |
  保健品季节性曲线。蛋白粉春节/健身季、护肝中秋国庆、维生素换季，
  出类目 × 月份的热度图。Use when 季节性 / 旺季淡季 / 节日趋势.
allowed-tools: [Bash, Read, Write]
triggers: [季节性, 旺季淡季, 节日趋势]
ecom: { domain: 12-product-selection, role: 选品, frequency: quarterly }
---

# 季节性曲线

## Step 1: 拉类目近 3 年逐月 GMV
从生意参谋市场大盘 / 巨量算数。

## Step 2: 归一化 + 画热度图
```python
import seaborn as sns
# 12 个月 × 3 年 heatmap
```

## Step 3: 识别爆发期 + 低谷期
## Step 4: 备货 / 活动 / 投放建议
节前 2 月开始备货 + 1 月开始预热。
