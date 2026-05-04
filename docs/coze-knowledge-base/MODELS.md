# 给扣子加第三方大模型让所有人用 · 完整方案

> 配合 `PLAN.md` + `FEISHU-INTEGRATION.md` 食用。
> 信息源：`raw/coze_cn/guides/{model_service,ark_model,deploy_custom_model,
> volcengine_ark_integration,model_management,viewing_model}.md` + `coze_pro/model_fee.md`。

## 0. TL;DR

| 接入方式 | 套餐 | 适合 | 是否第三方 |
|---|---|---|---|
| **官方扣子模型** | 所有版 | 豆包/DeepSeek/Kimi/阶跃/GLM | ❌ 不算 |
| **火山方舟接入点** | 企业标准/旗舰 | 字节系扩展（视觉/生成）| 算"半第三方" |
| **自定义模型接入** ⭐ | **仅企业旗舰版** | OpenAI / Claude / 自部署 / 任何 OpenAI 兼容 | ✅ 真第三方 |

**让所有人用 = 必须企业旗舰版，必须走"自定义模型接入"，必须给工作空间授权。**

如果你想做得**最专业**：在扣子和真实模型之间**架一层 AI Gateway**，扣子只接 1 个"网关模型"，背后想接多少模型就接多少。

---

## 1. 三种方式详细对比

### 1.1 方式 A：官方扣子模型（开箱即用，不算"接第三方"）

**有什么**（来自 `model_service.md`）：

| 厂商 | 模型 | 套餐 |
|---|---|---|
| **字节豆包** | Doubao-2.0-pro/lite/code、1.6 系列、1.5 系列、视觉/角色等 ~25 款 | 全部 |
| **深度求索** | DeepSeek-R1 / V3.2 / V3-0324 / V3-FunctionCall | 全部 |
| **月之暗面** | Kimi-8k/32k/128k | 全部 |
| **阶跃星辰** | step-1.5v / step-1v 视频图像理解 | **付费版** |
| **智谱 AI** | GLM-4.7 | 全部 |

**特点**：
- 登录即用，**不要任何配置**
- 计费：消耗**扣子积分**（部分免费，每模型 100 次/天）
- 部分模型**限时免费**（Kimi、阶跃星辰）

**结论**：你 800 人公司，**这一档基本覆盖 80% 场景**——豆包写作 + DeepSeek 推理 + Kimi 长文档 + GLM 编程。
**先把这一档用透**，再考虑接第三方。

### 1.2 方式 B：火山方舟接入点（**企业版才有**）

**做什么**（来自 `ark_model.md`）：
- 在火山方舟控制台创建"模型推理接入点"
- 拿 Endpoint ID，扣子里能选这个接入点
- 适合：豆包微调版、视频生成（doubao-seedance）、视觉生成（doubao-seedream）等

**配置流程**：
```
火山方舟控制台 → 模型推理 → 在线推理 → 创建推理接入点
  ↓
设置接入点名称、选模型版本、按 Token 或按模型单元付费、限流（建议不设）
  ↓
开通模型并接入 → 拿 Endpoint ID
  ↓
扣子里：智能体编排 → 选模型 → "自开通模型|在方舟自己开通的模型"分类
```

**计费**：火山方舟现金，**不消耗扣子积分**
**权限**：开通后默认所有工作空间可用，空间所有者可禁用

**结论**：仍然是**字节系内部**模型。要接 OpenAI/Claude，看下面 1.3。

### 1.3 方式 C：自定义模型接入（⭐ **真正的第三方**，仅企业旗舰版）

**做什么**（来自 `deploy_custom_model.md`）：
- 接入**任何 OpenAI Chat/Responses API 兼容**的模型：
  - OpenAI（GPT-4o, GPT-5, o1）
  - Anthropic Claude（通过兼容层）
  - 自部署 Llama / Qwen / Yi / DeepSeek
  - 第三方 AI 厂商提供的兼容端点
- 配置：API URL + API Key + 鉴权方式 + 模型能力声明
- 流式（stream=true）必须支持
- 密钥存储：明文 OR **火山 KMS 加密**

**配置参数（接入时填的关键字段）**：

