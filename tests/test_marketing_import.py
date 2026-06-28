"""Tests for the feed-only marketing lead importer."""

from __future__ import annotations

from sqlmodel import Session, select

from sgml_sales.core.enums import LeadStatus
from sgml_sales.models import Lead
from sgml_sales.services.marketing_import import (
    MARKETING_SOURCE,
    import_leads_from_csv,
)

# Mirrors the SGML-Marketing-Pipeline docs/lead-log-template.csv shape, including
# the shipped sample row that is meant to be deleted.
CSV = (
    "Date,Name / Business,Source,Magnet,Stage,Est $/mo,Notes\n"
    "2026-06-27,Example Co (delete this row),instagram,checklist,call-booked,2500,Sample\n"
    "2026-06-28,Northbound Skincare,linkedin,checklist,call-booked,2500,Carousel on cash flow\n"
    "2026-06-28,Peak Supplements,instagram,review,client,2500,Won after Margin Leak Review\n"
    "2026-06-28,Tidewater Goods,linkedin,checklist,lost,0,Went with in-house\n"
    "2026-06-28,,instagram,checklist,lead,2500,No name — should be skipped\n"
)


def _write_csv(tmp_path, text: str = CSV):
    path = tmp_path / "leads.csv"
    path.write_text(text, encoding="utf-8")
    return path


def test_import_creates_tagged_leads_and_skips_invalid(session: Session, tmp_path):
    result = import_leads_from_csv(session, _write_csv(tmp_path))

    # 3 real leads; the sample row and the nameless row are skipped as invalid.
    assert result.imported == 3
    assert result.skipped_invalid == 2
    assert result.skipped_duplicate == 0

    leads = session.exec(select(Lead)).all()
    assert {lead.name for lead in leads} == {
        "Northbound Skincare",
        "Peak Supplements",
        "Tidewater Goods",
    }
    # Every imported lead is tagged as coming from the marketing pipeline.
    assert all(lead.source == MARKETING_SOURCE for lead in leads)


def test_stage_maps_to_lead_status(session: Session, tmp_path):
    import_leads_from_csv(session, _write_csv(tmp_path))
    by_name = {lead.name: lead for lead in session.exec(select(Lead)).all()}

    assert by_name["Peak Supplements"].status == LeadStatus.CONVERTED  # client
    assert by_name["Tidewater Goods"].status == LeadStatus.UNQUALIFIED  # lost
    assert by_name["Northbound Skincare"].status == LeadStatus.NEW  # call-booked


def test_reimport_is_idempotent(session: Session, tmp_path):
    path = _write_csv(tmp_path)
    import_leads_from_csv(session, path)

    # Re-importing the same export creates nothing new — every row dedupes.
    again = import_leads_from_csv(session, path)
    assert again.imported == 0
    assert again.skipped_duplicate == 3

    assert len(session.exec(select(Lead)).all()) == 3
