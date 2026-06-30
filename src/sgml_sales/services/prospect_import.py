"""Universal prospect-list importer.

Drop in a CSV exported from **Store Leads, Apollo, Clay, LinkedIn Sales Navigator,
or a plain spreadsheet** and this turns each row into a `Lead` in SGML Sales —
mapping messy column names, parsing revenue, applying the ICP filter, deduping,
and tagging the source.

It is deliberately tolerant of header variations (each tool names columns
differently) and is the shared core behind both the CSV path and the Store Leads
API path (`services/store_leads.py`), so the record→lead mapping is written and
tested once.

Typical flow:
    Store Leads/Apollo/Clay export  ->  import_from_csv(...)  ->  scored Leads
"""

from __future__ import annotations

import argparse
import csv
import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TextIO

from sqlmodel import Session, select

from ..models import Lead

DEFAULT_SOURCE = "store-leads"

# ICP revenue band (USD) — the $1M–$10M sweet spot from SALES-STRATEGY.
ICP_MIN_REVENUE = 1_000_000.0
ICP_MAX_REVENUE = 10_000_000.0

# Header aliases → canonical field. Lower-cased, stripped before lookup.
_ALIASES: dict[str, tuple[str, ...]] = {
    "name": ("name", "name / business", "business", "store name", "merchant name",
             "company", "company name", "store", "merchant"),
    "website": ("website", "domain", "url", "store url", "homepage", "site", "domain name"),
    "email": ("email", "owner email", "contact email", "work email", "email address"),
    "country": ("country", "country code", "location", "merchant location", "region"),
    "platform": ("platform", "platforms", "ecommerce platform", "tech platform"),
    "category": ("category", "vertical", "categories", "industry", "niche"),
    "revenue": ("est_revenue", "estimated revenue", "revenue", "estimated sales",
                "estimated annual sales", "annual sales", "sales", "estimated monthly sales",
                "est. revenue", "est revenue"),
}

# Country values we treat as Canadian.
_CANADA = {"ca", "can", "canada"}


@dataclass
class ProspectRecord:
    """A normalized prospect, tool-agnostic."""

    name: str
    website: str | None = None
    email: str | None = None
    country: str | None = None
    platform: str | None = None
    category: str | None = None
    est_revenue: float | None = None


@dataclass
class ImportResult:
    imported: int = 0
    skipped_duplicate: int = 0
    skipped_invalid: int = 0
    filtered_out_icp: int = 0
    leads: list[Lead] = field(default_factory=list)

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return (
            f"imported={self.imported} duplicate={self.skipped_duplicate} "
            f"invalid={self.skipped_invalid} filtered_icp={self.filtered_out_icp}"
        )


def _norm_key(s: str | None) -> str:
    """Lower-case and collapse separators so 'merchant_name', 'Merchant Name',
    and 'merchant-name' all match the same alias."""
    s = (s or "").strip().lower()
    s = re.sub(r"[_\-]+", " ", s)
    return re.sub(r"\s+", " ", s)


# Aliases pre-normalized once, so CSV headers and API keys resolve identically.
_NORM_ALIASES: dict[str, tuple[str, ...]] = {
    canonical: tuple(_norm_key(a) for a in aliases) for canonical, aliases in _ALIASES.items()
}


_REV_SUFFIX = {"k": 1_000, "m": 1_000_000, "b": 1_000_000_000}


def parse_revenue(value: str | float | int | None) -> float | None:
    """Parse '$1.2M', '1,200,000', '2.5m', '$1M-$5M' → a float (USD).

    For a range, the lower bound is used (a conservative estimate).
    Returns None if nothing numeric can be read.
    """
    if value is None:
        return None
    if isinstance(value, int | float):
        return float(value) or None
    text = value.strip().lower().replace("$", "").replace(",", "").replace("usd", "").strip()
    if not text:
        return None
    # Range like "1m-5m" / "1m to 5m" → take the first (lower) number.
    first = re.split(r"\s*(?:-|–|to)\s*", text)[0].strip()
    m = re.match(r"^([0-9]*\.?[0-9]+)\s*([kmb])?$", first)
    if not m:
        return None
    num = float(m.group(1))
    if m.group(2):
        num *= _REV_SUFFIX[m.group(2)]
    return num or None