| 字段 | 说明 |
|---|---|
| 模型 icon + 展示名称 | 团队成员看到的样子，例 "Claude-3.5-Sonnet" |
| **模型唯一标识** | 例 `claude-3-5-sonnet-20240620`（发请求时填到 `model` 字段）|
| **模型 API URL** | 例 `https://api.anthropic.com/v1`（系统会自动拼 `/chat/completions`，所以**不要**带这部分）|
| API 协议 | 固定 OpenAI Chat/Completion 兼容 |
| **鉴权方式** | Authorization（标准 Bearer）OR 自定义 Header |
| **鉴权密钥** | API Key 或 Header Value，**强烈推荐火山 KMS 加密** |
| 模型能力 | 工具调用 / 图片理解 / 视频理解 / 音频 / 续写 / 深度思考 |
| 模型上下文长度 | 例 200000（Claude 3.5）|
| **自定义参数 schema** | JSON Schema 定义可调参数（temperature、top_p、max_tokens 等）|

**关键限制**：
- ⚠️ **必须企业旗舰版**（标准版没这功能）
- ⚠️ 操作权限只有**组织超级管理员 + 管理员**
- ⚠️ 自定义模型必须**默认所有空间禁用**，管理员**逐空间授权**才能用
- ⚠️ KMS 加密会产生火山引擎额外费用（**不消耗扣子积分**）
- ⚠️ 模型必须支持流式响应

---

## 2. ⭐ 最佳实践：架一层 AI Gateway

### 2.1 为什么强烈推荐

不要在扣子里直接接 OpenAI/Claude 等真实模型——架一层**统一网关**：

```
扣子 → 自定义模型："company-ai-gateway"
       │
       └── HTTP POST → https://ai-gateway.your-company.com/v1/chat/completions
                       │
                       └── 网关根据请求 model 字段路由：
                           - model: "gpt-4o" → OpenAI
                           - model: "claude-3-5-sonnet" → Anthropic
                           - model: "qwen-72b" → 自部署
                           - model: "doubao-1.6" → 火山方舟
                           - model: "deepseek-v3" → DeepSeek
```

### 2.2 网关带来的 7 个好处

1. **扣子里只配 1 个"模型"，加新模型不用进扣子**——改网关 yaml 就行
2. **统一密钥管理**：公司层面 1 把 OpenAI key、1 把 Claude key——不在扣子里散落
3. **统一日志审计**：所有 LLM 调用都过网关，全链路审计
4. **统一限流**：按部门 / 按 bot / 按模型设配额
5. **统一成本核算**：每月一份"模型调用账单"，按部门分摊
6. **A/B 切换**：同一 prompt 在线切模型对比效果
7. **故障切换**：OpenAI 宕机 → 自动 fallback 到 Claude

### 2.3 推荐网关方案（**开源**）

| 方案 | 特点 | 推荐度 |
|---|---|---|
| **LiteLLM Proxy**（github.com/BerriAI/litellm）| Python，OpenAI 兼容，200+ 模型，最流行 | ⭐⭐⭐⭐⭐ |
| **One-API**（github.com/songquanpeng/one-api）| Go，国内常用，UI 界面好 | ⭐⭐⭐⭐ |
| **OpenRouter**（saas）| 不自部署，按调用付费，省心 | ⭐⭐⭐ |
| **自研** | 完全可控但要工程投入 | ⭐⭐（不推荐）|

**强烈建议 LiteLLM Proxy**——你 7 工程师里 1 人用 1 周搞定。

### 2.4 LiteLLM Proxy 配置示例

```yaml
# litellm_config.yaml
model_list:
  - model_name: gpt-4o                    # 扣子里看到的名字
    litellm_params:
      model: openai/gpt-4o
      api_key: os.environ/OPENAI_API_KEY

  - model_name: claude-3-5-sonnet
    litellm_params:
      model: anthropic/claude-3-5-sonnet-20240620
      api_key: os.environ/ANTHROPIC_API_KEY

  - model_name: qwen-72b
    litellm_params:
      model: openai/qwen-72b               # OpenAI 兼容
      api_base: http://qwen-internal.your-company.com/v1
      api_key: os.environ/QWEN_API_KEY

  - model_name: deepseek-v3
    litellm_params:
      model: deepseek/deepseek-chat
      api_key: os.environ/DEEPSEEK_API_KEY

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY  # 扣子用这个 key 调网关
  database_url: postgresql://...              # 存 trace 和审计

router_settings:
  routing_strategy: simple-shuffle              # 或 latency-based
  fallbacks:
    - gpt-4o: ["claude-3-5-sonnet", "deepseek-v3"]   # GPT 挂了切 Claude

# 按 bot/部门设配额
budget_duration: monthly
max_budget: 5000  # 美元/月
```

