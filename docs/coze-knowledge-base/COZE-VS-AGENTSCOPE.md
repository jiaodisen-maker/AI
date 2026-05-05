# Coze vs AgentScope + HiClaw + HiMarket · 全栈对比

> 字节系 vs 阿里系，两大平行 AI Agent 生态对比。
> 对你 800 人保健品公司的实际决策建议在 §6。

## 0. TL;DR

| 维度 | Coze（字节）| AgentScope + HiClaw + HiMarket（阿里）|
|---|---|---|
| **形态** | SaaS 主 + 开源 Studio 弱 | **全开源** Apache 2.0 |
| **定位** | "**普通员工拖拽搭 bot**" | "**工程师写代码做 Agent 团队**" |
| **目标用户** | 业务方 + 开发者 + 个人 | **开发者主导** |
| **多 Agent 哲学** | 单 bot 内部多 Agent + 关键词跳转 | **多个独立 Agent + Matrix 房间协作** |
| **人机协作** | 卡片 + 飞书消息 | **共享 Matrix 房间，人能实时介入** |
| **上手难度** | 低（UI 拖拽）| 中-高（写代码 + 框架）|
| **企业级特性** | SSO、VPC、KMS、审计齐全 | 自部署，自己实现 |
| **学习曲线** | 1 天上手 | 1 周上手 |
| **生态完整度** | 大而全 | 工程化深，运营弱 |
| **适合 800 人推广** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **适合工程团队主导** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**对你 800 人保健品公司：用 Coze 做主力，AgentScope 备选/补充**——具体策略在 §6。

---

## 1. 两个生态的全景

### 1.1 字节 · Coze 生态（4 件套）

```
扣子（Coze）              主产品（Agent World、云电脑/手机/邮箱、记忆）
扣子编程（Coze Programming）开发者平台（低代码项目）
Coze Loop                 评测+观测+提示词管理（Apache 2.0 开源）
扣子罗盘                  提示词智能优化
Coze Studio（开源）        自部署版本（功能少）
Eino                      编排引擎（开源，CloudWeGo）
```

### 1.2 阿里 · AgentScope 生态（4 件套）

```
AgentScope                多 Agent 框架（核心）
HiClaw                    多 Agent 协作 OS（Matrix 协议）
CoPaw                     轻量 Agent runtime（本地模型支持）
HiMarket                  AI 应用市场（Agent / MCP / Model）
Higress                   AI 网关（之前我推荐 LiteLLM 的国产替代）
```

> 历史脉络：HiClaw 和 CoPaw 都是从独立项目**并入 AgentScope** 的，现在是阿里 AgentScope 生态的一部分。

### 1.3 一对一映射

| Coze 组件 | 阿里 AgentScope 对应 | 备注 |
|---|---|---|
| Coze 企业旗舰版（SaaS）| ❌ 没直接对应 | **阿里没全 SaaS 形态**，得自部署 |
| Coze Studio（开源）| AgentScope 框架 | 阿里这边更完整 |
| Coze Programming | AgentScope + HiClaw 应用层 | |
| 多 Agent 模式（关键词跳转）| **HiClaw Manager-Workers** | 阿里更精细 |
| Skill 商店 | **HiMarket** | |
| Coze Loop（评测）| AgentScope 评测组件 | Coze 这边更成熟 |
| 扣子罗盘（prompt 优化）| AgentScope ReAct + 自我反思 | |
| Eino（编排引擎）| AgentScope 核心 | |
| **Agent World** | **❌ 没有** | 这是 Coze 独家 |
| Skills 沙箱 | CoPaw 本地 runtime | |
| 飞书集成 | ❌ 自己接 | |
| AI 网关 | **Higress** | 阿里这边内置，Coze 要自建 |

