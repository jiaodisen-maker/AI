# 09-supply-chain 供应链/库存 (14 skills)

> 入库、批次效期、安全库存、补货、仓配、ERP 同步.

## 涉及岗位
- 供应链 / 库存管理员
- 采购
- 仓储
- ERP 管理员

## Skill 清单

### A. 入库 / 效期 (4)
- [inv-inbound-receive](inv-inbound-receive/) — 入库收货 + 批号 + 抽检
- [inv-batch-expiry-track](inv-batch-expiry-track/) — 批次效期追踪
- [inv-fefo-pick-rule](inv-fefo-pick-rule/) — FEFO 先效先出
- [inv-qc-report-archive](inv-qc-report-archive/) — 质检报告按批次归档

### B. 库存看板 / 预警 (4)
- [inv-stock-dashboard](inv-stock-dashboard/) — 实时库存
- [inv-safety-stock-calc](inv-safety-stock-calc/) — 安全库存
- [inv-stockout-alert](inv-stockout-alert/) — 缺货预警
- [inv-overstock-alert](inv-overstock-alert/) — 积压预警

### C. 补货 / 采购 (2)
- [inv-replenish-plan](inv-replenish-plan/) — 补货计划
- [inv-purchase-order](inv-purchase-order/) — 采购单

### D. 仓配 / 物流 (2)
- [inv-multi-warehouse-alloc](inv-multi-warehouse-alloc/) — 多仓调拨
- [inv-ship-sla-monitor](inv-ship-sla-monitor/) — 发货时效

### E. ERP / 异常 (2)
- [inv-erp-order-sync](inv-erp-order-sync/) — ERP 订单同步
- [inv-damage-report](inv-damage-report/) — 报损/报溢

## 保健品供应链特殊点
- **批次 + 效期**: 蓝帽子产品强制管理，每个批次都需质检报告 COA 归档
- **FEFO**: 先效先出，不按 FIFO (先进先出)
- **临期处理**: 90/60/30 天三档告警，触发促销/下架/报损
- **跨境**: 进口保健品备进口商资质 + 完税证明

## ERP 覆盖
- 旺店通 / 万里牛 / 聚水潭 / 易仓（跨境）
- 菜鸟 / 京东物流 / 顺丰丰畅 / 云仓

## 依赖的跨域 skill
- 缺货触发 → [04-paid-ads/qianchuan-realtime-optimize](../04-paid-ads/) 关计划
- 缺货触发 → [01-shelf-commerce/shelf-inventory-sync](../01-shelf-commerce/) 平台同步
- 报损触发 → [10-finance/fin-damage-report](../10-finance/)
