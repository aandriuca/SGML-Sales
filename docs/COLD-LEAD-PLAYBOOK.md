# SGML Sales — Cold Lead Playbook

> How SGML Accounting fills the top of the funnel with cold leads: Canadian e-commerce
> owners ($1M–$10M revenue). Companion to [`SALES-STRATEGY.md`](SALES-STRATEGY.md).

## The model: cold is a 3-stage machine

**SOURCE** (build a list of the right owners) → **ENGAGE** (multi-channel outreach to start
conversations) → **NURTURE** (expose the not-yet-ready to the marketing channel until they
raise a hand).

Most operators only run the middle stage and grind. The edge here is running all three,
inside a tight niche.

---

## Stage 1 — SOURCE

Two questions: where to **scrape** a list, and where prospects **gather**.

### Build the target list from
- **Store Leads (storeleads.app)** — primary tool. Filter Shopify/Amazon stores by
  **country = Canada**, estimated revenue ($1M–$10M), platform, and tech stack (Klaviyo,
  Gorgias, ReCharge signal serious operators).
- **LinkedIn Sales Navigator** — geography = Canada, industry = retail/consumer goods,
  title = Founder/Owner/CEO, headcount 5–50 (revenue proxy).
- **BuiltWith / Commerce Inspector / Koala Inspector** — platform detection.
- **Apollo.io or Clay** — enrich into verified emails + LinkedIn URLs. **Clay** can run the
  whole source → enrich → score pipeline semi-automatically.
- **Funding / expansion news** — Canadian DTC brands announcing raises (a why-now trigger).

### Where they gather (be present)
- **LinkedIn** — #1 channel to reach owners directly.
- **Communities:** eCommerceFuel (premium), r/shopify, r/ecommerce, r/FulfillmentByAmazon,
  DTC Slack/Discord groups, Canadian e-comm Facebook groups.
- **Events:** Shopify meetups, Toronto/Vancouver e-comm conferences, trade shows.
- **Newsletters/podcasts:** 2PM, DTC newsletter, Lean Luxe (for sponsorship/guesting).

**Starting list size:** 500–1,000 right-fit accounts, worked in weekly batches.

---

## Stage 2 — ENGAGE: multi-channel sequence

For a $30K trust-heavy service, single-channel cold email is not enough. Combine LinkedIn +
email over ~3 weeks.

| Day | Channel | Touch |
| --- | ------- | ----- |
| 1 | LinkedIn | Connection request, **no pitch** |
| 2 | Email | #1 — trigger/problem-led, soft |
| 4 | LinkedIn | Engage with their post / light note after accept |
| 6 | Email | #2 — **value** (the Profit-Leak Checklist — what each channel really keeps) |
| 9 | Email | #3 — proof / mini case study (a founder who found the leak) |
| 12 | LinkedIn | Short message |
| 16 | Email | #4 — warm door-open (NOT a fake-urgency break-up) |
| After | Nurture | Non-responders → Stage 3 |

### Message formula (transformation-led — see [`OUTREACH-VOICE.md`](OUTREACH-VOICE.md))

The voice here is aligned to the SGML Marketing Pipeline brand (`pipeline/brand.py`):
**we sell the owner's transformation, never the service.** Don't name deliverables;
imply the expertise *through* the clarity we hand them.

1. **See them** — a specific, credible observation about life as a multi-platform
   Canadian operator, not a problem lecture.
2. **The thing only clarity reveals** — one concrete, grounded detail: what each
   channel actually *keeps*, the leak hiding in plain sight, the number they can't see.
3. **Who they become** — imply the edge clarity buys (stronger business, better
   decisions, standing apart from peers). Let expertise show through it.
4. **Soft CTA** — the free **Margin Leak Review** ("worth a 15-min look?"), or the
   **Profit-Leak Checklist** for those not ready. No fake urgency.

### Templates

> Voice varies touch to touch on purpose — witty, then warm, then a quick story — so the
> sequence never reads like a blast. Full rationale in [`OUTREACH-VOICE.md`](OUTREACH-VOICE.md).

**Email #1** — *Subject: your real margin, by channel*
> Hi {First} — when a brand sells across Shopify and Amazon (plus the odd Etsy or
> wholesale order), the one number that quietly goes missing is what each channel
> actually *keeps* after fees, shipping, refunds and reserves. Most owners your size run
> on blended gut-feel — and it's usually one channel quietly carrying the other. Worth a
> 15-minute look at where yours really nets out? No slides, just your numbers. — {You}

**Email #2** — *value · Subject: 12 places margin leaks on multi-channel*
> No pitch, {First} — just the checklist we run on multi-platform sellers: ~12 spots
> where margin quietly leaks (overstated COGS, shipping you never fully recover,
> marketplace reserves nobody reconciles, refund and chargeback drag…). Most owners spot
> one inside ten minutes that's worth real money. Want me to send it over?

**Email #3** — *proof · Subject: the founder who thought Amazon was winning*
> {First} — a supplements brand we work with (Shopify + Amazon, ~$4M) was sure Amazon was
> their star. Seen clean, Amazon was barely breaking even and the storefront was carrying
> the whole business. Same revenue, completely different decisions: they leaned into the
> channel that actually paid them and stopped feeding the one that didn't. That clarity is
> the whole game — curious what yours would show?

