"""A6 Microtype 5 维 schema 校验测试 — 纯函数，无 DB / 无 LLM。"""
from worker.agents.a6_microtype import _load_schema, _validate_tags


def test_schema_loads_with_expected_dims():
    sch = _load_schema()
    assert "scenes" in sch
    assert "audiences" in sch
    assert "ingredients" in sch
    assert "emotions" in sch
    assert "restrictions" in sch
    assert len(sch["scenes"]) >= 10
    assert len(sch["ingredients"]) >= 15


def test_validate_valid_tags():
    ok, _ = _validate_tags(
        {
            "scene": "morning",
            "audience": "white_collar_female",
            "ingredient": "vitamin_b",
            "emotion": "fatigue",
            "restriction": "green_safe",
        }
    )
    assert ok


def test_validate_missing_dim():
    ok, err = _validate_tags(
        {
            "scene": "morning",
            "audience": "white_collar_female",
            "ingredient": "vitamin_b",
            "emotion": "fatigue",
            # restriction missing
        }
    )
    assert not ok
    assert "restriction" in err


def test_validate_out_of_set():
    ok, err = _validate_tags(
        {
            "scene": "morning",
            "audience": "white_collar_female",
            "ingredient": "vitamin_b",
            "emotion": "fatigue",
            "restriction": "platform_kuaishou",  # not in allowed set
        }
    )
    assert not ok
    assert "platform_kuaishou" in err


def test_seed_combinations_all_use_allowed_values():
    """yaml 自身的 50 个 seed 必须严格使用 allowed values（整体一致性）。"""
    from pathlib import Path

    import yaml

    raw = yaml.safe_load(
        (Path(__file__).resolve().parents[1] / "rules" / "microtype_schema.yaml").read_text(encoding="utf-8")
    )
    sch = _load_schema()
    pairs = ["scenes", "audiences", "ingredients", "emotions", "restrictions"]
    for seed in raw["seed_combinations"]:
        combo = seed["combo"]
        for value, dim_key in zip(combo, pairs, strict=True):
            assert value in sch[dim_key], f"seed {seed['id']}: {value!r} not in {dim_key}"
