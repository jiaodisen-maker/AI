---
name: ecom-fin-vat-invoice-issue
description: |
  增值税发票开具。按订单号/批量订单开普/专票，保健品商品税收分类
  编码 1030201，推送电子发票到客户邮箱。Use when 开发票 / 开票.
allowed-tools: [Bash, Read, Write, AskUserQuestion]
triggers: [开发票, 开票, 开票系统]
ecom: { domain: 10-finance, role: 财务, frequency: on-demand }
---

# 开票

## Step 1: 拉订单 + 客户税号
若信息不全 AskUserQuestion 补齐。

## Step 2: 开票前校验
- 订单已完成
- 无退款争议
- 税号格式
- 税收分类编码 (保健食品 1030201)

## Step 3: 调开票系统 (金税盘/诺诺/百望)
生成电子发票 PDF。

## Step 4: 推送客户邮箱 + 归档
