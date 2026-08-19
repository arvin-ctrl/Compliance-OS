# Agent 06 — Freight Audit & Payment (FAP) industry

**Research date:** 2026-08-19

## The category
~Century-old, mature, consolidated. Sits between a shipper's TMS and its AP/GL: ingest carrier invoices (EDI/PDF/paper), rate against stored contracts/tariffs, kick exceptions, pay the carrier, allocate to GL, report. Players: Cass (NASDAQ: CASS, f. 1906), AFS Logistics, Trax, nVision Global, Intelligent Audit (1996), CTSI-Global, A3, enVista, and AI-native Loop (2021).

**Scale (VERIFIED):** Cass processed **34.45M transportation invoices** and **$36.45B transportation dollar volume** FY2025, plus 16.51M facility invoices (10-K). Trax: $25B spend, 125+ enterprise customers, 21,000+ carriers, 120 countries (CLAIMED). AFS: 304M+ invoices, $39B managed annually (CLAIMED). Intelligent Audit: 2.1B+ shipments audited, 20% of Fortune 50 (CLAIMED).

## Direction of value — CONFIRMED, strongly

**FAP is a shipper-side cost-avoidance industry, not a carrier-side revenue industry.**

- Cass's 10-K: services provided to "**large manufacturing, distribution and retail enterprises**" — the shipper contracts; carriers are payees. (VERIFIED)
- Loop's homepage: "**80% of all carrier freight invoices contain errors or discrepancies**" and "**10% of freight spend is lost to overpayments**" — framed as shipper leakage.
- Loop's AP-automation product for brokers/3PLs is payables-only: audits what you *owe* carriers, not what customers owe you.

**Is any established vendor in the business of finding UNDER-billing for the carrier/broker? None found.** Nearest things:
1. Cass earns "discounts received for services provided to carriers" — a payment-network discount, not under-billing detection (VERIFIED, 10-K).
2. Intelligent Audit says it serves "shippers, 3PLs, and carriers", but carrier-facing artefacts are a Carrier Payments product (TriumphPay partnership) and an invoice-inquiry portal — getting paid faster on invoices already rendered.
3. nVision Global and Intelligent Audit run loss & damage claims desks — filed *by the shipper against the carrier*. Same direction.

**Regulation reinforces the asymmetry: 49 CFR Part 378 is "Processing… of Overcharge, Duplicate Payment, or Overcollection Claims" — there is no mirrored federal undercharge-claims procedure.** 49 U.S.C. §14705 gives a carrier 18 months to sue for unpaid charges and a shipper 18 months for overcharges — **symmetric in law, wholly asymmetric in tooling.**

## Pricing anchors

| Model | Anchor | Label |
|---|---|---|
| Cass blended processing fee | $66.13M fees ÷ 50.96M invoices = **~$1.30/invoice**; transport-only ≈ $1.92 | VERIFIED (arithmetic on filed figures) |
| Cass float leg | Financial fees $40.4M on $36.4B (~11bps); avg payments in advance of funding $175.1M; avg accounts & drafts payable **$1.16B, non-interest-bearing** | VERIFIED |
| Cass stated model | "per-item basis… discounts received for services provided to carriers… and by the accounts and drafts payable balances… used to generate interest income" | VERIFIED (quote) |
| Gain-share range | "gain shares can range from **5% upwards of 50%**" | CLAIMED |
| Betachon | "Our **standard fee is 50% of the savings recovered**"; no monthly fee | CLAIMED (published) |
| Contingency norm | net savings to shipper "typically **50–75% of total recovery**" ⇒ **provider keeps 25–50%** | CLAIMED |
| AFS | ocean audit is **gainshare — "if we don't find billing errors, you don't pay"**; post-audit "recover up to 8% of transportation spend" | CLAIMED |
| SSI | "nominal contingency fee based on the recoverable refunds"; no long-term contract, no cancellation fee | CLAIMED |
| Intelligent Audit | "price per invoice" model | CLAIMED |
| **Loop** | SaaS platform fee + volume-based; **explicitly does NOT take a % of recovered savings** | CLAIMED |

Loop cites **4–12 weeks onboarding**. Enterprise FAP typically multi-year, per-transaction.

## Accessorial evidence standards

FAP validates accessorials as **costs against a contract**, not as claims requiring field evidence. Loop "digitizes contracts and rate tables… never approves an invoice with an incorrect rate, service, or accessorial charge", naming tolls, cleaning and **lumper fees**; documents consumed are "bills of lading, shipment packets, contracts, and rate sheets", plus "carrier contract, emailed BOL, loadboard documents, SMS receipt, in-app POD". nVision runs "200+ audit points" including accessorial verification and fuel surcharge accuracy.

**No FAP vendor examined publishes handling for TONU or layover, and none ingests ELD/GPS or appointment data.**

**The hard evidence standard lives in regulation, not vendor product** — see FMC 46 CFR Part 541 (agent 10). Generalising to truckload, the survivable packet is: **rate confirmation (rate + free-time terms) + BOL/POD arrival & departure timestamps + the free-time calculation shown + receipts for pass-throughs + issuance inside the deadline.**

Practitioner guidance mirrors it (Laneproof, vendor blog, CLAIMED): "a signed service log, GPS timestamps proving dock time… and your contract's accessorial rate schedule. **If the carrier didn't submit timestamps, that alone is your dispute.**"

## Published error/recovery statistics

