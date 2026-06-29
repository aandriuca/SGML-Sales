"""Lead — top of the funnel, often sourced from the SGML Marketing Pipeline."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel

from ..core.enums import LeadStatus


def _utcnow() -> datetime:
    return datetime.now(UTC)


class Lead(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str | None = None
    source: str | None = Field(default=None, description="e.g. 'marketing-pipeline', 'referral'")
    status: LeadStatus = Field(default=LeadStatus.NEW, index=True)
    customer_id: int | None = Field(default=None, foreign_key="customer.id")
    created_at: datetime = Field(default_factory=_utcnow)
