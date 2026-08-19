# Agent 02 — MercuryGate (now Infios) + Trimble Transportation

**Research date:** 2026-08-19

## Corrections to the brief
- **MercuryGate no longer exists as a brand.** Körber Supply Chain Software completed the acquisition **2024-10-01**, rebranded to **Infios** March 2025. Every `mercurygate.com` deep link 301-redirects to `infios.com` root; the MercuryGate collateral library is gone. The product is "Infios Transportation Management (TM)".
- **Kuebix is no longer Trimble's.** Trimble announced its shutdown (2022) and sold it to FreightWise November 2023.

## What it actually does

**Trimble is the real accessorial-automation incumbent, and materially stronger than expected.**

*Detention is genuinely productised and has been since 2004.* TMW Back Office billing rates expose a `Method` field on the Time tab with **"Delay cumulative"** (one invoice detail for all detention on the order) vs **"Delay per stop"**. Free time is set as **`Min total` / `Max total` in decimal hours** (1.0000 = one hour). Two calculation modes: *"Compute Arrival/Departure difference only"* and *"Use 'greater' of Arrival or Scheduled Earliest time to compute time"* — the second is the contractually correct one, preventing early arrival from inflating the claim. (VERIFIED) A mirrored doc does the same for detention **pay**. The 2004 launch coverage: *"The system can determine automatically when a detention charge is warranted, and create an invoice detail for it"* — comparing actual time against **contracted tolerances per customer**.

*TruckMate has a separate, licensed Detention Billing program.* Requires **License Key #28000 or #28001**, driven by **Detention Rate Sheets** in Rates Maintenance > Detention Tab, filters by **Trailer (Demurrage) or Driver**, posts charges as an accessorial on the original freight bill or onto a new one. Stated prerequisite is decisive: *"Detention Billing requires real-time management tools on Driver or Equipment activity, which means you must have Mobile Communications integration with your Drivers and/or Trailers for Detention Billing to work."* (VERIFIED)

*The GPS→billing fusion is real but modular.* TMW.Suite catalogues **Geofencing** as a discrete item: *"Uses GPS position reports from certain in-cab logging and tracking systems to automate 'circle of service' event updates for Dispatch."* **TripAlert** flags transit delays and **excessive dwell** using HOS calculations. **Trimble Places** covers 4.9M geofenced locations with polygonal boundaries, marketed as: *"With accurate vehicle arrival and departure times, we can help carriers with contracts, service agreements, appointment windows, dispatch and detention fee collection."*

**So the chain geofence → auto arrival/departure → detention rate rule → auto invoice detail exists end to end at Trimble.** Caveats: assembled from separately-catalogued (separately-priced) modules; depends on *"certain"* in-cab systems; the 2004-era default detection path was driver macros or dispatcher keystrokes, not GPS.

*Contract ingestion is newly automated.* Trimble TMS *"reads your PDF rate sheets and RFP tables, including lanes, fuel surcharges and accessorials, and drops them straight into the rating engine"*; **Quick Bill** — *"When the freight you actually run matches the contracted rates, Quick Bill creates the invoice for you automatically"*; **Order Intake Agent** claims to *"eliminate the need for manual review in as many as 90% of standard order entries"*; a **Contract Intake Agent** builds rate tables from customer contracts.

**The most important negative finding: Trimble's 2025-11-17 AI-agent announcement contains NO agent for detention, accessorials, settlement, or claims.** Six agents announced (Order Intake, Invoice Scanning, Road Call, Fleet Assistant, Route Assistant, Tender Evaluation) — AI investment is going to order entry and maintenance, not revenue recovery.

**Infios is much weaker on accessorial origination.** Its TM page mentions reducing *"expediting, detention, and service failures"* — detention **avoidance**, not billing. No detention calculation module documented. The one genuine leakage feature is Control Tower: *"Finance can validate loads delivered but not invoiced and create invoices for those loads as required"* (VERIFIED) — load-level unbilled revenue, not accessorial-level.

