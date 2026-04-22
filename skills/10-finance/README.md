# 10-finance 财务/对账 (10 skills)

> 平台账单、退款、达人佣金、投放费用、发票.

## 涉及岗位
- 财务
- 电商运营（初审）

## Skill 清单

### A. 平台账单 (5)
- [fin-tmall-bill-reconcile](fin-tmall-bill-reconcile/) — 天猫货款/佣金
- [fin-jd-bill-reconcile](fin-jd-bill-reconcile/) — 京东货款
- [fin-douyin-bill-reconcile](fin-douyin-bill-reconcile/) — 抖音货款/服务费
- [fin-pdd-bill-reconcile](fin-pdd-bill-reconcile/) — 拼多多货款
- [fin-xiaohongshu-bill-reconcile](fin-xiaohongshu-bill-reconcile/) — 小红书货款

### B. 退款 / 佣金 (2)
- [fin-refund-reconcile](fin-refund-reconcile/) — 退款三方对账
- [fin-talent-commission-settle](fin-talent-commission-settle/) — 达人佣金结算

### C. 广告费 (1)
- [fin-ad-spend-reconcile](fin-ad-spend-reconcile/) — 投放费用对账

### D. 发票 (2)
- [fin-vat-invoice-issue](fin-vat-invoice-issue/) — 增票开具
- [fin-vat-invoice-collect](fin-vat-invoice-collect/) — 进项发票归档

## 平台扣点速查（注意随平台政策变动）
- 天猫: 类目技术服务费 2-5% + 营销扣点
- 京东 POP: 5-8%
- 抖音: 技术服务费 5-10% (类目差异)
- 小红书: 综合服务费 5-10%
- 拼多多: 货款提现手续费

## 依赖的跨域 skill
- 数据来源 → [06-data-analytics/channel-attribution-split](../06-data-analytics/channel-attribution-split/)
- 退款数据 → [09-supply-chain/inv-erp-order-sync](../09-supply-chain/inv-erp-order-sync/)
