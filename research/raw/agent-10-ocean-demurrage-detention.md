# Agent 10 — Ocean / drayage demurrage & detention (the regulatory wedge)

**Research date:** 2026-08-19
**Method note:** all regulatory claims verified against Federal Register API records and current eCFR full text, not secondary summaries. Several law-firm and SEO sources circulating misstate the FR citation as "87 FR 14330" (**correct: 89 FR 14330**) and many still describe § 541.4 as operative.

## Regulatory landscape — three layers, all verified

### 1. Interpretive Rule (2020) — 46 CFR § 545.5
85 FR 29638 (2020-05-18); reg text at 85 FR 29665. **VERIFIED** (eCFR, current). Establishes the **incentive principle**: D&D is judged by whether it actually incentivises freight fluidity. Named applications: cargo availability, empty return (detention when containers *cannot* be returned is "likely to be found unreasonable"), notice of cargo availability, government inspections. Also makes dispute-resolution policy quality itself a reasonableness factor. **This is a standard, not a checklist — it needs facts and argument.**

### 2. OSRA-22 — Pub. L. 117-146 (2022-06-16)
Created the **charge complaint** procedure at 46 U.S.C. § 41310. Critically, **§ 41310(b)(2) puts the burden of proof on the common carrier** to establish reasonableness of D&D charges. Remedies: refund/waiver under § 41310(c), civil penalties under §§ 41107, 41109. **VERIFIED.** Complaints go to chargecomplaints@fmc.gov; no filing fee; excludes charges before 2022-06-16.

### 3. D&D Billing Requirements final rule — 46 CFR Part 541
**89 FR 14330** (2024-02-26), Docket FMC-2022-0066, effective **2024-05-28**; corrections at 89 FR 39569 and 89 FR 41895. **VERIFIED via Federal Register API and eCFR full text.**

- **§ 541.6 — ~20 mandatory invoice elements** in four buckets plus certifications:
  - *identifying*: BOL number(s), container number(s), port of discharge for imports, **the basis for why the billed party is the proper party of interest**
  - *timing*: invoice date, due date, **allowed free time in days, free-time start date, free-time end date**, container availability date for imports, earliest return date for exports, **the specific dates charged**
  - *rate*: total due, **the applicable tariff name and rule number / service contract number and section**, the specific rate(s)
  - *dispute*: contact info, **a URL/QR code to a public page describing what documentation is required to win a waiver**, and defined timeframes
  - *certifications*: the billing party must state charges comply with FMC rules including § 545.5, **and that its own performance did not cause or contribute to the charges**
- **§ 541.5 — the kill switch:** *"Failure to include any of the required minimum information in this part in a demurrage or detention invoice **eliminates any obligation of the billed party to pay the applicable charge**."*
- **§ 541.7 — 30-day billing window:** invoice must issue within 30 calendar days of the date the charge was last incurred, else *"the billed party is not required to pay."* NVOCCs get 30 days from the invoice *they* received (§ 541.7(b)); an NVOCC caught in the middle can force its own billing party to grant an extra 30 days (§ 541.7(c)).
- **§ 541.8 — dual 30-day dispute clocks:** billed party gets ≥30 calendar days from invoice issuance to request mitigation/refund/waiver; billing party **must attempt to resolve within 30 days** of receipt.

### 4. The 2025 vacatur — most secondary sources get this wrong
In ***World Shipping Council v. FMC*, 152 F.4th 215, 220 (D.C. Cir. 2025)** (decided **2025-09-23**, No. 24-1088), the court held **46 CFR § 541.4** — the "properly issued invoices" provision limiting *who may be billed* — arbitrary and capricious, because FMC "failed to explain the seeming inconsistency between its contractual-privity-based rationale and its categorical bar against billing motor carriers even when in privity." **The court severed and set aside § 541.4.** FMC removed it from the CFR at **90 FR 60579** (2025-12-29), Docket FMC-2025-0107, stating *"The other provisions of the rule remain in effect."* **VERIFIED — full FR text read.**

