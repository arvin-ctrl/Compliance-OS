# Agent 13 — Freight back-office AI (document/email automation)

**Research date:** 2026-08-19

## What each target actually extracts

| Company | Ingests | Accuracy claim | Extracts accessorial *rules*? |
|---|---|---|---|
| **Vooma** | Emails, PDFs, spreadsheets → TMS load build; quote requests; voice | "90%+ reduction in data errors," 15% email quote win-rate lift (CLAIMED) | **No** — no accessorial/detention language anywhere on site |
| **Drumkit** | Quote emails, portal tenders, confirmation emails, appointments | None published | **No** — own back-office blog omits invoicing, AR, accessorials, detention entirely |
| **HappyRobot** | Voice, email, portals, "document parsing" (undetailed) | "70%+ autonomous resolution," 75% cost reduction (CLAIMED) | UNKNOWN — lists Finance → *Collections and settlement* |
| **Expedock** | Forwarding docs: commercial invoices, packing lists, statements; Freya agent | **99.97%** "guaranteed" (CLAIMED) | **No** — forwarder doc set, not truckload rate cons |
| **Loop (loop.com)** | Carrier contracts, printed invoices, PDFs, TMS data, **BOLs**, emails, ERP, lumper/toll/cleaning receipts | "Automate 99% of freight and parcel audits"; Great Dane 98% no-touch (CLAIMED) | **Closest anyone gets** — digitises contracts + rate tables into a rate engine, runs an explicit "accessorial audit" |
| **Vector** | BOL, POD, lumper receipts via driver mobile capture; OCR extracts load #, origin, consignee, weight, invoice amount; **geofenced gate-in/dock/gate-out timestamps** | 30% labour lift, 30–67% detention fee reduction, 50%+ dwell cut (CLAIMED) | No rule extraction, but **owns the timestamp evidence layer** |
| **Pallet** | Order entry, quoting, portal updates, BOL attachments | "98% touchless processing on load building" (CLAIMED, one customer) | **No** |
| **Levity** | Emails + attachments; 100M+ emails processed | None; own site's QA log shows *ongoing* invoice/company-name parsing failures | **No**, but lists AR/AP as a use case |
| **Laneproof** — *new find, most on-thesis* | **Rate con, BOL, POD, lumper slips, carrier invoices**; validates linehaul, **detention hours**, lumper, fuel, accessorials | None published | **Partially** — claims to pull "rate, accessorial terms, and detention clauses from every rate con" |
| Cargado | Cross-border marketplace + rate data. 250+ brokers, 2,100+ carriers | — | No |
| Optimal Dynamics | Dispatch/network optimisation | — | No |
| Shipium | Parcel rating/labels; "Billing Management" undetailed | — | No |
| Trucker Tools | GPS/ELD telematics tracking, load board | — | No |
| ExFreight | Digital forwarder (quoting/booking) | — | No |
| Fleetworthy / Rippey AI / Superdispatch | Sites 403'd or returned empty shells | UNKNOWN | UNKNOWN |

**Could NOT be verified as freight companies and are NOT asserted:** Nomad/Augment (`augment.co` is an unrelated work-management tool), Sherpa, Ivy/Odin, Instalogix, Kargo (`kargo.com` is adtech; `kargo.io` is a Kubernetes tool). **These need a second pass with search access.**

## Who touches billing

Only four touch money, and none does what the thesis needs:
- **Loop** — deepest, but **inverted direction**. Shipper-side freight audit & pay: it *reduces* what shippers pay carriers, does GL coding, cost allocation, carrier payment, claims management. **It audits invoices; it does not create them.**
- **Vector** — **Rendition Billing**: "automate your entire payment process from delivery to collections." **The only verified doc→invoice→collections path in the set.** Its detention work is also shipper-side (30% detention fee *reduction*).
- **Laneproof** — explicitly **does not create invoices**; issues pay/dispute verdicts so brokers can push back on carriers. Defensive, not offensive.
- **Levity** — AR/AP listed as a use case; no detail.
- **Vooma, Drumkit, Pallet, HappyRobot, Cargado, Optimal Dynamics — no invoicing. Drumkit's own back-office thought-leadership piece omits billing, AR, audit, accessorials and detention entirely. This is the gap.**

