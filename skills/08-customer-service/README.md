# 08-customer-service 客服运营 (14 skills)

> 售前、售后、差评、纠纷、FAQ、机器人训练.

## 涉及岗位
- 售前客服
- 售后客服
- 客服主管
- 知识库管理员
- 智能客服训练师

## Skill 清单

### A. 售前 (4)
- [cs-presale-consult-reply](cs-presale-consult-reply/) — 咨询应答 (合规口径)
- [cs-price-negotiate-script](cs-price-negotiate-script/) — 议价话术
- [cs-recommend-bundle](cs-recommend-bundle/) — 组合推荐
- [cs-urge-payment](cs-urge-payment/) — 催付

### B. 售后 (5)
- [cs-logistics-followup](cs-logistics-followup/) — 物流异常
- [cs-return-exchange-flow](cs-return-exchange-flow/) — 退换货
- [cs-refund-only-review](cs-refund-only-review/) — 仅退款审核
- [cs-bad-review-handle](cs-bad-review-handle/) — 差评应对
- [cs-dispute-escalate](cs-dispute-escalate/) — 纠纷升级

### C. 管理 / 训练 (5)
- [cs-faq-knowledge-build](cs-faq-knowledge-build/) — FAQ/话术库
- [cs-forbidden-word-check](cs-forbidden-word-check/) — 外发话术违禁词
- [cs-complaint-classify](cs-complaint-classify/) — 客诉分类
- [cs-bot-intent-train](cs-bot-intent-train/) — 机器人意图训练
- [cs-shift-schedule](cs-shift-schedule/) — 排班

## 关键指标
- 3 分钟人工回复率 ≥ 95%
- 客服询单转化率
- DSR (服务 / 描述 / 物流)
- 客诉率、升级率、闭环时长

## 保健品客服合规口径 (必培训)
- 不得承诺疗效: "治好 XX / 包治 / 见效"等禁语
- 功效话术: "辅助 X"「有助于」「帮助维持」（不可"治疗"）
- 必带话术: "本品不能代替药物，请遵医嘱"
- 敏感咨询（有 XX 病能不能吃）: 模板回答 + "建议咨询医生"
- 用户晒证言/前后对比 → 不得诱导写疗效词

所有外发话术自动过: [forbidden-word-scan](../11-compliance/forbidden-word-scan/)

## 依赖的跨域 skill
- 违禁词 → [11-compliance](../11-compliance/)
- 订单 → [09-supply-chain/inv-erp-order-sync](../09-supply-chain/)
- 评价 → [06-data-analytics/negative-review-spike](../06-data-analytics/)
