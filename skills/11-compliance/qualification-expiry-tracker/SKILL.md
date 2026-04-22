---
name: qualification-expiry-tracker
domain: 11-compliance
platform: all
role: 合规
frequency: daily
inputs: []
outputs:
  - 到期资质清单 + 紧急程度
  - 飞书推送 + 责任人
human_review_required: false
compliance_filter: false
data_sources:
  - 内部资质库
allowed-tools:
  - Read
  - Write
  - Bash
---

# 资质到期追踪 (`qualification-expiry-tracker`)

## 何时调用
每日 8:00 巡逻任务自动跑。

## 输出
- `expiry_report.md`
- 飞书卡片推送到合规群 + 对应责任人

## Workflow
1. 扫内部资质库所有记录
2. 计算到期剩余天数:
   - ≤ 7 天 → 紧急 🔴 电话 + 飞书
   - ≤ 30 天 → 高 🟠 飞书
   - ≤ 90 天 → 中 🟡 周报
3. 生成推送卡片 (资质名 / 产品 / 到期日 / 续期流程链接)
4. 若资质在平台已上传 → 提前 30 天提醒平台重新上传