### 2.5 在扣子里只接 1 个网关模型

```
扣子 → 企业组织管理 → 模型接入 → 自定义模型 → 接入模型
  模型展示名称：公司 AI 网关
  模型唯一标识：（不重要，因为扣子按 prompt 决定真实 model 字段）
  API URL：https://ai-gateway.your-company.com/v1
  鉴权：Authorization
  API Key：<LITELLM_MASTER_KEY>
  模型能力：工具调用 ✅ 图片理解 ✅ 深度思考 ✅
  上下文长度：200000
```

⚠️ **限制**：扣子的"模型唯一标识"会作为请求 body 的 `model` 字段。所以**你需要稍微 hack 一下**：要么在扣子里接 N 个"模型"（每个对应网关里一个 model_name），要么在 LiteLLM 侧做请求改写。

**实际推荐**：在扣子里接 5-10 个"模型"，每个指向网关同 URL 但不同 model 字段：

```
扣子里接：
  - "GPT-4o" → URL=网关, model_id="gpt-4o"
  - "Claude-3.5-Sonnet" → URL=网关, model_id="claude-3-5-sonnet"
  - "Qwen-72B-内部" → URL=网关, model_id="qwen-72b"
  - "DeepSeek-V3" → URL=网关, model_id="deepseek-v3"
```

新加模型 → 网关 yaml 加一行 → 扣子接一次（10 分钟），**比每次去 OpenAI/Claude 配密钥强多了**。

---

## 3. 给"所有人用"的部署流程

### 3.1 总流程

```
┌─────────────────────────────────────────────────────────┐
│  阶段 1  调研选型           你 + 工程师 1（1 周）        │
│  阶段 2  搭 AI Gateway     工程师 2（5 天）              │
│  阶段 3  扣子接入网关       工程师 1（2 天）             │
│  阶段 4  按部门授权空间     工程师 1（2 天）             │
│  阶段 5  成本 + 监控        工程师 6（1 周）             │
│  阶段 6  推广 + 培训        你（持续）                    │
└─────────────────────────────────────────────────────────┘
```

### 3.2 阶段 1：调研选型（1 周）

按场景列模型：

| 场景 | 推荐模型 | 来源 | 合规风险 |
|---|---|---|---|
| 销售助手主对话 | 豆包 1.6 / DeepSeek-V3.2 | 扣子官方 | 低 |
| 客户档案分析 | 豆包 1.5-pro-32k | 扣子官方 | 低 |
| 长文档 / 合同审查 | Kimi-128k / Claude-3.5-Sonnet | 扣子官方 / **自定义接入** | 海外模型🟡 |
| 复杂推理 | DeepSeek-R1 / OpenAI o1 | 扣子官方 / **自定义接入** | 海外模型🟡 |
| 代码生成 | 豆包 2.0-Code / GPT-4o / Claude-3.5 | 扣子官方 / **自定义接入** | 海外模型🟡 |
| 图片生成 | Doubao-Seedream | 扣子官方插件 | 低 |
| 视频生成 | Doubao-Seedance | 扣子官方插件 | 低 |
| **客户健康数据相关** | **豆包系列 / 国内自部署** | **绝不能用海外模型** | 🔴 数据出境 |

⚠️ **保健品合规红线**：客户姓名、电话、健康问题、订单等数据**严禁送海外模型**。
海外模型只能做**通用任务**：写作、翻译、营销策划、代码、对外英文邮件等。

### 3.3 阶段 2：搭 AI Gateway（5 天，工程师 2）

