---
name: draft-outreach
description: >-
  Draft a tailored cold-outreach sequence (LinkedIn + email) for a specific SGML
  prospect or segment, in SGML's aligned brand voice. Use when the user wants
  outreach copy, a cold sequence, connection/DM/email drafts, or a "first touch"
  for a Canadian e-commerce owner. Reads the canonical voice docs at run time so
  the copy never drifts from the brand.
---

# /draft-outreach — tailored cold outreach in SGML's voice

Generate a multi-channel cold-outreach sequence for one prospect (or a segment)
that sounds exactly like SGML: **owner-to-owner, transformation-led, never a
pitch for the service.**

## Step 0 — load the source of truth (do this first, every time)

The voice is NOT hardcoded here — it lives in the repo so it can't drift. Read,
in order:

1. `docs/OUTREACH-VOICE.md` — the binding voice rules + pre-send checklist.
2. `docs/COLD-LEAD-PLAYBOOK.md` — the cadence table, message formula, and the
   reference templates to adapt (not copy verbatim).

If `docs/OUTREACH-VOICE.md` cites `SGML-Marketing-Pipeline/pipeline/brand.py` and
that file is readable in this session, skim it too — it is the ultimate source of
truth. **Never modify the marketing repo** (it is read-only; see root `CLAUDE.md`).

## Step 1 — gather the inputs

You need enough to make the copy *specific*. Accept whatever the user gave; ask
**only** for what's missing and material (one short batch of questions, then go):

- **First name** and **business name** (or "segment" if drafting a template).
- **Platforms they sell on** (Shopify? + Amazon / Etsy / eBay / wholesale?). This
  drives the concrete detail — multi-platform is SGML's wedge.
- **Rough size** ($1M–$10M band) and **niche** (skincare / supplements / other).
- **Why-now trigger or observation**, if any (scaling past $1M, a raise, US
  expansion, a recent post they made, messy books). Optional but gold.

If the user just says "draft outreach for <segment>," produce a template version
with `{First}` / `{Business}` placeholders.

## Step 2 — draft the sequence

Mirror the playbook cadence (adapt if the user wants email-only or LinkedIn-only):

| Day | Channel | Touch |
| --- | --- | --- |
| 1 | LinkedIn | Connection request — **no pitch** |
| 2 | Email | #1 — see them + the number only clarity reveals |
| 4 | LinkedIn | Light engagement / note after accept |
| 6 | Email | #2 — value (offer the **Profit-Leak Checklist**) |
| 9 | Email | #3 — proof (a short, grounded story) |
| 12 | LinkedIn | Short message |
| 16 | Email | #4 — warm door-open (NOT a fake-urgency break-up) |

Apply the **transformation-led formula** to each substantive touch:

1. **See them** — a credible observation about life as a multi-platform Canadian
   operator. Not a problem lecture.
2. **The thing only clarity reveals** — ONE concrete, grounded detail tied to
   *their* platforms/niche: what each channel actually keeps after fees, shipping,
   refunds, reserves; the leak hiding in plain sight; the number they can't see.
3. **Who they become** — imply the edge clarity buys (a stronger business, sharper
   decisions, standing apart from peers). Let expertise show *through* it.
4. **Soft CTA** — the free **Margin Leak Review** (booked call = the conversion),
   or the **Profit-Leak Checklist** for the not-ready. Low friction. No urgency.

**Vary the tone touch to touch** so the sequence never reads like a blast — e.g.
witty → warm → a quick story → seriously diagnostic. Label each touch's register.

## Step 3 — self-check before you output (non-negotiable)

Run every draft against the `OUTREACH-VOICE.md` checklist and FIX violations:

- [ ] Centred on the **owner**, not on us?
- [ ] **No named service / deliverables** ("bookkeeping", "tax", "fractional CFO",
      "reconciliation", "we handle…")? Imply expertise through clarity instead.
- [ ] **One concrete, grounded detail** present (margin / leak / what they keep)?
- [ ] Transformation implied **credibly** — no "we change lives" fluff, no
      guarantees, no hype?
- [ ] **No clickbait or fake urgency** ("STOP scrolling", "last chance", "should I
      close your file?")? Tone varied from the previous touch?
- [ ] CTA is the **Margin Leak Review** (or Checklist), low-friction?

If any draft fails, rewrite it before showing the user.

## Step 4 — output format

Return the sequence ready to paste, clearly structured:

- One block per touch, in `Day / Channel / Tone` order.
- Email touches show a **Subject:** line and body.
- Keep emails short (~3–5 sentences); LinkedIn notes shorter.
- Use the prospect's real details inline (or `{placeholders}` for a template).
- End with a one-line note on **what to personalize further** before sending
  (e.g. swap in a detail from their latest post), and a reminder to send from the
  separate sending domain per the playbook's deliverability section.

## Good vs. bad (calibration)

- ❌ "We handle books *and* fractional-CFO work for Canadian e-comm operators —
  worth a 15-min look at your numbers?" *(names the service; pitch-led)*
- ✅ "When a brand sells across Shopify and Amazon, the one number that quietly
  goes missing is what each channel actually *keeps* after fees, shipping and
  reserves — usually one channel is carrying the other. Worth a look at where
  yours really nets out?" *(owner-centred; one concrete detail; service implied)*
