---
name: fin-vat-invoice-issue
domain: 10-finance
platform: all
role: 财务
frequency: on-demand
inputs: [订单号 / 批量订单号, invoice_type, buyer_info]
outputs: [发票号 + 开票记录]
human_review_required: true
data_sources: [订单系统, 开票系统 (金税盘/诺诺/百望)]
allowed-tools: [Bash, Read, Write]
---

# 增值税发票开具 (`fin-vat-invoice-issue`)

## Workflow
1. 订单系统拉订单信息 (金额/商品/客户税号/地址/电话)
2. 开票前校验:
   - 订单已完成 + 无退款争议
   - 客户税号格式正确
   - 商品名称 + 税收分类编码
3. 选发票类型: 普票 (个人) / 专票 (企业, 增值税 6% 或 13%)
4. 金税盘/开票系统开具
5. 电子发票推送客户邮箱
6. 归档到财务系统

## 保健品商品分类编码
- 保健食品: 1030201 (不同省份细目)
- 进口保健品: 1030202
