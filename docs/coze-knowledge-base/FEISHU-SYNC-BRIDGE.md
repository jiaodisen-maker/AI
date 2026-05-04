# 飞书全量实时同步到 Coze · 完整工程方案

> 配合 `FEISHU-INTEGRATION.md` + `DATA-SECURITY.md` + `AI-GATEWAY-SETUP.md` 食用。
> 本文是**工程级实施方案**，目标读者：工程师 5 + 工程师 7。
> 信息源：飞书 Open Platform 文档 + Coze OpenAPI 195 页（`raw/coze_cn/developer_guides/`）。

## 0. 严酷真相

读 `cozespace/using-coze-in-feishu.md` 后我之前以为 Coze "原生支持飞书"。再读细节发现**真相分两面**：

| | 真相 |
|---|---|
| ✅ Coze **能调用**飞书 | 通过插件主动读消息/文档/多维表格/日历/任务 |
| ❌ Coze **不能"听"**飞书事件 | 飞书的 message/edit/approval 等事件**不会主动推到 Coze** |

要做"飞书全部信息**实时**进 Coze"，**必须**自建 Bridge。
我之前写的 `memory-integration/sources/feishu/` 80% 代码可以**改造复用**——只是把"写入后端"从 GBrain 换成 Coze OpenAPI。

---

## 1. 总体架构

```
┌──────────────────────────────────────────────────────────────┐
│            飞书 Open Platform                                  │
│   消息  文档  多维表格  日历  任务  会议  通讯录  审批  邮箱  │
└──────────┬─────────────────────────────────────┬─────────────┘
           │ Webhook 事件订阅                   │ 长连接（无公网备选）
           ▼                                     ▼
   ┌──────────────────────────────────────────────┐
   │     Feishu→Coze Bridge（自建服务）            │
   │  - HTTPS Webhook 接收（FastAPI）             │
   │  - 验签 + 解密 + event_id 去重               │
   │  - 入 Redis Streams 队列                     │
   └──────────┬───────────────────────────────────┘
              │
              ▼
   ┌──────────────────────────────────────────────┐
   │     Worker 池（事件路由 + 翻译）              │
   │  消息事件 → 调 Coze chat API 触发 bot         │
   │  文档事件 → 调 Coze KB API 增删改文件          │
   │  多维表格 → 同步到飞书多维表格集成            │
   │  通讯录   → 调 Coze 成员管理 API              │
   │  审批     → 调对应 bot 工作流                 │
   │  会议     → 拉转写 + KB 写入                  │
   │  邮箱     → 客户档案数据库                    │
   └──────────┬───────────────────────────────────┘
              │
              ▼
   ┌──────────────────────────────────────────────┐
   │             Coze 企业旗舰版                    │
   │  bot / workflow / 知识库 / 数据库 / 成员      │
   └──────────────────────────────────────────────┘
              │
              ▲ 失败重试/回填   监控告警
              │
   ┌──────────────────────────────────────────────┐
   │  Postgres（审计）+ Prometheus + 飞书告警机器人  │
   └──────────────────────────────────────────────┘
```

---

## 2. 13 类飞书事件 → Coze 端点映射表

> 每行对应一个飞书事件类型 + 对应的 Coze 写入策略 + 实时性 SLO。

