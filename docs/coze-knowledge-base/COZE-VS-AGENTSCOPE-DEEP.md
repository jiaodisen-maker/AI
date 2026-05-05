# Coze vs AgentScope+HiClaw+HiMarket · 技术深度对比

> 比 `COZE-VS-AGENTSCOPE.md` 深 3 倍。包括协议级架构、代码级实现、保健品行业实际场景对比、工程师语言偏好、长期战略风险。

## 0. 5 个之前没讲透的关键洞察

### ① 编排引擎的语言之争（**Go vs Python**）
- **Eino**（Coze 后台）= **Go**：强类型、编译检查、高性能、协程并发
- **AgentScope** = **Python**：动态类型、REPL 友好、AI 工程师默认语言
- **影响**：你 7 工程师是 Java/Python 背景？AgentScope 上手快；是 Go 背景？Eino 更顺
- **大部分国内 AI 工程师不会 Go** —— 这是个**隐藏决策点**

### ② "Multi-Agent" 在两边是**完全不同的东西**
- Coze 的"多 Agent 模式" = 一个 bot 内部多个 prompt 块通过关键词跳转
- HiClaw 的"多 Agent" = 多个**独立进程的 Agent** 在 Matrix 房间通过协议消息协作
- 量级差距：Coze 的多 Agent 是"同一个 bot 不同人格"；HiClaw 是"多个 bot 组成团队"

### ③ Matrix 协议的**深远影响**
- HiClaw 用 Matrix 不是噱头——Matrix 是去中心化通讯协议
- 实际意义：Agent 协作日志**完全 git 友好**（Matrix room 历史可导出）、可联邦化、可审计
- 但代价：每个 Agent 是独立 Matrix 用户 = 成本和复杂度都增加

### ④ 字节 vs 阿里的**长期战略博弈**
- 字节：消费级 + Skill 商店生态（学校/培训/电商方向）
- 阿里：企业云 + 工程化（金融/制造/政务方向）
- 你保健品公司在哪边？**消费品 + B2C** → 字节生态更对口

### ⑤ 真正的**护城河**对比
- Coze 的护城河 = **业务方能用 + 飞书原生 + Agent World**
- AgentScope 的护城河 = **代码可见 + 自部署 + 不锁死**
- 你是 800 人公司——业务方友好 = 关键护城河

---

## 1. 协议级架构对比

### 1.1 Coze（Eino 引擎）的工作流执行模型

```
[Workflow 编辑器 UI]
        ↓
   生成 DAG（图）
   节点 = ChatModel / Tool / Retriever / ChatTemplate
   边 = field mapping（A.output.foo → B.input.bar）
        ↓
   Eino Graph runtime（Go）
        ↓
   Goroutine pool 并发执行节点
        ↓
   流式 streaming pipeline
```

**关键属性**：
- 编译时类型检查 → 上线前节点连不上会报错
- field mapping → 显式声明哪个字段流向哪个节点
- 流式优先 → LLM token 一吐出来下游就开跑
- 三种编排模式：**Chain**（线性）/ **Graph**（图）/ **Workflow**（带 field mapping 的 DAG）
- ADK（Agent Development Kit）支持中断/恢复（人在回路）

### 1.2 AgentScope 的执行模型

```
[Python 代码]
        ↓
   定义 Agent 类（继承 AgentBase）
   每个 Agent 有：
     - reply(msg: Message) → Message
     - memory: ShortTermMemory + LongTermMemory
     - toolkit: 注册的工具集
   消息驱动：Agent A → Message → Agent B
        ↓
   asyncio 异步执行
        ↓
   Pipeline / ReAct / Custom workflow
```

**核心抽象**（`arxiv.org/html/2508.16279v1`）：
- **Messages**：基本数据单元，含 sender/role/content（含多模态 + tool usage blocks）/metadata/UUID/timestamp
- **ChatModel**：统一 LLM 接口（formatter / async call / 统一 schema / usage tracking / hook）
- **Memory**：volatile + persistent（LongTermMemoryBase）
- **Toolkit**：本地工具 + 远程（MCP）工具，分组分发

### 1.3 HiClaw 的协作模型（**最有意思的设计**）