**关键差距**：
- ❌ AgentScope 生态**没有** Agent World（云电脑/云手机/邮箱）
- ❌ AgentScope 生态**没有**飞书原生集成
- ❌ AgentScope 生态**没有** SaaS 选项（一定要自部署）
- ✅ AgentScope 生态**有** Higress AI 网关（Coze 这边要自建 LiteLLM）
- ✅ AgentScope 生态**Matrix 协议**做协作更前卫

---

## 2. 12 维度对比表

| 维度 | Coze | AgentScope+HiClaw+HiMarket |
|---|---|---|
| **开源协议** | Coze Studio Apache 2.0；SaaS 闭源 | Apache 2.0 全开源 |
| **形态** | SaaS（企业旗舰主推）+ 弱开源 | **纯自部署** |
| **价格** | ¥5,980+ / 月（800 人 ≈ ¥61K）| **0 软件费 + 自部署成本（¥3-10K/月运维）** |
| **多 Agent 模型** | 单 bot 内部 Agent 跳转 | Manager-Workers 多 Agent 团队 |
| **协作机制** | 工作流 jump conditions | **Matrix 房间共享对话** |
| **人在回路** | bot 卡片 + 飞书消息 | **人和 Agent 在同房间，人能实时介入/审批** |
| **国内合规** | ✅ 字节生态 + 火山方舟 | ✅ 阿里云生态 |
| **国际化** | coze.com（海外版独立）| 一套适配 |
| **可视化拖拽** | ✅ 强（FlowGram）| ⚠️ 弱（主要写代码）|
| **运营/业务方友好** | ✅ 业务方能自己做 bot | ❌ 必须工程师 |
| **企业级特性** | SSO/VPC/KMS/审计齐全 | 自部署，得自己做 |
| **生态成熟度** | 客户案例 50+ / Skill 商店活跃 | 工程社区活跃，企业落地少 |

---

## 3. 多 Agent 协作哲学的关键差异

### 3.1 Coze 的"单 bot 多 Agent"

```
[销售助手 bot]
   │
   ├── router Agent（路由）
   ├── customer_analyst Agent
   ├── script_coach Agent
   ├── ops_assistant Agent
   └── compliance_guard Agent
```

- 都在**同一个 bot 实例**里
- 通过 **jump conditions（关键词）** 切换
- 状态（记忆/上下文）共享
- 用户感知是"一个 bot"

**适合**：相对收敛的业务场景（销售助手、客服）。

### 3.2 HiClaw 的"多 Agent + Matrix 房间"

```
       Matrix 房间："产品发布筹备"
          │
   ┌──────┼──────┬──────┬──────┐
   │      │      │      │      │
  人 1  Manager Worker1 Worker2 Worker3
                  ↓      ↓      ↓
              市场分析  写文案  做海报
              Agent     Agent  Agent
```

- 每个 Agent 是**独立的 Matrix 用户**
- 在**共享房间**里对话
- **人**也在房间里，看到所有 Agent 间消息
- Manager 负责**调度** Workers
- Workers 可以是**不同 runtime**（OpenClaw / QwenPaw / Hermes）混用
- 人**随时介入**：拒绝、修改、加新指令

**适合**：长任务（项目、研究、复杂创作）+ 强调透明性 + 多团队协作。

### 3.3 哪个更适合销售场景

**销售助手 → Coze**：
- 销售要快速回答（< 2s），单 bot 即可
- 业务相对收敛（查档案、给话术）
- 不需要多 Agent 长时间协作

**项目协作 / 复杂研究 → HiClaw**：
- 涉及多人多 Agent 长时间协作
- 需要透明度（每步都能看到）
- 需要人随时介入

---

## 4. 优劣势对比

### 4.1 Coze 优势

```
✅ SaaS 即开即用，业务方能自己做 bot
✅ Agent World（云电脑/手机/邮箱）是独家
✅ 飞书 / 微信 / 抖音 渠道集成最强
✅ 客户案例丰富（保健品行业有山西联康参考）
✅ Skill 商店生态活跃
✅ 评测平台 Coze Loop 成熟
```

