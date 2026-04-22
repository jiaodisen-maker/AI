# 04-paid-ads 付费投放 (22 skills)

> 跨全网主流广告平台的投放运营 — 从账户搭建、计划搭建、素材、实时调控到复盘。

## 涉及岗位
- 投放优化师 / 投手
- 素材策划
- 数据分析师
- 账户管理员

## 涉及平台
- 巨量引擎系: 巨量千川 / DOU+ / 巨量星图 / 巨量本地推
- 阿里系: 万相台无界版 (直通车/引力魔方/品销宝)
- 京东: 京准通 (快车/直投/DSP/京挑客)
- 拼多多: 多多搜索/多多场景/全站推广
- 小红书: 聚光 / 薯条 / 蒲公英
- 腾讯系: 朋友圈 ADQ / 视频号推流 / 微信豆
- B 站: 花火 / 必火 / 起飞
- 知乎: 知 + / 效果广告
- 百度: 信息流 / oCPC / 品专

## Skill 清单

### A. 巨量千川 (5)
- [qianchuan-plan-build](qianchuan-plan-build/) — 计划搭建
- [qianchuan-creative-test](qianchuan-creative-test/) — 素材 A/B
- [qianchuan-realtime-optimize](qianchuan-realtime-optimize/) — 实时调控
- [qianchuan-roi-report](qianchuan-roi-report/) — ROI 复盘
- [qianchuan-dmp-audience](qianchuan-dmp-audience/) — DMP 人群包

### B. 其他抖音系 (1)
- [dou-plus-boost](dou-plus-boost/) — DOU+/随心推加热

### C. 阿里系 (3)
- [wanxiangtai-plan-build](wanxiangtai-plan-build/) — 万相台计划
- [zhitongche-keyword-optimize](zhitongche-keyword-optimize/) — 直通车关键词
- [yinlimofang-audience](yinlimofang-audience/) — 引力魔方人群溢价

### D. 京东 (2)
- [jingzhuntong-plan-build](jingzhuntong-plan-build/) — 京准通计划搭建
- [jingzhuntong-optimize](jingzhuntong-optimize/) — 京准通实时调控

### E. 拼多多 (2)
- [pdd-duoduo-search-ad](pdd-duoduo-search-ad/) — 多多搜索投放
- [pdd-duoduo-scene-ad](pdd-duoduo-scene-ad/) — 多多场景/全站推广

### F. 小红书 (2)
- [xiaohongshu-juguang-plan](xiaohongshu-juguang-plan/) — 聚光信息流/搜索
- [xiaohongshu-shutiao-boost](xiaohongshu-shutiao-boost/) — 薯条加热

### G. 微信系 (3)
- [pengyouquan-ad-plan](pengyouquan-ad-plan/) — 朋友圈 ADQ
- [adq-video-plan](adq-video-plan/) — 视频号 ADQ + 微信豆
- [weixin-dou-boost](weixin-dou-boost/) — 微信豆老客触达

### H. 其他 (3)
- [bilibili-huahuo-plan](bilibili-huahuo-plan/) — B 站花火 UP 主商单
- [zhihu-plus-plan](zhihu-plus-plan/) — 知 + 加热
- [baidu-ocpc-plan](baidu-ocpc-plan/) — 百度 oCPC/搜索

### I. 共用 (1)
- [creative-script-library](creative-script-library/) — 跨平台素材脚本库

## 跨平台共用规范

### 命名
`日期_平台_产品_目标_人群_出价_素材ID_版本` 全公司统一。

### 素材生命周期
测试 → 跑量 → 衰减 → 封存 → 违规（五阶段标签）

### 归因
- Last-touch: 粗粒度监控
- Multi-touch: 大促复盘
- UTM + clickid: 跨域归因透传到 CRM

## 保健品投放特殊限制

1. **资质三件套必须上传**: 营业执照、保健食品 SC 证 + 蓝帽子、广告批文 (国食健广审字)
2. **素材必带**: 「保健食品不能代替药物」+ 蓝帽子 logo + 批文号
3. **禁用**: 明星代言 / 医生形象 / 患者形象 / 未经证实功效 / 暗示功效
4. **平台类目准入**: 千川/聚光/京准通 均需"保健品类目报白"
5. **行业 RTA / DMP**: 保健品常用"高净值养生人群包"+"慢病兴趣包"，需行业白名单

参考: [11-compliance/forbidden-word-scan](../11-compliance/forbidden-word-scan/)

## 依赖的跨域 skill
- 数据归因 → [06-data-analytics/channel-attribution-split](../06-data-analytics/channel-attribution-split/)
- 素材创意 → [02-content-commerce/*-script-write](../02-content-commerce/)
- 直播投流 → [05-live-commerce/live-realtime-buy-plan](../05-live-commerce/live-realtime-buy-plan/)
- 财务对账 → [10-finance/fin-ad-spend-reconcile](../10-finance/fin-ad-spend-reconcile/)
