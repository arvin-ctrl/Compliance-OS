# Agent 11 — Broker / 3PL margin leakage

**Research date:** 2026-08-19

## Anatomy of broker margin leakage

| Leak | Mechanism | Evidence | $ magnitude |
|---|---|---|---|
| **Accessorial paid to carrier, never billed to shipper** | Carrier invoices detention/lumper/layover post-delivery; AP pays it; AR already invoiced linehaul-only. No system reconciles the two sides. | **UNKNOWN — no independent published measurement of this specific gap exists.** Vendors describe it: Denim/Truckstop — "Detention, TONU, and layover get agreed verbally and never reach the invoice" (CLAIMED) | Per-event, Truckstop published ranges (VERIFIED as published guidance): detention $40–$510 (median ~$105); layover $200–$500/day; TONU $150–$300; lumper $25–$458 (median ~$146); liftgate $30–$106; redelivery to $500 (median ~$400) |
| **Missing documentation kills the rebill** | Shipper short-pays with no timestamped in/out or signed lumper receipt | Laneproof analysis of 12,000 broker invoice packets: **62% of loads where detention was billed lacked timestamped arrival/departure records; 44% missing signed lumper receipts; 55% had vague or absent rate-con accessorial language** (CLAIMED — vendor internal, unverified) | n/a |
| **Fuel surcharge mismatch** | Carrier FSC pegged to different DOE index week/peg table than customer FSC | Truckstop lists FSC among broker accessorials (VERIFIED); no frequency data | UNKNOWN |
| **Rebill / reclass / reweight (LTL)** | Carrier rebills after reweigh; broker eats the delta | Tai TMS markets against exactly this; claims "35% fewer billing disputes" (CLAIMED) | UNKNOWN |
| **TONU / reconsignment absorbed** | Verbal approval, no PO change customer-side | Truckstop billing guidance explicit that pass-through is a judgment call: "Not every accessorial charge should automatically land on the shipper's invoice" (VERIFIED) | $150–$300 per TONU |
| **Unbilled loads / late billing** | POD never chased; delivered but never invoiced | ClearLane sells "POD chase" + "Pre-billing revenue audit" (CLAIMED); FreightWaves Dec 2025: only **2% of brokerages report fully automated AR**, 43% only partially (VERIFIED reporting) | UNKNOWN |
| **Wrong customer rate / missed escalator** | Rate table not updated; annual escalator never applied | UNKNOWN | UNKNOWN |
| **Aged AR written off / short-pays absorbed** | Disputes past the customer's cut-off | FreightWaves Jun 2026: qualitative only | UNKNOWN |
| **Duplicate carrier payment** | Same invoice paid twice across email + portal | Triumph NextGen Audit markets duplicate-payment detection (CLAIMED) | Triumph "$114M in Potential Prevented Losses" (CLAIMED, scope unverified) |
| **Carrier over-billing absorbed** | Carrier bills detention not authorised in the rate con | Laneproof: "Rate con said no accessorials. Invoice says $450"; "Detention billed 3 hrs, POD shows 1.5 hrs. $187.50 overbilled" (CLAIMED) | Priced $149–$499/mo, implying modest per-broker recovery |
| **Systemic revenue-recognition failure** | Not a leak but proof the plumbing is weak | **Hub Group 8-K Item 4.02, filed 2026-05-12: FY2023 and FY2024 statements "materially misstated and should no longer be relied upon"; "certain transactions that were prematurely or incorrectly recognized or not adequately supported"; expects to conclude ICFR was not effective.** NT 10-Q filed twice since (May, Aug 2026). (**VERIFIED, SEC**) | A ~$4B 3PL restating two years |

**Widely-circulated leakage percentages (3–15% of revenue; 5–10% of invoices carry errors; 80% of carrier invoices contain a discrepancy) all trace to vendor marketing and mostly describe *warehouse* value-added billing, not truckload brokerage. Do not use them.**

## Brokerage economics & the value of 1%

All VERIFIED from filings:

