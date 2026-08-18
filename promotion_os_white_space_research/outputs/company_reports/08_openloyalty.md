# Company Report — Open Loyalty

Researcher: Research Agent 08 (Open Loyalty)
Date: 2026-08-18
Category: Loyalty / campaign engine
Manager: Manager B

## 1. Executive summary

Open Loyalty (openloyalty.io; company created inside Divante, Wrocław, Poland; EUR 2.3M R&D funding) is a **headless, API-first loyalty and gamification engine** sold as sales-led enterprise SaaS. Its actual core product is an **event-ingestion + rules + wallet-ledger system**: brands send transactions and custom events over REST, campaigns (rules with triggers, conditions, effects) evaluate them, and the engine mutates member state — points/units in multi-wallets, tiers, badges, rewards, coupons — with webhooks and daily data exports notifying surrounding systems (OPENLOYALTY-001, -004, -011, -018).

**Who buys it:** marketing/loyalty teams plus engineering/platform teams at mid-size-to-large B2C and B2B brands — retail (ALDO, Intersport), beverage/tobacco (Heineken Vietnam, JTI across 18 countries, BAT across Europe and America), banking/insurance (Asia Commercial Bank, Warba Bank, Prudential Vietnam, EFU Life), telecom, fuel, sports (U.S. Soccer, Club Brugge) (OPENLOYALTY-029). Claimed base: "100+ enterprise brands," ~1B loyalty events/month (OPENLOYALTY-001, -002).

**Job it is hired to do:** run the loyalty/incentive back end — earn/burn logic, gamification, and the value ledger — behind the customer's own front ends, replacing homegrown loyalty engines without replacing the rest of the stack. It is **not** hired for promotions-law compliance, action authorization, or regulatory evidence; nothing in the documented product addresses those jobs (OPENLOYALTY-043).

## 2. Product architecture

Concretely, the loop is:

**INPUT** → REST API events: purchase/return transactions (`POST /api/{storeCode}/transaction`), admin-defined **custom events** with schemas, internal lifecycle events (registration, tier change, profile update), redemption codes, scheduled automation triggers (daily/weekly/monthly/birthday/anniversary) (OPENLOYALTY-004, -045, -034).

**DECISION/PROCESS** → **Campaigns** evaluate the event against rules (max 6 rules / 30 conditions per campaign). Conditions test member state (tier, history, custom attributes, per-wallet balances, consents, address incl. country), transaction items (SKU/category/brand/labels), and event payloads; a Symfony-Expression-based language covers cases premade conditions don't (OPENLOYALTY-005, -007, -008). Campaign limits enforce per-member frequency caps and global/per-member unit budgets (OPENLOYALTY-006). Multiple campaigns on one trigger execute in Campaign Start Date order (OPENLOYALTY-010). **Evaluation is asynchronous relative to the API call**: the ingestion response confirms the event; effects arrive afterward via state change and the `CampaignEffectWasApplied` webhook (OPENLOYALTY-011).

**OUTPUT** → Effects, not decisions: add/deduct units to a wallet, give reward/coupon, set/remove member custom attribute, grant badge, assign tier (OPENLOYALTY-005). Downstream visibility comes from ~20 webhook event types (HMAC-SHA256 signed) and daily CSV delta exports to customer S3/GCS/Azure, including **campaign-execution records with the triggering context data** and per-effect result rows (OPENLOYALTY-012, -013, -016, -017, -018).

State containers: **Members** (profiles, custom fields, segments with 27 condition types, timeline), **Wallets** (multi-wallet, custom units, 5 expiration modes, pending/blocked/locked states, optional negative balance), **Unit transfers** (the ledger), **Tiers/Achievements/Badges/Leaderboards** (progress state), **Tenants** (per-country/brand isolation with own currency and timezone) (OPENLOYALTY-008, -025, -026, -033, -019). Legacy architecture (the retired open-source edition) was Symfony + Broadway CQRS/event sourcing; the current SaaS is closed source (OPENLOYALTY-031).

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Campaign engine (campaigns, referral campaigns, automations) | Event-triggered rules granting units/rewards/attributes/tiers; budgets & frequency caps; simulation | Marketing + engineering | Core | OPENLOYALTY-004, -005, -006, -009, -034 |
| Points/wallets & unit transfers | Multi-wallet balances, custom units, expirations, pending, ledger of transfers (add/spend/block/expire/cancel) | Marketing/finance | Core | OPENLOYALTY-025, -026 |
| Gamification (achievements, challenges, badges, leaderboards, fortune wheels) | Progress tracking, rankings with rewarding cycles, probability-based instant-win games with inventory/budget guards | Marketing | Core | OPENLOYALTY-035, -047 |
| Tiers | Tier sets, conditions, benefits, analytics | Marketing | Core | OPENLOYALTY-047 |
| Rewards & redemption | Reward catalog, coupons, unit costs, redemption status lifecycle, eligibility lists, fulfillment status changes | Marketing/ops | Core | OPENLOYALTY-044 |
| Members & segmentation | Profiles, custom field schemas, 27-condition segments, GDPR anonymize/delete | Marketing | Core | OPENLOYALTY-033, -036 |
| Integrations & data exchange | Webhooks (HMAC, SQS), Braze partner integration, Lambda/Zapier/EventBridge/Kafka examples, imports/exports, daily S3/GCS/Azure exports, MCP server for AI agents | Engineering | Core | OPENLOYALTY-012, -013, -018, -032, -042 |
| Administration & governance | Multi-tenant stores, RBAC/ACL, OIDC SSO, audit log + archives, translations, config duplication/exports | Engineering/IT | Core | OPENLOYALTY-014, -019, -021, -022, -037 |
| Analytics | Dashboards, tier/units/campaign analytics APIs, billable usage reports | Marketing | Core | OPENLOYALTY-046 |

