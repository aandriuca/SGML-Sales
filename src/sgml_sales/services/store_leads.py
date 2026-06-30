"""Automatic Store Leads pull (optional, key-gated).

If you have a paid Store Leads account with API access, set ``STORE_LEADS_API_KEY``
in ``.env`` and this fetches a Canada + $1M–$10M store list directly — no manual
export — then loads it as leads via the shared ``prospect_import`` normalizer.

    python -m sgml_sales.services.store_leads --max 250 --dry-run   # preview
    python -m sgml_sales.services.store_leads --max 250             # load leads

⚠️ VERIFY-ONCE: the Store Leads API docs are behind a login, so the exact search
path and filter parameter names below are best-effort defaults. Confirm them once
against your account's **API tab** (storeleads.app → Account → API) and tweak the
two constants `SEARCH_PATH` / `FILTER_PARAMS` if needed. The record→lead mapping
(the part that matters for us) is shared with prospect_import and unit-tested, so
only the request shape might need a small adjustment.
"""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.parse
import urllib.request

from sqlmodel import Session

from ..config import settings
from .prospect_import import (
    DEFAULT_SOURCE,
    ICP_MAX_REVENUE,
    ICP_MIN_REVENUE,
    ImportResult,
    import_prospects,
    normalize_record,
)

BASE_URL = "https://storeleads.app"
SEARCH_PATH = "/api/v1/all"  # VERIFY against your account's API tab
HTTP_METHOD = "GET"

# Our filter intent → Store Leads' query-param names. VERIFY these names.
FILTER_PARAMS = {
    "country": "country_codes",
    "platform": "platform",
    "min_revenue": "estimated_sales_min",
    "max_revenue": "estimated_sales_max",
    "limit": "limit",
}

# Keys under which the response might carry the list of stores (be tolerant).
_LIST_KEYS = ("domains", "data", "results", "stores", "items")


class StoreLeadsError(RuntimeError):
    pass


def _resolve_key(api_key: str | None) -> str:
    key = api_key or settings.store_leads_api_key
    if not key:
        raise StoreLeadsError(
            "No Store Leads API key. Set STORE_LEADS_API_KEY in .env or pass api_key=..."
        )
    return key


def fetch_stores(
    *,
    api_key: str | None = None,
    country: str = "ca",
    platform: str | None = "shopify",
    min_revenue: float | None = ICP_MIN_REVENUE,
    max_revenue: float | None = ICP_MAX_REVENUE,
    limit: int = 100,
    base_url: str = BASE_URL,
    search_path: str = SEARCH_PATH,
    timeout: float = 30.0,
) -> list[dict]:
    """Call the Store Leads search API and return the raw list of store records.

    Network only happens here, and only when called. Raises StoreLeadsError on
    auth/transport/parse failure.
    """
    key = _resolve_key(api_key)

    intent = {
        "country": country,
        "platform": platform,
        "min_revenue": int(min_revenue) if min_revenue is not None else None,
        "max_revenue": int(max_revenue) if max_revenue is not None else None,
        "limit": limit,
    }
    params = {
        FILTER_PARAMS[k]: v for k, v in intent.items() if v is not None and k in FILTER_PARAMS
    }
    url = f"{base_url}{search_path}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(url, method=HTTP_METHOD)
    req.add_header("Authorization", f"Bearer {key}")
    req.add_header("Accept", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (https only)
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:  # pragma: no cover - network
        raise StoreLeadsError(f"Store Leads API {e.code}: {e.reason}") from e
    except (urllib.error.URLError, TimeoutError, ValueError) as e:  # pragma: no cover - network
        raise StoreLeadsError(f"Store Leads request failed: {e}") from e

    return _extract_list(payload)


def _extract_list(payload: object) -> list[dict]:
    """Pull the store list out of the response, tolerating shape differences."""
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    if isinstance(payload, dict):
        for k in _LIST_KEYS:
            if isinstance(payload.get(k), list):
                return [r for r in payload[k] if isinstance(r, dict)]
    return []


def import_from_store_leads(
    session: Session,
    *,
    api_key: str | None = None,
    source: str = DEFAULT_SOURCE,
    **fetch_opts,
) -> ImportResult:
    """Fetch from Store Leads and load the results as leads."""
    raw = fetch_stores(api_key=api_key, **fetch_opts)
    records = [normalize_record(r) for r in raw]
    return import_prospects(session, records, source=source)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Pull a Canada $1-10M store list from Store Leads")
    parser.add_argument("--country", default="ca")
    parser.add_argument("--platform", default="shopify")
    parser.add_argument("--max", type=int, default=100, help="Max stores to fetch.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and preview; don't write.")
    args = parser.parse_args(argv)

    try:
        raw = fetch_stores(country=args.country, platform=args.platform, limit=args.max)
    except StoreLeadsError as e:
        print(f"ERROR: {e}")
        return 1

    if args.dry_run:
        print(f"Fetched {len(raw)} store(s). Sample normalized record:")
        if raw:
            print(normalize_record(raw[0]))
        return 0

    from ..database import engine, init_db

    init_db()
    with Session(engine) as session:
        records = [normalize_record(r) for r in raw]
        result = import_prospects(session, records, source=DEFAULT_SOURCE)
    print(f"Store Leads import: {result}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
