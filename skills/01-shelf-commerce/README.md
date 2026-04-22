# 01-shelf-commerce 货架电商运营 (28 skills)

> 天猫/淘宝/京东/拼多多 三个主流货架电商平台的日常运营工作。

## 涉及岗位
- 店铺运营 / 店长
- 商品运营 / 上架专员
- 视觉 / 装修
- 数据运营（见 06）
- 客服主管（见 08）

## 涉及平台后台
- 天猫/淘宝: 千牛 / 生意参谋 / 旺铺装修 / 阿里妈妈
- 京东: 京麦 / 京东商智 / 京准通
- 拼多多: 多多工作台 / 多多推广 / 数据中心

## Skill 清单

### A. 日常体检 (4)
- [tmall-store-daily-check](tmall-store-daily-check/) — 千牛日检: 健康分/待办/订单/差评/违规
- [jd-store-daily-check](jd-store-daily-check/) — 京麦日检: 京东店铺健康/订单/售后
- [pdd-store-daily-check](pdd-store-daily-check/) — 拼多多多多工作台日检
- [shelf-weekly-report](shelf-weekly-report/) — 货架电商周报自动生成

### B. 商品运营 (5)
- [taobao-product-publish](taobao-product-publish/) — 淘宝商品发布/上架/类目属性
- [tmall-product-optimize](tmall-product-optimize/) — 天猫商品标题/主图/详情页优化
- [jd-product-publish](jd-product-publish/) — 京东商品发布/SKU/属性/库存
- [pdd-product-publish](pdd-product-publish/) — 拼多多商品发布/参团/秒杀
- [shelf-bundle-config](shelf-bundle-config/) — 组合装/赠品装/SKU 捆绑配置

### C. 价格 / 库存 / 优惠 (3)
- [shelf-sku-price-adjust](shelf-sku-price-adjust/) — 跨平台价格调整 + 比价合规
- [shelf-inventory-sync](shelf-inventory-sync/) — ERP ↔ 各平台库存同步 + 缺货预警
- [shelf-coupon-plan](shelf-coupon-plan/) — 优惠券/满减/跨店满减方案

### D. 活动 / 大促 (5)
- [tmall-activity-signup](tmall-activity-signup/) — 聚划算/淘抢购/百亿补贴报名
- [jd-activity-signup](jd-activity-signup/) — 京东秒杀/京超/京东健康报名
- [pdd-activity-signup](pdd-activity-signup/) — 拼多多百亿补贴/限时秒杀报名
- [cross-platform-activity-calendar](cross-platform-activity-calendar/) — 大促档期日历
- [shelf-presale-deposit](shelf-presale-deposit/) — 大促预售定金/尾款节奏

### E. 视觉 / 装修 (3)
- [store-homepage-layout](store-homepage-layout/) — 旺铺/店铺首页装修
- [detail-page-ab-test](detail-page-ab-test/) — 详情页 A/B 测试
- [tmall-shop-decoration](tmall-shop-decoration/) — 天猫旺铺装修版本管理

### F. 流量 / 数据 (4)
- [sheng-yi-can-mou-pull](sheng-yi-can-mou-pull/) — 生意参谋数据拉取 + 清洗
- [sheng-yi-can-mou-keyword-mining](sheng-yi-can-mou-keyword-mining/) — 热搜词/蓝海词挖掘
- [jd-business-intelligence-pull](jd-business-intelligence-pull/) — 京东商智数据拉取
- [pdd-data-center-pull](pdd-data-center-pull/) — 拼多多数据中心拉取

### G. 会员 / 老客 (2)
- [customer-return-review](customer-return-review/) — 老客回访/短信/旺旺/京麦触达
- [shelf-free-sample-campaign](shelf-free-sample-campaign/) — 试用中心/众测投放

### H. 风控 / 合规 (2)
- [shelf-violation-appeal](shelf-violation-appeal/) — 平台违规申诉单生成
- [shelf-ip-dispute](shelf-ip-dispute/) — 知识产权投诉/维权

## 关键数据流

```
运营进场 → 拉 日检数据 → 发现异常 → 追根因（流量/转化/库存/投放）
                    ↓
            生成待办单 → 分派（自己/客服/投手/视觉）
                    ↓
            动作执行（改详情/报活动/加库存/调价）
                    ↓
            当日复盘 + 次日日检闭环
```

## 保健品类目注意
- **类目报白**: 天猫"滋补保健"需品牌授权 + 蓝帽子
- **京东**: 医药保健需经营许可证 + 保健食品注册证书
- **拼多多**: 健康食品/保健品类目需逐一上传证书
- **抖音/快手**: 虽不在本 domain 但需注意类目申请（见 02）

## 依赖的跨域 skill
- 合规扫描 → [11-compliance/forbidden-word-scan](../11-compliance/forbidden-word-scan/)
- 数据看板 → [06-data-analytics/daily-report-generate](../06-data-analytics/daily-report-generate/)
- 库存预警 → [09-supply-chain/inv-stockout-alert](../09-supply-chain/inv-stockout-alert/)
