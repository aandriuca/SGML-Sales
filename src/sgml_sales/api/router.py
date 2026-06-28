"""Aggregate router wiring every resource and report endpoint."""

from __future__ import annotations

from fastapi import APIRouter

from .routes import customers, invoices, leads, opportunities, orders, products, reports

api_router = APIRouter()
api_router.include_router(customers.router)
api_router.include_router(products.router)
api_router.include_router(leads.router)
api_router.include_router(opportunities.router)
api_router.include_router(orders.router)
api_router.include_router(invoices.router)
api_router.include_router(reports.router)
