---
name: kol-script-precheck
domain: 11-compliance
platform: douyin | kuaishou | shipinghao | xiaohongshu | bilibili
role: 合规
frequency: per-cooperation
inputs:
  - kol_draft: KOL 提交的稿件/脚本
  - kol_info: 达人信息 (粉丝量/认证/带货品类)
  - cooperation_type: 短视频 / 直播 / 图文
outputs:
  - 审核意见 + 修订版
  - 合同合规条款 (违禁词罚则)
human_review_required: true
compliance_filter: false
data_sources:
  - 违禁词库
  - 达人历史违规记录
allowed-tools:
  - Read
  - Write
---

# KOL/达人稿预审 (`kol-script-precheck`)

## 何时调用
达人合作报备稿发布前；直播合作开播前。

## 输入
- **kol_draft** — 达人原稿
- **kol_info** — 粉丝量 / 认证类型
- **cooperation_type** — 合作形式

## 输出
- `review_comments.md`
- `final_script.md`
- `contract_clauses.md` — 可嵌入合同的违规罚则

## Workflow
1. 核对达人粉丝量: 保健食品禁"具有一定影响力"代言 (惯例 100 万粉以上 KOL 受限)
2. 跑 `forbidden-word-scan` + `27-function-validator`
3. 核对必带元素: 平台报备标识 (如小红书蒲公英) / 广告标 / 必带声明
4. 核对带货品类: 保健品 × 医美 × 药品 差异化限制
5. 核对 demo 内容: 不得现场"治病"展示
6. 生成修订版 + 合同合规条款（违规罚则金额）

## 合同合规条款示例
- "若因达人违规口播导致品牌被罚, 达人承担 3 倍罚款金额"
- "违规内容需 2 小时内下架; 逾期每小时扣款 5000 元"
- "达人历史违规记录 ≥ 2 次者, 品牌有权单方解约且不退坑位费"
