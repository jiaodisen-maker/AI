# AI 中台 - 自进化企业 AI 操作系统

## 产品定位

以 Skill 为中心的企业 AI 中台，不是通用 AI 平台，而是**保健品行业深度适配的自进化 AI 操作系统**。

核心差异化：
- **经验引擎**：Skill 越用越准，人工修正自动沉淀为经验
- **巡逻系统**：不等命令，主动发现问题和机会
- **私有部署**：解决扣子的四堵墙（数据安全、海外模型、复杂 skill、信息合规）

## 验证状态

| 已验证（扣子阶段） | 待建设 |
|---|---|
| 员工愿意用对话触发 skill | 企业级运行时 |
| Skill 模式能编码业务经验 | 经验引擎（自进化） |
| 保健品合规检查是高频场景 | 巡逻系统（主动发现） |
| 飞书是自然入口 | 私有部署 + 数据安全 |

---

## 修正后的路线图

### Phase 0: 骨架 + 第一个 Skill（第 1-2 周）

**目标**：用最小代码跑通 "飞书发消息 → AI 生成合规文案 → 返回结果" 全链路。

```
员工在飞书说："帮我写一段胶原蛋白的小红书文案"
     ↓
飞书 Bot 收到消息
     ↓
Brain 识别意图 → 路由到 /compliant-copy skill
     ↓
Skill 调用 LLM（通过 LiteLLM 路由）
     ↓
合规引擎校验输出（禁词检查 + 广告法合规）
     ↓
返回结果到飞书
```

交付物：
- [x] 项目骨架（FastAPI + 目录结构）
- [x] Skill 格式规范 + 注册中心
- [x] LLM 路由层（LiteLLM）
- [x] 合规文案 Skill（第一个 skill）
- [x] 飞书 Bot webhook 接入
- [x] 基础 Web API

### Phase 1: 经验引擎（第 3-4 周）

**目标**：让 Skill 学会进化。

```
第 1 次运行：AI 生成文案，文案专员改了 30%
第 5 次运行：AI 吸收了修改 pattern，只需改 15%
第 20 次运行：AI 输出几乎不用改，文案专员只做微调
```

交付物：
- [ ] 执行记录系统（每次 skill 运行的 input/output/human_edit）
- [ ] 差异提取器（对比 AI 输出 vs 人工修改）
- [ ] Pattern 学习器（从差异中提取可复用规则）
- [ ] 经验注入器（生成时自动注入高置信度经验）
- [ ] 经验管理 Web UI（查看/编辑/删除经验规则）

### Phase 2: 数据层 + 更多 Skill（第 5-8 周）

**目标**：接通公司数据，让 AI 看得见业务全貌。

交付物：
- [ ] MySQL 连接器（产品库、订单库）
- [ ] ClickHouse 连接器（数据仓库查询）
- [ ] 向量检索（Milvus/Qdrant，企业文档 RAG）
- [ ] 数据查询 Skill：自然语言 → SQL → 结果
- [ ] 报表生成 Skill：自动周报/月报
- [ ] 竞品分析 Skill：爬取 + 对比分析

### Phase 3: 巡逻系统（第 9-10 周）

**目标**：从被动等命令变成主动发现问题。

```
每天 8:00  扫描昨日各渠道销售数据
           → 发现抖音胶原蛋白 ROI 下降 40%
           → 飞书推送给渠道运营 + 建议行动
           → 运营点击建议直接触发对应 skill
```

交付物：
- [ ] 定时任务调度器（APScheduler / Celery Beat）
- [ ] 异常检测引擎（基于规则 + 统计）
- [ ] 巡逻任务注册机制
- [ ] 飞书主动推送（卡片消息 + 可交互按钮）
- [ ] 巡逻日志 + 告警历史

### Phase 4: 多租户 + 权限 + 生产加固（第 11-14 周）

**目标**：从内部工具变成可服务多团队的平台。

交付物：
- [ ] 员工身份认证（飞书 SSO）
- [ ] 基于角色的权限控制（RBAC）
- [ ] Skill 级别权限（谁能用、谁能改）
- [ ] 操作审计日志
- [ ] 限流 + 熔断
- [ ] Docker Compose 一键部署
- [ ] 监控 + 告警（Prometheus + Grafana）

---

## 技术栈

