"""Request/response contracts (Pydantic models distinct from persistence tables)."""

from .inputs import (
    CustomerCreate,
    InvoiceCreate,
    LeadConvert,
    LeadCreate,
    OpportunityCreate,
    OrderCreate,
    ProductCreate,
)
from .reports import AccountingSummary, PipelineSummary

__all__ = [
    "AccountingSummary",
    "CustomerCreate",
    "InvoiceCreate",
    "LeadConvert",
    "LeadCreate",
    "OpportunityCreate",
    "OrderCreate",
    "PipelineSummary",
    "ProductCreate",
]