### 4.2 Coze 劣势

```
❌ SaaS 数据权交字节（合规审视点）
❌ 闭源核心，自部署版本（Coze Studio）功能少
❌ 推广全员要花真金白银（800 人 ¥61K/月）
❌ 多 Agent 协作较弱（关键词跳转 vs 房间协作）
❌ 第三方模型接入要自建网关
```

### 4.3 AgentScope 生态优势

```
✅ 全开源 Apache 2.0，数据 100% 自有
✅ Matrix 协议做 Agent 协作前卫且优雅
✅ Higress AI 网关原生集成（不用自建 LiteLLM）
✅ HiMarket 让 Agent 资产化
✅ 工程师能完全控制行为
✅ 软件费 ¥0
```

### 4.4 AgentScope 生态劣势

```
❌ 必须工程师，业务方不会用
❌ 没有飞书原生集成（自己接）
❌ 没有 Agent World（云电脑/手机/邮箱）
❌ 推广全员难度高（无 SaaS UI）
❌ 客户案例少，企业落地资源弱
❌ Coze Loop 这种成熟评测平台暂缺
❌ 自部署运维成本高
```

---

## 5. 国内合规对比

| | Coze | AgentScope |
|---|---|---|
| 数据存放 | 字节服务器（VPC 可选）| **你公司服务器** |
| 监管对接 | 字节做 | 自己做 |
| 等保 2.0 | 字节有 ISO/等保 | 自己跑等保 |
| PIPL 合规 | 共担 | 完全你担 |
| 数据出境 | 默认境内（火山）| 完全可控 |
| 灵活度 | 低（受 SaaS 约束）| 高（任意定制）|

**保健品行业（合规敏感）**：
- 客户健康问题不进任何系统 → 两家都满足（前提是你的 prompt + 过滤层做对）
- 客户姓名/电话 → Coze 走 PIIBlocker（自建网关）；AgentScope 完全你控制
- 监管审计 → AgentScope 自部署能完全自定义日志

---

## 6. 对你 800 人保健品公司的具体决策

### 6.1 推荐主战略：**Coze 主力 + AgentScope 备选**

**理由**：
1. 你目标是**全公司 800 人推广**——业务方要能自己用，**Coze SaaS 这点完胜**
2. 你已经付了 Coze 企业旗舰版钱
3. 你已用飞书——Coze 飞书集成原生支持
4. 你 7 工程师——足够用 Coze 扩展（自建插件 + Bridge + Gateway）

### 6.2 什么场景应该用 AgentScope（而非 Coze）

| 场景 | 用 AgentScope 的理由 |
|---|---|
| **真正敏感数据**（处方/病历）| 完全自部署，数据不出公司 |
| **多 Agent 长时间协作**（项目 / 研究）| Matrix 房间 + 人在回路更优 |
| **某个高级团队独立做 Agent 工程化** | 让他们用框架，不挤占 Coze 推广资源 |
| **未来想做对外 AI 产品** | AgentScope 自部署给客户更自由 |

### 6.3 三层架构建议（混用方案）

```
                  全公司 800 人主入口
                         │
                ┌────────▼────────┐
                │  飞书（统一入口） │
                └────────┬────────┘
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
   日常 bot         深度协作场景        敏感数据场景
  （销售/客服/HR）   （项目/研究）      （健康咨询/合同）
       │                 │                 │
       ▼                 ▼                 ▼
   Coze 企业旗舰    HiClaw（自部署）   AgentScope（自部署）
   覆盖 95% 场景     覆盖 4% 场景        覆盖 1% 场景
       │                 │                 │
       └─────────────────┴─────────────────┘
                         │
                         ▼
                   公司内部系统
                  （CRM/HR/SQL/...）
```

**资源分配**：
- 6 工程师做 Coze 扩展（CRM 插件 / Bridge / Gateway）
- **1 工程师专门探索 HiClaw + AgentScope**（用于敏感场景 PoC）

