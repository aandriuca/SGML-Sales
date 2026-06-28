"""Database engine, session management, and schema initialization."""

from __future__ import annotations

from collections.abc import Iterator

from sqlmodel import Session, SQLModel, create_engine

from .config import settings

# `check_same_thread` is a SQLite-only concern; harmless to pass for other backends? No —
# only set it for SQLite to avoid surprising other drivers.
_connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}

engine = create_engine(settings.database_url, echo=settings.debug, connect_args=_connect_args)


def init_db() -> None:
    """Create all tables. Models must be imported before this runs."""
    # Importing the models package registers every table on SQLModel.metadata.
    from . import models  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    """FastAPI dependency that yields a database session."""
    with Session(engine) as session:
        yield session
