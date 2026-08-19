# Agent 05 — Visibility Platforms (project44, FourKites)

**Research date:** 2026-08-19

## Corrections to the brief
- FourKites has migrated to **fourkites.ai** (fourkites.com 301-redirects).
- FourKites "Fin AI agents" **does not exist**. The agents are Tracy, Sam, Alan, Cassie, Polly, Sophie.
- p44 "Facility Insights"/"Network Intelligence" returned no matching product pages; the analogous assets are D&D Optimization, Port Intel, and the carrier VOC.

## What "detention" means in their products (precise)

Neither product is "(c) a billable claim". Both are **(a) descriptive + partial (b) cost allocation, pointed at the buyer.**

**project44** — D&D Optimization does "detention and demurrage fee calculations at the shipment level based on custom contracts" between the customer and *their terminals and ocean carriers*. This is **container D&D — the shipper's payable** — not truckload driver detention as a carrier receivable. (VERIFIED)

The closest thing to evidence handling is explicitly **defensive**: Ports & Terminals says historical data "enables you to audit confirmed pick-up and gate messages to **refute any inappropriate charges**." That is a claim-*defeating* workflow, not a claim-*filing* one. (VERIFIED)

For truckload detention p44 is (a) only. Its own explainer describes carriers tracking wait times "through check-in/check-out logs, ELDs... or yard management systems (YMS) **and invoice shippers for excess time**" — attributed to industry practice, with p44's role limited to systems that "automate scheduling, provide alerts, and measure dwell times to identify process gaps." **p44 does not claim to produce the invoice.** (VERIFIED)

**FourKites** — D&D capabilities are "exception dashboards, notifications and alerts" flagging containers "likely to incur D&D fees," explicitly framed as "shippers can mitigate fees **before they occur**." Dynamic Yard adds "proactive detention monitoring"; Yard Analytics computes facility-level detention exposure. **No invoice, no claim packet, no submission** — VERIFIED absence across every page fetched.

## Buyer-side conflict of interest — advertised, not inferred

**This is the strongest finding of this lane.**

FourKites measures its own success in **destroyed carrier detention revenue**:
- Trane Technologies "removed approximately **$2.69M** in annual detention costs across two facilities"
- Kimberly-Clark "**52% reduction** in detention fees" (CLAIMED — not corroborated in the underlying press release)
- Dynamic Yard customers see "reductions in detention costs ranging from **40% to as much as 80%**"
- Appointment Manager was launched to "**slash detention times** at Warehouses and Distribution Centers"

Every dollar in those case studies is a dollar a carrier did not bill. (VERIFIED)

project44's AI agent portfolio is sold on the promise that agents "**reduce freight spend**" for shipper operations teams. Its Intelligent TMS ships a **freight audit engine** that "flags discrepancies in real time" via "automated invoice validation" — invoice scrutiny aimed at reducing what the shipper pays, the exact inverse of carrier revenue recovery. (VERIFIED)

**Nuance — p44 is not monolithic.** Its carrier FAQ, under "What's in it for me?", lists benefit #2: "**Collecting fees when dwell time occurs, supported by historical data on wait times**" (VERIFIED verbatim). But benefit #1 on the same list is "**reducing** dwell time" — the two cancel out, and there is no product behind the collection angle.

**Why the conflict is structural:** revenue comes from shippers and facility operators. A credible carrier-side detention-billing product would take money directly out of the paying customer's pocket. Neither can build it without cannibalising its installed base.

## Data rights — the decisive constraint (and the hardest moat)

Both hold timestamps of adequate *technical* fidelity (geofenced arrival/departure, UTC, ELD-sourced). The blocker is **contractual, and severe.**

**project44 Carrier Services Agreement v18.3 EU** (VERIFIED, PDF):
- §5.1: "Carrier... shall retain ownership of Data **in the state as such Data is provided**."
- §5.2: "Any project44 Services prepared by project44 based in whole or in part on Data provided pursuant to the Agreement **shall be owned by project44**."
- §3.1–3.2: Shipment Data and Operational Status route *to Customers* (shippers); all other carrier data "discarded."
- §6.1 ("NO CHARGES"): data provided "free-of-charge" with no remuneration to the carrier.

**The carrier owns its raw pings; p44 owns the computed dwell/detention output.** A carrier contributes the raw material for its own detention evidence, receives no computed claim artifact back, and cannot assert ownership over the derivation.

**FourKites data-provider terms** mirror this: providers retain title in the Data (§3.1 grants a limited licence), but **§3.4: "FourKites shall own and retain all right, title, and interest in and to Aggregate Data."** Distribution is customer-controlled — data goes to third parties "to the extent requested or authorized by such Customer." **The shipper, not the carrier, gates who sees the timestamps.** (VERIFIED)

Neither agreement authorises *or* prohibits use as billing evidence. UNKNOWN whether a carrier's own exported data would survive a contested dispute; no case law or vendor guidance found.

## Capability scores

0 = absent · 1 = partial/adjacent · 2 = native