### 6.4 不该用 AgentScope 的场景

```
❌ 销售助手日常对话         → Coze 最优
❌ 飞书入口                 → Coze 原生
❌ 业务方自助做 bot         → AgentScope 业务方不会用
❌ 全员推广                 → AgentScope 无 SaaS UI
❌ 想用 Agent World         → AgentScope 没这能力
```

### 6.5 跟我之前的方案是否冲突

**不冲突**。我之前的方案核心是 Coze SaaS + 自建扩展。
现在加一个补充：**1 名工程师跟踪 AgentScope 生态**，准备好"逃生通道"或"高级场景补充"。

---

## 7. 替换风险评估

### 7.1 如果某天想**全切 AgentScope**

| 工作 | 难度 | 工程量 |
|---|---|---|
| 重做 Bridge → AgentScope 事件驱动 | 中 | 1 周 |
| 重做 CRM 插件（OpenAPI 标准）| 低 | 1 天 |
| 重做 AI Gateway（用 Higress 替换 LiteLLM）| 中 | 1 周 |
| 重新培训业务方 | **高** | **失败概率大** |
| 重做飞书集成（无原生）| 中 | 1 周 |
| 重做评测体系 | 中 | 1-2 周 |
| 业务连续性中断成本 | 高 | 推广可能倒退 3 个月 |

**结论**：**切换成本高，但你已经做的工程化准备不会浪费**——OpenAPI 插件、自建 Gateway 都能继续用。

### 7.2 反过来：如果阿里 AgentScope 出了 SaaS 杀手版

未来 1-2 年有可能。届时再评估。**现在不必赌**。

---

## 8. 不同公司的选择参考

| 公司类型 | 推荐 |
|---|---|
| 800 人保健品（你）| **Coze 主 + AgentScope 1 人探索** |
| 大厂 / 互联网 / 工程师占比 50%+ | **AgentScope 自部署主** |
| 50 人内创业公司 | **Coze 个人版/团队版即可** |
| 银行 / 金融 / 极敏感数据 | **AgentScope 完全自部署** |
| 医疗 / 药品（强监管）| **AgentScope** + 自部署模型 |
| 教育 / 培训 / 内容创作 | **Coze**（Skill 商店 + 视频 Agent 强）|
| 抖音电商 / 私域营销 | **Coze**（飞书+抖音渠道）|
| 跨国企业 | **Coze.com**（海外版）/ AgentScope |

---

## 9. 一句话总结

**Coze 是"AI 平民版"——业务方能用；AgentScope 是"AI 工程版"——工程师能控**。

你 800 人保健品公司，目标是**全员推广**——选 Coze 是对的。
但保留 1 个工程师跟踪 AgentScope 生态，作为**备选 + 高级场景补充**——这是聪明的。

---

## 10. 引用源

- HiClaw GitHub: https://github.com/agentscope-ai/HiClaw
- HiClaw 加入 AgentScope 公告: https://www.alibabacloud.com/blog/hiclaw-joins-agentscope-partnering-with-copaw-to-build-multi-agent-infrastructure_603006
- HiMarket 介绍: https://higress.cn/en/ai/himarket/himarket-introduction/
- HiMarket 升级公告（阿里云）: https://www.cnblogs.com/alisystemsoftware/p/19363664
- AgentScope 文档: https://github.com/modelscope/agentscope
- Higress AI 网关: https://higress.cn/
- 2026 Claw 生态对比（博客园）: https://www.cnblogs.com/aigclabs/p/19685517/claw-ai-agent-2026-guide

本目录其他相关：
- `PLAN.md` —— Coze 主战略
- `SAAS-VS-SELFBUILD.md` —— SaaS 边界讨论
- `MODELS.md` —— AI Gateway 选型（Higress 是 LiteLLM 的国产替代）
- `MEMORY-COMPARISON.md` —— Coze 记忆系统跟其他三方对比
