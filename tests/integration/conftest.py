"""Integration test fixtures.

需要真实 Postgres（DATABASE_URL env 设置 + pgvector 扩展可用）。
缺 DB 时所有集成测试自动 skip。
"""
import os

import pytest


def _has_db() -> bool:
    if not os.getenv("DATABASE_URL"):
        return False
    try:
        from sqlalchemy import create_engine
        eng = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
        with eng.connect() as conn:
            conn.execute(__import__("sqlalchemy").text("SELECT 1"))
        return True
    except Exception:
        return False


@pytest.fixture(scope="session", autouse=True)
def _skip_if_no_db():
    if not _has_db():
        pytest.skip("DATABASE_URL not reachable; integration tests skipped", allow_module_level=True)
