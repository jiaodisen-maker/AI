"""Tests for the Experience Engine."""

import pytest

from app.experience.engine import ExperienceEngine
from app.experience.models import ExperiencePattern
from app.experience.store import ExperienceStore


def test_text_to_ngrams_chinese():
    """Chinese text should produce character bigrams."""
    ngrams = ExperienceEngine._text_to_ngrams("抖音文案用口语化")
    assert "抖音" in ngrams
    assert "音文" in ngrams
    assert "文案" in ngrams
    assert "口语" in ngrams
    assert len(ngrams) == 7


def test_text_to_ngrams_english():
    """English text should also produce character bigrams."""
    ngrams = ExperienceEngine._text_to_ngrams("hello")
    assert "he" in ngrams
    assert "el" in ngrams
    assert len(ngrams) == 4


def test_text_to_ngrams_short():
    ngrams = ExperienceEngine._text_to_ngrams("a")
    assert ngrams == {"a"}


def test_text_to_ngrams_empty():
    ngrams = ExperienceEngine._text_to_ngrams("")
    assert ngrams == set()


@pytest.mark.asyncio
async def test_experience_store_add_record():
    store = ExperienceStore()
    from app.experience.models import ExperienceRecord

    record = ExperienceRecord(skill_id="test", ai_output="hello")
    rid = await store.add_record(record)
    assert rid

    records = store.get_records("test")
    assert len(records) == 1


@pytest.mark.asyncio
async def test_experience_store_patterns():
    store = ExperienceStore()
    pattern = ExperiencePattern(
        skill_id="test",
        pattern="抖音文案要口语化",
        confidence=0.8,
    )
    pid = await store.add_pattern(pattern)
    assert pid

    reliable = store.get_reliable_patterns("test")
    assert len(reliable) == 1
    assert reliable[0].pattern == "抖音文案要口语化"


@pytest.mark.asyncio
async def test_experience_store_confirm_reject():
    store = ExperienceStore()
    pattern = ExperiencePattern(
        id="p1",
        skill_id="test",
        pattern="test pattern",
        confidence=0.5,
    )
    await store.add_pattern(pattern)

    await store.confirm_pattern("p1")
    p = store._patterns["p1"]
    assert p.confidence == 0.6
    assert p.usage_count == 1

    await store.reject_pattern("p1")
    p = store._patterns["p1"]
    assert p.confidence == pytest.approx(0.4, abs=0.01)
