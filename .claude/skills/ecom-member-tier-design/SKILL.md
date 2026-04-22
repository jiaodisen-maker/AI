---
name: ecom-member-tier-design
description: |
  会员等级体系设计。按客单 × 频次 × 贡献度 给出 4-5 级等级 + 升级/保级规则 +
  权益矩阵 + 成本测算。Use when 设计会员体系 / 会员等级 / 积分体系 / 保级规则.
allowed-tools: [Bash, Read, Write]
triggers: [设计会员体系, 会员等级, 积分体系, 保级规则]
ecom: { domain: 07-crm, role: CRM, frequency: on-demand }
---

# 会员等级体系

## Step 1: 拉历史用户数据
从 CDP/CRM 拉近 12 个月的客单 × 频次 × GMV 分布。

## Step 2: 分位数划级
按 70/90/97/99 分位划 普通/银/金/钻/黑 5 级。

## Step 3: 升级保级规则
- 升级: 累计 GMV / 次数 达阈值
- 保级: 年度 GMV 不低于保级线

## Step 4: 权益矩阵 + 成本测算
生日礼 / 专享折扣 / 营养师 1v1 / 免邮 / 换新 / 优先客服。估算年权益总成本 vs 预期留存 GMV 提升。

## Step 5: 输出等级白皮书
