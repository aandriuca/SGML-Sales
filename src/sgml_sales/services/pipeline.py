"""Pipeline analytics derived from Opportunity records."""

from __future__ import annotations

from sqlmodel import Session, select

from ..core.enums import OpportunityStage
from ..models import Opportunity
from ..schemas.reports import PipelineSummary

_OPEN_STAGES = {
    OpportunityStage.PROSPECTING,
    OpportunityStage.QUALIFICATION,
    OpportunityStage.PROPOSAL,
    OpportunityStage.NEGOTIATION,
}


def pipeline_summary(session: Session) -> PipelineSummary:
    """Aggregate open pipeline value and closed-won totals."""
    opportunities = session.exec(select(Opportunity)).all()

    open_opps = [o for o in opportunities if o.stage in _OPEN_STAGES]
    closed_won = [o for o in opportunities if o.stage == OpportunityStage.CLOSED_WON]

    return PipelineSummary(
        open_opportunities=len(open_opps),
        total_pipeline_value=round(sum(o.amount for o in open_opps), 2),
        weighted_pipeline_value=round(sum(o.weighted_amount for o in open_opps), 2),
        closed_won_value=round(sum(o.amount for o in closed_won), 2),
    )
