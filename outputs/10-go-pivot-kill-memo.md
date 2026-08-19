# 10. GO / PIVOT / KILL Memo

**Date:** 2026-08-19 · **Research base:** 15 parallel agents, ~1,300 tool calls, primary sources only

---

# VERDICT: **PIVOT**

**The pain is real and large. The buyer named in the thesis is the wrong one, and the mechanism at the centre of the core hypothesis is broken by contract law.**

---

## What the research confirmed

**The problem is genuine and well-evidenced.** ATRI (Sept 2024, 2023 data): detention occurs on **39.3% of all truck stops** (56.2% refrigerated), costing **$3.6B in direct expense plus $11.5B in lost productivity** across **135 million hours**. **94.5% of fleets charge detention and are paid on fewer than half the invoices they submit.** Two independent ATRI endpoints converge on **~$91–94 of lost revenue per detention hour** against a typical charged rate of only ~$50 — **carriers are underwater on detention even when they collect in full.**

**The competitive lane is genuinely open.** Total disclosed venture funding in carrier-side unbilled-accessorial recovery: **$0.** Meanwhile the *opposite* side has raised nine figures — Freehand AI took **$75M in July 2026** specifically to deny *"unearned accessorial charges"* for Meta, GE, J&J and Pfizer; Loop has **$95M**. **The payer side is arming itself and the biller side has a $299 Google Sheet.**

**Four capabilities are simultaneously absent across all 30 vendors scored:** biller-direction accessorial detection, evidence packages as deliverables, collection tracking by accessorial type, and performance pricing. **Nobody parses a rate confirmation for accessorial *rules* — Vooma and Drumkit, the two best-funded rate-con ingestion products, both score 0.**

---

## Why it is not a GO

### 1. The entitlement is extinguished at the dock, not lost in the back office

This is the finding that reframes everything, verified across four real broker agreements:

| Broker | Condition precedent |
|---|---|
| **Arrive Logistics** | Notify **30 minutes *before*** detention starts; signed BOL with in **and** out times within 48 hrs — else *"a reduction of Carrier's accessorial payment by up to 50%, to be determined in Arrive's sole discretion"* |
| **Dray Alliance** | **60 minutes** before detention accrues — plus accessorial pay-**if**-paid |
| **TQL** | **1 GPS ping per 15 minutes** or *"no detention or layover"*; documents within 3 days |
| **Flock Freight** | POD within 24 hrs — *"Carrier hereby forfeits and waives any right to payment"* |

**The core hypothesis — documents in, entitlement detection, evidence package, claim out — assumes a live claim to recover. Mostly there isn't one.** A post-hoc packet is a request for a discretionary favour from the party that drafted the forfeiture clause. And these carriers **expressly waive their statutory rights** under 49 U.S.C. §14101(b)(1), so no federal default rescues them.

**Compounding it: the recovery window is contractual, not statutory.** §14705's 18 months governs *filing suit*, not billing. Arrive and Dray Alliance both run a 90-day billing waiver and a 180-day undercharge-notice cascade. **Any backward-looking TAM is overstated 3–4×.**

### 2. The economics fail at the buyer the thesis implies

ROI Model A: a **25-truck carrier** generates **$39,375 of incremental recovery**, worth **~$9,800 at 25%** — below the cost of a single sales touch, and 2.8× a Truckbase TMS seat. **Only 61,777 US carriers have 11 or more trucks. 710,386 have ten or fewer**, and that floor is price-anchored by a $12.99/month iOS app and a $299 Google Sheet.

The 150-truck model works beautifully — $297,000 recovered, larger than the carrier's entire operating profit at ATRI's sub-1% truckload margins. **But every one of those figures rests on an ASSUMED collection uplift from 37.5% to 60% that has never been measured. At 45%, the 25-truck tier becomes uninvestable.**

### 3. The central statistic is one self-selected survey

