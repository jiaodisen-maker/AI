---
name: ecom-cs-recommend-bundle
description: |
  组合套装 / 关联推荐。按客户人群 + 咨询商品 推荐 3 个组合 (如钙片+维D, 护肝+B族)。
  Use when 关联推荐 / 组合推荐 / 搭配买.
allowed-tools: [Bash, Read, Write]
triggers: [关联推荐, 组合推荐, 搭配买]
ecom: { domain: 08-customer-service, role: 客服, frequency: on-demand }
---

# 关联推荐

## Step 1: 读客户画像 + 咨询商品
## Step 2: 从篮分析 basket mining 结果推荐
## Step 3: 合规表述 (不能说"搭配吃更有效治 XX")
## Step 4: 附赠/券促成组合

推荐 3 档：
- 基础 (保健功能互补)
- 进阶 (人群场景匹配)
- 尊享 (礼盒)
