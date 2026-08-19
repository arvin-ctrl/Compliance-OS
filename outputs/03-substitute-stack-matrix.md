# 3. Substitute-Stack Matrix

A missing feature is not white space. What matters is what a buyer **actually assembles today** to get this job done, what it costs them, and where it genuinely fails. This is that inventory.

## Stack A — Owner-operator to 10 trucks (710,386 US carriers, 90.3% of the market)

| Layer | What they use | Cost | Where it fails |
|---|---|---|---|
| Timestamps | ELD dashboard (Motive $25–50/veh/mo; Samsara $27–33/veh/mo) + driver's phone photos | Already sunk | No load↔stop association; Samsara AG cell location has a **0.1–1.5 mile error radius** |
| Rules | Reading the rate con on a phone in a truck stop | $0 | Terms live in 6pt type on page 3 |
| Detection | Driver remembers to call dispatch | $0 | **The 30–60 minute pre-detention notice window is missed constantly** |
| Calculation | Mental arithmetic, or a **$299 Google Sheet** sold on Whop | $0–299 | — |
| Invoicing | Factoring portal (OTR, Apex, RTS at 1.5–5% of invoice) | Already sunk | Factor checks *document completeness*, never *entitlement* |
| Collection | Calling the broker | $0 | — |
| Niche apps | Detention Gun ($3.99/invoice or $12.99/mo); DockClaim ($49/mo) | $12–49/mo | Detention only; global 2-hour default, not the contract's terms |

**Honest assessment: this stack is bad, and it is nearly free.** The binding constraint is not capability — it is that **the driver has to do something in the moment and doesn't.** A product priced above ~$50/truck/month cannot win here, and ROI Model A shows a 25-truck carrier generates only **~$9,800 ACV at 25% of recovery** — below the cost of a single sales touch. **This segment is reachable only by self-serve or by embedding in the factor/ELD relationship.**

## Stack B — 11–100 trucks (56,715 US carriers)

| Layer | What they use | Cost | Where it fails |
|---|---|---|---|
| TMS | Truckbase (from $290/mo), Rose Rocket (from $2,080/mo), Prophesy, Axon | $3.5K–25K/yr | Accessorials are charge codes a human types |
| Timestamps | ELD + occasional geofence alerts | Sunk | Drop-and-hook collapses multiple stops into one arrival/departure pair |
| Rules | A spreadsheet of customer accessorial terms, maintained by one person | ~0.25 FTE | **Decays.** Arrive reserves the right to *"modify the Accessorial Rates or time frames… at any time, effective on notice"* |
| Detection → collection | **One billing/AR clerk** — BLS median $47,170, loaded **~$61,321/yr** | $61K/yr | The actual substitute. Overloaded, and the failure is silent |
| Escalation | Owner calls the broker's VP | $0 | Works once, burns relationship capital |

**This is the sweetest spot in the market and it is still hard.** ROI Model B (150 trucks) shows **$297,000 of incremental recovery** at a $65,340 price — and ATRI's 2026 cost data puts truckload operating margins **below 1.0%**, meaning that recovery is **larger than the carrier's entire operating profit.** That is the strongest single argument in this study.

**But the substitute is a human who is already paid for**, and the incumbent TMS (McLeod 34, Trimble 37) may already do detection if the modules are licensed.

## Stack C — 100+ truck carrier (5,062 US carriers)

| Layer | What they use | Cost |
|---|---|---|
| TMS | **McLeod LoadMaster or Trimble TMW.Suite** — $75K–$500K/yr, $100K–$500K implementation (all CLAIMED third-party) |
| Detention | **A real module.** McLeod: free time + warning time per customer *and* location, two periods, auto-append to billing. Trimble: `Delay cumulative`/`Delay per stop`, `Min total`/`Max total` decimal hours |
| Timestamps | Own ELD, integrated (Trimble owns PeopleNet; McLeod has 25+ ELD partners via Symphony) |
| Rules | Manually configured in customer + location profiles |
| Collection | AR department + McLeod's interactive AR Collections screen (26.1) |

**This stack genuinely works for detection.** Selling detection here is selling a feature they bought years ago. **What still fails: rule ingestion from the rate con (nobody does it), evidence packet assembly, dispute rebuttal, short-pay reason coding, and collection accounting by accessorial type — all 0 or 1 on both platforms.**

## Stack D — Freight broker / 3PL ($50M–$500M)

