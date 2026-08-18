# Company Report — Persona

Researcher: Research Agent 10 (Persona)
Date: 2026-08-18
Category: Identity / orchestration
Manager: Manager C

Seed domain: withpersona.com · docs.withpersona.com
Core question: **How much rule-based verification and case orchestration can customers configure?**

> Sourcing note: withpersona.com marketing pages (including /security, /pricing, /product/*) return HTTP 403 to automated fetching. This report is built primarily on docs.withpersona.com (fully accessible, including the machine-readable OpenAPI spec and llms.txt index) and help.withpersona.com (accessible), with marketing/commercial claims corroborated via press releases and third-party coverage at reduced confidence where noted.

## 1. Executive summary

**Actual core product.** Persona (Persona Identities, Inc., founded 2018, San Francisco) is a unified **identity platform**: modular building blocks to collect, verify, decision, investigate, and monitor the identities of people and businesses. The product pillars are Inquiries/Dynamic Flow (user-facing verification flows), Verifications (government ID, selfie/liveness, documents, database/authoritative-source checks), Reports (watchlist/PEP/adverse media/risk data pulls with continuous monitoring), Workflows (a no-code + custom-code automation and decisioning engine), Cases (a fully customizable investigation/manual-review center with SAR e-filing to FinCEN), Graph (link analysis for fraud rings), Transactions (customer-defined event objects for API-only decisioning), Lists, Accounts (persistent per-user state), Marketplace (~90+ third-party integrations), and Connect (cross-organization reuse of KYC/KYB results). [PERSONA-001, -027, -028]

**Who buys it.** Compliance/AML teams (KYC/CIP onboarding, sanctions screening, SAR filing), trust & safety and fraud teams (marketplaces, social platforms), and product/engineering teams embedding verification. 4,000+ businesses including OpenAI, LinkedIn, Block, Robinhood, Etsy, Twilio; $100M+ ARR (2024); $200M Series D at a $2B valuation (April 2025). [PERSONA-031]

**Job it is hired to do.** "Decide whether this person/business is who they claim to be, and what to do about it" — automate the verify→decision→investigate→monitor loop with configurable risk logic, while leaving an audit trail. It is emphatically **not** hired to encode regulatory content: customers author their own rules; Persona provides the execution, evidence, and signal infrastructure.

**Answer to the core question (summary).** Customer-configurable surface is very large: per-check required/optional verification configuration; template-level decisioning; a full workflow builder (event/API/scheduled triggers, conditionals over virtually any platform object plus third-party data, parallel branches, waits, ~20 action types including custom JavaScript and signed HTTPS calls); fully custom case templates (field schemas, statuses, queues, SLAs, actions, checklists); versioning with drafts, staged percentage rollouts, and revert on both workflows and inquiry templates. Constraints: decisioning is **asynchronous** (webhook/poll, not a synchronous authorization endpoint), several advanced knobs are enablement-gated ("contact us"/CSM), and configuration is dashboard-first with limited config-as-code.

## 2. Product architecture

Concrete flow (identity decisioning):

**INPUT** → An end user enters a flow (Hosted/Embedded/SDK **Inquiry**) or the customer's backend creates a **Transaction**/**Verification**/**Report** via API. Persona captures: user-submitted attributes and media (IDs, selfies, documents), device/network signals (GPS + IP geolocation, VPN/proxy/Tor/datacenter flags, fingerprints, behavioral bot scores), third-party data (Marketplace reports: LexisNexis, SentiLink, Chainalysis, Equifax OneView, Middesk, etc.), and any customer-supplied custom fields (schemas defined per inquiry template / transaction type / account type). [PERSONA-002, -019, -026, -027]

**DECISION/PROCESS** → (1) **Verifications** run configured checks; every required check must pass; each check returns status + reason codes + metadata. (2) **Workflows** — versioned automations triggered by events, API calls, or schedules — evaluate conditional logic over inquiry/report/case/account/graph/list/third-party criteria and execute actions: approve/decline/mark-for-review inquiries, run more reports, create cases, call external systems (signed HTTPS), run custom JavaScript, update CRMs. (3) **Cases** route items needing human judgment into customizable queues with SLAs, statuses (initial/intermediate/end), required reason tags, and one-click Case Actions (which are themselves workflows). [PERSONA-003, -004, -005, -010, -012, -015]

**OUTPUT** → Inquiry status approved/declined/needs_review (the native allow/deny/review model), verification passed/failed with per-check reasons, transaction custom statuses, case resolutions, SAR filings to FinCEN — all emitted as events (100+ event types) to webhooks and retrievable via the versioned REST API; evidence artifacts exportable as PDFs; every inquiry permanently pinned to the template version that produced it; workflow runs record their workflow version. [PERSONA-004, -013, -016, -020, -021, -041]

Persistent state lives in **Accounts** (all history for a person/business, custom types/fields/statuses, relations, consolidation), queried at decision time by workflows, Graph, and Lists. [PERSONA-039]

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Inquiries / Dynamic Flow | Configurable user-facing verification flows (hosted/embedded/SDK), branching UI, theming, versioned templates | Product/eng + compliance | Core | PERSONA-001, -016 |
| Verifications | Modular identity checks (gov ID, NFC, selfie, document, database, AAMVA/eCBSV/TIN/phone-carrier/Serpro) with per-check config | Compliance, fraud | Core | PERSONA-005, -007 |
| Reports | External data pulls: watchlist, PEP, adverse media, email/phone risk, business reports; continuous monitoring 1–365 days | Compliance/AML | Core | PERSONA-008, -009 |
| Workflows | No-code/custom-code automation & decisioning engine; event/API/scheduled triggers; versioned with staged rollouts | Ops, compliance, fraud | Core (advanced steps gated Growth+) | PERSONA-002, -003, -015 |
| Cases | Customizable investigation center: templates, field schemas, statuses, queues, SLAs, actions, analytics; AML/SAR module with FinCEN SDTM e-filing | Fraud ops, AML/BSA officers | Core | PERSONA-010–014 |
| Graph | Link analysis across accounts to find fraud rings; saved query templates; usable in workflow conditionals | Fraud/risk | Add-on (Growth+) | PERSONA-017, -030 |
| Transactions | Customer-defined event objects (custom schemas/statuses) for API-only, UI-less decisioning | Platform eng | Add-on (Enterprise, enablement-gated) | PERSONA-019 |
| Accounts / Lists / Devices | Persistent entity state, custom fields/statuses; match lists (IP, geo, country, ID number, face…); device intelligence | Fraud/risk | Core | PERSONA-018, -026, -039 |
| Marketplace | ~90+ integrations: identity/fraud data vendors, crypto risk, CRMs, support tools, LLM providers | All | Core distribution layer (Growth+) | PERSONA-027 |
| Connect | Cross-organization sharing/reuse of KYC/KYB results via share tokens | Partnerships/compliance | Add-on | PERSONA-028 |
| Relay | Privacy-preserving verification returning only a claim result (Privacy Pass/blind RSA), with server SDK/edge workers | Privacy-sensitive platforms | Add-on | PERSONA-042 |
| Solution Library | Pre-built packs: KYC, KYC+AML, KYC+Age Verification, KYC+Crypto Watchlist, etc. (template + workflows + case template) | New customers | Core onboarding accelerant | PERSONA-029 |

## 4. API / developer capability

- **APIs**: Versioned REST API (dated versions 2020-05-18 → 2025-12-08), JSON:API-style resources, 172 documented paths, published OpenAPI 3.1 spec and llms.txt index, plus a docs MCP server. Resources cover inquiries, verifications, reports, cases, case templates, transactions, accounts, lists/list items, importers (bulk), graph queries, events, devices, documents, webhooks, API keys/logs, user audit logs, OAuth (cross-org), Connect. [PERSONA-020]
- **SDKs**: client-side JS (v5; inlined/React/Vue), iOS (v3), Android (v2), React Native (v2); Relay server-side SDK + self-hosted gateway/edge workers. No general-purpose server API client libraries; API examples are raw HTTP in 8 languages. [PERSONA-042]
- **Webhooks**: 100+ event types; HMAC signatures, event filters, payload allowlists, PII attribute blocklists, custom headers, OAuth 2.0 outbound auth, 7 retries w/ exponential backoff, manual redelivery, event simulation, per-webhook API version pinning; 30-day event retention. [PERSONA-021]
- **Sandbox**: free, no real verifications; force pass/fail; dedicated simulate endpoints (Perform Simulate Actions, Set Simulated Data); sandbox report-hit triggering. [PERSONA-022]
- **Rules engine**: Workflows (Section 5) + verification check configuration; no standalone policy language — logic is built visually with expression/formula support and an Evaluate Code (JavaScript) escape hatch. [PERSONA-002, -003]
- **Synchronous decisioning**: **Not offered.** Docs steer real-time consumers to poll the API; workflow runs, reports, and graph queries are async (submitted → completed). Third-party analysis cites ~5s automated verification decisions. This is IDV-speed, not authorization-engine latency. [PERSONA-033, -034]
- **Latency claims**: none published in docs; `processing-time-seconds` is exposed on workflow runs. [PERSONA-034]
- **Versioning**: per-API-key and per-webhook version pinning; documented breaking vs. non-breaking change policy; changelog. [PERSONA-020]
- **Idempotency**: `Idempotency-Key` on all POSTs; stored result replay incl. errors; 24h key retention; parameter-mismatch protection. [PERSONA-020]
- **Integration model**: (a) hosted/embedded/SDK inquiry flows + webhooks (most customers); (b) API-only via Transactions + Workflows, Enterprise plan, enablement-gated — "full control over data processing, compliance checks, or fraud analysis" without Persona UI. IP allowlisting on API keys; API-key payload filters restrict record visibility per key. [PERSONA-019, -025]

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Yes. Conditionals reference inquiry fields (incl. custom fields), report results, case statuses, account tags/fields, template identity, database-match results, graph query output, list matches, and arbitrary third-party data ingested via API trigger schemas or Evaluate Code. [PERSONA-002, -017]
- **Store customer/user state?** Yes — Accounts with custom types/fields/statuses, relations, tags, consolidation; Transactions with custom schemas/statuses for event-level state. [PERSONA-019, -039]
- **Return reason codes?** Yes at the check level (name/status/reasons/requirement/metadata per check) and via a published fail-reason list; human decisions can require Status Tags ("reason for status change"). No single top-level decision reason-code taxonomy across the whole platform. [PERSONA-006, -014]
- **Output allow/deny/review?** Yes — approved/declined/needs_review is the native inquiry decision model, set by workflows, reviewers, or API. Case resolutions are customer-defined end statuses (e.g. Accept/Decline). [PERSONA-004, -011]
- **Simulate policies?** Partially. Sandbox simulate endpoints, webhook simulation, and — most notably — percentage rollouts that split live traffic between new (treatment) and prior (control) workflow versions with per-run version visibility. No offline backtest/replay of historical traffic against a draft policy. [PERSONA-015, -022]
- **Replay decisions?** No replay feature. Reconstruction is possible (Section 7) but there is no "re-run decision as-of date X" capability. [PERSONA-015, -016 — inference from documented feature set]
- **Version policies?** Yes, strongly: workflows, inquiry templates, and verification templates all have drafts → immutable published versions → history → revert; inquiries are permanently pinned to their template version; workflow runs record their workflow version. [PERSONA-015, -016]
- **Deploy rules independently of app code?** Yes — workflows and templates are edited/published in the dashboard, decoupled from customer app deployments; org-level workflows run across sandbox/production environments. [PERSONA-015, -036]

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance**: None. No sweepstakes/contest/AMOE/official-rules constructs anywhere in the API or docs. [PERSONA-035]
- **Generic regulatory workflow**: Strong for identity-adjacent compliance: KYC/CIP flows, KYB, sanctions/PEP/adverse-media screening with match adjudication, perpetual KYC (continuous monitoring), AML alert→SAR investigation case flows, and direct FinCEN SAR e-filing (SDTM). [PERSONA-008, -009, -013]
- **Jurisdiction restrictions**: Buildable, not shipped: country lists, geolocation lists, workflow conditionals on country/IP/GPS attributes; per-country ID/database coverage maps. Customers author the jurisdiction logic themselves. [PERSONA-018, -026]
- **Location verification**: IP geolocation + device GPS (lat/long/precision) + VPN/proxy/Tor/datacenter detection; not certified-grade geolocation compliance (no equivalent of GeoComply's iGaming attestation stack documented — labeled inference from absence). [PERSONA-026]
- **Legal content/rules**: Persona ships **no legal content**. Solution Library packs (KYC, KYC+AML, Age) are technical starting-point configurations; the KYC solution article explicitly avoids BSA/FinCEN/CIP citations. No legal-source provenance concept exists in the data model. [PERSONA-029]
- **Regulatory monitoring**: No product feature. Persona publishes educational content (e.g., age-verification laws by industry) and updates its products as laws emerge, but customers get no change-monitoring/alerting feature. [PERSONA-037 — inference]
- **Change management**: Excellent for *configuration* (drafts, immutable versions, staged rollouts, revert, comparisons) — but it is generic software change management, not legal-effective-date management. [PERSONA-015, -016]
- **Counsel approval**: Not offered. RBAC can restrict who may edit/publish templates and workflows (environment-level "Product" permissions), so a customer could informally reserve publish rights to a compliance role — labeled inference; there is no documented maker-checker/approval gate on publishing. [PERSONA-024]
- **Historical policy state**: Immutable version history on templates/workflows with per-decision version pinning gives strong historical config state; however there is no as-of-date query API across policy state, and no effective-dating (versions activate on publish/rollout, not on scheduled legal dates). [PERSONA-015, -016]

## 7. Audit / evidence

Can a customer reconstruct:

- **Exact inputs?** Yes — verification attributes and media are frozen at submission; inquiries retain collected fields; API logs (2 weeks) capture request/response. [PERSONA-020, -040]
- **Exact rule/policy?** Largely — the inquiry's template version (permanently pinned) captures screens/verifications/decision config; workflow runs record workflow version; published versions are immutable and comparable. Gap: Evaluate Code step contents and some dashboard-side config are visible in-dashboard, not via a full config-export API. [PERSONA-015, -016]
- **Exact version?** Yes (itmplv_ IDs; workflow-version relationships). [PERSONA-015, -016]
- **Exact output?** Yes — statuses, per-check results with reasons, events with IDs and timestamps; report match/dismiss history. [PERSONA-006, -008]
- **Exact timestamp?** Yes — created/completed timestamps on all objects; event created-at for server-side ordering. [PERSONA-020, -021]
- **Human approvals?** Yes — User Audit Logs (6 months, API-accessible: user, IP, UA, params, impersonator), case assignment/status history with required reason tags, case comments. [PERSONA-014, -023]
- **Source/legal authority?** No — no legal-source provenance anywhere. [Section 6; reasoned absence]

Evidence packaging: Print Inquiry/Report/Verification PDF endpoints, case export, SAR XML/FinCEN e-file. Retention: automated retention policies with cascading redaction exist (set up with Persona's help); field-level/conditional redaction via workflows; webhook/API attribute blocklists. Tamper-evidence is limited to HMAC-signed outbound payloads and write-once field policies — no documented cryptographic log integrity. [PERSONA-011, -013, -021, -025, -041]

**Net**: strong operational auditability for identity decisions; falls short of "evidence-grade decision reconstruction" as a product — reconstruction is an assembly exercise across objects, and 2-week API-log / 30-day webhook-event windows limit long-horizon forensic completeness (longer-lived objects themselves persist until redacted).

## 8. Enterprise readiness

- **SSO/RBAC**: SAML SSO (Google/Okta/Azure), SCIM (Okta, Entra), 2FA; roles as permission collections with org-level and environment-level scopes and per-permission constraints (e.g., restrict case access by template or assignment); default-role auto-assignment; SSO gated Growth+. [PERSONA-024]
- **Multitenancy / multi-brand**: Organizations contain multiple environments; org-level workflows span environments; Enterprise plan targets multiple business units/international subsidiaries; multi-org SSO documented; per-template theming and custom subdomains for brand separation. [PERSONA-024, -030, -036]
- **Environments**: sandbox + production, separate API keys/versions, per-environment permissions and rate limits. [PERSONA-020, -022]
- **Security certifications**: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, FERPA, Kantara (NIST SP 800-63), Age Check Certification Scheme (official pages; corroborated by press — MEDIUM confidence due to bot-blocked site). [PERSONA-032]
- **SLA**: No public uptime/SLA terms found; a status page domain (status.withpersona.com) exists. Unresolved. [G09 = ?]
- **Support / professional services**: tiered — Essential is self-serve/community; Growth/Enterprise add implementation and dedicated support; multiple advanced features require CSM/support enablement (Transactions, inquiry signals flag, face lists, check-default tuning, retention policies). [PERSONA-005, -019, -025, -030]
- **Customer scale**: 4,000+ businesses; OpenAI, LinkedIn, Block, Robinhood, Etsy, Twilio, DoorDash, Coursera, Brex; 300M+ verifications by 2024; 200+ countries, 20 languages. [PERSONA-031, -033]

## 9. Commercial model

- **Pricing**: Essential $250/month (annual) incl. 500 services/month, then $1.50/service; 60-day free trial; free 1-year Startup Program; Growth and Enterprise custom-priced. Third-party data suggests $0.50–$4.00 per verification by type/volume. Feature gating: Evaluate Code, continuous monitoring, SSO, Graph, advanced Cases → Growth+; API-only integration → Enterprise. [PERSONA-030]
- **Likely buyer**: compliance/AML leadership and trust & safety/fraud leadership, with engineering as implementer; usage-based spend scales with verification volume.
- **Implementation burden**: hosted-flow integrations are near-trivial (link/redirect); embedded/SDK moderate; API-only/Transactions integrations are enterprise projects with enablement dependencies. [PERSONA-019, -022]
- **Sales motion**: product-led at the bottom (self-serve Essential/trial), sales-led for Growth/Enterprise. [PERSONA-030]
- **Large-customer evidence**: Series D press and third-party coverage name marquee customers and $100M+ ARR. [PERSONA-031, -033]

## 10. Strengths

1. **Configurable orchestration depth**: triggers→conditionals→actions over every platform object plus third-party data, with custom JavaScript and signed outbound HTTP; case management that is genuinely schema-level customizable (fields, statuses, queues, SLAs, actions). [PERSONA-002, -003, -010–012]
2. **Version discipline**: immutable versions, per-decision version pinning, drafts, percentage rollouts with treatment/control, revert — rare rigor for a compliance-ops product. [PERSONA-015, -016]
3. **Signal breadth + vendor normalization**: first-party document/biometric/behavioral/device/network signals plus ~90+ marketplace integrations normalized into one report/event/conditional model. [PERSONA-026, -027]
4. **Developer platform maturity**: Stripe-style dated API versioning, idempotency, documented rate limits, webhooks with security controls, OpenAPI, sandbox simulation. [PERSONA-020–022]
5. **Regulated-workflow endpoints**: perpetual KYC monitoring and direct FinCEN SAR e-filing close the loop from detection to regulator filing. [PERSONA-009, -013]
6. **Scale and capital**: $2B valuation, $100M+ ARR, marquee AI-era customers; strategic push into agentic-AI identity. [PERSONA-031, -038]

## 11. Weaknesses / constraints

Evidence-backed:
- **No synchronous authorization**: no endpoint evaluates rules and returns a decision inline; docs recommend polling for real-time needs; workflow/graph/report processing is async. Unsuited as-is for sub-second in-transaction gating. [PERSONA-034]
- **No regulatory content**: zero legal rules, citations, jurisdictional policy libraries, effective-dating, or change monitoring; all compliance logic is customer-authored. [PERSONA-029, -035; Section 6]
- **Enablement gating / services touch**: Transactions, signals exposure, face lists, check-default tuning, retention policies, and production itself require contacting Persona. [PERSONA-005, -019, -022, -025]
- **Dashboard-first config**: no IaC/Terraform, no full config export/import API; workflow logic (including embedded JS) lives in the visual builder. [PERSONA-035; H09 evidence]
- **Forensic windows**: API logs 2 weeks, webhook events 30 days, user audit logs 6 months. [PERSONA-020, -021, -023]
- **No public SLA** found. [G09 = ?]

Labeled inference:
- **Identity-scoped worldview**: every object orbits a person/business identity; modeling non-identity regulated actions (a prize award, a wager, a credit issuance) requires bending Transactions + Workflows to a purpose they weren't designed for, without ledger/value primitives.
- **Switching cost is moderate and rising**: third-party analysis called switching low (~3 months), but that predates deep Workflows/Cases/Graph/Accounts adoption, which accretes state and process lock-in. [PERSONA-033]

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,PERSONA-035
A02,0,PERSONA-035
A03,0,PERSONA-035
A04,0,PERSONA-035
A05,0,PERSONA-035
A06,0,PERSONA-035
A07,0,PERSONA-035
A08,0,PERSONA-035
A09,0,PERSONA-035
A10,1,PERSONA-007;PERSONA-035
B01,3,PERSONA-002;PERSONA-019
B02,1,PERSONA-034
B03,1,PERSONA-033;PERSONA-034
B04,4,PERSONA-003;PERSONA-004
B05,3,PERSONA-006;PERSONA-014
B06,4,PERSONA-011;PERSONA-019;PERSONA-039
B07,4,PERSONA-001;PERSONA-039
B08,1,PERSONA-002
B09,2,PERSONA-015;PERSONA-022
B10,1,PERSONA-015;PERSONA-016
C01,2,PERSONA-018;PERSONA-002;PERSONA-037
C02,1,PERSONA-029
C03,1,PERSONA-019
C04,1,PERSONA-002;PERSONA-009
C05,3,PERSONA-015;PERSONA-016
C06,1,PERSONA-037
C07,2,PERSONA-015
C08,1,PERSONA-024
C09,0,
C10,1,PERSONA-029
D01,3,PERSONA-020;PERSONA-040
D02,3,PERSONA-020;PERSONA-021
D03,3,PERSONA-015;PERSONA-016
D04,3,PERSONA-040;PERSONA-016
D05,3,PERSONA-023;PERSONA-014
D06,2,PERSONA-016;PERSONA-023;PERSONA-040
D07,3,PERSONA-013;PERSONA-041
D08,3,PERSONA-025
D09,1,PERSONA-021;PERSONA-011
D10,3,PERSONA-023;PERSONA-020
E01,4,PERSONA-007;PERSONA-001
E02,3,PERSONA-029;PERSONA-037
E03,3,PERSONA-007;PERSONA-008
E04,3,PERSONA-026
E05,3,PERSONA-026
E06,3,PERSONA-026
E07,3,PERSONA-026;PERSONA-008
E08,3,PERSONA-005;PERSONA-017;PERSONA-018
E09,4,PERSONA-010;PERSONA-011;PERSONA-012;PERSONA-013
E10,4,PERSONA-027;PERSONA-002
F01,0,PERSONA-035
F02,0,PERSONA-035
F03,0,PERSONA-035
F04,0,PERSONA-035
F05,0,PERSONA-035
F06,0,PERSONA-035
F07,0,PERSONA-035
F08,0,PERSONA-035
F09,0,PERSONA-035
F10,1,PERSONA-003
G01,3,PERSONA-036;PERSONA-030;PERSONA-024
G02,3,PERSONA-024
G03,3,PERSONA-024
G04,2,PERSONA-010;PERSONA-012
G05,3,PERSONA-022;PERSONA-036
G06,3,PERSONA-022;PERSONA-015;PERSONA-021
G07,3,PERSONA-015;PERSONA-016
G08,4,PERSONA-021
G09,?,
G10,3,PERSONA-032
H01,4,PERSONA-020
H02,3,PERSONA-042
H03,4,PERSONA-021
H04,3,PERSONA-022
H05,4,PERSONA-020
H06,3,PERSONA-020
H07,3,PERSONA-020
H08,3,PERSONA-020;PERSONA-023
H09,2,PERSONA-011;PERSONA-016
H10,0,PERSONA-035
I01,3,PERSONA-013;PERSONA-008
I02,3,PERSONA-020;PERSONA-042
I03,1,
I04,3,PERSONA-017;PERSONA-026
I05,4,PERSONA-031
I06,3,PERSONA-030
I07,2,PERSONA-005;PERSONA-019;PERSONA-030
I08,2,PERSONA-033
I09,2,PERSONA-030;PERSONA-022
I10,2,PERSONA-030
J01,2,PERSONA-029;PERSONA-015;PERSONA-003
J02,1,PERSONA-015
J03,1,PERSONA-024
J04,1,PERSONA-015
J05,2,PERSONA-019;PERSONA-034
J06,3,PERSONA-027;PERSONA-008
J07,2,PERSONA-016;PERSONA-023;PERSONA-041
J08,1,PERSONA-015;PERSONA-016
J09,2,PERSONA-029;PERSONA-028
J10,2,PERSONA-015;PERSONA-036
```

**Score notes (0s, ?s, and judgment calls):**
- **A01–A09 = 0 / F01–F09 = 0**: positive evidence of absence, not mere non-mention — the complete published OpenAPI surface (172 paths) and full docs index contain zero sweepstakes/promotion/prize/winner/ledger/balance/loyalty/coupon/entitlement constructs [PERSONA-035]. A10 = 1 because TIN/IRS database verification is a genuine component of winner tax workflows, though no tax-reporting product exists.
- **C09 = 0** (reasoned inference, no claim ID): the data model has no legal-source/citation concept anywhere in templates, workflows, reports, or cases; the fully-enumerated API and docs would surface such a feature if it existed.
- **H10 = 0**: keyword scan of full spec/docs shows no Terraform/IaC support; configuration is dashboard-managed [PERSONA-035].
- **G09 = ?**: no public SLA documentation located; enterprise SLAs may exist contractually but are unverified (marketing site bot-blocked).
- **I03 = 1** (reasoned, no claim): Persona is not sold to marketing; the nearest touchpoint is conversion-rate optimization of verification flows — peripheral.
- **B08 = 1**: conditional routes are explicitly ordered within a flow graph (deterministic), but no rule-priority/conflict-resolution system across independent rules exists — labeled inference from the documented workflow model [PERSONA-002].
- **B04/B06/B07/E09/E10 = 4**: core-product capabilities documented in official docs (allow/deny/review lifecycle; custom schemas on transactions/cases/accounts; Accounts as the platform spine; Cases product depth incl. SAR; Marketplace normalization).
- **I07/I08/I09 scoring convention**: scored as degree of fit/burden (2 = moderate dependency/cost), with reasoning in Sections 9 and 11.

## 13. White-space implications

**1. Which proposed Promotion OS capabilities are already solved?** Identity/geo/fraud signal supply and normalization (J06 substantially — Marketplace + unified report/event model); customer-configurable decision orchestration with allow/deny/review outputs and reason codes at check level; versioned decision configuration with per-decision version pinning; human review/case orchestration incl. SLAs and regulator filing (SARs); operational audit logging; enterprise governance basics (RBAC/SSO/SCIM, environments, staged rollouts). [PERSONA-002–016, -023–027]

**2. Which are partially solved?** Evidence-grade reconstruction (J07: assembly across objects, short log windows, no as-of replay); impact analysis (J04: live percentage rollouts with control groups, but no pre-deployment simulation against historical traffic); policy packs (J09: technical solution bundles + Connect network, no legal content); jurisdiction logic (C01: country/geo lists and conditionals, customer-authored); lifecycle control plane (J10: strong config lifecycle, no regulatory semantics); cross-product action authorization (J05: Transactions can model arbitrary actions but decisioning is async and identity-framed).

**3. Which appear unsolved?** Regulatory rules as vendor-maintained executable content with legal-source provenance (C09/C10/J01 content half); counsel-as-approver / legal-to-production gates (C08, J02, J03 — no maker-checker on publishing at all); regulatory change monitoring (C06); effective-dated/temporal legal rules (C04); synchronous low-latency authorization (B02/B03); decision replay (B10/J08); everything promotion-specific (A block) and ledger/entitlement provenance (F block).

**4. Could this vendor add the missing capability easily?** The *software* pieces — approval gates on publishing, longer evidence retention, a sync decision API, effective-dated versions — are incremental for a $2B-funded platform with this version/RBAC infrastructure (inference: publishing approval is a natural extension of existing roles + drafts). The *content* pieces (maintained jurisdiction rule libraries with legal provenance, counsel network) are a different business requiring legal editorial operations; nothing indicates appetite — their stated direction is agentic-AI identity. Promotion administration and ledgers are far off-strategy. [PERSONA-031, -038]

**5. Could a customer assemble it using this vendor + internal engineering?** Substantially, for the identity-adjacent slice: a sophisticated team could model regulated actions as Transactions, encode jurisdiction logic in Workflows conditionals + country/geo Lists, gate publishing via role permissions, route edge cases to Cases, and pull evidence via APIs/PDFs. Gaps they cannot assemble on Persona: synchronous in-transaction authorization, legal content and provenance, counsel approval semantics, historical as-of replay, and any promotion/ledger constructs — those would remain internal engineering + outside counsel. The async model and dashboard-authored logic also make Persona awkward as the system-of-record for non-identity policy.

**6. What would make a customer buy a separate product instead?** (a) Needing **sub-second synchronous authorization** inside transaction paths; (b) wanting **vendor-maintained jurisdictional rule content with legal provenance and change monitoring** rather than authoring rules themselves; (c) needing **counsel-in-the-loop deployment governance** with evidentiary approval trails; (d) promotion/incentive domain objects (entries, prizes, AMOE, ledgered value) that Persona will not model; (e) desire for policy-as-code/IaC and long-horizon decision replay for regulator defense; (f) cost — running high-volume non-identity decisions through per-service-priced identity infrastructure is economically wrong.

## 14. Replacement risk

**HIGH.**

Persona already owns most of the *machinery* the proposed product needs — configurable rules orchestration, versioned deployment with rollouts, case management, signal normalization across ~90 vendors, audit logging, enterprise governance — plus 4,000+ customers, $100M+ ARR, and $200M of fresh capital. If "regulatory action authorization" emerged as a lucrative category, Persona could plausibly ship the software gaps (sync decision API, approval gates, effective dating) within its existing platform, and its Solution Library + Connect show it knows how to package reusable configurations and network effects. Two factors keep this at HIGH rather than EXTREME: (1) everything in Persona orbits *identity* — promotion administration, ledger provenance, and legal content are off-architecture and off-strategy (current strategic focus is agentic-AI identity); (2) maintained legal content with counsel workflows is an editorial/services muscle Persona has never built — it deliberately avoids making legal claims even in its KYC solution. [PERSONA-019, -029, -031, -035, -038]

## 15. Adjacent discoveries

Companies/substitutes encountered that merit consideration:

1. **Alloy (alloy.com)** — identity risk *decisioning/orchestration* layer over 200+ data vendors with policy workflows for banks/fintechs; the closest architectural substitute for the J05/J06 "normalize vendors + decision" slice, and more decision-engine-shaped than Persona. [PERSONA-033]
2. **Unit21 (unit21.ai)** — no-code fraud/AML risk-ops platform (rules engine + alert/case management + SAR filing); directly substitutes the Cases/Workflows slice for risk-ops buyers and shows rule-authoring UX for non-engineers. [PERSONA-033]
3. **Sumsub** — full-cycle verification + workflow builder + case management, aggressive on jurisdiction-specific compliance packaging (e.g., per-country age/KYC rule presets); worth checking for "regulatory content as product" behavior.
4. **Sardine** — device/behavior-first fraud + compliance platform with rules engine and case management; overlaps the E-block plus real-time risk scoring at transaction time (closer to synchronous decisioning than Persona).
5. **Footprint (onefootprint.com)** — newer IDV + onboarding platform with rules-based playbooks and vaulting; evidence that the configurable-verification-orchestration pattern is being commoditized downmarket.
6. (Also noted: **Middesk**, **SentiLink**, **Prove**, **Mastercard Identity**, **LexisNexis** appear *inside* Persona's marketplace — they are simultaneously suppliers and partial substitutes for specific signal slices.) [PERSONA-027]

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/10_persona.jsonl` (42 records). Summary table:

| Claim ID | Claim (abbreviated) | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| PERSONA-001 | Core objects: Inquiry, Verification, Account, Report, Case, Workflow; KYC/age/fraud/T&S use cases | docs.withpersona.com/how-persona-works | official-doc | 2026-08-18 | HIGH |
| PERSONA-002 | Workflow triggers (event/API/scheduled) + conditional logic over inquiry/report/case/account/graph/3rd-party criteria; API trigger schemas | docs.withpersona.com/workflows | official-doc | 2026-08-18 | HIGH |
| PERSONA-003 | Action library: approve/decline/review, create case, run report, Evaluate Code (JS), signed HTTPS, redact, CRM updates | docs.withpersona.com/workflows | official-doc | 2026-08-18 | HIGH |
| PERSONA-004 | Inquiry lifecycle: approved/declined/needs_review via automation, manual, or API; events per transition | docs.withpersona.com/model-lifecycle | official-doc | 2026-08-18 | HIGH |
| PERSONA-005 | Verification checks: per-check required/non-required config; user-behavior vs fraud types; CSM-assisted default tuning | docs.withpersona.com/verification-checks | official-doc | 2026-08-18 | HIGH |
| PERSONA-006 | Per-check API output: name/status/reasons/requirement/metadata (reason codes) | docs.withpersona.com/api-reference/verifications/retrieve-a-verification | official-doc | 2026-08-18 | HIGH |
| PERSONA-007 | Verification types incl. gov ID/NFC, selfie, document, database, AAMVA, eCBSV, TIN(IRS), phone-carrier, Serpro | docs.withpersona.com/verification-types | official-doc | 2026-08-18 | HIGH |
| PERSONA-008 | Reports: watchlist/PEP/adverse media/email/phone risk/address/business; templates; match-dismiss lifecycle | docs.withpersona.com/reports | official-doc | 2026-08-18 | HIGH |
| PERSONA-009 | Continuous monitoring 1–365 days; auto-halt on match; Growth/Enterprise | help.withpersona.com/articles/7LRMBbxLshF7sCcLhfhwF4/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-010 | Cases: configurable UI, SLAs, queues, analytics, automations; full CRUD/assign/status/search API; case events | docs.withpersona.com/cases | official-doc | 2026-08-18 | HIGH |
| PERSONA-011 | Case templates: custom field schemas (write_once, redaction-policy, required), custom resolutions; statuses typed initial/intermediate/end | docs.withpersona.com/api-reference/case-templates/retrieve-a-case-template | official-doc | 2026-08-18 | HIGH |
| PERSONA-012 | Case Actions: workflow-backed one-click ops ("anything a workflow or custom code can do") + system actions (queues, SLA deadlines, redaction) | help.withpersona.com/articles/3QokSTOfV7ZC7hNDPQ5HnT/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-013 | AML case mgmt + SAR: customizable status progressions, SLAs, checklists; SAR XML export or direct FinCEN SDTM e-filing; sar.* events | help.withpersona.com/articles/3PQYXlkWnkxRyWmAijjVux/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-014 | Case status governance: conditional status-switcher lockout; required reason tags per status change | help.withpersona.com/articles/2P8swNyjlHKiZPDCy5gnAu/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-015 | Workflow versioning: drafts → immutable versions → history → revert; percentage rollouts (treatment/control); runs record version | help.withpersona.com/articles/6YBOe6MD4R9WrwEuQND6jA/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-016 | Inquiry template versioning; every inquiry permanently pinned to its template version; compare and revert | help.withpersona.com/articles/2Luxrdu3Cdg6pcecKBJxvs/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-017 | Graph link analysis; parameterized query templates; API execution; graph data usable in workflow conditionals | docs.withpersona.com/graph | official-doc | 2026-08-18 | HIGH |
| PERSONA-018 | Lists: IP/geo/country/gov-ID/name/phone/email/fingerprint/face; workflow auto-approve/decline on match | docs.withpersona.com/lists | official-doc | 2026-08-18 | HIGH |
| PERSONA-019 | Transactions: custom-schema event objects, custom statuses, workflow-driven; API-only integration (Enterprise, gated) | docs.withpersona.com/transactions | official-doc | 2026-08-18 | HIGH |
| PERSONA-020 | API platform: dated versions per key/webhook, idempotency, rate limits + quotas, API logs (2wk) + request IDs, OpenAPI (172 paths) | docs.withpersona.com/versioning | official-doc | 2026-08-18 | HIGH |
| PERSONA-021 | Webhooks: HMAC, filters, PII blocklists, OAuth outbound, retries, simulation, per-webhook versioning, 30-day retention | docs.withpersona.com/webhooks | official-doc | 2026-08-18 | HIGH |
| PERSONA-022 | Sandbox: force pass/fail, simulate-action + simulated-data endpoints; production via sales | docs.withpersona.com/environments | official-doc | 2026-08-18 | HIGH |
| PERSONA-023 | User Audit Logs: 6 months, API-accessible; user/IP/UA/params/impersonator | docs.withpersona.com/api-reference/user-audit-logs/list-all-user-audit-logs | official-doc | 2026-08-18 | HIGH |
| PERSONA-024 | RBAC (org + environment scopes, constraints), SAML SSO, SCIM, 2FA, multi-org SSO; SSO Growth+ | help.withpersona.com/articles/Ge16TE6VaYZGWVNe2b9cx/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-025 | Redaction on all objects (incl. biometrics), conditional/field-level via workflows, attribute blocklists, automated retention policies (setup-assisted) | docs.withpersona.com/openapi (accounts redaction description) | official-doc | 2026-08-18 | HIGH |
| PERSONA-026 | Device/network intel in schema: is-vpn/is-proxy/is-tor/is-datacenter, proxy-type, threat-level, GPS + IP geo; inquiry fraud signals (bot score) | docs.withpersona.com/inquiry-signals (+ OpenAPI) | official-doc | 2026-08-18 | HIGH |
| PERSONA-027 | Marketplace ~90+ integrations: LexisNexis, Mastercard, Prove, SentiLink, Chainalysis, TRM, Nova Credit, MX, Equifax, Middesk, LLMs (Anthropic, Google) | help.withpersona.com/marketplace-and-3rd-party-integrations/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-028 | Connect: cross-org KYC/KYB reuse via scoped share tokens | docs.withpersona.com/connect | official-doc | 2026-08-18 | HIGH |
| PERSONA-029 | Solution Library packs (KYC, KYC+AML, KYC+Age…); KYC = template + 2 workflows + case template; no legal citations | help.withpersona.com/solutions/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-030 | Pricing: Essential $250/mo + $1.50/service; Growth/Enterprise custom; 60-day trial; documented feature gating | help.withpersona.com/articles/6oZbzp7jb7AWGClF5vpY3K/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-031 | $200M Series D @ $2B (Apr 2025); $100M+ ARR 2024; 4,000+ businesses; OpenAI/LinkedIn/Block/Robinhood/Etsy/Twilio | prnewswire.com (…302442649.html) | official-marketing | 2026-08-18 | MEDIUM |
| PERSONA-032 | SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, FERPA, Kantara, ACCS | withpersona.com/security/ (via snippets) | official-marketing | 2026-08-18 | MEDIUM |
| PERSONA-033 | Contrary Research: ~5s decisions; competitors Socure/Jumio/Onfido/Alloy/Unit21; low switching (~3mo); "AWS of identity" | research.contrary.com/company/persona | third-party | 2026-08-18 | MEDIUM |
| PERSONA-034 | Async decisioning model; docs recommend polling for real-time; no synchronous decision endpoint in full API (labeled inference) | docs.withpersona.com/webhooks | official-doc | 2026-08-18 | HIGH |
| PERSONA-035 | Keyword scan of full OpenAPI + docs: zero ledger/promotion/prize/loyalty/entitlement constructs; no IaC/Terraform | docs.withpersona.com/openapi.json | official-doc | 2026-08-18 | HIGH |
| PERSONA-036 | Org-level workflows span all environments (July 2023 migration); enterprise multi-BU support | help.withpersona.com/articles/5HxSRhTO1UkxuboAUu4TDz/ | official-doc | 2026-08-18 | HIGH |
| PERSONA-037 | Age verification packaged (KYC+Age solution; laws-by-industry content; ACCS cert) | withpersona.com/blog/age-verification-laws-by-industry/ | official-marketing | 2026-08-18 | MEDIUM |
| PERSONA-038 | AI-agent events: agent-conversation.*, case.agent-reviewed; LLM marketplace integrations | docs.withpersona.com/events | official-doc | 2026-08-18 | HIGH |
| PERSONA-039 | Accounts: persistent entity state, custom types/fields/statuses, relations, consolidation, importers | docs.withpersona.com/accounts | official-doc | 2026-08-18 | HIGH |
| PERSONA-040 | Verification inputs frozen at submission; investigation lock/unlock endpoints | docs.withpersona.com/verification-lifecycle | official-doc | 2026-08-18 | HIGH |
| PERSONA-041 | Evidence exports: Print Inquiry/Report/Verification PDF; case export; report history | docs.withpersona.com/api-reference/inquiries/print-an-inquiry-pdf | official-doc | 2026-08-18 | HIGH |
| PERSONA-042 | SDKs: JS v5 (+React/Vue), iOS v3, Android v2, RN v2; Relay server SDK/gateway/edge workers | docs.withpersona.com/mobile-sdks | official-doc | 2026-08-18 | HIGH |

## 17. Verdict

**MAJOR OVERLAP**

Persona is not a promotion-compliance vendor and sells no regulatory content, so it is not a direct threat to the Promotion OS *thesis as stated*. But it already operates most of the proposed machinery at enterprise scale: customer-configurable rule orchestration with allow/deny/review outputs and reason codes, immutable policy versioning with per-decision pinning and staged rollouts, deeply customizable case management through regulator filing (FinCEN SARs), cross-vendor signal normalization across ~90 integrations, and mature audit/logging — all with $100M+ ARR, marquee customers, and $200M of fresh capital. What it lacks maps exactly to the hypothesis's distinctive squares: legal content with provenance, counsel-approval deployment gates, regulatory change monitoring, synchronous low-latency authorization, historical replay, and all promotion/ledger domain objects. Any Promotion OS pitch must assume Persona (or a customer building on Persona) can cover the identity, orchestration, and evidence layers, and must differentiate on the legal-content and authorization layers Persona avoids.

---
*Report generated from research conducted 2026-08-18. All capability scores trace to the evidence ledger at `outputs/evidence/10_persona.jsonl`.*
