"""队列消费者：取事件 → 翻译 → 调外部 fetch → 调 Coze。

启动多份并发：
  python -m bridge.worker --consumer w1
  python -m bridge.worker --consumer w2
  ...
"""
from __future__ import annotations

import argparse
import asyncio
import logging
import time

from prometheus_client import Counter, Histogram

from . import audit, feishu_client, safety, translator
from .config import QUEUE
from .coze_client import CozeClient, PermanentError, RetryableError
from .queue import ack, consume, to_dlq


LOG = logging.getLogger("bridge.worker")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")

WORKER_TOTAL = Counter("bridge_worker_total", "events processed",
                       ["event_type", "kind", "result"])
WORKER_LATENCY = Histogram("bridge_worker_seconds", "process latency",
                            ["kind"])


# ============================================================
# 主处理流程
# ============================================================

async def process(event: dict, coze: CozeClient) -> None:
    et = event.get("header", {}).get("event_type", "?")
    event_id = event.get("header", {}).get("event_id", "?")

    # 1) 安全过滤
    block, reason = safety.should_block_to_coze(event)
    if block:
        audit.log_pii_block(event_id, et, reason, audit.hash_payload(event))
        WORKER_TOTAL.labels(et, "blocked", "ok").inc()
        return

    # 2) 翻译
    action = translator.translate(event)
    if action is None:
        WORKER_TOTAL.labels(et, "skip", "ok").inc()
        return

    kind = action["kind"]
    args = action["args"]
    fetch_needs = action.get("needs_external_fetch", [])

    # 3) 拉外部细节（如文档正文、转写）
    enriched = await _fetch_external(args, fetch_needs)
    args.update(enriched)

    # 4) 调 Coze
    t0 = time.perf_counter()
    try:
        await DISPATCH[kind](coze, args)
        elapsed_ms = (time.perf_counter() - t0) * 1000
        WORKER_LATENCY.labels(kind).observe(elapsed_ms / 1000)
        WORKER_TOTAL.labels(et, kind, "ok").inc()
        audit.log_sync(et, kind, True, event_id, elapsed_ms)
    except (RetryableError, PermanentError) as e:
        elapsed_ms = (time.perf_counter() - t0) * 1000
        audit.log_sync(et, kind, False, event_id, elapsed_ms, str(e))
        raise


async def _fetch_external(args: dict, needs: list[str]) -> dict:
    """异步拉飞书侧的细节数据。"""
    out: dict = {}

    if "docx_content" in needs and args.get("feishu_token"):
        out["content"] = await feishu_client.get_docx_raw_content(
            args["feishu_token"])

    if "vc_transcript" in needs and args.get("meeting_id"):
        out["transcript"] = await feishu_client.get_vc_transcript(
            args["meeting_id"])

    if "vc_attendees" in needs and args.get("meeting_id"):
        attendees = await feishu_client.list_vc_attendees(args["meeting_id"])
        out["attendees"] = [a.get("user_id") for a in attendees]

    if "mail_body" in needs and args.get("message_id"):
        mail = await feishu_client.get_mail_message(
            args["mailbox"], args["message_id"])
        body = mail.get("body", {})
        out["body"] = body.get("plain_text", "") if isinstance(body, dict) else ""

    return out


# ============================================================
# Action dispatch table
# ============================================================

async def _do_trigger_bot(coze: CozeClient, args: dict) -> None:
    await coze.trigger_bot(
        bot_id=args["bot_id"],
        user_id=args["user_id"],
        message=args["message"],
        conversation_id=args.get("conversation_id"),
    )


async def _do_upload_kb(coze: CozeClient, args: dict) -> None:
    if not args.get("content"):
        raise PermanentError("upload_kb missing content")
    await coze.upload_doc_to_kb(
        dataset_id=args["dataset_id"],
        name=args["name"],
        content=args["content"],
        source_type="local",
    )


async def _do_update_doc_via_token(coze: CozeClient, args: dict) -> None:
    """编辑事件：先查 KB 里有没有，没有 → 当 created 处理。"""
    feishu_token = args["feishu_token"]
    # TODO: 维护 feishu_token → coze document_id 映射
    document_id = await _lookup_doc_id_by_feishu_token(feishu_token)

    if not document_id:
        # 没找到 → 走 upload 流程
        from .config import COZE
        if not args.get("content"):
            raise PermanentError("update_doc missing content (need upload)")
        await coze.upload_doc_to_kb(
            dataset_id=COZE.kb_sop,
            name=args.get("name") or "untitled.md",
            content=args["content"],
            source_type="local",
        )
        return

    # 找到 → update（注意 Coze update 不一定支持改内容；多数情况是先删后建）
    await coze.delete_doc(document_id)
    from .config import COZE
    await coze.upload_doc_to_kb(
        dataset_id=COZE.kb_sop,
        name=args.get("name") or "untitled.md",
        content=args["content"],
        source_type="local",
    )


