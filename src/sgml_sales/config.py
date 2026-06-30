"""Application settings, loaded from environment / `.env`."""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "SGML Sales"
    environment: str = "development"
    debug: bool = True

    database_url: str = "sqlite:///./sgml_sales.db"

    # Company / branding — placeholders until sourced from SGML-Marketing-Pipeline.
    company_name: str = "[COMPANY NAME — placeholder]"
    company_currency: str = "USD"

    # Sourcing integrations. Set STORE_LEADS_API_KEY in .env to enable the
    # automatic Store Leads pull (services/store_leads.py). Optional.
    store_leads_api_key: str | None = None


settings = Settings()
