"""Product / service catalog entry."""

from __future__ import annotations

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sku: str = Field(index=True, unique=True)
    name: str
    description: str | None = None
    unit_price: float = Field(ge=0)
    active: bool = True
