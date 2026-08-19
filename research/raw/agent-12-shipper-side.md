# Agent 12 — Shipper side (enterprise TMS, dock/yard, dispute prevention)

**Research date:** 2026-08-19

## Headline, negative and verified

**No major shipper TMS adjudicates a detention claim against facility timestamps. They adjudicate against *price*, not against *time*.**

Oracle's own datasheet for Freight Payment, Billing and Claims (VERIFIED, Oracle-published PDF) states the mechanism verbatim: *"Freight bills are automatically matched against bill-of-lading details and audited based on **user-defined percentage and/or amount tolerances**. Freight bills within tolerance are approved and automatically interfaced to any Accounts Payables system."*

**That is a tolerance gate, not an evidence gate. A $400 detention line that falls inside the shipper's dollar/percent tolerance auto-pays without anyone checking whether the truck was actually there.**

Oracle's CLAIMS module is explicitly scoped to **cargo damage** — *"Enter claims for goods damaged in-transit… Submit the claim to the appropriate service provider… Track the progress of the claim to disposition"* — **not** accessorial disputes. Key Features list "Cover transportation rate contracts, discounts, and accessorial charges" — accessorials are *rated*, not *validated against events*.

Blue Yonder is the same shape (VERIFIED, FAQ page): *"It manages the complex world of Accessorials (Fuel Surcharges, Detention Fees, Stop-Off Charges)"* and *"It automatically compares the Carrier Invoice against the Contracted Rate. If a carrier overcharges by even $10, the system flags it."* **Contracted-rate comparison. Detention is named, but the check is "is $75/hr the right rate?" — never "did 2.4 hours actually elapse?"**

No language on gate timestamps, appointment verification, or free-time calculation was found on any Oracle or Blue Yonder page fetched (UNKNOWN → treated as absent). Manhattan's and e2open's pages returned no retrievable accessorial language (UNKNOWN).

## Capability scores

| Capability | Oracle OTM | Blue Yonder TMS | Opendock |
|---|---|---|---|
| rate_confirmation_ingestion | 2 | 2 | 0 |
| rate_rule_extraction | 1 | 1 | 0 |
| gps_eld_timestamps | **0** | **0** | **0** |
| appointment_ingestion | 1 | 1 | 2 |
| pod_bol_ingestion | 2 | 1 | 1 |
| detention | 1 | 1 | 1 |
| tonu | 0 | 0 | 0 |
| layover | 1 | 0 | 0 |
| lumper | 1 | 0 | 0 |
| demurrage | 1 | 0 | 0 |
| accessorial_detection | 1 | 2* | 0 |
| evidence_package | **0** | **0** | 1 |
| invoice_creation | 2 | 1 | 0 |
| claim_submission | 1 | 0 | 0 |
| collection_tracking | 1 | 0 | 0 |
| dispute_workflow | 1 | 1 | 0 |
| portal | 2 | 1 | 2 |
| tms_integration | 2 | 2 | 1 |
| eld_integration | **0** | **0** | **0** |
| email_sms_ingestion | 0 | 0 | 1 |
| accounting_integration | 2 | 2 | 0 |
| recovered_revenue_analytics | 1 | 1 | 1 |
| performance_pricing | **0** | **0** | **0** |
| customer_specific_rules | 2 | 2 | 1 |
| multi_carrier_shipper_support | 2 | 2 | 2 |
| **Total /50** | **27** | **21** | **13** |

\* **Note the polarity inversion:** Blue Yonder's `accessorial_detection` = 2 means detecting an **overcharge** — the mirror image of a carrier detecting an underbilling. **Every "2" in the TMS columns is a defensive capability.** The universal zeros — `gps_eld_timestamps`, `eld_integration`, `evidence_package`, `performance_pricing` — are exactly the columns a neutral evidence layer would own.

## Dock/yard timestamp ownership

**The gate record exists, it is machine-readable, and it is the shipper's.**

