---
name: ecom-warning-statement-insert
description: |
  自动插入「本品不能代替药物治疗疾病」警示语 + 蓝帽子 logo + 广告批文号。
  按媒介 (图文/短视频/直播/详情页/朋友圈) 选合适位置。Use when 插警示语 /
  加提示 / 本品不能代替药物.
allowed-tools: [Bash, Read, Write]
triggers: [插警示语, 加提示语, 本品不能代替药物]
ecom: { domain: 11-compliance, role: 合规, frequency: on-demand }
---

# 插警示语

## Step 1: 按 medium 决定位置
- 图文: 图角标 + 文末
- 短视频: 画面字幕 (全程) + 至少一次口播
- 直播: 悬浮挂件 + 每 30min 口播
- 详情页: 首屏 + 购买按钮附近
- 朋友圈: 文末 + 九宫格第 9 张

## Step 2: 必带元素
- 「本品不能代替药物治疗疾病」
- 蓝帽子 logo
- 广告批文号 (如有)
- 适宜/不适宜人群 (详情页必须)

## Step 3: 输出带位置标注的 markdown
Write 到 artifacts，供后续排版用。
