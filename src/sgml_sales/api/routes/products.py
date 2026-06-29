"""Product catalog endpoints."""

from ...models import Product
from ...schemas import ProductCreate
from ..crud import build_crud_router

router = build_crud_router(Product, ProductCreate, prefix="/products", tag="products")
