"""End-to-end-ish test walking a customer through the pipeline and the reports."""


def _create(client, path, payload):
    resp = client.post(path, json=payload)
    assert resp.status_code == 201, resp.text
    return resp.json()


def test_full_sales_flow_updates_reports(client):
    # 1. A customer enters the system.
    customer = _create(client, "/customers", {"name": "Acme Co", "email": "buyer@acme.test"})

    # 2. An opportunity is opened and pushed to negotiation.
    opp = _create(
        client,
        "/opportunities",
        {
            "name": "Acme annual deal",
            "customer_id": customer["id"],
            "stage": "negotiation",
            "amount": 50000,
            "probability": 0.5,
        },
    )

    pipeline = client.get("/reports/pipeline").json()
    assert pipeline["open_opportunities"] == 1
    assert pipeline["total_pipeline_value"] == 50000
    assert pipeline["weighted_pipeline_value"] == 25000

    # 3. Win the opportunity.
    won = client.post(f"/opportunities/{opp['id']}/stage", params={"stage": "closed_won"})
    assert won.status_code == 200
    pipeline = client.get("/reports/pipeline").json()
    assert pipeline["open_opportunities"] == 0
    assert pipeline["closed_won_value"] == 50000

    # 4. Invoice the customer, then collect payment.
    invoice = _create(
        client,
        "/invoices",
        {"customer_id": customer["id"], "amount": 50000, "status": "sent"},
    )

    accounting = client.get("/reports/accounting").json()
    assert accounting["accounts_receivable"] == 50000
    assert accounting["recognized_revenue"] == 0

    paid = client.post(f"/invoices/{invoice['id']}/pay")
    assert paid.status_code == 200
    assert paid.json()["status"] == "paid"

    accounting = client.get("/reports/accounting").json()
    assert accounting["accounts_receivable"] == 0
    assert accounting["recognized_revenue"] == 50000
