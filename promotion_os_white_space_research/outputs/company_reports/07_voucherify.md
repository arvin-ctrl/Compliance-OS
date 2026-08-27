# Company Report — Voucherify

Researcher: Research Agent 07 (Voucherify)
Date: 2026-08-18
Category: Incentive decisioning
Manager: Manager B

## 1. Executive summary

Voucherify (Katowice, Poland + New York; founded ~2015 out of rspective) is an API-first **incentive management and decisioning platform**: coupons/discounts, cart promotions, loyalty programs, referrals, gift cards/store credit, bundles, and digital wallets, delivered as a headless engine that plugs into a merchant's checkout, POS, app, and marketing stack. It brands itself an "Incentive Optimization Engine" with three pillars — incentive decisioning, orchestration, and analytics [VOUCHERIFY-001].

**Who buys it:** enterprise and mid-market marketing/loyalty/digital teams (QSR, retail/ecommerce, travel, fintech, telco), with engineering as co-buyer because integration is API-driven. Named customers include Trainline, easyJet holidays, KFC (Vietnam), Vodafone, Michelin, Breville [VOUCHERIFY-001, -036, -037].

**Job it is hired to do:** decide, in real time at checkout or in a customer touchpoint, *which incentive a given customer/cart is allowed to receive and at what value*, enforce guardrails (budgets, limits, stacking, exclusions), and keep the commercial bookkeeping (codes, balances, points, redemptions) consistent across channels — replacing hard-coded promo logic in commerce platforms [VOUCHERIFY-001, -035].

It is a *commercial-policy* decision engine, not a *regulatory-policy* one: there is no legal content, no jurisdiction semantics, no counsel workflow, and no evidence-grade decision reconstruction. But the mechanical skeleton — synchronous rule evaluation with reason codes, stateful customer context, budget guardrails, enterprise approval workflow, API-call audit logs — overlaps substantially with the proposed Promotion OS decision layer.

## 2. Product architecture

Core runtime loop (documented, not marketing):

**INPUT** — an API call carrying: customer identity (`source_id`) + attributes/metadata; an order object (items, amounts in minor units, item metadata, up to 500 items); the redeemables being attempted (codes, promotion tiers, stacks — up to 30); optional session lock; optional geo coordinates; arbitrary metadata for rule matching [VOUCHERIFY-007, -008].

**DECISION/PROCESS** — Voucherify evaluates, synchronously and server-side:
- **Qualification** (`POST /v1/qualifications`): forward-looking "what could this customer get?" across scenarios (ALL, CUSTOMER_WALLET, AUDIENCE_ONLY, PRODUCTS…), with server-side best-offer sorting (BEST_DEAL) and 5-minute result caching [VOUCHERIFY-006, -007].
- **Validation** (`/validations`): binding eligibility check of specific redeemables against validation rules (audience, product, price, budget, redemption-context, metadata rules with nested AND/OR logic), plus project-level stacking rules (priority by request order or category hierarchy, Always/Never-stackable categories, per-category caps) [VOUCHERIFY-004, -005, -008, -029].
- **Redemption** (`/redemptions`): applies the incentive, mutates state (code use counts, gift-card balance, loyalty points), and records the attempt — success or failure — permanently; rollback is possible for 3 months [VOUCHERIFY-009, -010].

**OUTPUT** — synchronous response: `valid: true/false`; per-redeemable status APPLICABLE / INAPPLICABLE / SKIPPED; structured error objects (code, key, message, details, request_id) and skip reasons (e.g. `exclusion_rules_not_met`, `applicable_redeemables_limit_exceeded`); recalculated order with per-item discount allocation; tracking_id. Side effects (webhooks, segment recalculation, point application) complete asynchronously [VOUCHERIFY-008, -020].

Supporting state: customer 360 object with auto-maintained aggregates (spend, AOV, redemption counts, points, referrals) feeding rules [VOUCHERIFY-024]; projects as isolated environments (per brand/region/stage) [VOUCHERIFY-016]; audit log storing request+response of every API call for 6–12 months [VOUCHERIFY-011].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Promotion engine (coupons + cart promotions) | Code-based and code-free discounts with validation rules, budgets, distribution | Marketing/digital | Core | VOUCHERIFY-001, -004, -016 |
| Qualifications / incentive decisioning | Real-time eligibility + best-offer selection per customer/cart | Marketing + engineering | Core | VOUCHERIFY-006, -007, -035 |
| Validation & redemption APIs | Synchronous allow/deny of specific incentives; stacking; rollback | Engineering | Core | VOUCHERIFY-008, -009, -029 |
| Loyalty (v2) | Members, cards, multi point-wallets, earning rules, tiers, benefits, rewards | Marketing/loyalty | Core | VOUCHERIFY-025 |
| Gift cards / store credit | Balance issuance, top-up, redemption, transactions ledger | Marketing/finance-adjacent | Core | VOUCHERIFY-026, -027 |
| Referral programs | Referrer/referee reward mechanics | Marketing | Core | VOUCHERIFY-001, -016 |
| Gamification (achievements) | Challenges, badges, streaks; UI via partners (Wyng, Brame, Odicci) | Marketing | Add-on/partner | VOUCHERIFY-034 |
| Areas & Stores + Geofencing | Regional campaign scoping, store-level access, coordinate-based location rules | Enterprise ops | Enterprise add-on | VOUCHERIFY-015, -032 |
| Approval requests | Maker-checker on campaigns/vouchers/validation rules | Enterprise governance | Enterprise add-on | VOUCHERIFY-012 |
| Management API | Programmatic projects/users/schemas/webhooks/branding/templates | Platform engineering | Enterprise add-on | VOUCHERIFY-014 |
| Audit log + exports | API request/response logs; CSV exports of core objects | Ops/analytics | Core (advanced filters enterprise) | VOUCHERIFY-011, -028 |
| Vincent (AI agent) | NL campaign creation, offer performance insight | Marketing | Add-on (new) | VOUCHERIFY-035 |