**Status check, 2026:** queried the Federal Register API for all FMC rules and proposed rules since Sept 2025. Only three exist: the § 541.4 removal, a Rulemaking Procedures NPRM (91 FR 26976), and a civil-penalty inflation adjustment (91 FR 32888). **There is no FMC re-proposal of § 541.4 as of 2026-08-19. Motor-carrier billability is now unregulated. §§ 541.5, 541.6, 541.7, 541.8 are fully intact.**

### Penalty regime (2026 amounts, VERIFIED at 91 FR 32888, 46 CFR 506.4)
46 U.S.C. § 41107(a) — **$74,943** per knowing-and-willful violation; **$14,988** per non-willful. Private route: FMC small claims, **46 CFR 502.301–.304** — claims **≤$50,000**, **$176 filing fee**, 3-year limitations period, respondent consent required.

## Dollar pool

| Metric | Figure | Period | Source | Label |
|---|---|---|---|---|
| D&D **charged** by 9 largest carriers | **$8.9B** | 2020–2022 | 89 FR 14330 at 14331 | VERIFIED |
| D&D **collected** by same 9 | **$6.9B** | 2020–2022 | 89 FR 14330 at 14331 | VERIFIED |
| D&D **collected**, cumulative | **$15.4B** | 2020-04-01 – 2025-03-31 | fmc.gov/detention-and-demurrage | VERIFIED |
| Implied non-collection | **~22%** of billed | 2020–2022 | derived | VERIFIED (derived) |
| **D&D invoices issued annually, US** | **1,135,000 – 2,270,000** (5–10% of containers in US-foreign trade) | 2024 est. | 89 FR 14330 PRA section | VERIFIED |
| Regulated billers (VOCC+MTO) | 354 | 2024 | 89 FR 14330 PRA section | VERIFIED |
| 2021 billed / waived by 9 carriers | $5.3B / $646.7M (~12% waiver rate) | 2021 | trade press citing FMC audit | CLAIMED |
| Avg accumulated D&D, 14 days, per container | NY $2,478; Oakland $2,325; LA $2,069; Savannah $2,014; Long Beach $1,973 | 2023 | Container xChange benchmark | CLAIMED |
| Per-diem rate range | $100–$300/container/day typical, >$500 in some cases | 2023–25 | Vizion, YardView | CLAIMED |

FMC now publishes only an **index** (Q2-2020 = base), not absolute quarterly dollars, so the current waiver *rate* is UNKNOWN. Q1-2025: billings −24%, collections −19% QoQ, waived +7%. Peak was Q4-2024, 85% above Q2-2020.

**Pool sizing:** ~1.7M invoices/yr × ~$1,500 avg ≈ **$2.5–3B/yr** billed. If ~12–22% is waivable and a recovery product captures a 20% contingency on even a third of that, the addressable fee pool is roughly **$25–50M/yr — real, but not enormous.**

## Vendors

**Terminal49** = tracking/alerting only; its own D&D page makes **no** dispute, appeal, or recovery claim (VERIFIED by fetch). Its API carries exactly the right primitives: Last Free Day, Available For Pickup, Pickup Datetime, terminal **holds**, **terminal fees**, and gate events (Empty Out / Full In / Full Out / Empty Returned), across 1,300+ terminals; pricing per-container, annual, **not published**.

**Container xChange is not a D&D product at all** — it is a container **trading marketplace** ("Free Forever" broker app); its famous D&D benchmark is content marketing (VERIFIED by fetch).

**Vizion** = container event API, explicitly avoidance-not-recovery. **PortPro** is the closest real thing: its Per Diem Dashboard reviews charges, attaches terminal records as backup, and moves charges through Draft → Disputed → Notified → Invoiced (VERIFIED) — but no recovery-rate or outcome data published. **Flexport** ships D&D forecasting/alerting and is itself an FMC respondent (Peloton, Giti Tire complaints, 2024) — **a defendant in this category, not a vendor of the wedge.** **OceanAudit** (Steve Ferreira) is the incumbent contingency recoverer: percentage-of-recovery pricing, claims ~$1M/week in identified refunds and $280K–$442K average client recovery (CLAIMED, unaudited) — **a manual boutique, not software.** **Cubic (gocubic.io)** is the only vendor found claiming automated FMC-element checking; evidence of a real shipping product is thin (CLAIMED).

