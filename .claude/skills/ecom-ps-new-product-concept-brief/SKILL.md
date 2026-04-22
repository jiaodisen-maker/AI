---
name: ecom-ps-new-product-concept-brief
description: |
  新品概念 brief。整合 市场容量 + 竞品空白 + 人群画像 + 毛利测算 输出
  新品概念单。Use when 新品提案 / 新品概念 / 研发协同.
allowed-tools: [Bash, Read, Write]
triggers: [新品提案, 新品概念, 研发协同]
ecom: { domain: 12-product-selection, role: 选品, frequency: on-demand }
---

# 新品概念 brief

## Step 1: 输入前置 skill 结果
- ecom-ps-category-market-size
- ecom-ps-competition-density
- ecom-ps-target-audience-profile
- ecom-ps-margin-feasibility

## Step 2: 合成概念
- 人群 × 场景 × 痛点 × 功效 × 价格带
- 对应哪个蓝帽子 27 项功能
- 差异化点

## Step 3: 输出 brief
给研发 / 配方 / 包装 / 供应链 四个部门的 brief。

## Step 4: 合规预审
功效声明走 27-function-validator 校验可行性。