## Pricing & funding

**Real disclosed pricing (rare):**
- **Laneproof** — $0 sandbox (20 docs/mo) · **$149/mo for 400 docs (~$0.37/doc)** · **$499/mo for 2,000 docs (~$0.25/doc)** · custom at 10,000+. A "document" = one uploaded file regardless of pages.
- **Pallet** — "pay for what the agents deliver, not seats or licenses" (outcome-based, no numbers)
- **Cargado** — subscription for brokers, free for carriers
- Vooma, Drumkit, HappyRobot, Loop, Expedock, Vector: **no public pricing** (`vooma.com/pricing` 404s)

**Funding (VERIFIED via official announcements):**

| Company | Raised |
|---|---|
| **HappyRobot** | $44M Series B (Sept 2025, Base10, ~$500M val) → **$150M Series C at $1.2B** (Prysm/Eurazeo); revenue up >5x since B, NDR >150% |
| **Loop** | **$95M Series C** (per own homepage) |
| **Pallet** | $27M Series B (May 2025, General Catalyst); **$50M total** |
| **Vooma** | **$16.6M** ($13M Series A Craft + $3.6M seed Index) |
| **Expedock** | $13.5M Series A (Insight, Aug 2022); **$17.5M total** — oldest money in the set |
| Drumkit | Not disclosed |
| Laneproof | Appears pre-seed/solo — a "$499 Founder-Assisted" tier is not a funded company's pricing page |

**Who can expand into recovery: HappyRobot ($1.2B, already sells "Collections and settlement") and Loop ($95M C, already owns rate-engine + audit + payment).** Pallet and Vooma have money but no billing surface. Expedock is capital-starved and has drifted toward managed BPO.

## Rate-con rule extraction: does anyone do it?

**Effectively no — this is genuinely open.**

- **Vooma, Drumkit, Pallet, HappyRobot** all extract *load/stop/rate/reference* fields to populate a TMS. **Zero evidence any parses the terms-and-conditions block where free time, detention $/hr, caps and notice requirements live.**
- **Loop** is the only company with a working *rules* engine — but its object is a **shipper–carrier contract**, not a per-load truckload rate confirmation, and its capability page does **not** document free time, per-hour detention, caps, or notice requirements as modelled entities. Direction is shipper-side savings.
- **Laneproof** is the only company *claiming* rate-con clause extraction, and its example is exactly the crux case: "Detention billed 3 hrs, POD shows 1.5 hrs." No accuracy numbers, no funding, tiny. **This is the closest competitor to the thesis and it is beatable.**
- Useful contrarian datapoint from the vendor literature: LLMs "lack the deterministic reliability required" for rule-governed extraction feeding billing — the argued fix is a multi-layer parser separating structured fields, conditional clauses, and free-text exceptions, normalising TONU/FSC/layover/detention triggers across inconsistent phrasing.

**Conclusion: rate-con *rule* extraction is unclaimed territory. Everyone is doing fields, not rules.**

## Handwritten BOL/POD accuracy reality — the load-bearing risk

**Honest answer: usable, not reliable.**

**Best available direct evidence** — *"From Handwriting to Structured Data: Benchmarking AI Digitisation of Handwritten Forms,"* arXiv 2604.16504 (Apr 2026), 17 frontier + open-source multimodal LLMs on handwritten forms:
- Overall **~85% accuracy**, weighted F1 ≈ **0.90**
- **Best hallucination rate 6%** — i.e. **one in ~16 fields is confidently invented**
- Best free-text error rates: **WER 0.50, CER 0.31** — half of handwritten free-text words wrong
- **Claude Sonnet 4.6 was best on formatted fields (dates and numerical values)** — the category in/out times fall into
- Prompt optimisation moved macro F1 by **>60%**, weighted metrics only 2–5% — gains are on rare/hard fields