#### Day 1-2：部署 LiteLLM
```bash
# 容器化部署
docker run -d \
  --name litellm-proxy \
  -p 4000:4000 \
  -v ./litellm_config.yaml:/app/config.yaml \
  -e DATABASE_URL=postgresql://... \
  -e OPENAI_API_KEY=sk-... \
  -e ANTHROPIC_API_KEY=sk-ant-... \
  -e DEEPSEEK_API_KEY=sk-ds-... \
  -e LITELLM_MASTER_KEY=sk-master-xxx \
  ghcr.io/berriai/litellm:main-stable

# 起一个 nginx + Cloudflare 给它套 HTTPS
```

#### Day 3：测试 + 兼容性
- 用 curl 测每个模型，确认流式正常
- 测工具调用（function calling）兼容性
- 测视觉模型（图片识别）兼容性

#### Day 4-5：审计 + 配额 + 监控
- 接 PostgreSQL 存所有调用 trace
- 设置 per-key 配额（按部门发 key）
- 接 Prometheus / Grafana 看延迟/错误率
- 接你公司告警通道

### 3.4 阶段 3：扣子接入网关（2 天，工程师 1）

#### 准备
- 把 `LITELLM_MASTER_KEY` 托管到**火山引擎 KMS**（强烈推荐）
  - 登录火山 KMS 控制台 → 新建凭据 → 凭据类型"通用凭据"
  - 凭据名 `coze-ai-gateway-key`
  - 凭据值：master key 明文
  - 加密主密钥：系统默认即可

#### 接入扣子
扣子编程 → 左下角企业 → 设置 → 模型接入 → 自定义模型 → 接入模型

按 §2.5 的 5-10 个"模型"分别接入，每个填：
- API URL：网关 URL
- 模型唯一标识：网关里对应的 model_name
- 鉴权：Authorization
- 鉴权密钥：火山 KMS 加密 → Secret Name = `coze-ai-gateway-key`
- 模型能力：根据真实模型勾选
- 上下文长度：填模型最大值
- 自定义参数 schema：用 §2.5 的 JSON Schema（temperature、top_p、max_tokens 等）

### 3.5 阶段 4：按部门授权空间（2 天）

按 `FEISHU-INTEGRATION.md §9` 的工作空间结构：

| 空间 | 开放的"自定义模型" | 理由 |
|---|---|---|
| 销售空间 | 豆包系列、DeepSeek-V3.2、Qwen-72B（自部署）| 涉及客户数据，全国内 |
| 客服空间 | 豆包系列、DeepSeek | 同上 |
| 市场空间 | 豆包、Claude-3.5、GPT-4o | 营销文案可用海外（不涉客户数据）|
| 培训空间 | 豆包、GPT-4o、Claude | 通用培训内容 |
| HR 空间 | 豆包系列 | HR 数据敏感 |
| 法务空间 | 豆包、Claude（合同审查）| Claude 长文档强 |
| 沙箱空间 | 全部模型 | 工程师测试用 |

操作：模型接入 → 自定义模型 → 模型 → ··· → **修改可用空间** → 逐空间开关

### 3.6 阶段 5：成本 + 监控（1 周，工程师 6）

#### LiteLLM 侧（统一视角）
- 每个部门发 1 个 LiteLLM API Key（ Coze 不直接用，但可分摊统计）
- LiteLLM 自带 admin UI 看：调用次数 / token 量 / 成本（美元/月）
- 每月对账：用 SQL 查 LiteLLM 的 logs 表，按 model + bot_id 分组

#### 扣子侧
- Coze Loop 看每个 bot 的 trace：哪个调用慢/贵
- "模型管理"页面看用量记录

#### 告警
- 单 bot 单日 token 量 > 阈值 → 飞书通知
- LiteLLM 月预算达 80% → 飞书 + 邮件
- 模型调用错误率 > 5% → 飞书

### 3.7 阶段 6：推广 + 培训（持续，你）

工程师视角不够——业务方要知道**什么模型适合什么场景**：

#### 给业务方的 1 页选模型指南