## 4. API / developer capability

- **APIs:** Broad REST API — qualifications, validations, redemptions, campaigns, vouchers, promotions, customers, orders, products, segments, events, exports, locations, loyalty v2, management API [VOUCHERIFY-003]. Region-scoped base URLs (EU/US/Asia + dedicated clusters) [VOUCHERIFY-020].
- **SDKs:** JavaScript/TypeScript, Python, PHP, Java, Ruby, .NET (official marketing, corroborated by public GitHub SDK repos) [VOUCHERIFY-002].
- **Webhooks:** project-level + distribution-level, HMAC-SHA256-signed, 10s response requirement, 12 retries with exponential backoff over 24h, auto-disable, monitored in the audit log; Kafka connectors referenced for event streaming [VOUCHERIFY-019, -034].
- **Sandbox:** every account has a Sandbox project (isolated data, 100 calls/hour); projects generally serve as dev/staging/prod environments [VOUCHERIFY-016, -018].
- **Rules engine:** validation rules (six rule families, nested logic `"(1 and 2) and (3)"`, rich operators, custom per-rule error messages) + separate stacking-rules layer for conflict resolution [VOUCHERIFY-004, -005, -029].
- **Synchronous decisioning:** validation/redemption results returned in the synchronous response; side effects async [VOUCHERIFY-020].
- **Latency claims:** "sub-50 ms API responses", 99.99% uptime, "3,300+ redemptions/minute in a POS with <100 ms" — official but marketing-grade numbers; status page shows 100% 90-day uptime on three AWS regions [VOUCHERIFY-002, -022, -023, -037].
- **Versioning:** dated API versions (current v2018-08-01), per-project pinning, per-request header override, changelog [VOUCHERIFY-017].
- **Idempotency:** *not documented*. No idempotency-key mechanism found in API fundamentals after targeted search; double-processing protection exists narrowly via validation session locks (TTL-based) [VOUCHERIFY-041, -008]. (Labeled inference of absence.)
- **Integration model:** composable/headless — merchant's checkout calls qualify→validate→redeem; CDP/ESP integrations (e.g., Braze Connected Content at Trainline); commerce connectors; AWS Marketplace listing [VOUCHERIFY-036, -021].

## 5. Rules / decision model

- **Arbitrary attributes:** Yes — metadata rules on customers, orders, order items, redemptions, and custom events, typed via metadata schemas [VOUCHERIFY-004, -005].
- **Customer/user state:** Yes — auto-maintained aggregates (spend, orders, redemption counts, points, tiers, referrals) plus static/dynamic segments; state directly referenceable in rules [VOUCHERIFY-024].
- **Reason codes:** Yes on deny — structured error objects with machine keys, failure_code/failure_message on redemptions, skip reasons, and *author-customizable* per-rule error messages. Qualification (the "what's available" path) returns only eligible items, without ineligibility reasons [VOUCHERIFY-005, -008, -010, -006].
- **Allow/deny/review:** Allow/deny (+SKIPPED) only. **No human-review/pending decision state exists** in the decision path; approvals exist only for configuration changes [VOUCHERIFY-008, -012].
- **Simulate policies:** Partial — sandbox projects, documented dry-run practice of full journeys, and qualification as a live "what-would-apply" probe. No what-if simulation of a rule change against historical traffic [VOUCHERIFY-016, -006].
- **Replay decisions:** No replay engine. Redemption records persist; full request/response retrievable from audit log for 6–12 months; validation records kept 30 days. Re-running a validation evaluates *current* rules, not rules-as-of-then [VOUCHERIFY-009, -010, -011].
- **Version policies:** No. Validation rules and campaigns have created_at/updated_at but no exposed version history; the decision record does not link to a policy version [VOUCHERIFY-005, -010].
- **Deploy rules independently of app code:** Yes — rules and campaigns are data, changed in dashboard/API without app deploys; campaign templates copy configurations across projects (staging→production) [VOUCHERIFY-004, -033].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance (sweepstakes/contest law):** None. Campaign types are discount coupons, loyalty, gift, referral, promotions; no sweepstakes/instant-win/drawing mechanics, no official-rules generation, no AMOE, no prize-law content. Gamification is achievements-based; chance-based UIs are delegated to partners (Wyng, Brame, Odicci) [VOUCHERIFY-016, -034]. (Reasoned absence from enumerated feature set.)
- **Generic regulatory workflow:** None as such. The approval-requests feature is a generic maker-checker on promotion configuration (Enterprise) [VOUCHERIFY-012].
- **Jurisdiction restrictions:** Achievable only as *merchant-built convention*: segments/metadata (e.g., country attributes), Areas & Stores regional scoping, per-region projects, and geofencing rules. No jurisdiction ontology, no legal semantics [VOUCHERIFY-004, -015, -032, -016].
- **Location verification:** Geofencing validates merchant-supplied coordinates against drawn boundaries; coordinate-based, not IP-based; **fails open** ("If no location is sent, geofencing rules are skipped"); no spoofing/VPN detection [VOUCHERIFY-015].
- **Legal content/rules:** None — no legal text, terms generation, or statutory rule library anywhere in docs [VOUCHERIFY-003].
- **Regulatory monitoring:** None (blog content only). (Reasoned absence.)
- **Change management:** Good *operational* change control: draft states, approval requests on campaigns/vouchers/validation rules, audit log of every change, campaign templates [VOUCHERIFY-012, -011, -030, -033].
- **Counsel approval:** Approvers are dashboard Admin users; no counsel role, no attestation/sign-off semantics, no external-reviewer support documented [VOUCHERIFY-012].
- **Historical policy state:** Not reconstructable from the product: no rule/campaign version history; audit log allows manual reconstruction of change sequences within 6–12 months only [VOUCHERIFY-005, -011].

