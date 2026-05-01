"""Temporal client — used by API to start AgenticInsightWorkflow."""
from temporalio.client import Client

from .config import get_settings

_client: Client | None = None


async def get_temporal_client() -> Client:
    global _client
    if _client is None:
        s = get_settings()
        _client = await Client.connect(s.temporal_address, namespace=s.temporal_namespace)
    return _client
