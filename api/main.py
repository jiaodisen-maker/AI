from fastapi import FastAPI

from .config import get_settings
from .routes import alerts, atoms, cases, generate, ingest, microtypes

settings = get_settings()

app = FastAPI(
    title="Agentic Insight Platform",
    version="0.1.0",
    description="v6 — 9 Agent pipeline for content insight automation",
)

app.include_router(ingest.router)
app.include_router(cases.router)
app.include_router(atoms.router)
app.include_router(microtypes.router)
app.include_router(generate.router)
app.include_router(alerts.router)


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "poc_crawled_enabled": settings.poc_crawled_enabled,
        "task_queue": settings.temporal_task_queue,
    }
