# Company Report — Votigo

Researcher: Research Agent 01 (Votigo)
Date: 2026-08-18
Category: Promotion administration
Manager: Manager A

Core question assigned: **How far beyond campaign administration does its API/compliance layer extend?**

Short answer, evidenced below: **Not far.** The API is a gated, campaign-scoped integration surface (campaigns/entries/analytics, Enterprise add-on, no public reference docs), and the compliance layer is a managed human service (rules drafting, registration/bonding, winner administration) rather than software infrastructure. Nothing in Votigo's stack functions as a reusable policy engine, decision authorization API, or evidence/replay system outside the promotions it hosts and administers.

## 1. Executive summary

**Actual core product.** Votigo (founded 2006, Boulder CO; ~22–27 employees, ~$2.8M est. 2024 revenue per third-party data [VOTIGO-026, VOTIGO-027]) is a hybrid: (a) a self-serve/managed SaaS promotions platform — sweepstakes, UGC contests, instant win, receipt validation, coupons/rebates, SMS text-to-win, loyalty — delivered as hosted microsites and embeds; and (b) a full-service promotion administration business (official rules drafting, state registration and bonding, drawings, winner verification, 1099 tax workflows, prize fulfillment), substantially built via its 2020 acquisition of US Sweepstakes & Fulfillment Co. [VOTIGO-001, VOTIGO-025]. It acts as the named legal "Sweepstakes Administrator" of record in client promotions' official rules [VOTIGO-003].

**Who buys it.** Brand marketing teams and agencies. Enterprise logos include Michelin, Kraft Heinz, NBCUniversal, Walmart, A+E, Allstate, AARP [VOTIGO-001, VOTIGO-025, VOTIGO-026]. SMB tiers self-serve at $240–$400/mo; Enterprise is call-for-pricing with setup fee and 12-month commitment [VOTIGO-016].

**Job it is hired to do.** "Run this promotion for us — make it engaging, keep it legal, and handle the winners and prizes" — i.e., outsource campaign execution *and* promotion-law operational risk in one vendor. Compliance is a deliverable of the engagement, not a product a customer's engineers integrate.

## 2. Product architecture

Two coupled subsystems:

**A. Campaign platform (software).**
INPUT: campaign configuration (promotion type from 20+ templates, entry form fields, dates, prize inventory, geo/age restrictions, brand assets) plus consumer entries arriving via hosted microsite, iframe embed, social channel, SMS keyword, QR, or API [VOTIGO-002, VOTIGO-012, VOTIGO-029, VOTIGO-035].
DECISION/PROCESS: entry validation (dedupe, IP tracking, CAPTCHA/2FA/OTP, behavioral fraud checks [VOTIGO-018]); instant-win "real-time prize logic" against a seeded prize inventory with timed releases [VOTIGO-017]; receipt OCR + real-time validation against campaign criteria (store/product/date/duplicate checks) [VOTIGO-021]; UGC moderation and voting [VOTIGO-023]; suspicious entries routed to Votigo's internal expert review queue [VOTIGO-019].
OUTPUT: entries database, instant win/lose results, redemption events, moderated galleries, real-time dashboards, exports, CRM syncs, webhook notifications [VOTIGO-012].

**B. Administration service (humans, assisted by the platform).**
INPUT: client's promotion concept, prize pool, target jurisdictions.
DECISION/PROCESS: Votigo staff ("Our legal experts," "drafted hundreds of rulesets" [VOTIGO-032]) draft official rules; file NY/FL/RI registrations and surety bonds when prize pool > $5,000 [VOTIGO-004]; run certified-RNG drawings with documented audit trails and optional independent verification [VOTIGO-006]; verify winners (affidavits, releases, deadline tracking) [VOTIGO-008]; collect W-9s and prepare/file 1099s [VOTIGO-007]; procure and ship prizes to 190+ countries [VOTIGO-009]; file winner lists post-promotion [VOTIGO-004].
OUTPUT: legally administered promotion with a paper/document evidence trail (rules pages hosted on votigo.com subdomains, drawing documentation, winner files, tax filings) [VOTIGO-003, VOTIGO-006].