Blume Global, Dray Alliance, Loadsmart, Expedock, Beacon, Freightos, Envase/WiseTech: **UNKNOWN** (not verified this session).

| Capability | Terminal49 | Container xChange | Ocean carrier portal |
|---|---|---|---|
| rate_confirmation_ingestion | 0 | 0 | 0 |
| rate_rule_extraction | 0 | 0 | 1 |
| gps_eld_timestamps | 0 | 0 | 0 |
| appointment_ingestion | 1 | 0 | 0 |
| pod_bol_ingestion | 1 | 0 | 1 |
| detention (trucking) | 0 | 0 | 0 |
| tonu / layover / lumper | 0 | 0 | 0 |
| demurrage | 2 | 1 | 2 |
| accessorial_detection | 1 | 0 | 0 |
| evidence_package | 1 | 0 | 1 |
| invoice_creation | 0 | 0 | 2 |
| claim_submission | 0 | 0 | 1 |
| collection_tracking | 0 | 0 | 2 |
| dispute_workflow | 0 | 0 | 1 |
| portal | 2 | 2 | 2 |
| tms_integration | 2 | 0 | 1 |
| eld_integration | 0 | 0 | 0 |
| email_sms_ingestion | 1 | 0 | 1 |
| accounting_integration | 0 | 0 | 1 |
| recovered_revenue_analytics | 0 | 0 | 0 |
| performance_pricing | **0** | **0** | **0** |
| customer_specific_rules | 1 | 0 | 1 |
| multi_carrier_shipper_support | 2 | 1 | **0** |
| **Total /50** | **14** | **4** | **17** |

Carrier portals score high but are structurally disqualified: each is single-carrier, and the portal operator is the adverse party. **No one scores above 0 on dispute_workflow + claim_submission + collection_tracking + recovered_revenue_analytics simultaneously. That quadrant is empty.**

## The regulatory-hook wedge assessment: STRONG, scored 7/10

**Materially stronger than trucking detention, for a specific structural reason. § 541.5 makes non-payment obligation turn on document completeness alone.** You do not need to prove the terminal was congested, that the chassis was unavailable, or that your driver waited three hours. **You need to prove that the invoice omitted the free-time start date, or the tariff rule number, or the § 541.6(e)(2) certification. That is a deterministic parse against 20 enumerated fields — an LLM-plus-rules problem with a legally defined right answer.**

Add § 541.7's 30-day issuance clock (pure date arithmetic, same nuclear consequence) and § 541.8(b)'s mandatory 30-day resolution duty, which converts carrier silence into an enforceable procedural violation. **Trucking detention has no analogue: no federal invoice-content mandate, no statutory clock, no burden-shifting.**

**Three caveats that lower the score from 10 to ~7:**
1. **The § 541.4 vacatur cut the strongest defence.** "You billed the wrong party" was the cleanest win, gone as of Dec 2025. What remains is defect-hunting, not standing-hunting.
2. **Carriers have had two years to fix their invoice templates.** The defect rate on 2026 invoices from Maersk/Hapag/MSC is almost certainly far lower than on 2024 invoices. **Defect density is UNKNOWN and is the single most important unknown in this thesis — measure it empirically on 200–500 real invoices before building anything.**
3. **§ 541.5 is untested at scale.** No published FMC decision found squarely holding that a missing element voids the charge. The FMC docket is thick with D&D complaints (Samsung, Bed Bath & Beyond, QVC, Crate & Barrel, Peloton, Nielsen & Bainbridge, Orleans International — filings continuing into June 2026), but these are § 41102(c) *reasonableness* cases, not § 541.5 *defect* cases.

## Buyer analysis

**BCO importer feels the most dollars; the NVOCC/forwarder has the most acute pain.** The BCO absorbs the $2,000-per-container hits but treats them as cost of goods, and the person who feels it rarely controls a software budget line. **Drayage carriers** feel it worst per-dollar-of-revenue — but the § 541.4 vacatur just removed their regulatory shield, and their margins won't support seat pricing.

**NVOCCs and forwarders are the sharpest wedge:** § 541.7(b)–(c) makes them simultaneously billed party *and* billing party with a cascading 30-day clock; they are directly liable (Peloton v. Flexport, Giti Tire v. Flexport, International Lumber v. CEVA); and their own invoices to customers must independently satisfy § 541.6. **They have compliance budget *and* recovery upside.**

