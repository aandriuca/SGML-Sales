"""Order — a booked sale, created when an opportunity/quote is accepted."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel

from ..core.enums import OrderStatus


def _utcnow() -> datetime:
    return datetime.now(UTC)


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id", index=True)
    opportunity_id: int | None = Field(default=None, foreign_key="opportunity.id")
    status: OrderStatus = Field(default=OrderStatus.DRAFT, index=True)
    total_amount: float = Field(default=0.0, ge=0)
    created_at: datetime = Field(default_factory=_utcnow)