| # | 飞书事件 | 同步对象 | Coze 端点 | SLO p99 | 频率 |
|---|---|---|---|---|---|
| 1 | `im.message.receive_v1`（私聊）| 消息 | **POST /v3/chat**（触发 bot）| < 1s | 高 |
| 2 | `im.message.receive_v1`（群@bot）| 消息 | **POST /v3/chat** | < 1s | 中 |
| 3 | `drive.file.created_v1`（新建文档）| 知识库 | **POST /v1/datasets/:id/documents**（create_knowledge_files）| < 5min | 低 |
| 4 | `drive.file.edit_v1`（编辑文档）| 知识库 | **POST /v1/datasets/:id/documents/:fid/update**（modify_knowledge_files）| < 60s | 中 |
| 5 | `drive.file.deleted_v1`（删除文档）| 知识库 | **DELETE /v1/datasets/:id/documents/:fid** | < 60s | 低 |
| 6 | `bitable.record.changed_v1`（多维表格变更）| 业务数据库 | 飞书多维表格集成（Coze 工作流）| < 5s | 高 |
| 7 | `calendar.calendar.event.changed_v4`（日程变更）| 日程提醒 | 触发提醒 bot | < 30s | 中 |
| 8 | `approval.instance.approved_v4`/`rejected_v4`| 审批 | 触发对应 bot | < 5s | 中 |
| 9 | `vc.meeting.recording_ready_v1`（录音就绪）| 会议纪要 | 拉转写 → KB + Bitable | < 5min | 低 |
| 10 | `contact.user.created_v3`（员工入职）| Coze 成员 | **POST /v1/enterprises/:eid/members**（add_enterprise_member）| < 1h | 低 |
| 11 | `contact.user.updated_v3`（员工变更）| Coze 成员 | **PUT /v1/enterprises/:eid/members/:uid** | < 1h | 低 |
| 12 | `contact.user.deleted_v3`（离职）| Coze 成员 | **DELETE /v1/enterprises/:eid/members/:uid** + 删长期记忆 | < 24h | 低 |
| 13 | `contact.department.updated_v3`（部门变更）| Coze 工作空间 | 调整工作空间成员 | < 24h | 低 |
| 14 | `wiki.space_node_changed_v1`（知识空间变更）| 知识库 | 增删改文档 | < 5min | 低 |
| 15 | `mail.user_mailbox.message.received_v1`（收邮件）| 客户档案 | 写入 Bitable + 触发分诊 bot | < 1min | 中 |

---

## 3. Bridge 服务的 6 大组件

### 3.1 Webhook 接收（FastAPI，已有 80% 代码）

复用 `memory-integration/sources/feishu/server.py`，只需要改 worker 的写入目标：

```
飞书事件 POST → Bridge HTTPS 入口
  ↓
验签（HMAC-SHA256，用 verification_token）
  ↓
解密（如开 encrypt_key，AES-256-CBC）
  ↓
URL 验证（首次配置返回 challenge）
  ↓
去重（event_id 在 Redis SETNX 1h）
  ↓
立即 ACK 200 OK（必须 < 200ms，否则飞书重投）
  ↓
入 Redis Streams 队列异步处理
```

### 3.2 长连接备选（无公网时）

复用 `long_connection.py`：用 `lark-oapi` 的 WebSocket 客户端，自动重连。
适合**内网部署 / 没有公网 HTTPS**的场景。

### 3.3 队列（Redis Streams）

```python
# queue 结构
feishu:events           # 主队列
feishu:events:dlq       # 死信队列（5 次重试失败入此）
feishu:events:cg        # consumer group: 5 个 worker 并发
```

**为什么用 Redis Streams**：
- 消费者组（consumer group）支持 ACK 机制
- 失败可重投
- 持久化
- 简单（不用 Kafka）

### 3.4 事件翻译器

每类飞书事件 → 对应 Coze 端点的具体翻译：

```python
# translator.py（伪代码）
EVENT_HANDLERS = {
    "im.message.receive_v1":               translate_message,
    "drive.file.created_v1":               translate_doc_created,
    "drive.file.edit_v1":                  translate_doc_edited,
    "drive.file.deleted_v1":               translate_doc_deleted,
    "bitable.record.changed_v1":           translate_bitable_change,
    "calendar.calendar.event.changed_v4":  translate_calendar,
    "approval.instance.approved_v4":       translate_approval,
    "approval.instance.rejected_v4":       translate_approval,
    "vc.meeting.recording_ready_v1":       translate_meeting_recording,
    "contact.user.created_v3":             translate_user_created,
    "contact.user.updated_v3":             translate_user_updated,
    "contact.user.deleted_v3":             translate_user_deleted,
    "contact.department.updated_v3":       translate_department,
    "wiki.space_node_changed_v1":          translate_wiki_change,
    "mail.user_mailbox.message.received_v1": translate_mail,
}
```

### 3.5 Coze OpenAPI 客户端（核心新代码）

