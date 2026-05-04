"""通知适配器。冲突 / 异常推到飞书或邮件。

接你 gstack 的 channels 层。
"""
from __future__ import annotations


async def send_review(conflict) -> None:
    """把记忆冲突推给负责人审核。"""
    # 接 channels.feishu.send_card(...) 或 email.send(...)
    print(f"[REVIEW] {conflict}")
