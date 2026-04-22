# 11-compliance 合规·保健品 (12 skills)

> 整个体系的护城河。保健品行业的合规成本 = 不做合规的处罚成本 × 10。

## 为什么这个 domain 最重要

- 《广告法》处罚: 广告费 1-3 倍 或 20-100 万元
- 《反不正当竞争法》: 最高 175 万元 (辛选案例)
- 《食品安全法》: 货值 10-30 倍
- 《电子商务法》: 平台下架 / 限流 / 封店
- 刑事风险: 虚假宣传达到"情节严重"可入刑

## Skill 清单

### A. 违禁词 (3)
- [forbidden-word-scan](forbidden-word-scan/) — 扫描极限词/医疗词/暗示功效词
- [ad-copy-rewrite](ad-copy-rewrite/) — 不合规文案自动改写
- [warning-statement-insert](warning-statement-insert/) — 警示语插入

### B. 蓝帽子 / 资质 (3)
- [27-function-validator](27-function-validator/) — 27 项功能校验 + 不扩大宣传
- [claim-vs-blue-cap-check](claim-vs-blue-cap-check/) — 声明 vs 备案一致性
- [qualification-upload-checklist](qualification-upload-checklist/) — 资质上传清单

### C. 内容审核 (3)
- [live-script-precheck](live-script-precheck/) — 直播脚本开播前审
- [kol-script-precheck](kol-script-precheck/) — KOL 达人稿预审
- [testimonial-compliance-check](testimonial-compliance-check/) — 见证/案例合规

### D. 平台规则 / 监控 (3)
- [qualification-expiry-tracker](qualification-expiry-tracker/) — 资质到期追踪
- [platform-health-rule-monitor](platform-health-rule-monitor/) — 各平台规则更新
- [live-replay-audit](live-replay-audit/) — 直播回放抽审

## 三类违禁词库 (贯穿所有内容/客服/直播 skill)

### 1. 绝对化用语
最 / 第一 / 国家级 / 100% / 顶级 / 唯一 / 王牌 / 绝对 / 最佳 / 最优 / 最高级 / 最新科学 / 最先进 / 独一无二 / 前无古人 / ...

### 2. 医疗功效词
治疗 / 治愈 / 根治 / 速效 / 抗癌 / 降三高 / 防癌 / 抑制 XX / 替代药品 / 疗效 / 药到病除 / ...

### 3. 暗示功效词
瘦十斤 / 三天见效 / 吃了就好 / 再也不用吃药 / ...（含谐音黑话）

### 4. 必带声明
- **保健食品广告**: "本品不能代替药物治疗疾病"
- **普通食品广告**: 不得宣称保健功能

## 蓝帽子 27 项功能（含糊对应，不可扩大）

1. 增强免疫力
2. 辅助降血脂
3. 辅助降血糖
4. 辅助降血压
5. 抗氧化
6. 辅助改善记忆
7. 缓解视疲劳
8. 促进排铅
9. 清咽
10. 改善睡眠
11. 促进泌乳
12. 缓解体力疲劳
13. 提高缺氧耐受力
14. 对辐射危害有辅助保护
15. 减肥
16. 改善生长发育
17. 增加骨密度
18. 改善营养性贫血
19. 对化学性肝损伤有辅助保护
20. 祛痤疮
21. 祛黄褐斑
22. 改善皮肤水分
23. 改善皮肤油分
24. 调节肠道菌群
25. 促进消化
26. 通便
27. 对胃粘膜损伤有辅助保护

**规则**: 你备案了什么功能，就只能宣传什么功能；不能把"辅助降血脂"宣传成"降血脂"（去掉"辅助"就违规）。

## 接入方式

每个内容生成类 skill frontmatter 必须:
```yaml
compliance_filter: true
```

运行时: 输出 → 自动走 `forbidden-word-scan` → 命中则 block + `ad-copy-rewrite` → 再过 → 放行/人工审。

## 依赖的跨域 skill
- 所有内容 / 客服 / 直播 skill 都挂本 domain 的过滤器
