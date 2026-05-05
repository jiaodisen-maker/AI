# Ctx2Skill（清华范式）深度研究与中台落地方案

> 项目：保健品行业 AI 中台（Skills 为中心 + 飞书入口 + 私有部署）
> 范式来源：清华大学 Ctx2Skill 工作（2026-05-03 发布的技能生态全栈之一）
> 分支：`claude/ctx2skill-research-DXk65`
> 更新：2026-05-05

---

## 0. TL;DR

**Ctx2Skill 不是写 prompt 的工具，而是让 Agent 在三智能体博弈里"长技能"的训练范式。**

核心一句话：把"人写 SKILL.md"换成"让 Challenger 出题、Reasoner 解题、Judge 判定，Reasoner 在博弈里把策略迭代成一个技能"。

对你这套保健品中台，关键判断是：

> **保健品行业天生有一个"强 Judge"——广告法合规校验和销售转化是可验证的。这意味着 Ctx2Skill 在你这里能跑出比通用领域更好的效果，因为我们不缺判定信号。**

这把之前那份"经验引擎"方案从"被动收集修订"升级为"主动博弈生长"，是工程级别的范式跃迁。

---

## 1. 范式核心：三智能体博弈 + Cross-time Replay

### 1.1 三智能体的分工

```
            ┌──────────────────────────────────┐
            │     Challenger（挑战者）           │
            │  · 生成探测任务                    │
            │  · 目标：找出 Reasoner 的盲区      │
            │  · 自身也学习：失败案例反推出题策略 │
            └──────────────┬───────────────────┘
                           │ task
                           ▼
            ┌──────────────────────────────────┐
            │     Reasoner（解题者）             │
            │  · 解决任务（即"用技能"）           │
            │  · 输入：任务 + 历史 Replay        │
            │  · 输出：解答 + 工具调用轨迹       │
            └──────────────┬───────────────────┘
                           │ output
                           ▼
            ┌──────────────────────────────────┐
            │     Judge（裁判）                  │
            │  · 二元反馈：成功 / 失败           │
            │  · 检查：完成度 + 格式 + 正确性    │
            └──────────────┬───────────────────┘
                           │ binary signal
                           ▼
                  Reasoner 策略更新
                           │
                           ▼
                  成功案例进入 Replay 库
```

**博弈平衡**：Challenger 越强，Reasoner 越要长新技能；Reasoner 越强，Challenger 越要出更难的题。技能边界自动外扩。

### 1.2 Cross-time Replay：防策略坍塌

对抗训练的经典毛病：**学了新的忘了旧的**。
论文实验：不开 Replay，早期技能准确率掉 30%+；开了后保持稳定。

机制：
- 每次训练混合「新任务 + 历史 Replay 任务」
- Replay 权重随时间衰减但**永不归零**
- 成功案例库是 Replay 的素材源

### 1.3 为什么是"二元反馈"
Judge 只给"对/错"，丢失了"错在哪里"的细粒度。
**这是工程权衡**：换取 Judge 极低的实现成本（一条规则、一个校验脚本就能当 Judge），可大规模并发跑。
论文报的成绩：技能覆盖率 68.3% → 89.7%（+21.4%），零标注、零人工介入。

---

## 2. 同日技能生态：五件套拼图

| 工作 | 解决问题 | 含义 |
|---|---|---|
| **Ctx2Skill** | 技能从哪来 | 博弈中"长" |
| **SSL Representation** | 技能怎么存 | 三层结构：Scheduling（调度）+ Structural（执行）+ Logical（动作资源），让技能可搜索/审计/操作 |
| **SkillSynth** | 技能怎么用 | 技能图谱采样过渡节点，Graph → Workflow → Task 显式控制链，合成可执行任务 |
| **D3-Gym** | 技能怎么测 | 可验证训练环境，565 任务覆盖 239 仓库，87.5% 验证准确率 |
| **Skills-Coach** | 技能怎么优 | **Training-Free GRPO**：四模块（Task Gen + Lightweight Opt + Comp Exec + Traceable Eval），不训模型也能优化技能 |

**对企业最关键的是 Skills-Coach**：你不会有自训大模型的算力和数据，但 Training-Free 路线让"博弈优化"也能在你的中台跑起来。

