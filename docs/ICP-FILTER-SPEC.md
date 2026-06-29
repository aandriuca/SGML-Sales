# ICP Filter Spec — repeatable right-fit list pulls

> The exact filter set for sourcing SGML's ideal prospects, so every list pull is
> consistent instead of reinvented each batch. Companion to
> [`SALES-STRATEGY.md`](SALES-STRATEGY.md) (the ICP) and
> [`COLD-LEAD-PLAYBOOK.md`](COLD-LEAD-PLAYBOOK.md) (Stage 1 — Source).

## The ICP in one line

**Canadian-owned e-commerce brands, $1M–$10M revenue, owner-operated, selling on
their own storefront and often also on marketplaces (hybrid).** Exclude
marketplace-only sellers. The reader/buyer is the **owner**.

## Hard filters (must all hold)

| Filter | Target | Why |
| --- | --- | --- |
| **Country** | Canada (HQ / owner Canadian-taxed) | The tax + multi-province GST/HST wedge only applies to Canadian-taxed owners. |
| **Revenue** | **$1M–$10M / yr** | Below $1M can't afford us; above $10M hires in-house. |
| **Model** | Own storefront, or **hybrid** (store + marketplaces) | Marketplace-*only* sellers are excluded (fly-by-night, not our fit). |
| **Decision-maker** | Founder / Owner / CEO reachable | We sell owner-to-owner; a bookkeeper is a barrier, not the buyer. |
| **Platform** | Shopify (primary), +Amazon / Etsy / eBay | Multi-platform = the reconciliation pain we're built for. |

## Soft signals (prioritize, don't require)

- **Serious-operator tech:** Klaviyo, Gorgias, ReCharge, Recharge/Loop, a 3PL.
- **Niche anchor:** skincare, supplements, cosmetics, wellness (strongest fit) —
  but keep the net wide across e-commerce.
- **Why-now triggers:** funding/raise announced, scaling past $1M, hiring finance,
  US expansion, "books are a mess" signals, CRA notice season / year-end.

---

## Tool 1 — Store Leads (storeleads.app) — primary list build

Filter set:

- **Country = Canada**
- **Platform = Shopify** (run a second pass for **Shopify + Amazon** where exposed)
- **Estimated revenue / sales = $1M–$10M** (or the closest band: e.g. 1M–5M, 5M–10M)
- **Tech / apps (any of, as quality signal):** Klaviyo, Gorgias, ReCharge
- **Category (optional niche pass):** Health & Beauty / Supplements / Cosmetics

Export columns to keep: store name, domain, est. revenue, platform(s), tech stack,
country, contact (if present). Tag the pull with its date + filter preset name.

## Tool 2 — LinkedIn Sales Navigator — find the owner

Filter set (revenue is proxied by headcount here):

- **Geography = Canada**
- **Industry = Retail / Consumer Goods / Apparel & Fashion / Health, Wellness & Fitness**
- **Company headcount = 11–50** (and a 2nd pass at **1–10** for lean DTC)
- **Seniority = Owner / Founder / CXO**
- **Title contains = Founder / Owner / CEO / Co-founder**
- *(Optional)* **Keywords = Shopify, e-commerce, DTC, Amazon**

Use this to attach a **named owner + LinkedIn URL** to each Store Leads domain.

## Tool 3 — Enrichment (Apollo.io or Clay)

- Match the Store Leads domain + the Sales Navigator person → **verified work email**
  + LinkedIn URL.
- **Clay** can run source → enrich → score end to end; have it flag rows missing a
  revenue signal or an owner contact for manual review.

## Disqualify / drop a row if

- Marketplace-**only** (no own storefront).
- Revenue clearly < $1M or > $10M.
- Not Canadian-taxed.
- Only a generic info@ / no reachable owner after enrichment (park in nurture, not
  active outreach).

---

## Output → SGML Sales

Land the cleaned list as one row per account; when worked, they become **leads with
`source = "marketing-pipeline"`** (if they came via content) or another source tag,
and flow through the importer / API. See
[`MARKETING-LEAD-IMPORT.md`](MARKETING-LEAD-IMPORT.md).

**Starting target:** 500–1,000 right-fit accounts, worked in weekly batches (per the
playbook's activity math).

## Saved presets (fill in once configured)

| Preset name | Tool | Notes |
| --- | --- | --- |
| `CA-Shopify-1to10M` | Store Leads | Base pull |
| `CA-Shopify-Amazon-hybrid` | Store Leads | Hybrid pass |
| `CA-founders-retail-11to50` | Sales Navigator | Owner match |
| `CA-skincare-supplements` | Store Leads | Niche pass |
