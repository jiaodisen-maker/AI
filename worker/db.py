"""Sync SQLAlchemy session for Temporal activities. Lazy engine creation."""
import os
from collections.abc import Generator
from contextlib import contextmanager
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


@lru_cache(maxsize=1)
def get_engine() -> Engine:
    url = os.getenv(
        "DATABASE_URL", "postgresql+psycopg://platform:platform@localhost:5432/platform"
    )
    return create_engine(url, pool_pre_ping=True, future=True)


@lru_cache(maxsize=1)
def _session_factory() -> sessionmaker:
    return sessionmaker(bind=get_engine(), autoflush=False, autocommit=False, future=True)


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    s = _session_factory()()
    try:
        yield s
        s.commit()
    except Exception:
        s.rollback()
        raise
    finally:
        s.close()