The critical architectural fact: jurisdictional knowledge lives in staff expertise and per-campaign documents, not in versioned machine-readable policy. The platform's only executable "regulatory" logic is entry-form gating (age, country/state geo-restriction) configured per campaign [VOTIGO-015].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Sweepstakes | Hosted entry microsites, daily entries, random drawing, fraud checks | Marketing | Core | VOTIGO-002, VOTIGO-006 |
| UGC contests | Photo/video/essay submission, moderation, voting, galleries, judging | Marketing | Core | VOTIGO-012, VOTIGO-023 |
| Instant win | Game mechanics, prize inventory, timed releases, real-time prize logic | Marketing | Core | VOTIGO-017 |
| Receipt/code promotions | OCR receipt validation, unique code generation/validation, purchase-based entry | Marketing (CPG/retail) | Core | VOTIGO-021 |
| Digital coupons & rebates | Single/multi-use codes, barcode/POS redemption, cashback processing | Marketing | Core | VOTIGO-022 |
| SMS / text-to-win | Short codes, keywords, TCPA opt-in/opt-out management, carrier approval | Marketing | Core | VOTIGO-029 |
| Loyalty & rewards | Program design + rewards issuance; large portals are custom builds | Marketing | Core-ish (services-heavy) | VOTIGO-033, VOTIGO-014 |
| Legal & compliance services | Official rules, NY/FL/RI registration + bonding, international vetting, alcohol/ABC compliance, winner list filing | Marketing (w/ legal sign-off) | Core service | VOTIGO-004, VOTIGO-005, VOTIGO-032 |
| Winner administration | Certified drawings, affidavits, W-9/1099, disqualification, alternate winners, fulfillment (190+ countries) | Marketing | Core service | VOTIGO-006 – VOTIGO-009 |
| AI sweepstakes layer | Fraud/anomaly monitoring, bot detection, AI-assisted verification, flag-to-human review | Marketing | Embedded feature | VOTIGO-018, VOTIGO-019, VOTIGO-020 |
| Developer API | REST/JSON campaign/entry/analytics integration | Engineering (on behalf of marketing) | **Enterprise add-on** | VOTIGO-010, VOTIGO-016 |
| Custom development | Bespoke microsites, portals, integrations (CRM, ecommerce, POS) | Marketing | Paid services | VOTIGO-014 |
| Agency/white-label | White-labeled microsites/dashboards, multi-client, preferred pricing | Agencies | Core motion | VOTIGO-024 |

## 4. API / developer capability

- **API**: REST, JSON ("Simple, lightweight JSON format for all requests and responses"); sample endpoint `POST /v1/campaigns/create`; resources for campaigns, entries, analytics/metrics, and (per the legacy developer page) winner management, UGC galleries, voting, and social features; OAuth 2.0 and API-key auth with "granular permission management" [VOTIGO-010].
- **Availability**: "Developer API Access" is an **Enterprise add-on**, absent from Standard/Pro plans [VOTIGO-016]. Reviewers ask for "less expensive API options" [VOTIGO-028 notes].
- **Documentation**: The site references a "Detailed API reference, code samples in multiple languages" but links no public docs; APITracker shows no developer docs, API reference, OpenAPI spec, changelog, sandbox, or status page [VOTIGO-010, VOTIGO-011]. Docs appear to be shared privately with Enterprise customers (inference).
- **SDKs**: One JavaScript configuration snippet (`new VotigoAPI({ apiKey, environment: 'production' })`); no published SDK packages found [VOTIGO-010].
- **Webhooks**: Claimed at feature level ("Real-time data transfer and event notifications") with no event catalog or delivery semantics documented [VOTIGO-012].
- **Sandbox**: Not documented. The `environment: 'production'` parameter implies at least one non-production environment (inference); Votigo-internal QA subdomains (qawww.votigo.com, wqa07.votigo.com) are visible in search indexes but are not a customer feature (inference).
- **Rules engine**: None exposed. Campaign logic is configured per campaign in the platform UI or built custom by Votigo's team; "full control over campaign logic" via API is a marketing phrase without documented rule primitives [VOTIGO-010].
- **Synchronous decisioning**: Exists only inside promotion flows (instant-win results, receipt validation, code verification) [VOTIGO-036]. No documented externally callable decision endpoint for arbitrary actions.
- **Latency claims**: "<1s Response" for the AI fraud layer; "Real-Time Validation" for receipts — marketing figures, no SLOs [VOTIGO-018, VOTIGO-021].
- **Versioning**: Only the `/v1/` path prefix; no versioning or deprecation policy documented [VOTIGO-010].
- **Idempotency**: Not documented anywhere.
- **Integration model**: Primary model is *hosted* (microsite/iframe/CNAME) requiring near-zero engineering [VOTIGO-035]; API/CRM integrations (Salesforce, HubSpot, Klaviyo, etc.) are for data sync into marketing stacks [VOTIGO-012]; deeper integrations are delivered as paid custom development [VOTIGO-014].

