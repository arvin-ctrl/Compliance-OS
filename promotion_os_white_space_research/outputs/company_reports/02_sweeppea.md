# Company Report — Sweeppea

Researcher: Research Agent 02 (Sweeppea)
Date: 2026-08-18
Category: Promotion administration
Manager: Manager A

## 1. Executive summary

Sweeppea (founded 2010, Coral Gables, FL) is a **sweepstakes administration company** that pairs a self-service SaaS campaign platform with a human full-service administration business. Its actual core product is the end-to-end running of legally compliant US/Canada sweepstakes: entry collection (web, text-to-win short code 65047, QR, social, Shopify buy-to-enter), official rules generation, AMOE handling, weighted random winner drawings, winner verification, prize fulfillment, FL/NY/RI registration and surety bonding, ABC alcohol approvals, and 1099/1096 tax workflows [SWEEPPEA-001, -004, -010, -011, -013].

Buyers are **brand and agency marketers** (Coca-Cola, Tyson, Honda, Yuengling appear in case studies/client lists as per-campaign engagements) and, increasingly, **developers/AI builders** via a REST API v3, CLI, and an 83-tool MCP server [SWEEPPEA-016, -025]. The job it is hired to do: "run a prize promotion that generates leads without getting us sued" — Sweeppea explicitly sells liability transfer, marketing itself as **"Compliance-as-a-Service"**: it "assumes the role of the Independent Administrator, which is a critical legal shield during audits or state inquiries," so "the platform is insulated from liability for the legal validity of the promotion" [SWEEPPEA-027].

Critical context: this is a very small company (~3 employees, ~$3M revenue per third-party directories) delivering compliance chiefly through templates, checklists, hardcoded guardrails, and human experts — not through policy infrastructure [SWEEPPEA-003, -037].

## 2. Product architecture

Core entities: **Business/Account** (sponsor profile, plan, wallet) → **Sweepstakes** (campaign with dates, entry page, settings) → **Entry Page** (80+ configurable settings incl. compliance switches) → **Rules documents** (primary/secondary official rules, wizard-generated HTML) → **Participants** (in collections: Participants / ParticipantsAmoe / OptOuts; groups; bonus entries) → **Winners** (drawn, scheduled drawings) → supporting modules (files, notes, calendar, billing, invoices, surveys, tickets) [SWEEPPEA-004, -007, -008, -016].

Concrete workflow:

- INPUT: campaign parameters (dates, prizes/ARV, eligibility states, min age, entry method) + entrant submissions (form/SMS/purchase events from Shopify or API `POST /participants/add`).
- DECISION/PROCESS: (a) at **campaign setup**, the rules wizard encodes eligibility and jurisdictional requirements into a legal document, and the MCP validation layer synchronously rejects tool calls violating hardcoded legal guardrails (illegal lottery without AMOE, COPPA under-13, alcohol age gates) or Sweeppea-editable "dynamic declarative rules" [SWEEPPEA-014]; (b) at **entry time**, platform filters run (spam/bot detection, IP blocking, duplicate limits, age-gate checkbox for 21+ promotions) [SWEEPPEA-022, -023]; (c) at **draw time**, weighted random selection over filtered eligible participants (draw blocked unless official rules exist) [SWEEPPEA-009]; (d) **post-draw**, human/service steps: winner verification (biometric app), affidavits, releases, 1099s, fulfillment [SWEEPPEA-010, -011, -024].
- OUTPUT: hosted entry page + hosted official rules URL, participant dataset, winner list ("drawing certification details" retrievable per marketing), tax documents, fulfillment [SWEEPPEA-029].

The compliance "engine" is therefore a mix of (1) document templates with jurisdiction parameters, (2) pre-launch checklists and automatic warnings, (3) a small set of inviolable server-side guardrails, and (4) professional services. There is **no customer-authorable policy engine, no runtime authorization API for external actions, and no decision-log substrate** [SWEEPPEA-017, -028].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Full-service administration | Humans design, draft rules, register/bond (FL/NY/RI), ABC approvals, draw, verify, fulfill, 1099/1096; from $2,999/sweeps + $399/mo | Brand/agency marketing | Core (flagship) | SWEEPPEA-001, -010, -013 |
| Self-service platform | SaaS campaign builder: entry pages, rules wizard, drawings, analytics; $99–$399/mo | SMB→mid-market marketing | Core | SWEEPPEA-001, -026 |
| Official Rules Wizard | 14-step generator with legal safeguards (NPN, void-where-prohibited, tax disclosures, AMOE language, state options) | Marketing/legal-adjacent | Core differentiator | SWEEPPEA-005, -012 |
| Shopify buy-to-enter app | Entries per dollar spent in real time; mandatory free-entry AMOE form; $29/mo | E-commerce merchants | Add-on channel | SWEEPPEA-035 |
| Text-to-win (short code 65047) | SMS entry with sweepkeys; TCPA guidance embedded | Marketing | Core legacy channel | SWEEPPEA-038 |
| REST API v3 / CLI / MCP server (83 tools) | Programmatic lifecycle: sweepstakes, participants, rules, winners, billing; AI-agent operation with server-side legal guardrails | Developers/platforms/AI builders | Growing core (Enterprise/API tier) | SWEEPPEA-016, -017, -018 |
| "Compliance-as-a-Service" for SaaS platforms | Embed sweepstakes engine; Sweeppea acts as Independent Administrator (liability shield), rules generation, certified draws, 1099s | Platform/engineering + legal | Positioning of API offering | SWEEPPEA-027, -028 |
| Winner management app | Biometric validation, face recognition, digital document signing for winner verification | Marketing/ops | Add-on | SWEEPPEA-024 |
| Non-profit module | Donate-to-enter with donation wallet, receipts, free-entry compliance option | Non-profits | Add-on vertical | SWEEPPEA-026 |
| Surveys / invoices / notes / calendar | Ancillary business modules (account-gated) | Same account | Add-ons | SWEEPPEA-016 |

