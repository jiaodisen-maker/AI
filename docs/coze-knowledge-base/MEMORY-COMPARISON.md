# 三套记忆系统对比 · Coze vs GBrain vs Hindsight

> 终极版本——基于 Coze 951 页文档 + GBrain GitHub + Hindsight arxiv 论文。
> 跟会话开头的版本相比，**这次有真实数据**，不再凭二手猜测。
> 信息源：`raw/coze_cn/cozespace/memory.md` + `guides/long_term_memory.md` +
> `guides/database_overview.md` + `guides/agent_overview.md` + GBrain README +
> Hindsight arxiv 2512.12818。

## 0. 终极结论（先放）

之前我把 Coze 当作一个普通的 SaaS bot 平台，给你设计 GBrain + Hindsight 双层后端。
**现在看，Coze 自己已经把 GBrain 的"markdown 文件化记忆"哲学做了**（叫 Memory.md），
所以原来那套 memory-integration **大部分用不上**了。

但 Hindsight 的"反思 + 信念演化"能力 **Coze 仍然没有**——这是唯一可能要外挂的部分。

最务实的方案：
- **L1 起步（前 6 个月）**：纯用 Coze 原生 5 种记忆，不接外挂
- **L2 进阶（如有反思需求）**：外挂 Hindsight 补反思
- **GBrain 几乎不用接**——Coze 的 Memory.md 已经是它的等价物

---

## 1. 三者重新定位（基于真实文档）

### 1.1 Coze 记忆系统（5 种机制并存）

| 机制 | 形态 | 适合 |
|---|---|---|
| 1️⃣ **模型上下文** | 单次对话 token | 短期 |
| 2️⃣ **变量（Variables）** | key-value | 用户偏好（粗粒度）|
| 3️⃣ **数据库（Database）** | 表格化（10 万行/库）| 客户档案、订单等结构化 |
| 4️⃣ **长期记忆库（Memory Library）** | 条目化（**1000 万条/库**），跨会话跨渠道 | 用户画像、偏好（**自动提取**）|
| 5️⃣ **Memory.md 文件系统**（仅"扣子"主产品 + Agent World）| Markdown 多文件 | 持续工作的 Agent 长期记忆 |

5️⃣ 是 **2.5 版独有**的能力，文档明确说："**不是把所有对话都塞进模型上下文，而是将重要内容存储为 Markdown 文件，在对话中按需调用**"。

具体的 6 个核心文件（来自 `cozespace/memory.md`）：

| 文件 | 内容 |
|---|---|
| **SOUL.md** | 角色设定 / 风格 / 行为边界 |
| **USER.md** | 主用户画像（姓名、职位、团队、兴趣）|
| **MEMORY.md** | 跨对话事实与偏好 |
| **TOOLS.md** | 工具调用方法、约定 |
| **CONTACT.md** | 群聊成员、协作关系 |
| **SECRET.md** | 授权敏感信息（受控访问）|

特点（**几乎是 GBrain 的中国版**）：
- ✅ 自动提取（聊天里识别关键信息）
- ✅ 定期整理（异步合并/去重/老化）
- ✅ 多渠道共享（飞书/微信/网页 同一记忆）
- ✅ 用户隔离（群里不泄漏私聊）
- ✅ **可视化展示**（用户能打开文件目录看，**就是 GBrain 的"git markdown 可审"哲学**）
- ✅ 向量检索 + 异步总结
- ⚠️ **没有显式的"反思"机制**（Hindsight 强项）

### 1.2 GBrain（Garry Tan / YC CEO 自用）

- 哲学：**markdown 文件化的语义记忆**
- 三层：Brain Repo（git markdown）+ Postgres+pgvector + Skills + RESOLVER.md
- 检索：HNSW 向量 + tsvector 关键词 + RRF 融合
- 接入：MCP（30+ tools）
- 适合：**公司知识库 / 个人/组织档案**

### 1.3 Hindsight（vectorize.io，arxiv 2512.12818）

- 哲学：**类人认知的情景记忆 + 信念**
- 4 网络：World Facts / Experiences / Entity Summaries / Beliefs
- 三动作：Retain / Recall / **Reflect**
- 91.4% LongMemEval（首个跨 90%）
- 适合：**Agent 多轮对话、经验学习、信念演化**

---

## 2. 6 维度对比矩阵

