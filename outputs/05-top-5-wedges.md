# 5. Top 5 Wedges

Seven candidates were generated from the consolidated evidence and scored against the nine survival criteria in the brief. Each is scored 1–5; **45 is the maximum.**

## Scorecard

| # | Wedge | Pain | Econ value | Clear buyer | Weak incumbent | Weak substitute | Add/switch | Solo MVP | Defensible | Expansion | **Total** |
|---|---|--|--|--|--|--|--|--|--|--|--|
| **W3** | **Broker AR margin recovery** | 4 | **5** | **5** | **5** | 4 | 4 | **5** | 3 | 4 | **39** |
| **W2** | **FMC D&D invoice-defect engine** | 4 | 3 | 4 | **5** | **5** | **5** | **5** | 2 | 3 | **36** |
| **W6** | **Short-pay / deduction ledger** | 4 | 3 | 4 | **5** | 4 | 4 | 4 | 4 | 4 | **36** |
| **W1** | **Real-time entitlement capture** | **5** | 4 | **5** | 3 | 4 | 4 | 3 | 3 | 4 | **35** |
| **W5** | **Contingency accessorial BPO** | **5** | 4 | 4 | 4 | 3 | **5** | 2 | 2 | 3 | **32** |
| W4 | Rate-con rule engine as infrastructure | 2 | 2 | 2 | **5** | **5** | 2 | 4 | 4 | **5** | 31 |
| W7 | Shipper-side dispute prevention | 2 | 3 | 2 | 3 | 2 | 2 | 1 | 2 | 3 | **20 — KILLED** |

Mapping to the brief's white-space hypotheses: **A** → W1 (reframed) · **B** → W5 · **C** → W3 · **D** → W4 · **E** → W1/W5 · **F** → W1/W6 · **G** → W7 (killed).

---

## W1 — Real-time entitlement capture
### *"Don't lose the claim at the dock"*

**This is white-space hypothesis A, reframed by the single most important finding in the research.**

The brief assumed the job is *recover what I failed to bill*. Four real broker contracts say otherwise. Arrive Logistics requires notice **30 minutes before** detention starts and a signed BOL with **in and out** times within 48 hours, else *"a reduction of Carrier's accessorial payment by up to 50%, to be determined in Arrive's sole discretion."* Dray Alliance: 60 minutes. TQL: *"Failure to accept or consistently track will result in no detention or layover"*, documents within 3 days. Flock: *"Carrier hereby forfeits and waives any right to payment."*

**The entitlement is extinguished at the dock. A product that finds unbilled detention six weeks later is asking for a gratuity from the party that wrote the forfeiture clause.**

**What it is:** ingest the rate confirmation, extract that broker's actual free time / rate / increment / cap / notice window, watch the geofence, and **fire the notice inside the contractual window** — to the broker, by the channel the contract names — then force in/out capture onto the POD and keep the tracking ping alive.

**Buyer:** carrier, 11–100 trucks. Owner or controller. ROI Model B: **$297,000 incremental recovery, $65,340 price, $231,660 net** — against ATRI truckload operating margins **below 1.0%**, so the recovery exceeds the entire operating profit.

**Why not the incumbent:** Trimble (37/50) and McLeod (34/50) both *calculate* detention. Neither reads the rules out of a rate con, and **neither has any concept of a notice window.** Their detention logic answers "how much?" — never "is the claim still alive?"

**Biggest risk:** it requires changing driver behaviour in the moment, which is exactly what every prior attempt has failed at. And Samsara §3.1 / Motive's *"outside of the scope"* clause make the data feed a platform risk.

---

## W2 — FMC demurrage & detention invoice-defect engine
### *"A federal statute does the selling"*

**The only wedge in this study where the law states the win condition.**

**46 CFR §541.5:** *"Failure to include any of the required minimum information in this part in a demurrage or detention invoice **eliminates any obligation of the billed party to pay the applicable charge**."*

**§541.6** enumerates ~20 mandatory elements — free-time start date, free-time end date, allowed free time in days, the specific dates charged, the applicable tariff name and rule number, a dispute-contact URL, and a certification that the biller's *own performance did not cause or contribute to the charges*. **§541.7** voids the charge if the invoice issues more than 30 days after the charge was last incurred. **§541.8** obliges the billing party to attempt resolution within 30 days. **46 U.S.C. §41310(b)(2) puts the burden of proof on the carrier.**