```python
# coze_client.py
import httpx
import os
from typing import Optional

class CozeClient:
    """Coze 企业旗舰版 OpenAPI 客户端。
    
    PAT 走火山 KMS，不写在代码里。
    """
    BASE = "https://api.coze.cn"
    
    def __init__(self, pat: str):
        self._cli = httpx.AsyncClient(
            base_url=self.BASE,
            headers={"Authorization": f"Bearer {pat}"},
            timeout=30,
        )
    
    # === 知识库 ===
    async def upload_doc_to_kb(self, dataset_id: str, name: str,
                                content: bytes | str,
                                source_type: str = "local") -> dict:
        """source_type: local|online_web."""
        if source_type == "local":
            import base64
            b64 = base64.b64encode(content if isinstance(content, bytes)
                                   else content.encode()).decode()
            payload = {
                "dataset_id": dataset_id,
                "document_bases": [{
                    "name": name,
                    "source_info": {
                        "file_base64": b64,
                        "file_type": name.rsplit(".", 1)[-1],
                    },
                }],
            }
        else:
            payload = {
                "dataset_id": dataset_id,
                "document_bases": [{
                    "name": name,
                    "source_info": {"web_url": content, "document_source": 1},
                }],
            }
        r = await self._cli.post("/v1/datasets/{dataset_id}/documents".format(
            dataset_id=dataset_id), json=payload)
        r.raise_for_status()
        return r.json()
    
    async def update_doc_in_kb(self, document_id: str,
                                name: Optional[str] = None,
                                update_rule: Optional[dict] = None) -> dict:
        payload = {}
        if name: payload["document_name"] = name
        if update_rule: payload["update_rule"] = update_rule
        r = await self._cli.post(f"/v1/datasets/documents/{document_id}/update",
                                  json=payload)
        r.raise_for_status()
        return r.json()
    
    async def delete_doc_in_kb(self, document_id: str) -> dict:
        r = await self._cli.delete(f"/v1/datasets/documents/{document_id}")
        r.raise_for_status()
        return r.json()
    
    # === 触发 bot（chat） ===
    async def trigger_bot(self, bot_id: str, user_id: str,
                          message: str, conversation_id: str = "",
                          stream: bool = False) -> dict:
        """通过 chat API 触发 bot 处理一条消息。
        
        Coze 的 bot 收到 chat 请求后会内部走 workflow。
        """
        payload = {
            "bot_id": bot_id,
            "user_id": user_id,
            "additional_messages": [{
                "role": "user",
                "type": "question",
                "content": message,
                "content_type": "text",
            }],
            "stream": stream,
        }
        if conversation_id:
            payload["conversation_id"] = conversation_id
        r = await self._cli.post("/v3/chat", json=payload)
        r.raise_for_status()
        return r.json()
    
    # === 成员管理 ===
    async def add_member(self, enterprise_id: str, user_name: str,
                          email: str, role: str = "member") -> dict:
        payload = {
            "enterprise_id": enterprise_id,
            "user_name": user_name,
            "email": email,
            "role": role,
        }
        r = await self._cli.post(
            f"/v1/enterprises/{enterprise_id}/members", json=payload)
        r.raise_for_status()
        return r.json()
    
    async def remove_member(self, enterprise_id: str, user_id: str) -> dict:
        r = await self._cli.delete(
            f"/v1/enterprises/{enterprise_id}/members/{user_id}")
        r.raise_for_status()
        return r.json()
    
    # === 工作流 ===
    async def trigger_workflow(self, workflow_id: str,
                                parameters: dict) -> dict:
        """直接调起工作流，不通过 bot。"""
        payload = {
            "workflow_id": workflow_id,
            "parameters": parameters,
        }
        r = await self._cli.post("/v1/workflow/run", json=payload)
        r.raise_for_status()
        return r.json()
    
    async def close(self):
        await self._cli.aclose()
```

> ⚠️ **API 路径要以 `docs/coze-knowledge-base/raw/coze_cn/developer_guides/` 为准** —— 我列的是常见模式，工程师 5 实现时按真实 API 校对。

### 3.6 失败处理 + 回填

```python
# worker.py (核心 loop)
async def process(event: dict):
    payload = translate(event)            # 翻译
    if not payload:
        return                             # 不是要同步的事件
    
    # 安全过滤
    if pii_detected(payload) and payload.get("target_is_overseas_model"):
        await audit_log("PII_BLOCK", event)
        return
    
    # 调 Coze
    try:
        await dispatch_to_coze(payload)
    except CozeRateLimitError:
        # 速率限制 → 退避重试
        raise RetryableError(retry_after=60)
    except CozeAPIError as e:
        # 真错误 → 进 DLQ
        raise PermanentError(e)


async def loop(consumer: str):
    async for msg_id, event in consume(consumer):
        for attempt in range(MAX_RETRIES):
            try:
                await process(event)
                await ack(msg_id)
                break
            except RetryableError as e:
                await asyncio.sleep(e.retry_after)
                continue
            except PermanentError as e:
                await to_dlq(event, str(e))
                await ack(msg_id)
                break
            except Exception as e:
                wait = BACKOFF * (2 ** attempt)
                logger.warning(f"transient err {e}, wait {wait}s")
                await asyncio.sleep(wait)
        else:
            await to_dlq(event, "exceeded retries")
            await ack(msg_id)
```