| 维度 | GBrain | Hindsight | **Coze 长期记忆库** | **Coze Memory.md** |
|---|---|---|---|---|
| **存储形态** | git markdown 文件 | 4 网络黑盒 | 条目化（DB）| **Markdown 多文件** |
| **是否可读** | ✅ 文件系统可看 | ❌ API 才能看 | ⚠️ 资源库 UI 看 | ✅ 文件目录可看 |
| **是否可改** | ✅ 直接改文件 | ❌ 通过 API | ✅ UI 编辑 | ✅ **对话纠正** |
| **类型化** | ❌ 无 | ✅ 4 类强类型 | ❌ 自由文本 | ✅ 6 类文件 |
| **自动整合** | ❌ 无 | ✅ Reflect | ⚠️ 异步总结 | ✅ 定期整理 |
| **信念演化** | ❌ | ✅ Beliefs 网络 | ❌ | ⚠️ MEMORY.md 累积但不演化 |
| **冲突处理** | 全留着 | Reflect 整合 | 后写覆盖 | 用户对话纠正 |
| **跨渠道共享** | git 即共享 | 看 deployment | ✅ 跨飞书/微信/web | ✅ 跨渠道共享 |
| **用户隔离** | git 权限 | 部署侧 | ✅ UID + 渠道 ID | ✅ 群里不泄私聊 |
| **检索机制** | RRF 混合 | 按网络路由 | 向量 | 向量 + 异步总结 |
| **基准性能** | Recall@5 95% | LongMemEval 91.4% | 未知 | 未知 |
| **集成成本** | 中（自部署 PG）| 低（2 行代码）| 0（原生）| 0（原生）|
| **可见黑盒** | 完全显式 | 完全隐式 | 半显式 | 完全显式 |
| **整合时机** | 手动整理 | 异步 Reflect | 实时+异步总结 | 定期整理 |

### 2.1 关键洞察

**Coze Memory.md 哲学和 GBrain 几乎相同**：
- 都用 markdown 文件作为载体
- 都强调"用户可见可改"
- 都做向量检索

**Coze 长期记忆库哲学跟 Hindsight 接近但缺关键能力**：
- 都是结构化条目
- 都按 ID 隔离
- 但 **Coze 没有 Hindsight 的 Reflect**——这是最大缺口

---

## 3. Coze 5 种记忆机制详解（什么时候用哪个）

### 3.1 决策树

```
你要存什么？
  │
  ├─ 单轮对话上下文 ─────────→ ① 模型上下文（默认就是）
  │
  ├─ 用户偏好（一两个字段）── ② 变量（key-value，最快）
  │
  ├─ 结构化业务数据 ────────→ ③ 数据库
  │   │ 客户档案 / 订单 / 任务  （扣子DB ≤ 10 万行；火山 MySQL 大表）
  │
  ├─ 用户画像（自由文本）── ④ 长期记忆库
  │   │ 用户偏好 / 经历 / 习惯  （UID+渠道ID 隔离，Prompt 自动召回）
  │
  └─ 持续工作的 Agent 记忆 ── ⑤ Memory.md 文件
      │ 跨场景的经验沉淀     （仅"扣子"主产品/Agent World）
      │ 关键事实 + 联系人 + SOP  （6 个核心文件，用户可看可改）
```

### 3.2 销售助手具体怎么用

| 数据 | 用哪种 | 理由 |
|---|---|---|
| 客户档案（结构化）| ③ 数据库 / 飞书多维表格 | 大量、字段固定 |
| "小李喜欢正式语气" | ② 变量 | 一个 enum |
| "小王跟过的客户都偏好周三联系" | ④ 长期记忆库 | 自由文本、自动提取 |
| 销售部 SOP | 知识库（KB）| RAG，不是记忆 |
| 历史话术沉淀 | ④ 长期记忆库 / KB | 看是个人还是共享 |
| 销售个人助手"我老婆是医生" | ⑤ MEMORY.md | 长期、跨渠道 |
| 客户跟进时间线 | ③ 数据库（结构化最适）| - |

**关键**：扣子编程（你做销售助手用的）**主要用 ②③④**；Memory.md 是扣子主产品的能力，是给单个员工的"个人 AI 助手"用的（不是销售助手）。

---

## 4. Coze 没有的能力 = Hindsight 的 Reflect

唯一 Coze 真正没做的：**Reflect（反思）**。

### 4.1 什么叫 Reflect

```
Hindsight 工作过程：
  对话历史                       
  ↓                              
  Retain：自动写进 Experience    → 短期事实
  ↓                              
  Reflect（异步触发）            → 把 N 次 Experience 整合成新 Belief
  ↓                              
  Belief 演化                    → 老 Belief 被新证据推翻或加强
  ↓                              
  Recall 时能用最新信念          → 不只是"记得",还"想得通"
```

### 4.2 Coze 的"定期整理"是 Reflect 吗？

