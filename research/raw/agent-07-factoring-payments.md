# Agent 07 — Factoring & Payments Layer

**Lane:** TriumphPay, OTR Solutions, Denim, RTS, Apex, eCapital, Relay Payments, Comdata/Corpay
**Research date:** 2026-08-19

## Headline findings

1. **TriumphPay Audit is broker-side accounts-payable audit, not carrier revenue recovery — VERIFIED, not inferred.** It detects overbilling, duplicates and fraud ("prevent financial leakage" *from the broker*). Triumph's own carrier guidance requires accessorials to be pre-approved on the rate confirmation; a missing detention charge reads to Audit as a **clean invoice**. Because Audit is funded by brokers (41 of the top 100), Triumph is structurally disincentivised from ever building carrier-side accessorial recovery. That conflict is a durable moat for a new entrant, not a temporary gap.

2. **No factor detects missing accessorials.** All five (OTR, Apex, RTS, eCapital, Denim) ingest rate con + invoice + POD, and all check *document completeness*, never *entitlement*. Apex's language — "any **approved** accessorial charges" — is the tell.

3. **Denim was acquired by Truckstop.com on 2025-08-19** (denim.com now 301-redirects to truckstop.com). Material competitive change: makes Denim/Truckstop the most likely of the three to ship something adjacent within 24 months.

## Network scale (SEC-filed / earnings calls — VERIFIED)

| Metric | Value | Source |
|---|---|---|
| Share of all brokered freight engaged | **63%** | TFIN Q3 2025 investor deck |
| Audit transaction volume touched | **$29B** | TFIN Q3 2025 investor deck |
| Payments processed, Q2 2026 | **$13.5B**, +34% QoQ | Q2 2026 earnings call |
| Network | 533 brokers, 57 factors, 74 shippers, 174,000+ carriers | TFIN Q3 2025 deck |
| Brokers using payments | 400+, incl. 41 of top 100 | TFIN Q3 2025 deck |
| Daily disbursement | $155MM/day | TFIN Q3 2025 deck |
| Average factored invoice | **~$2,200** | Q2 2026 call |
| Average discount rate | ~1.37%; NFE yield ~15.4%; ~10.4x turnover | TFIN deck p.11 |
| AR purchased TTM | $11B ($46MM invoices/day) | TFIN deck |
| Customers using BOTH payments and audit | only **22%** | TFIN deck |
| Loss prevention Jan 2023–Aug 2024 | $113.58MM — fraud, misdirected payments, double-brokering, bad data. **None of it carrier accessorial recovery.** | triumph.io |
| Intelligence segment | $2.39MM revenue, **-81.7% EBITDA margin**, flat 4 quarters | Q2 2026 call |

One genuinely impressive capability: Triumph shipped an ML system that interprets plain-text customer rules imported from broker TMSs — real rate-rule extraction, but pointed at broker AP.

## The "factor owns the invoice" strategic analysis

**Case FOR the factor as natural owner:** They already hold rate con + invoice + POD on every load, pre-underwritten. Existing carrier billing relationship and payments account. Collections staff already chasing the broker. Natural pricing mechanism (% of invoice). Recovered accessorial dollars are *incremental factorable AR* — a factor at 2.5% earns on every recovered dollar and improves retention. Triumph uniquely holds **both sides**: it audits the broker's AP and factors the carrier's AR, so it could see an accessorial approved on the broker side that never appeared on the carrier's invoice. Nobody else can see that.

**Case AGAINST — stronger:**

1. **Conflict of interest at the network level.** Audit revenue comes from brokers whose explicit goal is preventing payment leakage. A product that systematically increases what brokers owe carriers is adversarial to the customers paying for Audit. Structural, durable — not a temporary gap.
2. **Factor economics reward speed, not completeness.** Factoring makes money on turnover (~10.4x annually). A disputed detention claim slows collection, ages the receivable, risks chargeback on recourse. Factors are incentivised to fund clean invoices fast and reject messy ones — the opposite of recovery work.
3. **They lack the determinative data.** Detention entitlement is proven by arrival/departure timestamps. No factor holds them.
4. **Non-recourse makes it worse.** OTR's own detention blog positions non-recourse as "guaranteed payment even if detention charges are disputed" — the factor's answer to detention risk is to *price it into the discount rate*, not recover it.

**Synthesis: the factor owns the *invoice* but not the *entitlement*.** Entitlement lives in ELD/GPS, appointment times and gate in/out — data the factor never touches.

## Pricing anchors

