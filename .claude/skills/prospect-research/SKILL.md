---
name: prospect-research
description: >-
  Research a specific company (or a segment) and produce an ICP-fit assessment plus
  a tailored outreach angle for SGML. Use when the user wants to research a prospect,
  vet a brand, build/enrich a target list, find the owner, or prep a personalized
  first touch for a Canadian e-commerce business. Pairs with /qualify-lead (post-call
  scoring) and /draft-outreach (writes the sequence).
---

# /prospect-research — turn a name into a warm, personalized first touch

The homework step between the ICP spec and outreach: research a prospect, judge fit,
and surface the *one specific thing* that makes a first touch land.

## Step 0 — load the targeting spec

Read `docs/ICP-FILTER-SPEC.md` (hard filters, soft signals, disqualifiers) and
`docs/SALES-STRATEGY.md` (ICP + why-now triggers). Those define fit; this skill
gathers the evidence. The outreach voice lives in `docs/OUTREACH-VOICE.md`.

## Step 1 — take the input

- **A specific brand/domain** → research that one.
- **A segment** (e.g. "Canadian supplement brands on Shopify ~$2–5M") → propose a
  shortlist of candidates, then research the top few.

## Step 2 — research (use web search/fetch; be honest about confidence)

For each prospect, try to establish:

- **What they sell** + niche (skincare/supplements = strongest fit).
- **Platforms** — own Shopify storefront? Also Amazon / Etsy / eBay (hybrid = ideal)?
  Marketplace-**only** = disqualify.
- **Canadian?** — owner/HQ Canadian-taxed (the wedge depends on it).
- **Rough size** — proxy from team size, store traffic, press, funding. **$1M–$10M**
  is the band. Revenue from the open web is an *estimate* — say so.
- **The owner / decision-maker** — name + LinkedIn if findable (we sell owner-to-owner).
- **A why-now trigger** — a raise, US expansion, scaling past $1M, a new marketplace,
  hiring finance, year-end/CRA season, a public "ops are a mess" signal.

**Cite sources** for non-obvious claims. Mark anything you couldn't verify as
`unverified` — never invent revenue, ownership, or contact details.

## Step 3 — score fit

Rate **STRONG / POSSIBLE / WEAK / DISQUALIFIED** against the hard filters:

- DISQUALIFIED on any hard miss (not Canadian, marketplace-only, clearly outside
  $1M–$10M).
- STRONG when hard filters hold *and* a soft signal or trigger is present.
- Note the single biggest **unknown to verify** (usually revenue or owner contact)
  and where to confirm it (Store Leads / Sales Navigator / their About page).

## Step 4 — find the angle

The payoff: one **specific, grounded observation** that becomes the opener — tied to
*their* world (the platforms they juggle, a recent move, their category's margin
traps). This feeds the "see them" + "the thing only clarity reveals" beats of the
outreach formula. Keep it true and non-creepy; no faux-personal filler.

## Step 5 — output

Per prospect, a compact card:

- **Brand** — one line on what they sell.
- **Fit:** STRONG/POSSIBLE/WEAK/DISQUALIFIED — one-line why.
- **Platforms / Canadian / est. size** — with confidence + source.
- **Owner:** name + LinkedIn (or `unknown — find via Sales Navigator`).
- **Why-now trigger:** … (or `none found`).
- **Angle:** the one specific observation to open with.
- **Verify next:** the single thing to confirm before working the lead.
- **→ Hand off:** "run `/draft-outreach` with this angle" for STRONG/POSSIBLE.

End with a one-line note: import the worked rows into SGML Sales as leads (tag the
`source`), and that open-web revenue figures are estimates to confirm in the sourcing
tools before spending real outreach effort.
