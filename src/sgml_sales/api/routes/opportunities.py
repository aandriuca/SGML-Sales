"""Opportunity endpoints, including stage transitions."""

from fastapi import Depends, HTTPException
from sqlmodel import Session

from ...core.enums import OpportunityStage
from ...database import get_session
from ...models import Opportunity
from ...schemas import OpportunityCreate
from ..crud import build_crud_router

router = build_crud_router(
    Opportunity, OpportunityCreate, prefix="/opportunities", tag="opportunities"
)


@router.post("/{item_id}/stage", response_model=Opportunity)
def set_stage(
    item_id: int,
    stage: OpportunityStage,
    session: Session = Depends(get_session),
) -> Opportunity:
    """Advance (or move) an opportunity to a new pipeline stage."""
    opp = session.get(Opportunity, item_id)
    if opp is None:
        raise HTTPException(status_code=404, detail=f"Opportunity {item_id} not found")
    opp.stage = stage
    session.add(opp)
    session.commit()
    session.refresh(opp)
    return opp