```
                 Matrix 房间："产品发布筹备"
                 （Tuwunel 自托管 Matrix server）
                              │
        ┌────────────┬────────┴────────┬─────────────┐
        ▼            ▼                 ▼             ▼
       人 1         Manager           Worker 1      Worker 2
       (运营)       Agent             (OpenClaw)    (QwenPaw)
                    │
                    ↓ 调度
                    Workers 收到 task：
                      - "去做 X"
                      - "完成后发到房间"
                    │
                    ↓
                    Worker 执行（用 token 调 Higress AI Gateway）
                    │
                    ↓ 把进度/结果发回房间
                    所有人能看到 Worker 的每一步
```

**协议级特性**：
- Matrix 是**端到端加密**协议（默认）
- 消息**有顺序保证**（Matrix room state）
- **去中心化**——可以联邦化跨企业（理论上）
- **Worker 凭据隔离**：Workers 只有 consumer token，**真凭据（API key、PAT）留在 Higress 网关**
- **Manager-Workers 解耦**：Workers 可以是不同 runtime（OpenClaw / QwenPaw / Hermes / 自定义）混用

### 1.4 三种执行模型的影响

| 维度 | Coze（Eino DAG）| AgentScope（消息驱动）| HiClaw（Matrix 房间）|
|---|---|---|---|
| **同步/异步** | 流式同步（链）| 异步消息 | 异步消息 |
| **状态共享** | 工作流变量 | Agent 自己的 memory | 房间状态 |
| **协调粒度** | 细（节点级）| 中（Agent 级）| 粗（房间级）|
| **可观察** | 节点 trace | Agent 日志 | **房间历史 = 完整审计** |
| **人介入** | 工作流暂停节点 | 自定义 Agent | **人就在房间里，自然介入** |
| **去中心化** | ❌ 集中调度 | 部分（Agent 独立）| **✅ Matrix 联邦** |
| **多语言混用** | Go 一种 | Python 一种 | **任意（Matrix 用户即可）** |

**HiClaw 最大的卖点**：人和 Agent 平等，房间历史就是审计。
**Coze 最大的卖点**：业务方拖拽就能搭，不用写代码。
**AgentScope 最大的卖点**：Python 工程师能自然写。

---

## 2. 代码级对比：同一个"销售助手"在三边怎么实现

场景：用户问"查一下张三客户档案" → bot 调 CRM → 返回脱敏档案 + 风险分析

### 2.1 Coze 实现（**~0 行代码 + UI 拖拽**）

```yaml
# 在 Coze UI 里配（导出的 yaml 大致这样）
workflow:
  name: customer_analysis
  nodes:
    - id: start
      type: start
      next: extract_customer

    - id: extract_customer       # LLM 节点：抽取客户名
      type: llm
      prompt: 从用户消息里抽客户名或 ID
      model: deepseek-v3
      next: search

    - id: search                  # 调 CRM 插件
      type: plugin
      plugin: crm.search_customers
      input:
        keyword: "{{ extract_customer.output }}"
        salesperson_id: "{{ context.user_id }}"
      next: analyze

    - id: analyze                 # LLM 节点：基于档案出分析
      type: llm
      prompt_template: |
        基于以下客户档案出 3 亮点 + 2 风险 + 1 建议:
        {{ search.output }}
      model: deepseek-v3
      next: compliance

    - id: compliance              # 合规审核
      type: llm
      prompt: 检查输出是否含禁词
      model: doubao-1.6
      next: end

    - id: end
      type: end
```

**实际工作量**：1 业务 + 1 工程师拖拽 **2 小时**搞定。

### 2.2 AgentScope 实现（Python ~150 行）