**回填**（每天凌晨 + 启动时）：

```python
# backfill.py
async def daily_backfill():
    """飞书侧无 webhook 全量 API，要按数据源各拉一份。
    
    比对 Coze 侧已有数据，缺失的补；多余的删。
    """
    # 1. 拉飞书所有 chat
    feishu_chats = await feishu_api.list_all_chats()
    
    # 2. 拉飞书 24 小时内的消息（API 限制）
    since = utcnow() - timedelta(hours=24)
    for chat in feishu_chats:
        msgs = await feishu_api.list_messages(chat.id, since)
        for msg in msgs:
            ev = wrap_as_event(msg)
            if not await seen_before(ev["event_id"]):
                await enqueue(ev)
    
    # 3. 拉飞书最近变更的文档
    docs = await feishu_api.list_recent_docs(since)
    for doc in docs:
        ev = wrap_as_event(doc)
        if not await seen_before(ev["event_id"]):
            await enqueue(ev)
    
    # 4. 拉通讯录 diff
    feishu_users = await feishu_api.list_all_users()
    coze_members = await coze.list_members()
    for u in feishu_users:
        if u.user_id not in {m.id for m in coze_members}:
            await enqueue({"event_type": "contact.user.created_v3",
                            "user": u})
    # ... 同理处理离职 / 部门变更
```

---

## 4. 13 类事件的同步细节

### 4.1 私聊消息 → 触发 bot（事件 #1）

```python
async def translate_message(event: dict) -> dict:
    msg = event["event"]["message"]
    sender = event["event"]["sender"]
    
    chat_type = msg["chat_type"]
    if chat_type != "p2p":
        return None     # 群聊用单独的 handler
    
    text = extract_text(msg)
    sender_id = sender["sender_id"]["open_id"]
    
    # 路由：私聊触发"个人助手 bot"
    return {
        "action": "trigger_bot",
        "bot_id": COZE_PERSONAL_ASSISTANT_BOT_ID,
        "user_id": sender_id,            # 用 open_id 作 Coze user_id
        "message": text,
        "conversation_id": f"feishu-p2p-{sender_id}",
    }


async def dispatch_to_coze(payload):
    if payload["action"] == "trigger_bot":
        return await coze.trigger_bot(
            bot_id=payload["bot_id"],
            user_id=payload["user_id"],
            message=payload["message"],
            conversation_id=payload["conversation_id"],
        )
```

⚠️ **注意**：扣子发布到飞书的 bot 已经能直接处理飞书消息——这种情况**不要再走 Bridge**！否则双重处理。
**Bridge 只负责**："**飞书事件 → Coze 知识库/数据库/成员**"这种**数据**同步，**不**做"飞书消息 → bot"（那是 Coze 自己的能力）。

### 4.2 群聊@bot → 触发 bot（事件 #2）

跟 #1 类似，但 **Coze 发布到飞书后会自动处理**——Bridge 不参与。

### 4.3 文档新建 → 知识库（事件 #3）

```python
async def translate_doc_created(event: dict) -> dict:
    body = event["event"]
    file_token = body["file_token"]
    file_type = body["file_type"]      # docx / sheet / mindnote / ...
    
    # 仅同步特定类型 + 公开/部分公开权限的文档
    if file_type not in ("docx", "doc"):
        return None
    
    if not is_doc_shareable_to_kb(file_token):
        return None         # 涉密文档不进 KB
    
    # 拉飞书文档正文
    content = await feishu_api.get_docx_raw_content(file_token)
    
    # 决定进哪个知识库（按文档所在文件夹/标签判断）
    dataset_id = decide_kb_for_doc(body)
    if not dataset_id:
        return None
    
    return {
        "action": "upload_kb",
        "dataset_id": dataset_id,
        "name": body["file_name"],
        "content": content,
        "feishu_token": file_token,        # 留在 metadata 用于以后增量
    }
```

⚠️ **关键 schema 设计**：在 Coze 知识库的文档 metadata 里留 `feishu_token`，方便后续 edit/delete 同步。

