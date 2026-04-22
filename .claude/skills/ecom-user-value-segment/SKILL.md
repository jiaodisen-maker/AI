---
name: ecom-user-value-segment
description: |
  用户价值分层。按客单 × 频次 × 毛利贡献做三维分层，输出 8 段人群。
  与 06-data-analytics/rfm-segment 配合使用。Use when 用户分层 / 价值分层.
allowed-tools: [Bash, Read, Write]
triggers: [用户分层, 价值分层, 会员分层]
ecom: { domain: 07-crm, role: CRM, frequency: monthly }
---

# 用户价值分层

## Step 1: 拉近 12 月用户 GMV × 频次 × 毛利
从 CDP + 商品毛利表关联。

## Step 2: 三维分箱
每维度分高/中/低，2×2×2 = 8 段。

## Step 3: 输出分层 + 行动建议
- 高高高: VIP 营养师 1v1
- 高低高: 复购提醒 + 权益升级
- 低高低: 老客薅羊毛策略
...

## Step 4: 写回 CDP 标签 + 同步企微
调 ecom-qiwei-customer-tag 打标签。
