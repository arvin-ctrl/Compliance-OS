# Company Report — Socure

Researcher: Research Agent 11 (Socure)
Date: 2026-08-18
Category: Identity / fraud / compliance
Manager: Manager C

## 1. Executive summary

Socure is an AI-driven identity verification, fraud prevention, and compliance decisioning company. Its historical core product is **ID+**, a single multi-module REST API (`/api/3.0/EmailAuthScore`) that returns identity verification (Socure Verify/KYC), fraud scores (Sigma Identity, Sigma Synthetic, First-Party), email/phone/address risk scores, document verification (Predictive DocV), Global Watchlist screening, device/behavior signals (Digital Intelligence), and a **Decision module** that converts module outputs into accept/reject/refer/resubmit/review outcomes with reason codes [SOCURE-002, SOCURE-003, SOCURE-036].

In October 2024 Socure acquired Effectiv for $136M and in February 2025 launched **RiskOS**, a no-code decisioning and orchestration platform: visual workflow builder, decision rules, third-party data integrations, entity/velocity state, case management, champion/challenger testing, audit logs, and compliance report generation [SOCURE-030]. Socure claims 3,000+ customers including Citi, Capital One, Chime, SoFi, DraftKings, PrizePicks, Uber, 18–19 of the top 20 US banks, 13 US states, and two federal agencies [SOCURE-001, SOCURE-040]. Buyers are fraud/risk, compliance, and product/engineering teams at regulated enterprises. The job it is hired to do: decide, in real time, whether an identity-bearing event (account opening, login, transaction) should be allowed, denied, or reviewed — and prove why.

Answer to the core question (how broad is identity decisioning and regulatory workflow support?): decisioning breadth is now very large — RiskOS is a general-purpose risk decisioning control plane (workflow versioning, backtesting, shadow experiments, decision path traces, case ops, watchlist policy configuration, compliance reporting). But its regulatory support is **infrastructure, not content**: Socure explicitly "remains neutral on regulatory policy and doesn't decide which rules apply to your business" [SOCURE-028]. Customers author their own jurisdiction rules on Socure's rails.

## 2. Product architecture

Two generations coexist:

**ID+ (module API).** INPUT: consumer PII (name, address, DOB, SSN, email, phone, IP, device session, document images) + a `modules` array selecting which products to run. DECISION/PROCESS: each module runs against Socure's data network (400+ sources; identity graph with claimed 96.4% identity recurrence) and ML models; the optional Decision module applies configurable "Decision Logic" business rules over module outputs. OUTPUT: per-module scores (0.001–0.999) with model name+version, I/R reason codes, field validations with source attribution, watchlist matches, and a single decision outcome (accept/reject/refer/resubmit/review) [SOCURE-002, SOCURE-003, SOCURE-005, SOCURE-036, SOCURE-038].

**RiskOS (workflow platform, from Effectiv).** INPUT: an event posted to `/api/evaluation` (consumer, business, device, transaction data, plus arbitrary `custom` JSON fields). DECISION/PROCESS: a versioned no-code **workflow** executes sequentially — Input validation → Enrichment steps (Socure modules and third-party partners) → Condition/Transformation steps → Rule Scorecards → Decision Rules (first-match, top-down) → Manual Review routing; entity aggregations supply velocity/state; asynchronous steps (DocV, OTP) pause the evaluation [SOCURE-006, SOCURE-008, SOCURE-021, SOCURE-022]. OUTPUT: `decision` (ACCEPT/REJECT/REVIEW) + `status` (CLOSED/ON_HOLD) + `tags` + enrichment data and reason codes; async results and case decisions arrive by webhook; unresolved evaluations become **cases** in queues for human disposition, whose outcome is returned via API/webhook [SOCURE-005, SOCURE-012, SOCURE-014]. Every evaluation gets a unique Evaluation ID linked to an Application ID; a **Decision Path Trace** records each executed step for audit [SOCURE-011, SOCURE-042].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Socure Verify (KYC) | CIP/KYC identity verification against 400+ sources; field validations, source attribution; claims 98–99% auto-approval | Compliance | Core | SOCURE-005, SOCURE-026 |
| Sigma Identity / Synthetic / First-Party Fraud | ML fraud scores 0.001–0.999 with model name+version and reason codes | Fraud/risk | Core | SOCURE-038 |
| Email/Phone/Address RiskScores | Per-attribute risk scores and signals | Fraud/risk | Core | SOCURE-002, SOCURE-044 |
| Predictive DocV (+ Selfie, mDL) | Document + selfie verification, liveness, deepfake detection; 0.92s P95 claim | Fraud/compliance | Core | SOCURE-029, SOCURE-041 |
| Global Watchlist Screening with Monitoring | Sanctions/enforcement (1,400+ lists), 2.4M PEP profiles, adverse media; configurable match policies; continuous monitoring with webhooks; 1-step/2-step review workflows; audit trail | Compliance (AML) | Core | SOCURE-023, SOCURE-024, SOCURE-025 |
| Decision module (ID+) | Accept/reject/refer/resubmit/review from configurable Decision Logic | Fraud/risk | Core | SOCURE-003, SOCURE-036 |
| RiskOS workflows + Decision Rules | No-code versioned workflows; rules; experiments; backtesting; entity aggregations | Fraud/risk/compliance | Core (platform) | SOCURE-006–010, SOCURE-022 |
| RiskOS Case Management | Queues, statuses, dispositions, decision path trace, re-evaluation, fraud feedback | Fraud ops/compliance ops | Core | SOCURE-012, SOCURE-011, SOCURE-042 |
| Partner Ecosystem | 14 documented third-party enrichments (Experian, Middesk, Thomson Reuters Clear, SAM.gov, ICIJ…); reseller or bring-your-own-contract; 50+ claimed at launch, 200+ claimed on marketing site | Risk/eng | Add-on | SOCURE-034, SOCURE-030, SOCURE-004 |
| Age Assurance | Passive (device/phone/email) → active (selfie estimation, doc+selfie) waterfall; returns ACCEPT/REJECT + age18/21/25Plus booleans only | Compliance/product | Growing solution | SOCURE-028, SOCURE-029 |
| Business Onboarding (KYB), Transaction Monitoring, Credit Underwriting | Effectiv-derived solutions incl. SAR/CTR/UAR report generation claim | Compliance | Newer add-ons | SOCURE-030, SOCURE-046 |
| Account Intelligence / Bank Account Verification | Bank account status/ownership signals | Payments risk | Add-on | SOCURE-046, SOCURE-044 |
| RiskOS AI Suite (Oct 2025) | Rule Writing Assistant (NL→rules), Workflow Change Summary (audit docs), Case Review Assistant, GenAI Explainability, BI Agent, MCP Server | Risk/compliance ops | Add-on | SOCURE-039 |
| Socure Launch | Self-serve pre-configured onboarding workflows, sandbox signup | Startups/eng | Packaging | SOCURE-035 |