**Recommended buyer: mid-market NVOCC/forwarder (50–500 containers/month), sold as compliance-plus-recovery.**

## Data access & solo-founder feasibility: HIGH

Needed: (a) the D&D invoice itself — **the customer supplies this, no integration required**; (b) container events to contradict it. (b) is buyable: Terminal49's API exposes precisely LFD, Available For Pickup, Pickup Datetime, holds, terminal fees, and all four gate events across 1,300+ terminals, priced **per container, one-time, regardless of tracking duration** — the ideal cost structure for contingency work. Vizion is the alternative. Neither publishes prices (UNKNOWN).

**Feasibility genuinely higher than the trucking equivalent, because V1 is invoice-only: parse a PDF, check 20 fields plus two date arithmetic tests, emit a § 541.5/§ 541.7 dispute letter to the contact that § 541.6(d)(1) *requires* to be printed on the invoice. Zero integrations, zero telematics, zero carrier cooperation.** Container event data is a v2 enrichment for § 545.5 reasonableness arguments. Escalation path is cheap and real: FMC charge complaint (free) → small claims under 46 CFR 502.301 ($176, ≤$50K, **carrier bears burden of proof**).

## Ocean D&D vs trucking detention: comparative verdict

**Ocean D&D wins on legal basis and loses on unit economics.** The trucking-detention product must prove a contested fact (how long did the driver wait) against a counterparty with no duty to respond; the ocean D&D product checks a federal checklist against a counterparty with a statutory 30-day duty to respond and the burden of proof at the regulator. **That asymmetry is the whole thesis, and it is real and verified.**

Against that: **the ocean pool is concentrated (~354 billers, 9 carriers dominating), which means carriers can and did remediate their templates centrally — a single Maersk template fix erases a large share of the defect population overnight.** Trucking detention is fragmented across 10,000+ brokers, so the defect surface never closes. **Ocean D&D is therefore a higher-conviction, potentially shorter-lived opportunity whose half-life depends entirely on carrier template compliance in 2026, which nobody has published.**

**Verdict: pursue, but gate on one experiment.** Acquire 200–500 real 2026 D&D invoices from 3–5 NVOCCs and measure the § 541.6 defect rate and § 541.7 late-issuance rate. **If defects run >15%, this is a fundable wedge with a federal statute doing the selling. If <5%, the compliance window has closed and the residual business is § 545.5 reasonableness work — expert consulting (OceanAudit's model), not software.**

## Sources
ecfr.gov/current/title-46/part-541 · federalregister.gov/documents/2024/02/26/2024-02926/demurrage-and-detention-billing-requirements · /2024/05/09/2024-10136/...correction · **/2025/12/29/2025-23920/...properly-issued-invoices-provision-set-aside-by-court** · hklaw.com/en/insights/publications/2025/10/dc-circuit-vacates-key-provision-of-fmcs-demurrage-and-detention · federalregister.gov/documents/2020/05/18/2020-09370/interpretive-rule-on-demurrage-and-detention-under-the-shipping-act · /2026/06/02/2026-10996 · ecfr.gov/current/title-46/part-502/subpart-S · fmc.gov/detention-and-demurrage/ · fmc.gov/ocean-shipping-reform-act-of-2022-implementation/guidance-on-charge-complaint-interim-procedure/ · fmc.gov/articles/final-rule-on-demurrage-detention-cleared-to-take-full-effect-may-28/ · terminal49.com/detention-demurrage-charges/ · terminal49.com/api-pricing · portpro.io/features/drayage-carrier/per-diem-monitoring · container-xchange.com/blog/demurrage-detention/ · vizionapi.com/blog/know-your-charge-per-diem-demurrage-and-detention · oceanaudit.com · gocubic.io/guides/cost-optimization/demurrage-detention-dispute-playbook-2026 · freightwaves.com/news/peloton-flexport-wrongly-charged-millions-in-detention-demurrage-fees · beneschlaw.com/resources/demurrage-and-detention-billing-after-wsc-v-fmc.html
