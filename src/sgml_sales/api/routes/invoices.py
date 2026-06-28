"""Invoice endpoints, including marking an invoice paid."""

from datetime import UTC, datetime

from fastapi import Depends, HTTPException
from sqlmodel import Session

from ...core.enums import InvoiceStatus
from ...database import get_session
from ...models import Invoice
from ...schemas import InvoiceCreate
from ..crud import build_crud_router

router = build_crud_router(Invoice, InvoiceCreate, prefix="/invoices", tag="invoices")


@router.post("/{item_id}/pay", response_model=Invoice)
def mark_paid(item_id: int, session: Session = Depends(get_session)) -> Invoice:
    """Mark an invoice as paid and stamp the payment time (AR -> revenue)."""
    invoice = session.get(Invoice, item_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail=f"Invoice {item_id} not found")
    invoice.status = InvoiceStatus.PAID
    invoice.paid_at = datetime.now(UTC)
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice
