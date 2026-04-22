---
name: ecom-cs-price-negotiate-script
description: |
  议价话术生成。按客单 + 顾客级别 给 3 档议价台阶 + 守价底线 + 换赠品/换券
  替代降价。Use when 议价话术 / 顾客讲价.
allowed-tools: [Read, Write]
triggers: [议价话术, 顾客讲价]
ecom: { domain: 08-customer-service, role: 客服, frequency: on-demand }
---

# 议价话术

## 三档
1. 第一轮: 强调性价比 + 赠品 (不降价)
2. 第二轮: 给小额券 (1-3%)
3. 第三轮: 组合装优惠 (引导大客单)

## 守价底线
单品毛利最低 X%, 低于此 → 拒绝降价 + 推荐低价替代品。

## Step 1: 读顾客级别 (新客/老客/VIP)
## Step 2: 匹配对应话术
## Step 3: 记录议价成功率 (供复盘)
