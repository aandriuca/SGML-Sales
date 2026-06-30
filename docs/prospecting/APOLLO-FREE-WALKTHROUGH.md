# Apollo.io free-plan walkthrough — source leads for $0

A 5-minute, no-cost way to pull **Canadian e-commerce owners** (with emails) and load
them straight into SGML Sales. Apollo's free plan covers *both* finding the companies
*and* revealing a limited number of verified owner emails each month — rare for free.

> **Honest note on limits:** Apollo's free tier gives a *capped* number of email credits
> and exports per month (the exact numbers change over time). It's perfect for **dozens**
> of high-quality leads a month, not thousands. Check your current limits under
> Settings → Billing/Credits. When you outgrow it, a free **Store Leads** trial or
> Apollo's cheapest paid tier is the next step (the import works the same either way).

---

## Step 1 — sign up (free)

1. Go to **apollo.io** → **Sign up** (use your Google account — fastest).
2. Choose the **Free** plan. Skip/decline the paid upsell prompts — the free plan is
   enough to start.

## Step 2 — search for the right owners

In the left sidebar choose **Search → People** (people, so you get the owner + email,
with their company attached). Apply these filters (left panel):

**About the person**
- **Job Titles:** `Founder`, `Owner`, `CEO`, `Co-Founder`, `President`
  *(we sell owner-to-owner — skip bookkeepers/finance staff).*

**About the company**
- **Location / Company Location:** `Canada`
- **# Employees:** `1-10`, `11-20`, `21-50`
  *(this is your free stand-in for the $1M–$10M revenue band).*
- **Technologies:** `Shopify` *(targets real own-storefront operators — our wedge).*
- **Industry (optional):** `Retail`, `Consumer Goods`, `Apparel & Fashion`,
  `Health, Wellness & Fitness`, `Cosmetics`.

Tip: keep it broad at first (all categories), then narrow if you get too many.

## Step 3 — reveal emails & select

- The list shows people + companies. Click **Access Email** (or **Save**) on the ones
  that look right to reveal the verified email (this spends a free credit).
- Tick the checkboxes for the rows you want. Aim for a first batch of **25–50**.

## Step 4 — save to a list & export CSV

1. With rows selected → **Save to List** (name it e.g. `CA-ecom-batch1`).
2. Open the list → **Export** (top-right) → **CSV**.
3. Save the file.

## Step 5 — load it into SGML Sales

Drop the CSV into **`data/prospect-imports/`** and either tell me the filename, or run:

```bash
python -m sgml_sales.services.prospect_import data/prospect-imports/CA-ecom-batch1.csv
```

The importer already understands Apollo's column names (`Company`, `Company Domain`,
`Email`, `Industry`, `Company Country`…) — it maps them, dedupes by domain, and creates
leads tagged `source = "store-leads"` (rename with `--source apollo` if you like).

Then run **`/prospect-research`** on the strongest rows for the angle, and
**`/draft-outreach`** for the sequence.

## What Apollo gives us → what we keep

| Apollo column | Becomes (Lead field) |
| --- | --- |
| Company / Company Name | `name` |
| Company Domain / Website | `website` |
| Email | `email` |
| Industry | `category` |
| Company Country | `country` (used by `--strict` Canada filter) |

*Revenue isn't in a free Apollo export, so `est_revenue` stays empty — you filtered by
employee count instead, which is fine. The owner's personal name isn't stored yet (the
`Lead` has no contact-name field); flag me to add one if you want it on the record.*

## Free-stack summary

- **Apollo free** → companies + owner emails (capped monthly).
- **Hunter.io free** (~25 searches/mo) → backfill any missing emails.
- **Koala Inspector / Commerce Inspector** (free Chrome) → confirm Shopify while browsing.
- **Globe & Mail "Canada's Top Growing Companies" / Dragons' Den** → free, revenue-ranked
  Canadian names to seed searches.
- **Me** → web research to expand the candidate list at $0.
