"""飞书 event → MemoryRouter.write 的入参翻译器。

输出: {"content": str, "hints": dict}。
hints 里 source 总是 "feishu:<sub>"，type 决定路由（详见 RESOLVER 和 router 配置）。

注意：translator 不调任何外部服务，只做纯函数级转换。
"""
from __future__ import annotations

from typing import Any


def translate(event: dict) -> dict | None:
    """返回 None 表示该事件不进记忆系统（如心跳、订阅确认等）。"""
    header = event.get("header", {})
    etype = header.get("event_type")
    body = event.get("event", {})

    handler = _HANDLERS.get(etype)
    if not handler:
        return None
    return handler(body)


# ---- 各事件 handler -------------------------------------------------

def _msg(body: dict) -> dict | None:
    msg = body.get("message", {})
    sender = body.get("sender", {})
    chat_type = msg.get("chat_type")
    text = _extract_text(msg)
    if not text:
        return None

    sender_id = sender.get("sender_id", {}).get("open_id", "")
    return {
        "content": text,
        "hints": {
            "source": "feishu:im",
            "type": "experience" if chat_type == "p2p" else "interaction",
            "subject_ref": _person_ref(sender_id),
            "ts": msg.get("create_time"),
            "feishu_message_id": msg.get("message_id"),
            "chat_id": msg.get("chat_id"),
        },
    }


def _doc_edit(body: dict) -> dict:
    return {
        "content": f"[飞书文档已编辑] {body.get('file_name', '')}\n"
                   f"链接: {body.get('url', '')}\n"
                   f"摘要: {body.get('summary', '<待 worker 异步拉取正文>')}",
        "hints": {
            "source": "feishu:docs",
            "type": "document",
            "feishu_token": body.get("file_token"),
            "needs_full_fetch": True,   # worker 看到这个 flag 会去拉正文
        },
    }


def _calendar(body: dict) -> dict:
    ev = body.get("event", body)
    return {
        "content": f"[日程] {ev.get('summary', '')}\n"
                   f"时间: {ev.get('start_time')} - {ev.get('end_time')}\n"
                   f"参与人: {', '.join(_attendees(ev))}",
        "hints": {
            "source": "feishu:calendar",
            "type": "meeting",
            "feishu_event_id": ev.get("event_id"),
        },
    }


def _approval(body: dict) -> dict:
    return {
        "content": f"[审批] {body.get('approval_name')} #{body.get('instance_code')}\n"
                   f"结果: {body.get('status')}\n"
                   f"理由: {body.get('comment', '')}",
        "hints": {
            "source": "feishu:approval",
            "type": "decision",      # 走 both（事实+判断）
            "subject_ref": _person_ref(body.get("user_id", "")),
        },
    }


def _vc_recording(body: dict) -> dict:
    return {
        "content": f"[会议录音就绪] {body.get('topic', '')}\n"
                   f"时长: {body.get('duration')}s\n"
                   f"录音: {body.get('url')}",
        "hints": {
            "source": "feishu:vc",
            "type": "meeting_recording",
            "needs_transcript_fetch": True,  # worker 异步拉转写
        },
    }


def _contact(body: dict) -> dict:
    user = body.get("object", {})
    return {
        "content": f"# {user.get('name')}\n"
                   f"- 部门: {', '.join(user.get('department_ids', []))}\n"
                   f"- 邮箱: {user.get('email','')}\n"
                   f"- 手机: {user.get('mobile','')}\n",
        "hints": {
            "source": "feishu:contact",
            "type": "person_profile",
            "subject_ref": _person_ref(user.get("open_id", "")),
        },
    }


_HANDLERS = {
    "im.message.receive_v1":               _msg,
    "drive.file.edit_v1":                  _doc_edit,
    "drive.file.title_updated_v1":         _doc_edit,
    "calendar.calendar.event.changed_v4":  _calendar,
    "approval.instance.approved_v4":       _approval,
    "approval.instance.rejected_v4":       _approval,
    "vc.meeting.recording_ready_v1":       _vc_recording,
    "contact.user.updated_v3":             _contact,
}


# ---- 辅助 ---------------------------------------------------------

def _extract_text(msg: dict) -> str:
    import json as _j
    content = msg.get("content")
    if isinstance(content, str):
        try:
            content = _j.loads(content)
        except Exception:
            return content
    if isinstance(content, dict):
        return content.get("text") or content.get("content") or ""
    return ""


def _attendees(ev: dict) -> list[str]:
    return [a.get("display_name") or a.get("user_id", "")
            for a in ev.get("attendees", [])]


def _person_ref(open_id: str) -> str | None:
    if not open_id:
        return None
    # 约定：飞书 open_id → brain/people/feishu_<id>.md
    # 真实场景应通过 contact API 解析为人名 slug
    return f"brain/people/feishu_{open_id[:12]}.md"
