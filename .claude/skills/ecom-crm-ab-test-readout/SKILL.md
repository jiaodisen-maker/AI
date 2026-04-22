---
name: ecom-crm-ab-test-readout
description: |
  A/B 测试统计显著性复盘。p 值 + 置信区间 + uplift + 推荐是否放量。
  Use when AB 测试复盘 / AB 统计 / 实验显著性.
allowed-tools: [Bash, Read, Write]
triggers: [AB 测试复盘, AB 统计, 实验显著性]
ecom: { domain: 07-crm, role: CRM, frequency: on-demand }
---

# A/B 实验复盘

## Step 1: 输入
控制组 / 实验组 的 曝光 / 转化 / 客单。

## Step 2: 统计检验
```python
from scipy import stats
# 转化率 t 检验 / chi-square
p_value = stats.chi2_contingency([[c_conv, c_nonconv], [t_conv, t_nonconv]])[1]
```

## Step 3: 置信区间 + MDE
报告 uplift + 95% CI。

## Step 4: 建议
- p < 0.05 + uplift > 5%: 放量
- p < 0.05 但 uplift < 2%: 保留研究
- p > 0.05: 回收样本 or 放弃