## 4. API / developer capability

- **APIs**: Public REST API v3 (`api-v3.sweeppea.com`), OpenAPI 3.1, bearer-token auth; ~55 endpoints across account, sweepstakes, entry page, participants, groups, winners, rules, notes, calendar, billing, wallet, invoices, surveys, support, utility data [SWEEPPEA-017].
- **SDKs**: No conventional language SDKs. Instead: native Rust CLI (npm `@sweeppea/cli`, OS-keyring auth, `--json` for CI/CD), n8n nodes, Zapier (7,000+ apps), ChatGPT App, Agent Zero plugin [SWEEPPEA-018].
- **MCP server**: `mcp.sweeppea.com`, 83 tools in 18 categories, MCP protocol 2025-11-25, JSON-RPC 2.0 — marketed as the industry's first sweepstakes AI-agent integration [SWEEPPEA-016].
- **Webhooks**: claimed on marketing pages ("real-time webhooks... 'Winner Confirmed,' 'Rules Updated'") but absent from the API reference/OpenAPI spec — undocumented [SWEEPPEA-019, -039].
- **Sandbox**: claimed once on the SaaS marketing page; no sandbox base URL or test-key documentation exists [SWEEPPEA-020, -039].
- **Rules engine**: none exposed to customers. Server-side validation exists in the MCP layer: hardcoded legal guardrails + Sweeppea-editable declarative rules, rejecting violating calls before execution with structured payloads (`blocked_by`, `error_code`, `error_message`, `rule_id`) [SWEEPPEA-014, -015].
- **Synchronous decisioning**: only in the above sense (platform-operation gating) plus entry-time spam/duplicate/IP filters. No latency claims anywhere; no authorization endpoints exist in the fully enumerated spec [SWEEPPEA-017, -023].
- **Versioning**: v3 in base URL only; no versioning/deprecation policy, no idempotency keys, no documented rate-limit quotas, no error-code catalog (generic `{Response:false, Message}`) [SWEEPPEA-039].
- **Integration model**: hosted entry pages + rules URLs by default; headless via `POST /participants/add` for platforms that build their own front end (and are told to implement their own age/geo validation client-side) [SWEEPPEA-028, -040].

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** No. Custom form fields exist on entries [SWEEPPEA-008], but there is no customer-defined rule evaluation over attributes.
- **Store customer/user state?** Per-sweepstakes participant state only (entries, bonus entries, collections, groups, opt-outs, spam flags) [SWEEPPEA-008].
- **Return reason codes?** Only for MCP-layer validation rejections (`blocked_by`, `error_code`, `rule_id`) [SWEEPPEA-015]; core API errors are generic messages [SWEEPPEA-039].
- **Output allow/deny/review?** Deny-with-reason exists for platform tool calls (guardrails); no review state; no allow/deny/review model for end-user actions [SWEEPPEA-014, -028].
- **Simulate policies?** No simulation/dry-run capability anywhere in the enumerated API/tool surface [SWEEPPEA-017, -039].
- **Replay decisions?** No. Winner lists and participant data are fetchable after the fact; the evaluation itself is not reconstructable [SWEEPPEA-029].
- **Version policies?** No. Official rules documents are editable (`update_rule`) with no documented version history; the compliance guardrails are versioned only implicitly by Sweeppea internally [SWEEPPEA-014].
- **Deploy rules independently of app code?** Only Sweeppea itself can: its "dynamic declarative rules" are "editable by Sweeppea" and apply platform-wide — customers cannot author, deploy, or version rules [SWEEPPEA-014].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance (core)**: prize/chance/consideration lottery analysis, mandatory official rules, NPN + void-where-prohibited language, AMOE with "equal dignity," 17-item pre-launch checklist, prohibited categories (gambling mechanics, federally illegal substances, weapons/tobacco/vape, crypto-with-purchase, discriminatory targeting) [SWEEPPEA-005, -007, -012].
- **Generic regulatory workflow**: none — everything is sweepstakes/promotions-specific.
- **Jurisdiction restrictions**: state-selection options in the rules wizard (including presets that exclude FL/NY/RI to avoid registration), FL/NY $5,000 ARV thresholds with 7/30-day filing windows, RI $500 retailer rule, Canada skill-testing question, Quebec RACJ + French translation, 7 alcohol-board states [SWEEPPEA-012]. These live in **legal-document templates and warnings**, not in runtime enforcement — state eligibility is "NOT" handled by the geolocation setting [SWEEPPEA-021].
- **Location verification**: IP blocking, GPS/IP geofencing for physical radius (e.g., store radius); no VPN/proxy detection, no compliance-grade location assurance [SWEEPPEA-021].
- **Legal content/rules**: wizard-generated official rules; hosted rules URLs; abbreviated rules for ads; AI rules analysis (marketing claim) [SWEEPPEA-005].
- **Regulatory monitoring**: no product; Sweeppea maintains its own guides (annual "How to Run a Legal Sweepstakes"), a static 50-state guide, and vendor-edited guardrails [SWEEPPEA-036, -043].
- **Change management**: pause/unpause and update endpoints; no change-control or approval system [SWEEPPEA-004].
- **Counsel approval**: human review in full-service and Enterprise "Sweepstakes Compliance Review Services"; they "work with legal professionals"; no software approval gate, and no claim that reviewers are licensed attorneys [SWEEPPEA-006, -013, -037].
- **Historical policy state**: none documented (no rules version history, no point-in-time reconstruction).

