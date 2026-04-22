---
name: ecom-fin-vat-invoice-collect
description: |
  进项发票月度收集归档。清点供应商/平台/达人/物流/广告/办公 6 类支出，
  催票，录入财务系统，认证抵扣，月末出缺票清单影响利润表。
  Use when 催票 / 收进项 / 进项发票归档.
allowed-tools: [Bash, Read, Write]
triggers: [催票, 收进项, 进项发票归档]
ecom: { domain: 10-finance, role: 财务, frequency: monthly }
---

# 进项发票收集

## Step 1: 清点本月支出 6 类
供应商/平台服务费/达人佣金/物流/广告消耗/办公差旅。

## Step 2: 催票 (企微/邮件)
对未到的，每 3 天自动催。

## Step 3: 录入 + 认证抵扣
导入财务系统。

## Step 4: 月末缺票清单
影响利润表的缺票条目，推送 CFO。
