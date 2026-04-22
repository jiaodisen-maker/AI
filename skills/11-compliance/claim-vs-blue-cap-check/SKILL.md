---
name: claim-vs-blue-cap-check
domain: 11-compliance
platform: all
role: 合规
frequency: on-demand
inputs:
  - claim_list: 所有对外声明（列表）
  - blue_cap_number
outputs:
  - 每条声明的一致性判定
human_review_required: true
compliance_filter: false
data_sources:
  - 国家总局特殊食品信息查询
allowed-tools:
  - Read
  - WebFetch
---

# 声明 vs 蓝帽子备案一致性检查 (`claim-vs-blue-cap-check`)

## 何时调用
新品上架前，或批量审核旧文案时。

## 输入
- **claim_list** (必填) — `[{source, text}]` — 来自详情页/文案/直播的声明
- **blue_cap_number** (必填) — 蓝帽子批号

## 输出
- 每条声明 → `{consistent: bool, reason, suggested_rewrite}`
- 汇总报告 markdown

## Workflow
1. 查蓝帽子备案 → 拿到批文中的:
   - 功能 (必须在 27 项中)
   - 适宜人群
   - 不适宜人群
   - 食用量
   - 食用方法
2. 扫所有声明 → 逐条比对:
   - 功能声明 → 走 [27-function-validator](../27-function-validator/)
   - 人群声明 → 不能缺"不适宜人群"
   - 食用量 → 不能超过批文
3. 输出全量一致性报告

## 常见违规
- 备案适宜人群写"免疫力低下者"，广告写"所有人"
- 备案"辅助降血脂"，广告写"降血脂"
- 备案"食用量 2 粒/日"，广告写"多吃效果更好"
