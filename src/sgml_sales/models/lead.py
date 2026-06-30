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
    source: str | None = Field(default=None, description="e.g. 'marketing-pipeline', 'store-leads'")
    status: LeadStatus = Field(default=LeadStatus.NEW, index=True)
    customer_id: int | None = Field(default=None, foreign_key="customer.id")
    created_at: datetime = Field(default_factory=_utcnow)

    # Sourcing/enrichment context — populated from prospect-list imports (Store Leads,
    # Apollo, Clay…). All nullable & additive. NOTE: no migrations yet (init_db uses
    # create_all), so an existing SQLite file won't gain these columns automatically —
    # recreate the dev DB, or ALTER it, to pick them up.
    website: str | None = Field(default=None, description="Store domain, e.g. 'brand.com'")
    category: str | None = Field(default=None, description="Vertical, e.g. 'skincare'")
    platform: str | None = Field(default=None, description="e.g. 'shopify', 'shopify+amazon'")
    est_revenue: float | None = Field(
        default=None, description="Estimated annual revenue (USD); from sourcing tools"
    )