**Supporting context:** purpose-built HTR on clean, line-segmented modern handwriting (IAM) reaches **1.2–2.3% CER**. LLMs on *degraded* historical handwriting land at **5.7–7% CER, 8.9–15.9% WER**. Azure Document Intelligence supports handwriting in only 12 languages, and v2.1 supported none — **handwriting is a recent, narrow capability, not a solved one.**

**Translation to a faxed BOL with handwritten in/out times: expect 80–92% field-level accuracy on the time fields under good conditions, degrading sharply with 200-dpi fax artefacts, stamp overlap, cramped boxes and skew.**

**The 6% hallucination rate is the real killer: for billing, a fabricated "0800" is far worse than a blank, because it enters a dispute you will lose.** `1` vs `7`, `3` vs `8`, and AM/PM omission are the classic failure modes, and **a single wrong character on a 4-character time destroys the entire detention calculation.**

**Design implication: never bill straight from handwriting.** Treat the handwritten time as one signal, cross-check against GPS/ELD geofence timestamps and facility check-in records, require dual-model agreement, and route disagreement to a human. **Confidence-gated human-in-the-loop is not a V1 shortcut — it is the permanent architecture.**

## Build-vs-buy for a solo founder

**Verdict: buy the stack, build the rules layer. Do not build custom OCR.**

- **Cost per document is a non-issue.** At ~1,500 input tokens/page + ~800 output tokens: **Haiku 4.5 ≈ $0.006/page; Sonnet 5 ≈ $0.017/page; Opus 5 ≈ $0.028/page.** Batch API halves it. Reducto is credit-based at $0.015/credit after 15,000 free. **Laneproof's shipping price is $0.25–0.37/doc — a 10–60x gross margin over raw model cost, which tells you the value is not in the parse.**
- **What works:** typed rate-con field extraction, clause location, normalisation of TONU/FSC/layover/detention phrasing. Frontier VLMs handle this well. Use structured outputs with `strict: true` schemas.
- **What breaks:** (1) handwriting, per above; (2) **hallucinated values on absent fields** — the model invents "2 hours free time" when the rate con is silent, **so make every rule field explicitly nullable and require a verbatim source quote per extracted rule**; (3) multi-page rate cons where terms live on page 3 in 6pt type; (4) **non-determinism across runs on the same document, which is fatal if the output feeds an invoice**; (5) tables and rate matrices — the IDP Leaderboard shows table extraction still misses ~10%.
- **Recommended V1:** Azure DI or Reducto for layout/text + a frontier VLM for rule extraction with citations enabled, dual-model agreement, confidence gating, human queue. **Ship the *rules ontology* (free time, $/hr, increment, cap, notice window, proof requirement, customer overrides) — that's the defensible asset, not the parser.**

## Capability scores

| Capability | Vooma | Drumkit | Expedock | Loop |
|---|---|---|---|---|
| rate_confirmation_ingestion | 2 | 2 | 1 | 1 |
| **rate_rule_extraction** | **0** | **0** | **0** | **2** |
| gps_eld_timestamps | 1 | 1 | 0 | 0 |
| appointment_ingestion | 2 | 2 | 0 | 0 |
| pod_bol_ingestion | 0 | 1 | 2 | 2 |
| detention | 0 | 0 | 0 | 1 |
| tonu | 0 | 0 | 0 | 0 |
| layover | 0 | 0 | 0 | 0 |
| lumper | 0 | 0 | 0 | 2 |
| demurrage | 0 | 0 | 0 | 1 |
| accessorial_detection | 0 | 0 | 0 | 2 |
| evidence_package | 0 | 0 | 0 | 2 |
| **invoice_creation** | **0** | **0** | **1** | **0** |
| claim_submission | 0 | 0 | 0 | 1 |
| collection_tracking | 0 | 0 | 0 | 0 |
| dispute_workflow | 0 | 0 | 0 | 2 |
| portal | 2 | 2 | 1 | 2 |
| tms_integration | 2 | 2 | 2 | 2 |
| eld_integration | 1 | 1 | 0 | 0 |
| email_sms_ingestion | 2 | 2 | 2 | 1 |
| accounting_integration | 0 | 0 | 1 | 2 |
| recovered_revenue_analytics | 0 | 0 | 0 | 2* |
| performance_pricing | **0** | **0** | **0** | **0** |
| customer_specific_rules | 1 | 1 | 1 | 2 |
| multi_carrier_shipper_support | 2 | 2 | 1 | 2 |
| **Total /50** | **15** | **16** | **12** | **29** |