**Assessment vs core question**: the API is an entry/data conduit for promotions Votigo hosts. There is no public evidence it exposes compliance logic (eligibility rules, jurisdiction gating, audit records) as callable services.

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Partially. Custom entry-form fields and receipt criteria are evaluated within campaigns [VOTIGO-021]; no generic attribute/predicate language is documented.
- **Store customer/user state?** Promotion-scoped state: entry counts/limits, duplicate detection, loyalty membership, opt-ins [VOTIGO-018, VOTIGO-033]. No documented general customer-state store.
- **Return reason codes?** Minimal analog: receipt validation surfaces per-check results (store/product/date/duplicate verified) in the UI [VOTIGO-021]. No documented API reason codes.
- **Output allow/deny/review?** Implicitly: entries are accepted, rejected, or "automatically flagged for manual review by our expert team" — the review lane terminates in Votigo's internal ops, not a customer-facing decision object [VOTIGO-019].
- **Simulate policies?** No evidence.
- **Replay decisions?** No evidence. Drawing documentation supports after-the-fact defense of drawings, not decision replay [VOTIGO-006].
- **Version policies?** No evidence of versioned rule/policy objects. Official rules are dated legal documents per promotion (inference from hosted rules pages [VOTIGO-003]).
- **Deploy rules independently of app code?** Campaign configs are created/edited in the SaaS without customer code deploys — true in the narrow campaign sense [VOTIGO-002]; there is no policy artifact lifecycle beyond that.

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance**: Strong, human-delivered: official rules drafting, No Purchase Necessary/AMOE structuring, NY/FL/RI registration + surety bonds (> $5,000 prize pools), winner list filing, FTC/FCC/CAN-SPAM/COPPA/ADA coverage, TCPA for SMS [VOTIGO-004, VOTIGO-029, VOTIGO-034]. Votigo serves as named Administrator in official rules [VOTIGO-003].
- **Generic regulatory workflow**: None. Everything is promotion-specific.
- **Jurisdiction restrictions**: Software-level geo-restriction (country/state) and age gating configurable per campaign; a paid tier feature [VOTIGO-015]. Alcohol promotions get age verification + geo-targeting + "State ABC laws compliance" as a service package [VOTIGO-005].
- **Location verification**: IP-based tracking/monitoring [VOTIGO-013, VOTIGO-018]. No certified geolocation, GPS/Wi-Fi triangulation, or documented VPN/proxy detection.
- **Legal content/rules**: Human-drafted rules documents, translated/localized for international campaigns; "country-by-country legal vetting" with in-country counsel coordination [VOTIGO-005].
- **Regulatory monitoring**: No product. Staff expertise is kept current (educational blog tracks 2026 requirements) [VOTIGO-034]. The "compliance monitoring" on the AI page means monitoring *entries/campaigns* for integrity and eligibility, with expert oversight — not monitoring *regulations* [VOTIGO-020].
- **Change management**: No evidence of policy change-management tooling.
- **Counsel approval**: "Brand and regulatory requirements review" is part of the service [VOTIGO-004]; Votigo's own staff are "legal experts" (not stated to be licensed attorneys) [VOTIGO-032]. Inference: client in-house/outside counsel review is accommodated by email/document exchange; there is no software approval workflow with counsel as a first-class approver.
- **Historical policy state**: Old rules pages remain hosted (e.g., 2023 promotion rules still live [VOTIGO-003]) — an archive of documents, not queryable policy versions.

## 7. Audit / evidence

Can a customer reconstruct…

- **Exact inputs?** Partially: entries, receipts, and winner documents are stored and retrievable ("Secure document storage and retrieval") [VOTIGO-008, VOTIGO-021]. Not documented as an immutable input snapshot per decision.
- **Exact rule/policy?** The governing official rules document exists and is hosted/dated [VOTIGO-003]. Internal validation configs (fraud thresholds, receipt criteria) are not exposed.
- **Exact version?** No versioned policy objects; document dating only (inference).
- **Exact output?** Winners, disqualifications, and drawings are documented: "Complete Audit Trails — Detailed documentation of every drawing for legal protection," "Documented Disqualification Process" [VOTIGO-006].
- **Exact timestamp?** Entry timestamps implied by entry limits/periods; not documented as evidence features.
- **Human approvals?** For winner verification: affidavits, releases, deadline tracking are recorded [VOTIGO-008]. No platform-wide approval history.
- **Source/legal authority?** No. Rules cite jurisdictions implicitly; there is no provenance link from a decision to a legal source.

Net: evidence capability is **drawing- and winner-centric and document-based** — designed to defend a promotion if challenged (state AG, plaintiff, platform), not to reconstruct arbitrary automated decisions. Retention: only a 60-day deletion-on-request commitment in the privacy policy; no customer-configurable retention controls documented [VOTIGO-030].

## 8. Enterprise readiness

- **SSO/RBAC**: "Role-based access controls and custom permissions" claimed [VOTIGO-013]; Standard plan has "One Shared User Account" (an anti-signal for governance at low tiers); "Single Sign-On Options" is an Enterprise add-on; SAML/SCIM unspecified [VOTIGO-016].
- **Multitenancy/multi-brand**: Real: brands per plan (5 / 15 / unlimited), agency white-label with custom domains and branded dashboards, multi-market/language/brand launches [VOTIGO-016, VOTIGO-024].
- **Environments**: Not offered to customers as far as documented; API `environment` param hints at internal envs (inference) [VOTIGO-010].
- **Security certifications**: "SOC 2 Certified" / "SOC 2 Type II certification" claimed on two official pages [VOTIGO-013, VOTIGO-014]; no trust center, auditor letter, or report-request path found; privacy policy promises only "commercially reasonable" measures [VOTIGO-030]. Treat as claimed-but-unverified.
- **SLA**: "99.9% uptime guarantee" marketing claim; no published SLA or status page [VOTIGO-031].
- **Support**: 24/7 email/phone + dedicated client success team at Enterprise [VOTIGO-016]; support quality is the most consistently praised attribute in reviews [VOTIGO-028].
- **Professional services**: Central to the model — creative, legal, moderation, fulfillment, custom development [VOTIGO-014, VOTIGO-024, VOTIGO-025].
- **Customer scale examples**: Kraft Heinz Super Bowl campaign (53k entries, 465k visits, $400k rewards) [VOTIGO-023]; Michelin promotions on a votigo.com subdomain [VOTIGO-003]; claims of 500M+ entries lifetime and 10M+ loyalty members [VOTIGO-001, VOTIGO-033].
- **Counter-signal**: ~22–27 employees and ~$2.8M estimated revenue [VOTIGO-027] mean thin engineering capacity behind the enterprise logos; enterprise depth comes from services attention, not platform robustness (inference).

