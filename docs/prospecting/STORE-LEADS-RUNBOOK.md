# Store Leads Sourcing Runbook

> The repeatable, do-this-now recipe for pulling a right-fit Canadian e-commerce list
> from **Store Leads (storeleads.app)**, enriching it to reachable owners, and handing
> it to SGML Sales as worked leads. Extends [`../ICP-FILTER-SPEC.md`](../ICP-FILTER-SPEC.md)
> into an export workflow.

## Why Store Leads (the honest reason)

You can't reliably estimate a private store's revenue from the open web — DTC brands
don't publish it. Store Leads exists precisely to **estimate Shopify/Amazon store
revenue and filter by country + band**, which is the one filter that matters most for
us ($1M–$10M). That's why it's the primary tool, not web scraping. Treat its revenue
figure as a good *estimate* — a filter, not gospel; sanity-check obvious outliers.

## How big a list do we even need? (the 35-client math)

Year-one goal = **35 clients**. Working backward through the funnel
([`../SALES-STRATEGY.md`](../SALES-STRATEGY.md), [`../COLD-LEAD-PLAYBOOK.md`](../COLD-LEAD-PLAYBOOK.md)):

| Stage | Monthly | Basis |
| --- | --- | --- |
| New clients | ~3 | 35 ÷ 12 |
| Qualified discovery calls | ~10 | at ~30% close |
| Calls booked | ~13 | ~75% show |
| Right-fit leads | ~30–40 | channel-dependent |
| Fresh contacts touched | ~400–600 | at 2–3% lead→meeting |

→ **Source 500–1,000 right-fit accounts** and work them in **weekly batches of ~125**
(≈ 25 fresh/day × 5 days). You do NOT need to find every store — just keep ~1,000
good ones flowing. Scope is **all Canadian e-commerce categories**; skincare/supplements
is just the warmest entry point, not the boundary.

---

## Step 1 — the Store Leads filter set

Apply these filters (a base pass, then variations):

- **Country = Canada** (HQ / merchant location).
- **Platform = Shopify** (run a second pass surfacing stores that *also* sell on
  Amazon — hybrid sellers are the sweet spot).
- **Estimated sales / revenue = $1M–$10M** (pick the bands that cover it, e.g. $1–5M
  and $5–10M).
- **Apps / tech (quality signal, any of):** Klaviyo, Gorgias, ReCharge — serious
  operators, not hobby stores.
- **Exclude** brand-new domains (< ~1 yr) to avoid fly-by-night stores.

**Sort:** by estimated revenue (desc) for the biggest-fit first, or by "recently
updated/active" to favor live stores.

### Saved presets to create (name them in Store Leads)

| Preset | Filters |
| --- | --- |
| `CA-Shopify-1to5M` | Canada · Shopify · $1–5M |
| `CA-Shopify-5to10M` | Canada · Shopify · $5–10M |
| `CA-hybrid-Amazon` | Above + Amazon channel detected |
| `CA-serious-stack` | Above + Klaviyo/Gorgias/ReCharge |

## Step 2 — export these columns

Export the list to CSV. Keep at minimum:

- **Store / business name**
- **Domain / URL**
- **Estimated sales / revenue** (the band or figure)
- **Platform(s)** + **category / vertical**
- **Tech stack** (apps detected)
- **Country / region**
- **Contact email** (if present) + **social links**
- **Employee count** (if present — a second revenue proxy)

## Step 3 — enrich to a reachable owner (the missing piece)

Store Leads gives you **domains, not owners**. We sell owner-to-owner, so enrich:

- Run the domains through **Apollo.io** or **Clay** to get **founder/owner name +
  verified email + LinkedIn URL**.
- **Clay** can chain the whole thing: import the Store Leads list → enrich → score →
  export. If you set it up once, this becomes a near-automatic weekly pull.
- Cross-check the owner with **LinkedIn Sales Navigator** (Canada · Founder/Owner/CEO ·
  headcount 1–50) where Apollo/Clay come up empty.

Drop any row that's **marketplace-only**, clearly outside $1–10M, not Canadian, or has
no reachable owner after enrichment (park those in nurture, not active outreach).

## Step 4 — load it into SGML Sales (automated)

The `Lead` model now carries `website`, `category`, `platform`, and `est_revenue`, so an
enriched export lands with its full context. Two ways in:

### A) One command from a CSV export (any tool)

Export from Store Leads (or Apollo/Clay/a spreadsheet) and run:

```bash
python -m sgml_sales.services.prospect_import path/to/export.csv
# enforce the ICP band as a hard filter (Canada + $1M–$10M):
python -m sgml_sales.services.prospect_import path/to/export.csv --strict
```

It **maps the columns for you** (tolerant of each tool's header names — `Store Name` /
`merchant_name` / `Company` all resolve), parses revenue (`$3.2M`, `1,200,000`, `2.5m`),
**dedupes** by domain (idempotent re-runs), tags `source = "store-leads"`, and prints a
summary (`imported / duplicate / invalid / filtered_icp`). Ideal export columns: business
name, domain, owner email, est. revenue, platform, category, country.

### B) Zero-touch via the Store Leads API (paid API access)

If your Store Leads plan includes API access, set the key once and skip the manual export:

```bash
# .env
STORE_LEADS_API_KEY=sl_...

python -m sgml_sales.services.store_leads --max 250 --dry-run   # preview
python -m sgml_sales.services.store_leads --max 250             # fetch + load leads
```

> One-time setup: the API docs are behind a login, so confirm the exact search path /
> filter names against your account's **API tab** and adjust the two marked constants in
> `services/store_leads.py` if needed. The record→lead mapping is shared with the CSV path
> and unit-tested, so only the request shape might need a tiny tweak.

Then run **`/prospect-research`** on the strongest rows for the angle, and
**`/draft-outreach`** for the sequence.

## Step 5 — work it

- Load the batch into the interim CRM (Pipedrive/HubSpot) or the SGML Sales pipeline.
- Run the multi-channel sequence from the Cold Lead Playbook (~125/week).
- Feed non-responders into the marketing nurture (the Profit-Leak Checklist).

## A note on tools & ToS

Use the data tools (Store Leads, Apollo, Clay, Sales Navigator) under their terms —
they license this data. That's cleaner and far more reliable than scraping storefronts
directly, and it's the same data the "find-the-right-store" pitches are really built on.