---

## 3. 这套范式与你的中台高度契合的三个原因

### 3.1 你有天然强 Judge
通用 LLM agent 最大的难题是"哪里错了"难自动判定。
你不一样：

| Skill | 天然 Judge |
|---|---|
| 合规文案生成 | **广告法禁词表 + 句式规则**，自动判定，准确率接近 100% |
| 数据查询 | SQL 执行结果可对照真实数据 |
| 转化预测 / 渠道选择 | 实际投放后的 CTR/CVR/ROI |
| 客诉分类 | 升级率、二次投诉率、客户回评 |
| 异常检测 | 后续是否真的发生事件 |

**强 Judge = Ctx2Skill 在你这里能比论文数字跑得更稳**。

### 3.2 你有现成的 Challenger 素材
不缺"出题人"训练数据：
- Coze 上跑过的真实员工请求（含失败案例）
- 客诉记录（典型 + 罕见）
- 历史合规驳回案例
- 竞品突袭场景（新品/促销/新渠道）

把这些喂给 Challenger 模型，它就能学会"出真员工会问的题"。

### 3.3 Skills-Coach 的 Training-Free 路线匹配你的资源边界
保健品公司不会自训 70B 模型。Skills-Coach 的"不训模型只优化技能调用"刚好让 Ctx2Skill 在你这能落地：把"训练 Reasoner 模型"替换为"调整 Reasoner 用的 SKILL.md / references / scripts"。

→ **博弈循环还在，但优化对象从模型权重换成 Skill 工件**。这是企业版 Ctx2Skill 的关键改造。

---

## 4. 工程映射：把博弈装进中台

### 4.1 角色映射

| 论文角色 | 我们中台的实例 |
|---|---|
| **Reasoner** | 实际执行的 Skill（如 `compliance-copywriter`），底层调 Claude/Deepseek/本地 Qwen |
| **Challenger** | 自动出题 Agent，从客诉库/Coze 历史/竞品监控/边缘案例库采样，加扰动生成测试任务 |
| **Judge** | 分层校验栈：① 合规规则引擎（强）② 业务 KPI（中）③ 弱 LLM 自评（兜底） |
| **Replay 库** | ClickHouse 里成功 trace 的索引，按技能、渠道、产品分桶 |
| **优化器** | Skills-Coach 风格的 Training-Free 优化器：改 SKILL.md / references / scripts，不动权重 |

### 4.2 数据流

```
[Coze 历史 + 客诉 + 竞品爬虫 + 失败 trace]
            │
            ▼
        Challenger
        ├─ 任务采样器（覆盖技能空间各维度）
        ├─ 难度调度器（贴 Reasoner 当前边界）
        └─ 去重器（避免与历史任务重复）
            │ task
            ▼
        Reasoner（= 现役 Skill）
            │ output + trace
            ▼
        Judge（分层）
        ├─ L1 规则 Judge：合规、Schema、SQL 正确性  →  二元
        ├─ L2 KPI Judge：影子流量回灌真实 KPI       →  数值（阈值化为二元）
        └─ L3 弱 LLM Judge：仅用于无 L1/L2 信号场景 →  二元
            │ binary
            ▼
    ┌────── 失败 ──────┐    ┌────── 成功 ──────┐
    ▼                  ▼    ▼                  ▼
Challenger 学习      Skill-X 优化器    Replay 库       Pattern 提取
（更新出题策略）     （生成 SKILL.md   （加入索引）    （新增 references）
                      候选改进）
            │
            ▼
        Shadow Eval（D3-Gym 风格）
        ├─ 在固定评测集上跑候选 vX.Y
        ├─ Cross-time Replay：必须在历史任务上不退化
        └─ 通过 → PR → 人审 → 合并
```

### 4.3 工程组件清单