```
# 我该用哪个模型？

## 选模型最简单原则
不知道用什么 → 选「豆包 1.6」准没错

## 按场景

| 场景 | 用 |
|---|---|
| 日常对话 / 写文档 / 写邮件 | 豆包 1.6 |
| 销售话术 / 客户分析 | 豆包 1.5-pro |
| 长文档（>30K 字）| Kimi-128k |
| 复杂推理 / 数学 / 逻辑 | DeepSeek-R1 |
| 编程 | 豆包 2.0-Code |
| 翻译/英文营销文案 | GPT-4o（注意：不能含客户数据）|
| 合同审查 / 法律 | Claude-3.5-Sonnet |
| 想要"更聪明" | DeepSeek-R1 或 Claude |
| 想要"更便宜" | 豆包 1.5-Lite |

## 红线
❌ 客户姓名 / 电话 / 健康问题 → 绝不能用 GPT/Claude
❌ 处方 / 病历 → 绝不能用 GPT/Claude
✅ 营销文案 / 翻译 / 英文邮件 → GPT/Claude 可以
```

---

## 4. 成本估算

### 4.1 各模型大致成本（仅供参考，以厂商最新价格为准）

| 模型 | 输入价 | 输出价 | 100 万 token 总价 |
|---|---|---|---|
| 豆包 1.6（扣子积分）| ≈ 0.0008元/K | ≈ 0.002元/K | ¥2-3（积分换算）|
| DeepSeek-V3.2 | ≈ 0.0007元/K | ≈ 0.0028元/K | ¥1.5-3 |
| Kimi-128k | 限免 100 次/天 | | 0（限内）|
| **GPT-4o** | $2.5/M | $10/M | **$12.5 ≈ ¥90** |
| **Claude-3.5-Sonnet** | $3/M | $15/M | **$18 ≈ ¥130** |
| **OpenAI o1** | $15/M | $60/M | **$75 ≈ ¥540** |
| 自部署 Qwen-72B | 自有算力 | | 折算 ¥2-5（看硬件）|

### 4.2 800 人公司月度估算

```
日常对话（豆包/DeepSeek 主力）：
  800 人 × 30 次/天 × 22 天 × 2K tokens = 1.05 亿 tokens
  ≈ 200-300 元 / 月（积分形式）

复杂任务（10% 调海外模型）：
  20 万次/月 × 2K tokens × ¥130/M = 5,200 元/月
  ≈ ¥5,000-8,000 / 月（取决用量）

视觉/视频生成：
  ≈ ¥500-2,000/月

合计：约 ¥6,000-10,000 / 月（在你 §4.3 PLAN.md 的预算内）
```

### 4.3 强烈建议的成本硬控

1. **LiteLLM 侧**：设月预算上限 $1,500（约 ¥10,500），到点拒绝调用
2. **扣子侧**：按工作空间设积分上限
3. **每周对账**：按模型分组看消耗，发现异常 bot 立刻定位

---

## 5. 合规护栏（保健品行业重点）

### 5.1 数据不能出境的硬规则

| 数据类型 | 能用国内模型 | 能用海外模型 |
|---|---|---|
| 通用写作 / 翻译 | ✅ | ✅ |
| 营销文案 | ✅ | ✅（**不含客户名**）|
| 客户姓名 / 电话 / 地址 | ✅ | ❌ |
| 客户健康问题 | ✅（**仅做通用建议**）| ❌ |
| 处方 / 病历 | ❌（**不进 bot**）| ❌ |
| 销售订单 / 财务 | ✅ | ❌ |
| 内部 SOP / 制度 | ✅ | ✅ |
| 公司机密 / 战略 | ✅（**仅自部署**）| ❌ |

### 5.2 在 LiteLLM 网关做 PII 检测

```python
# 在 LiteLLM custom_callback 里加
from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()

async def block_pii_to_overseas(model, messages):
    if model not in ["gpt-4o", "claude-3-5-sonnet", "openai-o1"]:
        return  # 国内模型放行
    
    text = " ".join(m["content"] for m in messages)
    results = analyzer.analyze(text=text, language='zh',
                                entities=["PHONE_NUMBER", "EMAIL_ADDRESS",
                                          "PERSON", "MEDICAL_LICENSE"])
    if results:
        raise PermissionError(f"PII detected in overseas model call: {results}")
```

### 5.3 工作空间白名单 + 模型黑名单

按 §3.5 的方案：销售/客服/HR 空间**根本不接** GPT/Claude——从架构上断绝错用可能。

---

## 6. 4 周冲刺：模型层