```python
# customer_assistant.py
from agentscope.agents import AgentBase, ReActAgent
from agentscope.message import Message
from agentscope.models import OllamaChatModel, OpenAIChatModelConfig
from agentscope.service import ServiceToolkit
from agentscope.memory import TemporaryMemory
import httpx

# ----- 1. 定义工具 -----
async def search_customers(keyword: str, salesperson_id: str) -> dict:
    """从公司 CRM 搜客户。"""
    async with httpx.AsyncClient() as cli:
        r = await cli.get(
            "https://crm-api.your-company.com/customers/search",
            params={"keyword": keyword, "salesperson_id": salesperson_id},
            headers={"Authorization": f"Bearer {os.getenv('CRM_TOKEN')}"})
    return r.json()

# ----- 2. 注册工具 -----
toolkit = ServiceToolkit()
toolkit.add(search_customers)

# ----- 3. 创建 Agent -----
class SalesAgent(ReActAgent):
    def __init__(self, salesperson_id: str):
        super().__init__(
            name="sales_assistant",
            sys_prompt=open("prompts/customer_analyst.md").read(),
            model_config_name="deepseek-v3",
            tools=toolkit.json_schemas,
            memory=TemporaryMemory(),
        )
        self.salesperson_id = salesperson_id

    async def reply(self, msg: Message) -> Message:
        # 注入 salesperson_id 到上下文
        msg.metadata["salesperson_id"] = self.salesperson_id
        return await super().reply(msg)

# ----- 4. 合规审核 Agent -----
class ComplianceAgent(AgentBase):
    sys_prompt = open("prompts/compliance.md").read()

    async def reply(self, msg: Message) -> Message:
        verdict = await self.model(
            messages=[{"role": "system", "content": self.sys_prompt},
                       {"role": "user", "content": f"审核：{msg.content}"}])
        if "BLOCK" in verdict:
            return Message(role="assistant", content="本回答涉及合规风险，已拦截")
        return msg

# ----- 5. 编排 Pipeline -----
async def run(user_msg: str, salesperson_id: str) -> str:
    sales = SalesAgent(salesperson_id)
    compliance = ComplianceAgent(name="compliance")

    msg = Message(role="user", content=user_msg)
    sales_reply = await sales.reply(msg)
    final = await compliance.reply(sales_reply)
    return final.content


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(run("查一下张总客户", salesperson_id="wang_xx")))
```

**实际工作量**：1 工程师 **0.5-1 天**写 + 调试。
**优势**：完全可控、可单元测试、git 化。
**劣势**：业务方看不懂、改不了。

### 2.3 HiClaw 实现（**Matrix 房间 + Manager-Workers**）

```python
# 配置 hiclaw.yaml
manager:
  agent_runtime: copaw
  prompt: |
    你是销售部门的协调员。客户分析任务你拆解给 Workers。

workers:
  - id: customer_lookup_worker
    runtime: openclaw
    tools: [crm_search, crm_get_customer]
    prompt: 你专门查客户档案

  - id: analysis_worker
    runtime: qwenpaw
    tools: []
    prompt: 你基于档案做客户洞察分析

  - id: compliance_worker
    runtime: copaw
    tools: []
    prompt: 你做合规审核

room:
  name: "销售助手协作室"
  participants_join_url: https://matrix.your-company.com/rooms/sales-room
```

```python
# 业务代码（极简）
import hiclaw

async def query(user_msg: str, salesperson_id: str):
    # 进入销售协作室
    room = await hiclaw.join_room("销售助手协作室",
                                    user=salesperson_id)
    # 发任务给 Manager
    await room.send(f"@manager 查 {user_msg}")
    # 等 Manager 协调 + Workers 完成 + Compliance 审核
    final_msg = await room.wait_for(filter="from=compliance")
    return final_msg.content
```

**特别之处**：
- **运营/销售可以加入这个 Matrix 房间，看着 Agent 协作**——人随时打断/纠正
- 所有协作记录是 Matrix 房间历史（git 化导出）
- 不同 Worker 跑不同 runtime，可换可加

**实际工作量**：1 工程师 **2-3 天**搭 + 调试（学习 Matrix 协议有曲线）。

### 2.4 同一场景三边对比

| 维度 | Coze | AgentScope | HiClaw |
|---|---|---|---|
| **代码量** | 0（YAML 拖拽）| ~150 行 Python | ~30 行 Python + Matrix 房间 |
| **开发时间** | 2 小时 | 0.5-1 天 | 2-3 天 |
| **业务方能改？** | ✅ | ❌ | ❌ |
| **可单元测试？** | ❌（要在 Coze 里跑）| ✅ | ⚠️ 难（要 Matrix mock）|
| **可 git 化？** | ⚠️ Coze YAML 可 export 但不爽 | ✅ | ✅ |
| **可观察？** | Coze Loop | 自己埋点 | **Matrix 房间历史** |
| **跨语言？** | Go only | Python only | **任意（Matrix 协议）** |
| **流式？** | ✅ 原生 | ✅ asyncio | ⚠️ Matrix 不优化流式 |
| **人介入？** | 工作流暂停 + 卡片 | 自己实现 | **天然——人在房间里** |