## 9. Commercial model

- **Pricing (public)**: Standard $240/mo (annual), Pro $400/mo, Enterprise call-for-pricing with setup fee + 12-month commitment; API, SSO, white-label, CRM integration are Enterprise add-ons; 7-day trial; separate one-time-fee full-service campaigns [VOTIGO-016]. Historical Capterra listing shows feature-gated tiering complaints [VOTIGO-028].
- **Likely buyer**: brand/digital marketing manager or agency; legal touches the engagement but marketing owns budget (inference from site messaging and pricing framing).
- **Implementation burden**: Very low for hosted campaigns (microsite/iframe/CNAME) [VOTIGO-035]; moderate for API/CRM integration (Enterprise only); custom builds are Votigo-delivered projects [VOTIGO-014].
- **Sales motion**: Self-serve SMB + sales-led enterprise/full-service; 500+ agency partner channel [VOTIGO-024].
- **Large customers**: Fortune 500 roster evidenced by case studies and live administered promotions [VOTIGO-003, VOTIGO-023, VOTIGO-025, VOTIGO-026].

## 10. Strengths

1. **End-to-end promotion administration under one roof** — rules → registration/bonding → drawings → verification → 1099s → global fulfillment — with 20 years of operating history and administrator-of-record standing [VOTIGO-003 – VOTIGO-009, VOTIGO-025].
2. **Breadth of promotion mechanics** (20+ types incl. receipt OCR validation, instant win, SMS, coupons/rebates) behind one platform [VOTIGO-001, VOTIGO-021, VOTIGO-022].
3. **Low-friction deployment** via hosted microsites/embeds — marketing can launch without engineering [VOTIGO-035].
4. **Agency/white-label multi-brand machine** (500+ agencies) that multiplies distribution [VOTIGO-024].
5. **Operational fraud controls at entry time** (dedupe, IP, CAPTCHA/2FA/OTP, behavioral flags, human review) tuned to promotions abuse [VOTIGO-018, VOTIGO-019].
6. **High-touch service reputation** — reviews consistently praise support/flexibility [VOTIGO-028].

## 11. Weaknesses / constraints

Evidence-backed or labeled inference:

1. **Compliance is people, not product.** No machine-readable policy, no versioned rules engine, no counsel-workflow software; jurisdiction knowledge is embodied in staff and documents [VOTIGO-004, VOTIGO-032; inference from total absence across docs/pricing/API surface].
2. **API is shallow and gated**: Enterprise add-on, no public reference docs, no sandbox/idempotency/rate-limit/versioning documentation, no published SDKs, no status page [VOTIGO-010, VOTIGO-011, VOTIGO-016].
3. **Security posture is asserted, not demonstrated**: SOC 2 claims without a trust center; privacy policy promises only "commercially reasonable" protections and lists dated mechanisms (Shine the Light; no GDPR detail) [VOTIGO-013, VOTIGO-030].
4. **Small company vs. enterprise promises**: ~$2.8M est. revenue / ~22–27 staff supporting 7 offices, a global fulfillment operation, and Fortune 500 clients implies limited engineering bandwidth for platform R&D [VOTIGO-027; inference].
5. **Feature gating frictions and dated tooling** noted by reviewers (upgrade-to-unlock geo restriction/support; CSS/white-label costs; one unwarned fraudulent-voting incident) [VOTIGO-028].
6. **Marketing statistics are unauditable** ("100% Legal Compliance" guarantee, 98.7% bot detection, 0.01% fraud rate) — treat as positioning, not measured capability [VOTIGO-018, VOTIGO-020, VOTIGO-021].
7. **Evidence trail is document-grade, not system-grade**: drawing/winner documentation exists, but no immutable decision IDs, decision logs linked to policy versions, or replay [VOTIGO-006; inference from absence across all official material].

## 12. Capability matrix scores

Scores per `research/CAPABILITY_MATRIX.md`. Modality caveat: several Category A/C scores reflect **managed-service** capability (humans + platform), not software features; noted below.