Opendock's developer docs (VERIFIED, developer.loadsmart.com) expose asset-visit events with `createDateTime` per `eventType` — **Arrived**, **Docked**, **Departed**, plus attach/detach — joined to `appointmentId`, `licensePlate`, `dotNumber`. **That is a detention calculation in raw form.** But the endpoint (`GET /asset-visit`) sits under "for-warehouses"; **there is no documented carrier-facing timestamp API.** Carriers get a free login to *book, update, cancel* appointments and receive gate instructions by SMS — a scheduling surface, not an evidence surface.

Opendock's marketing is explicit about the *purpose* of the record: *"Digital timestamps reduce detention disputes and strengthen carrier trust"* and *"from gate-in to gate-out, each move is logged with time-stamped proof"* (VERIFIED). FourKites attaches a dollar figure: Trane Technologies *"removed roughly $2.69M in annual detention across two sites"* (CLAIMED). C3 Solutions' detention monitoring *"flags dwell time and notifies carriers as trailers come free"* — a shipper-side alarm, not carrier evidence.

**Read that FourKites number carefully. $2.69M was not recovered by a carrier — it was eliminated from a shipper's payable. The entire YMS category sells detention reduction to the party who pays it. The timestamp record is built as the shipper's defensive exhibit.**

## Evidence asymmetry analysis

The structure: **the shipper holds gate/dock timestamps in a YMS the carrier cannot query; the carrier holds ELD/geofence data the shipper has no contractual duty to accept. Neither is neutral, and the paying party controls adjudication.**

Practitioner guidance (CLAIMED, carrier-side blogs) says carriers must *layer* evidence — gate-clock photo, dock supervisor signature, BOL timestamps, then ELD as "the second layer" — because no single source is dispositive. Transport Topics frames it from the data side: *"The gap between the fleets that charge for detention and the less than 50% who actually receive payment can be closed using precise data"* (VERIFIED quote), citing "time-stamped, geofence-verified and electronic logging device-corroborated records."

**Outcome data settles who wins.** ATRI 2024 (VERIFIED): **94.5% of fleets charge detention fees, and they are paid for fewer than 50% of those invoices.** Detention occurred on **39.3% of all stops** in 2023 (56.2% reefer), costing **$3.6B direct + $11.5B lost productivity** across **135M+ hours**. Carriers also raised detention rates a **median 3% from 2018–2023** while hourly trucking cost rose **21.4%** — **carriers are not even repricing the exposure, let alone winning disputes.**

**Shippers win today, roughly half the time, by default.** That creates a theoretical market for a neutral standard — but note who is harmed. **The party losing $15B/yr is the carrier. A neutral evidence standard is a *transfer* from shipper to carrier. Asking a shipper to fund it is asking them to buy a weapon aimed at their own P&L.** Only two shipper motives survive: (a) killing the ~5–15% of accessorials billed *incorrectly* (CLAIMED, FreightPlus internal audit across 10,000+ monthly loads / $300M managed), and (b) carrier-of-choice positioning in a tight market. **Neither is a burning platform.**

## Shipper detention spend (cited)

Precise shipper-side detention-as-%-of-freight-spend does **not** exist in public data.

- **Accessorials = 20–30% of total freight spend** for a typical shipper (CLAIMED, FreightPlus 2026 — explicitly uncited by the publisher; their worked example hits 40.7% but is a modelled scenario)
- Accessorials add **8–15%** to a standard freight invoice; ~25–40% of mid-market shipments carry a non-fuel accessorial (CLAIMED, uncited)
- Detention rate **$75–$150/hr, free time 15–30 min** for LTL contexts (CLAIMED). Truckload commonly starts at 2 hours — **67% of carriers charging detention start at the two-hour mark** (VERIFIED, ATRI)
- **5–15% of accessorial charges are billed incorrectly** (CLAIMED, FreightPlus proprietary)

Detention specifically is a *fraction* of that accessorial bucket — the honest statement is **UNKNOWN, likely low-single-digit % of freight spend.**

**Budget owner:** freight audit & payment sits with transportation procurement/logistics ops for rules and with AP/finance for disbursement; Oracle's own flow confirms **AP holds the money but not the rules. That split is itself a problem: the person who feels the pain has no budget, and the budget holder has no visibility.**

## Enterprise procurement reality for a solo founder

