# 运维手册（Runbook）

> 出问题查这里。所有故障场景按"现象 → 诊断 → 修复"组织。

## 1. 服务整体不通

### 1.1 现象
- 飞书事件没进队列
- 用户飞书发消息 bot 不回
- /healthz 不通

### 1.2 诊断（按顺序）

```bash
# 1. ALB 健康检查
火山控制台 → ALB → 后端服务器 → 看 ECS 状态
  - 全 unhealthy → 进 1.3
  - 部分 unhealthy → 该 ECS 进 1.3

# 2. ECS 是否在跑
ssh ubuntu@<ECS IP>
docker compose ps
  - 全 Up → 进 1.4
  - 有 Down/Restarting → 进 1.5

# 3. 网络
curl localhost:8810/healthz       # ECS 内部
curl https://bridge.xxx/healthz   # 公网
```

### 1.3 ECS 全挂

```bash
# 火山控制台看 ECS 状态
- 已停止 → 启动
- CPU 100% → ssh 进去 top 看哪个进程占
- 网络异常 → 检查安全组
```

### 1.4 容器 Up 但服务不响应

```bash
docker compose logs bridge | tail -50
# 看最后是不是卡在某个调用上

# 重启
docker compose restart bridge

# 还不行 → 看 redis / postgres
docker compose logs redis postgres
```

### 1.5 容器 Restart 循环

```bash
docker compose logs bridge | grep -i error

# 常见原因：
# - .env 缺值（KMS 拉不到密钥）
# - postgres 连接失败
# - redis 连接失败
# - PAT 失效（401）
```

---

## 2. 队列堆积

### 2.1 现象
```bash
docker compose exec redis redis-cli xinfo stream feishu:events
# length 持续增长 > 1000
```

### 2.2 诊断

```bash
# worker 在不在跑
docker compose ps | grep worker
# 应该 3 个 Up

# worker 处理速度
docker compose logs worker-1 | tail -100 | grep "processing"
# 没新日志 → worker 卡在某个事件

# 哪个 event_type 堆积
docker compose exec redis redis-cli xrange feishu:events - + COUNT 100 | grep event_type
```

### 2.3 修复

| 原因 | 处理 |
|---|---|
| Coze 限流 429 | 看日志 `coze 429`；调小 worker 并发 / 联系 Coze 提配额 |
| Coze 5xx | 服务侧问题，等 / 减压 |
| 单条事件死循环 | 找出 event_id，手动从 stream 删 |
| worker OOM | 加 ECS 内存 / 加 worker 副本 |
| Postgres 慢 | 看 RDS 监控 |

紧急减压：

```bash
# 加 worker（临时）
docker compose up -d --scale worker-1=3

# 或暂停某类事件入队（在 server.py 加个 emergency switch）
docker compose exec redis redis-cli set emergency_pause:drive.file.created_v1 1 EX 600
```

---

## 3. DLQ 堆积

### 3.1 现象
```bash
docker compose exec redis redis-cli xlen feishu:events:dlq
# > 10
```

### 3.2 诊断

```bash
# 看 DLQ 里都什么 reason
docker compose exec redis redis-cli xrange feishu:events:dlq - + COUNT 50

# 按 reason 分组（最常见的 3 类）
# - "exceeded_retries" → 临时错误重试 5 次仍失败
# - "coze auth fail" → PAT 失效
# - "decrypt failed" → encrypt key 不对（极少）
```

### 3.3 修复

```
按 reason：
  PAT 失效  →  生成新 PAT，KMS 更新，重启 worker
  Coze 持续 5xx → 等 Coze 修复
  Schema 不对 → 翻 logs 找具体 event，反代码 / Coze API 变更
```

DLQ 不是自动重试——人工分析后再决定 requeue or drop。

---

## 4. PAT 失效

### 4.1 现象
- worker 日志 `coze auth fail: 401`
- DLQ 增长

### 4.2 修复

```bash
# 1. 在 Coze 后台撤销旧 PAT
# 2. 生成新 PAT（同样 90 天 + 同样权限）
# 3. 写入 KMS
volcengine kms update-secret --name bridge/coze-pat --value "pat_new"

# 4. 重启 worker（让它从 KMS 拉新值）
docker compose restart worker-1 worker-2 worker-3

# 5. 验证
docker compose logs worker-1 | grep -i "coze" | head
# 应该看到 200 OK
```

**预防**：日历提醒每 80 天换一次 PAT（不要等失效）。

---

## 5. 飞书 token 过期

### 5.1 现象
- feishu_client 调用 401
- token-refresher 日志报错

### 5.2 修复

```bash
# 看 token-refresher 状态
docker compose logs token-refresher | tail -20

# 手动续一次
docker compose exec token-refresher python -m bridge.token_refresher --once

# 还不行 → 检查 FEISHU_APP_ID/SECRET 是不是被改
```

