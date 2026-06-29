"""Response contracts for pipeline and accounting reporting endpoints."""

from __future__ import annotations

from pydantic import BaseModel


class PipelineSummary(BaseModel):
    open_opportunities: int
    total_pipeline_value: float
    weighted_pipeline_value: float
    closed_won_value: float


class AccountingSummary(BaseModel):
    currency: str
    accounts_receivable: float
    recognized_revenue: float
    invoices_outstanding: int
    invoices_paid: int
