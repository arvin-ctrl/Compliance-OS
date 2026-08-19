# Agent 01 — Carrier TMS Billing (McLeod + generic carrier TMS)

**Research date:** 2026-08-19

## Correction to the brief
There is no McLeod product called "Flowbot". The workflow engine is **FlowLogix**; the AI layer is **MPact.RespondAI** plus certified AI partners (Augment, Chain, CloneOps).

## What it actually does

**Detention is the one accessorial McLeod genuinely automates.** The Detention Management module has existed since at least 2004 and the mechanics are unchanged: "At the time of arrival of the load, the system will determine if the site has been designated as eligible for detention charges." Arrival/departure messages from mobile comms create and close the detention record; free time and warning time are configured **per customer and per shipping/receiving location**; two detention periods with different billing codes/rates are supported; the charge auto-appends to the load's billing record. (VERIFIED)

McLeod's own page: arrival/departure can be triggered by "your mobile communications/ELD system in conjunction with the McLeod Symphony Mobile Communications System module" and, "in the absence of mobile communications, manually dispatched movements can also initiate the arrival and departure event information."

**That last clause is the honest answer: detention auto-detects only if you license Symphony, have a supported ELD, and have configured location-level free time. Otherwise a human keys it.**

**Everything else is a charge code a human adds.** No evidence — in product pages, press releases, or release notes for 25.1, 25.2 or 26.1 — of automated detection of TONU, layover, lumper, demurrage, or shortage/damage. TONU in particular has no timestamp signature; it is a cancellation email. McLeod's AI work in 25.2/26.1 targets *inbound tender email → order* and *quote response*, not accessorial capture.

**Rate confirmations flow the wrong direction.** McLeod's eRate Confirmation is an *outbound* broker→carrier e-form with signature capture writing back into PowerBroker. **No evidence McLeod parses an inbound customer rate con PDF and extracts free time / $-per-hour / caps / notice windows.** Those rules are hand-keyed into customer and location profiles.

**Evidence packets are real but document-only.** LogixSolutions Rendition Billing "ensures every invoice meets customer-specific documentation rules by holding submissions until all required files are in place"; DocumentPower captures via scan station, mobile app, email, or third party. That gets POD/BOL/lumper receipt onto the invoice. It does **not** assemble the artifact that wins a detention dispute: a timestamped arrival/departure narrative + the rate-con clause + the email trail.

**Collections exist; accessorial-level dispute tracking does not.** 26.1 added a "fully interactive AR Collections screen" with document attachment; MPact.IQ gives point-in-time AR aging. Nothing surfaced showing short-pay reason codes, deduction matching, or win/loss tracking *by accessorial type*.

## Capability scores

**M** = McLeod · **G** = generic composite (Prophesy/Axon/TruckingOffice/Rose Rocket/AscendTMS)

| Dimension | M | G | Evidence | Label |
|---|---|---|---|---|
| rate_confirmation_ingestion | 1 | 1 | 25.2 AI "imports load tenders from unstructured email"; eRate Con outbound only | VERIFIED/CLAIMED |
| rate_rule_extraction | **0** | **0** | No evidence any target extracts free time/rate/cap terms from a rate con | UNKNOWN |
| gps_eld_timestamps | 2 | 1 | 25+ ELD partners via Symphony; arrival/departure creates detention record | VERIFIED |
| appointment_ingestion | 1 | 1 | Stop scheduling + predictive ETA; no appointment-vs-actual accessorial logic | CLAIMED |
| pod_bol_ingestion | 2 | 1 | DocumentPower multi-channel capture | VERIFIED |
| detention | **2** | 1 | Dedicated module: free time, warning time, 2 periods, per-customer/location rates | VERIFIED |
| tonu | 1 | 1 | Charge-code entry only; no detection logic | UNKNOWN |
| layover | 1 | 1 | Charge-code entry only | UNKNOWN |
| lumper | 1 | 1 | Receipts attach via Rendition Billing; capture manual | VERIFIED |
| demurrage | 0 | 0 | No per-diem/container clock in any target | UNKNOWN |
| accessorial_detection | 1 | 1 | Detention only; Prophesy auto-applies *rated* surcharges, not detected events | VERIFIED |
| evidence_package | 2 | 1 | Rendition Billing holds invoice "until all required files are in place" | VERIFIED |
| invoice_creation | 2 | 2 | Native GL/AR/AP | VERIFIED |
| claim_submission | 0 | 0 | No OS&D/cargo-claim submission workflow | UNKNOWN |
| collection_tracking | 2 | 1 | Automated Collections dunning + interactive AR screen (26.1) | VERIFIED |
| dispute_workflow | 1 | 0 | Attach docs in collections; no short-pay reason codes / rebuttal loop | CLAIMED |
| portal | 2 | 1 | Customer Portal, real-time load access 24/7 | VERIFIED |
| tms_integration | 2 | 2 | Is the TMS; native EDI + 260+ certified partners | VERIFIED |
| eld_integration | 2 | 1 | Samsara, Motive, Geotab, Platform Science, ISAAC, Omnitracs, Trimble, +18 | VERIFIED |
| email_sms_ingestion | 2 | 1 | AI email→order; automated alerts for missing paperwork | VERIFIED |
| accounting_integration | 2 | 2 | Integral GL/AR/AP + QuickBooks Online | VERIFIED |
| recovered_revenue_analytics | 1 | 1 | MPact.IQ detention/dwell per stop; no billed-vs-collected ledger | VERIFIED |
| performance_pricing | **0** | **0** | License/subscription only | VERIFIED |
| customer_specific_rules | 2 | 1 | Free time/warning/rate by customer *and* location | VERIFIED |
| multi_carrier_shipper_support | 2 | 1 | LoadMaster + PowerBroker + LTL | VERIFIED |

