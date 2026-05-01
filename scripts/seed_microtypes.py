"""把 rules/microtype_schema.yaml 的 50 个 seed_combinations 灌入 microtypes 表（status='active'）。

执行：
    python scripts/seed_microtypes.py

幂等：UNIQUE (scene, audience, ingredient, emotion, restriction) 约束，重复 seed ON CONFLICT DO NOTHING。
"""
import sys
from pathlib import Path

import yaml
from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from api.config import get_settings  # noqa: E402

SCHEMA_PATH = ROOT / "rules" / "microtype_schema.yaml"


def main() -> int:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    seeds = schema.get("seed_combinations", [])
    if not seeds:
        print("no seed_combinations in yaml")
        return 1

    engine = create_engine(get_settings().database_url)
    inserted = 0
    skipped = 0
    with engine.begin() as conn:
        for seed in seeds:
            combo = seed["combo"]
            if len(combo) != 5:
                print(f"skipping bad combo {seed['id']}: {combo}")
                skipped += 1
                continue
            scene, audience, ingredient, emotion, restriction = combo
            r = conn.execute(
                text(
                    """
                    INSERT INTO microtypes (
                        scene, audience, ingredient, emotion, restriction,
                        status, proposed_by_agent
                    )
                    VALUES (:s, :a, :i, :e, :r, 'active', FALSE)
                    ON CONFLICT (scene, audience, ingredient, emotion, restriction) DO NOTHING
                    """
                ),
                {
                    "s": scene,
                    "a": audience,
                    "i": ingredient,
                    "e": emotion,
                    "r": restriction,
                },
            )
            if r.rowcount > 0:
                inserted += 1
            else:
                skipped += 1

    print(f"inserted: {inserted}, skipped (already present): {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
