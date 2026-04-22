---
name: platform-health-rule-monitor
domain: 11-compliance
platform: all
role: 合规
frequency: weekly
inputs: []
outputs:
  - 规则变动日志 + 影响分析 + 行动项
human_review_required: true
compliance_filter: false
data_sources:
  - 天猫规则中心
  - 京东规则中心
  - 抖店规则中心
  - 小红书社区规范
  - 拼多多商家平台
  - 视频号助手规则
  - 市场监管总局 / 各地市监局
allowed-tools:
  - WebFetch
  - Read
  - Write
---

# 平台保健品规则更新监控 (`platform-health-rule-monitor`)

## 何时调用
每周一 9:00 巡逻任务。

## 输出
- `rule_diff_YYYYMMDD.md` — 规则对比
- 影响分析 (影响哪些 skill / 哪些店铺 / 哪些产品)
- 行动项分发到对应责任人

## Workflow
1. 抓取各平台规则中心最近 7 天公告 (用 [gstack browse scrape](../../README.md))
2. 过滤关键词: 保健食品 / 滋补 / 健康 / 医疗 / 广告 / 类目
3. 对比本地"规则快照库" → 识别新增/删除/变更
4. 用 LLM 生成影响摘要 (哪些 skill 需要更新、哪些素材需要重审)
5. 推送飞书 + 更新规则快照库

## 监控源
| 平台 | URL / 路径 |
|------|-----------|
| 天猫 | rules.tmall.com |
| 京东 | rule.jd.com |
| 抖店 | school.jinritemai.com |
| 小红书 | help.xiaohongshu.com |
| 拼多多 | rule.pinduoduo.com |
| 视频号 | channels.weixin.qq.com (帮助中心) |
| 市监总局 | samr.gov.cn (政策法规) |

## 近年重大规则变动（参考）
- 2024: 抖音加强保健食品类目准入
- 2024: 小红书发布 22 类违规营销治理
- 2025: 市监总局强化直播带货保健品监管
- 2026: 多平台落地"类目报白 + 资质双重验证"