## 7. Audit / evidence

Can a customer reconstruct a past decision?

- **Exact inputs:** Yes within retention — audit log stores request+response of every API call (6 months shared / 12 months dedicated); redemption objects permanently embed order, customer, metadata [VOUCHERIFY-011, -010].
- **Exact rule/policy:** No — the decision record does not capture evaluated rules; `validation_rules_assignments` reflect *current* state. Rule content as-of-decision-time must be inferred by manually diffing audit-log change events [VOUCHERIFY-010, -011].
- **Exact version:** No policy versioning exists [VOUCHERIFY-005].
- **Exact output:** Yes — redemption status/result/failure codes persist; validation outcomes retained 30 days; API responses in audit log 6–12 months [VOUCHERIFY-009, -010, -011].
- **Exact timestamp:** Yes — ISO 8601 timestamps on decisions and log entries [VOUCHERIFY-010, -011].
- **Human approvals:** Approval request statuses exist (Pending/Approved/Changes requested/Rejected); durable approval *history* retention is not documented [VOUCHERIFY-012].
- **Source/legal authority:** Not applicable — no legal provenance concept in the product [VOUCHERIFY-003].
- **Integrity:** No immutability/tamper-evidence guarantees documented; marketing's "full audit trails log every decision for compliance" overstates what docs support [VOUCHERIFY-011, -035].

Net: strong *operational* audit (better than most marketing tools), but not evidence-grade — retention-limited, no policy-version linkage, no integrity attestations, no regulator packaging.

## 8. Enterprise readiness

- **SSO/RBAC:** RBAC documented (Admin/User/Viewer/Merchant, per-project roles, Enterprise custom roles) [VOUCHERIFY-013]. SSO/SAML/2FA claimed on enterprise marketing pages; configuration docs not located [VOUCHERIFY-022].
- **Multitenancy/multi-brand:** projects per brand/region with isolated data and keys; Areas & Stores for market/store hierarchies with scoped users and API keys; Management API for programmatic provisioning and branding [VOUCHERIFY-016, -032, -014].
- **Environments:** Sandbox project + project-per-stage pattern + campaign templates copying between projects [VOUCHERIFY-016, -033].
- **Security certifications:** ISO 27001 and GDPR compliance claimed across official pages; SOC 2 not found [VOUCHERIFY-002, -022].
- **SLA:** 99.99% uptime marketed; custom SLA + dedicated AWS cluster for enterprise; status page corroborates (100% 90-day, EU/US/Asia) [VOUCHERIFY-022, -023].
- **Support/professional services:** tiered support (email → premium with personalized integration guidance); partner ecosystem; self-service-capable [VOUCHERIFY-021].
- **Customer scale:** Trainline (45 countries), KFC Vietnam POS/kiosks, easyJet holidays refund-to-gift-card program, Vodafone; vendor-reported 3,300+ redemptions/min POS at <100 ms [VOUCHERIFY-036, -037].

## 9. Commercial model

- **Pricing (public):** Business ~€600/mo (100 calls/min, 25k calls/mo, 3 projects); Organization ~€1,200/mo (200/min, 50k/mo, 5 projects); Enterprise custom (individual hosting, custom limits, advanced governance/security — SSO, audit-log advanced filters, approvals, geofencing, Areas & Stores, Management API are enterprise-tier). 60-day free trial; AWS Marketplace [VOUCHERIFY-021, -018].
- **Likely buyer:** marketing/loyalty leadership with engineering sign-off; procurement lands in martech budget.
- **Implementation burden:** real integration project (checkout/POS calls, customer/product sync, webhooks); "integration blueprint" docs and SDKs reduce it; weeks-to-months for enterprise (inference from integration model + case studies) [VOUCHERIFY-003, -036].
- **Sales motion:** self-serve trial + inside sales for Business/Organization; enterprise sales for the rest. Governance features gated to enterprise on request [VOUCHERIFY-021, -012].
- **Large-customer evidence:** section 8 names; six-times conversion uplift claim at Trainline [VOUCHERIFY-036].

## 10. Strengths