```
.platform/
├── runtime/                       # Reasoner 运行时
│   ├── skill_loader/              # 加载 SKILL.md
│   ├── tool_router/               # 多模型 + MCP 路由
│   └── trace_writer/              # 写 ClickHouse
│
├── challenger/                    # 出题方
│   ├── samplers/
│   │   ├── from_coze_history.py
│   │   ├── from_complaints.py
│   │   ├── from_competitor.py
│   │   └── boundary_explorer.py   # 主动探边
│   ├── policy/                    # 出题策略（可学习）
│   └── deduper/                   # 与历史任务相似度过滤
│
├── judge/                         # 裁判
│   ├── rules/
│   │   ├── ad_law_compliance.py   # 强 Judge
│   │   ├── schema_check.py
│   │   └── sql_correctness.py
│   ├── kpi/
│   │   └── shadow_traffic.py      # KPI 回灌
│   └── llm_fallback/              # 弱 Judge
│
├── replay/                        # Cross-time Replay
│   ├── store/                     # 成功案例索引
│   ├── sampler/                   # 时间衰减但不归零的采样
│   └── coverage_meter/            # 技能空间覆盖度监控
│
├── optimizer/                     # Skills-Coach 风格
│   ├── task_gen/                  # 出题（与 challenger 共用）
│   ├── lightweight_opt/           # 改 SKILL.md / references
│   ├── comp_exec/                 # 候选并行执行
│   └── traceable_eval/            # 可追溯评测
│
├── representation/                # SSL 三层结构
│   ├── scheduling/                # 何时触发：description + paths
│   ├── structural/                # 怎么执行：workflow + tool calls
│   └── logical/                   # 用什么动作资源：scripts + references
│
└── synthesizer/                   # SkillSynth 风格
    ├── skill_graph/               # 技能依赖图谱
    ├── transition_sampler/        # 采样过渡节点
    └── workflow_compiler/         # Graph → 多 Skill 编排
```

### 4.4 SKILL.md 的扩展（在之前 Spec v1 基础上）

```yaml
---
name: compliance-copywriter
description: ...
allowed-tools: ...

# Ctx2Skill 扩展
ctx2skill:
  reasoner-version: v1.3        # 当前服役版本
  challenger:
    sources: [coze-history, complaints, competitor]
    boundary-explore: true       # 是否允许探测边界
  judge:
    primary: rules/ad_law_compliance.py    # 强 Judge
    secondary: kpi/shadow_traffic.py       # KPI Judge
    pass-criteria: "compliance && revision-rounds<2"
  replay:
    bucket-keys: [channel, product-line]   # Replay 分桶维度
    decay: linear-with-floor
    floor-weight: 0.1                      # 永不归零
  optimizer:
    mode: training-free          # Skills-Coach 路线
    targets: [SKILL.md, references/, scripts/]
    forbidden-edits: [allowed-tools, data-scopes, compliance.*]  # 不能自动改安全字段

# SSL 结构化表示
ssl:
  scheduling: { triggers: [...], paths: [...] }
  structural: { workflow: ./workflow.yaml }
  logical:    { scripts: scripts/, refs: references/ }

# SkillSynth 图谱
synth:
  depends-on: [product-info-fetcher]
  composes-into: [new-product-launch-kit, weekly-campaign]
---
```

---

## 5. 路线图（基于范式重写）

### Phase 0｜建立可验证基底（Week 1-2）

**没有强 Judge，Ctx2Skill 不成立。先把 Judge 做厚。**

- [ ] **广告法合规 Judge**：禁词库 + 句式规则 + 已驳回案例库，目标准确率 ≥ 99%
- [ ] **Schema/SQL Judge**：每个数据 Skill 有可验证 schema
- [ ] **影子流量管道**：飞书 Bot 真实请求 → 同时跑现役 + 候选，结果对比但不影响用户
- [ ] **trace store（ClickHouse）+ Replay 索引基础**

**验收**：广告法 Judge 在 1000 条人工标注集上准确率达标，影子流量延迟开销 < 200ms。

### Phase 1｜Reasoner = 一个真 Skill（Week 3-5）

不要试图先把博弈跑起来。**先把一个 Skill 做到能服役。**

- [ ] 选 `compliance-copywriter` 作为首发 Reasoner
- [ ] 起初 Challenger = 真实员工 + Coze 历史回放（不是博弈，是流量）
- [ ] Judge 接通三层（规则 → KPI → 弱 LLM）
- [ ] Replay 库开始累积成功案例

**验收**：3 名内测员工 2 周，合规通过率 ≥ 96%，修订轮次中位数 ≤ 2。

### Phase 2｜Challenger 上线（Week 5-8）

