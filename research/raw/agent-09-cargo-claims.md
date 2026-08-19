# Agent 09 — Cargo claims / OS&D

**Research date:** 2026-08-19

## The "$50 billion in freight claims" figure is unverifiable and almost certainly wrong

It recurs across CorePiper, FreightClaims.com and Accio with no traceable primary source. Sanity-check against carrier-reported claims ratios: at 0.1%–0.9% of revenue paid in cargo claims, the entire US for-hire trucking sector would need ~$5–50 trillion in revenue to generate $50B in *paid* claims. **The real recoverable pool is single-digit billions.** The $50B number is best read as total damaged-goods value plus admin cost plus write-offs — most of which is never claim-shaped.

**Working ESTIMATE:** using the 0.35% claims-ratio baseline against a US LTL sector plausibly $50–60B revenue (UNKNOWN — LTL sector revenue not verified), LTL paid claims ≈ **$175–210M/yr**. Adding TL, parcel and drayage, the *paid* US surface-cargo claims pool is likely **$1–5B/yr**, with an unclaimed/denied/abandoned overhang of similar magnitude.

## Market numbers

| Metric | Value | Status | Source |
|---|---|---|---|
| Detention cost to US trucking 2023 | **$15.1B** = $3.6B direct + $11.5B lost productivity | VERIFIED | ATRI Sept 2024 |
| Share of truck stops with detention | **39.3%**; 135M hours lost | VERIFIED | ATRI |
| Fleets charging detention / paid | **94.5% charge; paid on <50% of invoices** | VERIFIED | ATRI |
| ODFL cargo claims ratio | **0.1%** of revenue (Q4 2025, repeatedly) | VERIFIED | ODFL Q4 2025 release |
| Saia cargo claims ratio | 0.3% (record low, Q2 2025) | CLAIMED | Saia 8-K via search |
| XPO / TForce claims ratios | 0.2% / 0.9% of revenue | CLAIMED | Warp citing earnings calls |
| LTL industry claims baseline | **0.35% of freight spend** | CLAIMED | Synchrogistics LTL Claims Ratio Index |
| LTL damage rate | **1.24%** (~1 in 80 shipments) | CLAIMED | Warp citing 2025 Flock Freight study (n=1,000) |
| Average LTL damage claim | **$1,796** | CLAIMED | Warp |
| Average claim, all modes | $1,200 (mid-market $2–3k) | CLAIMED | CorePiper / FreightClaims.com |
| Claim denial rate | LTL 50–60%; FTL 20–35%; parcel 30–45% | CLAIMED (vendor) | CorePiper |
| Claim-eligible events never filed | ~42%; ~30% abandoned pre-payout | CLAIMED (vendor) | CorePiper |
| Average resolution time | 47 days manual; LTL 60–90 days | CLAIMED (vendor) | CorePiper |
| Missed-deadline share of denials | 20–25% | CLAIMED (vendor) | FreightClaims.com |
| US inland marine DPW 2024 | $34.68B, −4.8% YoY | VERIFIED | AM Best |

## Legal / evidence requirements

**Statute — VERIFIED, 49 U.S.C. §14706:**
- **(a)** carrier "liable to the person entitled to recover under the receipt or bill of lading" for "actual loss or injury to the property."
- **(e)** "A carrier may not provide by rule, contract, or otherwise, a period of less than **9 months** for filing a claim … and a period of less than **2 years** for bringing a civil action." The 2 years runs from **written disallowance**, not delivery.
- **(c)(1)(A)** carriers may limit liability to a value "established by written or electronic declaration of the shipper or by written agreement" if reasonable.

**Prima facie case — VERIFIED, *Missouri Pacific R.R. v. Elmore & Stahl*, 377 U.S. 134 (1964):** shipper must show (1) tender **in good condition**, (2) **arrival damaged**, (3) **amount of damages**. Burden then shifts to the carrier, which must prove one of five common-law exceptions — act of God, public enemy, act of the shipper, public authority, inherent vice — **and** that it was free from negligence. Carrier non-negligence alone is not a defence.

**Regulatory mechanics — VERIFIED, 49 CFR Part 370:**
- **§370.3** a valid claim requires a written/electronic communication that (i) identifies the shipment, (ii) asserts liability, (iii) demands **a specified or determinable amount of money**. Explicitly insufficient standing alone: "bad order reports, appraisal reports of damage, notations of shortage or damage … or inspection reports issued by carriers."
- **§370.5** carrier must acknowledge in writing within **30 days**.
- **§370.9** carrier must **pay, decline, or make a firm compromise offer within 120 days**, then status-update every 60 days.
- **§370.11** salvage: notice to owner where practicable, disposal protecting all interested parties, lot-numbered itemised records, disclosure of self-dealing.