## Capability scores

| Capability | Infios | Trimble | Evidence |
|---|---|---|---|
| rate_confirmation_ingestion | 0 | **2** | T: order entry reads emails/PDFs into structured load records |
| rate_rule_extraction | 0 | **2** | T: reads PDF rate sheets/RFP tables incl. accessorials; Contract Intake Agent |
| gps_eld_timestamps | 1 | **2** | T: Geofencing auto-generates arrival/departure; TripAlert dwell+HOS |
| appointment_ingestion | 1 | 1 | T: "Scheduled Earliest" used in detention calc |
| pod_bol_ingestion | 1 | 1 | I: upload images/BOL/receipts to claim record. T: D2Link signature capture |
| detention | 0 | **2** | T: Delay cumulative/per-stop, Min/Max free time, auto invoice detail |
| tonu | 0 | 1 | T: generic Extra Charge Codes — manual |
| layover | 0 | 1 | T: same generic mechanism |
| lumper | 0 | 1 | T: same generic mechanism |
| demurrage | 0 | **2** | T: TruckMate Detention Billing filters by "Trailer (Demurrage)" |
| accessorial_detection | 1 | 1 | I: FAP flags accessorial discrepancies on inbound invoices |
| evidence_package | 1 | 1 | Neither assembles a dispute packet |
| invoice_creation | **2** | **2** | I: Control Tower delivered-not-invoiced. T: Quick Bill |
| claim_submission | **2** | 0 | I: "loss, damage, returns, overcharges and vendor claims" |
| collection_tracking | **2** | 1 | I: deadline alerts, communication records, audit trail |
| dispute_workflow | **2** | 1 | I: FedEx FBAP "managing disputes on behalf of customers" |
| portal | **2** | 1 | I: Claims Portal + Control Tower |
| tms_integration | **2** | **2** | I: 70+ pre-built integrations |
| eld_integration | 1 | **2** | T: owns PeopleNet/Trimble ELD; SmartLink/TotalMail/FleetConneX |
| email_sms_ingestion | 0 | **2** | T: Order Intake Agent processes email, PDFs, EDI |
| accounting_integration | **2** | **2** | I: SAP/NetSuite/Oracle/Dynamics |
| recovered_revenue_analytics | 1 | 1 | I: 120+ reports, "cuts claim losses 63%" |
| performance_pricing | **0** | **0** | Neither offers contingency; Trimble markets "predictable monthly pricing" |
| customer_specific_rules | **2** | **2** | T: per-customer free time + contracted tolerances |
| multi_carrier_shipper_support | **2** | **2** | I: all modes, 150+ countries, 5,000+ carriers |

**Totals: Infios 27/50 · Trimble 37/50.** Trimble is the highest-scoring incumbent found in the entire study.

## Pricing & switching cost

No vendor-published pricing for either. ITQlick estimates (**CLAIMED, low confidence**): MercuryGate ~$1,500/mo (1 user), ~$5,000/mo (10 users), ~$20,000/mo (100 users); SMB implementation $30–50k+ year one; 3–6 month timelines (up to ~9 months multi-client 3PL). Trimble claims "predictable monthly pricing", "20% reduction in monthly expenses", "7% increase in vehicle uptime" (CLAIMED, unsourced marketing).

**TruckMate's Detention Billing is license-key gated (#28000/#28001) and Geofencing/TripAlert are separate catalogue SKUs — detention automation is an upsell, not a default. Many Trimble customers likely own the platform but not the detention stack.**

## User-reported pain

Capterra TMW.Suite: a Settlement Administrator/Billing user — *"This didn't integrate with our accounting software that we were using"*, forcing manual re-keying of billing data. A Managing Director — *"I didn't like the price as it was higher and confusing"* (value-for-money 3.3/5). Training — *"You can't self train. You have to have someone show you the in's and out's."* TruckMate ~77% satisfaction with recurring "outdated interface" and "hard to learn" themes.

