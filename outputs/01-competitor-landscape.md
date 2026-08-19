# 1. Competitor Landscape

**Research date: 2026-08-19.** Labels: **VERIFIED** (primary source), **CLAIMED** (vendor marketing), **UNKNOWN** (could not establish).

## The organising insight

Everything in this market sorts by one question: **which side of the invoice does it serve?**

- **Payer-side** products recover money for shippers and brokers by **denying** accessorials.
- **Biller-side** products recover money for carriers and brokers by **capturing** unbilled accessorials.

They share vocabulary — "freight audit", "accessorial", "detention", "recovery", "revenue leakage" — and are economically opposite. **Nearly all the capital is on the payer side.**

| | Payer-side (deny) | Biller-side (capture) |
|---|---|---|
| Disclosed venture funding | **Freehand $75M · Loop $95M · Lighthouz (YC) · Laneproof** | **$0 identified** |
| Scale | Cass 34.45M invoices / $36.45B (FY2025, VERIFIED); TriumphPay touches 63% of brokered freight (VERIFIED) | ClearLane self-reports $247K recovered over six months (CLAIMED) |
| Sophistication | Contract digitisation, rate engines, 200+ audit points, autonomous dispute agents | Google Sheets templates, $12.99/mo iOS apps, one human BPO |

**Freehand AI raised a $75M Series C in July 2026 (Battery Ventures + NewRoad, backed by Penny Pritzker) explicitly to hunt "unearned accessorial charges" for Meta, GE, J&J, Unilever, Pfizer and Saks, claiming $260M recovered in 2025.** Carriers facing that machine currently have a spreadsheet. That asymmetry is the single clearest statement of the opportunity — and of the danger.

## Tier 1 — Carrier & enterprise TMS (the "good enough" default)