No separately-priced modules are documented; pricing is platform fee + active-member allowance with "no feature limits" (OPENLOYALTY-028).

## 4. API / developer capability

- **APIs:** Full public REST reference, 300+ endpoints across ~30 tags (members, points, wallets, campaigns, custom events, segments, tiers, rewards, audit, ACL, analytics, webhooks, imports/exports, tenants, bulk actions, health) (OPENLOYALTY-046). Admin-token, member-token, and API-key authentication.
- **SDKs:** None official; Postman collections; a notable **MCP server** exposing 145 API tools to AI agents (OPENLOYALTY-046, -032).
- **Webhooks:** ~20 event types; HMAC-SHA256 signatures with one-time secrets and rotation endpoint; direct-to-AWS-SQS delivery option (OPENLOYALTY-012, -013, -042).
- **Sandbox:** Dedicated staging environment (PoC/testing, no SLA, 50 req/s, "PII is not recommended") separate from production (OPENLOYALTY-003).
- **Rules engine:** Trigger→conditions→effects campaigns plus Symfony-Expression meta-language for custom conditions/effects (500-char cap) (OPENLOYALTY-005, -007).
- **Synchronous decisioning:** **Not the model.** Event ingestion returns synchronously; campaign effects apply asynchronously and surface via webhooks/exports. The only synchronous rule evaluation endpoint is the campaign **simulator** (OPENLOYALTY-011, -009).
- **Latency claims:** "120 ms avg API response time" (marketing); production soft limit 1,200 concurrent req/s; auth endpoints 20→40 RPM; 30s timeout (OPENLOYALTY-002, -003, -024).
- **Versioning:** "Updates will not break backward compatibility"; versioned endpoints; 3-month migration window; staged rollout staging→production, zero-downtime (OPENLOYALTY-023).
- **Idempotency:** Unresolved. Best practices advise idempotent POST/PATCH design and retries with backoff, but no Idempotency-Key header or documented duplicate rejection (e.g., on transaction `documentNumber`) was found (OPENLOYALTY-041).
- **Integration model:** Headless: customer builds all front ends and connects POS/eCommerce/CRM/CDP via REST + webhooks + daily warehouse exports; Braze is a documented bidirectional partner integration (OPENLOYALTY-002, -042). Third-party assessment: integration "demands developer resources," weeks-to-months implementations (OPENLOYALTY-038).

## 5. Rules / decision model

- **Arbitrary attributes?** Largely yes: member custom attributes, custom field schemas, transaction labels/items, custom event schema fields, all reachable in expressions (OPENLOYALTY-008, -045). Constraint: 6 rules/30 conditions per campaign, 500-char expressions (OPENLOYALTY-005, -024).
- **Customer/user state?** Yes — core strength: profiles, multi-wallet balances (active/spent/locked/blocked/expired), tiers, achievement progress, transaction history, segments, consents (OPENLOYALTY-008, -025, -033).
- **Reason codes?** No real-time reason codes. Post-hoc: execution records carry `executionStatus` (success/skipped/failed), failure `message`, and per-effect status/error in exports; the simulator shows which criteria were met (OPENLOYALTY-016, -017, -009).
- **Allow/deny/review output?** **No.** Effects are grants (units/rewards/attributes/tiers); there is no authorization verdict in the request path (OPENLOYALTY-005, -011).
- **Simulate policies?** Yes — campaign simulator (UI + API), single member/scenario at a time, auto-importing stored member data by ID (OPENLOYALTY-009).
- **Replay decisions?** No. Executions are logged with triggering context data, but there is no re-evaluation of a past event under past configuration (OPENLOYALTY-016; absence of any replay feature: OPENLOYALTY-043).
- **Version policies?** No campaign versioning/draft/rollback documented; audit log records that changes happened (who/when/what entity) but not full config diffs or restorable versions (OPENLOYALTY-005, -014, -015).
- **Deploy rules independently of app code?** Yes — campaigns are configuration changed in the admin panel or via API at runtime, decoupled from customer code; cross-environment promotion is manual via configuration exports with dependency sequencing (OPENLOYALTY-002, -037).

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance:** None. No official rules, AMOE, winner drawing certification, prize-tax, or eligibility-law features anywhere in the documented surface (OPENLOYALTY-043). Fortune-wheel guardrails (inventory, budget, win limits) are business controls, not legal ones (OPENLOYALTY-035).
- **Generic regulatory workflow:** None (no review queues, no attestations) (OPENLOYALTY-043).
- **Jurisdiction restrictions:** Achievable only **mechanically**: conditions/segments on `customer.address.country/province/postal`, and per-country tenants with own currency/timezone (used by JTI across 18 countries). No legal semantics attached (OPENLOYALTY-008, -033, -019, -029).
- **Location verification:** None — address is declared member data; no geolocation, IP, or device checks (OPENLOYALTY-008, -043).
- **Legal content/rules:** None; consents exist only as three boolean member fields (OPENLOYALTY-036).
- **Regulatory monitoring:** None (OPENLOYALTY-043).
- **Change management:** Vendor-side is strong (backward-compat guarantee, staged rollouts); customer-side is thin — config exports/duplication without versioning, diffing, or approvals (OPENLOYALTY-023, -037).
- **Counsel approval:** No approval workflow of any kind; ACL has only View/Modify levels (OPENLOYALTY-021, -043).
- **Historical policy state:** Not reconstructable as a product feature; audit log gives change events, not point-in-time configuration (OPENLOYALTY-014, -015).