## 4. API / developer capability

- **APIs:** ID+ `POST /api/3.0/EmailAuthScore` with `modules` array [SOCURE-036]; RiskOS `POST /api/evaluation` (OpenAPI spec referenced in docs); case decision integration APIs; batch CSV evaluations; portfolio scrub via SFTP [SOCURE-006, SOCURE-013, SOCURE-047].
- **SDKs:** DocV iOS 5.4.2 / Android 5.4.7 / React Native 5.2.8 / Web 5.0.0; Digital Intelligence iOS/Android/Web/React Native — capture/device SDKs, not general platform clients [SOCURE-044].
- **Webhooks:** documented envelope (`event_id`, `event_at`, `event_type`, `data` + customer metadata); events: `evaluation_completed`, `decision_update`, case lifecycle, `monitored_search_updated`; HTTPS POST with Basic/Bearer/OAuth 2.0 auth; retries with backoff [SOCURE-014, SOCURE-025].
- **Sandbox:** free self-serve sandbox (riskos.sandbox.socure.com), 10 TPS / 1,000 req/day; production keys start blocked until activation; DocV sandbox test scenarios documented [SOCURE-013, SOCURE-035].
- **Rules engine:** RiskOS workflow steps + Decision Rules (first-match), Rule Scorecards (−100..100), condition groups, transformations, reason-code-list conditions [SOCURE-006, SOCURE-008, SOCURE-020].
- **Synchronous decisioning:** "most evaluations return synchronously, while longer-running checks are delivered asynchronously through webhooks" [SOCURE-013]; marketing claims <150ms average workflow execution and >1,000 QPS [SOCURE-004].
- **Latency claims:** <150ms avg workflow execution (marketing); 0.92s P95 for ID+selfie decisions (marketing) [SOCURE-004, SOCURE-029].
- **Versioning:** ID+ path-versioned (`/api/3.0/`); model scores carry name+version "for auditing"; RiskOS endpoint versioning not documented [SOCURE-036, SOCURE-038].
- **Idempotency:** not documented anywhere found (unresolved).
- **Rate limits:** fully documented with `X-RateLimit-*` headers, 429 + `X-Retry-After`; account-level limits shared across sub-account keys [SOCURE-013].
- **Integration model:** direct API, hosted flows (Socure-hosted UX), or SDK capture + server API; MCP server for Cursor/Claude Code integration assistance; optional mTLS, JWE/JWS payload encryption, IP allowlisting [SOCURE-035, SOCURE-045, SOCURE-033].

## 5. Rules / decision model

- **Arbitrary attributes:** yes — `custom` JSON objects at five request levels are "exposed as variables in your workflow logic" (e.g. `$data.custom.origination_channel == "mobile_app"`); recommended ≤20–25 fields; stored but not indexed/searchable in cases [SOCURE-021].
- **Customer/user state:** yes — standard and custom entities with aggregations (Count, Distinct Count, Sum, Avg, Min, Max, First/Last Seen) over windows from 1 minute to 180 days or lifetime [SOCURE-022]; SocureID identity resolution and cross-customer identity graph on Socure's side.
- **Reason codes:** yes — I/R-prefixed codes per enrichment; reusable Reason Code Lists usable in conditions; codes returned in API responses and documented for audit logging [SOCURE-019, SOCURE-020, SOCURE-005].
- **Allow/deny/review output:** yes — ACCEPT/REJECT/REVIEW (+ Resubmit/Cancel/Refer variants) with `status` and `tags` [SOCURE-005, SOCURE-008, SOCURE-003].
- **Simulate policies:** yes — backtesting re-executes historical records against a draft and charts original-vs-updated decisions; custom JSON payload tests; champion/challenger **shadow experiments on 100% of live traffic** where only the champion's decision is returned [SOCURE-010, SOCURE-009]. Limitations: async workflows not testable (relief targeted Q4 2025), test results not exportable, one experiment at a time [SOCURE-010, SOCURE-009].
- **Replay decisions:** partially — Decision Path Trace lets reviewers "replay the flow of data through a workflow from a Case View" for any past decision [SOCURE-012, SOCURE-011]; re-evaluation runs a *fresh* evaluation (new Evaluation ID linked by Application ID) rather than replaying under the historical policy [SOCURE-042].
- **Version policies:** yes for workflows — Draft/Published/Live states, major/minor versions, version history, restore, archive; only one live workflow per use case [SOCURE-007]. Gaps: watchlist policies and reason code lists are not versioned; reason-code-list edits take immediate effect "without creating a new workflow version" and "don't generate audit trail entries" [SOCURE-024, SOCURE-020].
- **Deploy rules independently of app code:** yes — no-code Workflow Editor; publishing gated by Move-to-Live permission [SOCURE-006, SOCURE-007].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance:** none. Nothing in the full documentation index covers sweepstakes, contests, official rules, AMOE, winner handling, or prize tax [SOCURE-043]. Gaming customers (DraftKings, PrizePicks) use Socure for KYC/age/fraud at onboarding, not promotion administration [SOCURE-040, SOCURE-041].
- **Generic regulatory workflow:** meaningful — KYC/CIP programs ("Exceed CIP/KYC requirements", SEC 17Ad-17, FACTA Red Flags claims), AML watchlist screening/monitoring with 1-step/2-step compliance review workflows, compliance roles (Officer/Supervisor/Analyst), compliance report generation, claimed SAR/CTR/UAR report automation [SOCURE-026, SOCURE-023, SOCURE-015, SOCURE-018, SOCURE-030].
- **Jurisdiction restrictions:** infrastructure only. Age Assurance documents that "Socure remains neutral on regulatory policy and doesn't decide which rules apply to your business"; customers configure state rules, thresholds, and escalation paths themselves [SOCURE-028]. Watchlist policies support country filters [SOCURE-024]. No jurisdiction rule *content* is shipped.
- **Location verification:** weak relative to GeoComply — IP/device network risk signals ("risky networks", bots, emulators) [SOCURE-005]; no compliance-grade geofencing product.
- **Legal content/rules:** none shipped; the closest analog is the watchlist library (1,400+ lists, 2.4M PEPs) — regulatory *data*, not encoded law [SOCURE-023].
- **Regulatory monitoring:** limited to watchlist source-list change detection (Source List Audit Log; monitoring alerts on list adds/updates/removals) — not statute/regulation tracking [SOCURE-018, SOCURE-025].
- **Change management:** workflow lifecycle with versions/restore, audit logs of workflow and settings changes, AI Workflow Change Summary for audit documentation [SOCURE-007, SOCURE-017, SOCURE-039].
- **Counsel approval:** no counsel-specific workflow. Permission-gated publishing (Move to Live) and compliance-officer case approvals exist and could be *adapted* to put a lawyer in the loop (inference) [SOCURE-007, SOCURE-015].
- **Historical policy state:** workflow version history is viewable/restorable; audit reports capture settings before/after; but watchlist policy changes "apply to all future evaluations" with no retroactive view, and there is no documented "evaluate as of date X" capability [SOCURE-007, SOCURE-018, SOCURE-024].