---

## 3. 保健品行业 5 个核心场景对比

### 3.1 场景 A：销售对话（"小张这个客户怎么样"）

| | Coze | AgentScope | HiClaw |
|---|---|---|---|
| 用什么 | bot 工作流 + 多 Agent 模式 | ReActAgent + tools | Manager + 1 Worker |
| 实现复杂度 | 低 | 中 | 中 |
| 飞书入口 | ✅ 原生 | 自己接 | 自己接 |
| 响应延迟 | < 2s | < 3s | > 5s（Matrix overhead）|
| 推荐度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

### 3.2 场景 B：销售经理审核话术（人在回路）

| | Coze | AgentScope | HiClaw |
|---|---|---|---|
| 实现 | 工作流人审节点 + 飞书审批 | 自定义 Agent + 等待用户输入 | **Matrix 房间——经理就在群里** |
| 透明度 | 中（要看 Trace）| 中 | **高（房间历史完全透明）** |
| 推荐度 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

### 3.3 场景 C：合规审核（每条对外消息）

| | Coze | AgentScope | HiClaw |
|---|---|---|---|
| 实现 | 工作流 LLM 节点 + 自定义模型 | ComplianceAgent | Compliance Worker |
| 拦截可见性 | Coze Loop trace | 日志 | **房间消息（人随时看）** |
| 性能 | 多 Agent 并行 | 串行（除非自己异步）| 串行（Matrix 顺序）|
| 推荐度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

### 3.4 场景 D：长期项目跟进（一个客户跟 6 个月）

| | Coze | AgentScope | HiClaw |
|---|---|---|---|
| 状态保持 | 长期记忆库 + Memory.md | LongTermMemoryBase | 房间历史 + Worker 自记忆 |
| 多人协同 | 飞书群+bot | Pipeline | **多 Worker + 人** |
| 推荐度 | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

### 3.5 场景 E：保健品广告法合规（27 项功能 + 禁词）

| | Coze | AgentScope | HiClaw |
|---|---|---|---|
| 词库管理 | KB 文档 + Coze 内容安全策略 | Python 字典 | Higress 网关层 |
| 实时拦截 | 工作流节点 | Agent 链 | Manager 拦截 + Worker 内拦截 |
| 审计 | Coze Loop | 自己埋 | Matrix 房间 |
| 全员推广护栏 | ✅ 默认所有 bot | 自己实现 | 自己实现 |
| 推荐度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

### 3.6 综合得分（保健品 800 人场景）

| | Coze | AgentScope | HiClaw |
|---|---|---|---|
| 5 场景平均 | **4.0** | 3.0 | 3.6 |
| 业务方友好 | **5.0** | 1.0 | 1.5 |
| 工程化深度 | 3.5 | 5.0 | **5.0** |
| **总分** | **4.2** | 3.0 | 3.4 |

---

## 4. 隐藏成本深度分析

### 4.1 Coze 的隐藏成本

```
表面：¥61K/月（800 席）
+ 模型 token 费：¥3-10K/月
+ 自建扩展（CRM/Bridge/Gateway）：¥800-3,000/月基础设施
+ 工程人力（7 人 × 摊销 30%）：~¥30K/月
+ 推广运营（培训/案例/激励）：¥5-10K/月
─────────
真实成本：≈ ¥100-115K/月（约 ¥130/人/月）

锁定风险：
- 数据在字节
- 业务方依赖 Coze UI（迁移培训成本极高）
- Coze API 变更需追随（年度 1-2 次）
- Coze 不再支持你需要的功能 → 怎么办？
```

### 4.2 AgentScope 的隐藏成本

