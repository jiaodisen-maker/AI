---
name: live-script-precheck
domain: 11-compliance
platform: douyin | kuaishou | shipinghao | xiaohongshu | tmall | jd
role: 合规
frequency: per-live-session
inputs:
  - script: 直播脚本
  - anchor_name: 主播身份 (含资质: 营养师 / 药师 / 普通主播)
  - products: 参播 SKU 列表
outputs:
  - 合规报告 + 逐段修订
  - 主播培训卡 (口播禁语清单)
human_review_required: true
compliance_filter: false
data_sources:
  - 违禁词库
  - 平台直播合规规范
allowed-tools:
  - Read
  - Write
---

# 直播脚本合规预审 (`live-script-precheck`)

## 何时调用
直播开播前 24 小时，法务/合规岗过脚本。

## 输入
- **script** — 完整直播脚本 (含开场/产品讲解/催单/承接)
- **anchor_name** — 主播身份
- **products** — 产品 SKU + 蓝帽子批文 + 广告批文

## 输出
- `compliance_report.md` — 逐段标注风险
- `anchor_training_card.pdf` — 口播禁语清单

## Workflow
1. 分段: 开场 / 产品介绍 / demo / 价格 / 催单 / 承接 / 下播
2. 对每段跑 `forbidden-word-scan` + `27-function-validator`
3. 校验必带声明: "本品不能代替药物" 至少每 30 分钟一次
4. 校验 demo: 不得现场演示"治病""减重前后对比"
5. 校验产品资质是否已挂直播间悬浮挂件
6. 校验主播资质 vs 声明权限 (普通主播不可做医学建议)
7. 生成主播培训卡 + 监播提醒卡

## 常见违规
- "姐妹们这个真的管用,我自己吃了三个月瘦了十斤" → block
- 对比药品价格 "这比去医院便宜多了" → block
- "免费领,吃不好全额退款" → 需核对承诺