\* Loop's analytics measure shipper *savings*, not carrier/broker *recovered revenue* — same math, opposite sign.

## Partner vs competitor

**Partners:**
- **Vector — the single best partner.** Owns geofenced gate-in/dock/gate-out timestamps, driver-side BOL/POD capture, and rendition billing rails. **Its timestamp layer is the exact ground truth that de-risks handwriting.**
- Trucker Tools / Optimal Dynamics / Cargado / Shipium / ExFreight — adjacent, no overlap.
- **Vooma, Drumkit, Pallet** — front-office ingestion partners today. They put the rate con in the TMS; you read the rules out of it. **They become competitors the moment any ships billing** — Pallet's "quote to cash" language plus Vooma's funding make that a 12–24 month risk.
- Expedock, Levity, Rippey — forwarder-lane. Partner or irrelevant.

**Competitors:**
- **Laneproof** — direct, same documents, same crux. But defensive rather than offensive, doesn't create invoices, no funding, publishes no accuracy numbers. **Beat it on the recovery direction and on evidence packaging.**
- **Loop** — most capable, the structural competitor. Has already solved contract→rate-engine→accessorial audit and is well capitalised. **It sells to shippers, which is the counterparty you'd be billing. Assume it eventually offers a carrier-side mirror.**
- **HappyRobot** — competitor by trajectory, not product. $1.2B valuation, >150% NDR, "Collections and settlement" already on the site. **If it turns its voice/email agents toward AR recovery calls, it arrives with distribution you cannot match.**

**The wedge that survives all of this: nobody extracts accessorial *rules* from a rate confirmation and turns them into a carrier-side recovery claim with an evidence package. Loop owns rules but faces the shipper. Vector owns evidence but doesn't read rules. Vooma/Drumkit/Pallet own the inbox but don't touch money.**

## Sources
vooma.com + /resources/new-funding-and-products-launch · finance.yahoo.com/news/vooma-grabs-16-6m-funding-172719936.html · drumkit.ai + /blog/the-impact-of-ai-in-freight-brokerage... · happyrobot.ai · siliconangle.com/2025/09/03/happyrobot-secures-44m... · aiweekly.co/alerts/happyrobot-lands-150m-series-c-at-12b-for-freight-ai-agents · loop.com + /capabilities/freight-and-parcel-audit + /solutions/freight · expedock.com · prnewswire.com/news-releases/expedock-raises-13-5m-series-a... · withvector.com + /connected-carrier/imaging-ocr/ + /solutions/dwell-detention-fees/ · pallet.com · businesswire.com/news/home/20250527164246/en/Pallet-Secures-$27M-Series-B... · levity.ai · laneproof.com + /pricing + /blog/rate-confirmation-what-brokers-get-wrong · cargado.com · optimaldynamics.com · shipium.com · truckertools.com · exfreight.com
**Handwriting evidence:** arxiv.org/abs/2604.16504 · arxiv.org/abs/2411.03340 · arxiv.org/abs/2412.18524 · idp-leaderboard.org · github.com/getomni-ai/benchmark · learn.microsoft.com/en-us/azure/ai-services/document-intelligence/language-support/ocr
**Cost inputs:** reducto.ai/pricing · Claude model pricing (Opus 5 $5/$25, Sonnet 5 $3/$15 with $2/$10 intro through 2026-08-31, Haiku 4.5 $1/$5 per MTok)
