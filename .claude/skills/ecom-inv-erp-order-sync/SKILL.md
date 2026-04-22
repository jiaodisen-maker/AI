---
name: ecom-inv-erp-order-sync
description: |
  ERP (旺店通/万里牛/聚水潭) 多平台订单同步。各平台订单 → ERP 统一处理
  → 发货 → 回传单号 + 物流状态。Use when 订单同步 / 拉单 / ERP 同步.
allowed-tools: [Bash, Read, Write]
triggers: [订单同步, 拉单, ERP 同步]
ecom: { domain: 09-supply-chain, platform: all, role: 仓储, frequency: hourly }
---

# ERP 订单同步

## Step 1: 从各平台拉未同步订单
```bash
source /home/user/AI/.claude/skills/_ecom/lib/credentials.sh
# 天猫奇门 / 京东 POP API / 抖店 / 拼多多开放平台 / 小红书 / 视频号
```

## Step 2: 字段映射 + 去重
统一 SKU 映射（ERP SKU ↔ 平台商家编码），去重订单号。

## Step 3: 写入 ERP
```bash
# 旺店通 API：https://open.wangdian.cn/openapi2/order/push
```

## Step 4: 回传已发货单号 → 各平台
```bash
# 同样按平台 API 写回物流单号
```

## Step 5: 异常订单标记
地址异常 / 黄牛疑似 / 批量下单 → 打标 + 人工审。