- Enterprise (>$100K ACV) sales cycle: **90–180+ days**; deals over $100K "regularly run 6–9+ months" (VERIFIED, gradient.works citing Ebsta 2024 / Norwest 2024)
- Average B2B cycle now **6.5 months**, up from 4.9 in 2019 (VERIFIED)
- **Security review alone adds 2–6 weeks**; SOC 2/GDPR/vendor-risk adds 2–4 weeks even mid-market; late-surfacing SSO or SOC 2 gaps add another **10–21 days** (CLAIMED)
- **~1/3 of organisations have lost deals for lacking required security certification**; SOC 2 is "table stakes" (CLAIMED)
- Buying committee: **6–10 stakeholders**, enterprise reaching **17+** (CLAIMED, attributed to Gartner)

For a "dispute prevention" product, add: read access to the YMS/gate system (IT + facility ops), read access to the TMS (transportation IT), and a touch on AP — **a three-department integration.**

**Realistic solo-founder expectation: 9–15 months from first call to first dollar, with SOC 2 Type II required before signature.**

## Verdict on the shipper-side wedge

**Year-3 customer. Not a first customer. Do not start here.** Four independent reasons, each sufficient:

1. **Wrong side of the value transfer.** The $15B loss is the carrier's. Shippers already win ~50%+ of disputes via the tolerance-based auto-approval Oracle ships by default. "Dispute prevention" sold to a shipper is a modest overcharge-recovery play competing against incumbent FAP firms who already do it on contingency with zero integration lift.
2. **The evidence you need is behind the buyer's firewall.** Opendock's `asset-visit` timestamps are warehouse-scoped. A neutral standard requires shipper consent to publish evidence that will be used against them. **That is not a product problem; it is an incentive problem.**
3. **Cycle math kills a solo founder.** 9–15 months, 6–17 stakeholders, SOC 2 Type II gate. A single-person company burns its runway inside one enterprise cycle before revenue.
4. **The incumbents' zeros are not accidental.** Oracle and Blue Yonder score 0 on `gps_eld_timestamps` and `evidence_package` because timestamp-level adjudication is **not what their buyer wants. That gap is a *demand* gap, not a *supply* gap** — and unfilled gaps in mature categories usually mean nobody is paying.

**Where the shipper becomes interesting (year 3):** once a carrier-side install base makes you the de-facto evidence format, the shipper buys the *other end* of the wire — a defensible, auditable accessorial ledger that reduces both fraudulent claims and relationship friction. **The neutral standard has to be minted on the side that is bleeding, then sold to the side that pays. Build carrier-first; the shipper is second-order monetisation, and only after the format has network weight.**

## Coverage gaps (UNKNOWN)
e2open, SAP TM, Manhattan Active TM, Coupa, Körber, Alpega, MPO, Uber Freight Powered by Transplace accessorial specifics — pages 404'd or returned no relevant language; session WebSearch budget (200) exhausted. Also UNKNOWN: published shipper MSA cycle times, insurance/COI minimums, typical minimum enterprise deal size.

## Sources
oracle.com/a/ocom/docs/applications/supply-chain-management/oracle-freight-payment-billing-claims-ds.pdf · oracle.com/scm/logistics/transportation-management/ · info.blueyonder.com/transportation-management/what-is-blue-yonder-transportation-manager · gartner.com/en/documents/6290615 · developer.loadsmart.com/docs/opendock/for-warehouses/gate-operations · blog.opendock.com/dock-scheduling-process · lp.opendock.com/gate-management · fourkites.ai/platform/yard-management · withvector.com/blog/vector-vs-c3-solutions-comparison/ · truckingresearch.org/2024/09/new-research-documents-substantial-financial-and-safety-impacts-from-truck-driver-detention/ · truckinginfo.com/news/truck-driver-detention-study-shows-some-improvement · ttnews.com/articles/detention-data-drives-decisions · freightplus.io/blog-ltl-accessorial-charges-2026/ · gradient.works/blog/2025-b2b-sales-performance-benchmarks · cyberbase.ai/blog/enterprise-saas-deal-acceleration