**Email #4** — *door-open (not a gimmick) · Subject: leaving the door open*
> {First}, I'll stop landing in your inbox — clearly not the moment, and I'd rather be
> useful than noise. If the day comes you want a clean read on what each channel really
> keeps, the offer stands. Either way the checklist is yours to keep. Good luck with the
> build. — {You}

**LinkedIn (after accept)**
> Thanks for connecting, {First}. Not here to pitch — I spend my days helping Canadian
> e-comm founders see what each of their channels actually keeps once Shopify, Amazon and
> the rest are untangled. If a clean read on your real margin would ever be useful, say
> the word; if not, glad to follow the build.

### Benchmarks to expect
- Email: ~40–60% open (good deliverability), **3–8% reply, 1–3% → meeting**.
- LinkedIn: ~25–35% accept, 5–15% reply.
- Multi-channel lifts lead→meeting toward **3–4%**.

### Activity math (to hit ~10 discovery calls/month)
At ~2–3% lead→meeting, touch **~400–600 fresh contacts/month** ≈ **20–30 new
prospects/day + ~50 follow-ups/day**. This daily number drives the whole funnel.

### Deliverability infrastructure (do not skip)
- **Separate sending domain** (e.g. `getsgml.ca`), not the primary domain.
- Warm 2–3 inboxes; cap ~30–50 sends/inbox/day.
- Configure **SPF / DKIM / DMARC**.
- Run through **Smartlead or Instantly** (email) + **Expandi/HeyReach** (LinkedIn), or
  **lemlist** for both.

---

## Stage 3 — NURTURE: the marketing channel

~95% of cold prospects aren't ready today — the trigger hasn't hit. Don't discard them;
stay in front of them until it does. This half compounds.

**Bridge = a lead magnet.** Offer it in outreach, capture the opt-in, then nurture.
Use the **same two assets the marketing channel uses** so the funnel is one system
(see the Marketing Director Strategy §4 in the pipeline repo):
- **TOFU — "The Profit-Leak Checklist for Multi-Platform Sellers"** (~12 places margin
  leaks): the lighter-touch capture for prospects not ready to talk — **drafted** at
  [`lead-magnets/profit-leak-checklist.md`](lead-magnets/profit-leak-checklist.md). *(A
  GST/HST & US-nexus guide is a fine secondary magnet for compliance-triggered prospects.)*
- **BOFU — the free "Margin Leak Review" (30 min)**: the primary CTA; a mini-version of
  the service and our tracked conversion (the booked call).
- Opt-ins flow into the **newsletter + LinkedIn content** (the marketing channel).
- On reply/click/booking → back into the active outreach sequence as a warm lead.

**The loop:** Outbound → lead magnet → marketing nurture → re-engage warm → discovery call.

---

## Marketing integration (SGML Marketing Pipeline)

The nurture **voice** and the outreach **voice** must be one system — and now they are.
The marketing brand philosophy lives in `aandriuca/SGML-Marketing-Pipeline` at
**`pipeline/brand.py`** (the `MESSAGING` + `VOICE` blocks), imported into every content
stage. The templates and formula above are aligned to it; the distilled rules live in
[`OUTREACH-VOICE.md`](OUTREACH-VOICE.md), with `brand.py` as the source of truth.

**What alignment changed (vs. the old provisional templates):**
- Outreach now sells the **owner's transformation**, never the service — no more "we
  handle books and CFO work" or compliance-led openers.
- Every message earns its promise with **one concrete, grounded detail** (what each
  channel keeps, the margin leak).
- Tone **varies touch to touch**; the fake-urgency "should I close your file?" break-up
  is gone, replaced by a warm door-open.
- Outreach and the marketing channel now offer the **same two assets** (Profit-Leak
  Checklist + Margin Leak Review).

**Data wiring (done):** the marketing pipeline's opt-in/lead output routes into SGML Sales
as `source = "marketing-pipeline"` leads via a **feed-only** importer that reads the
marketing lead-log CSV — it never modifies the marketing pipeline. See
[`MARKETING-LEAD-IMPORT.md`](MARKETING-LEAD-IMPORT.md).

---

## Tool stack

| Job | Tool |
| --- | ---- |
| Source list | Store Leads + LinkedIn Sales Navigator |
| Enrich emails | Apollo or Clay |
| Email sequencing | Smartlead / Instantly |
| LinkedIn sequencing | Expandi / HeyReach (or lemlist for both) |
| CRM / track | Pipedrive or HubSpot free → SGML Sales later |

---

## Suggested next artifacts

- ✅ **`/draft-outreach`** skill — **built** (`.claude/skills/draft-outreach/`): given a
  prospect/segment, returns a tailored LinkedIn + email sequence in the aligned voice,
  self-checked against `OUTREACH-VOICE.md`.
- ✅ **Lead-magnet asset** — **drafted**: the **Profit-Leak Checklist for Multi-Platform
  Sellers** ([`lead-magnets/profit-leak-checklist.md`](lead-magnets/profit-leak-checklist.md)),
  the linchpin between outbound and the marketing channel. Stand it up as a PDF / landing
  page with email capture. (A GST/HST + US-nexus guide is a fine secondary magnet.)
- ✅ **ICP filter spec** — **written** ([`ICP-FILTER-SPEC.md`](ICP-FILTER-SPEC.md)): the
  exact Store Leads / Sales Navigator filter set + disqualifiers for repeatable list pulls.
- ✅ **`/qualify-lead`** skill — **built** (`.claude/skills/qualify-lead/`): scores a
  prospect against the qualification scorecard and recommends the next pipeline action.