| 层级 | 技术选型 | 理由 |
|---|---|---|
| Web 框架 | FastAPI | 异步、性能好、自动 OpenAPI 文档 |
| LLM 路由 | LiteLLM | 统一接口对接 100+ 模型，本地/海外/微调一套 API |
| 本地模型 | vLLM + Qwen-72B | 90% 请求走本地，成本 1/10 |
| 海外模型 | Claude Opus / GPT-4o | 复杂推理、创意任务 |
| 向量数据库 | Milvus / Qdrant | 企业文档 RAG |
| 分析数据库 | ClickHouse | 渠道数据分析、报表 |
| 业务数据库 | MySQL / PostgreSQL | 产品、订单、用户 |
| 缓存 | Redis | 会话状态、经验缓存、限流 |
| 任务队列 | Celery + Redis | 异步 skill 执行、定时巡逻 |
| 消息渠道 | 飞书开放平台 | 已验证的自然入口 |
| 文件存储 | MinIO / 阿里云 OSS | 生成的文档、报表、图片 |
| 部署 | Docker Compose → K8s | 先快后稳 |
| 监控 | Prometheus + Grafana | 全链路可观测 |

---

## Skill 格式规范

每个 Skill 是一个独立模块，遵循统一接口：

```python
class SkillMeta:
    id: str              # 唯一标识，如 "compliant-copy"
    name: str            # 显示名，如 "合规文案生成"
    description: str     # 描述，用于意图路由匹配
    category: str        # 分类：content / data / operation / product / patrol
    version: str         # 版本号
    author: str          # 作者
    triggers: list[str]  # 触发词，如 ["写文案", "生成文案", "合规文案"]
    parameters: dict     # 输入参数 JSON Schema
    permissions: list    # 需要的权限
    model_preference: str # 模型偏好：local / overseas / specialized
```

Skill 生命周期：
```
注册 → 发现 → 路由 → 执行 → 记录 → 学习 → 进化
```

---

## 经验引擎设计

### 核心循环

```
用户输入 → Skill prompt + 经验库 → LLM → AI 输出
                  ↑                          │
                  │                          ▼
                  │                     用户修改输出
                  │                          │
                  │                          ▼
                  └── 经验引擎提取差异 ←─ 记录修改 pattern
```

### 数据模型

```python
class ExperienceRecord:
    id: str
    skill_id: str
    input_context: dict      # 触发时的输入
    ai_output: str           # AI 原始输出
    human_edited: str        # 人工修改后的输出
    diff_summary: str        # 差异摘要
    extracted_patterns: list # 提取的规则
    created_at: datetime

class ExperiencePattern:
    id: str
    skill_id: str
    pattern: str             # 规则描述，如 "抖音文案用口语化表达"
    examples: list           # 正例/反例
    confidence: float        # 置信度 0-1
    usage_count: int         # 被应用次数
    effectiveness: float     # 有效性评分
    created_at: datetime
    updated_at: datetime
```

### 置信度机制

```
新 pattern 诞生    → confidence = 0.3
被第二次验证       → confidence = 0.5
5 次以上一致       → confidence = 0.8（自动注入 prompt）
被用户否决一次     → confidence -= 0.2
confidence < 0.1  → 自动归档
```

---

## 巡逻系统设计

### 巡逻任务类型

| 类型 | 频率 | 描述 |
|---|---|---|
| 渠道数据扫描 | 每天 8:00 | 扫描各渠道昨日销售、ROI、转化率 |
| 竞品监控 | 每天 10:00 | 爬取竞品价格、活动、新品信息 |
| 库存预警 | 每天 9:00 | 检查库存水位，预测断货风险 |
| 内容效果复盘 | 每周一 | 分析上周各平台内容表现 |
| 合规扫描 | 实时 | 新上线内容自动合规检查 |

### 告警级别

```
P0 - 立即通知（飞书消息 + 电话）：数据异常超过阈值 50%
P1 - 紧急通知（飞书消息）：数据异常超过阈值 20%
P2 - 日常通知（飞书卡片）：日常巡逻报告
P3 - 静默记录（仅日志）：微小波动
```

---

## 安全设计

### 四层安全模型

1. **身份层**：飞书 SSO → JWT token → 用户身份
2. **权限层**：RBAC — 角色（管理员/运营/内容/只读）→ Skill 级权限
3. **数据层**：数据分级（公开/内部/机密），Skill 只能访问授权数据
4. **审计层**：所有操作记录，可追溯、可回放

### 合规引擎

保健品广告法合规是核心需求，采用三层校验：

```
第一层：禁词库（300+ 禁用词/短语，正则匹配）
        "治疗""治愈""根治""特效""最佳"...

第二层：规则引擎（结构化规则）
        - 不得暗示疾病治疗效果
        - 必须包含"本品不能代替药物"声明
        - 功效宣称必须在批准范围内

第三层：LLM 审核（模型二次校验）
        把生成的文案交给另一个 LLM 做合规审核
        输出：通过 / 不通过 + 具体问题 + 修改建议
```