---

## 6. 数据没同步

### 6.1 现象
- 飞书发消息了但 Coze KB / 成员没变化
- 没看到错误，就是"没动"

### 6.2 诊断

```bash
# 1. webhook 收到了吗
docker compose logs bridge | grep "event.*enqueued" | tail -10

# 2. 入队了吗
docker compose exec redis redis-cli xlen feishu:events

# 3. worker 处理了吗
docker compose logs worker-1 worker-2 worker-3 | grep "processing" | tail -10

# 4. translator 返回 None 了吗（事件被忽略）
docker compose logs worker-1 | grep "skip"
# 大量 skip 说明 EVENT_HANDLERS 里这类事件没启用
```

### 6.3 常见原因

| 现象 | 原因 |
|---|---|
| `skip` | translator 里默认禁用了（如 im.message.receive_v1）|
| `blocked` | safety.py PII 拦截 |
| `coze 200 但 Coze 看不到` | 资源 ID 不对（kb_id / bot_id）|
| `dedup` 太多 | event_id 重复（飞书侧偶发，不影响）|

---

## 7. PII 拦截过多 / 误报

### 7.1 现象
- audit/pii_block.log 一天 > 100 条
- 业务方说"应该同步的没同步"

### 7.2 诊断

```bash
# 看拦截原因分布
cat /var/log/feishu-coze-bridge/pii_block.log | jq -r .reason | sort | uniq -c | sort -rn

# 常见误报：
# - 银行卡正则 \d{16,19} 太宽（订单号 / 物流单号被误抓）
# - 邮箱正则可能抓内部 @your-company.com 域名
```

### 7.3 修复

调 `bridge/safety.py`：

```python
# 银行卡加上下文（前后必须有"卡号"等关键词）
"bank_card": re.compile(r"(?:银行卡|卡号)\D*(\d{16,19})\b"),

# 邮箱排除自家域名（认为是内部，不算 PII）
INTERNAL_DOMAINS = {"your-company.com"}
def detect_pii(text):
    hits = ...
    # filter out internal emails
```

调完跑单测：

```bash
docker compose exec worker-1 python -m pytest tests/test_safety.py
```

部署：

```bash
docker compose build worker-1 worker-2 worker-3
docker compose up -d
```

---

## 8. 飞书事件订阅"配置失败"

### 8.1 配置时

```
现象：飞书后台保存事件订阅 → 提示"URL 验证失败"
```

诊断：

```bash
# 1. URL 公网通吗
curl https://bridge.your-company.com/healthz

# 2. ALB / Caddy 转到 bridge 容器吗
curl http://localhost:8810/healthz   # ECS 内

# 3. token / encrypt key 一致吗
docker compose exec bridge env | grep FEISHU_
```

修复：让飞书 token / encrypt key 跟 .env / KMS 一致 → 保存。

### 8.2 订阅几天后偶发"事件投递失败"

飞书后台事件订阅有"调用记录"页 → 看失败的请求和响应。

| 响应 | 原因 | 处理 |
|---|---|---|
| 5xx | 服务过载 | 加 worker / ECS |
| 超时 (5s) | 服务慢 | server.py 应在 200ms 内 ACK；查为啥慢 |
| 401 | token 不一致 | 检查 KMS |

---

## 9. 季度运维任务

```
□ PAT 轮换（每 80 天，不等失效）
□ KMS 凭据 rotate（年度）
□ 备份恢复演练（季度）
□ ALB 切流量演练（季度）
□ DLQ 清理（月度）
□ 升级依赖（pip update + 测试，月度）
□ 火山 ECS 系统补丁（月度）
□ Coze API 兼容性 review（每月看 Coze changelog）
```

---

## 10. 紧急联系人

```
□ 飞书超管：<姓名> <飞书 @>
□ Coze 商务经理：<联系方式>
□ 火山引擎 TAM：<联系方式>
□ 公司 DPO（数据合规）：<姓名>
□ 工程师 5（值班主）：<联系方式>
□ 工程师 1（架构师，升级到他）：<联系方式>
□ 你（产品负责人）：<联系方式>
```

---

## 附录：常用 redis-cli 命令

```bash
# 看 stream 状态
redis-cli xinfo stream feishu:events

# 看 consumer group lag
redis-cli xinfo groups feishu:events

# 看最近 10 条事件
redis-cli xrevrange feishu:events + - COUNT 10

# 删某条事件（用 stream id）
redis-cli xdel feishu:events 1234567890123-0

# 看 DLQ
redis-cli xrange feishu:events:dlq - +

# 清空 DLQ（小心！只在确认无价值时）
redis-cli del feishu:events:dlq
```