The 37.5% end-to-end collection rate derives from ATRI's voluntary, self-reported, unaudited survey, reached through secondary reporting because the primary PDF is lead-gated — **and the 75%-billed and 50%-paid figures may not be legitimately multiplicable.** DOT OIG's conclusion is unchanged since 2018: ***"Accurate industrywide data on driver detention do not currently exist."* FMCSA never implemented the data collection OIG recommended eight years ago.**

### 4. Someone competent already tried and left

**TrackChain (YC S21) → Tiriel.** A funded, YC-backed team held exactly this wedge and pivoted; detention/TONU recovery survives only as one of five agents inside a dispatch product. Separately, **Detention Source** holds *"the largest repository of facility-level detention data in the trucking industry"* and has never scaled or raised.

### 5. Real incumbent coverage where the thesis assumed none

**Trimble scores 37/50 and has shipped automatic detention since 2004** — per-customer contracted tolerances, `Delay cumulative`/`Delay per stop`, and the contractually correct *"greater of Arrival or Scheduled Earliest"* calculation mode. **McLeod scores 34/50** with per-customer *and* per-location free time. For a carrier already licensed on either, the detection pitch is answered.

### 6. Three structural risks stack on a claim that is already thin

- **Factoring may own it.** Agreements assign *"all accounts… and all proceeds thereof."* TQL's own rate confirmation remits to RTS Financial — factoring is the norm in the target segment. UCC §9-406 discharges the broker by paying the assignee.
- **Collection-agency licensing.** WA RCW 19.16.100 covers *"any obligation for the payment of money… arising out of any agreement or contract"* — **not consumer-limited.** Same in NC and MN. **Freight is commercial, so there is no FDCPA safe harbour**, and *Rowland v. California Men's Colony* forecloses appearing in court.
- **ELD platform risk.** Samsara §3.1 bars transferring Customer Data to third parties without written notice to Samsara — **which sending a claim to a broker may be.** Motive's ToS prohibits whatever it *"deems outside of the scope."*

---

## Why it is not a KILL

Four assets survive every attack:

1. **The problem is $15.1B, recurring on 39.3% of stops, and universally acknowledged.**
2. **The lane is genuinely unfunded** while the adversary side is at nine figures — an asymmetry that is itself the opportunity.
3. **Rate-con rule extraction is unclaimed and tractable.** The legal research answers RQ6 decisively: rules are **not** a long tail. Every schedule reduces to `free_time → rate × increment → cap` plus an on-time predicate — **2–3 shapes, ~5 parameters.** The problem is per-account capture and versioning, not ontology.
4. **Contingency pricing is proven** at 10–50% across ClearLane, Recoupex, collection law firms, Betachon and AFS — **and no software product uses it.**

---

## The pivot

### FROM
**Automated post-hoc recovery of unbilled carrier detention, sold to carriers.**

### TO
**Broker AR margin recovery — accessorials the broker paid its carrier and never billed its customer — sold to the broker's CFO, with real-time entitlement capture as stage two.**

**Why this specific pivot:**

| | Original thesis | Pivot |
|---|---|---|
| Claim runs against | A broker who wrote a forfeiture clause | **The broker's own customer, under a signed MSA** |
| Condition precedent | 30–60 min notice, already missed | **None** |
| Legal exposure | Collection licensing, factoring assignment, ELD ToS | **None of the three** |
| Deal size | $9.8K at 25 trucks | **$49K at $80M; $121K at $200M** |
| V1 input | Rate cons + GPS exports + emails | **One CSV export** |
| Incumbent coverage | Trimble 37, McLeod 34 | **`accessorial_detection` in the AR direction is 0 across every broker vendor** |
| Buyer urgency | Chronic | **RXO 13.3%→11.4%; CHRW cutting headcount 7.1%; Hub Group restating two years** |

**Everything valuable from the original thesis carries over** — the rate-con rule engine, the evidence packet, the outcome ledger, the contingency pricing, and eventually the ELD timestamps. **The pivot changes who signs and what claim you assert, not what you build.**

---

## The one gate

**PIVOT is conditional on a single measurement that has never been published anywhere:**

> **What percentage of a brokerage's gross revenue is paid to carriers in accessorials and never billed to its customers?**