| Vendor | Score /50 | Detention automation | Verdict |
|---|---|---|---|
| **Trimble** (TMW.Suite, TruckMate, Innovative) | **37** | **Genuine, since 2004.** `Delay cumulative`/`Delay per stop` methods; free time as `Min total`/`Max total` decimal hours; *"Use 'greater' of Arrival or Scheduled Earliest time"* (the contractually correct mode). TruckMate Detention Billing is **license-key gated (#28000/#28001)** and requires mobile-comms integration. | **HIGHEST-SCORING INCUMBENT.** Owns ELD + geofence + TMS + rating. But detention logic is 20 years old, upsell-gated, weak beyond detention/demurrage, **and absent on the collection side.** Its Nov 2025 AI-agent announcement shipped six agents — **none for detention, accessorials, settlement or claims.** |
| **McLeod** (LoadMaster, PowerBroker) | **34** | **Real module.** Free time and warning time per customer *and* per location; two detention periods; auto-appends to billing. **But:** *"in the absence of mobile communications, manually dispatched movements can also initiate the arrival and departure event information"* — auto-detection requires licensing Symphony + a supported ELD + configured free time. | Everything except detention is a charge code a human types. **No rate-con rule extraction anywhere.** Certifying third-party AI (Augment, Chain, CloneOps) rather than building. |
| **Infios** (ex-MercuryGate) | **27** | **None documented.** TM page mentions reducing *"expediting, detention, and service failures"* — avoidance, not billing. | Rebrand deleted the entire MercuryGate content library. Only leakage feature is Control Tower's *"validate loads delivered but not invoiced"* — load-level, not accessorial-level. Partner write-back to rates/invoices is **contractually restricted.** |
| **Oracle OTM** | 27 | **Tolerance gate, not evidence gate.** *"audited based on user-defined percentage and/or amount tolerances. Freight bills within tolerance are approved."* Claims module is cargo damage only. | A $400 detention line inside tolerance **auto-pays without anyone checking whether the truck was there.** |
| **Blue Yonder** | 21 | *"automatically compares the Carrier Invoice against the Contracted Rate. If a carrier overcharges by even $10, the system flags it."* | Checks "is $75/hr the right rate?" — **never "did 2.4 hours actually elapse?"** |
| Generic carrier TMS (Prophesy, Axon, Rose Rocket, AscendTMS, Truckbase) | 23 | Charge codes; Prophesy auto-applies *rated* surcharges, not detected events | Truckbase from $290/mo; Rose Rocket from $2,080/mo |

## Tier 2 — Visibility & appointment (own the timestamp, can't use it)

| Vendor | Score /50 | Position |
|---|---|---|
| **FourKites** | 30 | Sells detention **elimination by the dollar**: Trane *"removed approximately $2.69M in annual detention costs across two facilities"*; Dynamic Yard reductions *"40% to as much as 80%"*. Six AI agents (Tracy, Sam, Alan, Cassie, Polly, Sophie) — **no billing or claims agent.** |
| **project44** | 25 | D&D Optimization is **ocean containers, the shipper's payable.** Ports & Terminals is explicitly defensive: *"audit confirmed pick-up and gate messages to **refute any inappropriate charges**."* Its carrier FAQ dangles *"Collecting fees when dwell time occurs"* as benefit #2 — with **benefit #1 being "reducing dwell time"**, and no product behind either. |
| **Descartes** (MacroPoint, Aljex) | ~24 | Has appointment + X1/X3/AF/D1 arrival/departure event codes. **The 4.6 MB MacroPoint API doc contains zero occurrences of "detention", "dwell", "accessorial", "demurrage" or "lumper."** Free-time trigger produces an *alert*, not a calculation. |
| **Transporeon** | ~23 | Surcharge Management is manual: **the Surcharge DTO has `price` as a single FLOAT — no hours, no rate, no quantity.** Shipper can unilaterally amend it down. FASS covers *"only transports executed via Platform."* |
| **Opendock** (Loadsmart) | 13 | `GET /asset-visit` exposes **Arrived / Docked / Departed** timestamps — a detention calculation in raw form. **The endpoint sits under "for-warehouses". There is no carrier-facing timestamp API.** |

**The contractual moat is the real finding here.** project44's Carrier Services Agreement v18.3 EU §5.2: *"Any project44 Services prepared by project44 based in whole or in part on Data provided pursuant to the Agreement **shall be owned by project44**."* FourKites §3.4: *"FourKites shall own and retain all right, title, and interest in and to Aggregate Data"*, with distribution gated by the **shipper**. **A carrier feeds the raw material for its own detention evidence and never receives a claim artefact it controls.**

## Tier 3 — ELD / telematics (data suppliers with hostile terms)

| Vendor | Score /50 | Reality |
|---|---|---|
| **Motive** | 15 | **`GET /v1/geofences/events` is the best endpoint in this study** — pre-computed entry/exit with `duration` in seconds, plus `start_driver` **and** `end_driver` (drop-and-hook detection). Granular OAuth scopes. Self-serve app creation, same-day. **But rate limits are undocumented (no 429 in the response-code list) and the ToS bars use *"which Motive deems outside of the scope"* — unilateral and open-ended.** |
| **Samsara** | 11 | Detention Report exists but is **trailer-scoped, requires an AG-tracked trailer, and is dashboard-only — not API-addressable.** Asset Gateway cell-based location carries a **0.1–1.5 mile error radius**, fatal for yard-vs-dock. Documented drop-and-hook failure: *"Arrival and departure… trigger only once so all orders will have the same… Arrival, and Departure times."* **Integration Partner Terms §3.1 bars transferring Customer Data to any third party without written notice to Samsara — which the core act of sending a claim to a broker may trigger.** |

**Samsara's May 2026 warranty Claims Center — detect → evidence → claim → track reimbursement — is a working template pointed at OEM warranty instead of shipper detention. If they choose to, the pivot is short.**

## Tier 4 — Freight audit & payment (the substitute, pointed the wrong way)

Cass (34.45M invoices, $36.45B, FY2025 10-K), AFS ($39B managed), Trax ($25B), Intelligent Audit (2.1B+ shipments), nVision, CTSI-Global, A3, enVista, **Loop ($95M Series C)**.

**Direction confirmed:** Cass's 10-K describes serving *"large manufacturing, distribution and retail enterprises."* Loop: *"80% of all carrier freight invoices contain errors"*, *"10% of freight spend is lost to overpayments."* **No established vendor was found whose business is finding under-billing on behalf of the carrier.**

**Regulation encodes the asymmetry: 49 CFR Part 378 is "Processing… of Overcharge, Duplicate Payment, or Overcollection Claims." There is no mirrored federal undercharge-claims procedure.** 49 U.S.C. §14705 is symmetric in law and wholly asymmetric in tooling.

**Contingency pricing is well established here** — Betachon *"standard fee is 50% of the savings recovered"*; AFS ocean audit is gainshare; industry norm is the provider keeping **25–50%**.

## Tier 5 — Factoring & payments (hold the invoice, not the entitlement)

**TriumphPay** engages **63% of all brokered freight**; Audit touches **$29B**; 533 brokers, 57 factors, 174,000+ carriers; $13.5B payments in Q2 2026; average factored invoice ~$2,200; discount rate ~1.37% (all VERIFIED, SEC-filed).

**But TriumphPay Audit is broker-side AP audit.** Triumph's own carrier guidance requires accessorials to be pre-approved on the rate con — **a missing detention charge reads to Audit as a clean invoice.** Its $113.58M of prevented losses is fraud, misdirected payments and double-brokering — **none of it carrier accessorial recovery.**

**Because Audit is funded by brokers (41 of the top 100), Triumph is structurally disincentivised from ever building carrier-side recovery. That conflict is a durable moat for a new entrant, not a temporary gap.**

OTR, Apex, RTS, eCapital, Denim (**acquired by Truckstop 2025-08-19**) all offer "back office" — but it means **AR outsourcing, not revenue discovery.** Apex's language is the tell: required documents include *"any **approved** accessorial charges."* **All five score 0 on accessorial detection.**

## Tier 6 — Direct competitors (crowded at the bottom, empty at the top)

| Company | Model | Funding | Pricing | Status |
|---|---|---|---|---|
| **ClearLane** | Human BPO inside your TMS | None disclosed | **10–25% of recovered revenue** (VERIFIED) | Launched **May 2026**; accessorial audit added July 2026. $42K recovered "this month", $247K over six months, **no named logos** |
| **Detention Source** | Enterprise SaaS | None | $5K–$50K+/yr (CLAIMED) | **The instructive datapoint:** has automated detention invoicing, shipper approve/deny workflow, McLeod/TMW/Oracle integration, and *"the largest repository of facility-level detention data in the trucking industry"* — **and has stayed small and unfunded for years** |
| **detentioniq** | SaaS on ELD feed | UNKNOWN | Not disclosed | *"captures dwell from your ELD, builds the proof, and invoices it"* — the cleanest statement of the thesis. Detention only. No customers disclosed |
| **Tiriel** (fka TrackChain, YC S21) | AI dispatch workforce | YC | $99 first month, then $349+/mo | **THE PIVOT SIGNAL.** Detention/TONU recovery survived only as one of five agents. **Detention recovery was not strong enough to be the company** |
| **Laneproof** | Doc reconciliation | Pre-seed/solo | **$149/mo for 400 docs · $499/mo for 2,000** | **Only company claiming rate-con clause extraction** ("rate, accessorial terms, and detention clauses from every rate con"). But **defensive** — protects broker AP, doesn't create invoices |
| DockClaim / Detenly / FreightAI / Detention Gun / "Detention Tracker System" | App, SaaS, iOS app, **$299 Google Sheet** | None | $49/mo · $12.99/mo · $299 one-time | **The floor is brutally price-anchored** |

**Verdict: the lane is crowded at the bottom and empty at the top.** Zero disclosed venture funding in carrier-side unbilled-accessorial recovery. The best-capitalised adjacent players are on the opposite side of the invoice. The one company with the best proprietary data never scaled. **The one YC company that had this exact wedge pivoted away from it.**

## Tier 7 — Freight back-office AI (the inbox, not the money)

Vooma ($16.6M), Drumkit, **HappyRobot ($150M Series C at $1.2B; >150% NDR; "Collections and settlement" already on the site)**, Pallet ($50M total), Expedock ($17.5M), Vector, Levity, Cargado.

**All extract *fields* (load, stop, rate, reference) to populate a TMS. None parses the terms-and-conditions block where free time, detention $/hr, caps and notice requirements live.** Drumkit's own back-office thought-leadership piece omits billing, AR, audit, accessorials and detention entirely.

**Vector is the single best partner in the study** — geofenced gate-in/dock/gate-out timestamps, driver-side BOL/POD capture, and rendition billing rails. Its timestamp layer is exactly what de-risks handwriting extraction.

## Tier 8 — Ocean D&D and cargo claims (adjacent pools)

**Ocean:** Terminal49 (14/50 — tracking and alerting only, **its own D&D page makes no dispute or recovery claim**), Container xChange (**not a D&D product at all — a container trading marketplace**), Vizion, PortPro (closest: Draft → Disputed → Notified → Invoiced), Flexport (**an FMC respondent — a defendant in this category**), OceanAudit (manual contingency boutique), Cubic (thin). **No one scores above 0 on dispute_workflow + claim_submission + collection_tracking + recovered_revenue_analytics simultaneously. That quadrant is empty.**

**Cargo claims:** TranSolutions/myEZClaim (19/50, **now owned by Infios** — the category leader and the leading TMS claims module are the same product), FreightClaims.com, iNymbus ($0.40–$0.70/claim), Loadsure, Freehand ($75M). **A 3PL's internal claims desk scores 41/50 — your competitor is an underwater person, not a product.**

## The five structural facts that define this landscape

1. **Everyone who holds the timestamp is paid by the party who owes the money.** p44, FourKites, Opendock, Transporeon, Descartes — every one is funded by shippers or brokers. Their case studies measure detention *destroyed*.
2. **Everyone who holds the invoice lacks the entitlement data.** Factors and FAP vendors hold rate con + invoice + POD and have **no** GPS/ELD timestamps, no appointment times, no gate in/out.
3. **Nobody reads the rules.** Rate-con *rule* extraction — free time, $/hr, increment, cap, notice window — is unclaimed across all 40+ vendors examined. Loop has a rules engine pointed at shipper contracts; Laneproof claims it at pre-seed scale. Everyone else extracts fields.
4. **Nobody prices on outcome except humans.** ClearLane (10–25%), Recoupex (20–50%), collection law firms (25–40%), Betachon (50%) — all human services. **No software product in this market is priced on recovery.**
5. **Four capabilities are simultaneously zero across essentially every vendor:** `accessorial_detection` (biller direction), `evidence_package` as a deliverable, `collection_tracking` by accessorial type, and `performance_pricing`.