**No direct user complaint specifically about accessorial or detention billing found in either product — label UNKNOWN, not absence of pain.**

Sharpest third-party signal: Navix's Infios integration doc sells *"eliminate up to 12 manual audit steps and clicks per load"* against MercuryGate — implying native audit is click-heavy — and discloses a hard constraint: *"MercuryGate restricts partner integrations from modifying Shipping Order data, which encompasses customer rates and invoices."*

## Honest gaps

1. **Both audit the wrong direction.** Trimble *"flag[s] discrepancies—such as unexpected fuel surcharges or accessorial fees—for quick manual resolution"*; Infios FAP addresses *"discrepancies and overcharges."* Neither detects **under-billing**.
2. **Infios "Claims Management" is cargo loss & damage + overcharge claims** — a shipper recovering from carriers. Not accessorial revenue recovery despite keyword overlap.
3. **No evidence package as a deliverable.** Neither assembles rate-con clause + geofence timeline + POD timestamps + signed BOL into a submittable, short-pay-defensible packet.
4. **No short-pay recovery loop.** Neither reconciles a partial payment against the denied accessorial line, nor re-argues it.
5. **Trimble's detention is entitlement-*calculation*, not entitlement-*defence*** — it computes and bills, but has no workflow for when the shipper refuses.
6. **TONU has no home in either.** It's a non-move; there's no order to attach a delay charge to.
7. **Neither offers contingency pricing.**
8. **Integration write-back is restricted on Infios** — a partner recovery product can attach but not write rates/invoices.
9. **Trimble's AI roadmap skips settlement entirely.**

## Threat level

**Trimble: HIGH (defensive moat, not offensive competitor).** Owns ELD + geofence + TMS + rating and ships a working auto-detention path with per-customer free time. **For any carrier already on TMW.Suite/TruckMate *with* the mobile-comms and detention modules licensed, the core detection pitch is largely answered** — sell dispute defence, short-pay recovery, and evidence packaging instead. But its detention logic is 20+ years old, modular/upsell-gated, weak beyond detention/demurrage, and entirely absent on the collection side.

**Infios: LOW–MEDIUM, and destabilised.** Weak native accessorial origination, payer-side audit orientation, and an in-progress rebrand that deleted the entire MercuryGate content library — customer confusion and integration-partner churn create a live wedge. Watch for Infios bolting FAP logic onto TM.

## Method limits
`learn.transportation.trimble.com` help pages are JS-shelled and serve an SMTP-deprecation notice to fetchers — detention configuration details are from the search engine's index of those exact URLs (field names verbatim), not a direct render. Trimble pricing/implementation timelines UNKNOWN. WebSearch budget (200/200) exhausted.

## Sources
infios.com/en/knowledge-center/news/koerber-supply-chain-software-completes-acquisition-of-mercurygate · dcvelocity.com/technology/supply-chain-it/korber-supply-chain-software-to-rebrand-as-infios · infios.com/en/supply-chain-solutions/transportation-management · /freight-audit-and-payment · /claims-management · businesswire.com/news/home/20220215005144/en/MercuryGate-Launches-Smart-Transportation... · hs.navix.io/customer-support-center/integrating-mercurygate-with-navix · learn.transportation.trimble.com (BR-Ex-DetentionCharges, PR-Ex-DetentionPay, detentionbill, codesmaintaccchgs, Selecting204-990Settings) · truckinginfo.com/news/tmw-adds-detention-tracking-feature · transportation.trimble.com/en/solutions/transportation-management/carrier-tms · /products/tmw-suite · /en/solutions/freight-sourcing-settlement · transportationinfo.trimble.com/suitecatalog/tracking-mobile-communications · transportation.trimble.com/en/solutions/mapping-and-routing/trimble-places-data · news.trimble.com/Trimble-Announces-New-AI-Agents-and-Workflows... · freightwaves.com/news/trimble-to-shutdown-tms-provider-kuebix · capterra.com/p/266770/TMWSuite/