- **Real, documented synchronous decisioning core:** qualification → validation → redemption with structured statuses, machine-readable reason keys, custom per-rule error messages, session locking, rollback — a mature transactional decision API, not a campaign CMS [VOUCHERIFY-006, -007, -008].
- **Deep guardrail/conflict layer:** budget caps (count, amount, per-customer, per-period), stacking policy with category hierarchy priorities and exclusivity — deterministic multi-incentive conflict resolution [VOUCHERIFY-004, -029].
- **Stateful customer context** maintained automatically and usable in rules [VOUCHERIFY-024].
- **Ledgered value:** gift-card and loyalty transactions with type, reason, source, and post-transaction balance; point wallets with expiration; exports [VOUCHERIFY-025, -026, -028].
- **Enterprise governance beyond peers of its size:** approval workflow on campaigns *and validation rules*, RBAC with custom roles, area/store-scoped access, API-call-level audit log, Management API [VOUCHERIFY-011, -012, -013, -014, -032].
- **Developer platform hygiene:** dated API versioning with per-project pinning, documented rate limits with headers, signed webhooks with retries, sandbox, multi-region [VOUCHERIFY-017, -018, -019, -020].

## 11. Weaknesses / constraints

- **No decision-time policy versioning:** decision records don't reference rule versions; rules have no version history — "why was this allowed, under which rules?" is not answerable from the product beyond audit-log archaeology [VOUCHERIFY-010, -005, -011]. (Documented.)
- **Retention-limited evidence:** validations 30 days; API logs 6–12 months; no immutability guarantees [VOUCHERIFY-009, -011]. (Documented.)
- **No review state:** binary allow/deny; no queue for human adjudication of a decision [VOUCHERIFY-008]. (Documented.)
- **Qualification opacity:** eligibility responses omit "why not" reasons and skip several budget rules; 5-minute cache can serve stale eligibility [VOUCHERIFY-006]. (Documented.)
- **Geofencing fails open** and trusts client-supplied coordinates — unsuitable as regulatory location enforcement [VOUCHERIFY-015]. (Documented.)
- **No regulatory content or workflow:** no jurisdiction semantics, legal library, counsel roles, or compliance monitoring [VOUCHERIFY-003, -012]. (Reasoned absence.)
- **Idempotency undocumented** [VOUCHERIFY-041]. (Inference of absence.)
- **Usability/analytics complaints** in reviews (search, UI learning curve, analytics depth) [VOUCHERIFY-040]. (User-report.)
- **API quotas are commercial constraints** — decisioning volume is metered per plan [VOUCHERIFY-018, -021]. (Documented.)

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,VOUCHERIFY-016;VOUCHERIFY-034
A02,0,VOUCHERIFY-016;VOUCHERIFY-034
A03,1,VOUCHERIFY-034
A04,0,VOUCHERIFY-003;VOUCHERIFY-016
A05,0,VOUCHERIFY-003;VOUCHERIFY-016
A06,0,VOUCHERIFY-003;VOUCHERIFY-016
A07,1,VOUCHERIFY-006;VOUCHERIFY-024
A08,0,VOUCHERIFY-016;VOUCHERIFY-034
A09,1,VOUCHERIFY-025;VOUCHERIFY-027
A10,0,VOUCHERIFY-003
B01,4,VOUCHERIFY-006;VOUCHERIFY-007;VOUCHERIFY-008
B02,4,VOUCHERIFY-008;VOUCHERIFY-020
B03,3,VOUCHERIFY-002;VOUCHERIFY-022;VOUCHERIFY-023;VOUCHERIFY-037
B04,2,VOUCHERIFY-008;VOUCHERIFY-010
B05,3,VOUCHERIFY-005;VOUCHERIFY-008;VOUCHERIFY-010
B06,4,VOUCHERIFY-004;VOUCHERIFY-005;VOUCHERIFY-024
B07,4,VOUCHERIFY-024;VOUCHERIFY-025
B08,3,VOUCHERIFY-029
B09,2,VOUCHERIFY-016;VOUCHERIFY-006
B10,1,VOUCHERIFY-009;VOUCHERIFY-010;VOUCHERIFY-011
C01,1,VOUCHERIFY-004;VOUCHERIFY-015;VOUCHERIFY-032
C02,1,VOUCHERIFY-004
C03,1,VOUCHERIFY-004;VOUCHERIFY-008
C04,2,VOUCHERIFY-031
C05,1,VOUCHERIFY-005;VOUCHERIFY-011
C06,0,VOUCHERIFY-003
C07,1,VOUCHERIFY-016;VOUCHERIFY-035
C08,2,VOUCHERIFY-012
C09,0,VOUCHERIFY-003
C10,0,VOUCHERIFY-003;VOUCHERIFY-016
D01,3,VOUCHERIFY-010;VOUCHERIFY-008
D02,3,VOUCHERIFY-009;VOUCHERIFY-010;VOUCHERIFY-011
D03,1,VOUCHERIFY-010
D04,3,VOUCHERIFY-010;VOUCHERIFY-011
D05,2,VOUCHERIFY-012;VOUCHERIFY-011
D06,2,VOUCHERIFY-009;VOUCHERIFY-010;VOUCHERIFY-011
D07,2,VOUCHERIFY-028;VOUCHERIFY-011
D08,2,VOUCHERIFY-009;VOUCHERIFY-011
D09,?,
D10,2,VOUCHERIFY-011
E01,0,VOUCHERIFY-024
E02,1,VOUCHERIFY-024;VOUCHERIFY-004
E03,1,VOUCHERIFY-024
E04,2,VOUCHERIFY-015
E05,0,VOUCHERIFY-007;VOUCHERIFY-008
E06,0,VOUCHERIFY-015
E07,1,VOUCHERIFY-004;VOUCHERIFY-035
E08,?,
E09,0,VOUCHERIFY-008;VOUCHERIFY-012
E10,1,VOUCHERIFY-024;VOUCHERIFY-034
F01,4,VOUCHERIFY-025;VOUCHERIFY-027
F02,3,VOUCHERIFY-026;VOUCHERIFY-025
F03,2,VOUCHERIFY-026
F04,3,VOUCHERIFY-025;VOUCHERIFY-027;VOUCHERIFY-001
F05,3,VOUCHERIFY-031;VOUCHERIFY-025;VOUCHERIFY-028
F06,2,VOUCHERIFY-027
F07,4,VOUCHERIFY-008;VOUCHERIFY-004
F08,3,VOUCHERIFY-026
F09,3,VOUCHERIFY-025
F10,1,VOUCHERIFY-034;VOUCHERIFY-019
G01,3,VOUCHERIFY-016;VOUCHERIFY-032;VOUCHERIFY-014
G02,3,VOUCHERIFY-013
G03,2,VOUCHERIFY-022
G04,3,VOUCHERIFY-012
G05,3,VOUCHERIFY-016;VOUCHERIFY-033
G06,2,VOUCHERIFY-016;VOUCHERIFY-006
G07,3,VOUCHERIFY-012;VOUCHERIFY-011;VOUCHERIFY-030;VOUCHERIFY-033
G08,3,VOUCHERIFY-019
G09,3,VOUCHERIFY-021;VOUCHERIFY-022;VOUCHERIFY-023
G10,3,VOUCHERIFY-002;VOUCHERIFY-022
H01,4,VOUCHERIFY-003;VOUCHERIFY-007;VOUCHERIFY-008
H02,3,VOUCHERIFY-002;VOUCHERIFY-003
H03,3,VOUCHERIFY-019
H04,3,VOUCHERIFY-016;VOUCHERIFY-018
H05,3,VOUCHERIFY-017
H06,1,VOUCHERIFY-041;VOUCHERIFY-008
H07,3,VOUCHERIFY-018
H08,3,VOUCHERIFY-011
H09,2,VOUCHERIFY-033;VOUCHERIFY-028;VOUCHERIFY-014
H10,2,VOUCHERIFY-014
I01,1,VOUCHERIFY-022;VOUCHERIFY-011
I02,4,VOUCHERIFY-001;VOUCHERIFY-002;VOUCHERIFY-003
I03,4,VOUCHERIFY-001;VOUCHERIFY-036
I04,1,VOUCHERIFY-035
I05,3,VOUCHERIFY-036;VOUCHERIFY-037;VOUCHERIFY-002
I06,3,VOUCHERIFY-021
I07,2,VOUCHERIFY-021;VOUCHERIFY-022
I08,3,VOUCHERIFY-036;VOUCHERIFY-025
I09,2,VOUCHERIFY-003;VOUCHERIFY-036
I10,3,VOUCHERIFY-021
J01,1,VOUCHERIFY-004;VOUCHERIFY-005
J02,1,VOUCHERIFY-012;VOUCHERIFY-033
J03,1,VOUCHERIFY-012
J04,0,VOUCHERIFY-006;VOUCHERIFY-003
J05,2,VOUCHERIFY-008;VOUCHERIFY-037
J06,1,VOUCHERIFY-024
J07,1,VOUCHERIFY-010;VOUCHERIFY-011
J08,1,VOUCHERIFY-011;VOUCHERIFY-009
J09,1,VOUCHERIFY-033
J10,1,VOUCHERIFY-030;VOUCHERIFY-012
```

**Notes on 0, 1, and ? scores (reasoning, inference labeled):**

- **A01/A02/A06/A08 = 0:** Voucherify's own docs enumerate its five campaign types (discount coupons, loyalty cards, gift vouchers, referral codes, voucher-free promotions) and its gamification page enumerates achievement mechanics while explicitly delegating gamified UIs to partners — positive evidence that sweepstakes/contests/drawings/AMOE are outside the product. A04/A05/A10 = 0 on the same enumeration basis: no legal-content, rules-drafting, or tax features anywhere in docs. *Inference from enumerated feature set, labeled as such.*
- **A03/A07/A09 = 1:** peripheral adaptability only — partners deliver instant-win-style UIs on top of Voucherify's reward engine; custom events/publications could log "entries"; loyalty rewards include material items but fulfillment is the merchant's.
- **C06/C09/C10 = 0:** no regulatory monitoring, legal provenance, or legal policy library exists anywhere in documentation or marketing; the product has no legal content at all. *Reasoned inference of absence.*
- **B10 = 1, D03 = 1:** documented positively — the redemption schema does not reference evaluated rules or versions; validation data kept 30 days; audit log inspection is the only (manual, retention-limited) replay path.
- **E01/E05/E06/E09 = 0:** customer data is merchant-supplied and unverified (E01); request schemas contain no device signals (E05); geofencing docs state rules are skipped when no location is sent, i.e., the architecture trusts and fails open (E06); the decision model has no review state and approvals apply only to configuration, so no decision case management exists (E09). *Reasoned inference anchored to documented schemas/behavior.*
- **J04 = 0:** nothing resembling pre-rollout impact analysis exists; qualification is a forward-looking runtime probe with 5-minute cache, and testing guidance is sandbox-based QA. *Reasoned inference.*
- **H06 = 1:** idempotency keys undocumented (targeted search); session locks give partial double-processing protection. *Inference of absence.*
- **I01 = 1, I04 = 1:** governance/guardrail features exist but no legal/compliance or fraud buyer motion is visible; buyers are marketing/digital/engineering.
- **I08 = 3, I09 = 2:** *inference* — switching cost from embedded checkout integration plus stored-value balances (gift cards, points) and multi-team adoption (Trainline); integration burden is a real engineering project mitigated by SDKs/blueprints.
- **D09 = ?:** no information on tamper-evidence/integrity features either way. **E08 = ?:** referral/duplicate-account safeguards may exist but were not documented in researched sources.
- **G03 = 2:** SSO/SAML/2FA are claimed on official marketing but no configuration docs were located; kept below 3 per evidence standard.
- **B03 = 3 not 4:** latency figures (sub-50 ms, <100 ms POS) are marketing-grade; corroborated by enterprise POS case studies and status page, but no benchmark documentation.

## 13. White-space implications

1. **Already solved (by Voucherify, within the commercial-incentive domain):** real-time synchronous rule evaluation with reason codes (J05's mechanical core for one action type: granting/applying incentives); stateful customer context; budget/stacking guardrails; config-change governance (approvals, RBAC, audit log of changes); multi-region/multi-brand scoping; developer platform (API/SDK/webhooks/sandbox/versioning).
2. **Partially solved:** decision logging and reconstruction (inputs/outputs recoverable 6–12 months via audit log; permanent redemption records — but no policy-version linkage, limited retention, no integrity guarantees) [J07/J08 ≈ partial]; approval workflow (generic maker-checker that a legal team *could* be inserted into, without counsel semantics or attestation) [J02/J03 partial]; temporal rules (incentive validity windows, not legal effective dating) ; location rules (geofencing that fails open); reusable configuration (campaign templates internal to a customer) [J09 partial].
3. **Unsolved:** jurisdiction-aware regulatory rule content (J01); legal-to-production workflow with counsel as first-class approver (J02/J03); regulatory impact analysis (J04); cross-vendor identity/geo/fraud signal normalization (J06 — Voucherify consumes only merchant-supplied attributes); evidence-grade reconstruction and historical "why was this allowed?" replay with policy versions (J07/J08); policy packs/regulatory content network (J09); regulatory lifecycle control plane (J10); everything in category A (sweepstakes administration) and E (verification/risk signals).
4. **Could Voucherify add the missing capability easily?** Mechanically, some of it: policy versioning + decision-version linkage is an engineering increment on an existing rules platform; counsel-approver roles are a small extension of approval requests. But regulatory *content* (jurisdiction packs, legal provenance, monitoring) is a different competency and a different buyer (legal/compliance vs marketing), and evidence-grade retention/integrity conflicts with current 30-day/6-12-month retention economics. Their roadmap direction is AI offer optimization (Vincent), not compliance. Moderate capability, low apparent intent. *(Inference.)*
5. **Could a customer assemble it with Voucherify + internal engineering?** Partially. A sophisticated enterprise could encode state/jurisdiction restrictions as segments/metadata validation rules, feed external KYC/geo/fraud results in as metadata, gate changes through approval requests, and archive audit-log exports for evidence. Gaps that remain the customer's problem: rule content and legal maintenance, policy versioning/replay, fail-open geofencing, no review state, qualification's ignored budget rules, retention limits, and the fact that none of it carries legal provenance. This is exactly the "current vendor + internal engineering + outside counsel" baseline the enterprise-switch standard demands we beat.
6. **What would make a customer buy a separate product instead?** (a) A regulated action surface broader than incentives (account opening, prize award, wager, cross-product gating) that Voucherify cannot authorize; (b) auditor/regulator demands for decision reconstruction with policy versions and integrity guarantees beyond 6–12 months; (c) counsel-owned rule content with provenance and update service (statutory change monitoring); (d) a legal/compliance budget owner who will not run compliance logic inside the marketing team's promo tool; (e) signal verification (identity/age/location) that Voucherify structurally trusts rather than verifies.

## 14. Replacement risk

**MEDIUM.**

Voucherify already owns the hardest runtime asset — a production-grade, low-latency, stateful rules-decision engine with guardrails, approvals, and audit logs — plus enterprise distribution in exactly the verticals (QSR, travel, retail, fintech) where promotion regulation bites. If "regulatory decisioning for promotions" proved a budgeted category, Voucherify could ship a credible v1 (counsel approver role, rule versioning, extended log retention, jurisdiction rule templates) faster than most. Three factors cap the risk at MEDIUM rather than HIGH: (1) its buyer and roadmap are marketing-side (Vincent AI, offer optimization), not legal; (2) evidence-grade auditability and verified signals require architectural and content investments (retention, integrity, legal sourcing) with no visible groundwork; (3) its decision scope is confined to its own incentive objects — it is not positioned as a cross-product authorization layer, and repositioning would put it against policy-infrastructure vendors it does not resemble today. *(Assessment is inference from documented capability + positioning.)*

## 15. Adjacent discoveries

- **Eagle Eye (eagleeye.com)** — enterprise real-time promotions/loyalty execution (AIR platform; Tesco, Woolworths, Carrefour; "1.7B+ personalized offers weekly"). The up-market substitute for Voucherify-class decisioning at grocery scale; any promotion-decisioning white-space claim must survive Eagle Eye's existence [VOUCHERIFY-038].
- **Antavo (antavo.com)** — API-first enterprise loyalty platform (KFC, PUMA, Hyatt); competes for the same loyalty budget and shows how crowded the incentive-engine layer is [VOUCHERIFY-039].
- **Wyng, Brame, Odicci** — Voucherify's own gamification UI partners; they carry the interactive/chance-flavored promotion experiences (spin-to-win style) on top of reward engines, sitting between promotion administration (category A) and incentive engines [VOUCHERIFY-034].
- **Braze (and CDPs/ESPs generally)** — distribution complement observed in the Trainline stack; relevant because incentive decisioning increasingly gets consumed *through* engagement platforms [VOUCHERIFY-036].

## 16. Evidence ledger

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| VOUCHERIFY-001 | Core product: "Incentive Optimization Engine" with decisioning/orchestration/analytics + promo, loyalty, referral, gift card, bundling, wallet, gamification modules; enterprise marketing/loyalty buyer | https://www.voucherify.io/ | official-marketing | 2026-08-18 | HIGH |
| VOUCHERIFY-002 | API-first; SDKs in 6 languages; sub-50ms, 99.99% uptime, ISO 27001, GDPR; clients incl. Trainline, KFC, Vodafone, easyJet | https://www.voucherify.io/ | official-marketing | 2026-08-18 | MEDIUM |
| VOUCHERIFY-003 | Docs index enumerates full API/feature surface (validation rules, qualifications, redemptions, campaigns, loyalty, exports, webhooks, management API, approvals, geofencing) | https://docs.voucherify.io/llms.txt | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-004 | Validation rules: six families incl. audience, product/cart, price, budget limits, redemption context, metadata rules | https://docs.voucherify.io/optimize/validation-rules-reference.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-005 | Rule object: nested logic expressions, rich operators, basic/advanced/complex types, custom per-rule error messages; no version history | https://docs.voucherify.io/api-reference/validation-rules/validation-rule-object.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-006 | Qualifications API: eligibility scenarios, 5-min cache, ignores several budget rules, returns eligible items without ineligibility reasons | https://docs.voucherify.io/guides/checking-eligibility.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-007 | POST /v1/qualifications: customer+order+scenario+filters ($is/$in/junctions), BEST_DEAL sorting, per-item applicability, tracking_id | https://docs.voucherify.io/api-reference/qualifications/check-eligibility.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-008 | Validate stackable: ≤30 redeemables, APPLICABLE/INAPPLICABLE/SKIPPED, structured errors (key, request_id), skip reasons, session LOCK with TTL | https://docs.voucherify.io/api-reference/validations/validate-stackable-discounts.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-009 | Validations stored 30 days; all redemption attempts recorded (success/fail/reverted); rollback within 3 months | https://docs.voucherify.io/optimize/validations-and-redemptions.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-010 | Redemption object: id, timestamps, status, failure_code/message, channel, order, customer; does NOT record evaluated rules or config version | https://docs.voucherify.io/api-reference/redemptions/get-redemption.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-011 | Audit log: request+response of every API call; 6mo shared / 12mo dedicated retention; filters + export; no immutability claims | https://docs.voucherify.io/analyze/audit-logs.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-012 | Approval requests (Enterprise): gate campaigns/vouchers/validation rules; ≤5 Admin approvers; one approval suffices; 5 statuses | https://docs.voucherify.io/manage/approval-requests.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-013 | RBAC: Admin/User/Viewer/Merchant, per-project roles, Enterprise custom roles | https://docs.voucherify.io/manage/members-and-roles.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-014 | Management API (Enterprise): programmatic projects, users, schemas, stacking rules, webhooks, branding, templates | https://docs.voucherify.io/guides/management-api.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-015 | Geofencing (Enterprise): coordinate-based, merchant-supplied `geo:lat,long`; rules skipped if no location sent | https://docs.voucherify.io/orchestrate/geofencing.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-016 | Projects = isolated environments (brand/region/stage) incl. Sandbox; validation rules reusable; 5 campaign types enumerated | https://docs.voucherify.io/docs/key-concepts | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-017 | Dated API versioning (v2018-08-01), project pinning, header override, changelog | https://docs.voucherify.io/api-reference/versioning.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-018 | Rate limits per plan + rate-limit headers; sandbox 100 calls/hr | https://docs.voucherify.io/guides/limits.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-019 | Webhooks: HMAC-SHA256 signed, 12 retries/24h, 10s timeout, audit-log monitoring | https://docs.voucherify.io/api-reference/introduction-to-webhooks.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-020 | Regional endpoints (EU/US/AS + dedicated); synchronous decision result with async side effects | https://docs.voucherify.io/guides/api-overview.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-021 | Public pricing tiers with API-call quotas; 60-day trial; enterprise = custom hosting/governance; AWS Marketplace | https://www.voucherify.io/pricing | official-marketing | 2026-08-18 | HIGH |
| VOUCHERIFY-022 | Enterprise page: ISO 27001, GDPR, sub-50ms, 99.99%, approvals/change tracking, SSO/SAML/2FA, dedicated AWS cluster, custom SLA | https://www.voucherify.io/enterprise | official-marketing | 2026-08-18 | MEDIUM |
| VOUCHERIFY-023 | Status page: 3 AWS regions, 100% 90-day API uptime as of access date | https://status.voucherify.io/ | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-024 | Customer object auto-maintains aggregates (spend, AOV, redemptions, points, referrals) + metadata; segments | https://docs.voucherify.io/api-reference/customers/customer-object.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-025 | Loyalty v2: members/cards/point wallets/card definitions (pending points, expiration, pay-with-points), earning rules, 10-level tiers, transactions APIs | https://docs.voucherify.io/guides/loyalty-v2-overview.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-026 | Card transactions ledger: type, balance-after, created_at, source_id, reason; types Redemption/Refund/Addition; CSV export | https://support.voucherify.io/article/585-transactions | official-doc | 2026-08-18 | MEDIUM |
| VOUCHERIFY-027 | Gift cards: initial amount, top-up/redeem with real-time balance updates, validation-rule restrictions | https://docs.voucherify.io/build/gift-card-overview.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-028 | Exports API: vouchers/redemptions/publications/customers/orders/point expirations, filters, async generate+download | https://docs.voucherify.io/guides/csv-export.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-029 | Stacking rules: ALL/Partial policy, priority by request order or category hierarchy, exclusivity categories, 30/30/5 limits | https://docs.voucherify.io/orchestrate/stacking-rules.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-030 | Campaign states: Draft/Active/Disabled/Deleted | https://docs.voucherify.io/build/campaign-overview.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-031 | Voucher temporal controls: start/expiration, recurring validity timeframes, day-of-week, daily hours | https://docs.voucherify.io/api-reference/vouchers/voucher-object.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-032 | Areas & Stores (Enterprise): area/store campaign assignment; users and API keys scoped to areas/stores | https://docs.voucherify.io/orchestrate/areas-and-stores.md | official-doc | 2026-08-18 | HIGH |
| VOUCHERIFY-033 | Campaign templates: save/reuse configs, copy campaigns between projects in same cluster | https://support.voucherify.io/article/620-campaign-templates | official-doc | 2026-08-18 | MEDIUM |
| VOUCHERIFY-034 | Gamification = achievements only; UI via partners Wyng/Brame/Odicci; no sweepstakes/instant-win mechanics; Kafka connectors | https://www.voucherify.io/gamification-software | official-marketing | 2026-08-18 | HIGH |
| VOUCHERIFY-035 | Incentive decisioning marketing: real-time best-offer, guardrails, "full audit trails log every decision", fraud-attempt visibility, Vincent AI | https://www.voucherify.io/incentive-decisioning | official-marketing | 2026-08-18 | MEDIUM |
| VOUCHERIFY-036 | Trainline case study: Braze integration, geo targeting, metadata tagging, 6x purchase likelihood, multi-team rollout | https://www.voucherify.io/customers/trainline | case-study | 2026-08-18 | HIGH |
| VOUCHERIFY-037 | KFC Vietnam kiosk/mobile/POS usage; easyJet gift-card refunds; 3,300+ redemptions/min at <100 ms (vendor-reported) | https://www.voucherify.io/enterprise | official-marketing | 2026-08-18 | MEDIUM |
| VOUCHERIFY-038 | Adjacent: Eagle Eye AIR — enterprise real-time promotions/loyalty at grocer scale (Tesco, Woolworths; 1.7B offers/week) | https://www.eagleeye.com/ | official-marketing | 2026-08-18 | HIGH |
| VOUCHERIFY-039 | Adjacent: Antavo — API-first enterprise loyalty platform (KFC, PUMA, Hyatt) | https://antavo.com/ | official-marketing | 2026-08-18 | HIGH |
| VOUCHERIFY-040 | Review pain points: weak search, non-intuitive UI, shallow analytics, promo-setup flexibility requests | https://www.capterra.com/p/152431/Voucherify/reviews/ | user-report | 2026-08-18 | MEDIUM |
| VOUCHERIFY-041 | Idempotency keys not documented in API fundamentals (inference of absence); session locks provide partial protection | https://docs.voucherify.io/guides/api-overview.md | official-doc | 2026-08-18 | MEDIUM |

## 17. Verdict

**MAJOR OVERLAP**

Voucherify has already built most of the *mechanical* decision layer the Promotion OS hypothesis proposes: synchronous, low-latency, stateful rule evaluation with machine-readable reason codes, budget and stacking guardrails, approval-gated configuration changes, RBAC, regional scoping, and API-call-level audit logs — all documented, enterprise-deployed, and buyable today. A sophisticated enterprise could stretch it to encode some jurisdiction restrictions via metadata rules and gate them through approvals. But the overlap stops at the regulatory layer: no legal content or provenance, no counsel workflow semantics, no policy versioning, no decision-to-policy-version linkage, retention-limited logs without integrity guarantees, fail-open location checks, unverified merchant-supplied signals, and a decision scope confined to its own incentive objects for a marketing buyer. It is strong evidence that generic real-time promotion decisioning is a solved, crowded market — any white space must sit strictly in the regulatory/evidence/counsel layer above it.

*(≤150 words)*