**You do not have to prove the terminal was congested. You have to prove a field is missing. That is a deterministic parse against an enumerated list with a legally defined right answer.**

**Buyer:** mid-market NVOCC / freight forwarder, 50–500 containers/month. §541.7(b)–(c) makes them simultaneously billed party *and* billing party on a cascading 30-day clock; they are directly liable (Peloton v. Flexport, Giti Tire v. Flexport); and their own outbound invoices must independently satisfy §541.6. **Compliance budget *and* recovery upside.**

**V1 needs zero integrations.** The customer emails you a PDF. You check 20 fields and two date tests. You emit a §541.5/§541.7 dispute letter to the contact address that §541.6(d)(1) *requires* to be printed on that same invoice. Escalation is free (FMC charge complaint) or $176 (FMC small claims, ≤$50K, carrier bears the burden).

**Biggest risk, and it is severe:** the pool is concentrated — **354 regulated billers, 9 carriers dominating.** Carriers have had two years to fix their templates. **A single Maersk template fix erases a large share of the defect population overnight. Defect density on 2026 invoices is UNKNOWN and is the load-bearing unmeasured variable.**

---

## W3 — Broker AR margin recovery
### *"You paid your carrier $450 of detention and never billed your customer"*

**Highest-scoring wedge. Best deal size in the study, and the cleanest solo-founder MVP.**

**Every audit product in freight points at accounts payable** — did the carrier overbill me? Laneproof, TriumphPay Audit, Tai, Denim, Loop, Lighthouz, Freehand: all of them. **Nobody points at accounts receivable.** In the capability matrix, `accessorial_detection` in the biller direction and `recovered_revenue_analytics` are **0 across every broker vendor scored.** Nobody sells *"here is $312K you failed to invoice last year, pay me a share of it."*

**The economics are the best available.** One point of gross margin is **$500K / $2.0M / $10M** at $50M / $200M / $1B of gross revenue, and the recovered dollar carries **no cost of sale**. At CHRW's 34.3% NAST operating margin on gross profit, $500K of recovered AGP at a $50M broker is a **20–30% lift to operating income**.

**The pain is live and public.** RXO's brokerage gross margin fell **13.3% → 11.4%** year over year. CHRW held NAST at 14.6% only by cutting average headcount **7.1%**. **Hub Group filed an Item 4.02 non-reliance in May 2026** restating FY2023–FY2024 for *"transactions that were prematurely or incorrectly recognized or not adequately supported."* And only **2% of brokerages report fully automated AR.**

**MVP:** TMS export in (McLeod, Aljex, Turvo, Tai — all export CSV), reconcile carrier settlement against customer invoicing per load, ranked rebill list out with the evidence attached. **No integration project. No API. No ELD.**

**Biggest risk, and it is disqualifying if wrong:** **there is no published magnitude for broker paid-but-not-billed leakage.** Every figure in this space is vendor marketing. And Truckstop *teaches brokers to absorb accessorials deliberately* — *"Not every accessorial charge should automatically land on the shipper's invoice."* If leakage is 0.05% of revenue rather than 0.5%, only the $500M+ tier works: **~200 companies, not a venture market.**

---

## W6 — Short-pay / deduction ledger
### *"Why did we lose Customer X's detention?"*

**The question nobody in freight can currently answer, and the only genuinely defensible dataset in this study.**

Across the entire capability matrix, **collection tracking *by accessorial type* scores 0 or 1 everywhere.** McLeod's 26.1 release added an interactive AR Collections screen with document attachment — and still no short-pay reason codes, no deduction matching, no win/loss by accessorial type. Trimble scores 1. Agent 06 found that **no freight-audit vendor publishes a dispute win rate anywhere. It is a genuine public measurement void.**

**What it is:** every accessorial billed, matched to what was actually paid, coded by denial reason, aggregated by facility, by broker, and by clause. Output: *"Broker A pays 91% of detention when the BOL has out-times and 12% when it doesn't"* — and *"Facility B averages 3.4 hours dwell and denies 70% of claims."*

**Why it is defensible:** it accrues a proprietary corpus that gets more valuable with every customer and cannot be bought. Detention Source proved the value of facility-level dwell data — *"the largest repository of facility-level detention data in the trucking industry"* — **and then never monetised recovery.** The win/loss layer is the piece they never built.