```csv
square,score,claim_ids
A01,4,VOTIGO-001;VOTIGO-002;VOTIGO-003;VOTIGO-029
A02,4,VOTIGO-012;VOTIGO-023
A03,4,VOTIGO-017;VOTIGO-023
A04,4,VOTIGO-004;VOTIGO-032;VOTIGO-003
A05,4,VOTIGO-003;VOTIGO-004;VOTIGO-025
A06,3,VOTIGO-017;VOTIGO-034
A07,4,VOTIGO-001;VOTIGO-012;VOTIGO-023
A08,4,VOTIGO-006;VOTIGO-003
A09,4,VOTIGO-009;VOTIGO-025
A10,3,VOTIGO-007
B01,2,VOTIGO-010;VOTIGO-012
B02,2,VOTIGO-036;VOTIGO-021
B03,2,VOTIGO-017;VOTIGO-018;VOTIGO-036
B04,1,VOTIGO-019
B05,1,VOTIGO-021
B06,2,VOTIGO-010;VOTIGO-012
B07,2,VOTIGO-018;VOTIGO-033
B08,?,
B09,?,
B10,?,
C01,2,VOTIGO-004;VOTIGO-005;VOTIGO-015;VOTIGO-020
C02,2,VOTIGO-005
C03,1,VOTIGO-004;VOTIGO-029
C04,1,VOTIGO-017
C05,?,
C06,1,VOTIGO-034
C07,?,
C08,1,VOTIGO-004;VOTIGO-032
C09,?,
C10,0,VOTIGO-010;VOTIGO-011
D01,?,
D02,2,VOTIGO-006
D03,?,
D04,1,VOTIGO-021;VOTIGO-008
D05,2,VOTIGO-008
D06,1,VOTIGO-006
D07,2,VOTIGO-004;VOTIGO-006
D08,1,VOTIGO-030
D09,1,VOTIGO-006
D10,?,
E01,2,VOTIGO-008
E02,2,VOTIGO-005;VOTIGO-003
E03,1,VOTIGO-009
E04,2,VOTIGO-015;VOTIGO-018
E05,1,VOTIGO-018
E06,?,
E07,2,VOTIGO-013;VOTIGO-018
E08,2,VOTIGO-013;VOTIGO-018
E09,1,VOTIGO-019
E10,?,
F01,1,VOTIGO-033
F02,?,
F03,2,VOTIGO-006;VOTIGO-021
F04,2,VOTIGO-021;VOTIGO-022
F05,1,VOTIGO-017
F06,?,
F07,2,VOTIGO-022
F08,?,
F09,1,VOTIGO-033
F10,1,VOTIGO-014;VOTIGO-022
G01,3,VOTIGO-016;VOTIGO-024
G02,2,VOTIGO-013;VOTIGO-016
G03,2,VOTIGO-016
G04,1,VOTIGO-023
G05,1,VOTIGO-010
G06,?,
G07,?,
G08,2,VOTIGO-012
G09,2,VOTIGO-031;VOTIGO-016
G10,2,VOTIGO-013;VOTIGO-014;VOTIGO-030
H01,2,VOTIGO-010;VOTIGO-011;VOTIGO-016
H02,1,VOTIGO-010
H03,2,VOTIGO-012
H04,?,
H05,1,VOTIGO-010
H06,?,
H07,?,
H08,?,
H09,?,
H10,?,
I01,2,VOTIGO-004;VOTIGO-028
I02,1,VOTIGO-016;VOTIGO-011
I03,4,VOTIGO-001;VOTIGO-016;VOTIGO-023;VOTIGO-026
I04,1,VOTIGO-018
I05,3,VOTIGO-003;VOTIGO-023;VOTIGO-025;VOTIGO-026
I06,3,VOTIGO-016
I07,3,VOTIGO-016;VOTIGO-024;VOTIGO-025;VOTIGO-028
I08,1,VOTIGO-028;VOTIGO-035
I09,3,VOTIGO-035
I10,2,VOTIGO-016
J01,1,VOTIGO-015;VOTIGO-020
J02,1,VOTIGO-004;VOTIGO-032
J03,1,VOTIGO-032
J04,0,VOTIGO-020
J05,0,VOTIGO-010;VOTIGO-011
J06,0,VOTIGO-012
J07,1,VOTIGO-006;VOTIGO-008
J08,0,VOTIGO-010;VOTIGO-011
J09,1,VOTIGO-032
J10,0,VOTIGO-011;VOTIGO-020
```

**Scoring notes (0s, 1s, and material ?s):**