| Anchor | Figure | Status | Source |
|---|---|---|---|
| Triumph avg discount rate | ~1.37%; NFE yield ~15.4%; ~10.4x turnover | VERIFIED | SEC deck p.11 |
| Triumph avg invoice price | ~$2,200 | VERIFIED | Q2 2026 call |
| OTR Solutions | 2.5%–5%/invoice; from 2.5% w/ discounts at $100k+/mo; advance 97–100%; ~$3 ACH; no monthly minimum | CLAIMED (3rd-party) | truckingway / fundingcompass |
| RTS Financial | 1.5% (30+ loads/mo) to 2.0–2.5% typical; advance "more than 90%" within 24hr | Advance VERIFIED; rates CLAIMED | rtsinc.com |
| Apex Capital | ~2% flat recourse; not published; defaults to recourse | CLAIMED | smallfleethq |
| Denim/Truckstop | Not published (rate calculator by volume/invoice size/load-board tier) | VERIFIED non-disclosure | truckstop.com |
| eCapital | Advance up to 100%; rates not disclosed | VERIFIED non-disclosure | ecapital.com |
| Non-recourse premium | +0.5–1% over recourse | CLAIMED | multiple |
| Detention | $25–$100/hr; to $125 hazmat; 2hr grace | CLAIMED (OTR's own blog) | otrsolutions.com |
| Lumper | $150–$450/load; national avg $285 | CLAIMED (3rd-party) | foreigh.com |
| Relay Payments | **No published fees** | VERIFIED non-disclosure | relaypayments.com |

**Implication:** the market's mental anchor is **1.37%–5% of invoice face value**. A 20–30% contingency on *recovered* dollars is an unfamiliar shape — nobody in this set prices on performance. Both a positioning risk and a differentiator.

## Data held vs lacked

**Hold (VERIFIED):** rate confirmation, carrier invoice, POD/BOL, broker identity and credit, payment status and aging, historical rate/RPM data, factor-held-invoice assignments. Triumph adds broker-side AP approval state, network-wide fraud signals, $70B/yr verified transaction data.

**Lack (VERIFIED by absence across all vendor materials):** GPS/ELD arrival-departure timestamps; appointment times; gate in/out; dock check-in; driver messages; the broker–carrier **email thread** where accessorials get verbally approved; facility dwell history.

The gap is exactly the evidentiary layer.

## Capability scores

0 = none/no evidence · 1 = partial/manual/adjacent · 2 = productised. V=VERIFIED, C=CLAIMED, U=UNKNOWN.

| Capability | TriumphPay | OTR | Denim |
|---|---|---|---|
| rate_confirmation_ingestion | 2 V | 2 C | 2 C |
| rate_rule_extraction | 2 V (ML customer-rules engine) | 0 U | 0 U |
| gps_eld_timestamps | 0 V-absent | 0 | 0 |
| appointment_ingestion | 0 U | 0 U | 0 U |
| pod_bol_ingestion | 2 V | 2 C | 2 C |
| detention | 1 V (line item, requires pre-approval) | 1 C (photo+timestamp capture, ops team) | 0 U |
| tonu | 0 U | 0 U | 0 U |
| layover | 0 U | 0 U | 0 U |
| lumper | 1 V (receipt within 24hr) | 1 C | 0 U |
| demurrage | 0 U | 0 U | 0 U |
| **accessorial_detection (missing)** | **0 V-absent** | **0 U** | **0 U** |
| evidence_package | 1 V (doc packet, not claim-built) | 1 C | 1 C |
| invoice_creation | 1 V (presentment) | 2 C | 2 V |
| claim_submission | 1 V (invoice ≠ claim) | 1 C | 1 C |
| collection_tracking | 2 V | 2 V (in-house AR team) | 2 V |
| dispute_workflow | 2 V (variance/exception queue) | 1 C | 1 C |
| portal | 2 V | 2 V | 2 V |
| tms_integration | 2 V (TAI, 3PL, Descartes) | 1 C | 2 V (Turvo) |
| eld_integration | 0 V-absent | 0 | 0 |
| email_sms_ingestion | 1 C | 1 C | 1 C |
| accounting_integration | 1 U | 1 U | 1 U |
| recovered_revenue_analytics | 1 V ($114M — broker-side savings) | 1 V (RPM trends) | 1 V |
| performance_pricing | 0 V-absent | 0 | 0 |
| customer_specific_rules | 2 V | 0 U | 0 U |
| multi_carrier_shipper_support | 2 V (533/74/174k) | 1 C | 1 C |

**Every player scores 0 on the four capabilities that define the category: `accessorial_detection`, `gps_eld_timestamps`, `appointment_ingestion`, `performance_pricing`.**

## Channel-partner feasibility for a solo founder

**Realistic shape — "recovery engine behind the factor's brand."** Factor pushes rate con + invoice + POD via API; you match against ELD/appointment data the *carrier* authorises; you surface "you were owed $X detention on 14 loads"; the factor bills, funds and collects it as normal AR. Factor earns its discount rate on incremental volume plus a rev-share.

**Why a factor says yes:** near-zero build cost; differentiation in a commoditised market where rate is the only lever (RTS 1.5% vs OTR 2.5% is the whole sales pitch today); retention; incremental factorable volume at full margin.

**Obstacles, by severity:**
1. **Broker-relationship risk.** Factors depend on broker goodwill for collections. A tool increasing carrier claims against those brokers threatens it. Expect this objection first and hardest.
2. **Triumph is structurally closed.** Do not pursue as a channel — pursue as the incumbent you are structurally advantaged against.
3. **Data you need isn't theirs to give.** ELD access requires carrier-level OAuth. The factor is a distribution channel, not a data channel.
4. **Procurement asymmetry.** OTR/Apex/RTS/eCapital are PE-scale; Denim now inside Truckstop. Expect 6–12 months.
5. **Consolidation risk.** The Denim acquisition shows the layer is actively consolidating.

**Recommended sequencing:** start with mid-tier/regional factors who need differentiation and can decide fast; prove recovered-dollar numbers on 20–50 carriers; then approach OTR or eCapital. Avoid Triumph entirely as a partner.

## Threat level

- **TriumphPay — MEDIUM-LOW as direct competitor, HIGH as moat-holder.** Has the data and network, structurally will not build it. Watch for any carrier-side accessorial feature in LoadPay — that is the signal.
- **OTR Solutions — MEDIUM.** Closest to caring: publishes detention content, markets timestamp capture, has an ops team. But it is document capture, not detection.
- **Denim/Truckstop — MEDIUM-RISING.** Best automation DNA (75% of payments under a minute) now backed by Truckstop distribution and capital.
- **Apex, RTS, eCapital — LOW.**
- **Relay, Comdata/Corpay — LOW.** Disbursement rails; wrong side of the transaction. Potential *partners* for lumper reimbursement evidence.

## Competitor lead surfaced

**DetentionIQ** (detentioniq.com) — "captures dwell from your ELD, builds the proof, and invoices detention automatically." Exists *outside* the factoring layer precisely because factors can't reach ELD data. Flagged to the direct-competitor sweep.

## Research caveat

Agent hit the session WebSearch cap (200/200) partway through and completed remaining research via direct WebFetch; eCapital and RTS back-office detail is thinner and labelled accordingly.

## Sources

1. https://triumph.io/broker/audit/
2. https://www.sec.gov/Archives/edgar/data/1539638/000162828025035063/tfininvestordeck.htm
3. https://learn.tai-software.com/knowledge/triumphpay_audit
4. https://triumph.io/blog/factor/114-million-in-potential-prevented-losses/
5. https://triumph.io/loss-prevention/
6. https://www.investing.com/news/transcripts/earnings-call-transcript-triumph-financial-tops-q2-2026-estimates-on-revenue-93CH-4806526
7. https://ir.triumph.io/news-events/press-releases/detail/321/triumph-releases-second-quarter-2026-financial-results
8. https://otrsolutions.com/client-portal
9. https://otrsolutions.com/blog/detention-pay-in-trucking
10. https://otrsolutions.com/otr-select
11. https://truckstop.com/product/factoring/
12. https://www.freightwaves.com/news/truckstop-acquires-denim-for-ai-driven-invoice-solutions
13. https://www.prnewswire.com/news-releases/truckstopcom-acquires-denim-bring-enhanced-financial-solutions-and-back-office-automation-to-freight-carriers-and-brokers-302533125.html
14. https://www.apexcapitalcorp.com/blog/complete-freight-bill-guide/
15. https://www.rtsinc.com/product/factoring-services
16. https://ecapital.com/freight-factoring/
17. https://www.relaypayments.com/carriers
18. https://www.comdata.com/resources/news/comdata-launches-digital-lumper-payment-solution-for-fleets-nati/
19. https://www.detentioniq.com/
20. https://www.denim.com/blog/freight-factoring-rates-explained
