# ctx2skill 深度研究与落地方案

> 适用项目：保健品行业企业 AI 中台（Skills 为中心 + 飞书入口 + 私有部署）
> 研究分支：`claude/ctx2skill-research-DXk65`
> 更新日期：2026-05-05

---

## 0. TL;DR

**ctx2skill = 把"上下文（对话、工作流、老员工经验、运行日志）"系统性地萃取并固化为可复用 Skill 的工程方法论。**

它不是一个工具，而是一条流水线：

```
原始上下文 ──▶ 萃取 ──▶ 草稿 SKILL.md ──▶ 评测 ──▶ 迭代 ──▶ 上线 ──▶ 运行回流 ──▶ 自动改进
   (聊天/SOP/Excel/客诉)         (skill-creator)   (evals.json)         (经验引擎)
```

对你的中台而言，ctx2skill 解决的是**"把扣子上跑通的 prompt 经验沉淀为企业级、可审计、可进化的 Skill"**这个具体问题——这正是扣子的四堵墙之外，护城河的来源。

---

## 1. 概念溯源：业内"context → skill"的两条主线

业内目前有两个被叫做"ctx → skill"的不同事物，理解差异很重要：

### 1.1 `anthropics/skill-creator`（官方·权威）
**定位**：通过对话萃取 SKILL.md 的元 Skill。
**核心流程**（精炼自官方 SKILL.md）：

1. **EXTRACT**：先从当前对话历史里抓取——用户用过哪些工具、走过哪些步骤、做过哪些更正、输入输出格式、示例文件
2. **INTERVIEW**：再追问——触发场景、输出格式、边界条件、是否需要 evals
3. **WRITE**：产出 `SKILL.md` + 可选的 `scripts/` `references/` `assets/`，遵守渐进式披露（metadata <100 词、body <500 行、其余按需）
4. **EVAL**：起 with-skill / without-skill 两组并行子代理，写入 `evals/evals.json`、`grading.json`、`benchmark.json`
5. **ITERATE**：基于 `feedback.json` 改进，泛化而非过拟合
6. **OPTIMIZE DESCRIPTION**：用 60/40 train/test 跑 trigger eval，自动优化 description（决定 Skill 是否被路由）

四个 sub-agent：Executor / Grader / Comparator / Analyzer。

### 1.2 `stevesolun/ctx`（社区·实时推荐）
**定位**：实时 Skill/Agent/MCP 推荐引擎，挂在 Claude Code 的 `PostToolUse` + `Stop` hook 上。
**规模**：102k 节点 / 2.9M 边的知识图谱（91k skills + 464 agents + 10k MCP）。
**算法**：基于语义相似 + tag + slug + 来源重叠 + 质量分 + 使用模式的多信号打分，向当前任务推 top-K bundle。

### 1.3 我们要做的 ctx2skill ≠ 任一方
两者都是参考。我们要做的是**企业语境下的 ctx2skill**：

| 维度 | skill-creator | ctx | 我们的 ctx2skill |
|---|---|---|---|
| 输入 | 单次对话 | 当前 IDE 操作 | 飞书对话 + Coze 历史 + 客诉记录 + Excel SOP + 老员工访谈 |
| 输出 | 一个 SKILL.md | 推荐列表 | 带合规护栏 + 数据查询 + 经验回流的企业 Skill |
| 评测 | evals.json | 无 | evals + 真实业务 KPI（修改轮次、合规通过率、ROI） |
| 迭代 | 人工 review | 无 | 经验引擎自动 PR |

---

## 2. Skill 引擎核心机制（理解这些再设计才不会跑偏）

### 2.1 Skill 的本质
Skill 不是外部代码，是**按需注入大脑的高阶提示词**。命中后整段 SKILL.md 进入上下文并停留整个会话；Claude Code 不会重读，所以"全程要遵守的规则"必须写成常驻指令而非一次性步骤。

### 2.2 渐进式披露（Progressive Disclosure）
- **永驻 context**：所有 Skill 的 name + description（约 1536 字符上限）
- **触发后注入**：SKILL.md body
- **按需读取**：`references/*.md`、`scripts/*`、`assets/*`

含义：description 是路由的唯一钥匙；body 写工作流；细节文档放 references，让 Claude 用工具去读。

### 2.3 Frontmatter 关键字段（我们会扩展）