```
表面：¥0 软件费
+ 自部署运维：¥5-15K/月（含 K8s + 监控 + 备份 + 多模型）
+ 模型成本：跟 Coze 类似
+ 工程人力（更多）：7 人 × 摊销 50%（要全自己写）≈ ¥50K/月
+ 业务方培训成本：极高（业务方根本不会用）→ 必须靠工程师代做
+ 飞书集成自建：¥5K/月维护
+ 推广困难：自部署 → 业务方接受度低
─────────
真实成本：≈ ¥80-100K/月（约 ¥100-125/人/月）

锁定风险：
- 框架社区驱动 → 关键 bug 没人修就难
- 国内企业落地案例少 → 招人难
- 自部署所有问题都是你的问题
```

### 4.3 真相

**两边总成本接近**——Coze 砍了人力但加了软件费，AgentScope 反过来。

**关键差异**在**风险类型**：
- Coze 风险 = **厂商风险**（字节政策 / 涨价 / 技术路线变）
- AgentScope 风险 = **运维风险**（你公司自己扛）

---

## 5. 长期战略风险

### 5.1 字节 Coze 的战略

```
2024-2025：争夺 AI 应用层（跟阿里通义、百度文心心战）
2025-2026：Skill 商店变现（个人版 + 企业版双引擎）
2026-2027：Agent World 生态扩张（云电脑/手机/邮箱差异化）
未来：与 OpenAI / Claude 海外巨头错位竞争
```

风险：
- 字节会不会把 Coze 卖掉/拆分？（参考 TikTok）
- 涨价？（字节有国内云成本压力）
- 政策变化（国家对大模型企业牌照管制）

### 5.2 阿里 AgentScope 的战略

```
2024-2025：开源框架占心智（争夺开发者）
2025-2026：HiAgent 企业版变现 + 阿里云捆绑
2025-2026：HiMarket 商店生态
未来：跟 Coze 形成"开源 vs SaaS"长期对垒
```

风险：
- 阿里 AI 战略反复（LLM/Qwen/通义/AgentScope 多线）
- 开源社区持续投入？
- HiAgent 商业化进度（企业不愿付费）

### 5.3 双押注策略（**推荐**）

```
70%   投入 Coze（主战略）
20%   保留 AgentScope 探索（1 工程师持续跟踪）
10%   关注 OpenAI/Claude 国际方案（合规允许时）
```

**关键原则**：
- 你的**插件 (OpenAPI 3.0)** 任何平台都能用 → 不浪费
- 你的**AI Gateway** 任何平台都能用 → 不浪费
- 你的**业务方培训成本**只对 Coze 投资 → 锁定 Coze
- 决定切换的真正成本是**业务方培训**，不是技术

---

## 6. 工程团队语言/技能匹配度

### 6.1 你 7 工程师可能的背景

```
情况 A：Java/Python 主，少量 Go
  → AgentScope 无缝，Eino/Coze Studio 自部署有学习成本
  → 推荐：Coze SaaS + 不碰 Coze Studio

情况 B：Python AI 工程师为主
  → AgentScope 完美匹配，Coze SaaS 也能用
  → 推荐：Coze SaaS 主 + 1 人探 AgentScope

情况 C：Go + 后端工程师
  → Eino 直接友好，AgentScope 学习成本中
  → 推荐：可考虑 Coze Studio 自部署 + Eino 二开

情况 D：全栈/前端为主
  → Coze SaaS 友好（拖拽 UI），其他都难
  → 推荐：纯 Coze + 加 1 个后端工程师做 OpenAPI 插件
```

⚠️ **一个具体问题**：让你 7 工程师**自我评估**：
> "用 Go 写 Eino agent 跟用 Python 写 AgentScope agent，你哪个更快？"

如果一致回答 Python——**别走 Coze Studio 自部署路线**。

### 6.2 招聘市场难度

| 岗位 | 难度 | 月薪 |
|---|---|---|
| Coze bot 设计师（业务方）| 易（全民教程多） | 普通工资 |
| Python AI 工程师（AgentScope）| 中 | 30-60K |
| Go AI 工程师（Eino）| **难** | **40-80K**（少且贵）|
| Matrix 协议熟手（HiClaw）| **极难** | 50K+（几乎招不到，要培养）|

---

## 7. 国际化与跨境

### 7.1 Coze.com（海外版）

- 跟国内版**不同账号体系**
- 海外服务器
- 模型清单不同（含 GPT/Claude）
- 适合**跨国电商 / 跨境业务**