**Why it is not a standalone company on day one:** it is an analytics layer on top of a billing flow you must first own. **This is the year-2 moat, not the year-1 wedge** — but it must be designed in from the first schema, because retrofitting outcome capture is how every incumbent ended up at 0.

---

## W5 — Contingency accessorial BPO
### *"Humans first, software behind them"*

**Market-validated, and the brief penalises it.**

ClearLane launched May 2026 charging **10–25% of recovered revenue** across detention, layover, TONU, lumper and rate discrepancies — *"If the audit finds nothing, you pay nothing."* Recoupex charges **20–50%** on cargo claims. Freight collection law firms charge **25–40%**. Betachon charges **50% of savings recovered**. AFS runs ocean audit on gainshare.

**Contingency pricing on freight recovery is proven. It is just never proven on software.**

The strongest argument for starting here: it is the fastest way to **measure the unmeasured variables** — the actual collection uplift (assumed 37.5%→60% in every ROI model), the real per-broker denial reasons, and whether post-hoc claims convert at all given the conditions precedent.

**Why it scores lowest of the five:** the brief explicitly penalises ideas requiring staffing before first revenue. ClearLane already occupies it with a team. Margins are service margins. **And it does not compound** — every new customer needs new hours.

**Correct use: not as the business, but as the paid discovery instrument for W1 and W3.**

---

## W4 — Rate-con rule engine (infrastructure, not a wedge)

**The single most genuinely unclaimed capability found: nobody parses a rate confirmation for accessorial *rules*.** Vooma and Drumkit — the two best-funded rate-con ingestion products — score **0** on `rate_rule_extraction`. They extract load, stop, rate, reference. They do not touch the terms block where free time, $/hr, increment, cap and notice window live. Loop has a rules engine pointed at shipper contracts. Laneproof claims it at pre-seed scale.

**And the rules are tractable.** The legal research answers RQ6 decisively: **the space is not a long tail of rule shapes.** Every schedule reduces to `free_time → rate × increment → cap`, plus an on-time-arrival predicate. **2–3 shapes, ~5 parameters.** The engineering problem is per-account parameter capture and versioning, not ontology design.

**Why it scores 31 and is not a wedge:** nobody feels "I lack a rules engine" as a pain, and no clear buyer writes a cheque for it. **It is the shared asset underneath W1, W3, W5 and W6 — build it as infrastructure, monetise it through a wedge.**

---

## W7 — Shipper-side dispute prevention — **KILLED**

White-space hypothesis G, and it does not survive.

Four independent disqualifiers, each sufficient on its own: (1) **wrong side of the value transfer** — a neutral evidence standard moves money from shipper to carrier, so asking the shipper to fund it is asking them to buy a weapon aimed at their own P&L; (2) the evidence sits behind the buyer's own firewall (Opendock's `asset-visit` timestamps are warehouse-scoped, with **no carrier-facing API**); (3) **9–15 months and SOC 2 Type II before first dollar** with a 6–17 person buying committee; (4) Oracle and Blue Yonder score 0 on `gps_eld_timestamps` and `evidence_package` because **timestamp-level adjudication is a demand gap, not a supply gap** — and unfilled gaps in mature categories usually mean nobody is paying.

**A missing feature is not white space. This is the clearest example in the study.**

---

## The answer the brief demands

> **"Why would a company add this when it already has software, staff, and consultants?"**

**For W3 (broker AR):** because your software audits accounts payable and this audits accounts receivable — opposite directions, and nothing you own does the second one. Because your staff is at 2% AR automation and shrinking 7% a year. Because a consultant produces a report, and this produces a rebill list weekly, inside the customer's dispute window. **And because you pay only out of dollars that arrive.**

**For W2 (ocean D&D):** because no software you own checks a D&D invoice against 46 CFR §541.6's twenty required elements, your staff does not know §541.5 voids the charge outright, and the consultant who does this (OceanAudit) is one person charging a percentage. **The rule already says you don't owe the money. Nobody is reading the invoice.**

**For W1 (real-time capture):** because your TMS calculates detention *after* the claim is already dead. It has no concept of a 30-minute notice window because it was designed in 2004, and the clause that kills your claim was written into your broker agreement last year.