- **A-category 3–4s** rest on official product pages corroborated by operational artifacts (live administered rules naming Votigo as Administrator [VOTIGO-003], the Kraft Heinz case study [VOTIGO-023], and the US Sweepstakes acquisition [VOTIGO-025]) — these are managed-service + platform capabilities, category-leading in the promotions vertical. A06 (AMOE) is 3 not 4: explicitly claimed ("alternate means of entry" compliance) and consistent with its administrator role, but no workflow documentation.
- **C10 = 0 (labeled inference)**: Positive-absence reasoning — Votigo's entire compliance layer is delivered as human services and per-campaign legal documents; no product page, pricing line, or API surface anywhere references machine-readable policy artifacts, and its API directory footprint is empty [VOTIGO-010, VOTIGO-011]. A machine-readable legal policy library is incompatible with the observed delivery model, not merely unmentioned.
- **J04, J05, J06, J08, J10 = 0 (labeled inference)**: Same architecture-based reasoning. The API is campaign-scoped (campaigns/entries/analytics) with no authorization primitives [VOTIGO-010, VOTIGO-011]; integrations are marketing-stack (CRM/e-commerce), not risk-vendor normalization [VOTIGO-012]; "compliance monitoring" is expert service over entries, precluding systematic impact analysis or a policy lifecycle control plane [VOTIGO-020]. There is no decision engine whose decisions could be replayed.
- **J01/J02/J03/J07/J09 = 1**: Manual/peripheral analogs exist — executable age/geo entry gating [VOTIGO-015], a human legal-review-then-launch workflow [VOTIGO-004], "legal experts" reviewing rules [VOTIGO-032], drawing/winner documentation as promotion-scoped evidence [VOTIGO-006, VOTIGO-008], and reusable human rules know-how ("hundreds of rulesets") [VOTIGO-032].
- **B04/B05 = 1**: Allow/deny/flag-for-review happens operationally inside Votigo's flows, and receipt validation surfaces per-check results in UI, but neither is a documented decision-output or reason-code model [VOTIGO-019, VOTIGO-021].
- **Material ?s**: B08–B10 (rule conflict, simulation, replay), C05/C07/C09, D01/D03/D10, H04/H06–H10 — no evidence either way; the public developer surface is too thin to verify (no public docs [VOTIGO-011]). These ?s are themselves informative: for an infrastructure purchase, unverifiable = fails procurement diligence (inference).
- **Directionality notes**: I07 = 3 means professional services are *deeply embedded* in the model (self-serve exists, so not absolute); I09 = 3 means integration burden is *low* (hosted model); I08 = 1 means switching cost is *low* (episodic campaigns; loyalty portals add some stickiness — inference).
- **G10 = 2 not 3**: SOC 2 / SOC 2 Type II claimed on two official pages but with no trust center or attestation access, and a privacy policy that undercuts the claim [VOTIGO-013, VOTIGO-014, VOTIGO-030].

## 13. White-space implications

1. **Already solved by Votigo**: The entire *promotion administration* layer of the hypothesis — official rules, AMOE structuring, state registration/bonding, certified drawings, winner verification, tax workflows, fulfillment (A01–A10) — solved as a mature managed service with platform support. Also solved: campaign-level fraud screening and age/state entry gating as configuration [VOTIGO-004–VOTIGO-009, VOTIGO-015, VOTIGO-018].
2. **Partially solved**: Promotion-scoped synchronous decisioning (instant win, receipt validation, code redemption) [VOTIGO-036]; promotion-scoped evidence (drawing audit trails, winner documents, filed winner lists) [VOTIGO-006]; jurisdiction awareness (staff expertise + geo/age config, alcohol/ABC packages) [VOTIGO-005]; multi-brand governance [VOTIGO-024].
3. **Unsolved (by Votigo)**: Everything J01–J10 as *software*: executable versioned regulatory policy, legal-to-production deployment with counsel approvals, impact analysis, cross-product real-time action authorization with reasons, cross-vendor signal normalization, evidence-grade decision reconstruction/replay, policy packs, and a policy lifecycle control plane. Also unsolved: credible developer platform basics (public docs, sandbox, idempotency, versioning policy) [VOTIGO-010, VOTIGO-011].
4. **Could Votigo add the missing capability easily?** No. It lacks the engineering scale (~22–27 people [VOTIGO-027]), the developer-platform DNA (no public docs after 20 years [VOTIGO-011]), and the buyer relationships (marketing, not platform/compliance engineering [VOTIGO-016]). It could — and does — add "AI compliance" *messaging* cheaply [VOTIGO-020], which may muddy category perception without delivering infrastructure (inference).
5. **Could a customer assemble it using Votigo + internal engineering?** Only for promotions, and awkwardly: Votigo handles the legal/administrative wrapper while internal engineering builds eligibility/authorization logic in-app. The Enterprise API could feed entries/winners into internal systems, but customers cannot externalize *decisioning* to Votigo (no decision API), and evidence would be split between Votigo documents and internal logs. For any regulated action beyond promotions (payouts, account gating, wagering, cannabis/alcohol commerce), Votigo contributes nothing [VOTIGO-010, VOTIGO-036] (inference).
6. **What would make a customer buy a separate product instead?** (a) Promotions volume/frequency high enough that per-campaign service fees and human turnaround become a bottleneck — the hypothesis's frequency test; (b) need for the *same* eligibility/compliance logic to run across owned products in real time, not inside a vendor-hosted microsite; (c) audit/regulator pressure requiring systematic decision reconstruction rather than per-drawing paperwork; (d) engineering/compliance buyers who require SOC 2 attestation, public docs, SLAs, and sandboxes that Votigo cannot evidence [VOTIGO-011, VOTIGO-030, VOTIGO-031]. Conversely — and this argues *against* the white space — for the large population of brands running a handful of promotions per year, Votigo's "we take the liability and the labor" model is likely *more* attractive than operating policy infrastructure (inference).

## 14. Replacement risk

**LOW** (for entering the proposed Promotion OS software space).

