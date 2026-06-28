"""Customer endpoints."""

from ...models import Customer
from ...schemas import CustomerCreate
from ..crud import build_crud_router

router = build_crud_router(Customer, CustomerCreate, prefix="/customers", tag="customers")
