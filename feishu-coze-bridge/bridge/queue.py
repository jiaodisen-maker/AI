"""Redis Streams 队列：server 入队，worker 消费，失败入 DLQ。"""
from __future__ import annotations

import json
from typing import AsyncGenerator

import redis.asyncio as redis

from .config import QUEUE


_r = redis.from_url(QUEUE.redis_url)


async def ensure_group() -> None:
    try:
        await _r.xgroup_create(QUEUE.stream, QUEUE.group, id="0", mkstream=True)
    except redis.ResponseError as e:
        if "BUSYGROUP" not in str(e):
            raise


async def enqueue(event: dict) -> str:
    return (await _r.xadd(QUEUE.stream, {"data": json.dumps(event)})).decode()


async def consume(consumer: str, batch: int = 8, block_ms: int = 5000
                  ) -> AsyncGenerator[tuple[str, dict], None]:
    await ensure_group()
    while True:
        msgs = await _r.xreadgroup(
            QUEUE.group, consumer, {QUEUE.stream: ">"},
            count=batch, block=block_ms,
        )
        for _stream, entries in msgs or []:
            for msg_id, fields in entries:
                yield msg_id.decode(), json.loads(fields[b"data"])


async def ack(msg_id: str) -> None:
    await _r.xack(QUEUE.stream, QUEUE.group, msg_id)


async def to_dlq(event: dict, reason: str) -> None:
    await _r.xadd(QUEUE.dlq, {
        "data": json.dumps(event),
        "reason": reason,
    })


async def stream_size() -> int:
    return await _r.xlen(QUEUE.stream)


async def dlq_size() -> int:
    return await _r.xlen(QUEUE.dlq)
