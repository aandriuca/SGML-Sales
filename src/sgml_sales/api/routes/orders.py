"""Order endpoints."""

from ...models import Order
from ...schemas import OrderCreate
from ..crud import build_crud_router

router = build_crud_router(Order, OrderCreate, prefix="/orders", tag="orders")