| 字段 | 用途 | 我们的扩展 |
|---|---|---|
| `description` | 触发路由 | 必须包含触发短语 |
| `allowed-tools` | 免确认工具 | 配合企业权限白名单 |
| `disable-model-invocation` | 禁止 LLM 自动调用（写动作类） | 部署/发布类必开 |
| `context: fork` + `agent` | 子代理隔离运行 | 长流程 skill 必开 |
| `paths` | 仅在匹配文件时激活 | 渠道目录隔离 |
| `hooks` | Skill 生命周期钩子 | 接入审计/合规拦截 |
| **新增 `compliance`** | 合规域 | `health-supplement` 等 |
| **新增 `data-scopes`** | 数据访问范围 | `mysql:orders.*` |
| **新增 `experience-id`** | 经验引擎绑定 | 用于回流和自动改进 |
| **新增 `kpi`** | 成功度量 | `revision-rounds<2` |

### 2.4 动态上下文注入
``!`gh pr diff` ``、``!`mysql -e "..."`` 在 Skill 渲染时执行，结果替换占位符。这是实现"Skill 自带数据查询"的关键——Skill 触发即查询，Claude 看到的是结果。

### 2.5 Fork Context vs Inline
- **Inline**：参考资料类（"API 规范"），合并进主对话
- **Fork**：动作类、长流程、需要隔离干扰的（"生成合规文案"），跑在子代理里，主对话只看摘要

我们的中台 Skill **大部分应当 fork**——主对话短，权限清晰，可审计。

---

## 3. ctx2skill 工程方法论（你这套中台需要的）

### 3.1 上下文来源分级

```
L0  原始信号（高噪声）
    ├── 飞书对话日志
    ├── Coze 已有 workflow 导出
    ├── 客诉/工单文本
    └── Excel SOP / Word 规范

L1  半结构化（人工标注后）
    ├── "老员工访谈"（1 小时 / 角色）
    ├── 修订对（before/after 文案）
    └── 失败案例集

L2  结构化（可直接喂 skill-creator）
    ├── 任务模板
    ├── 输入/输出 schema
    └── 边界条件清单

L3  Skill（产物）
    └── SKILL.md + references + scripts + evals
```

### 3.2 四种萃取模式

| 模式 | 适用 | 主导者 | 工具 |
|---|---|---|---|
| **A. 对话萃取** | "把刚才聊的变成 skill" | LLM | 改造版 skill-creator |
| **B. SOP 反向工程** | 已有 Word/PDF 规范 | LLM + 人 | RAG → 草稿 → 人审 |
| **C. 修订对学习** | 有 N 份"AI 初稿 vs 人工终稿" | LLM | diff 萃取 + pattern 归纳 |
| **D. 老员工访谈** | 经验在脑子里 | 人 | 结构化访谈模板 |

四种模式都收敛到同一个产物格式（见 §4），这是关键。

### 3.3 评测：业务 KPI 而非 LLM 自评

skill-creator 的 evals 适合做"功能正确性"，但你的中台要测的是**业务有效性**：

| Skill 类型 | 评测指标 |
|---|---|
| 合规文案生成 | 合规通过率（自动）、修改轮次（人工标注）、转化率（A/B） |
| 数据查询 | SQL 正确率、Top-K hit、首响应延迟 |
| 异常检测 | 召回率、误报率、首次有效告警时长 |
| 客诉处理 | 一次解决率、升级率、用户满意度 |

**实操**：每个 Skill 配两套 eval：一套技术 eval（写在 `evals/evals.json`），一套业务 eval（写在 `evals/business.json`，从生产日志抽样）。

### 3.4 经验引擎闭环（你的真正护城河）

```
Skill 运行
   │
   ├──▶ 输入/输出/工具调用 → 写入 trace store (ClickHouse)
   ├──▶ 人工修正（飞书"重做"按钮 / Web UI 编辑）→ 写入 corrections
   └──▶ 业务结果回灌（转化率/合规审核结果）→ 写入 outcomes
                              │
                              ▼
              每周/触发式 自动改进 Job
                              │
       ┌──────────────────────┼─────────────────────┐
       ▼                      ▼                     ▼
   pattern 提取           description 调优        references 增补
   （差异聚类）          （trigger eval loop）   （新案例进库）
       │                      │                     │
       └──────────────────────┴─────────────────────┘
                              │
                              ▼
                  生成 PR：skill-vX.Y.Z
                              │
                              ▼
                 影子运行（shadow eval）→ 通过则自动合并
