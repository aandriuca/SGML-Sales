---
name: qualify-lead
description: >-
  Score a prospect or lead against SGML's qualification scorecard and return a
  verdict (qualified / not yet / disqualified), per-gate reasoning, and the next
  action. Use when the user wants to qualify a lead, decide if a deal is a real
  opportunity, prep or debrief a discovery call, or triage inbound/imported leads.
---

# /qualify-lead — apply SGML's qualification scorecard

Decide whether a prospect is a real **Opportunity** yet — protecting time and win
rate by not advancing bad-fit deals.

## Step 0 — load the scorecard (do this first)

Read `docs/SALES-STRATEGY.md` and use its **Qualification scorecard** and **ICP** as
the binding source. (Summarized below, but the doc wins if it has changed.) For
sourcing fit, `docs/ICP-FILTER-SPEC.md` is the reference.

## Step 1 — gather what's known

Take whatever the user provides — discovery-call notes, research, an imported lead.
Ask only for what's missing and material. You're assessing five gates:

1. **ICP fit** — Canadian e-commerce, **$1M–$10M** revenue, owner-operated, own
   storefront or hybrid (NOT marketplace-only).
2. **Specific named pain** — a concrete problem they articulated (not a vague "books
   are messy"): e.g. "we can't tell if Amazon makes money," "GST/HST is a guess."
3. **Decision-maker engaged** — the **owner** is the one talking, not a bookkeeper
   or finance staffer (who is often a barrier).
4. **Why-now trigger** — scaling past $1M, a raise, US expansion, year-end/CRA,
   outgrowing a cheap bookkeeper.
5. **Budget sanity** — **$2.5k/mo** is reasonable for their size.

## Step 2 — score each gate

Mark each **✅ pass / ❌ fail / ❓ unknown**, with one line of evidence. Treat ❓ as
not-yet-satisfied, and say what question would resolve it.

## Step 3 — verdict (apply the rule)

Per the strategy: a deal is a real Opportunity **only if all five hold**. **Miss two
→ not yet an opportunity.**

- **QUALIFIED** — all five pass. Advance to Opportunity.
- **NOT YET** — one gap (or unknowns). Nurturable; name the single thing to resolve.
- **DISQUALIFIED** — two+ fail, or a hard ICP miss (not Canadian, marketplace-only,
  wildly outside the revenue band). Don't burn cycles; route to nurture or drop.

Also flag the **diagnostic** from the strategy when relevant: if good-fit deals
aren't closing, the issue is qualification/offer, not top-of-funnel.

## Step 4 — next action (tie to the pipeline)

Recommend the concrete next step and the matching SGML Sales move:

- **QUALIFIED →** convert the lead to an opportunity:
  `POST /leads/{id}/convert` (creates/links the Customer + Opportunity at the
  *qualification* stage). Then propose scope.
- **NOT YET →** keep as a lead; `POST /leads/{id}/status` stays `new`/`qualified` as
  appropriate; put them on the nurture track (offer the Profit-Leak Checklist) and
  note the one trigger/answer to wait for.
- **DISQUALIFIED →** `POST /leads/{id}/status?status=unqualified`; nurture or drop.

## Output format

1. A short **scorecard table** — Gate | Verdict | Evidence.
2. The **verdict** (one of the three) + one-sentence rationale.
3. The **next action** (with the API call or sales step).
4. If useful, the **one question** that would move a NOT YET to a decision.

Keep it tight and decision-oriented — this is a triage aid, not an essay.
