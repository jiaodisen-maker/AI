# 火山引擎 ECS 最小部署（Day 1，4 小时完成）

> 目标：1 台 ECS + Docker Compose，端到端跑通飞书 → Coze。
> 完成后能看到飞书发消息触发 Coze bot，文档变更同步进 KB。

## 0. 你需要的账号 + 资源

```
□ 火山引擎账号（已有）+ 余额 ≥ ¥500
□ 火山扣子企业旗舰版（已有，能拿到 PAT）
□ 飞书企业管理员账号（能在开放平台建应用）
□ 1 个域名（可注册新的，约 ¥80/年）
□ 域名能改 DNS 解析
□ 你自己的笔电（运行命令用）
```

## 1. 开火山 ECS（15 分钟）

火山引擎控制台 → 云服务器 ECS → 创建实例：

| 配置项 | 值 |
|---|---|
| 地域 | **华北2（北京）** 或 华东2（上海）—— 跟你的 Coze 同区 |
| 镜像 | Ubuntu 22.04 LTS 64bit |
| 实例规格 | **ecs.g3i.xlarge**（4 vCPU + 16 GB） |
| 存储 | 系统盘 50 GB SSD |
| 公网 IP | **分配 EIP**（按流量计费 1 Mbps 起步）|
| 网络 | 默认 VPC + 默认子网 |
| 安全组 | 创建新组：开 22 / 80 / 443 |
| 登录方式 | 创建密钥对 |
| 实例名 | `bridge-prod-1` |

⚠️ **不要用突发型 t6**——webhook 高峰期会被限流。

成本约 **¥350/月**（含 EIP 1Mbps 包月）。

## 2. 域名 + DNS（15 分钟）

把子域指向 ECS 公网 IP：

```
类型: A
主机记录: bridge
记录值: <你的 ECS 公网 IP>
TTL: 600
```

`dig bridge.your-company.com` 应能解出你的 IP（5-30 分钟生效）。

## 3. 服务器初始化（10 分钟）

SSH 登录后：

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
exit              # 重新登录使 docker 组生效
```

重连验证：

```bash
docker --version
docker compose version
git --version
```

## 4. 拉代码（5 分钟）

```bash
cd ~
git clone https://github.com/jiaodisen-maker/AI.git
cd AI/feishu-coze-bridge
```

## 5. 飞书开放平台配置（30 分钟）

### 5.1 创建应用

[飞书开放平台](https://open.feishu.cn) → 开发者后台 → 应用管理 → 创建自建应用

记下：**App ID** + **App Secret**

### 5.2 申请权限

```
消息：im:message / im:message.group_at_msg / im:chat
文档：drive:drive / docx:document
会议：vc:meeting / vc:meeting.recording
通讯录：contact:user.base / contact:user.email / contact:department
日历：calendar:calendar
多维表格（可选）：bitable:app
审批：approval:instance.callback
邮箱：mail:user_mailbox
```

申请后等管理员审批（1-2 小时）。

### 5.3 配置事件订阅

- 模式：`Webhook`
- 请求 URL：`https://bridge.your-company.com/webhook/feishu`
- 加密方式：自动生成 `Encrypt Key` 和 `Verification Token`

**记下这两个值**，等会要填进 `.env`。

### 5.4 添加事件（**先别保存**，等服务起了再保存）

按 §5.2 申请的权限范围全选 13 类事件（im / drive / vc / contact / calendar / approval / mail）。

## 6. Coze 配置（15 分钟）

### 6.1 拿 PAT

[扣子编程](https://code.coze.cn) → 鉴权 → 个人访问令牌 → 创建

权限：
```
✅ Bot:Read/Write
✅ Workflow:Read/Run
✅ Knowledge:Read/Write
✅ Conversation:Read/Write
✅ Chat
✅ Member:Read/Write
```

有效期 90 天，季度轮换。

### 6.2 抄资源 ID

```
COZE_ENTERPRISE_ID
COZE_PERSONAL_ASSISTANT_BOT_ID
COZE_MEETING_DIGEST_BOT_ID
COZE_SOP_KB_DATASET_ID
COZE_MEETING_TRANSCRIPTS_KB_DATASET_ID
COZE_MEETING_DIGEST_WORKFLOW_ID
```

未建的先在 Coze 后台手动建（空也行），回填 ID。

## 7. 配置 + 启动（30 分钟）

### 7.1 写 .env

```bash
cd ~/AI/feishu-coze-bridge
cp .env.example .env
nano .env
```

填好所有值。**敏感字段先明文，Day 2 迁火山 KMS**。

### 7.2 改域名

```bash
sed -i 's/bridge.your-company.com/bridge.actual-domain.com/' Caddyfile
```

### 7.3 起服务

```bash
docker compose up -d
docker compose ps
```

7 个服务应全 Up：postgres / redis / bridge / 3×worker / token-refresher / backfill / caddy。

### 7.4 看日志

```bash
docker compose logs -f bridge
```

Caddy 自动申请 Let's Encrypt（1-3 分钟）。
然后 `Uvicorn running on http://0.0.0.0:8810`。

### 7.5 自检

```bash
# 健康
curl https://bridge.your-company.com/healthz
# {"ok":true,"ts":...}

# 测 webhook 路径
curl -X POST https://bridge.your-company.com/webhook/feishu \
  -H "Content-Type: application/json" \
  -d '{"type":"url_verification","challenge":"test"}'
# 期望 401（token 不对，但说明路径通了）
```

## 8. 回飞书后台保存事件订阅（5 分钟）

回 §5.3 的事件订阅页 → 点"**保存**"。

飞书会发 `url_verification` 请求 → 你的服务返回 challenge → 飞书显示"配置成功" ✅

不成功看日志：

```bash
docker compose logs bridge | grep webhook
```

| 错误 | 原因 |
|---|---|
| 401 bad token | `FEISHU_VERIFICATION_TOKEN` 不一致 |
| decrypt failed | `FEISHU_ENCRYPT_KEY` 错 |
| connection timeout | 安全组没开 443 / DNS 没生效 |

## 9. 端到端测试（5 分钟）

### 9.1 发消息

飞书任意 chat 发消息，看日志：

```
[bridge] event im.message.receive_v1 enqueued
[worker:w1] processing im.message.receive_v1
```

### 9.2 文档

新建一个 docx：

```
[bridge] event drive.file.created_v1 enqueued
[worker:w1] upload_kb name=untitled.md
```

Coze → KB → 看到新文档 ✅

### 9.3 通讯录

加一个测试员工：

```
[bridge] event contact.user.created_v3 enqueued
[worker:w1] add_coze_member email=test@your-company.com
```

Coze → 成员 → 看到新成员 ✅

## 10. Day 1 完成

进入 `02-go-live-checklist.md` 跑完整验收。

接下来：
- **Day 2**：密钥迁火山 KMS（重要！现在明文 .env 是临时的）
- Day 3-4：监控告警
- Week 2：双实例 + RDS + ALB（`03-production-ha.md`）

---

## 故障速查

| 现象 | 检查 | 解决 |
|---|---|---|
| bridge 一直 restart | `docker compose logs bridge` | .env 缺值 |
| Caddy 证书失败 | `docker compose logs caddy` | DNS 没生效或 80 端口占 |
| 飞书 URL 验证失败 | bridge 日志 | token / encrypt key 不一致 |
| 消息不进队列 | `redis-cli xlen feishu:events` | 看流长度 |
| 队列堆积不消费 | `docker compose ps worker-*` | worker 挂了 |
| Coze API 401 | `docker compose logs worker` | PAT 失效或权限不够 |
