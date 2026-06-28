"""Opportunity — a qualified deal moving through sales stages."""

from __future__ import annotations

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel

from ..core.enums import OpportunityStage


def _utcnow() -> datetime:
    return datetime.now(UTC)


class Opportunity(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    customer_id: int = Field(foreign_key="customer.id", index=True)
    lead_id: int | None = Field(default=None, foreign_key="lead.id")
    stage: OpportunityStage = Field(default=OpportunityStage.PROSPECTING, index=True)
    amount: float = Field(default=0.0, ge=0, description="Expected deal value")
    probability: float = Field(default=0.0, ge=0, le=1, description="Win probability 0..1")
    created_at: datetime = Field(default_factory=_utcnow)

    @property
    def weighted_amount(self) -> float:
        """Pipeline value adjusted by win probability."""
        return round(self.amount * self.probability, 2)
