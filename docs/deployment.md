# AI 中台 — 部署指南

## 一、环境要求

```
服务器: 4核 8GB+ RAM (推荐 8核 16GB)
OS:    Ubuntu 22.04+ / CentOS 8+
Docker: 24.0+
Docker Compose: v2.20+
```

## 二、快速部署（Docker Compose 一键启动）

```bash
# 1. 克隆代码
git clone https://github.com/jiaodisen-maker/AI.git
cd AI
git checkout claude/continue-ai-middleware-Z1bve

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env，填入实际值：
#   LOCAL_MODEL_BASE_URL — LLM API 地址（DataEyes 或本地 vLLM）
#   LOCAL_MODEL_API_KEY  — API Key
#   FEISHU_APP_ID/SECRET — 飞书 Bot 配置（可选）

# 3. 一键启动（API + MySQL + Redis + Neo4j）
docker compose up -d

# 4. 验证
curl http://localhost:8080/api/health
# 预期: {"status":"healthy","version":"0.1.0","service":"ai-zhongtai"}

# 5. 查看各服务
docker compose ps
# api   → http://localhost:8080  (API + Swagger)
# mysql → localhost:3306         (业务数据库)
# redis → localhost:6379         (缓存/记忆)
# neo4j → http://localhost:7474  (知识图谱 Web UI)
```

## 三、服务端口

| 服务 | 端口 | 用途 |
|---|---|---|
| API | 8080 | FastAPI + Swagger 文档 |
| MySQL | 3306 | 业务数据库（Skill 日志、经验 Pattern） |
| Redis | 6379 | 会话记忆、经验缓存、飞书去重 |
| Neo4j Web | 7474 | 知识图谱可视化界面 |
| Neo4j Bolt | 7687 | 知识图谱连接协议 |

## 四、默认账号

| 服务 | 用户名 | 密码 |
|---|---|---|
| MySQL | zhongtai | zhongtai123 |
| MySQL root | root | root123 |
| Neo4j | neo4j | zhongtai123 |

**生产环境请修改所有默认密码！**

## 五、开发模式（不用 Docker）

```bash
# 1. 安装依赖
pip install -e ".[dev]"
pip install agentscope pyyaml aiosqlite

# 2. 可选：安装 Deep Agent 依赖
pip install -e ".[deep]"

# 3. 配置 .env
cp .env.example .env
# 开发模式默认用 SQLite，不需要 MySQL

# 4. 启动
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

# 5. 运行测试
python -m pytest tests/ -v
```

## 六、LLM 模型配置

### 方案 A: DataEyes API（推荐起步）

```env
LOCAL_MODEL_BASE_URL=https://cloud.dataeyes.ai/v1
LOCAL_MODEL_NAME=qwen2.5-72b-instruct
LOCAL_MODEL_API_KEY=sk-your-key-here
```

### 方案 B: 本地 vLLM 部署

```bash
# 安装 vLLM
pip install vllm

# 启动 Qwen2.5-72B (需要 4×A100 80GB)
vllm serve Qwen/Qwen2.5-72B-Instruct \
  --host 0.0.0.0 --port 8000 \
  --tensor-parallel-size 4

# .env 配置
LOCAL_MODEL_BASE_URL=http://localhost:8000/v1
LOCAL_MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
LOCAL_MODEL_API_KEY=not-needed
```

### 方案 C: DeepSeek API（低成本）

```env
LOCAL_MODEL_BASE_URL=https://api.deepseek.com/v1
LOCAL_MODEL_NAME=deepseek-chat
LOCAL_MODEL_API_KEY=sk-your-deepseek-key
```

## 七、飞书 Bot 配置

```
1. 登录飞书开放平台 https://open.feishu.cn
2. 创建企业自建应用
3. 添加机器人能力
4. 配置事件订阅：
   - 请求地址: https://your-domain.com/api/feishu/webhook
   - 订阅事件: im.message.receive_v1
5. 获取 App ID / App Secret / Verification Token
6. 填入 .env:
   FEISHU_APP_ID=cli_xxx
   FEISHU_APP_SECRET=xxx
   FEISHU_VERIFICATION_TOKEN=xxx
```

## 八、CLI 管理工具

```bash
# 健康检查
python -m app.cli.main health

# 技能管理
python -m app.cli.main skill list
python -m app.cli.main skill exec compliant-copy "写一篇胶原蛋白小红书文案"

# 本体管理
python -m app.cli.main ontology list
python -m app.cli.main ontology validate

# 巡逻任务
python -m app.cli.main patrol list
```

## 九、验证清单

部署后逐项验证：

```bash
# 1. 健康检查
curl http://localhost:8080/api/health

# 2. Swagger 文档
open http://localhost:8080/docs

# 3. 技能列表
curl http://localhost:8080/api/skills/

# 4. 本体查询
curl http://localhost:8080/api/ontology/compliance/胶原蛋白

# 5. 对话测试（需要 LLM）
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"帮我写一篇胶原蛋白的小红书文案"}'

# 6. 工作流测试
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"/workflow 新品上市文案流程"}'

# 7. Neo4j Web UI
open http://localhost:7474

# 8. 运行测试套件
python -m pytest tests/ -v
```

## 十、生产环境加固

```
□ 修改所有默认密码
□ 配置 HTTPS（Nginx 反向代理 + Let's Encrypt）
□ 设置 SECRET_KEY 为 32+ 字符随机字符串
□ 关闭 DEBUG=false
□ 配置日志轮转
□ 设置 MySQL 自动备份
□ 配置监控告警（Prometheus + Grafana 或 Langfuse）
□ 限制 Neo4j/MySQL 端口仅内网访问
```
