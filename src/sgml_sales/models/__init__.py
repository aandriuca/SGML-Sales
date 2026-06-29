"""SQLModel table definitions. Importing this package registers all tables."""

from .customer import Customer
from .invoice import Invoice
from .lead import Lead
from .opportunity import Opportunity
from .order import Order
from .product import Product

__all__ = ["Customer", "Invoice", "Lead", "Opportunity", "Order", "Product"]
