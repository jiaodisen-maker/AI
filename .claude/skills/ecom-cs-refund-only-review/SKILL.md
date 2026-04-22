---
name: ecom-cs-refund-only-review
description: |
  仅退款审核。识别合理 (收到破损/错发) vs 欺诈 (零元购/羊毛党)。
  对拼多多场景特别注意仅退款率。Use when 仅退款审核 / 仅退款判定.
allowed-tools: [Bash, Read, Write]
triggers: [仅退款审核, 仅退款判定]
ecom: { domain: 08-customer-service, role: 客服, frequency: daily }
---

# 仅退款审核

## 合理情形 → 通过
- 实物破损 (图片)
- 错发 (图片)
- 过敏反应 (医生证明)

## 欺诈情形 → 拒绝 + 平台介入
- 无图无据
- 同 IP 多次仅退款
- 收货人黑名单

## Step 1: 读订单 + 聊天记录 + 举证材料
## Step 2: 规则引擎 + LLM 综合判定
## Step 3: 欺诈客户加黑名单