| Capability | p44 | FourKites |
|---|---|---|
| rate_confirmation_ingestion | 1 | 1 |
| rate_rule_extraction | 1 | 2 (parses base rates, surcharges, accessorial fees, FAK — ocean) |
| gps_eld_timestamps | 2 | 2 (900+ GPS/ELD providers) |
| appointment_ingestion | 2 | 2 |
| pod_bol_ingestion | 0 (no evidence found — treat as UNKNOWN) | 2 (Polly chases missing PODs) |
| detention | 1 | 1 |
| tonu | 0 | 0 |
| layover | 0 | 0 |
| lumper | 0 | 0 |
| demurrage | 2 | 2 |
| accessorial_detection | 1 (shipper-side) | 1 |
| evidence_package | 1 (defensive: "refute") | 1 |
| invoice_creation | **0** | **0** |
| claim_submission | **0** | **0** |
| collection_tracking | **0** | **0** |
| dispute_workflow | 1 (defensive) | 1 (Cassie "validates receiver claims") |
| portal | 2 | 2 |
| tms_integration | 2 (ships its own TMS) | 2 |
| eld_integration | 2 | 2 |
| email_sms_ingestion | 1 | 2 (Tracy: email, WhatsApp, voice, SMS) |
| accounting_integration | 1 | 1 |
| recovered_revenue_analytics | 1 (cost *avoided*, not revenue recovered) | 1 |
| performance_pricing | **0** | **0** |
| customer_specific_rules | 2 | 2 |
| multi_carrier_shipper_support | 2 (280,000+ carriers) | 2 |

**Totals: p44 25/50 · FourKites 30/50** — concentrated entirely in ingestion and detection. Both score **0 on invoice_creation, claim_submission, collection_tracking, performance_pricing, TONU, layover, and lumper.**

## Pricing & access

Carrier-side connectivity is **free on both** (VERIFIED): p44 — "Nothing. Joining the project44 carrier network is entirely free for carriers"; FourKites — "Free to join. Free to use. Always." But free tiers are *data-contribution* tiers: no detention analytics, no D&D module, no billing output.

No public pricing from either (VERIFIED — both direct to sales). Third-party estimates, all CLAIMED: FourKites enterprise "starts at approximately $75,000 annually"; p44 "$50,000 to $200,000 per year" for 10K–100K annual shipments; ~$3.03/container ocean.

**A carrier can buy the platform, but there is no billing product to buy — and at $75K+ entry against per-load detention economics, the math fails below large-fleet scale.**

## Threat level: p44 LOW-MEDIUM · FourKites LOW

*Why not lower for p44:* it alone has the full mechanical stack — a TMS, a freight audit engine already parsing invoices and flagging discrepancies, per-customer contractual rate rules, an aggressively-extended agent framework (LunaPath.ai acquisition; 34% YoY new-ARR growth attributed to agent momentum). Re-pointing that audit engine from payables to receivables is an engineering afternoon.

*Why it still won't happen:* the six-agent portfolio contains **no** billing, claims, or recovery agent — the roster is Procurement, Disruption, Network Ops, Exceptions, Slot Booking, Carrier Onboarding, all sold to reduce shipper spend. And §5.2 means p44 would be selling carriers a claim built on data p44 owns and the shipper paid for, against the shipper who is p44's actual customer.

**Realistic risk is displacement, not competition.** If these platforms drive detention incidence down 40–80% at enterprise facilities, the recoverable pool shrinks at exactly the accounts most worth pursuing. **Counter-position: enterprise shippers running p44/FourKites are the *hardest* targets; the addressable market is the long tail of facilities with no YMS, where the timestamps are unowned.**

Watch two signals: an accessorial or settlement agent appearing in either agent roster, and any move toward contingency pricing. Neither is present today.

## Honest gaps in this research
- No named accounting/AP/freight-audit integration partners verified for either vendor. UNKNOWN — search budget exhausted (200/200).
- p44 `pod_bol_ingestion` scored 0 on absence of evidence, not evidence of absence. Treat as UNKNOWN.
- developers.project44.com returned 403; could not confirm at endpoint level whether geofence entry/exit or computed dwell fields are exposed, or their precision/immutability — exactly what determines billing-evidence quality.
- p44 **US** carrier agreement not read; only the EU v18.3 version. US terms may differ materially on §5.2.
- No FourKites master services agreement published; customer-side data rights UNKNOWN.

## Sources
p44: project44.com/press-releases/project44-launches-detention-demurrage-optimization-to-better-manage-risk-and-reduce-costs/ · /platform/visibility/ports-terminals/ · /for-carriers/carrier-faq · /blog/how-project44s-visibility-benefits-carriers/ · /press-releases/project44-launches-ai-agent-portfolio-at-decision44-.../ · /press-releases/project44-unveils-intelligent-tms-.../ · /resources/what-is-detention-cost-in-supply-chain/ · /carriers/connect/api/ · developers.project44.com/api-reference · nmc-eu12.voc.project44.com/resources/Documents/Portal_services_agreement_Carriers_version_18.3_EU_Final.pdf

FourKites: fourkites.ai/press/fourkites-releases-powerful-new-capabilities-to-manage-runaway-demurrage-and-detention-fees · /press/fourkites-helps-alleviate-warehouse-labor-crisis-with-next-generation-dynamic-yard... · /press/fourkites-introduces-industry-first-enhancements-to-eliminate-manual-workflows-and-slash-detention-times... · /platform/yard-management · /fourkites-ai/agentic-ai · /press/booking-connect-ocean-agentic-freight-booking · /network/carriers · /legal/general-terms-and-conditions-for-data-providers

Third-party pricing (CLAIMED): locus.sh/blogs/project44-pricing-guide/ · locus.sh/blogs/fourkites-pricing-guide/ · blogs.tradlinx.com/how-much-does-project44-fourkites-or-vizion-really-cost...