### 4.4 文档编辑 → 知识库更新（事件 #4）

```python
async def translate_doc_edited(event: dict) -> dict:
    file_token = event["event"]["file_token"]
    
    # 在 Coze 找 metadata.feishu_token == file_token 的文档
    doc = await find_coze_doc_by_feishu_token(file_token)
    if not doc:
        # KB 里没这文档（可能是当时未同步）→ 走 created 流程
        return await translate_doc_created(event)
    
    return {
        "action": "update_kb",
        "document_id": doc.id,
        "name": event["event"].get("file_name"),
        "update_rule": {
            "update_type": 1,    # 1=更新内容
            # 更新内容需重新 base64 上传
        },
    }
```

⚠️ **注意**：Coze 的 `modify_knowledge_files` API 仅支持改名/改解析配置；**改内容要先删后建**或用专门的"重新解析"接口（取决于 Coze 版本，工程师 5 验证）。

**实用做法**：
- 文档编辑频繁 → debounce 60 秒（同 file_token 在 60 秒内多次编辑只同步最后一次）
- 大文档 → 异步重建（用户不感知）
- 留旧版本备份 30 天

### 4.5 多维表格变更 → 业务数据库（事件 #6）

**架构选择**：
- **方案 A：Bridge 同步到 Coze 数据库** —— 双写问题，不推荐
- ✅ **方案 B：直接用飞书多维表格当 Coze 数据库**（看 `FEISHU-INTEGRATION.md §4`）—— 推荐

如果选 B，**Bridge 不需要处理这类事件**——Coze 工作流直接通过"飞书多维表格集成"读最新数据。

如果选 A：

```python
async def translate_bitable_change(event: dict) -> dict:
    body = event["event"]
    table_id = body["table_id"]
    record_id = body["record_id"]
    action = body["action_type"]    # create / update / delete
    
    # 查表名 → 决定同步到 Coze 哪个数据库
    coze_db = MAPPING.get(table_id)
    if not coze_db:
        return None
    
    # 拉最新记录
    record = await feishu_api.bitable_get_record(table_id, record_id)
    
    return {
        "action": "sync_db_record",
        "coze_db_id": coze_db.id,
        "record_id": record_id,
        "fields": record.fields,
        "op": action,
    }
```

⚠️ **Coze 数据库 OpenAPI 写入限制**：目前 Coze 数据库**主要通过工作流操作**，**OpenAPI 直接写入支持有限**。建议用方案 B。

### 4.6 通讯录变更 → 成员同步（事件 #10-#13）

```python
async def translate_user_created(event: dict) -> dict:
    user = event["event"]["object"]
    return {
        "action": "add_member",
        "enterprise_id": COZE_ENTERPRISE_ID,
        "user_name": email_prefix(user["email"]),
        "email": user["email"],
        "role": map_department_to_role(user["department_ids"]),
    }


async def translate_user_deleted(event: dict) -> dict:
    user = event["event"]["object"]
    return {
        "action": "remove_member_full_cleanup",
        "enterprise_id": COZE_ENTERPRISE_ID,
        "user_id": email_prefix(user["email"]),
        # 离职 30 天内删长期记忆（PIPL 47 条）
        "schedule_memory_cleanup_at": utcnow() + timedelta(days=30),
    }


async def dispatch_to_coze(payload):
    if payload["action"] == "remove_member_full_cleanup":
        # 1. 撤销 Coze 成员权限
        await coze.remove_member(payload["enterprise_id"], payload["user_id"])
        # 2. 排程 30 天后删长期记忆
        await schedule_task(
            "delete_user_memory",
            run_at=payload["schedule_memory_cleanup_at"],
            kwargs={"user_id": payload["user_id"]},
        )
```

### 4.7 会议录音就绪 → 知识库 + 数据库（事件 #9）

