---
name: ecom-qualification-expiry-tracker
description: |
  资质到期追踪。每日巡逻本司资质库，7/30/90 天三档告警，提前续期 + 平台
  重传提醒。Use when 资质到期 / 资质续期 / 蓝帽子到期.
allowed-tools: [Bash, Read, Write]
triggers: [资质到期, 资质续期, 蓝帽子到期]
ecom: { domain: 11-compliance, role: 合规, frequency: daily }
---

# 资质到期追踪

## Step 1: 扫本司资质库
```bash
QUAL=~/.zhongtai/qualifications/*.json
```
每个记录含: 资质类型 / 证号 / 有效期 / 平台 / 责任人。

## Step 2: 计算剩余天数
- ≤ 7 天 → 🔴 电话 + 飞书 @责任人 @老板
- ≤ 30 天 → 🟠 飞书 @责任人
- ≤ 90 天 → 🟡 周报

## Step 3: 各平台上传状态同步
若平台已传 → 提前 30 天提醒重新上传新版。