**Limitation of liability** (§14706(f)): carrier must maintain a compliant tariff, give "a reasonable opportunity to choose between two or more levels of liability", obtain agreement, and issue a BOL reflecting it — "the absence of any one of these factors will deprive the carrier of this useful defense."

**Brokers are generally not liable under Carmack** — the claim runs against the carrier. Brokers assume liability only by contract language ("transport", "deliver", "ensure delivery") or by holding out as a carrier. **Concealed damage requires notice within 5 business days of delivery** under NMFC rules.

**Evidence packet that wins:** clean BOL at origin (no exception), POD **with the exception noted at delivery**, commercial invoice proving value, photos, repair/replacement estimate, salvage disposition, governing contract/tariff for the liability cap. **The load-bearing item is the noted exception on the POD — without it, element (2) is contested and the claim usually dies.**

## Who automates this today

**Consolidation alert:** `transolutionsinc.com` now 301-redirects to `infios.com/en/supply-chain-solutions/claims-management`, and myEZClaim support routes to `@infios.com` — **TranSolutions/myEZClaim is owned by Infios** (the MercuryGate/Körber entity). MercuryGate's OS&D page also redirects to Infios. **The category leader and the leading TMS claims module are now the same product.**

Landscape: TranSolutions/myEZClaim (forms + 120+ reports + 400 claim codes, manual entry, no auto-submit); FreightClaims.com (AI email/OCR claim entry); **iNymbus** (RPA into 50+ carrier portals, **$0.40–$0.70 per claim**); **Freehand.ai** ($75M Series B July 2026, Battery + NewRoad; claims $260M recovered in 2025; performance-based pricing — positioned on invoice *audit*, not OS&D specifically); Cass and nVision Global (managed services; nVision claims 87% recovery over ~8,000 claims); **Loadsure** (per-load cargo insurance MGA, Lloyd's coverholder, $11M Series A 2022, <3 days claim-to-payout); telematics/visibility (Tive, Overhaul, Copeland/Sensitech) supply *sensor evidence* but do not file claims. **Only ~28% of mid-market shippers use dedicated claims software** (CLAIMED).

| Capability | myEZClaim | Loadsure | 3PL claims desk |
|---|---|---|---|
| rate_confirmation_ingestion | 0 | 1 | 2 |
| rate_rule_extraction | 0 | 0 | 1 |
| gps_eld_timestamps | 0 | 0 | 1 |
| appointment_ingestion | 0 | 0 | 2 |
| pod_bol_ingestion | 1 | 1 | 2 |
| detention | 0 | 0 | 2 |
| tonu | 0 | 0 | 2 |
| layover | 0 | 0 | 2 |
| lumper | 0 | 0 | 2 |
| demurrage | 0 | 0 | 1 |
| accessorial_detection | 0 | 0 | 1 |
| evidence_package | 2 | 1 | 2 |
| invoice_creation | 2 | 0 | 2 |
| claim_submission | 1 | 1 | 2 |
| collection_tracking | 2 | 0 | 2 |
| dispute_workflow | 2 | 1 | 2 |
| portal | 1 | 2 | 1 |
| tms_integration | 2 | 2 | 2 |
| eld_integration | 0 | 0 | 1 |
| email_sms_ingestion | 0 | 0 | 2 |
| accounting_integration | 1 | 0 | 2 |
| recovered_revenue_analytics | 2 | 0 | 1 |
| performance_pricing | 0 | 0 | 0 |
| customer_specific_rules | 1 | 1 | 2 |
| multi_carrier_shipper_support | 2 | 2 | 2 |
| **Total /50** | **19** | **12** | **41** |

**The 3PL desk scores highest because a human can do everything — the gap is coverage and throughput, not capability. That is the honest competitive picture: your competitor is an underwater person, not a product.**

## Contingency recovery firms & pricing

**Recoupex** (cargo claims recovery for exporters, forwarders, marine insurers), verbatim: *"Only if Recoupex is successful at recovering your cost, do we charge a **20%-50% success-fee**, which we deduct from your claim compensation"* — no upfront, subscription, or membership fee. Claims 77% of submitted claims recovered in 2025, 8–12 week resolution.

**Freight-collection law firms** (Freight Collection Solutions Law Group, Reesor & Associates, Blake Carter) run **25–40% contingency**, scaling with debt age and whether suit is needed.

**Freehand.ai** runs "performance-based pricing" with a $500K-in-30-days-or-$10K-credit guarantee. **iNymbus** $0.40–$0.70/claim.

**A 20–35% contingency on recovered dollars is a defensible, market-validated price point.**

## Claims vs detention: which pool is bigger

**Detention wins on every automation-relevant axis.**

| | Cargo claims | Detention |
|---|---|---|
| Recoverable pool | ~$1–5B/yr paid (ESTIMATE) | $3.6B direct, <50% collected → **$2–4B uncollected** (VERIFIED base) |
| Event frequency | **1.24% of LTL shipments** | **39.3% of all stops — ~30x** |
| Entitlement determinability | Contested: condition at origin, concealed damage, inherent vice, packaging, liability caps | Arithmetic: rate con free time + geofence timestamps |
| Evidence owner | Third parties (consignee must note the exception) | The carrier's own ELD/GPS |
| Counterparty defences | Five Carmack defences + released-rate caps | "We waived it" / "we dispute the timestamps" |
| Clock | 9 months — no urgency | 30–90 day billing windows — urgent |
| Failure mode | **Denial** (50–60% LTL) | **Never invoiced** |

Claims may be a marginally larger gross pool, but detention's recoverable pool is *cleaner*. **Detention's failure mode is that nobody bills it — a pure automation problem. Claims' failure mode is that the claim gets denied on the merits — a legal-judgment problem AI cannot fully close.** And detention's 39.3% event rate means an agent produces value on nearly every load; **a claims agent sits idle 98.8% of the time.**

## Solo-founder suitability verdict

**Claims is a worse wedge than detention for a solo founder.** Five reasons:

1. **AI cannot determine entitlement.** Detention entitlement is `timestamps + contract terms → dollars`. Claims entitlement requires proving good condition at origin, that the exception was noted at delivery, that no Carmack defence applies, and computing recovery net of a released-rate cap extracted from an NMFC class or contract. Steps 1 and 3 depend on facts no system reliably holds.
2. **Frequency is 30x lower.** Contingency economics need volume.
3. **Legal exposure is materially higher.** Asserting liability and demanding a specified sum against a third party on contingency implicates state debt-collection licensing, and advising on settlement value edges toward unauthorised practice of law. **Detention billing is your customer's own invoice on their own contract — no third-party liability assertion.**
4. **The buyer is different and harder.** Claims buyers are shipper-side claims desks (procurement cycle, Fortune 500, Freehand's $75M-funded turf). Detention buyers are carrier-side ops/AR at small fleets — reachable by one person.
5. **No urgency.** A 9-month clock kills the forcing function.

**Counterpoints worth respecting:** claim sizes are larger ($1,796 avg LTL vs ~$100–500 detention); the legal framework is near-strict-liability once the prima facie case is made; regulatory deadlines (30/120/60 days) give automatic leverage most claimants never invoke; and incumbent software is weak (myEZClaim 19/50, doesn't even auto-submit).

**Recommendation: build detention first, add OS&D claims as expansion once you already hold the BOL/POD/telemetry pipe. The document set overlaps ~70%; claims is a natural attach, not a beachhead.**

## Sources
law.cornell.edu/uscode/text/49/14706 · law.cornell.edu/cfr/text/49/370.3 · /370.5 · /370.9 · /370.11 · law.cornell.edu/supremecourt/text/377/134 · govinfo.gov/content/pkg/USREPORTS-377/pdf/USREPORTS-377-134.pdf · beneschlaw.com/insight/carmack-amendment-liability-reminder-of-the-basic-legal-principles/ · stonedeanlaw.com/carmack-the-magnificent-2/ · truckingresearch.org/2024/09/new-research-documents-substantial-financial-and-safety-impacts-from-truck-driver-detention/ · ir.odfl.com/news-events/press-releases/detail/339/... · news.ambest.com/newscontent.aspx?refnum=268434 · wearewarp.com/research/ltl-damage-rates-fewer-touches · corepiper.com/blog/state-of-freight-claims-2026/ · freightclaims.com/best-freight-claims-software/ · /freight-claim-time-limits/ · freehand.ai · infios.com/en/supply-chain-solutions/claims-management · loadsure.net/for-freight/ · recoupex.com · atsinc.com/blog/a-freight-brokers-role-in-cargo-claims · synchrogistics.com/synchro-ltl-claims-index/