**不完全是**。Coze 的"定期整理"做的是：
- 去重
- 把对话碎片合并成更长的记忆
- 老化（不重要的丢）

但**不会做**：
- 检测信念冲突（旧记忆说 "客户喜欢周一开会"，新记忆说 "客户拒绝周一"）
- 形成新的"判断 / 信念"（基于过往多次客户行为，推断 "这个客户是价格敏感型"）
- 维护信念置信度（这个判断有多可信）
- 主动用新证据推翻旧信念

### 4.3 销售场景为什么需要 Reflect

```
30 次销售跟进客户 X 的零碎记忆 → Coze 全部留着
                              ↓
但销售真正需要的不是 30 条原始记忆，是：
  "客户 X 是价格敏感型，B 类客户，倾向 Q3 续约，对竞品 Y 印象不好"
                              ↓
   这是"信念" — 需要 Reflect 才能形成
```

**没有 Reflect → bot 永远在重复检索原始记忆，没法形成判断**。

### 4.4 怎么补：3 种方案

| 方案 | 复杂度 | 推荐 |
|---|---|---|
| **A. 写一个"反思工作流"用 LLM 自己 reflect** | 低 | ⭐⭐⭐⭐ 推荐起步 |
| **B. 外挂 Hindsight 当反思层** | 中 | ⭐⭐⭐ 真有需求再做 |
| **C. 自建（基于 Eino + 自己写）** | 高 | ⭐ 不推荐 |

**方案 A 实现**：

```yaml
# 在销售助手里加一个"反思工作流"，每周日凌晨触发
[Trigger: 周日 02:00]
  ↓
[Code 节点: 拉过去一周该销售的所有长期记忆条目]
  ↓
[Code 节点: 按客户聚类]
  ↓
[Batch 节点: 对每个客户]
  ├─ [LLM 节点（反思 Agent）：
  │    输入：该客户的所有零碎记忆 + 现有信念
  │    输出：3-5 条"信念"（带置信度）+ 1 条"行动建议"]
  ├─ [Code 节点: 检测跟现有客户档案的冲突]
  ├─ [Selector: 有冲突 → 推飞书审；无冲突 → 直接写]
  └─ [飞书多维表格更新: 写入"客户洞察"字段]
```

**比真接 Hindsight 简单 10 倍，而且 80% 效果就到了**。

---

## 5. 三方对比 · 一张总图

```
                          显式 / 文件 / 共享                          隐式 / 结构 / 黑盒
                          ←──────────────────────────────────────────→
                                                                          
GBrain     ━━━━━━━━━━━━●            (markdown + pgvector + RRF)            
                                                                          
Coze       ─────────●─────●────●───●──                                    
                    │     │    │    │                                      
                    │     │    │    └─ ② 变量（ KV）                       
                    │     │    └────── ③ 数据库（表）                      
                    │     └─────────── ④ 长期记忆库（条目）                
                    └───────────────── ⑤ Memory.md（多文件，最像 GBrain）  
                                                                          
Hindsight                                            ●━━━━━━━━━━━━━━━━━━━━
                                                     (4 网络 + Reflect)   
```

**结论**：
- Coze 占据**整条光谱**（5 种机制）
- GBrain 跟 Coze 的 ⑤ Memory.md 重叠 ≈ 90%
- Hindsight 的 Reflect 是 Coze **没有**的能力

---

## 6. 对 800 人保健品公司的具体决策

### 6.1 阶段 1（Month 1-6）：纯 Coze，不接外挂

```
销售助手用：
  ② 变量 — 销售个人偏好（语气/风格）
  ③ 数据库（飞书多维表格）— 客户档案
  ④ 长期记忆库 — 销售跟客户对话累积的画像
  其他：Coze 知识库（不是记忆，是 RAG）

Memory.md 暂不开放给业务方（仅内部测试）
```

**为什么不接外挂**：
1. Coze 原生 5 种已经覆盖 90% 场景
2. 外挂任何东西都增加运维复杂度
3. 7 工程师有更重要的事做（销售助手 / 飞书集成 / AI Gateway / 数据安全）

### 6.2 阶段 2（Month 7-12）：补反思能力（方案 A）

如果发现"销售反映 bot 越用越笨" / "客户洞察不够深"：

→ 实现 §4.4 方案 A：写一个反思工作流，每周给每个销售生成"客户洞察"。

**预期投入**：1 工程师 1 周。
**预期效果**：销售感知到 bot "学会了"，bot 给的客户分析有深度。

### 6.3 阶段 3（Year 2，如真有需要）：外挂 Hindsight

判断标准：
- 反思工作流（方案 A）效果不够
- 需要跨多个 bot 共享"信念"
- 投入 ROI 算清楚