```

这一段是 skill-creator **没有**的，是企业 Skill 工程的真正核心。

---

## 4. 我们的 Skill 标准（Spec v1）

```yaml
---
# 官方字段
name: compliance-copywriter
description: |
  生成保健品营销文案，自带广告法合规校验和渠道适配。
  使用场景：用户在飞书或 Web 提到"写文案/详情页/小红书/抖音种草/产品卖点提炼"，
  即使未明确说"合规"也应触发。
allowed-tools:
  - Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/check_compliance.py *)
  - mcp__product_db__query
context: fork
agent: copywriter-agent
disable-model-invocation: false

# 企业扩展字段
spec-version: "1.0"
owner: content-ops@company
compliance:
  domain: health-supplement
  rule-set: ${COMPLIANCE_RULES_PATH}/ad-law-2024.json
  blocking: true
data-scopes:
  - mysql:products.basic_info
  - milvus:past-copies
  - oss:assets/templates
experience-id: copy-v3
kpi:
  revision-rounds: "<2"
  compliance-pass-rate: ">0.98"
audit:
  log-level: full
  retention-days: 365
hooks:
  pre-run: ${CLAUDE_SKILL_DIR}/hooks/auth.sh
  post-run: ${CLAUDE_SKILL_DIR}/hooks/log_to_clickhouse.sh
---

## 角色
你是一名资深保健品文案，熟悉广告法和小红书/抖音/京东详情页的不同语言风格。

## 输入
- 产品 ID：$0
- 渠道：$1（小红书 | 抖音 | 公众号 | 京东详情页）
- 卖点偏好（可选）：$ARGUMENTS[2:]

## 工作流
1. 查产品基础信息：!`python3 ${CLAUDE_SKILL_DIR}/scripts/fetch_product.py $0`
2. 查同类历史最佳文案：从 milvus:past-copies 取 top 3
3. 按渠道模板生成 3 版草稿
4. 自动跑合规校验：!`python3 ${CLAUDE_SKILL_DIR}/scripts/check_compliance.py`
5. 输出：3 版草稿 + 合规报告 + 修改建议

## 渠道写作要点
- 小红书：见 [references/xiaohongshu.md](references/xiaohongshu.md)
- 抖音：见 [references/douyin.md](references/douyin.md)
...

## 不允许的表达
见 [references/forbidden-words.md](references/forbidden-words.md)

