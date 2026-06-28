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
| 6 | Email | #2 — **value** (e.g. "3 GST/HST mistakes Shopify sellers make") |
| 9 | Email | #3 — proof / mini case study |
| 12 | LinkedIn | Short message |
| 16 | Email | #4 — break-up ("should I close your file?") |
| After | Nurture | Non-responders → Stage 3 |

### Message formula (lead with *them*, never the service)
1. **Observation** specific to their segment.
2. **Problem/cost** — the pain.
3. **Proof** — "we do this *only* for Canadian e-comm operators your size."
4. **Soft CTA** — low friction ("worth a 15-min look?"), not "book a demo."

### Templates

**Email #1** — *Subject: GST/HST + Shopify*
> Hi {First}, quick one — most Canadian e-comm brands past ~$1M start tripping on GST/HST
> across provinces and multi-channel reconciliation (Shopify + Amazon + Stripe rarely tie
> out cleanly). We handle books *and* fractional-CFO work exclusively for Canadian
> e-commerce operators in your range. Worth a 15-minute look at how your numbers are set
> up? — {You}

**LinkedIn (after accept)**
> Thanks for connecting, {First}. Not pitching — I run an accounting/CFO practice that
> works *only* with Canadian e-comm founders ($1–10M). Happy to share a quick GST/HST +
> US-nexus checklist we use with clients if useful, no strings.

> ⚠️ **Voice is provisional.** Tune these to the SGML Marketing Pipeline brand philosophy
> once that repo is accessible (see "Marketing integration" below).

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

**Bridge = a lead magnet.** Offer it in outreach, capture the opt-in, then nurture:
- Asset ideas: *"The Canadian E-commerce Accounting Checklist"* or *"GST/HST & US
  Sales-Tax Nexus Guide for Shopify Sellers."*
- Opt-ins flow into the **newsletter + LinkedIn content** (the marketing channel).
- On reply/click/booking → back into the active outreach sequence as a warm lead.

**The loop:** Outbound → lead magnet → marketing nurture → re-engage warm → discovery call.

---

## Marketing integration (SGML Marketing Pipeline)

The nurture **voice** and the outreach **voice** must be one system. The marketing
philosophy lives in the separate `aandriuca/SGML-Marketing-Pipeline` repo, which was **not
accessible** during these sessions (session scoped to `SGML-Sales` only).

**To integrate:**
1. Add `SGML-Marketing-Pipeline` to the environment's allowed repositories.
2. Start a new session scoped to **both** repos.
3. Align the outreach templates above to the marketing brand philosophy, and wire the
   marketing pipeline's lead output into SGML Sales as `source = "marketing-pipeline"`
   leads (the `Lead.source` field already supports this).

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

- **`/draft-outreach`** skill — given a prospect/segment, returns a tailored LinkedIn +
  email sequence in the SGML voice.
- **Lead-magnet asset** — the GST/HST + US-nexus checklist (linchpin between outbound and
  the marketing channel).
- **ICP filter spec** — the exact Store Leads / Sales Navigator filter set, saved for repeatable
  list pulls.