def normalize_record(raw: dict) -> ProspectRecord:
    """Turn a raw export row (CSV) or API record into a ProspectRecord.

    Keys are matched against the aliases regardless of separators/case, so the
    same function handles every tool's column naming and the API's JSON keys.
    """
    norm = {_norm_key(k): v for k, v in raw.items()}

    def get(canonical: str) -> object:
        for alias in _NORM_ALIASES[canonical]:
            if alias in norm:
                return norm[alias]
        return None

    def clean(v: object) -> str | None:
        s = str(v).strip() if v is not None else ""
        return s or None

    return ProspectRecord(
        name=clean(get("name")) or "",
        website=clean(get("website")),
        email=clean(get("email")),
        country=clean(get("country")),
        platform=clean(get("platform")),
        category=clean(get("category")),
        est_revenue=parse_revenue(get("revenue")),
    )


def passes_icp(
    rec: ProspectRecord,
    *,
    canada_only: bool,
    min_revenue: float | None,
    max_revenue: float | None,
) -> bool:
    """Hard ICP gate. Unknown values pass (don't drop on missing data)."""
    if canada_only and rec.country is not None:
        if _norm_key(rec.country) not in _CANADA:
            return False
    if rec.est_revenue is not None:
        if min_revenue is not None and rec.est_revenue < min_revenue:
            return False
        if max_revenue is not None and rec.est_revenue > max_revenue:
            return False
    return True


def _dedupe_key(rec: ProspectRecord) -> str:
    return _norm_key(rec.website) or _norm_key(rec.name)


def import_prospects(
    session: Session,
    records: Iterable[ProspectRecord],
    *,
    source: str = DEFAULT_SOURCE,
    canada_only: bool = False,
    min_revenue: float | None = None,
    max_revenue: float | None = None,
) -> ImportResult:
    """Create Leads from normalized prospect records.

    Idempotent: dedupes on website (else name) against existing leads of the same
    source and within the batch. Pass min/max revenue and canada_only to enforce
    the ICP band as a hard filter (off by default — assume the export was filtered
    at source).
    """
    result = ImportResult()

    existing: set[str] = set()
    for lead in session.exec(select(Lead).where(Lead.source == source)).all():
        existing.add(_norm_key(lead.website) or _norm_key(lead.name))

    for rec in records:
        if not rec.name and not rec.website:
            result.skipped_invalid += 1
            continue
        if not passes_icp(
            rec, canada_only=canada_only, min_revenue=min_revenue, max_revenue=max_revenue
        ):
            result.filtered_out_icp += 1
            continue
        key = _dedupe_key(rec)
        if key in existing:
            result.skipped_duplicate += 1
            continue

        lead = Lead(
            name=rec.name or rec.website or "(unknown)",
            email=rec.email,
            source=source,
            website=rec.website,
            category=rec.category,
            platform=rec.platform,
            est_revenue=rec.est_revenue,
        )
        session.add(lead)
        existing.add(key)
        result.leads.append(lead)
        result.imported += 1

    if result.imported:
        session.commit()
        for lead in result.leads:
            session.refresh(lead)
    return result


def import_from_rows(session: Session, rows: Iterable[dict], **opts) -> ImportResult:
    return import_prospects(session, (normalize_record(row) for row in rows), **opts)


def import_from_csv(session: Session, source_csv: str | Path | TextIO, **opts) -> ImportResult:
    """Import prospects from a CSV path or open text stream."""
    if isinstance(source_csv, str | Path):
        with Path(source_csv).open(newline="", encoding="utf-8-sig") as fh:
            return import_from_rows(session, list(csv.DictReader(fh)), **opts)
    return import_from_rows(session, list(csv.DictReader(source_csv)), **opts)


def main(argv: list[str] | None = None) -> int:
    """CLI: python -m sgml_sales.services.prospect_import <export.csv> [--strict] ..."""
    parser = argparse.ArgumentParser(
        description="Import a prospect list (Store Leads/Apollo/Clay/CSV) into SGML Sales."
    )
    parser.add_argument("csv_path", help="Path to the exported prospect CSV.")
    parser.add_argument("--source", default=DEFAULT_SOURCE, help="Lead.source tag.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=f"Enforce the ICP band (Canada + ${ICP_MIN_REVENUE:,.0f}-${ICP_MAX_REVENUE:,.0f}).",
    )
    args = parser.parse_args(argv)

    from ..database import engine, init_db

    init_db()
    opts = {}
    if args.strict:
        opts = {"canada_only": True, "min_revenue": ICP_MIN_REVENUE, "max_revenue": ICP_MAX_REVENUE}
    with Session(engine) as session:
        result = import_from_csv(session, args.csv_path, source=args.source, **opts)
    print(f"Prospect import [{args.source}]: {result}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