Votigo's assets — legal-operations expertise, fulfillment logistics, enterprise brand relationships, administrator-of-record standing — are the *service* complement of the proposed product, but its software trajectory points the other way: a 20-year-old platform with no public API docs, no policy artifacts, no developer community, ~$2.8M revenue, and a 22–27-person team spread across campaigns, fulfillment, and custom builds [VOTIGO-010, VOTIGO-011, VOTIGO-027]. Building a policy-as-code control plane with counsel workflows and evidence-grade replay is a different company. Two caveats: (1) **demand-suppression risk is real and higher than entry risk** — Votigo and its peers absorb exactly the pain (promotion compliance) that would otherwise drive brands to buy policy software, so the wedge's addressable pain in the promotions vertical is already monetized by services (inference); (2) Votigo's "AI compliance monitoring" messaging shows it will cheaply occupy adjacent *positioning* even without infrastructure [VOTIGO-020].

## 15. Adjacent discoveries

Beyond the assigned 15-company set, these surfaced during research and merit consideration:

1. **Brandmovers** (brandmovers.com) — full-service sweepstakes platform + administration with promotional strategy, sweepstakes law expertise, winner management, fulfillment; a direct Votigo peer at enterprise scale.
2. **Marden-Kane** (mardenkane.com) — sweepstakes administration/fulfillment agency since 1957; the archetype legacy administrator; evidence that the services substitute is old, entrenched, and plural.
3. **PrizeLogic** — enterprise digital promotions/loyalty provider (Southfield, MI) known for large CPG/retail instant-win and rebate programs; closest large-scale services+platform hybrid.
4. **National Sweepstakes Company** (nationalsweepstakescompany.com) — boutique sweepstakes administration, drawings, prize fulfillment; shows a long tail of administrators competing on service.
5. **Don Jagoda Associates / Ventura Associates** — long-standing promotion administration agencies repeatedly cited alongside the above; further substitutes on the legal-administration wedge.
6. **SweepWidget** (sweepwidget.com) — self-serve giveaway tool with documented country/state geo-targeting; represents the low-end software substitute compressing prices beneath enterprise platforms.