## 7. Audit / evidence

Can a customer reconstruct:

- **Exact inputs?** Partially — participant records and form data are retained and exportable; draw-time filter parameters are not documented as persisted [SWEEPPEA-008, -029].
- **Exact rule/policy?** Partially — the official rules HTML document exists at a hosted URL, but edits overwrite without documented version history [SWEEPPEA-005].
- **Exact version?** No — no versioning of rules documents or platform guardrails is documented.
- **Exact output?** Yes for winners: winner lists fetchable; marketing says "fetch and store the drawing certification details via `GET /winners` to provide to the user if their campaign is ever audited," though the winner-tools reference documents no certification schema [SWEEPPEA-029].
- **Exact timestamp?** Likely for entries/draw schedules (dates precise to minute with timezones at campaign level); not documented as an audit log [SWEEPPEA-012].
- **Human approvals?** No — no recorded approval history (MCP destructive-op confirmations are session behavior, not records) [SWEEPPEA-016].
- **Source/legal authority?** No — generated rules carry no machine-readable citation of the underlying statute [SWEEPPEA-043].

Net: "auditable records of participant data and winner selections" [SWEEPPEA-029] is real at the data level and reinforced by the Independent Administrator role (the administrator's files serve as the audit package in a state inquiry), but this is **records custody, not evidence-grade decision reconstruction**. Retention is a fixed policy (participant data deleted within 72 hours of account closure), not configurable [SWEEPPEA-031].

## 8. Enterprise readiness

- **SSO/RBAC**: no evidence of SAML/SSO or role-based access anywhere (2FA only); unresolved [SWEEPPEA-030].
- **Multitenancy/multi-brand**: agency dashboard managing ~10 client sweepstakes; Enterprise plan covers 20 sweepstakes; no formal org hierarchy or per-brand permissions documented [SWEEPPEA-042, -026].
- **Environments**: no staging documented; sandbox claimed only in marketing [SWEEPPEA-020, -039].
- **Security certifications**: security outline shows solid basics (HTTPS, encrypted backups, 2FA, firewalls/DDOS, AWS) but concedes some active data is not encrypted at rest; "SOC 2 Type II" appears only as "for enterprise custom development" and about-us attributes SOC 2 to AWS infrastructure — no attestation, ISO 27001, or pen-test report found; Trust Center content could not be retrieved [SWEEPPEA-030, -002].
- **SLA**: "99.9% uptime guarantee" marketing statement; no SLA document [SWEEPPEA-030].
- **Support/professional services**: 24/7 email+phone on paid plans; dedicated account managers; $750 platform training; heavy PS involvement is the model [SWEEPPEA-037].
- **Customer scale examples**: national brands (Coca-Cola, Tyson, Honda) as per-campaign clients, not platform integrations [SWEEPPEA-025]. Company is ~3 people per third-party directories — a material constraint on enterprise procurement (inference from SWEEPPEA-003).

## 9. Commercial model

Pricing is fully public: Self-service $99 (Allegro, 1 active sweeps) / $399 (3 active sweeps, unlimited participants); Shopify $29; Non-profit $399 + 6% donation fee; Full-service from $2,999/sweepstakes + $399/mo platform fee; Enterprise custom (20 sweepstakes, API access, compliance review services) [SWEEPPEA-001, -026]. Likely buyer: brand/agency marketing manager; secondary: platform engineering teams embedding sweepstakes; legal is an influencer, not the wallet [SWEEPPEA-025, -027]. Implementation burden is low (hosted pages, app-store installs, simple REST) [SWEEPPEA-035]. Sales motion: self-serve free trial + inside sales for full service; "Human Expert + Platform" framing [SWEEPPEA-037]. Large-company evidence is campaign-services revenue, not enterprise software contracts [SWEEPPEA-025].

## 10. Strengths

- **Deep, genuine sweepstakes-law operationalization**: FL/NY/RI thresholds and filing windows, equal-dignity AMOE, alcohol/cannabis/COPPA rules, Quebec/Canada specifics — encoded into wizards, checklists, warnings, and inviolable guardrails [SWEEPPEA-012, -014].
- **Liability transfer as the product**: Independent Administrator role + bonds/registrations + 1099s is a clean, defensible value proposition marketed literally as "Compliance-as-a-Service" [SWEEPPEA-027, -013].
- **Unusually modern developer/AI surface for its category**: OpenAPI 3.1, native CLI, 83-tool MCP server with server-side compliance validation and structured rejections — ahead of most promotion administrators [SWEEPPEA-014, -016, -017].
- **Purchase-to-enter compliance niche** (Shopify entries-per-dollar with mandatory AMOE) — a legally tricky mechanic productized [SWEEPPEA-035].
- **Transparent pricing and self-serve motion** rare in the administration category [SWEEPPEA-026].

## 11. Weaknesses / constraints

- **Tiny organization** (~3 people, ~$3M revenue per directories) delivering a services-heavy model — throughput, redundancy, and enterprise procurement risk (third-party estimate; labeled as such) [SWEEPPEA-003, -037].
- **Marketing-vs-documentation gaps**: webhooks, sandbox, "certified" drawings, and SOC 2 are claimed in marketing but absent or ambiguous in official docs [SWEEPPEA-019, -020, -029, -030].
- **No policy infrastructure**: no customer-authorable rules, no versioning, no simulation, no decision logs, no approval workflows — compliance logic is vendor-internal and template-shaped [SWEEPPEA-014, -017, -039].
- **Runtime eligibility left to the customer** in the embedded model ("Implement front-end validation (Age Gate) before the API call") [SWEEPPEA-028].
- **Enterprise governance thin**: no documented SSO/RBAC/staging/attestations; partial encryption at rest admitted [SWEEPPEA-030].
- **US/Canada scope only**; jurisdiction intelligence is static educational + template content, with no change-monitoring product [SWEEPPEA-036, -043] (inference: keeping it current depends on the two principals).

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,4,SWEEPPEA-004;SWEEPPEA-001;SWEEPPEA-035
A02,2,SWEEPPEA-041
A03,1,SWEEPPEA-041;SWEEPPEA-009
A04,4,SWEEPPEA-005;SWEEPPEA-012
A05,3,SWEEPPEA-006;SWEEPPEA-013;SWEEPPEA-037
A06,4,SWEEPPEA-007;SWEEPPEA-014
A07,4,SWEEPPEA-008;SWEEPPEA-035;SWEEPPEA-038
A08,3,SWEEPPEA-009;SWEEPPEA-029
A09,3,SWEEPPEA-010
A10,3,SWEEPPEA-011
B01,1,SWEEPPEA-040;SWEEPPEA-017
B02,2,SWEEPPEA-014;SWEEPPEA-023;SWEEPPEA-007
B03,0,SWEEPPEA-017;SWEEPPEA-028
B04,1,SWEEPPEA-014;SWEEPPEA-015
B05,1,SWEEPPEA-015
B06,2,SWEEPPEA-008;SWEEPPEA-040
B07,2,SWEEPPEA-008
B08,0,SWEEPPEA-017;SWEEPPEA-014
B09,0,SWEEPPEA-017;SWEEPPEA-039
B10,0,SWEEPPEA-017;SWEEPPEA-039
C01,3,SWEEPPEA-012;SWEEPPEA-013;SWEEPPEA-043
C02,3,SWEEPPEA-012;SWEEPPEA-014
C03,2,SWEEPPEA-012;SWEEPPEA-007;SWEEPPEA-038
C04,1,SWEEPPEA-005;SWEEPPEA-012
C05,?,
C06,1,SWEEPPEA-036;SWEEPPEA-014
C07,1,SWEEPPEA-012;SWEEPPEA-014
C08,1,SWEEPPEA-006;SWEEPPEA-013;SWEEPPEA-037
C09,1,SWEEPPEA-043
C10,1,SWEEPPEA-012;SWEEPPEA-014
D01,1,SWEEPPEA-009;SWEEPPEA-029
D02,1,SWEEPPEA-029
D03,0,SWEEPPEA-017;SWEEPPEA-039
D04,1,SWEEPPEA-008;SWEEPPEA-029
D05,0,SWEEPPEA-017;SWEEPPEA-016
D06,1,SWEEPPEA-029
D07,2,SWEEPPEA-029;SWEEPPEA-027;SWEEPPEA-026
D08,1,SWEEPPEA-031
D09,?,
D10,1,SWEEPPEA-026;SWEEPPEA-030
E01,2,SWEEPPEA-024;SWEEPPEA-011
E02,2,SWEEPPEA-022
E03,?,
E04,2,SWEEPPEA-021
E05,1,SWEEPPEA-023
E06,?,
E07,1,SWEEPPEA-023
E08,2,SWEEPPEA-023;SWEEPPEA-008
E09,1,SWEEPPEA-016;SWEEPPEA-024
E10,0,SWEEPPEA-018;SWEEPPEA-017
F01,1,SWEEPPEA-032
F02,1,SWEEPPEA-032
F03,1,SWEEPPEA-009
F04,1,SWEEPPEA-035
F05,1,SWEEPPEA-004
F06,0,SWEEPPEA-032;SWEEPPEA-017
F07,1,SWEEPPEA-009;SWEEPPEA-011
F08,0,SWEEPPEA-032;SWEEPPEA-017
F09,0,SWEEPPEA-032;SWEEPPEA-017
F10,0,SWEEPPEA-032;SWEEPPEA-017
G01,2,SWEEPPEA-042;SWEEPPEA-026
G02,?,
G03,?,
G04,0,SWEEPPEA-016;SWEEPPEA-017
G05,1,SWEEPPEA-020;SWEEPPEA-039
G06,0,SWEEPPEA-017;SWEEPPEA-039
G07,1,SWEEPPEA-004
G08,1,SWEEPPEA-019;SWEEPPEA-039
G09,1,SWEEPPEA-030
G10,1,SWEEPPEA-030;SWEEPPEA-002
H01,3,SWEEPPEA-017;SWEEPPEA-016
H02,2,SWEEPPEA-018;SWEEPPEA-016
H03,1,SWEEPPEA-019;SWEEPPEA-039
H04,1,SWEEPPEA-020;SWEEPPEA-039
H05,1,SWEEPPEA-017;SWEEPPEA-039
H06,0,SWEEPPEA-039;SWEEPPEA-017
H07,1,SWEEPPEA-039;SWEEPPEA-030
H08,1,SWEEPPEA-017
H09,2,SWEEPPEA-016;SWEEPPEA-026
H10,1,SWEEPPEA-018
I01,2,SWEEPPEA-027;SWEEPPEA-006
I02,2,SWEEPPEA-027;SWEEPPEA-018
I03,4,SWEEPPEA-025;SWEEPPEA-001
I04,0,SWEEPPEA-023;SWEEPPEA-017
I05,2,SWEEPPEA-025;SWEEPPEA-002;SWEEPPEA-003
I06,3,SWEEPPEA-026;SWEEPPEA-001
I07,3,SWEEPPEA-037;SWEEPPEA-001
I08,1,SWEEPPEA-025;SWEEPPEA-037
I09,3,SWEEPPEA-035;SWEEPPEA-017
I10,4,SWEEPPEA-026
J01,1,SWEEPPEA-014;SWEEPPEA-012
J02,0,SWEEPPEA-017;SWEEPPEA-016
J03,1,SWEEPPEA-006;SWEEPPEA-037
J04,0,SWEEPPEA-012;SWEEPPEA-017
J05,0,SWEEPPEA-028;SWEEPPEA-017
J06,0,SWEEPPEA-018;SWEEPPEA-017
J07,1,SWEEPPEA-029
J08,0,SWEEPPEA-017;SWEEPPEA-039
J09,1,SWEEPPEA-014;SWEEPPEA-012
J10,0,SWEEPPEA-017;SWEEPPEA-016
```

**Notes on 0 scores (positive evidence of absence, not mere non-mention).** The REST API surface is fully enumerated in a published OpenAPI 3.1 spec and the MCP surface in a complete 83-tool catalog [SWEEPPEA-016, -017]; neither contains decision/authorization, simulation, replay, policy-versioning, approval-workflow, signal-orchestration, or user-ledger endpoints, and the API reference explicitly lacks idempotency/webhook/sandbox sections [SWEEPPEA-039]. Specifics: **B03** no decision API exists and Sweeppea instructs customers to enforce eligibility client-side [SWEEPPEA-028]; **B08/B09/B10** no customer rules engine, dry-run, or replay in the enumerated surface; **D03/D05** no policy versions or recorded approvals exist to link; **E10** integrations list is marketing tools only (Zapier/Klaviyo/Shopify), no IDV/fraud vendor orchestration; **F06/F08–F10** the only wallet is account-level billing funds — no end-user value ledger exists (architecture precludes) [SWEEPPEA-032]; **G04/G06** no approval-workflow or policy-testing tools in the catalogs; **H06** the complete API contract defines no idempotency mechanism; **I04** no fraud/risk-buyer product or motion exists (fraud features are embedded abuse controls); **J02/J04/J05/J06/J08/J10** the proposed-differentiator architecture (deployment pipeline, impact analysis, cross-product authorization, signal normalization, replay, control plane) is absent from every enumerated surface — labeled inference from documented enumeration. **Directional notes**: I07 scored 3 = high PS dependency (services-led model); I08 scored 1 = low switching cost; I09 scored 3 = low integration burden (hosted pages/turnkey). **? squares**: C05 (rules version history unknown), D09 (tamper-evidence unknown), E03 (address verification unknown; winner addresses collected), E06 (VPN detection unknown), G02/G03 (RBAC/SSO undocumented; in-app capability cannot be ruled out).

## 13. White-space implications

1. **Already solved (by Sweeppea, for sweepstakes)**: Category-A promotion administration — creation, official rules generation, AMOE, entry management, drawings, fulfillment, tax — plus the liability-transfer wrapper (Independent Administrator, bonding/registration) [SWEEPPEA-004→-013, -027]. If "Promotion OS" means administering sweepstakes compliantly, Sweeppea and its service-bureau peers already sell that outcome.
2. **Partially solved**: jurisdiction intelligence as encoded templates/thresholds/warnings (C01–C03) and even embryonic policy-as-guardrails: hardcoded legal rules plus Sweeppea-editable declarative rules that synchronously reject violating operations with reason-coded payloads [SWEEPPEA-012, -014, -015]. Audit exists as records custody (D07=2), not decision evidence.
3. **Unsolved**: everything J-shaped — customer-authorable versioned regulatory policy (J01), legal-to-production deployment with counsel approval gates (J02/J03), impact analysis (J04), real-time cross-product action authorization (J05 — explicitly delegated to the customer's front end [SWEEPPEA-028]), signal normalization (J06), evidence-grade reconstruction/replay (J07/J08), lifecycle control plane (J10). Also unsolved: enterprise governance (SSO/RBAC/attestations) and developer-platform hardening (idempotency, webhooks, sandbox).
4. **Could Sweeppea add the missing capability easily?** No. The gap is architectural (no decision substrate, no policy versioning) and organizational (~3 people, services-led). It could plausibly extend its MCP guardrails into a marketed "compliance rules API" for sweepstakes setup checks, but building an authorization/evidence control plane for regulated actions across products is far beyond its demonstrated scope (inference) [SWEEPPEA-003, -014, -017].
5. **Could a customer assemble it using Sweeppea + internal engineering?** Only the promotion-administration slice: use Sweeppea as compliance back office (rules, AMOE, draws, bonding, 1099s) while building eligibility gating, geo/identity checks, and audit logging in-house — exactly the division Sweeppea prescribes [SWEEPPEA-027, -028]. The decisioning/evidence layer would be 100% internal build; Sweeppea contributes nothing to it.
6. **What would make a customer buy a separate product instead?** (a) Promotions being one of many regulated actions (gaming, cannabis, alcohol delivery, fintech incentives) needing one authorization/evidence plane; (b) needing runtime enforcement and "why was this allowed?" reconstruction that a document-and-service bureau cannot produce; (c) enterprise governance requirements (SSO, RBAC, attestations, SLAs) Sweeppea does not evidence; (d) vendor-risk aversion to a 3-person supplier for production-path decisions. Conversely, if the pain is only "run compliant sweepstakes," Sweeppea's $3–15K-per-campaign service undercuts any infrastructure purchase — the strongest argument against the wedge for this vertical.

## 14. Replacement risk

**LOW.** Sweeppea's compliance is delivered as templates, checklists, a handful of hardcoded guardrails, and human service — not as policy infrastructure it could repoint at regulatory action authorization. It has no decisioning, versioning, evidence, or governance substrate, a ~3-person team, and a services-led P&L [SWEEPPEA-003, -014, -017, -037]. Its MCP-first developer strategy shows genuine technical agility (an AI-operable compliance-guarded API shipped before larger rivals), so it could encroach on *sweepstakes-setup compliance checks as an API*, but not on an enterprise regulatory control plane. The bigger competitive effect is substitutive, not replacement: it lowers the perceived need for promotion-compliance software by absorbing liability cheaply per campaign.

## 15. Adjacent discoveries

- **Woobox** (woobox.com) — named directly in Sweeppea's own comparison as a promotions-platform rival; represents the high-volume, low-compliance DIY tier [SWEEPPEA-033].
- **Marden-Kane** (mardenkane.com) — sweepstakes administration/fulfillment agency since 1957 running programs for brands like Coca-Cola/Hy-Vee; the enterprise-grade human substitute for any promotion-compliance software [SWEEPPEA-034].
- **National Sweepstakes Company** (nationalsweepstakescompany.com) — structures promotions for legal compliance, originates official rules, bonds/registers with states; direct full-service substitute [SWEEPPEA-034].
- **US Sweepstakes & Fulfillment Co.** (ussweeps.com) — full-service administrator with SMS/text-promotion practice competing with Sweeppea's text-to-win core [SWEEPPEA-034].
- **randomdraws.com** — certified random prize-draw service; unbundles the "certified drawing" component that Sweeppea bundles [SWEEPPEA-034].
- (Substitute category) **Promotions counsel at law firms** — the FL/NY/RI filings, rules review, and ABC approvals Sweeppea performs are classically done by outside counsel + a bonding agent; any white-space thesis must beat this labor market, not just software rivals (inference from SWEEPPEA-006, -013, -034).

## 16. Evidence ledger

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| SWEEPPEA-001 | Full-service (from $2,999/sweeps + $399/mo) + self-service SaaS ($99–$399/mo) + $29 Shopify app | https://www.sweeppea.com/pricing | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-002 | Founded 2010 Coral Gables FL; 2 named principals; Coca-Cola/Honda/Tyson etc. client claims; "AWS infrastructure with SOC 2 compliance" | https://www.sweeppea.com/about-us | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-003 | Directories estimate ~3 employees, ~$3M revenue | https://www.zoominfo.com/c/sweeppea/410613718 | third-party | 2026-08-18 | MEDIUM |
| SWEEPPEA-004 | Full sweepstakes lifecycle via REST API v3 (create/clone/update/pause/delete, auto entry pages) | https://apidocs.sweeppea.com/openapi.json | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-005 | Official rules productized: 14-step wizard, NPN/void-where-prohibited/tax disclosures auto-inserted | https://raw.githubusercontent.com/Sweeppea-Development-Lab/mcp-documentation/main/08-rules-tools.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-006 | Human legal administration: advice, rules drafting, ad-material review | https://www.sweeppeasweeps.com/sweepstakes-administration.html | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-007 | AMOE first-class: ParticipantsAmoe collection, ActivateAmoeSwitch required with purchase entry, equal dignity | https://raw.githubusercontent.com/Sweeppea-Development-Lab/mcp-documentation/main/legal-compliance.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-008 | Entry management API: add/fetch/count/single/delete, groups, collections, custom fields, bonus entries | https://apidocs.sweeppea.com/openapi.json | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-009 | Weighted random draws with eligibility filters; scheduled/recurring; blocked without official rules | https://raw.githubusercontent.com/Sweeppea-Development-Lab/mcp-documentation/main/11-winner-tools.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-010 | Full-service prize fulfillment (purchase/pack/ship, travel, insured, digital cards) | https://www.sweeppea.com/full-service-sweepstakes-administration | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-011 | Tax workflows: 1099/1096, affidavits, releases, SSN/Tax-ID storage for 1099-MISC | https://www.sweeppea.com/sweepstakes-api-saas-platforms | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-012 | Jurisdiction rules encoded: FL/NY $5k + 7/30-day windows, RI $500, state-exclusion presets, Quebec RACJ, Canada skill question, 7 ABC states | https://raw.githubusercontent.com/Sweeppea-Development-Lab/mcp-documentation/main/legal-compliance.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-013 | Surety bonds & state registrations FL/NY/RI; ABC approvals — human service | https://www.sweeppea.com/full-service-sweepstakes-administration | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-014 | MCP server-side validation: hardcoded legal guardrails + Sweeppea-editable dynamic rules; violating calls rejected pre-execution | https://raw.githubusercontent.com/Sweeppea-Development-Lab/sweeppea-mcp-info/main/README.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-015 | Structured rejection payloads: blocked_by, error_code, error_message, rule_id | https://raw.githubusercontent.com/Sweeppea-Development-Lab/sweeppea-mcp-info/main/README.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-016 | MCP server v1.19.0: 83 tools, 18 categories, mcp.sweeppea.com, JSON-RPC 2.0 | https://github.com/Sweeppea-Development-Lab/mcp-documentation | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-017 | REST API v3, OpenAPI 3.1, ~55 endpoints; NO decision/policy/simulation/log endpoints in enumerated surface | https://apidocs.sweeppea.com/openapi.json | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-018 | CLI (Rust binary, --json CI/CD), n8n nodes, Zapier, ChatGPT App, Agent Zero; no language SDKs | https://clidocs.sweeppea.com/ | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-019 | Webhooks claimed in marketing; absent from API reference | https://www.sweeppea.com/integrations | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-020 | Sandbox claimed in marketing; absent from API reference | https://www.sweeppea.com/sweepstakes-api-saas-platforms | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-021 | Geo: IP blocking, GPS/IP radius geofencing; explicitly NOT for state-level restrictions (those live in rules text) | https://raw.githubusercontent.com/Sweeppea-Development-Lab/mcp-documentation/main/04-entry-page-tools.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-022 | Age controls: min_age 13/18/21; Age Gate only for 21+ alcohol/cannabis; under-13 refused (COPPA) | https://raw.githubusercontent.com/Sweeppea-Development-Lab/mcp-documentation/main/04-entry-page-tools.md | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-023 | Fraud/abuse: Turnstile, IP detection, AI spam filters, duplicate limits, mute/blacklist | https://www.sweeppea.com/features | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-024 | Winner verification app: biometric validation, face recognition, digital signing | https://www.sweeppea.com/features | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-025 | Case studies: Coca-Cola, Tyson, Ensueño, San Juan Seltzer, United Association, DiamondBack | https://www.sweeppea.com/sweepstakes-case-studies | case-study | 2026-08-18 | HIGH |
| SWEEPPEA-026 | Public Enterprise tier: 20 sweeps, API access, "Sweepstakes Compliance Review Services", bulk export | https://www.sweeppea.com/pricing | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-027 | "Compliance-as-a-Service" positioning: Independent Administrator = legal shield; platform "insulated from liability" | https://www.sweeppea.com/sweepstakes-api-saas-platforms | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-028 | Customers must "Implement front-end validation (Age Gate) before the API call" — no runtime authorization by Sweeppea | https://www.sweeppea.com/sweepstakes-api-saas-platforms | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-029 | Audit claims: auditable participant/winner records; "drawing certification details" via GET /winners; but no certification schema in reference docs | https://raw.githubusercontent.com/Sweeppea-Development-Lab/sweeppea-mcp-info/main/README.md | official-doc | 2026-08-18 | MEDIUM |
| SWEEPPEA-030 | Security outline: HTTPS, encrypted backups, 2FA, AWS, WAF; partial at-rest encryption; SOC 2 wording scoped/ambiguous; no attestation found | https://www.sweeppea.com/security-online | official-doc | 2026-08-18 | MEDIUM |
| SWEEPPEA-031 | Participant data deleted within 72h of account closure; GDPR controller/processor; SCCs | https://www.sweeppea.com/gdpr-privacy-policy | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-032 | Wallet = account-level billing funds (+ nonprofit donation wallet); no end-user ledger exists | https://apidocs.sweeppea.com/openapi.json | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-033 | Sweeppea compares itself vs Woobox/ShortStack/ViralSweep on compliance-administration differentiators | https://www.sweeppea.com/sweepstakes-platform-comparison | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-034 | Service-bureau substitutes: Marden-Kane, National Sweepstakes Company, US Sweepstakes & Fulfillment, Odds On, randomdraws.com | https://www.mardenkane.com/ | third-party | 2026-08-18 | HIGH |
| SWEEPPEA-035 | Shopify buy-to-enter: entries-per-dollar in real time; mandatory compliant free-entry form | https://www.sweeppea.com/made-for-shopify/ | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-036 | No change-monitoring product; regulatory knowledge maintained by Sweeppea in guides + vendor-edited guardrails | https://www.sweeppeasweeps.com/sweepstakes-and-contest-rules-by-state.html | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-037 | "Human Expert + Platform" model; compliance outcomes depend on Sweeppea staff; $750 training | https://www.sweeppea.com/pricing | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-038 | Text-to-win short code 65047; TCPA guidance (opt-in language, STOP/HELP, quiet hours) | https://www.sweeppea.com/blog/what-is-a-sweepkey-and-other-text-to-win-sweepstakes-lingo/ | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-039 | API reference lacks webhooks, sandbox, versioning policy, idempotency, rate-limit quotas, request logs, error catalog | https://apidocs.sweeppea.com/ | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-040 | POST /participants/add = entry-event ingestion (source, custom fields, bonus entries), supports entries-per-dollar sync | https://apidocs.sweeppea.com/openapi.json | official-doc | 2026-08-18 | HIGH |
| SWEEPPEA-041 | Contests/games administered as human service (judging); platform/API are sweepstakes-centric; no instant-win engine documented | https://www.sweeppeasweeps.com/ | official-marketing | 2026-08-18 | MEDIUM |
| SWEEPPEA-042 | Agency "silent compliance partner"; ~10 client sweeps per dashboard; "Sweepstakes-as-a-Service" | https://www.sweeppea.com/sweepstakes-management-agencies | official-marketing | 2026-08-18 | HIGH |
| SWEEPPEA-043 | Static 50-state + DC law guide; compliance glossary; no machine-readable legal provenance in generated rules | https://www.sweeppeasweeps.com/sweepstakes-and-contest-rules-by-state.html | official-marketing | 2026-08-18 | HIGH |

Full machine-readable ledger: `outputs/evidence/02_sweeppea.jsonl` (43 records).

## 17. Verdict

**SUBSTITUTE**

Sweeppea's "Compliance-as-a-Service" does not cover the proposed J01–J10 wedge as software: there is no customer-authorable policy, no runtime action authorization (it explicitly tells customers to enforce eligibility client-side), no versioning, simulation, replay, or evidence-grade reconstruction, and only embryonic vendor-internal guardrails [SWEEPPEA-014, -017, -028]. But for the promotion vertical it substitutes for the wedge's *outcome*: a brand can pay $3–15K per campaign to transfer rules drafting, AMOE, bonding/registration, drawings, and audit-file custody — plus liability itself via the Independent Administrator role — to a bureau, eliminating the need to buy regulatory decisioning infrastructure for sweepstakes [SWEEPPEA-013, -027]. Any Promotion OS thesis must therefore beat cheap, liability-absorbing service bureaus (Sweeppea, Marden-Kane, National Sweepstakes Co.), not merely out-feature them. Category-A overlap is deep; architectural overlap with the differentiators is near zero; replacement risk LOW.