## 7. Audit / evidence

Can a customer reconstruct, for a given campaign firing:

- **Exact inputs?** Largely yes — `contextData` ("member's data, transaction data" that triggered the campaign) is captured per execution in the daily export (OPENLOYALTY-016).
- **Exact rule/policy?** Partially — `campaignId` is linked, but with no campaign versioning the rule *as configured at execution time* is only inferable if unchanged since (OPENLOYALTY-016, -005).
- **Exact version?** No (no policy/config versioning) (OPENLOYALTY-005, -043).
- **Exact output?** Yes — per-effect result rows (type, points, couponValue, rewardId, walletCode, status, error) plus the unit-transfer ledger and reward status-change history (OPENLOYALTY-017, -026, -044).
- **Exact timestamp?** Yes — `executedAt`/`createdAt` per execution and per transfer; tenant-timezone semantics documented (OPENLOYALTY-016, -020).
- **Human approvals?** No approvals exist; admin *actions* (member-data changes, ACL/admin changes, auth events, exports) are logged with user, IP, entity, timestamp, filterable and CSV-exportable via `GET /api/audit/log` + archive endpoints (OPENLOYALTY-014, -015).
- **Source/legal authority?** No such concept (OPENLOYALTY-043).

Retention controls and tamper-evidence/immutability of logs are **not documented** (left `?`). A dormant Hyperledger "loyalty-blockchain" side project exists but is not part of the product (OPENLOYALTY-031).

## 8. Enterprise readiness

- **SSO/RBAC:** OIDC SSO (Okta, Entra ID) for admins; custom roles with View/Modify per resource, API-manageable (OPENLOYALTY-022, -021).
- **Multitenancy/multi-brand:** Tenants with own currency, code, timezone, members, campaigns, rewards; global admins/roles/config; config duplication across tenants; "separate tenants per country/project" (OPENLOYALTY-019, -037, -028).
- **Environments:** Staging + production; five production AWS regions (Dublin, Frankfurt, Ohio, Singapore, Sydney); data-residency options Europe/APAC/North America (OPENLOYALTY-003, -028).
- **Security certifications:** ISO 27001 + ISO 9001 (DEKRA, since 2022, renewed 2025), OWASP Top-10/CWE-25 testing, GDPR/CCPA claims, encryption at rest/in transit, per-customer Kubernetes namespaces. **No SOC 2 found** (OPENLOYALTY-027, -028).
- **SLA:** Docs: 99.9% uptime; pricing/marketing: 99.99%, P1 response <30 min, resolution <2 h, 24/7 monitoring (discrepancy noted) (OPENLOYALTY-003, -028, -002).
- **Support/professional services:** Loyalty Experts, Customer Success Managers, Technical Consultants included by package; implementation still requires customer developers (OPENLOYALTY-028, -038).
- **Customer scale:** JTI 18 countries; BAT Europe+America; ALDO global rollout in 3 months; banks/insurers/telcos; 1B events/month claim (OPENLOYALTY-029, -002).

## 9. Commercial model

- **Pricing:** Not published. Platform Fee + Allowance Fee scaled by monthly Active Members ("a Registered Member who performs at least one Loyalty Event per calendar month"); all tiers route to sales (OPENLOYALTY-028, -038).
- **Likely buyer:** Marketing/loyalty leadership with engineering/platform sign-off; no legal, compliance, or fraud buyer motion exists (OPENLOYALTY-001, -043).
- **Implementation burden:** High for a SaaS — headless model requires the customer to build member-facing experiences and integrations; third parties report weeks-to-months deployments (OPENLOYALTY-038).
- **Sales motion:** Sales-led enterprise with included services; no self-serve tier or public trial (OPENLOYALTY-028, -038).
- **Large-customer evidence:** Extensive named enterprise case studies incl. regulated-industry operators (tobacco, alcohol, banking, insurance, fuel) (OPENLOYALTY-029).

## 10. Strengths

- **Event-driven rules + rich customer state**, the strongest overlap area: six trigger classes, custom event schemas, expression language over member/transaction/event/wallet context (OPENLOYALTY-004, -007, -008, -045).
- **True value ledger:** multi-wallet units with expirations, pending, blocking, transfer-level ledger, budget linkage back to campaigns, cancellation returning units to campaign pools (OPENLOYALTY-025, -026, -006, -017).
- **Operational multi-region, multi-tenant SaaS:** 5 AWS regions, data residency options, tenant-per-country model with timezone-correct rule evaluation (OPENLOYALTY-003, -019, -020).
- **Developer platform hygiene:** full public API reference, backward-compat guarantee with 3-month migrations, documented limits, HMAC webhooks, daily warehouse exports, an MCP server (OPENLOYALTY-046, -023, -024, -013, -018, -032).
- **Execution-level telemetry:** per-execution context data and per-effect results exported daily — better decision-record raw material than most campaign tools (OPENLOYALTY-016, -017).
- **Enterprise proof in regulated verticals** (tobacco, banking, insurance) without itself being a compliance product (OPENLOYALTY-029).