(Also relevant context: Merkle's promotion arm — formerly HelloWorld — historically served the largest enterprise promotions; category managers may want it in the appendix.)

## 16. Evidence ledger

Full records in `outputs/evidence/01_votigo.jsonl` (36 records). Condensed table:

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| VOTIGO-001 | Positioning: promotions platform + legal/admin + fulfillment; 15k campaigns, 500M entries; Fortune 500 clients | https://www.votigo.com/ | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-002 | Sweepstakes: hosted microsites, iframe/CNAME, fraud detection, real-time tracking | https://www.votigo.com/promotions-engagement/sweepstakes | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-003 | Votigo named "SWEEPSTAKES ADMINISTRATOR" in live official rules on votigo.com subdomain | https://michelin.votigo.com/fbsweeps/pages/TheBigChillSweepstakes/rules | official-doc | 2026-08-18 | HIGH |
| VOTIGO-004 | Custom official rules; NY/FL/RI registration + bonds >$5,000; winner list filing; FTC/COPPA/ADA/NPN coverage | https://www.votigo.com/legal-admin/legal-compliance-services | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-005 | International country-by-country vetting, GDPR/CASL, translation; alcohol/ABC compliance with age+geo | https://www.votigo.com/legal-admin/legal-compliance-services | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-006 | Certified RNG drawings, complete audit trails, independent verification | https://www.votigo.com/legal-admin/winner-administration | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-007 | W-9 collection, prize value calc, 1099 preparation & filing (page cites >$2,000) | https://www.votigo.com/legal-admin/winner-administration | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-008 | Affidavits, liability/publicity releases, deadline tracking, secure document storage | https://www.votigo.com/legal-admin/winner-administration | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-009 | Prize fulfillment: physical/digital/cash, 190+ countries, customs, alternates/disqualification | https://www.votigo.com/legal-admin/winner-administration | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-010 | API: REST/JSON, OAuth2/API key, POST /v1/campaigns/create, campaigns/entries/analytics; no public docs linked; 99.9% uptime claim | https://www.votigo.com/technology/developer-api | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-011 | APITracker profile empty: no docs, reference, webhooks docs, sandbox, OpenAPI, changelog, status page | https://apitracker.io/a/votigo | third-party | 2026-08-18 | MEDIUM |
| VOTIGO-012 | Platform: RESTful API (campaigns/entries/reporting), webhooks event notifications, CRM integrations | https://www.votigo.com/technology/platform-features | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-013 | Claims: SOC 2 Certified, 256-bit encryption, fraud/duplicate/IP controls, WCAG/ADA, RBAC | https://www.votigo.com/technology/platform-features | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-014 | Custom dev: SOC 2 Type II claim, GDPR/CCPA, stacks/clouds, CRM/ecommerce/POS integrations, 2.3M-member custom loyalty portal | https://www.votigo.com/technology/custom-development | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-015 | Geo-restriction paid tier feature (Pro+); enterprise geo-targeting | https://www.votigo.com/solutions/pricing-and-plans.php | official-doc | 2026-08-18 | HIGH |
| VOTIGO-016 | Pricing: $240/$400/mo tiers; Enterprise = setup fee, 12-mo commitment; API, SSO, white-label as Enterprise add-ons; 7-day trial | https://www.votigo.com/solutions/pricing-and-plans.php | official-doc | 2026-08-18 | HIGH |
| VOTIGO-017 | Instant win: real-time prize logic, inventory, timed releases; bundled rules/bonding/tax/AMOE compliance | https://www.votigo.com/promotions-engagement/instant-win-games | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-018 | AI fraud: real-time validation, behavioral patterns, CAPTCHA/2FA/OTP, adaptive IP + rate limits; unaudited stats, <1s claim | https://www.votigo.com/technology/ai-sweepstakes | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-019 | Suspicious entries flagged for manual review by Votigo's internal expert team | https://www.votigo.com/technology/ai-sweepstakes | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-020 | "Multi-Jurisdiction Compliance 50+ States", automated eligibility workflows, "100% Legal Compliance" guarantee — expert service framing | https://www.votigo.com/technology/ai-sweepstakes | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-021 | Receipt OCR + real-time validation with per-check results; cashback/rebate support | https://www.votigo.com/promotions-engagement/receipt-code-based-promotions | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-022 | Coupons: single/multi-use codes, barcode/POS, redemption tracking; rebates with secure payment processing | https://www.votigo.com/promotions-engagement/digital-coupons-rebates | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-023 | Kraft Heinz UGC + instant win case study: 53k entries, 465k visits, $400k rewards, real-time moderation | https://www.votigo.com/case-studies/kraftheinz_ugc | case-study | 2026-08-18 | HIGH |
| VOTIGO-024 | Agencies: white-label microsites/dashboards, multi-brand/multi-client, 500+ partners, end-to-end services | https://www.votigo.com/for-agencies | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-025 | 2020 acquisition of US Sweepstakes & Fulfillment Co. (administration, rules, legal consulting, fulfillment, rebates) | https://social.votigo.com/2020/11/05/votigo-inc-completes-acquisition-of-us-sweepstakes-fulfillment-co/ | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-026 | Founded 2006; 7 offices; hybrid "platform backed by hands-on campaign execution"; Fortune 500 clients | https://www.votigo.com/about | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-027 | Est. $2.8M revenue (2024), 22 employees, $2.3M raised (last round 2019) | https://getlatka.com/companies/votigo-inc | third-party | 2026-08-18 | LOW |
| VOTIGO-028 | Reviews: outstanding service; cons: tier gating ("restrict foreign votes… upgrade"), CSS/white-label cost, one fraud-voting incident | https://www.capterra.com/p/140293/Contests-Sweepstakes/ | user-report | 2026-08-18 | MEDIUM |
| VOTIGO-029 | SMS text-to-win: short codes, keywords, TCPA opt-in/opt-out, carrier approval, SMS winner notification | https://www.votigo.com/products/sms-and-mobile | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-030 | Privacy policy: 60-day deletion, "commercially reasonable" security, processor role for customer campaigns | https://www.votigo.com/privacy-policy | official-doc | 2026-08-18 | HIGH |
| VOTIGO-031 | "99.9% uptime guarantee" claim; 24/7 enterprise support; no published SLA/status page | https://www.votigo.com/technology/developer-api | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-032 | "Legal experts… drafted hundreds of rulesets"; $5,000 NY/FL/RI bonding trigger; filing/deadline services | https://www.votigo.com/products/services.php | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-033 | Loyalty: rewards via fulfillment services; 10M+ members claim; "Full API Access"; no wallet/ledger docs | https://www.votigo.com/promotions-engagement/loyalty-rewards-programs | official-marketing | 2026-08-18 | MEDIUM |
| VOTIGO-034 | Blog tracks current law: NY/FL bonding equal to prize value, RI retail, AMOE equal odds | https://social.votigo.com/2026/04/15/sweepstakes-legal-requirements/ | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-035 | Hosted pages/iframe/CNAME = minimal integration; 150+ countries, 25+ languages | https://www.votigo.com/technology/platform-features | official-marketing | 2026-08-18 | HIGH |
| VOTIGO-036 | Synchronous evaluation exists only inside hosted promotion flows (instant win, receipts, codes) | https://www.votigo.com/promotions-engagement/instant-win-games | official-marketing | 2026-08-18 | MEDIUM |

## 17. Verdict

**SUBSTITUTE**

Votigo does not overlap with Promotion OS's proposed architecture — it has no policy engine, no decision API, no counsel workflow software, no evidence-grade replay (J-scores 0–1). But it substitutes for the *outcome* that architecture would sell in the promotions vertical: enterprises hand Votigo the compliance problem (rules, registrations, bonding, drawings, winner verification, tax, fulfillment) as a managed service, with Votigo as administrator of record absorbing operational burden. For brands running episodic promotions, that service model is cheaper, lower-risk, and requires zero engineering — a direct answer to "why not keep your current vendor + counsel?" Its capability ceiling (gated shallow API, unverifiable security posture, ~25-person team) means it poses low entry risk into policy infrastructure, but it — and its many service peers — already monetizes the pain the wedge targets. Any Promotion OS thesis must beat the services substitute on frequency, cross-product reach, and evidence rigor, not on promotion administration itself.
