"""Accounting reconciliation derived from Invoice records.

These functions are the hook point for syncing to an external ledger
(e.g. the SGL accounting system).
"""

from __future__ import annotations

from sqlmodel import Session, select

from ..config import settings
from ..core.enums import InvoiceStatus
from ..models import Invoice
from ..schemas.reports import AccountingSummary

# Statuses that represent money owed to us but not yet collected.
_OUTSTANDING = {InvoiceStatus.SENT}


def accounting_summary(session: Session) -> AccountingSummary:
    """Compute accounts receivable and recognized revenue from invoices."""
    invoices = session.exec(select(Invoice)).all()

    outstanding = [i for i in invoices if i.status in _OUTSTANDING]
    paid = [i for i in invoices if i.status == InvoiceStatus.PAID]

    return AccountingSummary(
        currency=settings.company_currency,
        accounts_receivable=round(sum(i.amount for i in outstanding), 2),
        recognized_revenue=round(sum(i.amount for i in paid), 2),
        invoices_outstanding=len(outstanding),
        invoices_paid=len(paid),
    )