Every dollar figure in this space today is vendor marketing, and the widely-cited "3–15% of revenue" describes **warehouse value-added billing**, not truckload brokerage. Worse, **Truckstop actively teaches brokers to absorb accessorials as a relationship decision** — if absorption is deliberate policy rather than error, the product is noise.

| Measured leakage | Decision |
|---|---|
| **> 0.3%** of gross revenue | **GO.** $50M brokers viable. Build. |
| **0.1 – 0.3%** | **Narrow GO.** $200M+ only. Smaller market, still real. |
| **< 0.05%** | **KILL.** Only ~200 companies clear. Not a venture market. |

**Cost of the measurement: three NDAs, three CSV exports, two weeks, and a spreadsheet. It is worth more than the next quarter of engineering.**

---

## What was killed outright

| | Why |
|---|---|
| **Shipper-side dispute prevention** | Wrong side of the value transfer; evidence behind the buyer's firewall; 9–15 months and SOC 2 Type II before first dollar. **Oracle and Blue Yonder score 0 on `gps_eld_timestamps` because timestamp adjudication is a demand gap, not a supply gap.** |
| **Owner-operator / sub-25-truck** | ACV below the cost of one sales touch, against a $12.99/mo floor |
| **Cargo claims as a beachhead** | **30× lower event frequency** (1.24% of LTL shipments vs 39.3% of stops); entitlement contested on the merits, not merely unbilled; higher legal exposure. **Expansion, not beachhead.** |
| **Contingency BPO as the business** | Service margins don't compound; ClearLane already there. **Retained as the paid discovery instrument.** |

## What is parked, with a trigger

**Ocean D&D invoice-defect engine.** The strongest legal position in the entire study: **46 CFR §541.5 — *"Failure to include any of the required minimum information… eliminates any obligation of the billed party to pay the applicable charge."*** Twenty enumerated fields, a 30-day issuance clock, a mandatory 30-day response duty, burden of proof on the carrier, and escalation that costs $0 or $176. **V1 needs zero integrations — the customer emails a PDF.**

**Parked because the pool is concentrated (354 billers, 9 carriers dominating), carriers have had two years to fix templates since 2024-05-28, the strongest defence (§541.4) was vacated by the D.C. Circuit in Sept 2025, and the 2026 defect rate is unmeasured.**

**Trigger: measure the §541.6 defect rate and §541.7 late-issuance rate on 200–500 real 2026 invoices from 3–5 NVOCCs. Above ~15%, this becomes the primary wedge and a federal statute does the selling. Below ~5%, the window has closed.**

---

## Research quality — stated plainly

**Strengths:** primary sources throughout (SEC filings, eCFR and Federal Register full text, actual broker-carrier agreements, vendor API documentation); every claim labelled VERIFIED / CLAIMED / UNKNOWN; three factual corrections to the brief itself (DOT OIG report ID is ST2018019 not ST-2018-002; FourKites "Fin AI" does not exist; McLeod has no product called "Flowbot").

**Weaknesses that matter:**
- **The session's WebSearch budget (200 calls) was exhausted**, and roughly half the agents completed their later research via direct fetch only. Several lanes are thinner than they appear.
- **Reddit, LinkedIn and TIA were unreachable** (domain-blocked, HTTP 429, HTTP 403). **There are no primary practitioner voices in this research. No quotes were fabricated to fill the gap — but "what operators actually say" is genuinely unvalidated and needs a human pass.**
- **ATRI's primary PDFs are lead-gated.** The single most important statistic in the thesis reaches us through secondary reporting.
- **No customer interviews were conducted.** This is desk research. Every conclusion about willingness to pay is inference.

---

## The one-line answer

> **The money is real, the incumbents genuinely don't cover it, and the buyer in the brief is the wrong one — because by the time a carrier's detention claim reaches a recovery product, the contract has already killed it. The same engine pointed at a broker's own unbilled receivables faces no forfeiture clause, no licensing exposure, and a deal ten times larger. PIVOT there, and gate it on one number nobody has ever published.**