**Totals: McLeod 34/50 · Generic composite 23/50.**

## Pricing & switching cost

McLeod publishes no price. Third-party estimates — all **CLAIMED**, from competitor/agency blogs: $75k–$200k/yr for 100–500 trucks; $200k–$500k/yr for 500–5,000 trucks; $50k–$150k/yr PowerBroker; $100k–$500k implementation; +$40k–$80k portal/analytics.

**Detention Management, Symphony, DocumentPower and MPact are separately licensed modules — a carrier can own McLeod and still not own automated detention.**

Corroborating user signal: "It is very very expensive. This can actually be quite cost prohibitive to smaller companies" (Capterra, Feb 2018); "Vendor charges you for everything it can" (Capterra, Dec 2017).

Switching cost is enormous — **which is the point: sell alongside McLeod, never against it.**

## User-reported pain

Reddit was crawler-blocked to this session. Verifiable quotes:

- Capterra LoadMaster (3.7/5, 16 reviews): "Customer Service and training is a joke. Need help? You call, get billed for it, and the person you talk to has no idea what they are doing either." — VP Logistics, Jul 2020
- "Running reports can make the program crash or lag. At times, it can even freeze." — Logistics Manager, Dec 2020
- "Takes so much effort to integrate and customize." — Broker, Oct 2023
- Axon (closed-system failure mode): "No integration abilities. Siloed data, does not play well with others… if you don't do it Axon's way, you're screwed."
- Field reality on evidence: "make sure you let the brokers dispatch know when you have arrived so the clock starts ticking, and there is no argument later on" — TruckersReport, Sep 2021
- Vendor framing (CLAIMED): legacy TMS captures "around 40% of the detention they're owed"; McLeod "demand[s] dedicated administrative resources"
- Benchmark citing ATRI Sep 2024: fleets bill detention at 94.5% but collect on "fewer than 50 percent of the invoices they submit"

## Honest gaps

1. **Rule ingestion is the real hole.** Nobody reads the rate con. Every free-time/rate/cap/notice-window value is hand-configured per customer per location, then rots. Real gap; customers care (it's why detention bills get denied on "no notice within 1 hour"); **not trivial for McLeod to close** — needs document AI plus a rules ontology, which is why they're certifying partners instead of building.
2. **Non-detention accessorials have no detection layer.** Real gap, moderate pain, and **cheap for McLeod to partially close** with FlowLogix rules — this alone is not a company.
3. **No dispute/short-pay ledger by accessorial type.** Cannot answer "what % of billed detention did we collect from Customer X, and why did we lose?" High CFO pain, medium difficulty.
4. **Evidence packets are document checklists, not arguments.**
5. **Business model gap.** McLeod cannot sell contingency. A recovery vendor charging 20–30% of collected dollars sells to the CFO with zero implementation risk — McLeod structurally cannot match that.

## Threat level: MEDIUM-HIGH (partner-or-die dynamic, not a feature race)

McLeod ships two major releases a year and is aggressively certifying third-party AI rather than building it. They will **not** build rate-con rule extraction or contingency-priced recovery in 18–24 months — it's off-model. They **could** close gap #2 in one release. **The genuine threat is that the 260-partner certified program blesses a *different* startup as the detention/accessorial recovery partner.**

Strategy implication: get certified early, sit on top of the Symphony arrival/departure feed and DocumentPower images (both already exist and are the hard part), and monetise on recovery percentage — the seam McLeod's license model cannot cross.

## Research limitations
Reddit blocked to this session's crawler. CCJ and dockclaim.com returned 403. McLeod's own detention and case-study pages served a generic template to direct fetch; detention-page language is quoted from indexed search snippets cross-checked against the 2004 FleetOwner and 2020 TheTrucker articles describing the same mechanics. No McLeod pricing verified.

## Sources
mcleodsoftware.com/detention-truckload-carriers/ · fleetowner.com/news/article/21659908/mcleod-offers-detention-module-to-bill-for-downtime · thetrucker.com/trucking-news/equipment-tech/mcleod-releases-version-20-1... · mcleodsoftware.com/accounting-factoring-finance/ · /billing-and-settlements-automation-truckload-carriers/ · /loadmaster-integrations-truckload-carriers/ · /rate-confirmations/ · /documentpower-truckload-carriers/ · /solutions/ · capterra.com/p/16847/LoadMaster/reviews/ · truckinginfo.com/10251439/mcleods-new-tms-release... · trucknews.com/products/mcleod-software-version-26-1... · torotms.com/blog/driver-detention-management-software · torotms.com/blog/axon-trucking-software-reviews-pricing-alternatives · infios.com/mile/solutions/dispatch-tms · help.roserocket.com/platform/invoicing-overview · thetruckersreport.com/truckingindustryforum/threads/question-for-the-brokers-about-detention.2344760/ · millennialstrucking.com/blog/accessorial-charges-trucking-uncollected-revenue · prnewswire.com/news-releases/chain-and-mcleod-software-launch-certified-integration...
