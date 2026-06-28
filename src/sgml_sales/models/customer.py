"""Customer (account) entity — the anchor every pipeline record links back to."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


def _utcnow() -> datetime:
    return datetime.now(UTC)


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    phone: str | None = None
    company: str | None = None
    created_at: datetime = Field(default_factory=_utcnow)
