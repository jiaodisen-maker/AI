"""可靠性子系统的本地状态：探针历史、告警去重、SLO 滚动统计。

SQLite 单文件足够（探针频率低、写入小）。
"""
from __future__ import annotations

import json
import os
import sqlite3
import threading
from datetime import datetime, timedelta
from pathlib import Path


_LOCK = threading.Lock()


class State:
    def __init__(self, path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(path, check_same_thread=False)
        self._db.executescript("""
            CREATE TABLE IF NOT EXISTS kv (
                k TEXT PRIMARY KEY,
                v TEXT,
                updated_at TEXT
            );
            CREATE TABLE IF NOT EXISTS probes (
                ts TEXT, name TEXT, ok INTEGER,
                detail TEXT, elapsed_ms REAL, critical INTEGER
            );
            CREATE TABLE IF NOT EXISTS alert_dedup (
                key TEXT PRIMARY KEY, last_emit TEXT
            );
            CREATE INDEX IF NOT EXISTS ix_probes_ts ON probes(ts);
        """)
        self._db.commit()

    # --- 简单 KV ---------------------------------------------------
    def get(self, k: str, default=None):
        with _LOCK:
            row = self._db.execute("SELECT v FROM kv WHERE k=?", (k,)).fetchone()
        return json.loads(row[0]) if row else default

    def set(self, k: str, v) -> None:
        with _LOCK:
            self._db.execute(
                "INSERT INTO kv(k,v,updated_at) VALUES(?,?,?) "
                "ON CONFLICT(k) DO UPDATE SET v=excluded.v, updated_at=excluded.updated_at",
                (k, json.dumps(v), datetime.utcnow().isoformat()))
            self._db.commit()

    def get_int(self, k, default=0):
        return int(self.get(k, default))

    def set_int(self, k, v):
        self.set(k, int(v))

    def get_ts(self, k):
        v = self.get(k)
        return datetime.fromisoformat(v) if v else None

    def set_ts(self, k, dt: datetime | None = None):
        self.set(k, (dt or datetime.utcnow()).isoformat())

    def older_than(self, k: str, delta: timedelta) -> bool:
        with _LOCK:
            row = self._db.execute("SELECT updated_at FROM kv WHERE k=?", (k,)).fetchone()
        if not row:
            return True
        return datetime.fromisoformat(row[0]) < datetime.utcnow() - delta

    # --- 探针记录 + critical 连击 ---------------------------------
    def record_probes(self, probes) -> None:
        ts = datetime.utcnow().isoformat()
        with _LOCK:
            self._db.executemany(
                "INSERT INTO probes(ts,name,ok,detail,elapsed_ms,critical) "
                "VALUES(?,?,?,?,?,?)",
                [(ts, p.name, int(p.ok), p.detail, p.elapsed_ms, int(p.critical))
                 for p in probes])
            self._db.commit()

    def bump_critical_streak(self) -> int:
        n = self.get_int("critical_streak", 0) + 1
        self.set_int("critical_streak", n)
        return n

    def reset_critical_streak(self) -> None:
        self.set_int("critical_streak", 0)

    # --- 告警去重 -------------------------------------------------
    def should_emit(self, dedup_key: str, cooldown: timedelta) -> bool:
        with _LOCK:
            row = self._db.execute(
                "SELECT last_emit FROM alert_dedup WHERE key=?", (dedup_key,)
            ).fetchone()
            now = datetime.utcnow()
            if row and datetime.fromisoformat(row[0]) > now - cooldown:
                return False
            self._db.execute(
                "INSERT INTO alert_dedup(key,last_emit) VALUES(?,?) "
                "ON CONFLICT(key) DO UPDATE SET last_emit=excluded.last_emit",
                (dedup_key, now.isoformat()))
            self._db.commit()
        return True