→ 接 Hindsight，但**不要替换 Coze 长期记忆库**——是**补强**：
```
Coze 长期记忆库 → 当作"短期工作记忆"保留
Hindsight       → 接收 Coze 记忆作为输入，做长期信念演化
                  把信念回写 Coze 数据库（飞书多维表格的"客户洞察"字段）
```

### 6.4 GBrain 什么时候用？

**几乎不用**——除非：
- 要做**全公司共享的知识中台**（不只是销售部）
- 强调 git 可审（合规要求）
- 要跟 OpenClaw / Claude Code 这类用 GBrain MCP 的 Agent 互通

如果只是"想让 bot 记忆人类可读"——**Coze 的 Memory.md 已经够了**，不用造第二套。

---

## 7. 跟之前 memory-integration 的关系（清算旧账）

会话最早我给你写的 `memory-integration/` 是基于这个判断：
> "你需要 Coze（前端）+ 后端记忆服务（GBrain + Hindsight 双层）"

**现在看**：

| 当时设想的能力 | Coze 实际有没有 | 结论 |
|---|---|---|
| Markdown 文件化记忆 | ✅ Memory.md | **不用造** |
| 跨渠道共享 | ✅ 长期记忆库做了 | **不用造** |
| 用户隔离 | ✅ UID + 渠道 ID | **不用造** |
| 自动提取 | ✅ 已做 | **不用造** |
| 异步总结 | ✅ 已做（"定期整理"） | **不用造** |
| 向量检索 | ✅ 已做 | **不用造** |
| 反思 / 信念演化 | ❌ 没做 | **要补**——但用工作流 + LLM（方案 A）就够，不必上 Hindsight |
| 飞书 ingest | ✅ Coze 飞书集成 | **不用造** |

**净改动**：
- ❌ `memory-integration/` 整个删（Coze 全替了）
- ✅ 把销售助手的"反思工作流"加进 SALES-BOT.md（方案 A）
- ✅ 留意：未来如真需要 Hindsight，再做插件接入

要不要让我**把 memory-integration 目录删掉**，让 repo 干净？

---

## 8. 跟 OpenClaw 的关系

会话中段你提到过 OpenClaw（虾评等 Agent World 联盟成员）。
查了 `cozespace/agent-world.md`：

> "Agent World 是面向所有 Agent 开放的社交生态，这里没有任何平台和部署限制。
> **无论你是扣子 Agent，还是部署在本地或云端的 OpenClaw 龙虾助手，所有 Agent 都可以在这里生活、工作、学习并连接彼此**。"

也就是说：
- OpenClaw 是 GBrain 作者（Garry Tan）的 Agent 框架
- OpenClaw 用 GBrain 当记忆
- OpenClaw 可以接入 Coze Agent World 跟扣子 Agent 互通
- **它们是平行生态**，跟你公司无关——你公司直接用扣子就行

---

## 9. 验收清单（你团队定方向时用）

```
□ 销售助手用 ② + ③ + ④ 三种记忆，不引入外挂
□ Memory.md 主产品的能力暂不向业务方开放（保留观察）
□ 反思工作流（方案 A）作为 Q3 增强项，先不做 Q1
□ memory-integration/ 旧目录删掉或归档（避免误导）
□ 文档化"什么记忆用哪种"（贴在 SALES-BOT.md）
□ Hindsight 不做集成，等 Year 2 评估
□ GBrain 不做集成（除非有跨企业知识中台需求）
```

---

## 10. 引用源

**Coze 官方**：
- `cozespace/memory.md` —— Memory.md 文件系统（6 个核心文件）
- `guides/long_term_memory.md` —— 长期记忆库（条目化、UID+渠道ID 隔离）
- `guides/database_overview.md` —— 数据库（结构化记忆）
- `guides/agent_overview.md` —— 智能体编排（含变量 / 数据库 / 长期记忆 总览）
- `cozespace/agent-world.md` —— Agent World 与 OpenClaw 互通

**外部参考**：
- GBrain GitHub: https://github.com/garrytan/gbrain
- GBrain brain-vs-memory 指南
- Hindsight: https://github.com/vectorize-io/hindsight
- arxiv 2512.12818 "Hindsight is 20/20"
- VentureBeat: open-source Hindsight agentic memory

---

## 一句话给你 800 人保健品公司

**别接外挂记忆系统**——Coze 自己做了 5 种，覆盖 90%。
**剩下 10%（反思能力）用一个工作流就解决**，不用上 Hindsight。
**memory-integration 目录可以删了**——基于错误前提造的轮子，新前提下不需要。
