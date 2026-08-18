# Company Report — Realtime Media (RTM)

Researcher: Research Agent 03 (Realtime Media / RTM)
Date: 2026-08-18
Category: Promotion administration
Manager: Manager A

## 1. Executive summary

**Actual core product:** Realtime Media (rtm.com, Norristown PA, ~51–57 employees, roots to 1994, 30+ years in promotions) is a **full-service promotion administration agency**, not a software company. Its core product is a bundled human-plus-technology service: strategy, in-house sweepstakes lawyers who draft official rules and manage state registration/bonding, microsite/game build (PromoPick™ template-plus platform), entry management and fraud mitigation on RTM-hosted properties, winner drawings and verification, prize sourcing/warehousing/fulfillment, winner tax paperwork (W-9/1099-MISC), and winner customer support [RTM-001, RTM-003, RTM-007, RTM-008, RTM-019, RTM-020].

**Who buys it:** Brand marketing teams and their agencies (white-label available) at consumer enterprises — DraftKings, Netflix, Disney, Subway, Hershey's, KFC, Royal Caribbean, GM/OnStar, Kohl's; RTM claims campaigns for 100+ Fortune 500 companies [RTM-002, RTM-022, RTM-025].

**Job it is hired to do:** "Run this promotion for us legally, securely, and completely, so marketing gets engagement without legal, fraud, or fulfillment risk." RTM absorbs the compliance and operations burden per campaign; it is the incumbent *service substitute* for promotion-compliance software. It also has a productized wedge: **PromoAdmin™** (standalone administration behind a client's own front end) and a **Promotions API** that powers registrations, time-seeded instant-win results, and loyalty gamification inside client apps (Sling TV) — but with no public developer documentation [RTM-009, RTM-010, RTM-012, RTM-023].

## 2. Product architecture

Concrete workflow (assembled from official pages; delivery mode noted per step):

**INPUT** → client campaign brief (prize pool, audience, channels, timing); participant entries (microsite form, social, SMS, in-app via API, receipt upload, mail-in AMOE); client behavioral events in API mode (e.g., Sling "30 minutes watched") [RTM-009, RTM-012, RTM-030].

**DECISION/PROCESS** →
1. *Pre-launch (human):* in-house counsel drafts full/abbreviated official rules (as fast as 5 business days), files state registrations and surety bonds where applicable (e.g., FL/NY >$5,000; RI >$500 retail), reviews marketing collateral for disclosure/advertising law; pre-launch risk assessment sets rules, entry limits, user flows, prize structures [RTM-003, RTM-004, RTM-016, RTM-018, RTM-019].
2. *Runtime (software, RTM-hosted):* entry validation and collection; three-layer fraud engine (bot/abuse heuristics + AI, behavior-based CAPTCHA-less validation, real-time monitoring and risk scoring); proprietary scoring marks users fraudulent and blocks them from winning; time-seeded instant-win draws executed at play time via API or microsite; receipt OCR + human review validates SKUs [RTM-009, RTM-014, RTM-015, RTM-017, RTM-028, RTM-037].
3. *Post-entry (human + tools):* random drawings conducted by RTM as impartial third-party administrator; winner outreach (email/social/phone/SMS); verification via PandaDoc/DocuSign declarations, eligibility/release forms and W-9 for prizes >$600; team review before winner confirmation [RTM-006, RTM-024].

**OUTPUT** → compliant live promotion; winner list; e-signed winner records; fulfilled prizes (200+ retailer gift cards, warehouse partners, discounted UPS/USPS); 1099-MISC filings; participant/entry data returned to client via secure encrypted file transfer; daily reporting for receipt programs [RTM-007, RTM-008, RTM-028, RTM-035].

The "platform" is operated *by RTM for the client*. There is no customer-operable console, policy engine, or self-serve tooling evidenced anywhere on the site [RTM-030, RTM-034].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Full-service promotion administration | End-to-end sweepstakes/contest/instant-win execution: strategy, legal, build, fraud, winners, fulfillment | Brand marketing | Core | RTM-001, RTM-002 |
| Legal administration | Rules drafting (5-day turnaround), state registration/bonding, AMOE + PO boxes, collateral review, regulated-industry and international coordination | Marketing (legal consulted) | Core differentiator | RTM-003, RTM-004, RTM-005, RTM-019 |
| PromoPick™ | Template-plus microsite/game platform: branded front ends, plug-and-play modules, 5–7 day launches | Marketing | Core tech vehicle | RTM-022, RTM-023 |
| PromoAdmin™ | Standalone administration behind the client's own front end: rules/compliance, winner selection & outreach, redemption, fulfillment | Marketing/agencies | Unbundled core | RTM-023, RTM-026 |
| API Promotions | Backend gamification API: registrations, time-seeded instant-win results, game logic, real-time behavior tracking, loyalty add-on | Marketing + client engineering | Add-on (growing) | RTM-009, RTM-011, RTM-012 |
| Fraud engine | 3-layer bot/behavior/risk-scoring stack on RTM-hosted properties | Bundled (not sold separately) | Embedded | RTM-014, RTM-015 |
| Receipt validation | AI OCR + expert review, SKU validation, receipt-fraud detection, daily reporting | Marketing (CPG) | Add-on | RTM-028 |
| Winner administration & prize fulfillment | Drawings, verification, DocuSign declarations, W-9/1099, sourcing, warehousing, shipping, redemption sites | Marketing | Core | RTM-006, RTM-007, RTM-008, RTM-027 |
| Loyalty & rewards | Buy/get, do/get, text-to-win; prepaid cards, gift-card network, merch fulfillment | Marketing/loyalty | Add-on | RTM-029 |
| Agency white-label | RTM as invisible back end for agencies | Agencies | Channel | RTM-025 |

## 4. API / developer capability

- **API:** A production Promotions API exists: "accept and validate sweepstakes registrations", "trigger time-seeded instant win play results", "power game logic across interactive formats", "track gameplay and behavior in real time"; loyalty add-on uses "real-time API calls to power reward logic, user progression, and engagement streaks" [RTM-009, RTM-011]. Proven at enterprise scale with Sling TV (watch-to-win, streaks, Winners Wall) [RTM-012].
- **Documentation:** **Not public.** "If you would like to see our API Documentation, please reach out to connect with a member of our strategy team" [RTM-010]. No developer portal or docs subdomain exists.
- **SDKs / webhooks / sandbox / versioning / idempotency / rate limits:** none documented anywhere public; all unresolved [RTM-010].
- **Latency claims:** none published; "real time" is marketing language only [RTM-037].
- **Integration model:** three tiers — (1) file exports, live in 2–4 weeks, no integration; (2) lightweight API integration keeping "backend logic and compliance services fully in play," full integrations 6–8 weeks; (3) fully integrated loyalty add-on [RTM-011]. RTM hosts the backend in all tiers; client owns the front end [RTM-009].
- **Rules engine:** campaign game logic (odds, winning moments, entry limits) is configured by RTM per campaign, not exposed to customers as an authorable rules engine [RTM-017, RTM-034].
- **Data hand-off:** secure encrypted file transfer of participant/entry data; daily reporting cited only for receipt programs [RTM-028, RTM-035].

**Assessment (inference):** this is an integration surface for embedding RTM-run promotions into client apps — not a developer platform. The 6–8 week, sales-mediated, undocumented-in-public model is the opposite of self-serve policy/decisioning infrastructure.

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Partially. It ingests client-defined behavioral events (watch time, purchases via receipts, in-app actions) to drive entries/plays [RTM-012, RTM-028]. No evidence of a general attribute-evaluation language; campaign logic is bespoke per engagement (inference).
- **Store customer/user state?** Yes, within campaigns: entries, plays, streaks, progression, fraud scores [RTM-009, RTM-012, RTM-015].
- **Return reason codes?** No evidence. Fraud scoring is deliberately "discreet" (opaque) [RTM-015].
- **Output allow/deny/review?** Only as promotion mechanics: entry accepted/blocked (fraud), win/lose (instant win), winner "pending verification" → confirmed/disqualified — a human review state, not an API output contract [RTM-014, RTM-024]. Inference: no authorization-style decision API.
- **Simulate policies?** No evidence. Pre-launch risk assessment is a manual consulting exercise [RTM-016].
- **Replay decisions?** No evidence.
- **Version policies?** No evidence of versioned policy artifacts; official rules are dated legal documents per promotion (inference).
- **Deploy rules independently of app code?** In the service sense only: RTM changes campaign configuration on its own hosted backend; clients cannot self-deploy rules [RTM-034].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance:** deep and real, delivered by humans — rules drafting, registration/bonding, AMOE, collateral review, winner paperwork, 1099s [RTM-003, RTM-007].
- **Generic regulatory workflow:** none. Everything is promotion-scoped [RTM-034] (inference).
- **Jurisdiction restrictions:** 50-state knowledge demonstrated (FL/NY >$5,000 registration+bond with 7/30-day lead times; RI >$500 retail; 13 states with special restrictions), plus regulated verticals (alcohol, pharma, financial services) and international via outside counsel network [RTM-003, RTM-018]. Encoded in people and documents, not software.
- **Location verification:** IP tracking only; no GPS/Wi-Fi geolocation or VPN-detection product evidenced [RTM-033].
- **Legal content/rules:** official rules and disclosures as bespoke legal documents; speed (5 days) implies internal template libraries (inference) [RTM-004].
- **Regulatory monitoring:** maintained educational content on state law; no monitoring product or alerting [RTM-018].
- **Change management:** dedicated project managers per campaign; manual [RTM-033].
- **Counsel approval:** structurally present — in-house sweepstakes lawyers on every project review rules and collateral before launch; no software approval workflow [RTM-019].
- **Historical policy state:** no evidence of queryable historical rule/policy state; past promotions' rules exist as archived documents (inference).

## 7. Audit / evidence

Can a customer reconstruct…
- **Exact inputs?** Partially: participant/entry data is delivered via secure file transfer; receipt images/SKU validations exist during campaigns [RTM-028, RTM-035]. No queryable log product.
- **Exact rule/policy?** The official rules document per promotion, yes (legal document). Runtime game/fraud configuration: no evidence.
- **Exact version?** No evidence of version linkage between a given entry/win decision and a configuration version.
- **Exact output?** Winner lists, win/lose results, and fulfillment records exist operationally [RTM-006, RTM-007]; drawing methodology and records format are not publicly documented [RTM-006].
- **Exact timestamp?** Plausible (entries are time-stamped for time-seeded wins — inference); not documented.
- **Human approvals?** Winner-side yes: PandaDoc/DocuSign e-signed declarations and release forms are durable human-verification records [RTM-024]. Counsel-side approvals are internal with no exposed history.
- **Source/legal authority?** No evidence rules link to statutory sources for clients.

SOC 2 Type 2 ("process integrity") plus registration/bond filings and 1099 filings mean RTM *produces* compliance artifacts as a byproduct of service [RTM-013, RTM-003]; it does not sell an evidence or audit product. Retention controls unverifiable — privacy policy PDF was down (HTTP 503 twice) [RTM-038].

## 8. Enterprise readiness

- **SSO/RBAC:** no customer-facing evidence (there is no customer console to govern) [RTM-034]. Internal access controls audited annually under SOC 2 Type 2 [RTM-013].
- **Multitenancy/multi-brand:** service-bureau style — RTM runs thousands of promotions across brands and white-labels for agencies [RTM-020, RTM-025].
- **Environments:** "meticulous QA" cited for agency work; no staging/sandbox evidence [RTM-025].
- **Security certifications:** SOC 2 Type 2 attestation; encryption in transit/at rest; GDPR/CCPA alignment; ISO 27001 badge (likely the hosting environment — inference) [RTM-013, RTM-036].
- **SLA:** none published; winner-support response target 2–3 business days [RTM-024].
- **Support/professional services:** the offering *is* professional services: dedicated PMs, in-house lawyers, fulfillment managers, US-based team, multi-lingual winner support [RTM-019, RTM-025].
- **Customer scale:** Fortune 500 roster (Netflix, NFL, Walmart, Comcast, NBCUniversal claimed; DraftKings, Disney, Subway, Hershey's, GM evidenced via site/case studies) [RTM-002, RTM-022, RTM-027].

## 9. Commercial model

- **Pricing:** not public; custom quotes; explicitly unbundlable ("full-service support or just specific services") [RTM-026]. Positions on "superior value pricing" vs competitors [RTM-031-adjacent claims].
- **Likely buyer:** brand marketing / promotions managers; agencies as channel; legal teams consulted, engineering involved only in API mode [RTM-003, RTM-011, RTM-025].
- **Implementation burden:** near-zero for RTM-hosted microsites (3-week instant-win launches, 5–7 day PromoPick quick-turns); 2–4 weeks file-based; 6–8 weeks full API [RTM-011, RTM-017, RTM-022].
- **Sales motion:** contact/quote-driven, relationship-based, per-campaign or program engagements; no self-serve signup exists [RTM-026, RTM-034].
- **Large-customer evidence:** DraftKings redemption program reused across promotions; Sling loyalty integration; 100+ Fortune 500 claim [RTM-012, RTM-022, RTM-027].

## 10. Strengths

1. **Complete promotion-compliance operations under one roof** — lawyers, bonding/registration, AMOE PO boxes, drawings, DocuSign winner verification, 1099s, warehousing — genuinely end-to-end [RTM-003, RTM-007, RTM-008].
2. **In-house sweepstakes counsel on every project** with regulated-industry (alcohol/pharma/financial) and international reach — the counsel-in-the-loop model as a service [RTM-003, RTM-019].
3. **Speed**: rules in 5 days, quick-turn campaigns in 5–7 days, instant win in ~3 weeks [RTM-004, RTM-017, RTM-022].
4. **Embedded, battle-tested fraud engine** with real-time risk scoring on every hosted promotion [RTM-014, RTM-015].
5. **Enterprise trust surface**: SOC 2 Type 2, GDPR/CCPA, Fortune 500 roster, 30 years of precedent including GE's first online instant win [RTM-013, RTM-020, RTM-022].
6. **A real production API** for embedded gamification proven inside a major streaming service's loyalty program [RTM-009, RTM-012].

## 11. Weaknesses / constraints

Evidence-backed or labeled inference:

1. **No customer-operable software layer**: no console, no rules authoring, no dashboards described anywhere — even the "platform" page describes services [RTM-030, RTM-034].
2. **Closed developer surface**: API docs by sales request only; no SDKs, sandbox, versioning, webhooks, or rate limits documented publicly [RTM-010].
3. **Human-scaled**: ~51–57 employees executing bespoke engagements; capacity and margins scale with headcount, not software (inference from RTM-021, RTM-001).
4. **Compliance knowledge is not productized**: 50-state expertise lives in people and blog content, not in versioned, machine-readable policy [RTM-018, RTM-034] (inference).
5. **Opaque decisioning**: fraud scoring is intentionally "discreet"; no reason codes, no explainability, no decision replay [RTM-015] (absence inference).
6. **No published SLAs, no pricing transparency, no self-serve** [RTM-024, RTM-026].
7. **Fraud engine scope**: deployed "on all microsites built and managed by Realtime Media" — protection is tied to RTM-hosted properties [RTM-015].
8. **Category is crowded with service peers** (Merkle/HelloWorld, PrizeLogic, Marden-Kane, Ventura, National Sweepstakes, Promosis) limiting pricing power [RTM-032].

## 12. Capability matrix scores

Scoring convention: scores reflect the capability as delivered (service or software); notes flag delivery mode because it matters downstream. `?` = unresolved (no public evidence either way); 0 scores are reasoned, per notes.

```csv
square,score,claim_ids
A01,4,RTM-001;RTM-002;RTM-023
A02,4,RTM-002;RTM-006
A03,4,RTM-017;RTM-012;RTM-020
A04,4,RTM-003;RTM-004;RTM-019
A05,4,RTM-003;RTM-019;RTM-033
A06,3,RTM-005;RTM-030
A07,4,RTM-002;RTM-028;RTM-030;RTM-035
A08,4,RTM-006;RTM-007
A09,4,RTM-008;RTM-027;RTM-029
A10,3,RTM-007;RTM-024
B01,2,RTM-009;RTM-011
B02,2,RTM-037;RTM-017
B03,?,
B04,1,RTM-009;RTM-024
B05,?,
B06,2,RTM-012;RTM-028
B07,2,RTM-009;RTM-012
B08,?,
B09,?,
B10,?,
C01,2,RTM-003;RTM-018
C02,2,RTM-003
C03,1,RTM-003;RTM-018
C04,1,RTM-018
C05,?,
C06,1,RTM-018
C07,1,RTM-016
C08,2,RTM-019;RTM-003
C09,?,
C10,0,RTM-034
D01,?,
D02,1,RTM-035;RTM-015
D03,?,
D04,?,
D05,1,RTM-024
D06,?,
D07,1,RTM-003;RTM-018
D08,?,RTM-038
D09,?,
D10,?,
E01,2,RTM-033;RTM-024
E02,1,RTM-024
E03,1,RTM-024;RTM-027
E04,1,RTM-033
E05,2,RTM-014;RTM-015
E06,?,
E07,3,RTM-014;RTM-015
E08,2,RTM-014;RTM-015
E09,1,RTM-024;RTM-006
E10,?,
F01,1,RTM-011
F02,1,RTM-009
F03,2,RTM-007;RTM-027
F04,1,RTM-012;RTM-027
F05,1,RTM-027
F06,?,
F07,2,RTM-027;RTM-024
F08,?,
F09,2,RTM-008;RTM-029
F10,2,RTM-011;RTM-012
G01,2,RTM-025;RTM-020
G02,?,
G03,?,
G04,1,RTM-003;RTM-033
G05,1,RTM-025
G06,?,
G07,1,RTM-033;RTM-031
G08,?,
G09,?,
G10,3,RTM-013;RTM-022;RTM-036
H01,2,RTM-009;RTM-010;RTM-011
H02,?,
H03,?,
H04,?,
H05,?,
H06,?,
H07,0,RTM-010
H08,?,
H09,?,RTM-011
H10,0,RTM-034;RTM-011
I01,2,RTM-003;RTM-004
I02,1,RTM-011
I03,4,RTM-001;RTM-025;RTM-031
I04,1,RTM-014
I05,4,RTM-002;RTM-022;RTM-027
I06,0,RTM-026;RTM-034
I07,4,RTM-001;RTM-019;RTM-031
I08,1,RTM-011;RTM-026
I09,2,RTM-011;RTM-030
I10,1,RTM-026;RTM-033
J01,1,RTM-003;RTM-016
J02,1,RTM-004;RTM-019
J03,2,RTM-019;RTM-003
J04,1,RTM-016
J05,0,RTM-009;RTM-034
J06,?,
J07,1,RTM-024;RTM-003
J08,?,
J09,1,RTM-004;RTM-033
J10,0,RTM-034;RTM-003
```

**Scoring notes (0s, 1s, and judgment calls):**

- **A-row 4s:** promotion administration is RTM's core, category-defining business, evidenced by official service pages, operational FAQs (winner-facing documentation), case studies, and a 30-year Fortune-500 track record. A06=3 (AMOE+PO boxes explicit but thinly documented); A10=3 (W-9/1099-MISC filing explicit; process detail thin).
- **B-row:** the API is real but promotion-scoped. B02 synchronous evaluation and B04 accept/block/pending outcomes are **inference** from API descriptions and winner workflow — they are promotion mechanics, not an authorization output model. B03/B05/B08–B10: no public architecture, latency, reason-code, priority, simulation, or replay evidence → `?`.
- **C-row:** jurisdiction competence is strong **as a human service** (C01/C02=2 capped because nothing is productized or machine-readable). C04=1: registration lead-time calendars (FL 7d / NY 30d) are managed manually. C06=1: monitoring exists as staff expertise + educational content. C07=1: pre-launch risk assessment is manual and fraud/structure-oriented. C08=2: real counsel-in-the-loop on every project, but no software workflow. **C10=0 (reasoned inference):** RTM's deliverable is human-drafted legal documents; across ~60 non-blog pages and all searches there is no policy engine, library, or machine-readable artifact, and the services-first architecture precludes one today [RTM-034].
- **D-row:** operational records exist (entry files, e-signed declarations, filings) but nothing is offered as an audit/evidence product; most squares `?`. D08 `?` because the privacy policy was unreachable (RTM-038).
- **E-row:** fraud is the strongest signal capability (E07=3, official FAQ + product page). Identity (E01=2) is fraud-tool naming plus document-based winner verification, not doc-scan IDV. E04=1: IP tracking only. E06/E10 `?`.
- **F-row:** prizes and rewards have real provenance/redemption controls (F03/F07=2) but there is no ledger product; loyalty balances live in client systems (F01=1, inference from the Sling model).
- **G-row:** G10=3 (SOC 2 Type 2 + ISO 27001 claims + GDPR/CCPA). Governance software squares (G02/G03/G06/G08/G09) `?` — there is no customer console to govern, but absence of mention is not proof for adjacent internal tooling.
- **H-row:** H01=2 (production API, gated docs). **H07=0 (reasoned inference):** publicly documented rate limits cannot exist because no public API documentation exists at all — docs are provided only via sales contact [RTM-010]. **H10=0 (reasoned inference):** RTM hosts everything; its integration models are exhaustively enumerated (file/API/loyalty) and there is no customer-deployable infrastructure for IaC to manage [RTM-011, RTM-034]. H09 `?`: entry-data file exports exist but a policy/config export concept does not apply publicly.
- **I-row:** **I06=0 (reasoned):** every path to purchase is quote/contact-mediated; campaigns are "built-for-you"; no signup or product login exists [RTM-026, RTM-034]. I07=4 is descriptive: the offering is professional services. I08=1: engagement is per-campaign and administrators are switchable; API/loyalty integrations (6–8 weeks) add moderate stickiness for that minority segment. I09=2 recorded as low-to-moderate burden (RTM-hosted = near zero; API = 6–8 weeks).
- **J-row:** J03=2 because counsel-as-approver genuinely exists — as headcount, not workflow software. J01/J02/J04/J07/J09=1: partial, manual, campaign-scoped analogues. **J05=0 and J10=0 (reasoned inference):** the architecture is promotion-campaign-scoped with no authorization semantics and no policy artifacts to lifecycle-manage; nothing in any material suggests cross-product regulated-action authorization or a policy control plane [RTM-009, RTM-034]. J06/J08 `?`.

## 13. White-space implications

1. **Already solved (by RTM, as a service):** the entire promotion-administration layer — official rules, state registration/bonding calendars, AMOE, counsel review of campaigns and collateral, certified-style third-party drawings, winner verification with e-signed evidence, tax filings, fulfillment (A01–A10 ≈ 3–4). Also solved: promotion-scoped fraud screening with real-time risk scoring (E07) and embedded gamification via API (B01 partial). For the *promotions* domain, "counsel as approver" (J03) and "legal-to-production" (J02) already happen — as people and process, at 5-day turnaround.
2. **Partially solved:** jurisdiction intelligence (C01/C02 — expert humans + content, zero productization); pre-launch impact assessment (C07 — manual, fraud-oriented); decision evidence (D02/D05 — files and DocuSign records, no reconstruction product); stateful real-time mechanics (B02/B07 — campaign-scoped); loyalty/ledger touchpoints (F10 — client keeps the ledger).
3. **Unsolved (no evidence at all):** machine-readable/versioned policy (C05/C10), reason codes and decision replay (B05/B10), policy simulation (B09), evidence-grade reconstruction and regulator export (D06/D07 as products), historical "why was this allowed?" (J08), cross-product action authorization (J05), signal normalization across vendors (J06), any policy lifecycle control plane (J10), and the entire self-serve developer platform (H02–H10).
4. **Could RTM add the missing capability easily?** No. A ~55-person services firm with a closed API, no developer platform, and revenue tied to bundled execution would need a different company shape (product engineering, docs, SLAs, self-serve) to build policy-as-code infrastructure. It could plausibly add point features (a client dashboard, published API docs, a rules-status portal) but not an enterprise control plane (inference from RTM-010, RTM-021, RTM-034).
5. **Could a customer assemble it using RTM + internal engineering?** Partially, and this is the realistic incumbent pattern: RTM (or a peer) as the compliance/administration service + internal engineering for in-app logic + the client's own fraud/identity vendors. Sling demonstrates exactly this assembly [RTM-012]. What the assembly does *not* yield: versioned executable policy, decision logs with reasons, replay, counsel approval workflow in software, or reusable jurisdiction packs — the client gets compliant *campaigns*, not compliance *infrastructure*.
6. **What would make a customer buy a separate product instead?** (a) Promotion/incentive decisions happening inside their own products at API scale and frequency where per-campaign service engagement breaks down; (b) needing auditable "why was this allowed?" evidence across many jurisdictions and product surfaces (sweepstakes + gambling-adjacent + fintech incentives), which a service's file exports and PDFs cannot answer; (c) wanting counsel approval, versioning, and rollout impact analysis as governed software workflow rather than emails to an agency; (d) multi-vendor signal normalization that an agency's proprietary, hosted-only fraud engine cannot provide. Conversely — and this argues *against* the hypothesis — for the classic promotions use case RTM's bundle (legal + bond + PO box + drawings + 1099 + warehouse) includes physical-world obligations no software product can fully absorb, which suppresses demand for software-only alternatives among mainstream brands.

## 14. Replacement risk

**LOW.**

RTM is unlikely to enter a regulatory policy-infrastructure space: it is a small (~51–57 person), owner-operated services firm whose economics, go-to-market (quote-driven campaigns), and technology posture (closed API, no docs, no self-serve, no customer console) all point away from enterprise software [RTM-010, RTM-021, RTM-026, RTM-034]. Its productization trajectory (PromoPick templates 2015→2020, API promotions, PromoAdmin unbundling) is about delivering *its own service* more efficiently, not about shipping customer-operated policy tooling [RTM-022, RTM-023].

The real competitive effect is different: RTM (and peers) are **entrenched substitutes on the promotions wedge** — they absorb exactly the pain (rules, jurisdictions, counsel, evidence paperwork) that a Promotion OS would monetize, at per-campaign prices, with humans who accept liability-adjacent work software cannot. A Promotion OS selling into brands will constantly hear "our administrator already handles that." Risk of RTM *building* the product: LOW. Risk of RTM *suppressing demand* for it in mainstream promotions: HIGH (inference).

## 15. Adjacent discoveries

Companies/substitutes that should be considered (beyond the assigned 15):

1. **Merkle (HelloWorld, formerly ePrize)** — the enterprise-scale promotions technology + administration arm inside a dentsu agency; the strongest "big brand promotions platform + services" comparable; if any promotions vendor could productize compliance at scale, it is this one [RTM-032].
2. **PrizeLogic** — enterprise promotion/loyalty/rebate execution for major CPG/retail brands; overlaps RTM on administration plus deeper rebate/receipt programs [RTM-032].
3. **Marden-Kane** — administrator since 1957; evidence that this category sustains decades-old, small, human-scaled firms rather than consolidating into software [RTM-032].
4. **National Sweepstakes Company / Promosis / Ventura Associates / Don Jagoda** — the long tail of administration/judging agencies; collectively they are the substitute layer for legal administration and drawings [RTM-032].
5. **Promotion-law boutiques as the counsel substitute** — e.g., Klein Moynihan Turco and similar firms publish state registration/bonding guidance and serve as outside counsel; for the J02/J03 hypothesis, licensed counsel + an administrator is the incumbent "workflow" (observed during research on state-law sources).

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/03_rtm.jsonl` (38 records). Same records:

| Claim ID | Claim (abbreviated) | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| RTM-001 | Full-service digital promotions & sweepstakes administration company (strategy → legal → build → winners → fulfillment) | https://www.rtm.com/ | official-marketing | 2026-08-18 | HIGH |
| RTM-002 | Builds sweepstakes, contests, instant win, UGC, loyalty; clients incl. DraftKings, Netflix, Disney, Subway, Hershey's, KFC, Royal Caribbean, OnStar | https://www.rtm.com/ | official-marketing | 2026-08-18 | HIGH |
| RTM-003 | Legal admin: rules drafting, surety bonds & state registration, winner declarations/releases/tax forms, collateral review, AMOE+PO boxes, regulated industries, international counsel | https://www.rtm.com/sweepstakes-legal-administration | official-marketing | 2026-08-18 | HIGH |
| RTM-004 | Rules drafted with go-to-market in as few as 5 business days; in-house legal experts | https://www.rtm.com/lp/promotion-law/legal-administration | official-marketing | 2026-08-18 | MEDIUM |
| RTM-005 | Manages alternate (free) means of entry and PO box services | https://www.rtm.com/sweepstakes-legal-administration | official-marketing | 2026-08-18 | HIGH |
| RTM-006 | Random drawings as impartial third-party administrator; judging/voting; moderation; anti-fraud verification in drawings | https://www.rtm.com/faq/winner-selection | official-doc | 2026-08-18 | HIGH |
| RTM-007 | Winner admin: declarations, eligibility/release forms, W9 & 1099-MISC filing, bonding/registration, multi-channel outreach, in-house prize redemption tool | https://www.rtm.com/winner-administration | official-marketing | 2026-08-18 | HIGH |
| RTM-008 | Fulfillment: in-house sourcing, warehouse partners, 200+ retailer gift cards, discounted UPS/USPS; vehicles, trips, cash | https://www.rtm.com/prize-fulfillment | official-marketing | 2026-08-18 | HIGH |
| RTM-009 | Promotions API: validates registrations, triggers time-seeded instant win results, powers game logic, tracks behavior in real time; client owns front end | https://www.rtm.com/api-promotions | official-marketing | 2026-08-18 | HIGH |
| RTM-010 | API documentation only via sales contact; no public developer portal/SDKs/sandbox/rate limits | https://www.rtm.com/api-promotions | official-marketing | 2026-08-18 | HIGH |
| RTM-011 | Integration tiers: file exports 2–4 wks; API integration 6–8 wks with RTM compliance services in play; real-time loyalty add-on | https://www.rtm.com/api-promotions | official-marketing | 2026-08-18 | HIGH |
| RTM-012 | Sling Rewards: entries/plays per 30 min watched, streaks, live Winners Wall, up to $25,000 cash — via RTM API | https://www.rtm.com/api-promotions | case-study | 2026-08-18 | HIGH |
| RTM-013 | SOC 2 Type 2 attestation; encryption in transit/at rest; annual access-control audits; GDPR/CCPA alignment | https://www.rtm.com/sweepstakes-legal-administration/data-security | official-marketing | 2026-08-18 | HIGH |
| RTM-014 | 3-layer fraud framework: AI bot mitigation, CAPTCHA-less behavioral validation, live monitoring & risk scoring | https://www.rtm.com/fraud-prevention | official-marketing | 2026-08-18 | HIGH |
| RTM-015 | Proprietary scoring system marks users fraudulent, blocks winning; deployed on all RTM-managed microsites | https://www.rtm.com/faq/fraud-mitigation | official-doc | 2026-08-18 | HIGH |
| RTM-016 | Every promotion includes pre-launch risk assessment informing rules, limits, user flows, prize structures | https://www.rtm.com/fraud-prevention | official-marketing | 2026-08-18 | HIGH |
| RTM-017 | Instant win: predetermined winning moments/odds-based, time-seeded; 4 formats; embeddable in site/app/CRM; ~3-week launch | https://www.rtm.com/sweepstakes-and-more/instant-win-games | official-marketing | 2026-08-18 | HIGH |
| RTM-018 | 50-state law guidance: FL/NY >$5,000 registration+bond (7/30-day lead), RI >$500 retail; 13 special states; legal team assists | https://www.rtm.com/blog/contests-and-sweepstakes-laws-by-state | official-marketing | 2026-08-18 | MEDIUM |
| RTM-019 | "Every project is supported by in-house sweepstakes lawyers, project managers, and fulfillment managers" | https://www.rtm.com/lp/sweepstakes/sweepstakes-administration | official-marketing | 2026-08-18 | HIGH |
| RTM-020 | 30+ years; powered GE's first online instant win; Norristown PA; CEO Robert Bernstock; co-owners Bernstock & Tierney Sr. | https://www.rtm.com/our-company | official-marketing | 2026-08-18 | HIGH |
| RTM-021 | ~51–57 employees; opened 1994 in Philadelphia | https://www.zoominfo.com/pic/realtime-media-inc/32292996 | third-party | 2026-08-18 | MEDIUM |
| RTM-022 | PromoPick (2020 PR): 5–7 day launches; ISO27001/GDPR/CCPA claims; template-plus; 100+ Fortune 500 clients incl. NFL, Walmart, Comcast | https://www.prnewswire.com/news-releases/realtime-media-releases-latest-version-of-promopick-the-market-leading-solution-for-digital-promotions-301066057.html | official-marketing | 2026-08-18 | MEDIUM |
| RTM-023 | PromoAdmin™ standalone admin support (rules/compliance, winner selection & outreach, redemption, fulfillment); PromoPick™ entry-collection tech | https://www.rtm.com/ | official-marketing | 2026-08-18 | HIGH |
| RTM-024 | Winner verification: PandaDoc/DocuSign declarations; >$600 → eligibility/release + W9; team review; 1099 in January; 2–3 day support target | https://www.rtm.com/winner-faq | official-doc | 2026-08-18 | HIGH |
| RTM-025 | Agency white-label; end-to-end for agencies; secure tech, meticulous QA, fraud engine; US-based in-house team | https://www.rtm.com/for-agencies | official-marketing | 2026-08-18 | HIGH |
| RTM-026 | No published pricing; custom quotes; services can be unbundled | https://www.rtm.com/faq/sweepstakes-contest-pricing | official-doc | 2026-08-18 | HIGH |
| RTM-027 | DraftKings: custom Winner Redemption Site; unique single-use codes; fraud minimized; quick-turn reuse across promotions | https://www.rtm.com/case-studies/draftkings-prize-redemption-and-fulfillment | case-study | 2026-08-18 | HIGH |
| RTM-028 | Receipt validation: AI OCR + expert oversight; SKU validation; receipt-fraud detection; daily reporting | https://www.rtm.com/loyalty-rewards/receipt-validation | official-marketing | 2026-08-18 | HIGH |
| RTM-029 | Loyalty mechanics: buy/get, do/get; rewards via coupons, prepaid Visa/MC, retailer gift cards, merch; end-to-end fulfillment | https://www.rtm.com/loyalty-rewards | official-marketing | 2026-08-18 | HIGH |
| RTM-030 | Entry channels incl. microsites, social, in-store, SMS, trade shows, in-app, mail-in/AMOE; "platform" page describes no dashboards/APIs/analytics | https://www.rtm.com/lp/sweepstakes/sweepstakes-platform | official-marketing | 2026-08-18 | MEDIUM |
| RTM-031 | 31 FeaturedCustomers reviews; praise for experienced responsive team and full-service ease (Hershey's, Royal Caribbean, etc.) | https://www.featuredcustomers.com/vendor/realtime-media | third-party | 2026-08-18 | MEDIUM |
| RTM-032 | Peer administrators: Marden-Kane (1957–), Merkle/HelloWorld (ex-ePrize), PrizeLogic, Ventura, Don Jagoda, National Sweepstakes Co., Promosis | https://www.mardenkane.com/ | third-party | 2026-08-18 | MEDIUM |
| RTM-033 | Quick-turn: 3-layer fraud w/ IP tracking, bot detection, identity verification, SOC 2-level security; rules+legal+collateral review included | https://www.rtm.com/quick-turn-sweepstakes | official-marketing | 2026-08-18 | HIGH |
| RTM-034 | Services-first model site-wide; no customer-operable policy software, console, or self-serve; API docs gated (reasoned absence, inference) | https://www.rtm.com/lp/sweepstakes/sweepstakes-platform | official-marketing | 2026-08-18 | MEDIUM |
| RTM-035 | Web-based tools for secure encrypted file transfer of participant and entry data | https://www.rtm.com/sweepstakes-legal-administration | official-marketing | 2026-08-18 | HIGH |
| RTM-036 | ISO 27001 badge in site footer; ISO 27001-compliant hosting environment claim | https://www.rtm.com/sweepstakes-and-more | official-marketing | 2026-08-18 | MEDIUM |
| RTM-037 | Synchronous evaluation of instant-win/loyalty logic at API call time (inference; no latency/SLO documentation) | https://www.rtm.com/api-promotions | official-marketing | 2026-08-18 | MEDIUM |
| RTM-038 | Privacy policy PDF unreachable (HTTP 503 twice on 2026-08-18); retention practices unverified | https://privacy.rtm.com/privacypolicy.pdf | official-doc | 2026-08-18 | LOW |

## 17. Verdict

**SUBSTITUTE**

RTM does not build any of the proposed Promotion OS software: no executable policy, no authorization API, no decision logs/replay, no counsel workflow tooling, no developer platform (J-row: 0–2; H-row mostly ?/0). It cannot plausibly pivot to become one (LOW replacement risk: ~55 people, quote-driven services, closed API). But it is a direct substitute for the *outcome* the hypothesis sells in the promotions domain: for a per-campaign fee, enterprises get jurisdiction-aware rules, counsel-in-the-loop approval, registration/bonding, AMOE, fraud screening, evidence paperwork (DocuSign declarations, 1099s), and fulfillment — physical-world obligations software alone cannot absorb. Any Promotion OS pitch to brands running sweepstakes will compete with "our administrator already handles that," from RTM and a deep bench of peers (Merkle/HelloWorld, PrizeLogic, Marden-Kane). The hypothesis survives against RTM only where decisioning is continuous, in-product, cross-jurisdictional, and evidence-hungry — beyond campaign administration.

