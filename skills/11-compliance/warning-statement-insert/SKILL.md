---
name: warning-statement-insert
domain: 11-compliance
platform: all
role: 合规
frequency: on-demand
inputs:
  - content: 已过违禁词的合规文案
  - medium: 图文 / 短视频 / 直播 / 详情页 / 朋友圈
outputs:
  - 插入警示语后的最终文案
  - 插入位置建议
human_review_required: false
compliance_filter: false
data_sources: []
allowed-tools:
  - Write
---

# 警示语插入 (`warning-statement-insert`)

## 何时调用
所有保健食品广告内容发布前。

## 输入
- **content** (必填) — 合规文案
- **medium** (必填) — 发布媒介

## 输出
- 带警示语的文案 (text + 位置标注)

## Workflow
1. 根据 medium 选择警示语位置策略:
   - 图文 → 图片角标 + 文案末尾
   - 短视频 → 画面字幕 + 口播 + 描述
   - 直播 → 悬浮挂件 + 每 30 分钟口播一次
   - 详情页 → 首屏 + 购买按钮附近
2. 插入标准警示语 "本品不能代替药物治疗疾病"
3. 保健食品必带蓝帽子 logo + 广告批文号 (国食健广审字)
4. 根据平台字数限制适配

## 必带元素
- 「本品不能代替药物治疗疾病」
- 蓝帽子 logo (保健食品标志)
- 广告批准文号 (如有)
- 不适宜人群 / 适宜人群 (详情页必须)
