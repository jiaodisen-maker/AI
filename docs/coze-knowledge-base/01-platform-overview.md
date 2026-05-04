# 01 · Coze 平台架构总览

## 1. 技术栈

| 层 | 用什么 | 关键意义 |
|---|---|---|
| **编排引擎** | [Eino](https://github.com/cloudwego/eino)（CloudWeGo Go 框架）| 工作流是 DAG；ChatModel/Tool/Retriever/Embedding 抽象统一 |
| **画布** | FlowGram | 拖拽编辑器 |
| **后端** | Golang + 微服务 + DDD + [Hertz](https://github.com/cloudwego/hertz) | 高并发，企业版多租户隔离 |
| **前端** | React + TypeScript | 可视化拖拽 |
| **存储** | 默认 TOS（对象）+ VikingDB（向量），可换 | 私有部署可改 MinIO + Milvus 等 |
| **模型** | Doubao / 方舟 / OpenAI / Claude / DeepSeek / 通义 / 自部署 | 通过 YAML 模板加载 |

## 2. 三层抽象

```
┌────────────────────────────────────────┐
│  Workflow Engine（FlowGram + Eino）   │  最上层：编排
│  - DAG / 控制流 / 数据流               │
│  - 节点：LLM/Plugin/Workflow/Code/    │
│    Selector/Loop/Batch/Knowledge/...  │
└────────────────┬───────────────────────┘
                 │
┌────────────────▼───────────────────────┐
│  Agent Builder                         │  中层：Agent
│  - Prompt + RAG + Plugin               │
│  - Multi-Agent 模式（jump conditions）│
│  - Memory（变量 / 数据库 / 长期记忆） │
└────────────────┬───────────────────────┘
                 │
┌────────────────▼───────────────────────┐
│  Model Service Layer                   │  底层：模型
│  - 统一接口：OpenAI/Claude/Ark/...    │
│  - 动态负载均衡                       │
└────────────────────────────────────────┘
```

## 3. 工作流节点类型

### 3.1 基础节点
- **大模型节点（LLM）**：动态变量注入、prompt 工程
- **插件节点（Plugin）**：调外部能力（OpenAPI 导入）
- **工作流节点（Sub-workflow）**：嵌套调用

### 3.2 业务逻辑节点
- **代码节点（Code）**：运行 Python（**Coze Studio 自部署有 SSRF / 代码执行风险，公网暴露要慎重**）
- **选择器（Selector）**：条件分支
- **循环（Loop）** / **批处理（Batch）**：迭代和并行

### 3.3 集成节点
- **知识库（Knowledge）**：RAG 检索
- **API 节点**：调外部 HTTP

## 4. Multi-Agent 模式

每个节点 = 一个 Agent（独立 prompt + 独立 skills）；通过 **jump conditions**（关键词触发）在 bot 间传递控制。

适合：客服分诊、复杂业务编排（销售-售后-合规分工）。

## 5. 与生态的关系

| 关联 | 说明 |
|---|---|
| **Coze Loop** | 配套的**评测 + 观测 + 提示词管理**平台。开源 Apache 2.0。SDK：Go / Python / Node。|
| **HiAgent** | 火山引擎面向**高合规企业**的兄弟产品。私有化、CRM/ERP 深度对接。|
| **Coze Studio**（开源）| 自部署版本。包含**核心引擎**但**不含 Agent World**（云电脑/云手机/邮箱）|
| **Eino** | 编排引擎。开源，可独立用 Go 写 Agent，**逃生通道**——你的工作流可以脱离 Coze 跑 |

## 6. 关键限制（公开抱怨集合）

- ❌ Coze Pro SaaS **没有 bot 级 RBAC**，只到工作空间级
- ❌ 资源点机制不透明，**预估难**
- ❌ 自部署版**SSRF / 越权 / Python 代码执行**有公开 issue
- ❌ Agent World 只在 SaaS 上，**自部署 / HiAgent 都没有**

## 引用源

- [GitHub coze-dev/coze-studio](https://github.com/coze-dev/coze-studio)
- [GitHub coze-dev/coze-loop](https://github.com/coze-dev/coze-loop)
- [Eino 框架文档（CloudWeGo）](https://www.cloudwego.io/docs/eino/)
- [Coze 工作流节点类型 wiki](https://github.com/coze-dev/coze-studio/wiki)
