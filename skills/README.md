# skills/

国内电商运营全工作流 skill 化 — 为保健品 AI 中台沉淀的 223 个能力。

## 文档入口

- [FRAMEWORK.md](FRAMEWORK.md) — 设计原则、运行时形态、合规要点
- [INDEX.md](INDEX.md) — 223 个 skill 完整索引

## 12 大领域

01. [shelf-commerce 货架电商](01-shelf-commerce/) — 天猫/淘宝/京东/拼多多 日常运营
02. [content-commerce 内容兴趣电商](02-content-commerce/) — 抖音/快手/视频号/小红书
03. [private-domain 私域](03-private-domain/) — 微信生态全套
04. [paid-ads 付费投放](04-paid-ads/) — 千川/万相台/京准通/聚光等
05. [live-commerce 直播带货](05-live-commerce/) — 自播+达播全流程
06. [data-analytics 数据分析](06-data-analytics/) — 看板/归因/异常
07. [crm CRM/会员](07-crm/) — 用户分层/自动化触达
08. [customer-service 客服](08-customer-service/) — 售前售后/合规话术
09. [supply-chain 供应链/库存](09-supply-chain/) — 批次效期/安全库存
10. [finance 财务对账](10-finance/) — 平台账单/达人结算
11. [compliance 合规·保健品](11-compliance/) — 广告法/蓝帽子/平台规则
12. [product-selection 选品/新品/竞品](12-product-selection/) — 决策依据

## 调用方式

任意 SKILL.md 可被三种方式调用：

```bash
# 1. Claude Code 本地（dev/dogfood）
ln -s skills/01-shelf-commerce/tmall-store-daily-check .claude/skills/
# 然后 /tmall-store-daily-check

# 2. 飞书 Bot（生产）
# Bot 收到 "做个店铺日检" → Agent SDK → 路由到 tmall-store-daily-check skill

# 3. 定时巡逻（patrol）
# cron 8:00 → 调用 patrol-runner → 拉 daily 频次的所有 skill 跑
```

## 贡献

新增 skill：
1. `mkdir skills/<domain>/<skill-name>`
2. 复制 `_template/SKILL.md` 填写
3. 在所属 domain 的 README.md 加一行
4. 在 INDEX.md 加一行
5. PR 提交，走 review

修改 skill：直接 PR；如果改了输出 schema，需通知所有调用方。
