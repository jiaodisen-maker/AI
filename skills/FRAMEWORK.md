# 国内电商运营 Skills 框架

> 把国内电商运营的工作全部 skill 化 — 为保健品 AI 中台准备的能力清单与执行规范。

## 设计原则

1. **每个 skill = 一个明确的工作动作**，颗粒度到「进 X 后台 → 拉 X 报表 → 调 X 参数 → 输出 X 文档」
2. **每个 skill 必须可由 AI 独立或半独立完成**（人类只在关键节点审批）
3. **每个内容类 skill 自带合规过滤器**（保健品广告法、平台行业规则）
4. **每个数据类 skill 自带异常检测分支**（不只是被动出报表）
5. **每个 skill 携带经验沉淀槽位**（input → ai_output → human_edited → diff → pattern → 下次自动注入）

## 12 大领域

| # | 领域 | 中文 | Skill 数 | 主要痛点 |
|---|------|------|---------|---------|
| 01 | shelf-commerce | 货架电商运营 | 28 | 多平台多店，重复操作 |
| 02 | content-commerce | 内容/兴趣电商 | 26 | 内容生产+合规审核 |
| 03 | private-domain | 私域运营 | 25 | 1v1 触达、SOP 管理 |
| 04 | paid-ads | 付费投放 | 22 | 多平台账户、实时调控 |
| 05 | live-commerce | 直播带货 | 22 | 自播+达播、复盘 |
| 06 | data-analytics | 数据分析 | 24 | 跨平台数据整合 |
| 07 | crm | CRM/会员运营 | 12 | 用户分层、自动化触达 |
| 08 | customer-service | 客服运营 | 14 | 售前售后、合规话术 |
| 09 | supply-chain | 供应链/库存 | 14 | 批次效期、安全库存 |
| 10 | finance | 财务/对账 | 10 | 多平台账单、达人佣金 |
| 11 | compliance | 合规（保健品） | 12 | 广告法、蓝帽子、平台规则 |
| 12 | product-selection | 选品/竞品/新品 | 14 | 决策依据、市场扫描 |

合计 **223 个 skill**（不含 alias / 子工作流）。

## Skill 文件规范 (frontmatter)

每个 SKILL.md 顶部必须有 YAML frontmatter：

```yaml
---
name: <kebab-case-name>          # 唯一标识，全公司无重名
domain: 01-shelf-commerce        # 12 大领域之一
platform: tmall|jd|pdd|...|all   # 适用平台
role: 运营|内容|投手|客服|...     # 主要执行人角色
frequency: daily|weekly|...      # 调用频次
inputs:                          # 输入清单
  - 店铺ID
  - 时间范围
outputs:                         # 输出清单
  - 日检报告.md
human_review_required: true      # 是否需要人工最终审核（合规/财务类必须 true）
compliance_filter: true          # 是否走广告法过滤器（内容类必须 true）
data_sources:                    # 数据来源
  - 生意参谋
  - 抖店罗盘
allowed-tools:                   # Claude Code 可调工具（如挂入 .claude/skills）
  - Bash
  - WebFetch
  - Write
---
```

## 三种运行时形态

每个 skill 可以以三种形态被调用，**SKILL.md 是统一的入口**：

| 形态 | 触发方 | 实现 |
|------|-------|------|
| Claude Code skill | 开发者 / Claude | `.claude/skills/<name>/SKILL.md` |
| 飞书 Bot 命令 | 员工对话 | Bot 路由到 Agent SDK + skill 注册表 |
| 定时巡逻任务 | 调度器 | cron 触发 → Agent SDK → 多 skill 编排 |

## 经验引擎接入点

每次 skill 执行：
```
record_execution(skill_name, inputs, ai_output, human_edited_output, timestamp, user_id)
```

定期任务：
```
extract_patterns(skill_name, lookback_days=30) → update_skill_prompt(skill_name)
```

## 保健品行业贯穿要点

所有内容/客服/直播 skill 都必须挂以下三类过滤器：

1. **极限词**: 最 / 第一 / 国家级 / 100% / 顶级 / 唯一 / 王牌 / 绝对 ...
2. **医疗功效词**: 治疗 / 治愈 / 根治 / 速效 / 抗癌 / 降三高 / 防 XX 病 / 替代药品 ...
3. **必带声明**: 「保健食品不能代替药物治疗疾病」+ 蓝帽子 logo + 广告批文号

参考：`11-compliance/forbidden-word-scan/SKILL.md`

## 目录树速览

```
skills/
├── FRAMEWORK.md          ← 你正在看的这个
├── INDEX.md              ← 全部 223 个 skill 索引（带描述）
├── README.md             ← 项目说明
├── 01-shelf-commerce/    ← 28 skills
├── 02-content-commerce/  ← 26 skills
├── 03-private-domain/    ← 25 skills
├── 04-paid-ads/          ← 22 skills
├── 05-live-commerce/     ← 22 skills
├── 06-data-analytics/    ← 24 skills
├── 07-crm/               ← 12 skills
├── 08-customer-service/  ← 14 skills
├── 09-supply-chain/      ← 14 skills
├── 10-finance/           ← 10 skills
├── 11-compliance/        ← 12 skills
└── 12-product-selection/ ← 14 skills
```
