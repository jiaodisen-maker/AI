"""Health check endpoint."""

from __future__ import annotations

from fastapi import APIRouter

from app import __version__

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": __version__,
        "service": "ai-zhongtai",
    }
