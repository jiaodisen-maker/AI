"""YAML ontology loader with hot-reload support."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

DEFINITIONS_DIR = Path(__file__).parent / "definitions"


class OntologyLoader:
    """Loads and caches ontology definitions from YAML files."""

    def __init__(self, definitions_dir: Path | None = None) -> None:
        self.definitions_dir = definitions_dir or DEFINITIONS_DIR
        self._cache: dict[str, Any] = {}

    def load_all(self) -> dict[str, Any]:
        """Load all ontology YAML files into a merged dict."""
        self._cache.clear()

        if not self.definitions_dir.exists():
            logger.warning("Ontology definitions dir not found: %s", self.definitions_dir)
            return self._cache

        for yaml_file in sorted(self.definitions_dir.rglob("*.yaml")):
            key = yaml_file.stem
            try:
                with open(yaml_file, encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
                self._cache[key] = data
                logger.info("Loaded ontology: %s (%d top-level keys)", key, len(data))
            except Exception as e:
                logger.error("Failed to load ontology %s: %s", yaml_file, e)

        return self._cache

    def get(self, dimension: str) -> dict[str, Any]:
        """Get a specific ontology dimension."""
        if not self._cache:
            self.load_all()
        return self._cache.get(dimension, {})

    def reload(self) -> dict[str, Any]:
        """Hot-reload all ontology files."""
        logger.info("Reloading ontology definitions...")
        return self.load_all()

    @property
    def dimensions(self) -> list[str]:
        """List loaded ontology dimensions."""
        if not self._cache:
            self.load_all()
        return list(self._cache.keys())
