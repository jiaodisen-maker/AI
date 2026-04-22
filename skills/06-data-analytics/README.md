# 06-data-analytics 数据分析 (24 skills)

> 跨全平台数据底表 → 指标体系 → 看板 → 归因 → 异常检测.

## 涉及岗位
- 数据分析师
- BI 工程师
- 增长运营

## Skill 清单

### A. 指标体系 (3)
- [gmv-decompose](gmv-decompose/) — GMV 5 层驱动树
- [metrics-dictionary-build](metrics-dictionary-build/) — 指标字典
- [target-cascade](target-cascade/) — 目标逐层分解

### B. 报表 (4)
- [daily-report-generate](daily-report-generate/) — 日报
- [weekly-report-generate](weekly-report-generate/) — 周报
- [monthly-report-generate](monthly-report-generate/) — 月报
- [dual11-warroom-dashboard](dual11-warroom-dashboard/) — 大促作战看板

### C. 归因 (2)
- [channel-attribution-split](channel-attribution-split/) — 渠道拆分
- [multi-touch-attribution](multi-touch-attribution/) — 多触点归因

### D. 用户分析 (4)
- [rfm-segment](rfm-segment/) — RFM 8 段
- [aipl-build](aipl-build/) — AIPL 人群资产
- [aarrr-funnel](aarrr-funnel/) — AARRR 漏斗
- [cohort-retention](cohort-retention/) — 留存曲线

### E. 商品分析 (4)
- [bestseller-detect](bestseller-detect/) — 爆款识别
- [dead-stock-detect](dead-stock-detect/) — 滞销识别
- [product-lifecycle-stage](product-lifecycle-stage/) — 生命周期分级
- [sku-portfolio-abc](sku-portfolio-abc/) — ABC 分析

### F. 流量分析 (2)
- [traffic-source-breakdown](traffic-source-breakdown/) — 来源结构
- [keyword-performance](keyword-performance/) — 关键词表现

### G. 异常检测 (3)
- [roi-drop-alarm](roi-drop-alarm/) — ROI 异常下跌
- [stockout-alarm](stockout-alarm/) — 缺货预测
- [negative-review-spike](negative-review-spike/) — 负面暴增

### H. 工具 (2)
- [feishu-multidim-sync](feishu-multidim-sync/) — 飞书多维表格
- [bi-dashboard-build](bi-dashboard-build/) — BI 看板搭建

## 数据源接入清单

| 数据源 | 类型 | 覆盖 |
|--------|------|------|
| 生意参谋 | 官方后台 | 天猫/淘宝 |
| 数据银行 | 官方后台 | 阿里系 AIPL |
| 巨量算数 | 官方 | 抖音行业 |
| 巨量百应 | 官方 | 抖音达人 |
| 抖店罗盘 | 官方 | 抖店 |
| 千瓜 | 第三方 | 小红书 |
| 新红 | 第三方 | 小红书 |
| 蝉妈妈 | 第三方 | 抖音 |
| 飞瓜 | 第三方 | 抖音/快手 |
| 京东商智 | 官方 | 京东 |
| 奇门 API | 官方 | 订单/商品/库存 |
| ERP (旺店通等) | 内部 | 订单/库存 |

## 指标口径（不可歧义）

- **GMV**: 含未支付，下单即计
- **成交 GMV**: 仅支付
- **回款 GMV**: 扣退款后
- **ROI**: GMV / 投放花费（不是毛利 / 投放）
- **ROAS**: 等同 ROI
- **CPC**: 花费 / 点击
- **CPA**: 花费 / 转化（成交）
- **CTR**: 点击 / 曝光
- **CVR**: 转化 / 点击
- **UV 价值**: GMV / UV
- **复购率**: 90 日内再次购买人数 / 首购人数（口径可配）
- **LTV**: 用户生命周期 GMV

## 异常告警机制

所有异常检测 skill → 触发 → [qiwei-sop-trigger](../03-private-domain/qiwei-sop-trigger/) 推送飞书 + 企微 + 建议动作。

## 依赖的跨域 skill
- 所有其他 domain 都会消费本 domain 的 daily/weekly-report
- CRM 分层 → [07-crm/user-value-segment](../07-crm/user-value-segment/)
- 异常 → 触发 → [04-paid-ads/qianchuan-realtime-optimize](../04-paid-ads/qianchuan-realtime-optimize/)
