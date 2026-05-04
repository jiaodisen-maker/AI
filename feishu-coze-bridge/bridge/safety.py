"""数据安全过滤：L4 数据不进 Coze。

参考 docs/coze-knowledge-base/DATA-SECURITY.md。
"""
from __future__ import annotations

import re


# 中国本地化 PII 正则
PATTERNS = {
    "phone_cn":   re.compile(r"1[3-9]\d{9}"),
    "id_card_cn": re.compile(r"[1-9]\d{5}(?:19|20)\d{6}\d{3}[\dXx]"),
    "bank_card":  re.compile(r"\b\d{16,19}\b"),
    "email":      re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"),
}

# 保健品行业禁词（医疗类，L4 数据触发）
MEDICAL_KEYWORDS = [
    "处方", "病历", "确诊", "病理", "化验", "诊断书",
    "病史", "手术记录", "检查报告",
]


def detect_pii(text: str) -> list[str]:
    """返回命中的规则名清单（空则无 PII）."""
    if not text:
        return []
    hits: list[str] = []
    for name, pat in PATTERNS.items():
        if pat.search(text):
            hits.append(name)
    return hits


def detect_medical(text: str) -> list[str]:
    if not text:
        return []
    return [kw for kw in MEDICAL_KEYWORDS if kw in text]


def should_block_to_coze(payload: dict) -> tuple[bool, str]:
    """决定一个事件 payload 要不要拒绝同步到 Coze。

    返回 (block?, reason)。
    """
    text = _extract_text(payload)
    if not text:
        return False, ""

    # L4 医疗数据：绝不进 Coze
    med = detect_medical(text)
    if med:
        return True, f"medical_keyword:{','.join(med)}"

    # L4 身份证：绝不进
    if PATTERNS["id_card_cn"].search(text):
        return True, "id_card"

    # 银行卡：绝不进
    if PATTERNS["bank_card"].search(text):
        return True, "bank_card"

    # 手机/邮箱：可以同步（业务需要），但要在 Coze 侧脱敏
    return False, ""


def mask_pii(text: str) -> str:
    """脱敏文本（手机/邮箱），保留可读性。"""
    if not text:
        return text
    text = PATTERNS["phone_cn"].sub(
        lambda m: m.group()[:3] + "****" + m.group()[-4:], text)
    text = PATTERNS["email"].sub(
        lambda m: m.group()[0] + "***@" + m.group().split("@")[-1], text)
    return text


def _extract_text(payload: dict) -> str:
    """从飞书事件里抽出文本字段（best effort）."""
    parts: list[str] = []

    # 消息内容
    msg = payload.get("event", {}).get("message", {})
    if msg:
        content = msg.get("content")
        if isinstance(content, str):
            parts.append(content)

    # 文档摘要
    parts.append(payload.get("event", {}).get("summary", ""))

    # 邮件 subject + body
    mail = payload.get("event", {}).get("message", {})
    parts.append(mail.get("subject", ""))
    body = mail.get("body", {})
    if isinstance(body, dict):
        parts.append(body.get("plain_text", ""))

    return " ".join(p for p in parts if p)
