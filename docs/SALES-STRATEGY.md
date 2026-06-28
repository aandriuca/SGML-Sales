# SGML Sales — Sales Strategy

> Working strategy for building SGML Accounting's sales organization, captured from the
> virtual-VP-of-Sales mentoring sessions. This is a living document — refine as the motion
> is validated in market.

## The business in one line

SGML Accounting sells **bookkeeping, finance, accounting, taxation, and fractional-CFO
services** on a **recurring retainer** (~$2,500/month = **$30,000/year per client**) to
**Canadian e-commerce companies doing $1M–$10M in revenue**. B2B. Founder-led today
(single operator, no CRM yet).

## The goal

Reach **$10M in recurring (renewable) revenue**, incrementally — first milestone **$1M**,
then scale to **$10M** over time. Not $10M/year of new sales; $10M of standing,
renewable book.

## The revenue model (the whole game on one page)

Clean unit economics: **1 client = $30K/year recurring.**

| Milestone | Clients needed | Notes |
| --------- | -------------- | ----- |
| $1M       | ~34            | First target |
| $10M      | ~333           | At $30K ACV — a 333-client business |

### Two strategic levers (decided early)

1. **Raise average revenue per client.** If the blended average rises to ~$5K/mo
   ($60K/yr) by mixing in fractional-CFO / advisory tiers, then **$10M = ~167 clients
   instead of 333** — half the sales and delivery headcount for the same revenue. This is
   the single biggest lever to compress the timeline.
   - *Note:* The operator has indicated pricing is largely market-dictated and they know
     how to navigate it, so this lever is acknowledged but not the current focus.
2. **Retention compounds.** Accounting is sticky (90%+ annual retention when well served),
   so the base compounds — the job is mostly *adding*, not *replacing*. This is what makes
   a "renewable $10M" realistic. Early-stage risk is churn from bad-fit clients → protect
   with tight qualification.

### Capacity reality

$10M / 333 clients cannot be reached or delivered solo. It is a team build: multiple
quota-carrying closers plus a delivery team (a bookkeeper handles ~20–40 e-comm clients
depending on complexity; CFO work is heavier). Sales must run in sync with delivery
hiring. Raising ACV is the lever that shrinks both headcounts.

## Ideal Customer Profile (ICP) & wedge

**Wedge / positioning:** *Accounting and CFO services built specifically for Canadian
e-commerce operators.* The niche is the moat. Generic accountants don't understand:

- Shopify / Amazon / Stripe multi-channel reconciliation
- GST/HST across provinces
- US sales-tax nexus
- Inventory & COGS accounting
- Cash-flow forecasting around inventory buys

**ICP filters:** Canadian, e-commerce, $1M–$10M revenue, owner-operated.

**Why-now triggers to target:** tax / year-end season; scaling past $1M and "the books are
a mess"; outgrowing a cheap/overwhelmed bookkeeper; raising capital or a bank loan; a CRA
notice/audit; expanding into the US.

## Pipeline stages (the motion)

These map onto the SGML Sales app entities (Lead → Opportunity → Order → Invoice):

1. **Lead** — fits ICP (CA e-comm, $1–10M)
2. **Engaged** — replied / connected
3. **Discovery booked**
4. **Qualified (→ Opportunity)** — pain + decision-maker + trigger confirmed
5. **Proposal / scope sent**
6. **Verbal / negotiation**
7. **Closed-won** — engagement letter signed + pre-authorized debit set up
8. **Onboarded** — handed to delivery

### Qualification scorecard (gate into stage 4)

Mark a deal as a real Opportunity only if **all** hold:

- ✅ Canadian e-commerce doing $1M–$10M
- ✅ A *specific* pain they named
- ✅ The **owner / decision-maker is on the call**
- ✅ A why-now trigger
- ✅ $2.5K/mo is sane for their size

Miss two and it is not yet an opportunity — this protects time and win rate.

## The funnel to the first $1M (12-month view)

| Metric | Target | Basis |
| ------ | ------ | ----- |
| New clients | ~34 | $1M ÷ $30K |
| New clients / month | ~3 | 34 ÷ 12 |
| Qualified discovery calls / month | ~10 | at 30% close on right-fit deals |
| Calls booked / month | ~13 | ~75% show rate |
| Right-fit leads / month | ~30–40 | channel-dependent |

**Diagnostic rule:** if closing >30%, the problem is *top of funnel*; if not closing, the
problem is *qualification or offer*. Always know which lever to pull.

## Benchmarks (reference)

- Pipeline coverage: ~3–4× target in open pipeline.
- Quota: a rep's quota should be ~4–6× their OTE to be profitable.
- Win rate: ~20–30% qualified-opportunity → closed-won is healthy B2B.
- Ramp: 3–6 months for a new rep.

## Tooling stance

Don't let software become procrastination. **Start selling now** with a lightweight CRM
(HubSpot free or Pipedrive) or a tight spreadsheet using the 8 stages above; **evolve into
the SGML Sales app** as scale and the accounting/billing integration justify it.

## Operating model: virtual VP + skills

- **Now:** Claude runs as the **virtual VP of Sales** in these sessions — design, coach,
  review numbers, work stuck deals.
- **Once the motion is proven** (~5–10 closed the same repeatable way): **codify into
  Claude Code Skills** — e.g. `/qualify-lead`, `/draft-proposal`, `/weekly-pipeline-review`,
  `/prospect-research`. Don't automate an unproven process.

## Current focus

**Filling the funnel with cold leads** — see [`COLD-LEAD-PLAYBOOK.md`](COLD-LEAD-PLAYBOOK.md).
Referrals/partnerships are being worked separately by the operator.

## Open threads / next decisions

- ~~Tune the cold-outreach **voice** to match the SGML Marketing Pipeline philosophy
  (pending repo access).~~ **Done** — aligned to `pipeline/brand.py`; see
  [`OUTREACH-VOICE.md`](OUTREACH-VOICE.md) and the realigned Cold Lead Playbook templates.
- Define the tiered offer ladder to raise blended ACV (operator-led).
- Pick the interim CRM and load the 8 stages.
- ~~Build the first concrete skill or asset (candidate: `/draft-outreach`…).~~ **Done** —
  `/draft-outreach` skill built (`.claude/skills/draft-outreach/`). Next asset candidate:
  the Profit-Leak Checklist lead magnet.