| Stat | Value | Label |
|---|---|---|
| Invoices with errors (Loop) | "80%"… elsewhere "20%"… elsewhere "wrong up to 25% of the time" | CLAIMED — **internally inconsistent across Loop's own pages** |
| Invoices with errors (Trax) | "5–8%"; "3–6% with systematic audit" | CLAIMED |
| Freight spend lost | 10% (Loop); 1–5% recoverable (Trax) | CLAIMED |
| Recovery by mode | Parcel 2–5%; LTL 3–8%; **TL 1–3%**; blended 2–8% | CLAIMED |
| Savings delivered | Trax 5–7%; Loop 5–7% audit + 15–20% contract, 7–20x yr-1 ROI; AFS >3% parcel; nVision 5–15%, **"$25 per invoice" average savings** | CLAIMED |
| Concrete case | Great Dane: **$73K overcharges on $5.1M audited = 1.4%** | CLAIMED |
| Post-audit lookback | AFS ocean: recovery "up to 4 years after ship date" | CLAIMED |
| **Dispute win rates** | **No vendor publishes one** | **UNKNOWN** |

## Capability scores

| Capability | FAP category | Loop | Intelligent Audit |
|---|---|---|---|
| rate_confirmation_ingestion | 2 | 2 | 2 |
| rate_rule_extraction | 2 | 2 | 2 |
| gps_eld_timestamps | **0** | **0** | **0** |
| appointment_ingestion | **0** | **0** | **0** |
| pod_bol_ingestion | 2 | 2 | 1 |
| detention (as cost) | 1 | 1 | 1 |
| tonu | 0 | 0 | 0 |
| layover | 0 | 0 | 0 |
| lumper | 1 | 1 | 0 |
| demurrage | 2 | 1 | 1 |
| accessorial_detection (overcharge direction) | 2 | 2 | 2 |
| evidence_package | 1 | 1 | 1 |
| invoice_creation | **0** | **0** | **0** |
| claim_submission | 2 | 0 | 2 |
| collection_tracking | 1 | 0 | 1 |
| dispute_workflow | 2 | 1 | 2 |
| portal | 2 | 2 | 2 |
| tms_integration | 2 | 2 | 2 |
| eld_integration | **0** | **0** | **0** |
| email_sms_ingestion | 1 | 2 | 1 |
| accounting_integration | 2 | 2 | 1 |
| recovered_revenue_analytics (cost-side) | 2 | 2 | 2 |
| performance_pricing | 2 | **0** | 1 |
| customer_specific_rules | 2 | 2 | 2 |
| multi_carrier_shipper_support | 2 | 2 | 2 |

Every 0 on gps_eld/appointment/TONU/layover reflects **absence of published evidence**, not proof of absence.

## Partner vs competitor

**Partner case.** Direction of value is opposite: FAP defends the shipper's payables; carrier-side recovery builds the carrier's receivables. FAP already holds the exact reference data a carrier-side product needs — digitised contracts, accessorial rate schedules, free-time terms — and Cass/Trax/IA operate carrier-facing portals and payment rails (IA × TriumphPay). **A carrier-side packet arriving pre-validated against the shipper's own contract is *cheaper for the FAP to approve*, and FAP economics (per-item fees) reward touchless throughput, not disputes.**

**Competitor case.** Every dollar a carrier recovers is a dollar the FAP's client pays — the FAP scorecard is "5–7% spend reduction" and "99%+ overcharges caught". **Gain-share FAPs are structurally hostile: their fee is a share of what the carrier doesn't collect.** FAP owns the rate-engine layer; extending it to score under-billing is a feature, not a company. Brokers are the ambiguous middle: Loop already sells them AP automation and could add AR.

**Realistic read: channel partner for evidence exchange and settlement, competitor for the detection layer.** The defensible wedge is the one no FAP has: **ELD/GPS and appointment timestamps as first-class evidence, plus a packet built to the FMC's issuance-deadline-and-required-elements standard.**

## Honest gaps
- No FAP publishes list pricing. Every figure except the Cass arithmetic is CLAIMED, mostly from competitor/SEO pages.
- The "5–10% of invoices contain a discrepancy" figure attributed to an *American Shipper* 2024 FAP Benchmark Study appeared only in secondary summaries — primary not fetched, **not asserted**.
- Loop's own error-rate claims (20% vs 25% vs 80%) contradict each other; none is sourced.
- Trax, CTSI-Global, enVista pages 403'd/404'd; accessorial logic UNKNOWN.
- **No dispute win-rate data exists publicly anywhere in this category. That is a genuine measurement void and the single most valuable proprietary metric a carrier-side product could accumulate.**

## Sources
sec.gov/Archives/edgar/data/708781/000070878126000010/cass-20251231.htm · traxtech.com · afs.net/service/audit/ · /service/post-audit/ · intelligentaudit.com · loop.com · /3pl/accounts-payable-automation · /capabilities/freight-and-parcel-audit · /shippers · /article/freight-audit · /article/4-best-freight-audit-companies... · corporate.nvisionglobal.com/freight-audit/ · betachon.com/freight-audit-recovery-services/ · darrigoconsulting.com/blog/shipping-audit-freight-audit-guide · ssui.com/contingency-parcel-freight-invoice-audits/ · govregs.com/uscode/title49_subtitleIV_partB_chapter147_section14705 · federalregister.gov/documents/2024/05/14/2024-10515/... · hklaw.com/en/insights/publications/2024/02/fmc-announces-demurrage-and-detention-final-rule · laneproof.com/blog/billing-disputes-freight-documents-that-win
