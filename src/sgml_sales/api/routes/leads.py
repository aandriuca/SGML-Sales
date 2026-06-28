"""Lead endpoints."""

from ...models import Lead
from ...schemas import LeadCreate
from ..crud import build_crud_router

router = build_crud_router(Lead, LeadCreate, prefix="/leads", tag="leads")
