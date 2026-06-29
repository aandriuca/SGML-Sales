"""FastAPI application factory and entry point for SGML Sales."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api import api_router
from .config import settings
from .database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup. For production, prefer Alembic migrations.
    init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description=(
            f"Sales infrastructure & accounting API for {settings.company_name}. "
            "Tracks the lead -> opportunity -> order -> invoice pipeline."
        ),
        version="0.1.0",
        lifespan=lifespan,
    )

    @app.get("/health", tags=["meta"])
    def health() -> dict[str, str]:
        return {"status": "ok", "app": settings.app_name, "environment": settings.environment}

    app.include_router(api_router)
    return app


app = create_app()