```python
async def translate_meeting_recording(event: dict) -> dict:
    meeting_id = event["event"]["meeting"]["id"]
    
    # 拉转写
    transcript = await feishu_api.vc_get_transcript(meeting_id)
    if not transcript:
        return None     # 还没准备好
    
    # 拉与会人
    attendees = await feishu_api.vc_list_attendees(meeting_id)
    
    return {
        "action": "process_meeting",
        "meeting_id": meeting_id,
        "transcript": transcript,
        "attendees": [a.user_id for a in attendees],
    }


async def dispatch_to_coze(payload):
    if payload["action"] == "process_meeting":
        # 1. 转写存进 KB（仅与会人能读）
        await coze.upload_doc_to_kb(
            dataset_id=COZE_MEETING_TRANSCRIPTS_KB,
            name=f"meeting_{payload['meeting_id']}.md",
            content=payload["transcript"],
            source_type="local",
        )
        # 2. 触发"会议消化" workflow，自动出摘要 + 行动项
        await coze.trigger_workflow(
            workflow_id=COZE_MEETING_DIGEST_WORKFLOW,
            parameters={
                "transcript": payload["transcript"],
                "attendees": payload["attendees"],
            },
        )
```

### 4.8 邮箱收件 → 客户档案（事件 #15）

```python
async def translate_mail(event: dict) -> dict:
    mail = event["event"]["message"]
    
    # 仅同步特定邮箱（销售公账等）
    if mail["mailbox_address"] != "sales@your-company.com":
        return None
    
    # 提取发件人 → 查 CRM 是否是已知客户
    from_email = mail["from"]["address"]
    customer = await crm_api.find_customer_by_email(from_email)
    
    return {
        "action": "log_customer_interaction",
        "customer_id": customer.id if customer else None,
        "from": from_email,
        "subject": mail["subject"],
        "body": mail["body"],
        "received_at": mail["timestamp"],
    }
```

### 4.9 审批 → 触发 bot（事件 #8）

适合"自动化业务流"——审批通过后调用 bot 做后续动作（如：销售折扣申请通过 → 通知客户）。

```python
async def translate_approval(event: dict) -> dict:
    body = event["event"]
    approval_code = body["approval_code"]
    instance_code = body["instance_code"]
    status = body["status"]              # APPROVED / REJECTED
    
    # 按审批类型路由到不同 bot
    bot_id = APPROVAL_BOT_MAPPING.get(approval_code)
    if not bot_id:
        return None
    
    # 拉详情
    instance = await feishu_api.approval_get_instance(instance_code)
    
    return {
        "action": "trigger_bot",
        "bot_id": bot_id,
        "user_id": instance.user_id,
        "message": f"审批 {status}: {instance.summary}",
        "metadata": {"instance_code": instance_code, "status": status},
    }
```

---

## 5. Coze OpenAPI 端点速查

来自 195 页 `developer_guides/`：

| Coze API | 路径 | 用于哪类同步 |
|---|---|---|
| `create_knowledge_files` | POST `/v1/datasets/:id/documents` | 文档新建 |
| `modify_knowledge_files` | POST `/v1/datasets/documents/:fid/update` | 文档编辑 |
| `delete_knowledge_files` | DELETE `/v1/datasets/documents/:fid` | 文档删除 |
| `list_knowledge_files` | GET `/v1/datasets/:id/documents` | 同步前查重 |
| `chat_v3` | POST `/v3/chat` | 触发 bot |
| `add_enterprise_member` | POST `/v1/enterprises/:eid/members` | 员工入职 |
| `remove_enterprise_member` | DELETE `/v1/enterprises/:eid/members/:uid` | 员工离职 |
| `add_space_member` | POST `/v1/workspaces/:wid/members` | 部门变更 |
| `create_message` | POST `/v3/conversations/:cid/messages` | 主动发消息 |
| `workflow_run` | POST `/v1/workflow/run` | 直接调起工作流 |

⚠️ **限流**：企业旗舰版整体 12,000 RPM —— Bridge **必须**按事件类型分配配额（消息事件 70% / 文档 20% / 其他 10%），不要让某类事件吃光。

⚠️ **PAT 走火山 KMS** —— Bridge 启动时拉密钥，不写在 yaml/env 里。

---

## 6. 实时性 SLO

| 指标 | 目标 | 度量方法 |
|---|---|---|
| Webhook 入口 → ACK | < 200ms | Caddy access log |
| 入队延迟 | < 50ms | Bridge → Redis xadd |
| 队列等待（p50）| < 1s | Redis Streams lag |
| 翻译 + Coze 调用（消息）| < 800ms | Worker trace |
| 翻译 + Coze 调用（文档）| < 30s | 文档大小决定 |
| **端到端（p99，消息）**| **< 2s** | 飞书 send → Coze 收到 chat 请求 |
| **端到端（p99，文档）**| **< 60s** | 飞书 edit → KB 更新可查 |
| 失败 → DLQ | 5 次重试后 | 监控 |
| 回填扫描频率 | 每天凌晨 + 启动 | cron |