- [ ] **Sampler 接入**：客诉库、竞品监控、Coze 失败历史
- [ ] **Boundary Explorer**：每周扫一次 Reasoner 已通过任务的"邻域"，生成扰动版本
- [ ] **Dedup**：embedding 相似度 + 任务结构哈希，避免重复
- [ ] Challenger 输出先**不直接训 Reasoner**，先开 PR 让人看："这是 Challenger 认为 Reasoner 会失败的 50 个任务"——快速建立信任

**验收**：人审命中率（Reasoner 真失败 / Challenger 预测失败）≥ 60%。低于此值说明 Challenger 噪声太大。

### Phase 3｜Skills-Coach 优化器闭环（Week 8-12）

- [ ] **Lightweight Opt**：失败聚类 → LLM 提议 SKILL.md/references 修改 → 候选 v候选 N 个
- [ ] **Comp Exec**：N 个候选并行跑同一 task 集
- [ ] **Cross-time Replay 评测**：候选必须在历史成功任务上不退化（误退化率 < 2%）
- [ ] **Traceable Eval**：每次改进都能回答"这次改了什么、解决了哪类失败、引入了什么风险"

**前 3 个月只开 PR，不自动合并**。建立人对系统的信任。

**验收**：8 周后 `compliance-copywriter` 经历 ≥ 3 次自动 PR，KPI 单调改进。

### Phase 4｜SSL + SkillSynth（Week 12+）

- [ ] 把现役 Skill 全部改写成 SSL 三层结构（用 `${CLAUDE_SKILL_DIR}` + `references/` + `scripts/` 自然落地）
- [ ] 起 Skill 图谱：依赖关系 + 过渡节点
- [ ] 第一个组合任务："新品上市营销 kit" = 卖点提炼 → 多平台文案 → 合规审核 → ROI 预测
- [ ] SkillSynth 用图谱合成员工没问过的组合任务，丢给 Challenger 当种子

### Phase 5｜更多 Skill + 更厚 Judge（持续）

每加一个新 Skill 重复 Phase 1-3。Judge 越厚，新 Skill 越快进入博弈循环。

---

## 6. 关键决策点

### 6.1 不要追求"零人工"
论文里 zero supervision 是研究指标。生产环境前 6 个月**必须人审 PR**。系统稳定后再讨论自动合并范围（先合并 references 类小改，再考虑 SKILL.md 主体）。

### 6.2 Judge 严禁用单个 LLM 自评
弱 LLM 自评是兜底，不是主裁。所有写动作类、合规类 Skill 必须有规则 Judge。**没有强 Judge 的 Skill 不进入博弈循环，回退为人工修订模式。**

### 6.3 Cross-time Replay 的衰减下限不能为 0
论文实验已经证明，Replay 权重归零会在数月后引发"忘了广告法 2020 版"这种问题。**地板权重 ≥ 0.05**。

### 6.4 Challenger 的"挑战难度"必须可调
难度过高 → Reasoner 全错 → 学习信号噪声大；难度过低 → 没新技能可长。
建议用**目标成功率 50-70%** 作为难度调度器目标（论文 sweet spot）。

### 6.5 Training-Free vs 微调
默认 Training-Free（Skills-Coach 路线）。
仅当某个 Skill 经历 10+ 次优化仍卡瓶颈时，才考虑收集对应数据微调一个本地小模型作为该 Skill 专用 Reasoner。

### 6.6 二元反馈的信息丢失怎么补
论文承认这是权衡。我们的补法：
- Judge 必须**附带 reason code**（例如 `FAIL/AD_LAW/FORBIDDEN_WORD/治疗`）
- 失败聚类用 reason code 作主键，让 Optimizer 看到"错在哪类"，而不只是"错了"

---

## 7. 风险与对策

