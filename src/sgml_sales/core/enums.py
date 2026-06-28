"""Domain enumerations shared across models, schemas, and services."""

from __future__ import annotations

from enum import StrEnum


class LeadStatus(StrEnum):
    NEW = "new"
    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"
    CONVERTED = "converted"


class OpportunityStage(StrEnum):
    PROSPECTING = "prospecting"
    QUALIFICATION = "qualification"
    PROPOSAL = "proposal"
    NEGOTIATION = "negotiation"
    CLOSED_WON = "closed_won"
    CLOSED_LOST = "closed_lost"


class OrderStatus(StrEnum):
    DRAFT = "draft"
    CONFIRMED = "confirmed"
    FULFILLED = "fulfilled"
    CANCELLED = "cancelled"


class InvoiceStatus(StrEnum):
    DRAFT = "draft"
    SENT = "sent"
    PAID = "paid"
    VOID = "void"
