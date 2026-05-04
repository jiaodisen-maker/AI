"""飞书事件 → Coze 动作（dict）的纯函数翻译器。

输出统一为 `Action` dict：
  {
    "kind": "trigger_bot" | "upload_kb" | "update_doc" | ... ,
    "args": {...},
    "needs_external_fetch": ["docx_content" | "vc_transcript" | ...],
  }

worker.py 拿到 Action 后再调 coze_client / feishu_client。

不在这里调任何外部服务（保持纯函数 + 易测）。
"""
from __future__ import annotations

import json
from typing import Callable

from .config import COZE


# ============================================================
# 1. 消息（私聊）触发个人助手 bot
# ============================================================

def _msg(event: dict) -> dict | None:
    body = event.get("event", {})
    msg = body.get("message", {})
    sender = body.get("sender", {})

    # ⚠️ 注意：发布到飞书的 bot 已经能直接处理私聊消息——这条 handler
    # 只在你**明确想用 Bridge 中转**（如做特殊预处理 / 跨 bot 路由）时启用。
    # 默认应该让 Coze 原生飞书集成处理。
    return None     # 默认禁用，需要时改成下面的实现

    # 启用版本（参考）：
    # text = _extract_text(msg)
    # if not text or msg.get("chat_type") != "p2p":
    #     return None
    # sender_open_id = sender.get("sender_id", {}).get("open_id", "")
    # return {
    #     "kind": "trigger_bot",
    #     "args": {
    #         "bot_id": COZE.bot_personal_assistant,
    #         "user_id": sender_open_id,
    #         "message": text,
    #         "conversation_id": f"feishu-p2p-{sender_open_id}",
    #     },
    # }


# ============================================================
# 2. 文档新建 / 编辑 / 删除 → 知识库 CRUD
# ============================================================

def _doc_created(event: dict) -> dict | None:
    body = event.get("event", {})
    file_token = body.get("file_token")
    file_type = body.get("file_type", "")
    file_name = body.get("file_name", "")

    if not file_token or file_type not in ("docx", "doc"):
        return None

    # 决定进哪个 KB（按文件夹/标签判断）
    dataset_id = _decide_kb_for_doc(body)
    if not dataset_id:
        return None

    return {
        "kind": "upload_kb",
        "args": {
            "dataset_id": dataset_id,
            "name": file_name,
            "feishu_token": file_token,
        },
        "needs_external_fetch": ["docx_content"],
    }


def _doc_edited(event: dict) -> dict | None:
    body = event.get("event", {})
    file_token = body.get("file_token")
    if not file_token:
        return None

    return {
        "kind": "update_doc_via_token",
        "args": {
            "feishu_token": file_token,
            "name": body.get("file_name"),
        },
        "needs_external_fetch": ["docx_content"],
    }


def _doc_deleted(event: dict) -> dict | None:
    body = event.get("event", {})
    file_token = body.get("file_token")
    if not file_token:
        return None
    return {
        "kind": "delete_doc_via_token",
        "args": {"feishu_token": file_token},
    }


# ============================================================
# 3. 多维表格变更（默认不同步——直接用飞书集成更好）
# ============================================================

def _bitable_change(event: dict) -> dict | None:
    # 推荐方案：用飞书多维表格集成，让 Coze 工作流按需读最新数据。
    # 只在你坚持要镜像到 Coze 数据库时启用此 handler。
    return None


# ============================================================
# 4. 日历变更 → 提醒 bot
# ============================================================

def _calendar_changed(event: dict) -> dict | None:
    body = event.get("event", {})
    ev = body.get("event", body)
    if not ev:
        return None

    summary_text = (
        f"[日程变更] {ev.get('summary', '')}\n"
        f"时间: {ev.get('start_time')} - {ev.get('end_time')}\n"
        f"参与人: {', '.join(_attendee_names(ev))}"
    )

    creator = ev.get("organizer", {}).get("user_id", "")
    if not creator:
        return None

    return {
        "kind": "trigger_bot",
        "args": {
            "bot_id": COZE.bot_personal_assistant,
            "user_id": creator,
            "message": summary_text,
            "conversation_id": f"feishu-calendar-{creator}",
        },
    }


# ============================================================
# 5. 审批 → 触发对应 bot
# ============================================================

def _approval(event: dict) -> dict | None:
    body = event.get("event", {})
    approval_code = body.get("approval_code", "")
    instance_code = body.get("instance_code", "")
    status = body.get("status", "")

    if not (approval_code and instance_code):
        return None

    # 按 approval_code 路由（生产从 config 加载映射表）
    bot_id = APPROVAL_BOT_MAPPING.get(approval_code, COZE.bot_approval_handler)
    if not bot_id:
        return None

    return {
        "kind": "trigger_bot",
        "args": {
            "bot_id": bot_id,
            "user_id": body.get("user_id", "system"),
            "message": (f"[审批 {status}] {approval_code}/{instance_code}\n"
                        f"理由: {body.get('comment', '')}"),
            "conversation_id": f"feishu-approval-{instance_code}",
        },
    }


APPROVAL_BOT_MAPPING: dict[str, str] = {
    # "approval_code_xxx": "bot_id_yyy",
}


# ============================================================
# 6. 会议录音就绪 → 拉转写 + KB + 触发摘要 workflow
# ============================================================

