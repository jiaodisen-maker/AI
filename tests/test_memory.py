"""Tests for Session Memory."""

import pytest

from app.memory.session import SessionMemory


@pytest.mark.asyncio
async def test_add_and_get_messages():
    memory = SessionMemory()  # In-memory mode (no Redis)

    await memory.add_message("s1", "user", "你好")
    await memory.add_message("s1", "assistant", "你好！有什么可以帮你的？")

    history = await memory.get_history("s1")
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "你好"
    assert history[1]["role"] == "assistant"


@pytest.mark.asyncio
async def test_separate_sessions():
    memory = SessionMemory()

    await memory.add_message("s1", "user", "session 1")
    await memory.add_message("s2", "user", "session 2")

    h1 = await memory.get_history("s1")
    h2 = await memory.get_history("s2")
    assert len(h1) == 1
    assert len(h2) == 1
    assert h1[0]["content"] == "session 1"
    assert h2[0]["content"] == "session 2"


@pytest.mark.asyncio
async def test_clear_session():
    memory = SessionMemory()

    await memory.add_message("s1", "user", "hello")
    await memory.clear_session("s1")

    history = await memory.get_history("s1")
    assert len(history) == 0


@pytest.mark.asyncio
async def test_max_history_length():
    memory = SessionMemory()

    for i in range(60):
        await memory.add_message("s1", "user", f"message {i}")

    history = await memory.get_history("s1")
    assert len(history) == 50  # MAX_HISTORY_LENGTH