| 风险 | 对策 |
|---|---|
| Challenger 出题崩坏（生成无意义任务） | Dedup + 可解性预筛（先让强模型解一遍，能解才入库） |
| Judge 假阳/假阴 | 每月红队抽审 200 条 Judge 判定，错误率 > 3% 触发 Judge 升级 |
| 策略坍塌（论文已识别） | Cross-time Replay + 每周强制跑 v1.0 旧任务集，回归测试 |
| 自动 PR 引入隐性 regression | Shadow Eval + KPI 单调性约束，KPI 任意维度退化超 5% 自动 reject |
| 计算成本翻倍（三智能体并发） | Challenger 异步离线跑（每天一批），Reasoner 实时，Judge 一半规则一半 LLM |
| 监管/审计要求 | SSL 三层结构 + 完整 trace 存档 365 天 + 每次自动 PR 留 CHANGELOG |
| 飞书/扣子环境变化 | 飞书层只做触发/通知，Skill 工件与平台解耦（之前 office-hours 的判断仍成立） |

---

## 8. 第一个里程碑（21 天）

把"博弈最小闭环"装到 `compliance-copywriter` 上。

| 周 | 交付 |
|---|---|
| W1 | 广告法 Judge（规则版）准确率 ≥ 99% on 1000 条标注集；trace store 起跑 |
| W1 | `compliance-copywriter` v1.0 上线，3 名员工内测 |
| W2 | Replay 库累积 ≥ 200 条成功案例；Challenger 接通 Coze 历史回放 |
| W2 | Boundary Explorer 跑首轮，产出 50 条 Challenger 任务，人审命中率统计 |
| W3 | Skills-Coach 优化器跑首轮：5 个候选 SKILL.md 并行评测 |
| W3 | 生成第一个自动 PR `v1.0 → v1.1`，人审通过后合并 |

**成功标准**：员工说"它的合规判断我相信"，且能看到 v1.0 → v1.1 的具体改进点（从失败聚类反推）。

---

## 9. 与之前 office-hours 设计的差异（迭代说明）

| 之前方案 | 现在（基于清华 Ctx2Skill） |
|---|---|
| 经验引擎 = 收集修订 → 改 SKILL.md | 三智能体博弈：Challenger 主动出题，不等真实员工出错 |
| 人工分析失败模式 | Skills-Coach 自动聚类 + 候选并行评测 |
| 担心策略坍塌靠人工回归 | Cross-time Replay 工程化保证 |
| Skill 是平铺的 SKILL.md | SSL 三层（调度/执行/资源）+ SkillSynth 图谱组合 |
| 飞书 + Web 双入口 | 不变 |
| 飞书入口策略 | 不变（短结果飞书，长结果 Web） |
| 私有部署、多模型路由 | 不变 |

**核心升级**：从"被动收集真实失败"升级为"主动博弈探边"。前者天花板是真实流量覆盖度；后者天花板是 Challenger 想象力。

---

## 10. 接下来的具体动作（建议）

二选一，本周内启动其中一个：

- **A. 立刻开 Phase 0 的 Judge**（推荐）：广告法合规 Judge 是整套范式的基石。先把它做到 ≥99% 准确率，整个博弈循环才有意义。这件事 1-2 周可见结果，且即使 Ctx2Skill 范式变了，Judge 本身也不浪费。
- **B. 先做 Phase 1 的 Reasoner**：直接把 `compliance-copywriter` v1.0 上线，等真实流量反馈再回头补 Judge。落地更快但不解决根本问题。

**强烈推荐 A**——Ctx2Skill 在你这能赢的核心理由就是"强 Judge"，这是护城河，不是配套。

要我现在就开始动 A 的具体实现（建广告法 Judge 的项目骨架 + 禁词库 + 规则模板）吗？

---

## 参考与说明

清华 Ctx2Skill 及同日工作（SSL / SkillSynth / D3-Gym / Skills-Coach）的具体引用按用户提供的描述记录。本文档中的实验数字（68.3% → 89.7% 等）以及 arXiv 编号引自原始论述，未独立复核——上线前建议读原文 confirm。

相关业内对照：
- [stevesolun/ctx — 实时 Skill 推荐引擎（与"长技能"思路互补，可作为 Skill 选择层）](https://github.com/stevesolun/ctx)
- [anthropics/skills/skill-creator — 单 Skill 萃取与 eval](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [Trace2Skill (arxiv 2603.25158) — 从执行轨迹蒸馏可迁移技能](https://arxiv.org/abs/2603.25158)
- [Meta Context Engineering via Agentic Skill Evolution (2601.21557)](https://arxiv.org/abs/2601.21557)

仓库内：`gstack，我想像的AI中台...md`（office-hours 产品方向）。
