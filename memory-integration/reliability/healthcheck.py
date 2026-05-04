"""端到端健康探针。每分钟跑一次。

任一 critical=true 的探针红，立即告警；连续 N 次升级到电话。
"""
from __future__ import annotations

import argparse
import asyncio
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import yaml
import redis.asyncio as redis

from .alerts import emit
from .state import State

CFG = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "config.yaml")))
HC = CFG["healthcheck"]


@dataclass
class ProbeResult:
    name: str
    ok: bool
    detail: str = ""
    elapsed_ms: float = 0.0
    critical: bool = False


async def _redis_ping(r) -> ProbeResult:
    t0 = time.perf_counter()
    try:
        pong = await r.ping()
        return ProbeResult("redis_ping", bool(pong),
                           elapsed_ms=(time.perf_counter() - t0) * 1000,
                           critical=True)
    except Exception as e:
        return ProbeResult("redis_ping", False, detail=str(e), critical=True)


async def _token_ttl(r) -> ProbeResult:
    threshold = HC["probes"]["token_ttl_min_s"]["value"]
    ttl = await r.ttl("feishu:tenant_access_token")
    ok = ttl is not None and ttl >= threshold
    return ProbeResult("token_ttl", ok, detail=f"ttl={ttl}s", critical=True)


async def _queue_consumers(r) -> ProbeResult:
    try:
        info = await r.xinfo_groups("feishu:events")
        any_group = info[0] if info else {}
        n = any_group.get(b"consumers") or 0
        ok = n >= HC["probes"]["queue_consumers_min"]["value"]
        return ProbeResult("queue_consumers", ok, detail=f"consumers={n}",
                           critical=True)
    except Exception as e:
        return ProbeResult("queue_consumers", False, detail=str(e), critical=True)


async def _queue_lag(r) -> ProbeResult:
    threshold = HC["probes"]["queue_lag_max"]["value"]
    try:
        info = await r.xinfo_groups("feishu:events")
        lag = max((g.get(b"lag", 0) or 0) for g in info) if info else 0
        return ProbeResult("queue_lag", lag <= threshold, detail=f"lag={lag}")
    except Exception as e:
        return ProbeResult("queue_lag", False, detail=str(e))


async def _dlq_increment(r, state: State) -> ProbeResult:
    threshold = HC["probes"]["dlq_increment_per_h"]["value"]
    try:
        size = await r.xlen("feishu:events:dlq")
        last = state.get_int("dlq_last_size_1h_ago", default=size)
        delta = size - last
        # 每小时滚动一次基线
        if state.older_than("dlq_last_size_1h_ago", timedelta(hours=1)):
            state.set_int("dlq_last_size_1h_ago", size)
        return ProbeResult("dlq_increment", delta < threshold,
                           detail=f"+{delta}/h")
    except Exception as e:
        return ProbeResult("dlq_increment", False, detail=str(e))


async def _write_probe() -> ProbeResult:
    threshold = HC["probes"]["write_probe_ms"]["value"]
    from ..scripts.router import MemoryRouter
    t0 = time.perf_counter()
    try:
        await MemoryRouter().write(
            "__probe__",
            {"type": "test", "source": "reliability", "probe_ts": time.time()})
        ms = (time.perf_counter() - t0) * 1000
        return ProbeResult("write_probe", ms < threshold, elapsed_ms=ms,
                           critical=True)
    except Exception as e:
        return ProbeResult("write_probe", False, detail=str(e), critical=True)


async def _read_probe() -> ProbeResult:
    threshold = HC["probes"]["read_probe_ms"]["value"]
    from ..scripts.router import MemoryRouter
    t0 = time.perf_counter()
    try:
        hits = await MemoryRouter().recall("__probe__", k=1)
        ms = (time.perf_counter() - t0) * 1000
        ok = ms < threshold and bool(hits)
        return ProbeResult("read_probe", ok, elapsed_ms=ms,
                           detail=f"hits={len(hits)}", critical=True)
    except Exception as e:
        return ProbeResult("read_probe", False, detail=str(e), critical=True)


async def _consolidation_lag(state: State) -> ProbeResult:
    threshold_h = HC["probes"]["consolidation_max_h"]["value"]
    last = state.get_ts("last_consolidation_run")
    if not last:
        return ProbeResult("consolidation_lag", False, detail="never run")
    age_h = (datetime.utcnow() - last).total_seconds() / 3600
    return ProbeResult("consolidation_lag", age_h < threshold_h,
                       detail=f"{age_h:.1f}h")


async def run_once() -> list[ProbeResult]:
    r = redis.from_url(CFG.get("queue", {}).get("url", "redis://localhost:6379/0"))
    state = State(CFG["storage"]["state_db"])

    probes = await asyncio.gather(
        _redis_ping(r),
        _token_ttl(r),
        _queue_consumers(r),
        _queue_lag(r),
        _dlq_increment(r, state),
        _write_probe(),
        _read_probe(),
        _consolidation_lag(state),
    )

    state.record_probes(probes)
    return probes


async def evaluate_and_alert(probes: list[ProbeResult], state: State):
    failed = [p for p in probes if not p.ok]
    if not failed:
        state.reset_critical_streak()
        return

    has_critical = any(p.critical for p in failed)
    severity = "CRITICAL" if has_critical else "WARN"

    if has_critical:
        streak = state.bump_critical_streak()
        if streak >= HC["escalation"]["consecutive_critical_for_phone"]:
            severity = "FATAL"

    msg = "记忆层健康探针失败:\n" + "\n".join(
        f"  - {p.name}: {p.detail or 'failed'}" for p in failed)
    await emit(severity=severity, title="memory healthcheck", body=msg,
               dedup_key=f"hc:{','.join(p.name for p in failed)}")


async def loop():
    state = State(CFG["storage"]["state_db"])
    while True:
        try:
            probes = await run_once()
            await evaluate_and_alert(probes, state)
        except Exception as e:
            await emit("CRITICAL", "healthcheck crashed", str(e),
                       dedup_key="hc:crashed")
        await asyncio.sleep(HC["interval_seconds"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--cron", action="store_true")
    args = ap.parse_args()

    if args.cron:
        asyncio.run(loop())
    else:
        probes = asyncio.run(run_once())
        for p in probes:
            mark = "✓" if p.ok else "✗"
            print(f"  {mark} {p.name:22s} {p.detail}  ({p.elapsed_ms:.0f}ms)")
        if any(not p.ok for p in probes):
            raise SystemExit(1)


if __name__ == "__main__":
    main()