async def _do_delete_doc_via_token(coze: CozeClient, args: dict) -> None:
    document_id = await _lookup_doc_id_by_feishu_token(args["feishu_token"])
    if document_id:
        await coze.delete_doc(document_id)


async def _do_process_meeting(coze: CozeClient, args: dict) -> None:
    transcript = args.get("transcript", "")
    if not transcript:
        # 还没准备好——下次回填
        raise RetryableError("meeting transcript not ready", retry_after=300)

    from .config import COZE

    # 1) 转写存进 KB
    await coze.upload_doc_to_kb(
        dataset_id=COZE.kb_meeting_transcripts,
        name=f"meeting_{args['meeting_id']}.md",
        content=transcript,
        source_type="local",
    )

    # 2) 触发"会议消化" workflow
    if COZE.workflow_meeting_digest:
        await coze.trigger_workflow(
            workflow_id=COZE.workflow_meeting_digest,
            parameters={
                "transcript": transcript,
                "attendees": args.get("attendees", []),
                "meeting_id": args["meeting_id"],
                "topic": args.get("topic", ""),
            },
        )


async def _do_add_coze_member(coze: CozeClient, args: dict) -> None:
    await coze.add_member(
        user_name=args["user_name"],
        email=args["email"],
        role=args.get("role", "member"),
    )


async def _do_update_coze_member_role(coze: CozeClient, args: dict) -> None:
    # TODO: 实现 update（看 Coze 实际 API；可能需要 remove + add）
    LOG.warning("update_coze_member_role not implemented yet, args=%s", args)


async def _do_remove_coze_member_with_cleanup(coze: CozeClient, args: dict) -> None:
    # 先撤销成员权限
    await coze.remove_member(args["user_id"])
    # 30 天后清长期记忆 → 通过单独的 cron 任务实现
    LOG.info("scheduled memory cleanup for %s in %d days",
             args["user_id"], args["schedule_memory_cleanup_days"])
    # TODO: insert into postgres scheduled_tasks


async def _do_log_customer_interaction(coze: CozeClient, args: dict) -> None:
    """邮件 → 通过触发"客户分诊 bot"处理，bot 内部用插件写多维表格。"""
    from .config import COZE
    if not COZE.bot_approval_handler:
        return
    msg = (f"[新客户邮件] from={args.get('from_email')}\n"
           f"subject: {args.get('subject')}\n\n"
           f"{(args.get('body') or '')[:2000]}")
    await coze.trigger_bot(
        bot_id=COZE.bot_approval_handler,
        user_id="system-mail-bridge",
        message=msg,
        conversation_id=f"feishu-mail-{args.get('message_id', 'x')}",
    )


DISPATCH = {
    "trigger_bot":                       _do_trigger_bot,
    "upload_kb":                         _do_upload_kb,
    "update_doc_via_token":              _do_update_doc_via_token,
    "delete_doc_via_token":              _do_delete_doc_via_token,
    "process_meeting":                   _do_process_meeting,
    "add_coze_member":                   _do_add_coze_member,
    "update_coze_member_role":           _do_update_coze_member_role,
    "remove_coze_member_with_cleanup":   _do_remove_coze_member_with_cleanup,
    "log_customer_interaction":          _do_log_customer_interaction,
}


# ============================================================
# 持久化的 feishu_token → coze document_id 映射
# ============================================================

async def _lookup_doc_id_by_feishu_token(feishu_token: str) -> str | None:
    """TODO: 维护一张 feishu_token ↔ coze_document_id 表（Postgres）。

    每次 upload 后写入；update/delete 时按 token 查 doc_id。
    """
    return None     # 暂未实现，update 走"先删后建"


# ============================================================
# Main loop
# ============================================================

async def loop(consumer: str) -> None:
    LOG.info("worker %s starting", consumer)
    coze = CozeClient()
    try:
        async for msg_id, event in consume(consumer):
            for attempt in range(QUEUE.max_retries):
                try:
                    await process(event, coze)
                    await ack(msg_id)
                    break
                except RetryableError as e:
                    wait = min(e.retry_after, 60)
                    LOG.warning("retryable: %s (wait %.1fs, attempt %d)",
                                e, wait, attempt)
                    await asyncio.sleep(wait)
                except PermanentError as e:
                    LOG.error("permanent: %s -> DLQ", e)
                    await to_dlq(event, str(e))
                    await ack(msg_id)
                    break
                except Exception as e:
                    wait = (QUEUE.backoff_base_ms / 1000) * (2 ** attempt)
                    LOG.warning("unknown: %r (wait %.1fs, attempt %d)",
                                e, wait, attempt)
                    await asyncio.sleep(wait)
            else:
                LOG.error("exceeded retries -> DLQ event_id=%s",
                          event.get("header", {}).get("event_id"))
                await to_dlq(event, "exceeded_retries")
                await ack(msg_id)
    finally:
        await coze.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--consumer", default="w-default")
    args = ap.parse_args()
    asyncio.run(loop(args.consumer))


if __name__ == "__main__":
    main()