## 7. Audit / evidence

Can a customer reconstruct:

- **Exact inputs?** Largely yes — compliance Transaction Details reports include submitted fields and module outputs; case views show submitted data and enrichment results; `data_enrichments` returned in API [SOCURE-018, SOCURE-005, SOCURE-011].
- **Exact rule/policy?** Yes for the executed path — Decision Path Trace records "each step that executed during the evaluation," condition outcomes, branches taken, and the final decision, positioned "for internal governance or external audits" [SOCURE-011].
- **Exact version?** Partially — model scores return name+version "for auditing" [SOCURE-038]; workflow versions are tracked [SOCURE-007]; but an explicit decision→workflow-version linkage in the trace is not documented, and reason-code-list edits bypass versioning and audit trails [SOCURE-020].
- **Exact output?** Yes — decision, status, tags, scores, reason codes persisted per Evaluation ID; case outcomes delivered by API/webhook [SOCURE-005, SOCURE-012, SOCURE-042].
- **Exact timestamp?** Yes — event timestamps in webhooks, report date/processing-time fields, audit-log timestamps [SOCURE-014, SOCURE-018, SOCURE-017].
- **Human approvals?** Yes — case statuses, assignments, comments, dispositions; `decision_update` webhook; Account Activity audit report (user, timestamp, IP, action); two-step compliance review [SOCURE-012, SOCURE-014, SOCURE-018, SOCURE-023].
- **Source/legal authority?** Data-source level only — `fieldSourceAttribution` (e.g. SSA, USPS), watchlist Source List and source documentation [SOCURE-005, SOCURE-018, SOCURE-023]. No mapping of rules to statutes/citations.

Overall: strong operational auditability (audit logs, before/after settings change logs, exportable CSV compliance reports, watchlist "complete audit trail to evidence compliance decisions") with two documented integrity gaps (unversioned/unaudited reason-code-list edits; policy changes not replayable retroactively) [SOCURE-017, SOCURE-018, SOCURE-023, SOCURE-020, SOCURE-024].

## 8. Enterprise readiness

- **SSO/RBAC:** SAML SSO guides for Okta, Microsoft Entra ID, Google Workspace, PingOne, IBM Security Verify, Salesforce [SOCURE-016]. System-defined roles with PII segregation (Developer role has no PII access), workflow-publish rights, and dedicated Compliance Officer/Supervisor/Analyst roles [SOCURE-015].
- **Multitenancy/multi-brand:** primary account + sub-accounts; Direct Customer and Channel Partner account models; sub-account keys share account-level rate limits [SOCURE-015, SOCURE-013].
- **Environments:** sandbox and production with separate endpoints and limits [SOCURE-013].
- **Security certifications:** FedRAMP Moderate Authorized, GovRAMP Moderate, Kantara-certified for NIST SP 800-63 IAL (per authorized distributor Carahsoft) [SOCURE-032]; ISO 27000-series certifications announced 2018; TLS 1.2+/1.3, optional JWE/JWS payload encryption, mTLS, IP allowlisting [SOCURE-033]. SOC 2 status not verified in public sources during this research.
- **SLA:** no public SLA found; third-party buyer guidance treats SLAs/service credits as negotiated contract terms [SOCURE-037].
- **Support/professional services:** RiskOS Enterprise is "fully customized… with advanced controls and guidance" (services-supported); Socure Launch is self-serve [SOCURE-004, SOCURE-035].
- **Customer scale:** 2.7B verification requests in 2024 (370M unique identities); 2,800→3,000+ customers; 18–19 of top 20 US banks; Gartner MQ IDV Leader 2024; 13 states, 30+ state agencies, 2 federal agencies [SOCURE-031, SOCURE-001, SOCURE-040].

## 9. Commercial model

- **Pricing:** not public. Third-party buyer research reports attempt-based (per-verification) pricing that "can escalate quickly when retry rates are high," plus manual-review/premium-support cost sensitivity [SOCURE-037]. Sandbox is free [SOCURE-013].
- **Likely buyer:** fraud/risk leadership and compliance (BSA/AML, KYC) at banks, fintechs, crypto, gaming, marketplaces, public sector; engineering as implementer [SOCURE-001, SOCURE-046].
- **Implementation burden:** low for Launch pre-configured workflows/hosted flows ("start building in minutes"); higher for enterprise custom RiskOS deployments — third-party reviews cite implementation complexity [SOCURE-035, SOCURE-037].
- **Sales motion:** enterprise sales-led; self-serve Launch wedge for startups; Carahsoft channel for government [SOCURE-004, SOCURE-035, SOCURE-032].
- **Large customers:** extensive named logos (Citi, Capital One, Chime, SoFi, Robinhood, DraftKings, PrizePicks, Uber, Gusto, Poshmark) and top-bank penetration claims [SOCURE-001, SOCURE-040].

