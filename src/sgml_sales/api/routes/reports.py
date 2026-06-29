"""Reporting endpoints: pipeline analytics and accounting reconciliation."""

from fastapi import APIRouter, Depends
from sqlmodel import Session

from ...database import get_session
from ...schemas.reports import AccountingSummary, PipelineSummary
from ...services import accounting_summary, pipeline_summary

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/pipeline", response_model=PipelineSummary)
def get_pipeline(session: Session = Depends(get_session)) -> PipelineSummary:
    return pipeline_summary(session)


@router.get("/accounting", response_model=AccountingSummary)
def get_accounting(session: Session = Depends(get_session)) -> AccountingSummary:
    return accounting_summary(session)
