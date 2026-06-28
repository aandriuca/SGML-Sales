"""Tests for lead status transitions and conversion to an opportunity."""

from __future__ import annotations


def _create(client, path, payload):
    resp = client.post(path, json=payload)
    assert resp.status_code == 201, resp.text
    return resp.json()


def test_set_status_moves_lead(client):
    lead = _create(
        client, "/leads", {"name": "Northbound Skincare", "source": "marketing-pipeline"}
    )
    assert lead["status"] == "new"

    resp = client.post(f"/leads/{lead['id']}/status", params={"status": "qualified"})
    assert resp.status_code == 200, resp.text
    assert resp.json()["status"] == "qualified"


def test_set_status_404_for_missing_lead(client):
    resp = client.post("/leads/999/status", params={"status": "qualified"})
    assert resp.status_code == 404


def test_convert_creates_customer_and_opportunity(client):
    lead = _create(client, "/leads", {"name": "Peak Supplements", "email": "owner@peak.test"})

    resp = client.post(f"/leads/{lead['id']}/convert", json={"amount": 30000, "probability": 0.2})
    assert resp.status_code == 201, resp.text
    opp = resp.json()

    # Opportunity is anchored to a (newly created) customer and back-links the lead.
    assert opp["lead_id"] == lead["id"]
    assert opp["customer_id"] is not None
    assert opp["stage"] == "qualification"
    assert opp["amount"] == 30000

    # The lead is now marked converted and linked to the same customer.
    refetched = client.get(f"/leads/{lead['id']}").json()
    assert refetched["status"] == "converted"
    assert refetched["customer_id"] == opp["customer_id"]

    # And it shows up in the pipeline report as open, weighted value.
    pipeline = client.get("/reports/pipeline").json()
    assert pipeline["open_opportunities"] == 1
    assert pipeline["weighted_pipeline_value"] == 6000  # 30000 * 0.2


def test_convert_links_existing_customer(client):
    customer = _create(client, "/customers", {"name": "Acme Co"})
    lead = _create(client, "/leads", {"name": "Acme lead"})

    resp = client.post(
        f"/leads/{lead['id']}/convert",
        json={"customer_id": customer["id"], "opportunity_name": "Acme retainer"},
    )
    assert resp.status_code == 201, resp.text
    opp = resp.json()
    assert opp["customer_id"] == customer["id"]
    assert opp["name"] == "Acme retainer"


def test_convert_twice_is_rejected(client):
    lead = _create(client, "/leads", {"name": "Twice Co"})
    assert client.post(f"/leads/{lead['id']}/convert", json={}).status_code == 201

    again = client.post(f"/leads/{lead['id']}/convert", json={})
    assert again.status_code == 409


def test_convert_unknown_customer_404(client):
    lead = _create(client, "/leads", {"name": "Ghost Co"})
    resp = client.post(f"/leads/{lead['id']}/convert", json={"customer_id": 999})
    assert resp.status_code == 404
