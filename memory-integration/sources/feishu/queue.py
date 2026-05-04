"""Redis Streams 队列。

server.py / long_connection.py 入队；worker.py 消费；失败进 DLQ。
"""
from __future__ import annotations

import json
import os
import yaml
import redis.asyncio as redis

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
_r = redis.from_url(CFG["queue"]["url"])
STREAM = CFG["queue"]["stream_key"]
GROUP = CFG["queue"]["consumer_group"]
DLQ = CFG["queue"]["dlq_stream"]


async def ensure_group():
    try:
        await _r.xgroup_create(STREAM, GROUP, id="0", mkstream=True)
    except redis.ResponseError as e:
        if "BUSYGROUP" not in str(e):
            raise


async def enqueue(event: dict) -> str:
    return await _r.xadd(STREAM, {"data": json.dumps(event)})


async def consume(consumer: str, batch: int = 16, block_ms: int = 5000):
    """生成器：(msg_id, event_dict)。"""
    await ensure_group()
    while True:
        msgs = await _r.xreadgroup(GROUP, consumer,
                                   {STREAM: ">"},
                                   count=batch, block=block_ms)
        for _stream, entries in msgs or []:
            for msg_id, fields in entries:
                yield msg_id, json.loads(fields[b"data"])


async def ack(msg_id: str) -> None:
    await _r.xack(STREAM, GROUP, msg_id)


async def to_dlq(event: dict, reason: str) -> None:
    await _r.xadd(DLQ, {"data": json.dumps(event), "reason": reason})