| Filer | Metric | FY2025 |
|---|---|---|
| **C.H. Robinson (NAST)** | Revenues $11,562.714M; adjusted gross profits $1,706.329M | **14.8%** AGP margin (Q4 14.6%, +20bps) |
| **RXO (Truck Brokerage)** | FY2025 brokerage gross profit $560M; Q4 GM 11.9% | **13.3%** |
| **RXO Q1 2026** | Truck brokerage revenue $1,097M, gross margin $125M | **11.4%** (vs 13.3% Q1'25) |
| **Landstar** | Revenue $4,743.760M; gross profit $404.194M; variable contribution $668.020M | GP **8.5%**; VC **14.1%** |

**13–15% gross margin band, compressing** (RXO lost ~190bps y/y into Q1 2026 on tightening capacity).

**One percentage point of gross margin recovered** (MODEL — arithmetic, not a cited figure):

| Gross revenue | 1 pt = | Equivalent new revenue to sell at 14.6% |
|---|---|---|
| $50M | **$500K** | $3.4M |
| $200M | **$2.0M** | $13.7M |
| $1B | **$10M** | $68.5M |

The recovered dollar carries **no incremental cost of sale**, so it lands nearly whole on operating income. CHRW's NAST ran a 34.3% adjusted operating margin *on gross profit* in Q4 2025 (VERIFIED) — **$500K of recovered AGP at a $50M broker is worth roughly a 20–30% lift to operating income, not 1%.**

Productivity anchor (VERIFIED, CHRW FY2025 10-K): 37 million shipments, 12,733 average employees = **~2,900 shipments per employee per year**; CHRW explicitly manages to "shipments per person per day." Best-in-class; typical mid-market brokers far below. No public per-load back-office headcount benchmark exists (TIA's is member-gated; tianet.org 403).

## Vendor coverage

**Does any vendor detect a load where an accessorial was PAID but not BILLED? Essentially no. Every audit product points at AP (did the carrier overbill me?), not AR (did I forget to rebill my customer?).**

- **Turvo** — automated invoicing, payment reconciliation, "identify discrepancies". No margin-leakage or paid-vs-billed language. ~$5,000/mo entry.
- **Tai TMS** — closest: audit engine "compares LTL invoices against rate confirmations, flagging discrepancies in reweights, reclasses, and accessorials **before payment**". LTL-centric, pre-bill, AP-side. $995–$7,925/mo.
- **Revenova** — auto-applicable accessorial types by location; "flags those fees that don't apply". Prevention at billing time.
- **Alvys** — "accessorials are automatically deducted so the right amount is invoiced". Prevention, no audit.
- **Rose Rocket** — Accessorial Tracking + Freight Audit & Pay listed; no paid-vs-billed claim. From $2,080/mo.
- **McLeod PowerBroker** — Rendition Billing automates invoicing on customer rules. No published unbilled-charge exception report.
- **Denim → absorbed by Truckstop** (denim.com/audit 301s to truckstop.com/product/factoring/). Denim Audit checked "proof of delivery, carrier invoices, and rate confirmations for inconsistencies" via OCR+LLM, "20-second" analysis, 100,000+ docs.
- **Greenscreens.ai → absorbed by Triumph** (greenscreens.ai 301s to triumph.io/solutions/rates). Pricing only.
- **Triumph NextGen Audit** — AP-side.
- **Highway / Parade / Trucker Tools** — zero billing surface.
- **Laneproof** — genuine 2025/26 entrant: three-way reconciliation of rate con + BOL + POD, "$187.50 overbilled" verdicts, $149–$499/mo, targeting 200–1,000 loads/month brokers. **Protects AP, not AR.**
- **ClearLane** (BPO) — the only one selling "Shipper billing with accessorials capture" *and* "Pre-billing revenue audit". Claims DSO ↓30%+, 99% invoice accuracy.

| Capability | Turvo | Denim (Truckstop) | McLeod PowerBroker | Excel + AR clerk |
|---|---|---|---|---|
| rate_confirmation_ingestion | 1 | 2 | 2 | 1 |
| rate_rule_extraction | 1 | 1 | 2 | 1 |
| gps_eld_timestamps | 2 | 0 | 2 | 0 |
| appointment_ingestion | 1 | 0 | 2 | 0 |
| pod_bol_ingestion | 2 | 2 | 2 | 1 |
| detention | 1 | 1 | 1 | 1 |
| tonu | 1 | 1 | 1 | 1 |
| layover | 1 | 1 | 1 | 1 |
| lumper | 1 | 1 | 1 | 1 |
| demurrage | 0 | 0 | 1 | 1 |
| **accessorial_detection (paid≠billed)** | **0** | **1** | **1** | **1** |
| evidence_package | 1 | 1 | 1 | 1 |
| invoice_creation | 2 | 2 | 2 | 1 |
| claim_submission | 0 | 0 | 1 | 1 |
| collection_tracking | 1 | 2 | 2 | 1 |
| dispute_workflow | 1 | 1 | 1 | 1 |
| portal | 2 | 2 | 2 | 0 |
| tms_integration | 2 | 2 | 2 | 1 |
| eld_integration | 2 | 0 | 2 | 0 |
| email_sms_ingestion | 1 | 1 | 1 | 1 |
| accounting_integration | 2 | 2 | 2 | 1 |
| recovered_revenue_analytics | **0** | **0** | **0** | **0** |
| performance_pricing | **0** | 1 | **0** | **0** |
| customer_specific_rules | 1 | 1 | 2 | 1 |
| multi_carrier_shipper_support | 2 | 2 | 2 | 1 |
| **Total /50** | **28** | **27** | **36** | **19** |

**Three zeros hold across every vendor: accessorial_detection on the AR side, recovered_revenue_analytics, and performance pricing. Nobody sells "here is $312K you failed to invoice last year, pay me a share of it."**

## What brokers actually say

**Stated gap:** Reddit r/FreightBrokers could not be retrieved — WebFetch blocks reddit.com at the domain level and direct curl returned HTTP 429 every attempt. LinkedIn and tianet.org returned 403. WebSearch budget exhausted (200/200). **This section is thin and no quotes were manufactured to fill it. It needs a human pass.**

From named publishers:
- **Truckstop** (VERIFIED): "Not every accessorial charge should automatically land on the shipper's invoice," gated on *Was it disclosed? Is it documented? Does the relationship support friction?* And: "Lumper receipts, detention timestamps, and BOL notations are what make a pass-through stick when a shipper pushes back." **This is the industry telling brokers that absorbing accessorials is normal practice — which is exactly why leakage is invisible.**
- **FreightWaves 2025-12-10:** 68% of surveyed brokerages experienced financial stress in the prior year; only **2%** report fully automated AR, **43%** partially automated. Clayton Griffin (President, OTR Solutions): *"When teams have to spend their time chasing PODs and reconciling invoices, they have less time for the true high value work."*
- **FreightWaves 2019-12-03:** "billing error disputes… account for up to 30% of the invoices received."

## Buyer persona & budget

**Primary buyer: the CFO / Controller / VP Finance** of a $50M–$500M brokerage. Not the VP of Ops (owns loads, not the P&L bridge), not IT. Sub-$50M the owner-principal is the buyer, two-call close, but ACV <$25K.

**Why the CFO:** the pitch is a receivable, not a workflow. It reconciles two ledgers they already own — carrier settlement (AP) and customer invoicing (AR) — and outputs a rebill list. $30–150K/yr clears without board approval; a contingency deal often clears with no budget line at all.

**Objections, in the order you'll hear them:**
1. *"My customer won't pay a 90-day-old rebill."* Real and fatal past the dispute window — **the product must run weekly, not as an annual look-back.**
2. *"I chose not to bill that."* Absorption is often a deliberate relationship decision (Truckstop literally teaches it). **You must let the broker mark accounts/lanes "absorb by policy" or every alert is noise.**
3. *"My TMS already does this."* It doesn't — but McLeod/Tai/Revenova all *sound* like they do. Need a side-by-side on a real export, fast.
4. *"I'm not giving you my rate data."* Margin data is the most sensitive file a broker owns. Read-only export, no carrier-rate redistribution, contractual non-aggregation.
5. *"Prove it before I pay."* Free retro run on 12 months of TMS export, then price on recovered dollars. **Zero vendor in this lane prices on performance.**

**Wedge product:** TMS-export-in, ranked rebill list out, evidence packet attached. Works on McLeod, Aljex, Turvo, Tai exports **without an integration project.**

## Broker leakage vs carrier detention: verdict

**Broker margin leakage is the better wedge.** Four reasons:

1. **The money is already contracted.** A missed accessorial rebill goes to a customer with a signed MSA and an existing AR relationship. Carrier detention recovery is an *adversarial claim* against a broker/shipper who has every incentive to deny it. Truckstop's own median detention charge is **~$105** — **the fight costs more than the ticket.**
2. **Deal size.** 1 pt of gross margin = $500K / $2.0M / $10M at $50M / $200M / $1B. A carrier chases $105 events across a fleet where most US carriers run fewer than 10 trucks. Broker ACV plausibly $30–150K; carrier ACV is per-truck SaaS in the low hundreds.
3. **The buyer has a P&L reason to move now.** RXO's brokerage gross margin fell 13.3% → **11.4%** y/y (VERIFIED). CHRW held NAST at 14.6% only by cutting average headcount **7.1% y/y**. Brokers are squeezed on both sides and cannot hire their way out; **recovered margin is the only free dollar left.**
4. **Structurally unserved.** Every audit vendor points at AP. The AR side scored 0–1 for all four subjects. And the consolidation pattern — **Denim → Truckstop, Greenscreens → Triumph** — says point solutions in broker back office get bought by payment networks: **a credible exit path, not a red flag.**

**The counter-argument you must respect: carrier detention has a measurable, universally acknowledged problem statement; broker paid-but-not-billed leakage has NO published magnitude at all.** Every dollar figure in this space today is vendor marketing. **Before writing a check, run a retro on 2–3 real brokers' TMS exports. If leakage is 0.05% of revenue rather than 0.5%, the $50M segment is unsellable and only the $500M+ tier works — ~200 companies, not a venture market. That single measurement is the highest-value next step in this lane.**

## Market-structure findings surfaced incidentally
- denim.com now 301-redirects to truckstop.com (Denim absorbed by Truckstop)
- greenscreens.ai now 301-redirects to triumph.io (Greenscreens absorbed by Triumph)
- **The broker back-office/pricing point-solution layer is consolidating into payment/factoring networks.**

## Sources
s25.q4cdn.com/568306620/files/doc_financials/2025/q4/Q4-2025-Earnings-Release.pdf · sec.gov/Archives/edgar/data/1043277/000104327726000009/chrw-20251231.htm · investors.rxo.com/news/news-details/2026/RXO-Announces-Fourth-Quarter-Results/ · s201.q4cdn.com/733042408/files/doc_financials/2026/q1/RXO2026Q1PressReleasevF.pdf · sec.gov/Archives/edgar/data/853816/000119312526064756/d66072d10k.htm · **sec.gov/Archives/edgar/data/940942/000119312526218141/d146211d8k.htm (Hub Group 4.02)** · truckstop.com/blog/accessorial-charges/ · freightwaves.com/news/the-hidden-cost-of-manual-processes-in-freight-brokerage · /news/back-office-automation-a-boon-for-broker-growth-and-cash-flow · prnewswire.com/news-releases/denim-introduces-ai-powered-audit-tool... · triumph.io/solutions/rates/ · /broker/audit/ · laneproof.com · getclearlane.com/solutions/freight-brokers/ · tai-software.com · turvo.com/articles/tms-broker-software/ · revenova.com · alvys.com · roserocket.com · mcleodsoftware.com/powerbroker-logistics-brokerage-3pl/
