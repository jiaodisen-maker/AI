"""Enterprise Ontology Module — 12-dimension business knowledge model.

The ontology is the semantic foundation of the AI middleware platform.
It tells agents WHO does WHAT, HOW things are done, and WHAT rules apply.
Agents query the ontology via MCP tools instead of guessing.
"""

from app.ontology.loader import OntologyLoader
from app.ontology.service import OntologyService

__all__ = ["OntologyLoader", "OntologyService"]
