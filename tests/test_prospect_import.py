"""Tests for the universal prospect-list importer and Store Leads normalization."""

from __future__ import annotations

from sqlmodel import Session, select

from sgml_sales.models import Lead
from sgml_sales.services.prospect_import import (
    import_from_csv,
    import_prospects,
    normalize_record,
    parse_revenue,
)
from sgml_sales.services.store_leads import _extract_list

# A Store-Leads-ish export with intentionally varied headers + a header BOM.
CSV = (
    "Store Name,Domain,Country,Platform,Category,Estimated Sales,Owner Email\n"
    "Northbound Skincare,northbound.ca,CA,Shopify,Skincare,\"$3,200,000\",owner@northbound.ca\n"
    "Maple Pet Co,maplepet.com,Canada,Shopify + Amazon,Pet,4.5M,\n"
    "Tiny Hobby Store,tinyhobby.ca,CA,Shopify,Crafts,250000,\n"          # below band
    "Yankee Goods,yankeegoods.com,US,Shopify,Home,5000000,\n"            # not Canadian
    ",,,,,,\n"                                                            # empty → invalid
)


def _write(tmp_path, text=CSV):
    p = tmp_path / "stores.csv"
    p.write_text(text, encoding="utf-8")
    return p


def test_parse_revenue_formats():
    assert parse_revenue("$3,200,000") == 3_200_000
    assert parse_revenue("4.5M") == 4_500_000
    assert parse_revenue("250k") == 250_000
    assert parse_revenue("$1M-$5M") == 1_000_000  # lower bound
    assert parse_revenue(2_000_000) == 2_000_000
    assert parse_revenue("n/a") is None
    assert parse_revenue("") is None


def test_import_maps_varied_headers_and_fields(session: Session, tmp_path):
    result = import_from_csv(session, _write(tmp_path), source="store-leads")

    # 4 real rows import (band/country filter OFF by default); the empty row is invalid.
    assert result.imported == 4
    assert result.skipped_invalid == 1

    by_name = {lead.name: lead for lead in session.exec(select(Lead)).all()}
    north = by_name["Northbound Skincare"]
    assert north.website == "northbound.ca"
    assert north.platform == "Shopify"
    assert north.category == "Skincare"
    assert north.est_revenue == 3_200_000
    assert north.email == "owner@northbound.ca"
    assert north.source == "store-leads"
    assert by_name["Maple Pet Co"].est_revenue == 4_500_000


def test_strict_icp_filter_drops_out_of_band_and_foreign(session: Session, tmp_path):
    result = import_from_csv(
        session,
        _write(tmp_path),
        source="store-leads",
        canada_only=True,
        min_revenue=1_000_000,
        max_revenue=10_000_000,
    )
    # Keeps the 2 Canadian in-band; drops the sub-$1M and the US row; empty is invalid.
    assert result.imported == 2
    assert result.filtered_out_icp == 2
    assert result.skipped_invalid == 1
    names = {lead.name for lead in session.exec(select(Lead)).all()}
    assert names == {"Northbound Skincare", "Maple Pet Co"}


def test_dedupe_by_website_on_reimport(session: Session, tmp_path):
    path = _write(tmp_path)
    import_from_csv(session, path, source="store-leads")
    again = import_from_csv(session, path, source="store-leads")
    assert again.imported == 0
    assert again.skipped_duplicate == 4


def test_normalize_record_from_api_shape():
    # Mimics a Store Leads API record (keys differ from CSV headers).
    raw = {
        "merchant_name": "Glow Labs",
        "domain": "glowlabs.ca",
        "country": "ca",
        "platform": "shopify",
        "categories": "Beauty",
        "estimated_sales": 2_750_000,
    }
    rec = normalize_record(raw)
    assert rec.name == "Glow Labs"
    assert rec.website == "glowlabs.ca"
    assert rec.est_revenue == 2_750_000
    assert rec.category == "Beauty"


def test_import_prospects_from_api_records(session: Session):
    rec = {"merchant_name": "Glow Labs", "domain": "glowlabs.ca", "estimated_sales": 2_750_000}
    records = [normalize_record(rec), normalize_record(dict(rec))]  # second row is a duplicate
    result = import_prospects(session, records, source="store-leads")
    assert result.imported == 1
    assert result.skipped_duplicate == 1


def test_extract_list_tolerates_response_shapes():
    assert _extract_list({"domains": [{"a": 1}]}) == [{"a": 1}]
    assert _extract_list({"results": [{"b": 2}]}) == [{"b": 2}]
    assert _extract_list([{"c": 3}]) == [{"c": 3}]
    assert _extract_list({"unexpected": 5}) == []