| Week | 任务 | 谁 | 交付 |
|---|---|---|---|
| 1 | 调研业务场景 → 模型选型；申请 OpenAI/Claude 企业账号；密钥准备 | 你 + 工程师 1 | 模型选型表 + 所有 API Keys |
| 1-2 | 部署 LiteLLM Proxy + Postgres + 监控 | 工程师 2 | 公网 HTTPS endpoint + admin UI |
| 2 | LiteLLM 接 5 个模型并测通（豆包/DeepSeek/Qwen 自部署/GPT-4o/Claude-3.5）| 工程师 2 | 5 个 model_name 都通 |
| 2 | 火山 KMS 托管 master key | 工程师 1 | KMS 凭据 |
| 3 | 在扣子接入 5 个"自定义模型" + JSON Schema 配置 | 工程师 1 | 5 个模型扣子可见 |
| 3 | 按部门给工作空间授权 | 工程师 1 | 6 个空间权限设好 |
| 4 | 业务方培训 + 选模型指南发布 + Coze Loop 监控接入 | 你 + 工程师 6 | 文档 + 培训完成 |

---

## 7. 风险 + 对策

| 风险 | 严重度 | 对策 |
|---|---|---|
| **OpenAI / Claude API 在国内不稳定 / 被封** | 🔴 高 | LiteLLM 配 fallback；备用渠道（如 OpenRouter / 国内代理）|
| **客户数据被员工误送海外模型** | 🔴 高 | 1) 工作空间不开放海外模型 2) LiteLLM 加 PII 拦截 |
| **网关挂了影响所有扣子 bot** | 🔴 高 | 高可用部署（双实例 + LB）；扣子里也保留 1-2 个直连官方模型作 fallback |
| **海外模型成本失控** | 🟡 中 | LiteLLM 月预算硬上限；按部门发独立 key |
| **API Key 泄露** | 🔴 高 | 全部用火山 KMS；不写 yaml；rotate 季度一次 |
| **业务方乱选模型导致体验差** | 🟡 中 | 写"选模型指南"+ 默认推荐豆包；Coze Loop 评测发现问题 |
| **海外模型协议变化** | 🟢 低 | LiteLLM 升级即可，扣子端不感知 |
| **企业旗舰版到期 → 自定义模型不可用** | 🔴 高 | 提前 30 天预警续费 |

---

## 8. 还有一个问题：**官方扣子模型** vs **自定义接入** 的取舍

你可能问：豆包扣子官方就有，何必通过 LiteLLM 再接一次？

**答案**：

| 维度 | 官方扣子模型 | 通过 LiteLLM 自定义接入 |
|---|---|---|
| 配置 | 0 配置 | 需建网关 |
| 计费 | 扣子积分 | 火山方舟现金 / 自部署算力 |
| 限流 | 扣子统一控 | 自己控 |
| 审计 | Coze Loop | LiteLLM + Coze Loop 双份 |
| **统一口径** | 扣子定义 | **公司统一定义（更灵活）** |
| 模型选择 | 扣子提供啥用啥 | **任意 OpenAI 兼容模型** |
| 切换/弃用 | 等扣子 | **公司自己控制** |

**最佳实践**：**两者并用**——
- 简单场景 / 95% 任务 → **直接用扣子官方模型**（豆包 / DeepSeek / Kimi），省事
- 需要 GPT/Claude/自部署 / 想统一审计 / 多模型路由 → **走 LiteLLM 网关**

不要硬把豆包也走网关——多一跳，慢一点，没必要。

---

## 9. 引用源

- `guides/model_service.md` —— 模型服务总览（豆包/DeepSeek/Kimi/阶跃/GLM 全清单）
- `guides/ark_model.md` —— 火山方舟接入点
- `guides/deploy_custom_model.md` —— **自定义模型接入完整流程**
- `guides/volcengine_ark_integration.md` —— 火山方舟集成
- `guides/model_management.md` —— 模型生命周期管理
- `guides/viewing_model.md` —— 性能 + 用量监控
- `coze_pro/model_fee.md` —— 模型计费规则

外部参考：
- LiteLLM Proxy: https://github.com/BerriAI/litellm
- One-API: https://github.com/songquanpeng/one-api
- 火山引擎 KMS: 凭据托管
