# Coze 知识库（800 人保健品公司落地）

> 最新更新：2026-05-04，基于 951 页官方文档抓取后的方案。
> 真相：这次的数据**全部基于** `raw/` 下抓的 docs.coze.cn 原文。
> 不再基于互联网博客的二手猜测。

## 你应该按这个顺序读

| 文件 | 内容 | 谁该读 |
|---|---|---|
| **`PLAN.md`** | 800 人公司全面落地总方案：套餐/能力/决策矩阵/成本/推广路径 | **你 + 工程师 1（架构师）** |
| **`SALES-BOT.md`** | 销售助手详细方案：架构/数据/工作流/合规/4 周 sprint | **工程师 4-7** |
| **`FEISHU-INTEGRATION.md`** | 飞书 ⇄ 扣子 8 层深度结合：身份/入口/数据/流程/触达/合规/沉淀/治理 | **全员必读** |
| **`MODELS.md`** | 给扣子加第三方大模型让所有人用：3 种方式 + AI Gateway 最佳实践 + 部门授权 + 合规 | **工程师 1+2+你** |
| **`AI-GATEWAY-SETUP.md`** | LiteLLM Proxy 完整部署：Docker Compose + Caddy + Postgres + KMS + PII + 双实例 + 飞书告警 + 验收清单 | **工程师 2 主，工程师 1 review** |
| **`DATA-SECURITY.md`** | 外部数据进来全栈数据安全：12 类威胁 / 4 级分级 / 7 层防御 / 应急预案 / PIPL+保健品合规清单 | **DPO + 法务 + 你 + 工程师 1+6** |
| **`MEMORY-COMPARISON.md`** | Coze 5 种记忆机制 vs GBrain vs Hindsight：决策树 + Reflect 缺口 + 800 人公司具体决策 | **架构师 + 你** |
| `raw/_index.json` | 951 页 URL → 文件映射，按主题导航文档 | 任何人想查原文 |
| `raw/coze_cn/` | 951 页扣子官方文档原文，按板块（coze_pro / cozespace / guides 等）| 工程师查证 |
| `raw/github_coze/` | 73 页 Coze Studio + Coze Loop GitHub wiki | 工程师 1（涉及自部署/扩展时）|

## 951 页内容分布

| 板块 | 页数 | 说明 |
|---|---|---|
| `coze_pro` | 30 | **计费 + 企业版（重要！）** |
| `cozespace` | 27 | Agent World / 云电脑 / 云手机 / 邮箱 |
| `cozeloop` | 120 | 评测 + 观测 + 提示词管理 |
| `guides` | 437 | **主体使用指南**（智能体/工作流/知识库/插件/数据库/记忆）|
| `developer_guides` | 195 | CLI + 开发者指南 |
| `tutorial` | 69 | 实践教程 |
| `customers` | 29 | **客户案例（含医疗行业 shanxi_health）** |
| `dev_how_to_guides` | 32 | how-to |

## ⚠️ 已过时文档（被新数据替代，仅供历史对比）

下列文件基于 2026-01 前的二手数据，**部分数字已过时**。
**不要再引用它们做决策** —— 用 `PLAN.md` + `SALES-BOT.md`。

- ⚠️ `01-platform-overview.md` —— 架构层面大体正确，但缺细节
- ❌ `02-versions-and-pricing.md` —— **数字全错**（4980/300万资源点等）
- ⚠️ `03-coze-2.5-features.md` —— 大方向对，部分数字是猜的
- ❌ `04-enterprise-edition.md` —— **企业版细节多错**
- ⚠️ `05-coze-loop.md` —— 描述大体对

正确的请直接看 `PLAN.md` + `raw/coze_cn/coze_pro/*.md` 原文。

## `_gaps.md` 状态

之前列的 8 项缺口，**现在 7 项都关闭**（951 页里都有了）。
剩下 1 项（HiAgent vs Coze Pro 私有部署对比）需要走单独商务渠道，不是文档能查的。

## 抓取工具

`tools/` 下：
- `scrape-coze-docs.py` —— 静态 HTML 抓取（GitHub 等用）
- `scrape-coze-docs-rendered.py` —— Playwright 渲染（docs.coze.cn 等 SPA 用）
- `rebuild-index.py` —— 从 .md 文件重建 _index.json

每两周建议跑一次增量更新（resume 模式）：
```bash
python tools/scrape-coze-docs-rendered.py --site coze_cn --resume
git diff docs/coze-knowledge-base/raw/ | head -100
git add . && git commit -m "scrape: weekly update" && git push
```

## 维护规约

- 看到新版本/新功能 → 在对应文件里加一节，**别开新文件**
- 数字过期了 → 划线保留 + 加新数字 + 注明日期
- 引用本目录时写 `docs/coze-knowledge-base/PLAN.md#X` 不要复制粘贴数字到处散