def _meeting_recording(event: dict) -> dict | None:
    body = event.get("event", {})
    meeting = body.get("meeting", {})
    meeting_id = meeting.get("id")
    if not meeting_id:
        return None

    return {
        "kind": "process_meeting",
        "args": {
            "meeting_id": meeting_id,
            "topic": meeting.get("topic", ""),
        },
        "needs_external_fetch": ["vc_transcript", "vc_attendees"],
    }


# ============================================================
# 7-10. 通讯录变更 → Coze 成员管理
# ============================================================

def _user_created(event: dict) -> dict | None:
    user = event.get("event", {}).get("object", {})
    if not user.get("email"):
        return None
    return {
        "kind": "add_coze_member",
        "args": {
            "user_name": _email_prefix(user["email"]),
            "email": user["email"],
            "role": _role_from_department(user.get("department_ids", [])),
        },
    }


def _user_updated(event: dict) -> dict | None:
    user = event.get("event", {}).get("object", {})
    # 仅当部门变化时才同步（Coze 没有"全字段更新"，只有移动空间）
    if user.get("department_ids"):
        return {
            "kind": "update_coze_member_role",
            "args": {
                "user_id": _email_prefix(user.get("email", "")),
                "new_role": _role_from_department(user["department_ids"]),
            },
        }
    return None


def _user_deleted(event: dict) -> dict | None:
    user = event.get("event", {}).get("object", {})
    if not user.get("email"):
        return None
    return {
        "kind": "remove_coze_member_with_cleanup",
        "args": {
            "user_id": _email_prefix(user["email"]),
            # 30 天后清长期记忆（PIPL 47 条）
            "schedule_memory_cleanup_days": 30,
        },
    }


def _department_updated(event: dict) -> dict | None:
    # TODO: 部门变更 → 调整工作空间成员（具体策略业务方决定）
    return None


# ============================================================
# 11. 邮箱收件 → 客户档案 + 触发分诊 bot
# ============================================================

def _mail_received(event: dict) -> dict | None:
    body = event.get("event", {})
    mail = body.get("message", {})
    mailbox = mail.get("mailbox_address", "")

    # 仅处理特定公账邮箱
    if mailbox not in WATCHED_MAILBOXES:
        return None

    return {
        "kind": "log_customer_interaction",
        "args": {
            "mailbox": mailbox,
            "from_email": mail.get("from", {}).get("address", ""),
            "subject": mail.get("subject", ""),
            "received_at": mail.get("timestamp"),
            "message_id": mail.get("message_id"),
        },
        "needs_external_fetch": ["mail_body"],
    }


WATCHED_MAILBOXES = {
    "sales@your-company.com",
    "service@your-company.com",
}


# ============================================================
# 12. Wiki 变更 → 知识库
# ============================================================

def _wiki_node_changed(event: dict) -> dict | None:
    # TODO: 跟 doc_created 类似，把 wiki 节点同步进 KB
    return None


# ============================================================
# 主路由表
# ============================================================

EVENT_HANDLERS: dict[str, Callable[[dict], dict | None]] = {
    "im.message.receive_v1":               _msg,
    "drive.file.created_v1":               _doc_created,
    "drive.file.edit_v1":                  _doc_edited,
    "drive.file.title_updated_v1":         _doc_edited,
    "drive.file.deleted_v1":               _doc_deleted,
    "bitable.record.changed_v1":           _bitable_change,
    "calendar.calendar.event.changed_v4":  _calendar_changed,
    "approval.instance.approved_v4":       _approval,
    "approval.instance.rejected_v4":       _approval,
    "vc.meeting.recording_ready_v1":       _meeting_recording,
    "contact.user.created_v3":             _user_created,
    "contact.user.updated_v3":             _user_updated,
    "contact.user.deleted_v3":             _user_deleted,
    "contact.department.updated_v3":       _department_updated,
    "im.message.read_v1":                  lambda e: None,   # 显式忽略
    "wiki.space_node_changed_v1":          _wiki_node_changed,
    "mail.user_mailbox.message.received_v1": _mail_received,
}


def translate(event: dict) -> dict | None:
    """主入口。返回 Action dict 或 None（None 表示这事件不同步）。"""
    et = event.get("header", {}).get("event_type")
    handler = EVENT_HANDLERS.get(et)
    if handler is None:
        return None
    return handler(event)


# ============================================================
# 辅助
# ============================================================

def _extract_text(msg: dict) -> str:
    content = msg.get("content")
    if isinstance(content, str):
        try:
            content = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            return content
    if isinstance(content, dict):
        return content.get("text") or content.get("content") or ""
    return ""


def _attendee_names(ev: dict) -> list[str]:
    return [a.get("display_name") or a.get("user_id", "")
            for a in ev.get("attendees", [])]


def _email_prefix(email: str) -> str:
    return email.split("@", 1)[0] if "@" in email else email


def _role_from_department(dept_ids: list[str]) -> str:
    """从飞书部门 ID 决定 Coze 角色。生产从配置加载映射。"""
    # TODO: 接入公司部门表
    return "member"


def _decide_kb_for_doc(body: dict) -> str | None:
    """按文档归属决定进哪个 KB。生产从规则文件加载。"""
    # 简化：所有 docx 都进 SOP KB
    # 实际应按 folder_id / labels 判断（哪些文件夹归销售 / HR / 培训）
    return COZE.kb_sop or None