### 7.2 AgentScope 国际化

- 全开源 → 任意部署
- 在国外用：Hugging Face / Modal / Replicate 等都支持
- 模型选择更广

### 7.3 你保健品 800 人公司

如果你是**国内市场为主** → Coze.cn 即可
如果有**跨境业务**（海外 KOL / 海外销售）→ Coze.com 海外版 + AgentScope 自部署混用

---

## 8. 真正的决策树

```
你公司情况
  │
  ├─ 工程师多 + 数据极敏感 + 数据自有诉求强
  │  → AgentScope 自部署主战略
  │
  ├─ 业务方多 + 全员推广 + 飞书重度用户
  │  → Coze 主战略（你公司）
  │
  ├─ 中小团队 + 个人开发者
  │  → Coze 个人版/团队版
  │
  ├─ 大厂 + 工程文化重 + 想完全控制
  │  → AgentScope 自部署 + Eino 二开
  │
  └─ 跨境业务
      → Coze.com + AgentScope 国际化
```

---

## 9. 最后的建议（**对你 800 人保健品**）

### 9.1 主战略：Coze 不变

理由：业务方友好 + 飞书原生 + 推广可行性最高 + 客户案例（山西联康医疗 50+ bot）。

### 9.2 但**额外做 3 件事**

#### A. 1 工程师跟踪 AgentScope 半年

```
任务：
- 跑通 AgentScope 1.0 quickstart
- 用 AgentScope 重做销售助手核心场景（PoC 不上线）
- 评估 HiClaw 在"项目协作"场景的可行性
- 季度做内部分享

预算：1 人 × 50% × 6 月 ≈ ¥45K
回报：当 Coze 出问题时有 plan B；当某场景需要时立即可用
```

#### B. 关键场景**双跑**

```
"销售助手日常对话"  → Coze 主跑
"项目协作（产品发布筹备）"  → 用 HiClaw PoC（小范围 5 人测试）
"敏感健康咨询"  → 用 AgentScope 自部署 + 国内开源大模型（小范围 PoC）
```

#### C. AI Gateway 用 Higress（不是 LiteLLM）

我之前推荐 LiteLLM，**改推 Higress**：
- 阿里出，国内活跃
- AgentScope 生态原生
- 切换 AI 平台时不锁定

具体见 `MODELS.md`、`AI-GATEWAY-SETUP.md` 改造计划（你工程师 2 重写）。

---

## 10. 一句话技术结论

> **Coze 是给业务方的精装房；AgentScope 是给工程师的毛坯房；HiClaw 是工程师组建多 Agent 团队的协议层。**

> 你 800 人保健品 = **精装房主居 + 毛坯房备用 + 协议层探索**。

---

## 11. 附：3 个产品的定位金句

- **Coze**：扣子让 1 亿人用上 AI Agent。
- **AgentScope**：Build and run agents you can see, understand and trust.
- **HiClaw**：Open-source Collaborative Multi-Agent OS for transparent, human-in-the-loop task coordination via Matrix rooms.

---

## 12. 引用源（深度版）

- AgentScope 1.0 论文（arxiv 2508.16279v1）
- Eino 框架（CloudWeGo / 字节）：https://github.com/cloudwego/eino
- HiClaw（agentscope-ai/HiClaw）：https://github.com/agentscope-ai/HiClaw
- HiMarket（Higress 项目）
- AgentScope GitHub（12K+ stars）：https://github.com/agentscope-ai/agentscope
- AgentScope Memory 模式：DeepWiki memory-management-patterns
- HiClaw 加入 AgentScope 公告（Alibaba Cloud Blog）
- 2026 Claw 生态对比（博客园 aigclabs）

本目录其他相关：
- `COZE-VS-AGENTSCOPE.md` —— 高层概览版（这次 deep dive 的前提）
- `MODELS.md` + `AI-GATEWAY-SETUP.md` —— 网关选型（含 Higress 评估）
- `MEMORY-COMPARISON.md` —— 记忆系统五方对比（Coze / GBrain / Hindsight / AgentScope memory）
- `SAAS-VS-SELFBUILD.md` —— SaaS 边界 + 你公司服务架构