## 11. Weaknesses / constraints

- **No synchronous decision path:** effects are asynchronous; the platform cannot gate an action (allow/deny/review) in the request flow (OPENLOYALTY-011, -005). [Documented behavior]
- **No policy governance:** no campaign versioning, drafts, diffs, rollback, or approval workflow; ACL stops at View/Modify (OPENLOYALTY-005, -021, -037). [Documented absence]
- **No regulatory, identity, location, or fraud capability of any kind** across the entire documented surface (OPENLOYALTY-043). [Inference from full-docs enumeration, labeled]
- **Rule-model ceilings:** 6 rules/30 conditions per campaign, 500-char expressions, start-date-only ordering, max 4 automations, 200k automation audience (OPENLOYALTY-005, -024, -010, -034). [Documented]
- **Audit gaps:** retention, immutability/tamper-evidence undocumented; audit log covers admin/member actions but not full config version history (OPENLOYALTY-014, -015). [Documented absence]
- **Heavy integration dependency and opaque pricing** — developer-resource-hungry, weeks-to-months, sales-only pricing (OPENLOYALTY-038, -028). [Third-party + official]
- **SLA inconsistency:** 99.9% in docs vs 99.99% in marketing/pricing (OPENLOYALTY-003, -028, -002). [Documented discrepancy]
- **Small vendor** relative to enterprise suites: Divante spin-off, EUR 2.3M disclosed R&D funding (OPENLOYALTY-030). [MEDIUM confidence]

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,1,OPENLOYALTY-001;OPENLOYALTY-035
A02,2,OPENLOYALTY-001;OPENLOYALTY-047
A03,3,OPENLOYALTY-035;OPENLOYALTY-001
A04,0,OPENLOYALTY-043
A05,0,OPENLOYALTY-043
A06,0,OPENLOYALTY-043
A07,2,OPENLOYALTY-045;OPENLOYALTY-006
A08,1,OPENLOYALTY-035;OPENLOYALTY-001
A09,2,OPENLOYALTY-044
A10,0,OPENLOYALTY-043
B01,4,OPENLOYALTY-004;OPENLOYALTY-045;OPENLOYALTY-046
B02,1,OPENLOYALTY-011;OPENLOYALTY-009
B03,1,OPENLOYALTY-002;OPENLOYALTY-011
B04,0,OPENLOYALTY-005;OPENLOYALTY-011
B05,1,OPENLOYALTY-016;OPENLOYALTY-017;OPENLOYALTY-009
B06,4,OPENLOYALTY-007;OPENLOYALTY-008;OPENLOYALTY-045
B07,4,OPENLOYALTY-008;OPENLOYALTY-033;OPENLOYALTY-025
B08,1,OPENLOYALTY-010;OPENLOYALTY-005
B09,3,OPENLOYALTY-009
B10,1,OPENLOYALTY-016
C01,1,OPENLOYALTY-008;OPENLOYALTY-033;OPENLOYALTY-019
C02,1,OPENLOYALTY-008
C03,0,OPENLOYALTY-043
C04,2,OPENLOYALTY-005;OPENLOYALTY-006;OPENLOYALTY-020;OPENLOYALTY-034
C05,1,OPENLOYALTY-014;OPENLOYALTY-015;OPENLOYALTY-005
C06,0,OPENLOYALTY-043
C07,1,OPENLOYALTY-009
C08,0,OPENLOYALTY-021;OPENLOYALTY-043
C09,0,OPENLOYALTY-043
C10,0,OPENLOYALTY-043
D01,2,OPENLOYALTY-016;OPENLOYALTY-017;OPENLOYALTY-014
D02,3,OPENLOYALTY-016;OPENLOYALTY-017;OPENLOYALTY-018
D03,1,OPENLOYALTY-016;OPENLOYALTY-005
D04,3,OPENLOYALTY-016
D05,1,OPENLOYALTY-015;OPENLOYALTY-014
D06,2,OPENLOYALTY-016;OPENLOYALTY-017;OPENLOYALTY-014
D07,2,OPENLOYALTY-014;OPENLOYALTY-018
D08,?,
D09,?,
D10,2,OPENLOYALTY-014;OPENLOYALTY-015
E01,0,OPENLOYALTY-043
E02,0,OPENLOYALTY-043;OPENLOYALTY-033
E03,0,OPENLOYALTY-043;OPENLOYALTY-008
E04,0,OPENLOYALTY-043;OPENLOYALTY-008
E05,0,OPENLOYALTY-043
E06,0,OPENLOYALTY-043
E07,0,OPENLOYALTY-043;OPENLOYALTY-006;OPENLOYALTY-025
E08,1,OPENLOYALTY-024
E09,0,OPENLOYALTY-043
E10,0,OPENLOYALTY-043;OPENLOYALTY-042
F01,4,OPENLOYALTY-025;OPENLOYALTY-008
F02,4,OPENLOYALTY-026;OPENLOYALTY-012;OPENLOYALTY-018
F03,3,OPENLOYALTY-017;OPENLOYALTY-016;OPENLOYALTY-006
F04,4,OPENLOYALTY-017;OPENLOYALTY-005;OPENLOYALTY-006
F05,4,OPENLOYALTY-025;OPENLOYALTY-012;OPENLOYALTY-026
F06,2,OPENLOYALTY-025;OPENLOYALTY-008
F07,3,OPENLOYALTY-044;OPENLOYALTY-005
F08,2,OPENLOYALTY-026;OPENLOYALTY-018
F09,3,OPENLOYALTY-025;OPENLOYALTY-001
F10,2,OPENLOYALTY-018;OPENLOYALTY-031
G01,4,OPENLOYALTY-019;OPENLOYALTY-037;OPENLOYALTY-029
G02,3,OPENLOYALTY-021
G03,3,OPENLOYALTY-022
G04,0,OPENLOYALTY-021;OPENLOYALTY-043
G05,3,OPENLOYALTY-003;OPENLOYALTY-037
G06,3,OPENLOYALTY-009;OPENLOYALTY-003
G07,2,OPENLOYALTY-023;OPENLOYALTY-037;OPENLOYALTY-014
G08,4,OPENLOYALTY-012;OPENLOYALTY-013;OPENLOYALTY-042
G09,3,OPENLOYALTY-028;OPENLOYALTY-003
G10,3,OPENLOYALTY-027;OPENLOYALTY-028
H01,4,OPENLOYALTY-046;OPENLOYALTY-002
H02,1,OPENLOYALTY-046;OPENLOYALTY-032
H03,4,OPENLOYALTY-012;OPENLOYALTY-013
H04,3,OPENLOYALTY-003
H05,3,OPENLOYALTY-023
H06,?,OPENLOYALTY-041
H07,3,OPENLOYALTY-024;OPENLOYALTY-003
H08,1,OPENLOYALTY-014;OPENLOYALTY-016
H09,3,OPENLOYALTY-037
H10,0,OPENLOYALTY-043;OPENLOYALTY-042
I01,0,OPENLOYALTY-001;OPENLOYALTY-038
I02,4,OPENLOYALTY-001;OPENLOYALTY-002;OPENLOYALTY-046
I03,4,OPENLOYALTY-001;OPENLOYALTY-028
I04,0,OPENLOYALTY-043
I05,4,OPENLOYALTY-001;OPENLOYALTY-029
I06,0,OPENLOYALTY-028;OPENLOYALTY-038
I07,2,OPENLOYALTY-028;OPENLOYALTY-038
I08,3,OPENLOYALTY-018;OPENLOYALTY-037
I09,3,OPENLOYALTY-038;OPENLOYALTY-028
I10,1,OPENLOYALTY-028;OPENLOYALTY-038
J01,0,OPENLOYALTY-043;OPENLOYALTY-005
J02,0,OPENLOYALTY-043;OPENLOYALTY-037
J03,0,OPENLOYALTY-021;OPENLOYALTY-043
J04,0,OPENLOYALTY-009;OPENLOYALTY-043
J05,0,OPENLOYALTY-005;OPENLOYALTY-011
J06,0,OPENLOYALTY-043
J07,1,OPENLOYALTY-016;OPENLOYALTY-017;OPENLOYALTY-014
J08,1,OPENLOYALTY-016;OPENLOYALTY-014
J09,1,OPENLOYALTY-037;OPENLOYALTY-047
J10,0,OPENLOYALTY-043
```

**Scoring notes (0s, 1s, and ?s):**

- All 0 scores rest on OPENLOYALTY-043, a **labeled inference of absence**: the complete official sitemaps (238 user-guide + 67 technical-guide + 302 API-reference pages) enumerate the entire documented product surface, and none of these features appear anywhere in it — this is positive enumeration evidence, not mere "unmentioned on website."
- B04/J05 = 0: the enumerated effect list (add/deduct units, give reward, set/remove attribute, grant badge, assign tier) contains no allow/deny/review output, and the async effects architecture precludes request-path authorization (OPENLOYALTY-005, -011).
- C08/G04/J03 = 0: ACL permission levels are exhaustively documented as View/Modify only; no approval concept exists (OPENLOYALTY-021).
- E07 = 0: only static caps (campaign limits, transfer caps) exist — guardrails, not scoring (OPENLOYALTY-006, -025).
- I01/I04/I06 = 0: positive evidence — buyer pages target marketers/developers; pricing is sales-led with all tiers routing to sales (OPENLOYALTY-001, -028, -038).
- A07 = 2 and I08 = 3 are **inferences** (adaptation of custom events + limits to entry-like workflows; lock-in from stateful ledger + integrations), labeled as such.
- `?` squares: D08 (audit retention undocumented), D09 (no log-integrity claims either way; dormant blockchain side project is not the product), H06 (idempotency guidance exists but no documented server-side guarantee).

## 13. White-space implications

1. **Already solved by Open Loyalty:** event ingestion at scale with custom event schemas (B01), rich stateful customer context (B06/B07), promotion-linked value ledger with provenance, budgets, and expirations (F01–F05, F07), multi-tenant/multi-region operation with timezone-correct rules (G01, G05), webhooks/exports/API platform (G08, H01, H03–H05, H07), campaign simulation (B09).
2. **Partially solved:** decision logging — execution records with input context and per-effect results, but no policy-version linkage (D02, D04 vs D03); temporal rules (start/end dates, period caps — no legal effective-date semantics, C04); geography as data (address conditions, country tenants — no verification or legal meaning, C01); config portability without governance (H09 vs G04/G07); post-hoc outcome reasons in exports rather than reason codes at decision time (B05).
3. **Unsolved:** everything regulatory and authorization-shaped — J01–J06, J10 entirely; counsel workflows (C08), legal provenance (C09), policy libraries (C10), regulatory monitoring (C06), impact analysis beyond one-member simulation (C07/J04); synchronous allow/deny/review with reason codes (B02–B05); identity/geo/fraud signals (all of E); evidence-grade reconstruction and replay (J07/J08); promotion-law administration (A04–A06, A08, A10).
4. **Could the vendor add the missing capability easily?** Approval workflows, campaign versioning, and richer decision logs: yes — incremental engineering on existing primitives (audit log, config exports). A synchronous authorization API: hard — it inverts their async effects architecture and SLA posture. Jurisdictional legal content, counsel networks, and regulatory monitoring: no — that is a legal-operations business they show zero motion toward, and their buyer (marketing) doesn't fund it.
5. **Could a customer assemble it using Open Loyalty + internal engineering?** Only the incentive-execution half. A sophisticated team could encode geo/age/eligibility conditions as campaign conditions and segments, use wallets as the regulated-value ledger, and mine execution exports for audit. But there is no gate to call before an action (effects fire after the fact), no policy versioning to defend a decision, no verified location/identity inputs, and no counsel-facing surface — the authorization layer, evidence layer, and legal-content layer would all be net-new internal builds. Open Loyalty would sit **behind** such a system as the fulfillment engine.
6. **What would make a customer buy a separate product instead?** Needing a real-time allow/deny/review verdict across products (not just loyalty grants); regulator-defensible reconstruction tied to policy versions and human approvals; verified identity/geo/fraud inputs; counsel-owned policy lifecycle with impact analysis; and a compliance/legal budget owner — none of which Open Loyalty's architecture, roadmap signals, or buyer motion address.

## 14. Replacement risk

**MEDIUM.**

Open Loyalty owns several substrate pieces a Promotion OS would need: high-volume event ingestion, an expression-based rules engine over rich customer state, a value ledger with provenance, multi-tenant/multi-region operations, ISO-certified hosting, and enterprise customers in regulated verticals (tobacco, alcohol, banking, insurance, fuel) who feel promotion-compliance pain. If those customers pulled for it, Open Loyalty could plausibly ship approval workflows, campaign versioning, and stronger audit — the cheap 20% (OPENLOYALTY-016, -017, -021, -029).

But the core of the proposed space works against them: synchronous cross-product authorization contradicts their async effects architecture (OPENLOYALTY-011); regulatory content, counsel workflows, and legal provenance are an operations-heavy business outside their marketing-buyer motion (OPENLOYALTY-043, -001); and they are a small, focused vendor (OPENLOYALTY-030) competing hard in loyalty against Antavo/Talon.One/White Label Loyalty. Entering regulatory decisioning would be a strategic pivot, not an extension. Not LOW, because the substrate and regulated-industry footholds are real.

## 15. Adjacent discoveries

1. **Antavo** (antavo.com) — enterprise loyalty cloud, API-first plus no-code, Gartner/Forrester-cited, clients KFC/Puma/SKIMS/Hyatt. Matters: the strongest direct alternative in Open Loyalty's category; any loyalty-adjacent wedge must clear it too (OPENLOYALTY-039).
2. **White Label Loyalty** (whitelabel-loyalty.com) — event-based, API-first loyalty engine with real-time rules ("100M+ loyalty events"), clients PepsiCo/AkzoNobel/Burger King EMEA. Matters: architecturally closest analog (event-driven rules engine), showing the pattern is commoditizing (OPENLOYALTY-040).
3. Also surfaced (for the manager appendix, not researched in depth): **Capillary Technologies**, **Annex Cloud**, **Salesforce Loyalty Management**, **Comarch Loyalty**, **TrueLoyal** — enterprise loyalty suites listed as Open Loyalty alternatives (OPENLOYALTY-038); **Braze** as the engagement layer Open Loyalty officially plugs into (OPENLOYALTY-042).

## 16. Evidence ledger

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| OPENLOYALTY-001 | API-first headless gamified loyalty engine; "100+ enterprise brands"; clients Aldo, Heineken, Intersport, BAT, limango, Club Brugge | https://www.openloyalty.io/ | official-marketing | 2026-08-18 | HIGH |
| OPENLOYALTY-002 | 120 ms avg API response, 99.99% uptime, 1B events/month, 75M transactions/yr; logic controlled entirely via REST API | https://www.openloyalty.io/technology/loyalty-program-api | official-marketing | 2026-08-18 | MEDIUM |
| OPENLOYALTY-003 | Production (99.9% SLA, 1,200 req/s soft limit) in AWS Dublin/Frankfurt/Ohio/Singapore/Sydney; staging PoC env, no SLA, "PII not recommended" | https://help.openloyalty.io/technical-guide/api-fundamentals/environments-capabilities | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-004 | Six campaign trigger types: purchase, return, internal event, custom event, achievement, redemption code | https://help.openloyalty.io/campaigns/campaigns/campaigns-and-referral-campaigns/creating-campaigns | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-005 | Rule model: 6 rules/30 conditions; effects = add/deduct units, give reward, set/remove attribute, grant badge, assign tier; no drafts/versioning/priority | https://help.openloyalty.io/campaigns/campaigns/campaigns-and-referral-campaigns/creating-campaigns | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-006 | Per-member frequency caps, global + per-member unit budgets; canceled transfers return to pool | https://help.openloyalty.io/campaigns/campaigns/campaign-limitation | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-007 | Symfony-Expression-based custom conditions and effects; 500-char cap | https://help.openloyalty.io/integrations-and-data-exchange/expressions | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-008 | Expression context: customer profile/address/consents/tier/per-wallet counters, transaction items, event.body.*, executionContext.processedAt | https://help.openloyalty.io/integrations-and-data-exchange/expressions/attributes-list | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-009 | Campaign simulator (UI + API): shows which campaigns fire and rewards granted; auto-imports member data by ID | https://help.openloyalty.io/campaigns/campaigns/campaign-simulation | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-010 | Same-trigger campaigns execute in Campaign Start Date order; no priority model | https://help.openloyalty.io/campaigns/campaigns/campaign-simulation | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-011 | Effects are async: transaction POST "should trigger CampaignEffectWasApplied webhook"; no synchronous decision output | https://help.openloyalty.io/technical-guide/getting-started-guide/add-transaction | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-012 | ~20 webhook event types (TransactionRegistered, CampaignEffectWasApplied, WalletBalanceUpdated, CustomerLevelChanged, PointsWillExpire, ...) | https://help.openloyalty.io/integrations-and-data-exchange/webhooks/what-triggers-a-webhook | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-013 | HMAC-SHA256 webhook signatures, one-time secrets, rotation endpoint | https://help.openloyalty.io/integrations-and-data-exchange/webhooks/hmac | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-014 | GET /api/audit/log: auditLogId, store, eventType, entityType/Id, username, userId, userType, ip, createdAt; filters; archives/exports endpoints | https://help.openloyalty.io/api-reference/audit/get-all-system-logs | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-015 | System log covers member-data, auth, ACL, admin activity, audit views, transaction views; CSV export; admin-only | https://help.openloyalty.io/administration/settings/admins/system-logs | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-016 | Campaign Execution export: contextData (triggering member/transaction data), executionStatus success/skipped/failed, messages, timestamps | https://help.openloyalty.io/technical-guide/data-exports/data-structure-and-types/campaign-execution | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-017 | Effect Results export: per-effect status, type, points, couponValue, rewardId, walletCode, error, linked by campaignExecutionId | https://help.openloyalty.io/technical-guide/data-exports/data-structure-and-types/campaign-calculated-effect-results | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-018 | Daily CSV delta exports to customer S3/GCS/Azure for liability tracking, analytics, warehousing | https://help.openloyalty.io/technical-guide/data-exports/overview | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-019 | Tenants: per-tenant currency/code/name/members/campaigns; global config/admins/roles; timezone strategy per tenant | https://help.openloyalty.io/administration/settings/tenants | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-020 | Campaign rules and achievement triggers evaluated in tenant's configured timezone; timestamps converted on ingestion | https://help.openloyalty.io/faq/timezones | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-021 | ACL roles: View/Modify per resource across ~20 resource groups; API-manageable; no approval level | https://help.openloyalty.io/administration/settings/roles/available-permissions-acl | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-022 | OIDC SSO for admins; Okta and Microsoft Entra ID guides | https://help.openloyalty.io/technical-guide/authentication/enabling-sso-login | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-023 | No-breaking-changes guarantee; versioned endpoints; 3-month migration window; zero-downtime staged rollouts | https://help.openloyalty.io/technical-guide/backward-compatibility-policy | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-024 | Limits: auth 20→40 RPM, 30s timeout, _page max 500, 100MB imports, 500-char expressions; unique loyalty card numbers per tenant | https://help.openloyalty.io/technical-guide/api-fundamentals/limits | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-025 | Multi-wallet types, custom units, 5 expiration modes, pending periods, negative balances, transfer caps | https://help.openloyalty.io/members-and-activity/wallets/wallet-types-and-configuration | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-026 | Unit-transfer ledger: admin changes, spends, P2P, expired/blocked; API add/spend/block/cancel/expire/activate + labels | https://help.openloyalty.io/members-and-activity/wallets/unit-transfers | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-027 | ISO 27001 + ISO 9001 (DEKRA) since Nov 2022, renewed Sept 2025; OWASP Top-10/CWE-25 testing; no SOC 2 | https://www.openloyalty.io/news/open-loyalty-iso-certifications | official-marketing | 2026-08-18 | HIGH |
| OPENLOYALTY-028 | Sales-led pricing: Platform Fee + Active-Member Allowance; 99.99% SLA, P1 <30min/<2h; EU/APAC/NA data residency; separate K8s namespaces | https://www.openloyalty.io/pricing | official-marketing | 2026-08-18 | HIGH |
| OPENLOYALTY-029 | Enterprise case studies: JTI (18 countries), BAT (EU+America), ALDO (global, 3 months), U.S. Soccer, banks, insurers, telco, fuel | https://www.openloyalty.io/clients | case-study | 2026-08-18 | HIGH |
| OPENLOYALTY-030 | Divante-incubated (Wrocław, Poland); EUR 2.3M R&D funding (EUR 1.3M NCBR) | https://www.divante.com/resources/news/open-loyalty-secures-funding-to-expand-technology | official-marketing | 2026-08-18 | MEDIUM |
| OPENLOYALTY-031 | Open-source edition retired from official org (only dormant Hyperledger side projects remain); forks note 200-member/testing-only limit | https://github.com/OpenLoyalty | third-party | 2026-08-18 | MEDIUM |
| OPENLOYALTY-032 | Official MCP server: 145 API tools across 22 domains for AI agents | https://help.openloyalty.io/technical-guide/integration/mcp-server | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-033 | Segments: 27 condition types incl. country/city/province/postal, tier, custom attributes, achievements, custom events | https://help.openloyalty.io/members-and-activity/members/segments/segment-conditions | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-034 | Automation campaigns: daily/weekly/monthly/birthday/anniversary at 00:00 tenant time; 200k audience cap; max 4 | https://help.openloyalty.io/campaigns/campaigns/automation-campaigns | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-035 | Fortune wheels: independent probability + business-logic layer blocking wins on inventory/budget/member limits | https://help.openloyalty.io/gamification/fortune-wheels/how-probability-works | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-036 | GDPR: anonymize or delete members; consent booleans on member profile | https://help.openloyalty.io/faq/gdpr | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-037 | Config duplication across tenants (same env); cross-env migration via per-module configuration exports with manual dependency sequencing | https://help.openloyalty.io/global-management/config-duplication | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-038 | Third-party: developer-resource-heavy, weeks-to-months deployments, opaque sales-led pricing, enterprise-only; alternatives list | https://wiserreview.com/blog/open-loyalty-alternatives/ | third-party | 2026-08-18 | MEDIUM |
| OPENLOYALTY-039 | Adjacent competitor Antavo: enterprise loyalty, API-first + no-code, KFC/Puma/SKIMS/Hyatt | https://antavo.com/ | official-marketing | 2026-08-18 | MEDIUM |
| OPENLOYALTY-040 | Adjacent competitor White Label Loyalty: event-based API-first loyalty engine, PepsiCo/AkzoNobel/Burger King EMEA | https://whitelabel-loyalty.com/ | official-marketing | 2026-08-18 | MEDIUM |
| OPENLOYALTY-041 | Best practices: retries/backoff, 429s, scroll pagination, mandatory User-Agent; idempotent-design advice but no documented idempotency-key guarantee | https://help.openloyalty.io/technical-guide/api-fundamentals/best-practices | official-doc | 2026-08-18 | MEDIUM |
| OPENLOYALTY-042 | Integrations: Braze partner (bidirectional), webhooks-to-SQS, Lambda/Zapier/EventBridge/Kafka examples; none are risk-signal vendors | https://help.openloyalty.io/technical-guide/sitemap-pages.xml | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-043 | INFERENCE (labeled): full doc sitemaps (238+67+302 pages) enumerate no identity/geo/fraud, approval, legal/regulatory, promotion-law, or IaC features | https://help.openloyalty.io/sitemap.xml | official-doc | 2026-08-18 | MEDIUM |
| OPENLOYALTY-044 | Rewards/redemption: status lifecycle + history, bulk status changes, cancel redeemed reward, eligible-members list, fortune-wheel draw | https://help.openloyalty.io/api-reference/sitemap-pages.xml | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-045 | Custom events: admin-defined schemas, POSTed by external systems, drive campaigns/achievements/webhooks | https://help.openloyalty.io/api-reference/custom-event | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-046 | Public REST reference, 300+ endpoints, ~30 tags; Postman collections; no official SDKs | https://help.openloyalty.io/api-reference | official-doc | 2026-08-18 | HIGH |
| OPENLOYALTY-047 | Docs cookbook: 20+ sample campaigns, 7 sample achievements, pay-with-points patterns; challenges/leaderboards/badges/tiers modules | https://help.openloyalty.io/sitemap-pages.xml | official-doc | 2026-08-18 | HIGH |

Full machine-readable ledger: `outputs/evidence/08_openloyalty.jsonl` (47 records).

## 17. Verdict

**COMPLEMENT**

Open Loyalty overlaps heavily on mechanical substrate — event-driven rules over rich customer state (B01, B06, B07), promotion-linked value ledger (F01–F05), multi-tenant/multi-region governance (G01, G05), and a mature developer platform (H) — and its execution exports even resemble a rudimentary decision log (D02/D04). But it evaluates rules **asynchronously and outputs reward effects, never allow/deny/review verdicts**; it has no policy versioning, approvals, replay, legal content, or identity/geo/fraud signals, and its buyer is marketing, not legal/compliance. Every J-square scores 0–1. In a Promotion OS world it is the incentive-execution engine sitting *behind* an authorization layer, not a rival to one — while exerting substitution pressure only on the generic promotion-rules portion of the thesis ("our loyalty engine already does rules"). Its regulated-industry customer base makes it a credible partial entrant if pulled, hence MEDIUM replacement risk, but today it complements rather than competes.
