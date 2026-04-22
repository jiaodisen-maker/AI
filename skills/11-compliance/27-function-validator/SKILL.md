---
name: 27-function-validator
domain: 11-compliance
platform: all
role: 合规
frequency: on-demand
inputs:
  - claim: 宣传文案中的功效声明
  - product_blue_cap_number: 产品蓝帽子备案号
outputs:
  - 每条声明的合规状态 + 备案原功能 + 偏差说明
human_review_required: true
compliance_filter: false
data_sources:
  - 内部蓝帽子备案库
  - 国家市场监督管理总局 特殊食品信息查询平台
allowed-tools:
  - Read
  - Write
  - WebFetch
---

# 蓝帽子 27 项功能校验 (`27-function-validator`)

## 何时调用
保健食品文案/直播脚本/详情页声明发布前，校验是否"扩大宣传"。

## 输入
- **claim** (必填) — string — 宣传文案里的功效声明句子
- **product_blue_cap_number** (必填) — 蓝帽子批号（国食健字 XXX / 卫食健字 XXX）

## 输出
- `matched_function`: 27 项中对应的一项
- `claim_vs_registered`: exact | narrower | broader | unrelated
- `action`: pass | block | rewrite
- `suggested_rewrite`: 如 broader → 改窄

## Workflow
1. 查产品备案信息 → 获取注册/备案的功能项
2. 对宣传声明做语义分类 → 映射到 27 项之一
3. 比对:
   - exact 一致 → pass
   - narrower 声明比备案窄 → pass (允许降级)
   - broader 声明比备案宽 → block (必改)
   - unrelated 与备案无关 → block (必改)
4. 输出偏差 + 建议改写

## 27 项功能清单
（见 [../README.md](../README.md)）

## 判定示例

| 备案 | 声明 | 判定 |
|------|------|------|
| 辅助降血脂 | 辅助降血脂 | exact ✅ |
| 辅助降血脂 | 降血脂 | broader ❌ (少了"辅助") |
| 辅助降血脂 | 防心梗 | unrelated ❌ |
| 增强免疫力 | 支持免疫 | narrower ✅ |
| 通便 | 治便秘 | broader ❌ (涉及疗效) |

## 失败/降级
- 备案查不到 → error + 建议上传资质
- 声明无法分类 → warn + 人工审
