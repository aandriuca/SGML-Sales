"""Invoice — the accounting/AR record for a booked order."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel

from ..core.enums import InvoiceStatus


def _utcnow() -> datetime:
    return datetime.now(UTC)


class Invoice(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id", index=True)
    order_id: int | None = Field(default=None, foreign_key="order.id")
    status: InvoiceStatus = Field(default=InvoiceStatus.DRAFT, index=True)
    amount: float = Field(ge=0)
    currency: str = "USD"
    issued_at: datetime = Field(default_factory=_utcnow)
    due_at: datetime | None = None
    paid_at: datetime | None = None
