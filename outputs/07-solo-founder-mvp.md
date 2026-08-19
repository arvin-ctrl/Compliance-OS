# 7. Solo-Founder MVP Definition

## Direct answer to the brief's MVP test

> *"Can V1 work from uploaded rate confirmation + BOL/POD + exported GPS timestamps + supporting emails, calculate entitlement, and generate an invoice/evidence packet without a TMS/ELD integration?"*

**Technically yes. Commercially, that exact V1 is the wrong product, and the reason is legal, not technical.**

The pipeline works: rate cons are typed PDFs that parse cleanly; accessorial rules reduce to `free_time → rate × increment → cap` plus an on-time predicate — **2–3 shapes, ~5 parameters**; GPS exports are CSV; entitlement is arithmetic.

**But the claims it produces are mostly already dead.** Arrive Logistics requires notice **30 minutes before** detention begins and a signed BOL with in *and* out times within 48 hours, else *"a reduction of Carrier's accessorial payment by up to 50%, to be determined in Arrive's sole discretion."* Dray Alliance requires 60 minutes. TQL voids detention entirely for a broken tracking ping. Flock: *"Carrier hereby forfeits and waives any right to payment."*

**A post-hoc packet arrives after the condition precedent has failed. You are not presenting a claim; you are requesting a favour from the party that drafted the forfeiture clause.**

So the narrowest sellable V1 is the one where **the money is not contingent on a condition the customer already missed.**

---

## The V1: "The Rebill Report"

**A broker's own accessorials, paid to carriers and never billed to customers.**

The claim runs against the broker's **own customer, under a signed MSA, with an existing AR relationship** — no third-party liability assertion, no collection-agency licensing exposure, no factoring assignment problem, no ELD terms-of-service risk.

### Input — one file

A CSV export from the broker's TMS covering 12 months: load ID, customer, carrier, customer invoice lines, carrier settlement lines. **Every TMS in the market exports this — McLeod, Aljex, Turvo, Tai, Alvys, Revenova.** No API. No integration project. No IT ticket.

Optional enrichment: a folder of rate confirmation PDFs.

### Process

1. **Reconcile per load.** Carrier settlement lines vs customer invoice lines. Surface every accessorial paid out with no corresponding line billed in.
2. **Determine billability.** Parse the customer contract or rate con for whether that accessorial is passable-through, at what markup, and under what documentation condition. *This is the rate-con rule engine — the one genuinely unclaimed capability in the study.*
3. **Rank by urgency, not size.** Each candidate carries **days remaining in that customer's dispute window**. A $2,400 line with 9 days left outranks a $6,000 line with 210 days.
4. **Assemble the evidence.** Carrier invoice, POD, rate con clause, timestamp trail, correspondence — as an argument, not a checklist.
5. **Flag absorb-by-policy.** Let the broker mark accounts, lanes, or customers as deliberately absorbed. **Truckstop actively teaches absorption as a relationship decision — without this, every alert is noise and the product is uninstalled in week two.**

### Output

A ranked rebill list with an evidence packet per line, delivered **weekly**. Not a dashboard. Not a monthly report. A work queue with a deadline attached.

### What V1 deliberately does NOT do

- **No collection.** You produce the invoice; the broker sends it. This keeps you clear of WA RCW 19.16.110, NC G.S. §58-70-15 and Minn. Stat. §332.31, none of which is consumer-limited and none of which has a fintech exemption.
- **No ELD integration.** Avoids Samsara §3.1 and Motive's *"outside of the scope"* clause entirely at this stage.
- **No handwriting dependency.** At ~85% accuracy and a **6% hallucination rate**, handwritten in/out times cannot feed an invoice. V1 uses structured TMS data only.
- **No TMS write-back.** Infios contractually restricts partner modification of rates and invoices; do not build against that.
- **No real-time anything.** That is Stage 2.

---

## Why this is the right V1 for one person

| Test | Assessment |
|---|---|
| File upload / CSV start | **Yes — a single CSV.** The brief's stated preference, exactly. |
| Deep integrations before revenue | **Zero.** |
| Large team | No — one person can run parse, reconcile, review and deliver. |
| Multi-year procurement | No — the buyer is a CFO approving $30–150K without a board. |
| Proprietary dataset needed at start | No. **The dataset accrues:** every rebill outcome builds a win/loss corpus by customer, facility and clause that nobody else has. |
| 24/7 staffing | No — weekly batch. |
| Legal exposure | **Lowest of any wedge examined.** |

---

## Build sequence

**Weeks 1–3 — the reconciler.** Load-level AP/AR diff from CSV. Plain code, no AI. This alone produces the demo.

**Weeks 4–7 — the rule engine.** Rate-con and contract parsing into structured rules. Use a frontier VLM with **structured outputs (`strict: true`), every rule field explicitly nullable, and a required verbatim source quote per extracted rule** — the documented failure mode is the model inventing "2 hours free time" when the document is silent. Dual-model agreement; disagreement routes to a human queue. At ~$0.006–0.028 per page, **cost is a non-issue; determinism is the issue.**

**Weeks 8–10 — evidence assembly and the outcome ledger.** Build outcome capture into the first schema. **Retrofitting it is exactly how every incumbent ended up scoring 0 on collection tracking by accessorial type.**

**Weeks 11–12 — three paid retro runs.** See the acquisition plan.

---

## Stage 2 (month 4+, only if V1 sells): the real-time notice

Once you hold the rules per broker per customer, add: watch the geofence, and **fire the notice inside the contractual window — automatically, with no driver action.** This is where the larger pool sits ($15.1B, 39.3% of stops) and where entitlement is actually preserved rather than salvaged.

Gate Stage 2 behind three things: V1 revenue, counsel's opinion on Samsara §3.1 and Motive's ToS, and **at least three ELD sources including one ELD-agnostic** so no single terms change ends the company.

---

## The measurement that must come first

**Before writing production code, run the reconciler against 2–3 real brokers' TMS exports and measure actual paid-but-not-billed leakage as a percentage of gross revenue.**

There is **no published magnitude for this number anywhere.** Every figure in the market is vendor marketing, and the widely-cited "3–15% of revenue" describes *warehouse* value-added billing, not truckload brokerage.

| Measured leakage | Consequence |
|---|---|
| **> 0.3% of gross revenue** | $50M brokers are viable; proceed to build |
| **0.1–0.3%** | Only $200M+ brokers work; narrower but real |
| **< 0.05%** | **Only the $500M+ tier clears — ~200 companies. Not a venture market. Stop.** |

**That single measurement is worth more than the next three months of engineering.** It is cheap: a spreadsheet, a signed NDA, and three phone calls.