---

## 7. 失败处理 + 回填

### 7.1 三级失败分类

| 类型 | 处理 | 例 |
|---|---|---|
| **临时错误** | 指数退避重试（5 次）| 网络抖动、Coze 5xx、限流 |
| **永久错误** | 进 DLQ + 告警 | 验签错、字段格式错、PAT 失效 |
| **需要人审** | 进 DLQ + 飞书审核 | 文档大小超限、PII 拦截 |

### 7.2 回填策略

```
触发时机：
  - 启动时（所有 worker ready 后跑一次）
  - 每天凌晨 03:00 cron
  - 手动触发（管理员命令）
  - DLQ 超过阈值时自动触发

回填范围：
  - 消息：过去 24h（飞书 API 限制）
  - 文档：按修改时间 since cursor
  - 多维表格：按变更时间 since cursor
  - 通讯录：全量 diff
  - 邮箱：过去 24h

策略：
  1. 拉飞书侧 since cursor 的所有变更
  2. 包成事件，进队列（idempotency 自动去重）
  3. 处理完更新 cursor
```

---

## 8. 数据安全过滤（哪些不同步）

按 `DATA-SECURITY.md` 数据分级：

```python
def should_sync(event: dict) -> bool:
    et = event["header"]["event_type"]
    
    # L4 极敏感不进 Coze
    if et == "im.message.receive_v1":
        text = extract_text(event)
        if contains_medical_record(text):
            return False                     # 病历/处方不同步
        if contains_id_card(text):
            audit_pii(event)                 # 留痕但不同步
            return False
    
    if et == "drive.file.created_v1":
        labels = event["event"].get("labels", [])
        if "极敏感" in labels or "法务" in labels:
            return False
    
    if et == "approval.instance.*":
        if event["event"]["approval_code"] in HR_INTERNAL_APPROVALS:
            return False                      # HR 内部审批不进 bot
    
    return True
```

**所有过滤决策都进审计**——出问题能查为什么没同步。

---

## 9. 监控告警（飞书机器人）

关键指标：

| 指标 | 阈值 | 告警通道 |
|---|---|---|
| Webhook 错误率 | > 1% | 飞书 @值班 |
| 队列长度 | > 1000 | 飞书 @值班 |
| DLQ 增长 | > 10/h | 飞书 @值班 |
| Coze API 错误率 | > 5% | 飞书 @值班 |
| PAT 即将失效 | < 24h | 飞书 + 邮件 |
| 端到端延迟 p99 | > 5s | 飞书 |
| PII 拦截事件 | 任何 | 飞书 + 留痕 |
| 回填失败 | 任何 | 飞书 |

---

## 10. 部署

### 10.1 资源

```
1 台 ECS 4C8G   webhook + worker（PoC）→ 升级到 2 台
1 火山 RDS PG    审计日志（共用 AI Gateway 的）
1 火山 Redis     队列（独立实例 1C2G 即可）
1 域名 + HTTPS   bridge.your-company.com
```

### 10.2 docker-compose.yml 骨架

```yaml
version: "3.9"

services:
  bridge:
    build: ./feishu-coze-bridge
    env_file: .env
    ports:
      - "127.0.0.1:8810:8810"
    depends_on: [redis, postgres]
    deploy:
      restart_policy: { condition: on-failure }
      replicas: 2

  worker:
    build: ./feishu-coze-bridge
    command: ["python", "-m", "bridge.worker", "--consumer", "${HOSTNAME}"]
    env_file: .env
    depends_on: [bridge]
    deploy:
      replicas: 5     # 5 个并发消费者

  token-refresher:
    build: ./feishu-coze-bridge
    command: ["python", "-m", "bridge.token_refresher", "--cron"]
    env_file: .env

  backfill:
    build: ./feishu-coze-bridge
    command: ["python", "-m", "bridge.backfill", "--cron"]
    env_file: .env

  redis:
    image: redis:7-alpine
    volumes: [redis_data:/data]

  caddy:
    image: caddy:2-alpine
    ports: ["443:443", "80:80"]
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro

volumes:
  redis_data:
```

### 10.3 4 周交付路线