| Layer | What they use | Cost | Where it fails |
|---|---|---|---|
| TMS | McLeod PowerBroker (36/50), Turvo (~$5,000/mo), Tai ($995–$7,925/mo), Aljex, Alvys, Revenova | $12K–$95K/yr | All prevent *over*-billing; none detects *under*-billing on the AR side |
| Carrier AP audit | Laneproof ($149–$499/mo), TriumphPay Audit, Denim/Truckstop | $1.8K–6K/yr + | **Points at AP. Every one.** |
| AR | **43% of brokerages are only partially automated; only 2% fully** (FreightWaves, Dec 2025) | staff | The actual gap |
| Margin analysis | Excel, monthly, after close | staff | Too late for the customer's dispute window |
| Escalation | Account manager relationship | $0 | **Truckstop literally teaches brokers to absorb accessorials**: *"Not every accessorial charge should automatically land on the shipper's invoice"* |

**The economics here are the best in the study.** 1 point of gross margin = **$500K / $2.0M / $10M** at $50M / $200M / $1B revenue, and the recovered dollar carries no cost of sale — at CHRW's 34.3% NAST operating margin on gross profit, **$500K of recovered AGP at a $50M broker is a 20–30% lift to operating income.**

**And the pain is live:** RXO's brokerage gross margin fell **13.3% → 11.4%** year over year; CHRW held NAST at 14.6% only by cutting headcount **7.1%**. **Hub Group filed an Item 4.02 non-reliance in May 2026 restating FY2023–FY2024** for *"transactions that were prematurely or incorrectly recognized or not adequately supported"* — freight brokerage revenue recognition breaks even at $4B scale.

**The fatal unknown: there is NO published magnitude for broker paid-but-not-billed leakage.** Every dollar figure in this space is vendor marketing. That single measurement is the highest-value next step in this lane.

## Stack E — Enterprise shipper

| Layer | What they use |
|---|---|
| TMS | Oracle OTM (27/50), Blue Yonder (21/50), SAP TM, e2open, Manhattan |
| Accessorial validation | **Tolerance gate.** Oracle: *"audited based on user-defined percentage and/or amount tolerances. Freight bills within tolerance are approved and automatically interfaced to any Accounts Payables system"* |
| Gate timestamps | Opendock (`GET /asset-visit`: Arrived/Docked/Departed), FourKites Dynamic Yard, C3 |
| Audit | Cass / AFS / Trax / Intelligent Audit — **often on contingency at 25–50% of savings** |
| Detention reduction | FourKites Dynamic Yard (40–80% reductions claimed; Trane **$2.69M removed**) |

**This stack is excellent at its actual job, which is paying less.** A "dispute prevention" product sold here competes with incumbent FAP firms already working on contingency with zero integration lift — and **asks the shipper to fund a weapon aimed at its own P&L.**

## Stack F — Ocean / drayage D&D

| Layer | What they use | Where it fails |
|---|---|---|
| Container events | Terminal49 (LFD, holds, gate events, 1,300+ terminals, per-container pricing), Vizion | Tracking and alerting only — **Terminal49's own D&D page makes no dispute or recovery claim** |
| Dispute | **Ocean carrier's own portal** — the adverse party's system, single-carrier | Structurally disqualified as neutral evidence |
| Recovery | **OceanAudit** — manual contingency boutique, ~$1M/week identified (CLAIMED) | A person, not software |
| Drayage ops | PortPro Per Diem Dashboard (Draft → Disputed → Notified → Invoiced) | Closest to real; no published outcome data |
| Escalation | FMC charge complaint (**free**); FMC small claims (**$176, ≤$50K, carrier bears burden of proof**) | Almost nobody uses it |

**This is the thinnest substitute stack in the entire study.** Nobody scores above 0 on `dispute_workflow` + `claim_submission` + `collection_tracking` + `recovered_revenue_analytics` simultaneously. **That quadrant is empty** — and a federal rule (46 CFR §541.5) makes non-payment turn on **document completeness alone.**

## Cross-cutting: what every stack lacks

| Capability | Present in any substitute stack? |
|---|---|
| Rate-con **rule** extraction (free time, $/hr, increment, cap, notice window) | **No.** Not one, at any price point |
| Pre-detention notice fired **inside the 30–60 minute contractual window** | **No.** This is where the money is actually lost |
| Forcing in **and** out times onto the signed BOL | Partially — Vector's driver capture is closest |
| Evidence packet assembled as an **argument** | **No.** Everything is a document checklist |
| Collection outcome tracked **by accessorial type** | **No.** Nobody can answer "why did we lose Customer X's detention?" |
| Contingency pricing on **software** | **No.** Only humans price this way |

## The honest counter-argument

**Three of these stacks are good enough that the buyer will not move.**

- **Stack A** is nearly free, and no price above $50/truck/month clears.
- **Stack C** already has working detention detection in a system that cost six figures and cannot be ripped out.
- **Stack E** is optimally designed for its owner's actual goal.

**The stacks with real, unserved failure are B (a single overloaded clerk), D (the AR side of broker margin, unmeasured), and F (an empty quadrant with a federal statute behind it).** Those three define the wedge shortlist.