## 10. Strengths

- Category-leading identity/fraud signal quality at massive scale (2.7B requests/yr; identity graph with claimed 96.4% recurrence; Gartner MQ Leader) [SOCURE-031, SOCURE-030].
- A genuine decisioning control plane post-Effectiv: no-code versioned workflows, first-match decision rules, entity/velocity state, backtesting, live shadow experiments, case management with decision path traces [SOCURE-006–012, SOCURE-022].
- Compliance operations depth: watchlist screening + continuous monitoring with configurable match policies, 1-step/2-step review, compliance roles, exportable audit/compliance reports, claimed SAR/CTR/UAR generation [SOCURE-023–025, SOCURE-015, SOCURE-018, SOCURE-030].
- Vendor orchestration: third-party enrichments in the same workflow, with a reseller contracting option ("only need to sign an agreement with Socure") [SOCURE-034].
- Public-sector-grade assurance (FedRAMP Moderate, Kantara NIST 800-63 IAL2) — unusual among fraud vendors [SOCURE-032].
- Developer experience praised by buyers (API ergonomics, docs); free self-serve sandbox; documented rate limits and webhooks [SOCURE-037, SOCURE-013, SOCURE-014].

## 11. Weaknesses / constraints

- **No regulatory content.** Socure documents explicit neutrality: it does not decide which rules apply; customers must author jurisdiction/state rules themselves [SOCURE-028]. No statute-linked rule provenance anywhere.
- **Governance gaps in policy artifacts:** reason-code-list edits change live behavior with no new version and no audit-trail entry [SOCURE-020]; watchlist policy changes are forward-only with no retroactive reconstruction [SOCURE-024]; decision→workflow-version linkage not documented (inference from absence in Decision Path Trace docs) [SOCURE-011].
- **Testing limits:** backtesting unavailable for workflows with async steps; test results not exportable; one experiment at a time [SOCURE-010, SOCURE-009].
- **Identity-event-centric:** the decision model is organized around identities/accounts/transactions; nothing addresses non-identity regulated actions, promotions, or entitlement/ledger semantics [SOCURE-043] (inference from full doc enumeration).
- **Opaque pricing; attempt-based cost escalation and implementation complexity reported by buyers** (third-party, LOW-MEDIUM confidence) [SOCURE-037].
- **US-centric data advantage**; international coverage exists but the flagship graph claims are US-population-based (inference; marketing emphasizes US banks/agencies) [SOCURE-001, SOCURE-031].

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,SOCURE-043
A02,0,SOCURE-043
A03,0,SOCURE-043
A04,0,SOCURE-043
A05,0,SOCURE-043
A06,0,SOCURE-043
A07,0,SOCURE-043
A08,0,SOCURE-043
A09,0,SOCURE-043
A10,0,SOCURE-043
B01,4,SOCURE-006;SOCURE-030;SOCURE-036
B02,4,SOCURE-005;SOCURE-013
B03,3,SOCURE-013;SOCURE-004;SOCURE-029
B04,4,SOCURE-003;SOCURE-005;SOCURE-008
B05,4,SOCURE-019;SOCURE-005;SOCURE-020
B06,3,SOCURE-021
B07,3,SOCURE-022;SOCURE-012
B08,3,SOCURE-008
B09,3,SOCURE-009;SOCURE-010
B10,3,SOCURE-011;SOCURE-012;SOCURE-042
C01,2,SOCURE-028;SOCURE-024
C02,2,SOCURE-046;SOCURE-035
C03,1,SOCURE-006;SOCURE-021
C04,?,
C05,3,SOCURE-007;SOCURE-018
C06,1,SOCURE-018;SOCURE-025
C07,3,SOCURE-010;SOCURE-009
C08,1,SOCURE-007;SOCURE-015
C09,1,SOCURE-023;SOCURE-005
C10,1,SOCURE-023;SOCURE-028
D01,3,SOCURE-042;SOCURE-014;SOCURE-018
D02,4,SOCURE-012;SOCURE-018
D03,2,SOCURE-038;SOCURE-007
D04,3,SOCURE-011;SOCURE-018
D05,3,SOCURE-012;SOCURE-018;SOCURE-015
D06,3,SOCURE-011;SOCURE-012
D07,3,SOCURE-018;SOCURE-030;SOCURE-023
D08,?,
D09,?,
D10,3,SOCURE-017;SOCURE-018;SOCURE-039
E01,4,SOCURE-026;SOCURE-031;SOCURE-002
E02,4,SOCURE-028;SOCURE-029
E03,3,SOCURE-005;SOCURE-026;SOCURE-044
E04,1,SOCURE-005
E05,3,SOCURE-044;SOCURE-005
E06,2,SOCURE-005;SOCURE-041
E07,4,SOCURE-038;SOCURE-002;SOCURE-031
E08,3,SOCURE-022;SOCURE-030
E09,4,SOCURE-012;SOCURE-023
E10,4,SOCURE-034;SOCURE-030;SOCURE-004
F01,0,SOCURE-043
F02,0,SOCURE-043
F03,0,SOCURE-043
F04,0,SOCURE-043
F05,0,SOCURE-043
F06,0,SOCURE-043
F07,0,SOCURE-043
F08,0,SOCURE-043
F09,0,SOCURE-043
F10,1,SOCURE-030
G01,3,SOCURE-015;SOCURE-013
G02,3,SOCURE-015
G03,3,SOCURE-016
G04,2,SOCURE-007;SOCURE-015;SOCURE-023
G05,3,SOCURE-013;SOCURE-035
G06,3,SOCURE-010;SOCURE-009
G07,3,SOCURE-007;SOCURE-017;SOCURE-039
G08,3,SOCURE-014
G09,?,
G10,3,SOCURE-032;SOCURE-033
H01,4,SOCURE-002;SOCURE-013;SOCURE-036
H02,3,SOCURE-044
H03,3,SOCURE-014
H04,3,SOCURE-013;SOCURE-035
H05,2,SOCURE-036;SOCURE-038
H06,?,
H07,3,SOCURE-013
H08,3,SOCURE-047;SOCURE-018;SOCURE-012
H09,1,SOCURE-018
H10,?,
I01,3,SOCURE-023;SOCURE-018;SOCURE-015
I02,3,SOCURE-035;SOCURE-045
I03,1,SOCURE-026
I04,4,SOCURE-001;SOCURE-031
I05,4,SOCURE-001;SOCURE-040;SOCURE-031
I06,3,SOCURE-035;SOCURE-013
I07,2,SOCURE-004;SOCURE-037
I08,3,SOCURE-012;SOCURE-031
I09,2,SOCURE-035;SOCURE-037
I10,1,SOCURE-037;SOCURE-013
J01,2,SOCURE-006;SOCURE-028
J02,1,SOCURE-007
J03,1,SOCURE-015;SOCURE-007
J04,2,SOCURE-010;SOCURE-009
J05,2,SOCURE-046;SOCURE-030
J06,3,SOCURE-034;SOCURE-030
J07,3,SOCURE-011;SOCURE-018;SOCURE-020
J08,2,SOCURE-011;SOCURE-024;SOCURE-042
J09,2,SOCURE-035;SOCURE-046;SOCURE-023
J10,2,SOCURE-007;SOCURE-039
```

**Scoring notes (0s, 1s, and ?s):**

- **A01–A10 = 0 (reasoned inference, labeled as such):** the complete RiskOS/DevHub documentation indexes (llms.txt trees enumerating every guide) contain no promotion, sweepstakes, contest, entry, drawing, prize, AMOE, or winner-tax functionality, and the product architecture (identity-event decisioning) has no promotion entities [SOCURE-043]. This is enumeration-based absence, not mere non-mention.
- **F01–F09 = 0 (same basis):** no wallet/ledger/balance/reward entities anywhere in the doc tree [SOCURE-043]. **F10 = 1:** transaction/payment event ingestion exists for monitoring (inference: consuming transaction streams is peripheral ledger *adjacency*, not ledger integration) [SOCURE-030].
- **C03 = 1 (inference):** workflows can branch on action/channel attributes via custom fields, but no legal action-rule content exists.
- **C04 = ?:** no evidence of effective-date/scheduled rule activation; only forward-only policy changes and recency filters found.
- **C06 = 1:** watchlist source-list change detection only; no statute/regulation monitoring.
- **C08 = 1 (inference):** Move-to-Live permission gating and compliance-officer case approvals could be assigned to counsel, but no counsel/policy-approval workflow is documented.
- **C09/C10 = 1:** provenance and libraries exist at the *data* level (source attribution, watchlist library), not the legal-authority level.
- **D08 = ?:** retention controls not documented in public docs reviewed. **D09 = ?:** no tamper-evidence features found; negative signal — reason-code-list changes generate no audit-trail entries [SOCURE-020].
- **E04 = 1 (inference):** IP/network risk signals only; no compliance-grade geolocation/geofencing.
- **G09 = ?:** no public SLA; buyer guidance implies negotiated SLAs [SOCURE-037].
- **H06 = ?:** idempotency keys not documented. **H10 = ?:** MCP server exists for AI-assisted integration [SOCURE-045], but no Terraform/IaC or config-as-code evidence either way. **H09 = 1:** Product Settings audit report exports configuration values as CSV, but it is reporting, not round-trippable config export [SOCURE-018].
- **I03 = 1 (inference):** conversion/growth messaging targets growth teams, but no marketing-buyer product exists. **I08 = 3 (inference from documented features):** switching costs derive from embedded workflows, case operations, and fraud-feedback loops that train Socure's models [SOCURE-012].
- **I10 = 1:** no public pricing; free sandbox documented; attempt-based pricing reported by third party.

## 13. White-space implications

1. **Already solved by Socure (for identity/fraud/AML domains):** real-time allow/deny/review decisioning with reason codes (J05's mechanics, B-row); cross-vendor signal orchestration inside one workflow with unified contracting (J06); decision evidence — path traces, audit logs, exportable compliance reports (much of J07); policy testing/impact analysis on historical traffic and live shadow mode (J04's mechanics); versioned no-code rule deployment (parts of J01/J10); case management and compliance review workflows.
2. **Partially solved:** historical replay (per-decision traces exist, but no "evaluate under the policy as of date X" and policy artifacts like watchlist policies/reason-code lists are unversioned) (J08); policy lifecycle control plane exists for *decision* policies but lacks legal-content awareness, effective dates, and counsel gates (J10, J02); reusable packs exist as pre-configured *risk* workflows and watchlist libraries, not legal policy packs (J09).
3. **Unsolved:** jurisdiction-specific regulatory rules as maintained, provenance-linked content (J01 content half); counsel-as-approver legal workflow (J03); regulatory change monitoring tied to rule updates (C06 beyond watchlists); promotion/sweepstakes domain entirely (A-row); entitlement/ledger provenance (F-row); statute-level "why was this allowed" evidence linking decisions to legal authority.
4. **Could Socure add the missing capability easily?** The *infrastructure* pieces (effective dates, policy versioning hardening, counsel approval gates) — yes, easily; they are incremental features on RiskOS. The *content* pieces (maintained jurisdiction rule packs with legal provenance for promotions/marketing law) — organizationally hard: Socure has deliberately positioned itself as regulatorily neutral [SOCURE-028] and its data moat is identity, not law. Age Assurance shows it will productize *verification methods* demanded by new laws, while pushing rule-authoring onto customers.
5. **Could a customer assemble it with Socure + internal engineering?** Substantially, for identity-gated actions: a sophisticated enterprise could encode state-by-state eligibility rules as RiskOS workflows (age gates, geography conditions via custom fields, watchlist policies), get decision traces, backtesting, case review, and compliance exports. They would still self-supply: legal rule content and maintenance, counsel sign-off process (outside the tool), effective-date semantics, statute provenance, promotion-specific objects (entries, AMOE, prizes), and any ledger/entitlement layer. RiskOS's custom fields being "stored, not indexed" and forward-only policy semantics limit evidence-grade regulatory replay [SOCURE-021, SOCURE-024].
6. **What would make a customer buy a separate product instead?** (a) Needing maintained multi-jurisdiction legal content with citations and updates — Socure refuses that role; (b) needing counsel-in-the-loop policy release governance and "as-of" historical replay for regulator defense; (c) domains where the decision subject is a *promotion/action*, not an identity — Socure's data network adds little there and its attempt-based pricing suits identity checks, not high-volume entitlement decisions; (d) needing a system of record for promotions/entitlements (A/F rows) that no risk platform offers.

## 14. Replacement risk

**HIGH.**

Socure has demonstrated both appetite and ability to expand into adjacent decisioning infrastructure: it paid $136M for Effectiv and shipped RiskOS within four months [SOCURE-030], then layered AI agents for rule writing and audit documentation within a year [SOCURE-039]. It already sells to compliance buyers at 3,000+ enterprises, holds FedRAMP Moderate, and covers the B/D/E rows of the proposed product at 3–4 strength. If "regulatory action authorization" became a visible market, Socure could plausibly reposition RiskOS for it — the workflow, evidence, and orchestration rails exist today. Two factors keep this below EXTREME: (1) Socure's stated strategy is identity-centric and regulatorily neutral — it does not author or warrant legal rule content, which is the heart of J01–J03/J09; (2) the promotion/entitlement domain (A/F rows) is entirely outside its object model and pricing logic. The realistic threat is Socure as the incumbent rail that customers *extend* rather than replace.

## 15. Adjacent discoveries

Companies/substitutes encountered that should be considered in this research:

- **Alloy (alloy.com)** — identity risk decisioning/orchestration platform for banks and fintechs (partners with Socure as a data source); its policy-workflow + multi-vendor orchestration model is the closest architectural analog to RiskOS and to the proposed decisioning layer.
- **Unit21** — no-code fraud/AML operations platform (rules engine, case management, SAR e-filing); demonstrates that regulatory *filing* workflows (SARs) are already productized in adjacent compliance ops.
- **Sardine** — fraud + compliance platform combining device intelligence, rules, case management, and AI agents; competes directly with RiskOS-style unified decisioning.
- **Sumsub** — full-cycle verification/orchestration suite frequently cross-shopped with Socure internationally (also: Trulioo, Jumio, Veriff, Prove, Onfido appear as IDV substitutes in buyer research [SOCURE-037]).

## 16. Evidence ledger

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| SOCURE-001 | 3,000+ customers; Citi, Capital One, Coinbase, Revolut, DraftKings, Discover, SoFi, Chime, Gemini, Uber; 19/20 top US banks; 13/15 top card issuers; 600 fintechs; 130 public-sector orgs; "AI-Native Trust Infrastructure" | https://www.socure.com/ | official-marketing | 2026-08-18 | HIGH |
| SOCURE-002 | ID+ is a modular single-API platform: KYC, DocV, Global Watchlist, Decision, Digital Intelligence, Email/Phone/Address Risk, Sigma Identity/Synthetic fraud modules | https://developer.socure.us/ | official-doc | 2026-08-18 | HIGH |
| SOCURE-003 | Decision Module returns "a simple decision outcome (reject, refer, resubmit, review, or accept)… based on a set of predefined business rules" over ID+ module data | https://developer.socure.us/docs/idplus/modules/decision | official-doc | 2026-08-18 | HIGH |
| SOCURE-004 | RiskOS: "decision engine and orchestration platform with identity at the core"; <150ms avg workflow execution; >1,000 QPS; 200+ pre-integrated data products; RiskOS Enterprise (customized) vs Socure Launch (self-serve) | https://www.socure.com/solutions/riskos | official-marketing | 2026-08-18 | MEDIUM |
| SOCURE-005 | Evaluation API returns decision (ACCEPT/REJECT/REVIEW) + status + tags; staged flow (Digital Intelligence bots/emulators/risky networks → Verify fieldValidations + fieldSourceAttribution (SSA, USPS…) → Sigma scores → Watchlist matches); reasonCodes per module; step-up tags | https://help.socure.com/riskos/docs/kyc-watchlist-screening-direct-api-handle-results | official-doc | 2026-08-18 | HIGH |
| SOCURE-006 | RiskOS workflow = "configurable sequence of steps that evaluates incoming events and produces a decision"; 10 step types; no-code Workflow Editor; invoked via /api/evaluation; responses include decisions, enrichment data, reason codes, tags | https://help.socure.com/riskos/docs/workflow-overview.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-007 | Lifecycle Draft→Published→Live; "only one workflow per use case can be live"; major/minor versioning; version history with restore; archive; Move-to-Live permission-gated | https://help.socure.com/riskos/docs/manage-workflow-lifecycle.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-008 | Decision Rules step: outcomes Accept/Reject/Resubmit/Cancel/Manual Review; "rules are evaluated in order, and the first matching rule is applied"; tags in API responses; fallback Else path | https://help.socure.com/riskos/docs/decision-rules.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-009 | Experiments: champion/challenger both run "on 100% of the same live traffic"; only champion's decision returned; 7 comparison metrics; Declare Winner promotes challenger; sync-only; one at a time | https://help.socure.com/riskos/docs/experiments.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-010 | Backtesting re-executes historical records against draft workflow; compares original vs updated decisions; custom JSON payload tests; async workflows not testable; results not exportable | https://help.socure.com/riskos/docs/workflow-testing.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-011 | Decision Path Trace records each executed step, condition outcomes, branches, final decision — "a clear, step-by-step record of the automated decision process for internal governance or external audits" | https://help.socure.com/riskos/docs/decision-path.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-012 | Case management: queues, customizable statuses, accept/reject dispositions returned "via API"; fraud feedback to Socure; reviewers can "replay the flow of data through a workflow from a Case View" | https://help.socure.com/riskos/docs/case-management-overview.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-013 | Sandbox free (10 TPS, 1,000/day) vs production (activated limits); "most evaluations return synchronously"; X-RateLimit headers; 429 + X-Retry-After; sub-account keys share account-level limits | https://help.socure.com/riskos/reference/get-started.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-014 | Webhooks: envelope event_id/event_at/event_type/data; events incl. evaluation_completed, decision_update, case lifecycle, watchlist monitoring; HTTPS POST; Basic/Bearer/OAuth2; retries with backoff | https://help.socure.com/riskos/reference/webhooks-overview.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-015 | System roles: Account Owner, Administrator (sub-accounts), Fraud Analyst, Developer ("no access to PII"), Compliance Officer/Supervisor/Analyst (1-step/2-step approvals); move-to-live rights per role | https://help.socure.com/riskos/docs/role-permission.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-016 | SAML SSO documented for Okta, Microsoft Entra ID, Google Workspace, PingOne, IBM Security Verify, Salesforce, other IdPs | https://help.socure.com/riskos/docs/riskostm-settings/llms.txt | official-doc | 2026-08-18 | HIGH |
| SOCURE-017 | Audit Logs track "what changed, who made it, and when it occurred" for account settings and workflow configurations; admin-accessible | https://help.socure.com/riskos/docs/use-audit-logs.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-018 | Compliance reports (CSV, customizable fields): Transaction Details; Audit reports incl. Account Activity (user, timestamp, IP, action) and Product Settings Change Log (before/after/user); Watchlist Comprehensive Screening Report; Source List Audit Log | https://help.socure.com/riskos/docs/generate-report.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-019 | Reason codes: I (informational) / R (risk) prefixes; scores 0.001–0.999 probabilistic; guidance to "log codes with decisions for audit trails"; codes usable in automated workflow conditions | https://help.socure.com/riskos/docs/reason-codes.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-020 | Reason Code Lists reusable across workflows; "editing a reason code list will have an immediate effect on the workflow, without creating a new workflow version"; changes "don't generate audit trail entries" | https://help.socure.com/riskos/docs/reason-code-lists.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-021 | Custom fields: `custom` JSON objects at 5 request levels; "exposed as variables in your workflow logic" (full JSON path); ≤20–25 recommended; "stored, not indexed — cannot search or filter cases by custom field values" | https://help.socure.com/riskos/docs/custom-fields.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-022 | Entities (standard + custom) with aggregations: 8 functions (Count, Distinct Count, Sum, Avg, Min, Max, First/Last Seen); windows 1 min–180 days or lifetime | https://help.socure.com/riskos/docs/entities-aggregations.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-023 | Watchlist: 1,400+ sanctions/enforcement lists; 2.4M PEP profiles; adverse media from 100,000+ sources; Entity Match Score 0–100; AI-generated match summaries; one-step and two-step review workflows; "complete audit trail to evidence compliance decisions" | https://help.socure.com/riskos/docs/watchlist.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-024 | Watchlist policies: separate screening vs monitoring policies per category; name-match threshold (default 70) + entity correlation score; DOB/country/entity-type filters; "Policy changes apply to all future evaluations. They won't retroactively change existing cases." | https://help.socure.com/riskos/docs/setup-policies.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-025 | Monitoring: enrollment via workflow logic, automonitoring, API, batch, or console; alerts on list addition/update/removal via monitored_search_updated webhook incl. watchlist_case_id | https://help.socure.com/riskos/docs/watchlist-monitoring.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-026 | Socure Verify: 400+ data sources; "Exceed CIP/KYC requirements"; "Adhere to SEC 17AD-17 and FACTA Red Flag requirements"; 99% mainstream / 95% Gen Z verification; custom approve/deny lists | https://www.socure.com/products/identity-verification | official-marketing | 2026-08-18 | MEDIUM |
| SOCURE-027 | "FCRA does not apply to Socure's identity verification (IDV) products"; customers contractually prohibited from FCRA use; auto-decline thresholds only pre-credit; UK CRAIN notice required | https://help.socure.com/riskos/docs/consumer-reports-data.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-028 | Age Assurance: RiskOS-native; confirms 18/21/25+; passive (device/phone/email graph) then active (selfie estimation, doc+selfie); returns only ACCEPT/REJECT + age18/21/25Plus booleans; "Socure remains neutral on regulatory policy and doesn't decide which rules apply to your business" — customers configure state rules | https://help.socure.com/riskos/docs/age-assurance.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-029 | Age assurance marketing: addresses "COPPA, AADC, and DSA"; 0.92s P95 for ID+selfie decisions; >95% Gen Z coverage; web/mobile SDKs + RiskOS workflows | https://www.socure.com/use-cases/age-assurance | official-marketing | 2026-08-18 | MEDIUM |
| SOCURE-030 | Effectiv acquired Oct 2024 ($136M); RiskOS launched 2025-02-12: no-code drag-and-drop rules "with complete audit history"; 50+ pre-integrated third-party data solutions; automated SAR/CTR/UAR report generation; transaction monitoring, KYB, credit underwriting; A/B testing + shadow mode; "tens of thousands of real-time computations per second"; 96.4% identity recurrence; ~90% onboarding approval claim | https://www.prnewswire.com/news-releases/socure-launches-riskos-the-first-risk-decisioning-engine-built-on-the-industrys-most-comprehensive-identity-graph-302374581.html | official-marketing | 2026-08-18 | HIGH |
| SOCURE-031 | 2024: 2.7B identity verification requests (370M unique identities, 2x 2023); customers +42% to 2,800+; +54% GAAP revenue; Leader in Gartner's inaugural 2024 MQ for IDV; public sector +193% across 13 states | https://www.biometricupdate.com/202502/socure-fields-2-7-billion-identity-verification-requests-in-2024 | third-party | 2026-08-18 | MEDIUM |
| SOCURE-032 | "The platform is FedRAMP Moderate Authorized, GovRAMP Moderate Authorized, and certified by the Kantara Initiative for compliance with NIST SP 800-63 Identity Assurance Level"; SocureGov; DOL and GSA case studies | https://www.carahsoft.com/socure | third-party | 2026-08-18 | MEDIUM |
| SOCURE-033 | Security: TLS 1.2+ (1.3 recommended); optional JWE/JWS payload encryption on Evaluation/DocV endpoints; optional mTLS (X.509); IP/domain allowlisting | https://help.socure.com/riskos/docs/security-network-controls.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-034 | Partner Ecosystem: 14 documented integrations (Experian, Middesk, Thomson Reuters Clear, SAM.gov, ICIJ, Lob, Kyckr, Markaaz…); Reseller model ("customers only need to sign an agreement with Socure") vs Connector (customer contract); partner responses usable in subsequent workflow steps and case tiles | https://help.socure.com/riskos/docs/partner-ecosystem.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-035 | Socure Launch: self-serve sandbox signup (riskos.sandbox.socure.com), "start building in minutes"; 5 pre-configured solutions (Prefill/KYC+Fraud+Watchlist/DocV variants) via hosted flow or direct API; one active solution per Launch account | https://help.socure.com/riskos/docs/solutions-for-startups-overview.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-036 | ID+ endpoint https://service.socure.com/api/3.0/EmailAuthScore; modules array (e.g. "emailrisk, phonerisk, fraud, addressrisk, synthetic, decision, kyc"); outcomes Reject/Refer/Resubmit/Review/Accept | https://docs.pingidentity.com/auth-node-ref/latest/cloud/socure-id.html | third-party | 2026-08-18 | MEDIUM |
| SOCURE-037 | Buyer research: praise for "fast integration, strong API ergonomics, and helpful documentation" and detection accuracy; complaints of pricing pressure and implementation complexity; "attempt-based pricing can escalate quickly"; SLAs/service credits to be negotiated; competitors listed incl. Persona, Sumsub, Jumio, Trulioo, Veriff, Prove; 3.8/5 across 108 aggregated reviews | https://www.rfp.wiki/it-security/identity-verification/socure | third-party | 2026-08-18 | LOW |
| SOCURE-038 | Sigma Identity Fraud: scores 0.001–0.999 (higher = riskier); each score returns "a name and a version… for auditing and to differentiate between models"; boolean reason codes; catalogs in dashboard (sandbox + production) | https://help.socure.com/riskos/docs/sigma-identity-fraud.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-039 | RiskOS AI Suite (2025-10-28): Rule Writing Assistant (natural-language rules), Workflow Change Summary ("generates audit documentation automatically"), RiskOS MCP Server, Case Review Assistant, GenAI Explainability, Business Intelligence Agent; human-in-the-loop positioning | https://www.businesswire.com/news/home/20251028150397/en/Socure-Expands-RiskOS-Platform-with-AI-Suite-of-Agents-and-Assistants-Designed-to-Automate-and-Accelerate-Identity-Risk-Compliance-Decisions | official-marketing | 2026-08-18 | HIGH |
| SOCURE-040 | About: CEO/founder Johnny Ayers; customers incl. "the largest sportsbook operators", DraftKings, PrizePicks, Robinhood, Gusto, Poshmark; 18 of top 20 banks; 13 US states, 30+ state agencies, 20+ higher-ed, 2 federal agencies; investors incl. Accel, T. Rowe Price, Tiger Global, Two Sigma, Bain, Santander | https://www.socure.com/company/about | official-marketing | 2026-08-18 | HIGH |
| SOCURE-041 | Gaming: 98% auto-approvals with "up to 90% reduction in manual review"; DocV detects fake IDs/spoofing; selfie reverification with deepfake detection for account protection | https://www.socure.com/industries/gaming | official-marketing | 2026-08-18 | MEDIUM |
| SOCURE-042 | Case re-evaluation: "rerunning a case creates a new evaluation with a unique Evaluation ID, which is linked to the original by the same Application ID"; Connected Evaluation view; feature requires account enablement | https://help.socure.com/riskos/docs/case-reevaluation.md | official-doc | 2026-08-18 | HIGH |
| SOCURE-043 | Complete RiskOS documentation index (llms.txt tree: workflows, case management, enrichments/products, analytics, allow/deny lists, user management, settings, API reference) contains no promotion/sweepstakes/contest/entry/prize/AMOE/wallet/ledger functionality — basis for A-row and F-row absence scores (labeled inference) | https://help.socure.com/riskos/llms.txt | official-doc | 2026-08-18 | HIGH |
| SOCURE-044 | DevHub SDK/module index: DocV SDKs (iOS 5.4.2, Android 5.4.7, React Native 5.2.8, Web 5.0.0), Digital Intelligence SDKs; module list incl. Address/Email/Phone Risk, Graph Intelligence, Alert List, Prefill, Deceased Check, eCBSV | https://developer.socure.us/llms.txt | official-doc | 2026-08-18 | HIGH |
| SOCURE-045 | Developer resources: RiskOS MCP Server ("Integrate Using Cursor / Claude Code"); webhook configuration reference; payload encryption; mTLS; IP filtering; custom fields; customer metadata pass-through; resuming paused evaluations | https://help.socure.com/riskos/docs/developer-resources/llms.txt | official-doc | 2026-08-18 | HIGH |
| SOCURE-046 | Enterprise Solutions catalog: Consumer Onboarding (standard + Advanced Prefill), Trust & Safety, Bank Account Verification, Business Onboarding (KYB), Login/Authentication, Workforce Verification, Age Assurance, Hosted Flows | https://help.socure.com/riskos/docs/enterprise-solutions/llms.txt | official-doc | 2026-08-18 | HIGH |
| SOCURE-047 | Analytics: Business and Operations dashboards (KPIs, drill-downs); data report CSV downloads; compliance report generation; Portfolio Scrub uploads incl. encrypted SFTP | https://help.socure.com/riskos/docs/analytics-reports/llms.txt | official-doc | 2026-08-18 | HIGH |

## 17. Verdict

**MAJOR OVERLAP**

Socure is not a promotion-compliance vendor — the A and F rows are empty and it ships no jurisdictional legal content, explicitly declaring regulatory neutrality. But post-Effectiv, RiskOS delivers most of the *mechanical* architecture Promotion OS proposes: a synchronous event-decision API with allow/deny/review outputs and reason codes, no-code versioned policy workflows, custom attributes, entity state, backtesting and live shadow impact analysis, third-party signal orchestration with unified contracting, case management with per-decision path traces, RBAC/SSO, audit logs, and exportable compliance reports — sold at scale to 3,000+ regulated enterprises including sportsbooks. Any Promotion OS pitch will be evaluated against "we already run Socure/RiskOS and can build the rules ourselves." The defensible remainder is legal-content-as-product (jurisdiction packs with provenance, counsel workflow, effective-date replay) and the promotion/entitlement object model — precisely the parts Socure has chosen not to own. Overlap is major; identity adjacency makes it a probable fast follower.