| Week | 任务 | 工程师 |
|---|---|---|
| 1 | 飞书开放平台建应用 + Webhook + 验签去重入队 | 5 |
| 1 | Coze OpenAPI 客户端 + PAT 走火山 KMS | 7 |
| 2 | 通讯录全量同步 + 自动入职/离职 | 5 |
| 2 | 文档同步：飞书云文档 → Coze KB（含编辑/删除）| 5 |
| 3 | 会议纪要消化（拉转写 → KB + 触发摘要 workflow）| 5 |
| 3 | 审批触发 bot + 邮箱客户档案 | 7 |
| 4 | 回填守护进程 + 数据安全过滤 + 监控 + 告警 | 6 |
| 4 | 故障演练 + 文档化 SOP | 6 + 你 |

---

## 11. 验收清单（30 项）

### 入口
```
□ 飞书开放平台应用建好，权限申请齐
□ Webhook 验签 + 解密通过
□ event_id 去重在 Redis 工作
□ 200 ms 内 ACK
□ URL 验证通（飞书后台测试）
□ 长连接备选可启动（无公网时）
```

### 同步链路
```
□ 13 类事件全部有 translator
□ 不在 13 类的事件优雅丢弃 + 留日志
□ 消息触发 bot p99 < 2s（实测）
□ 文档同步到 KB p99 < 60s（实测）
□ 通讯录全量同步通（800 人 < 1h）
□ 会议纪要消化通（含拉转写 + KB + workflow）
```

### 失败处理
```
□ 5 次重试 + DLQ 工作正常
□ DLQ 内容能在飞书后台查看
□ 启动回填跑通
□ 每天凌晨回填跑
□ 回填的 idempotency 不重复处理
```

### 数据安全
```
□ L4 数据（医疗/身份证/病历）拦截不同步
□ 拦截留审计
□ PAT 走火山 KMS（不在 yaml）
□ Bridge 通信 TLS 1.3
□ 离职员工 30 天后长期记忆自动删
```

### 监控
```
□ 关键指标进 Prometheus
□ Grafana 仪表盘
□ 8 类告警都接入飞书机器人
□ DPO 看板（PII 拦截事件）
```

### 运维
```
□ 双实例 + 故障切换演练
□ 模型 / Coze 故障时降级（不阻塞飞书）
□ Bridge 全停时飞书 webhook 不丢（飞书重投 + 启动回填）
□ 文档化 SOP（接手新员工能 1 天上手）
```

---

## 12. 跟之前 `memory-integration/sources/feishu/` 的关系

我会话早期写过一套 `memory-integration/sources/feishu/`，**80% 代码可以直接复用**：

| 文件 | 可复用？ | 改造点 |
|---|---|---|
| `server.py`（Webhook 接收）| ✅ 直接复用 | 改 dispatch 目标 |
| `long_connection.py` | ✅ 直接复用 | 同上 |
| `idempotency.py` | ✅ 直接复用 | - |
| `queue.py` | ✅ 直接复用 | - |
| `token_refresher.py` | ✅ 直接复用 | - |
| `translator.py` | ⚠️ 改造 | 翻译目标从 memory_router 改为 Coze OpenAPI |
| `worker.py` | ⚠️ 改造 | 写入端从 GBrain/Hindsight 改为 CozeClient |
| `backfill.py` | ⚠️ 改造 | 同上 |

**建议**：直接把 `memory-integration/sources/feishu/` 改名为 `feishu-coze-bridge/`，重写 `worker.py` 和 `translator.py`，其他保留。

---

## 13. 引用源

**Coze OpenAPI**（`raw/coze_cn/developer_guides/`）：
- `authentication.md` —— 鉴权方式 + PAT 用法
- `create_knowledge_files.md` —— 知识库上传
- `modify_knowledge_files.md` / `delete_knowledge_files.md`
- `list_knowledge_files.md`
- `chat_v3.md` —— 触发 bot
- `add_enterprise_member.md` / `remove_enterprise_member.md`
- `add_space_member.md` / `remove_space_member.md`
- `create_workspace.md` / `create_organization.md`
- `workflow_resume.md` / `get_workflow_info.md`

**飞书 Open Platform**：
- 事件订阅：https://open.feishu.cn/document/server-docs/event-subscription-guide
- 长连接 SDK：lark-oapi-server-sdk
- 通讯录 API
- 多维表格 API
- 文档 API
- 日历 API
- 会议 API
- 邮箱 API

**之前已写的代码**：
- `memory-integration/sources/feishu/*.py`（80% 可复用）
