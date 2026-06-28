"""Lead endpoints — CRUD plus status transitions and conversion to an opportunity.

This is where an inbound lead (often imported from the marketing pipeline) gets
*worked*: moved through statuses and, once qualified, converted into a real
Opportunity anchored to a Customer.
"""

from fastapi import Depends, HTTPException
from sqlmodel import Session

from ...core.enums import LeadStatus, OpportunityStage
from ...database import get_session
from ...models import Customer, Lead, Opportunity
from ...schemas import LeadConvert, LeadCreate
from ..crud import build_crud_router

router = build_crud_router(Lead, LeadCreate, prefix="/leads", tag="leads")


@router.post("/{item_id}/status", response_model=Lead)
def set_status(
    item_id: int,
    status: LeadStatus,
    session: Session = Depends(get_session),
) -> Lead:
    """Move a lead to a new status (e.g. new -> qualified / unqualified)."""
    lead = session.get(Lead, item_id)
    if lead is None:
        raise HTTPException(status_code=404, detail=f"Lead {item_id} not found")
    lead.status = status
    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead


@router.post("/{item_id}/convert", response_model=Opportunity, status_code=201)
def convert(
    item_id: int,
    payload: LeadConvert,
    session: Session = Depends(get_session),
) -> Opportunity:
    """Convert a qualified lead into an Opportunity, creating/linking a Customer.

    Marks the lead CONVERTED and links it to the Customer. Re-converting an
    already-converted lead is rejected (409) to avoid duplicate opportunities.
    """
    lead = session.get(Lead, item_id)
    if lead is None:
        raise HTTPException(status_code=404, detail=f"Lead {item_id} not found")
    if lead.status == LeadStatus.CONVERTED:
        raise HTTPException(status_code=409, detail=f"Lead {item_id} is already converted")

    # Resolve the account: link the one given, or spin up a Customer from the lead.
    if payload.customer_id is None:
        customer = Customer(name=lead.name, email=lead.email)
        session.add(customer)
        session.commit()
        session.refresh(customer)
        customer_id = customer.id
    else:
        if session.get(Customer, payload.customer_id) is None:
            raise HTTPException(
                status_code=404, detail=f"Customer {payload.customer_id} not found"
            )
        customer_id = payload.customer_id

    opp = Opportunity(
        name=payload.opportunity_name or f"{lead.name} — engagement",
        customer_id=customer_id,
        lead_id=lead.id,
        stage=OpportunityStage.QUALIFICATION,
        amount=payload.amount,
        probability=payload.probability,
    )
    session.add(opp)

    lead.status = LeadStatus.CONVERTED
    lead.customer_id = customer_id
    session.add(lead)

    session.commit()
    session.refresh(opp)
    return opp
