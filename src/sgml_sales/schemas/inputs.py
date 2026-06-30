"""Create (input) schemas.

SQLModel `table=True` models cannot be used directly as FastAPI request bodies —
their columns are interpreted as query parameters. These non-table schemas define
exactly the client-settable fields for each resource.
"""

from __future__ import annotations

from datetime import datetime

from sqlmodel import SQLModel

from ..core.enums import InvoiceStatus, LeadStatus, OpportunityStage, OrderStatus


class CustomerCreate(SQLModel):
    name: str
    email: str | None = None
    phone: str | None = None
    company: str | None = None


class ProductCreate(SQLModel):
    sku: str
    name: str
    description: str | None = None
    unit_price: float
    active: bool = True


class LeadCreate(SQLModel):
    name: str
    email: str | None = None
    source: str | None = None
    status: LeadStatus = LeadStatus.NEW
    customer_id: int | None = None
    website: str | None = None
    category: str | None = None
    platform: str | None = None
    est_revenue: float | None = None


class LeadConvert(SQLModel):
    """Body for converting a qualified lead into an opportunity.

    If ``customer_id`` is omitted, a Customer is created from the lead's
    name/email. ``amount`` defaults to the annual ACV ($2.5k/mo retainer ≈
    $30k/yr per SALES-STRATEGY); override per deal.
    """

    customer_id: int | None = None
    opportunity_name: str | None = None
    amount: float = 30000.0
    probability: float = 0.1


class OpportunityCreate(SQLModel):
    name: str
    customer_id: int
    lead_id: int | None = None
    stage: OpportunityStage = OpportunityStage.PROSPECTING
    amount: float = 0.0
    probability: float = 0.0


class OrderCreate(SQLModel):
    customer_id: int
    opportunity_id: int | None = None
    status: OrderStatus = OrderStatus.DRAFT
    total_amount: float = 0.0


class InvoiceCreate(SQLModel):
    customer_id: int
    order_id: int | None = None
    status: InvoiceStatus = InvoiceStatus.DRAFT
    amount: float
    currency: str = "USD"
    due_at: datetime | None = None