## 失败案例（学习用）
见 [references/past-mistakes.md](references/past-mistakes.md)
```

**目录结构**：

```
.skills/compliance-copywriter/
├── SKILL.md
├── scripts/
│   ├── fetch_product.py
│   └── check_compliance.py
├── references/
│   ├── xiaohongshu.md
│   ├── douyin.md
│   ├── forbidden-words.md  ← 自动从合规库同步
│   └── past-mistakes.md    ← 经验引擎回灌
├── evals/
│   ├── evals.json          ← 技术 eval
│   ├── business.json       ← 业务 eval
│   └── trigger.json        ← description 触发 eval
├── hooks/
│   ├── auth.sh
│   └── log_to_clickhouse.sh
└── CHANGELOG.md            ← 经验引擎自动 PR 留痕
```

---

## 5. 落地方案：四阶段路线图

### Phase 0｜规范与脚手架（Week 1-2）

**目标**：定义 Skill Spec v1 + 跑通最小工具链，为后续所有 skill 立标准。

**交付物**：
- [ ] `spec/skill-spec-v1.md`：上面 §4 那份规范，加 schema 校验
- [ ] `tools/skill-lint`：CLI，校验 SKILL.md 是否合规
- [ ] `tools/skill-scaffold`：`skill-scaffold new compliance-copywriter` 一键起目录
- [ ] `runtime/`：基于 Claude Agent SDK 的最小执行器，能加载本地 Skill 跑通
- [ ] CI：PR 必跑 skill-lint + 影子 eval

**验收**：手写 1 个最简单 Skill（如 `/today-sales` 自然语言查昨日销售），从飞书发起到回执 < 10s。

---

### Phase 1｜ctx2skill 萃取流水线（Week 3-6）

**目标**：建立从原始上下文到 Skill 草稿的工程通路。

**子模块**：

#### 1.1 改造版 skill-creator（基于官方 fork）
- 输入接口扩展：飞书会话 ID、Coze workflow JSON、SOP 文档路径、修订对 zip
- 输出接口对齐：直接产 §4 的目录结构（带企业字段）
- 内置访谈模板：4 模式（A/B/C/D）各一套问卷

#### 1.2 老员工访谈工坊
- 1 小时结构化访谈剧本（产品经理设计，AI 主持）
- 录音 → 转写 → 自动萃取候选 Skill 列表 → 人工排序

#### 1.3 Coze 迁移器
- 把扣子的 workflow JSON 翻译成 SKILL.md 草稿
- 资产（知识库、提示词模板）落到 `references/`

#### 1.4 修订对学习器
- 接入飞书云文档/Office 修订历史
- 用 diff + LLM 聚类提取 pattern → 写入 `references/past-mistakes.md`

**验收**：把扣子上 3 个跑通的 skill（合规文案、产品卖点提炼、客诉分类）迁移到自建运行时，人工修订量 ≤ 2 轮。

---

### Phase 2｜运行时 + 经验引擎（Week 5-10，与 Phase 1 并行）

**目标**：让 Skill 不只能跑，还能"自己进化"。

**核心组件**：

#### 2.1 执行运行时（Skill Runtime）
- 基于 Claude Agent SDK，本地部署
- 多模型路由（vLLM 本地 / Claude / Deepseek）：简单走本地、合规走微调、复杂走海外
- 权限+审计层：每次调用记 (user, skill, inputs, tools, outputs, kpis)
- 沙箱：所有 Bash/SQL/HTTP 走白名单 MCP，不裸跑

#### 2.2 Trace Store
- ClickHouse：trace 表（高写入）、corrections 表、outcomes 表
- 每条 trace ≥ 7 天热数据，全量冷归档到 OSS

#### 2.3 经验引擎（自动改进 Job）
按 §3.4 的闭环，每周跑：
- **Pattern Mining**：对每个 Skill 的 corrections 做 diff 聚类
- **Description Loop**：用 trigger.json 跑 `run_loop.py`（移植自 skill-creator）优化 description
- **References Updater**：新增的好案例 → references；新发现的雷区 → forbidden-words
- **Shadow Eval**：候选 vX.Y → 在影子流量上跑，KPI 不退化才发 PR

#### 2.4 Skill 推荐器（借鉴 stevesolun/ctx）
- 当用户在飞书发模糊请求 → 推荐 top-3 候选 skill 让用户选
- 当 ops 在 Web 工作台时 → 监听上下文（当前打开的产品、当前渠道）→ 主动推荐

**验收**：上线 8 周后，1 个 skill（合规文案）在零人工干预下从 v1.0 → v1.3，合规通过率从 92% → 98%，修改轮次从 2.4 → 1.3。

---

### Phase 3｜入口与编排（Week 8-12）

**目标**：把 Skill 暴露给非技术员工。

#### 3.1 飞书 Bot
- @机器人 → 意图识别 → Skill 路由 → 结果回卡片
- 简单结果（短文本）直出；长结果（多版文案、数据表）发 Web UI 链接
- "重做"按钮 → 触发 corrections 回流
- 定时巡逻任务推送（异常检测、竞品变化）

#### 3.2 Web 工作台
- Skill 市场（按部门/角色分类）
- 单 Skill 工作面板（输入区、多版输出对比、修订记录、合规报告）
- 经验引擎可视化（每个 skill 的版本历史 + KPI 趋势）
- skill-creator 入口（PM/资深员工创建新 skill）

#### 3.3 编排（多 Skill 组合）
- 复杂任务（"上市新品的全套营销 kit"）= skill 编排：
  `产品卖点提炼` → `多平台文案生成` → `合规审核` → `投放 ROI 预测`
- 用 fork-context 跑每一步，主代理只做 orchestration

**验收**：3 个角色（运营、文案、产品）各 5 个真实员工内测 2 周，DAU > 60%，NPS > 30。

---

### Phase 4｜规模化与护城河（Week 12+）

- **Skill 市场治理**：版本、deprecation、依赖关系、权限审计
- **跨 Skill 知识迁移**：文案 skill 的合规知识 → 客诉 skill 的回复合规
- **主动巡逻**：定时 Skill 扫描数据/竞品 → 发现机会主动推送
- **多租户/SaaS**：把"以 skill 为中心的中台"产品化卖给同类企业

---

## 6. 关键决策点（必须先想清楚再写代码）

### 6.1 Skill 粒度
**原则**：一个 Skill 解决一个完整业务动作，而不是一个 prompt 模板。
反例：`/improve-text`（太宽）；正例：`/xiaohongshu-product-launch`（具体场景）。

### 6.2 Description 的可观测性
描述错了，全盘错了。建议：
- 每个 Skill 上线必须有 ≥20 条 trigger eval（10 触发 + 10 非触发）
- 真实流量里的 misroute 比例必须 < 5%

### 6.3 安全边界
- 写动作类（部署、发消息、改库存） → `disable-model-invocation: true`
- 涉敏数据 → `data-scopes` 强制白名单 + Hook 审批

### 6.4 经验引擎不要"自动合并"过早
前 3 个月，自动改进只能开 PR，**人工 review** 才能合并。建立信任后再开自动合并。

### 6.5 飞书 vs Web 双入口策略
你已经决定了——飞书做触发/通知，Web 做工作台。Skill 设计时把"短结果路径"和"长结果路径"分开。

---

## 7. 风险与对策

| 风险 | 对策 |
|---|---|
| Skill 数量爆炸（500+ 后无人维护） | 推荐器（§2.4）+ 强制 owner 字段 + 90 天无调用自动归档 |
| description 互相打架（多个 skill 都被触发） | 触发评测必跑 + 优先级字段 + 同义 skill 强制合并 |
| 合规误判（漏过禁词或过度阻断） | 双层校验：Skill 内合规 + 网关层合规；每月红队测试 |
| 经验引擎过拟合到少量样本 | 60/40 train/test 强制分割（沿用 skill-creator）+ shadow eval |
| 老员工不愿"教 AI" | 经验引擎可视化把功劳归到提供修订的人；季度积分激励 |
| 海外模型断供 | LiteLLM 抽象层 + 关键 skill 本地微调降级路径 |
| 数据出域 | 全程私有部署 + Skill 内禁外网 + 出口 DLP |

---

## 8. 第一个里程碑（建议 14 天内可见）

**单 Skill 端到端样板：`/compliance-copywriter`**

- Day 1-2：写 Spec v1，搭脚手架
- Day 3-5：访谈 1 名资深文案 + Coze 迁移，产 SKILL.md v0.1
- Day 6-8：写 evals（技术 + 业务 + 触发），跑 skill-creator 改进至 v0.3
- Day 9-10：接飞书 Bot + Web 工作台 MVP
- Day 11-12：3 名内测员工真实使用 + 收 corrections
- Day 13-14：经验引擎跑首轮，产 v0.4，做 demo

**成功标准**：内测员工说"比扣子上那个好用，且我相信它的合规判断"。

---

## 9. 与现有资产的衔接

- **gstack**：把 gstack 的 skill 设计哲学（带 checklist、质量门禁、多步审查）作为本 Spec 的基线参考。可考虑用 gstack 的 sandbox 做我们 Web 工作台 QA 自测。
- **office-hours 设计文档**：`~/.gstack/projects/jiaodisen-maker-AI/20260410-design-ai-zhongtai.md` 是产品方向源；本文档是工程实现源；两者一致。
- **扣子（Coze）**：Phase 1.3 完成后，扣子作为"草稿场"——新想法先在扣子 PoC，验证后用迁移器转成正式 Skill。

---

## 10. 接下来一步（建议）

二选一：

- **A. 立刻动手**：从 Phase 0 开始，先把 Spec v1 + skill-lint + scaffold 做出来（约 3 天人时），有了脚手架后所有 skill 都按这条流水线走。
- **B. 先单点突破**：跳过 Phase 0 的工程基础，直接做 §8 那个 14 天里程碑，跑通一个完整闭环再回头补规范。

**推荐 B**——你已经被扣子验证过需求，现在最缺的是"自建一条端到端 demo 给老板/团队看"。规范在第一个 skill 跑通后会自然涌现，比凭空设计准。

---

## 参考来源

- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
- [anthropics/skills - skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [Improving skill-creator: Test, measure, and refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)
- [stevesolun/ctx — real-time skill recommendation engine](https://github.com/stevesolun/ctx)
- [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- [Agent Skills 第一性原理深度解析](https://academy.claude-code.club/practical-skills/claude-skills/skills-first-principles)
- 仓库内：`gstack，我想像的AI中台...md`（产品愿景与 office-hours 记录）
