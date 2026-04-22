---
name: ecom-cs-dispute-escalate
description: |
  纠纷升级。收集订单 / 聊天 / 物流 / 质检 证据包，准备平台介入举证。
  Use when 纠纷升级 / 平台介入 / 举证材料.
allowed-tools: [Bash, Read, Write]
triggers: [纠纷升级, 平台介入, 举证材料]
ecom: { domain: 08-customer-service, role: 客服, frequency: on-demand }
---

# 纠纷升级

## Step 1: 自动收集证据包
- 订单截图
- 聊天记录 (千牛/飞鸽/快服务)
- 物流轨迹
- 质检报告 (如有)
- 发货视频 (如有)

## Step 2: 组装 PDF
平台介入常要求 PDF 附件.

## Step 3: 提交平台
各平台介入入口, 按规则上传.

## Step 4: 跟踪结果 + 复盘
