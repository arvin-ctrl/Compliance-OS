# Company Report — Cerbos

Researcher: Research Agent 14 (Cerbos)
Date: 2026-08-18
Category: Generic policy infrastructure
Manager: Manager D

Core question (from COMPANIES.md): How much policy versioning, decision logs, APIs, and enterprise governance already exist?

Short answer: a great deal. Policy versioning, decision logs with policy-revision lineage, synchronous decision APIs, and a managed policy lifecycle control plane are the core of the product. What does NOT exist is any regulatory/legal content, counsel-facing workflow, impact analysis, identity/geo/fraud signal generation, or any promotion-domain functionality.

## 1. Executive summary

**Actual core product.** Cerbos is an open-core, application-authorization platform with three components: (1) **Cerbos PDP** — an Apache-2.0, stateless policy decision point (Go, ~4.5k GitHub stars) that evaluates YAML/CEL policies over principal/resource/action requests and returns ALLOW/DENY synchronously via gRPC/REST; (2) **Cerbos Hub** — the commercial control plane for policy authoring, testing, versioning, signed bundle distribution to PDP fleets, and centralized decision-log collection; (3) **Cerbos Synapse** — a newer enrichment layer that fetches identity/resource attributes from IdPs, databases, and APIs at decision time (CERBOS-001, CERBOS-032, CERBOS-030).

**Who buys it.** Engineering/platform teams (and increasingly security/identity teams) at software companies that want to rip authorization logic out of application code. Case-study customers include Utility Warehouse (FTSE 250, 4,500 internal services on the free OSS PDP) and 9fin (fintech data platform) (CERBOS-028, CERBOS-029). Pricing is public and self-serve from $0 to $933+/month, with SSO/self-hosted-Hub enterprise deals on top (CERBOS-026).

**Job it is hired to do.** "Decouple permission logic from app code": centralize who-can-do-what rules as versioned, tested policy files; answer allow/deny questions in-line at request time across thousands of services; and prove afterwards — via decision logs tied to policy versions — why any access was allowed or denied (CERBOS-001, CERBOS-011, CERBOS-012). Since 2025 the company has aggressively repositioned the same engine for AI-agent/MCP tool-call authorization (CERBOS-038, CERBOS-039).

## 2. Product architecture

INPUT -> DECISION/PROCESS -> OUTPUT

- **INPUT:** An API call (gRPC or REST `CheckResources`, or AuthZEN endpoints) containing: principal (ID, IdP roles, policy version, scope, free-form attributes), one or more resources (kind, ID, scope, free-form attributes), a list of actions, optional auxData (JWTs), and since v0.51.0 an optional `requestContext` (correlation IDs, session IDs) that flows into audit logs (CERBOS-002, CERBOS-013). Attributes can optionally be fetched/enriched by Synapse from IdPs/DBs/APIs with TTL caching instead of being supplied by the caller (CERBOS-030).
- **DECISION/PROCESS:** The stateless PDP evaluates the request against compiled policies loaded from a store (disk, git, blob, SQL DB, or Hub-distributed encrypted bundle). Evaluation: match resource policy by name+version (fallback `default`), walk the scope hierarchy (most-specific-first, two documented conflict modes), compute derived roles from base roles + CEL conditions, evaluate CEL rule conditions over P/R/auxData/globals with time functions (`now()`, `timeSince()`), apply deny-override semantics, optionally validate attributes against JSON Schemas (reject/warn) (CERBOS-007, CERBOS-008, CERBOS-009, CERBOS-034, CERBOS-035, CERBOS-006, CERBOS-010, CERBOS-024).
- **OUTPUT:** Per-action `EFFECT_ALLOW`/`EFFECT_DENY`; optional CEL `outputs` (arbitrary values, usable as human-readable reasons); optional metadata (`matchedPolicy`, `matchedScope`, `effectiveDerivedRoles`); `validationErrors`; and a `cerbosCallId` that keys the audit-log entry. In parallel, an access-log and decision-log record (full inputs + outcome + store-specific policy revision metadata such as the git commit hash) is written to local store/file/Kafka/Hub (CERBOS-002, CERBOS-005, CERBOS-011, CERBOS-012).

A second decision mode, `PlanResources`, does partial evaluation and returns ALWAYS_ALLOWED / ALWAYS_DENIED / CONDITIONAL (a condition AST) so the application can filter database queries to only permitted rows (CERBOS-036).

The lifecycle loop around the engine: policies live in git → Hub validates + runs the YAML test suite on every change → on green, builds an encrypted, signed, versioned bundle → pushes to all connected PDPs "within seconds"; failed tests block deployment; every deployment attempt is pinned to immutable policy-store versions and can be reverted (CERBOS-015, CERBOS-016, CERBOS-018).

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Cerbos PDP (OSS, Apache 2.0) | Stateless authorization engine; CheckResources/PlanResources APIs; audit logging; Admin API; runs as service, sidecar, daemonset, serverless, or in-process | Engineering/platform | Core | CERBOS-002, CERBOS-032, CERBOS-043 |
| Policy framework | Resource/principal/role/derived-roles policies, scoped policies, exported constants/variables, JSON Schemas, CEL conditions | Engineering | Core | CERBOS-008, CERBOS-009, CERBOS-035 |
| Cerbos Hub — policy stores & deployments | Versioned cloud policy containers (git-synced or API/CLI/UI-managed), test-gated CI/CD, signed encrypted bundles, fleet distribution, rollback, environment separation | Engineering/platform | Commercial core | CERBOS-015, CERBOS-016, CERBOS-019 |
| Cerbos Hub — audit log collection | Centralized decision + access logs from PDP fleet; search/filter UI; plan-based retention (1 week–1 year, custom for enterprise); PDP-side masking; age-encrypted exports | Engineering, security/compliance stakeholders | Commercial add-on (bundled in plans) | CERBOS-014, CERBOS-026 |
| Cerbos Hub — playgrounds | Collaborative browser IDE for policies with live evaluation (Explore tab, permissions matrix) | Engineering | Add-on (free) | CERBOS-037 |
| Embedded PDP (ePDP) | WASM policy bundles evaluated in-process in browsers/edge/serverless/React Native; 10–60s bundle polling; local-only decision logs via `onDecision` | Engineering | Add-on via Hub | CERBOS-020, CERBOS-045 |
| Cerbos Synapse | Decision-time enrichment: fetches principal/resource attributes from IdPs (Okta, Entra, Auth0…), DBs (Postgres, MySQL, Neo4j…), gateways/Kafka/K8s; custom WASM adapters; TTL caching | Engineering/identity | New add-on (maturity unclear) | CERBOS-030 |
| AI/MCP authorization | Same engine gating AI-agent tool calls (user context + tool + target resource → allow/deny + audit trail) | Engineering/security | Positioning/solution layer | CERBOS-038, CERBOS-039 |

## 4. API / developer capability

- **APIs:** gRPC (port 3593) + REST; `CheckResources` (batch: default 50 resources × 50 actions, configurable), `PlanResources`, `ServerInfo`; OpenID **AuthZEN** interop endpoints (`/access/v1/evaluation(s)`) — a standards-based interface (CERBOS-002, CERBOS-021). Admin API: policy add/update/list/disable/delete, policy inspection, schema CRUD, store reload, revision purge, audit-log retrieval; basic auth with a **single admin user only**; dynamic policy mutation requires SQL-backed stores (CERBOS-023).
- **SDKs:** JS, Go, Python, Java, .NET, Rust, PHP, Ruby (PEP clients); separate Hub SDKs for programmatic policy-store management (CERBOS-022).
- **Webhooks:** None documented for either PDP or Hub (Kafka audit streaming is the documented push channel) — left unresolved (CERBOS-011).
- **Sandbox:** Hub playgrounds (collaborative IDE with live decision exploration); free PoC tier; trivially runnable local Docker (CERBOS-037, CERBOS-026).
- **Rules engine:** CEL conditions over free-form attributes, derived roles, scoped policy hierarchies, JSON Schema input validation, deny-override semantics (CERBOS-006, CERBOS-009, CERBOS-034, CERBOS-035).
- **Synchronous decisioning:** Core mode — request/response evaluation in-line with app requests (CERBOS-002).
- **Latency claims:** "Sub-millisecond policy evaluation" (marketing); architecture supports it structurally: stateless engine deployed as sidecar or in-process WASM, no network fan-out (CERBOS-003, CERBOS-020).
- **Versioning:** Policy schema `apiVersion: api.cerbos.dev/v1`; namespaced v1 gRPC services; policy-level `version` field; Hub bundle/build versioning. No formal REST deprecation-policy document located (CERBOS-040, CERBOS-007, CERBOS-015).
- **Idempotency:** Check APIs are stateless reads (inherently idempotent); Admin API policy writes are upserts (POST/PUT add-or-update). No idempotency-key mechanism, none needed for the decision path (CERBOS-023 — inference labeled).
- **Integration model:** Instrument every enforcement point with an SDK call to a self-hosted PDP (service/sidecar) or embedded WASM PDP; policies distributed from git/Hub. Query-plan adapters (Prisma, Drizzle, Mongoose, SQLAlchemy, Convex, LangChain/ChromaDB) translate CONDITIONAL plans into ORM filters (CERBOS-036, CERBOS-043).

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Yes — free-form principal/resource attributes, JWT auxData, globals, all via CEL; optional JSON Schema contracts (CERBOS-006, CERBOS-035).
- **Store customer/user state?** No — the PDP is deliberately stateless; context must arrive in the request or be fetched at decision time by Synapse (TTL-cached) from customer systems. No counters, velocity, or history features (CERBOS-003, CERBOS-030 — inference labeled).
- **Return reason codes?** Partially — CEL `outputs` return arbitrary explanation values per triggered rule; `includeMeta` exposes matchedPolicy/matchedScope/effectiveDerivedRoles. No standardized reason-code taxonomy (CERBOS-005, CERBOS-002).
- **Output allow/deny/review?** Allow/deny only. No first-class "review/escalate" verdict; it could be emulated with outputs but the API contract is binary (CERBOS-004 — inference labeled).
- **Simulate policies?** Offline yes — full YAML test framework (fixtures, expected effects/outputs, pinned `now`), CI actions, and playground live exploration. No shadow/dry-run against production traffic and no what-if against historical decisions (CERBOS-017, CERBOS-037).
- **Replay decisions?** Reconstructable, not push-button — decision logs capture full inputs, outcome, outputs, and store-specific policy revision (e.g., git commit hash); Hub deployments pin immutable policy versions. Re-execution requires manually checking out that revision; no replay tool is documented (CERBOS-011, CERBOS-012, CERBOS-016 — inference labeled).
- **Version policies?** Yes, at three layers: policy `version` field (parallel versions, e.g. staging/production, `default` fallback), store revision (git history / immutable Hub store versions), and bundle/build versioning with rollback (CERBOS-007, CERBOS-015, CERBOS-016).
- **Deploy rules independently of app code?** Yes — this is the product's thesis: policy changes flow git → Hub CI → signed bundle → fleet "within seconds", with failed tests blocking rollout (CERBOS-015, CERBOS-018).

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance:** None. No sweepstakes/contest/AMOE/prize concepts anywhere in docs or marketing (CERBOS-008, CERBOS-039 — reasoned absence).
- **Generic regulatory workflow:** None as workflow. "Compliance" positioning is posture-level ("compliance-ready" for SOC 2, HIPAA, ISO 27001, GDPR, PCI DSS, NIS2, DORA) — i.e., Cerbos helps customers evidence access control, it does not encode regulations (CERBOS-001, CERBOS-039).
- **Jurisdiction restrictions:** Mechanism only. Scoped policies explicitly support "regional… customisations to global access rules" (e.g., scope `eu.de`), and CEL can gate on a `region`/`jurisdiction` attribute the caller supplies. Zero jurisdiction content, no legal semantics (CERBOS-009 — mechanism vs content distinction is this report's inference).
- **Location verification:** None. Cerbos consumes whatever location attribute the caller passes; it has no geolocation, VPN, or proximity capability (CERBOS-006 — reasoned absence).
- **Legal content/rules:** None. Policy format has no field for legal citations/provenance (no metadata/annotations block in the documented schema) (CERBOS-040 — reasoned absence).
- **Regulatory monitoring:** None (reasoned absence; entirely outside the documented product domain).
- **Change management:** Strong but generic: test-gated CI/CD, signed immutable bundles, environment deployments, rollback, full revision history (CERBOS-015, CERBOS-016, CERBOS-018).
- **Counsel approval:** Not in product. The documented change-control path is git PRs and reviews; a legal reviewer could be made a required PR approver, but Hub has no approval workflow, no legal-reviewer role, and the artifacts under review are YAML+CEL, which is hostile to non-engineers (CERBOS-019, CERBOS-041 — inference labeled).
- **Historical policy state:** Strong: multiple live policy versions, git history, immutable Hub store versions per deployment attempt ("audit exactly which policies were in effect at any given point in time"), and decision logs stamped with the policy revision used (CERBOS-007, CERBOS-016, CERBOS-012).

## 7. Audit / evidence

Can a customer reconstruct:

- **Exact inputs?** Yes — decision logs record the request context (principal, resource, attributes, auxData) plus app-supplied `requestContext`; caveat: JSONPath masking can strip fields, and embedded PDPs only log locally via `onDecision` (CERBOS-011, CERBOS-013, CERBOS-014, CERBOS-045).
- **Exact rule/policy?** Yes — matched policy/scope in response meta; Hub audit UI links each decision's policy name to its source code (CERBOS-002, CERBOS-014).
- **Exact version?** Yes — store-specific revision metadata (e.g., git commit hash) recorded per decision since v0.33.0; deployments pinned to immutable store versions (CERBOS-012, CERBOS-016).
- **Exact output?** Yes — effects and rule outputs are logged (CERBOS-011, CERBOS-014).
- **Exact timestamp?** Yes — audit entries are timestamped, keyed by `cerbosCallId`, correlatable with app logs (CERBOS-011).
- **Human approvals?** Only outside the product — via the customer's git history/PR record; Hub stores no approval events (CERBOS-019, CERBOS-041 — inference).
- **Source/legal authority?** No — no concept of legal provenance exists (CERBOS-040 — reasoned absence).

Additional evidence properties: retention 7 days (local default) to 1 year (Production plan) or custom (Enterprise); PDP-side masking before transmission; age-encrypted JSONL exports gated to Hub Owners; bundle signing for distribution integrity — but **no documented tamper-evidence (hash-chaining/WORM) on the audit log itself** (CERBOS-011, CERBOS-014, CERBOS-018, CERBOS-026).

## 8. Enterprise readiness

- **SSO/RBAC:** Hub RBAC with org roles (Owner/Developer/Analyst/Viewer/Member) and workspace roles (Owner/Developer/Analyst/Viewer; Analyst can view but not export audit logs). SSO is Enterprise-plan-only, thinly documented (CERBOS-025, CERBOS-026).
- **Multitenancy / multi-brand:** Scoped policies for per-tenant/per-region policy trees; Hub workspaces for team/tenant separation; "per-tenant custom policies" is a promoted use case (CERBOS-009, CERBOS-015, CERBOS-039).
- **Environments:** Hub deployments (production/staging), policy `version` field, playgrounds (CERBOS-016, CERBOS-007, CERBOS-037).
- **Security certifications:** SOC 2 Type II (announced 2024-01-09; scope/auditor unspecified) (CERBOS-027).
- **SLA:** "Uptime SLA" on paid Hub plans; "Enterprise support SLA" custom tier; details not published (CERBOS-026).
- **Support / professional services:** Community → live chat → phone + quarterly training (Enterprise). No PS-dependency signals; case studies stress self-serve adoption ("very low bar to get going") (CERBOS-026, CERBOS-029).
- **Customer scale examples:** Utility Warehouse — FTSE 250, 4,500 services, 200+ engineers, self-hosted OSS; 9fin — fintech, product packaging in 10 minutes (CERBOS-028, CERBOS-029).
- **Deployment freedom:** cloud/on-prem/air-gapped; self-hosted Hub available at Enterprise tier (CERBOS-001, CERBOS-026).

## 9. Commercial model

- **Pricing (public):** OSS free forever; Hub PoC $0 (100 monthly active principals, 2 PDPs, 1-week logs); Development from $25/mo (3-month logs); Production from $933/mo (5,000 MAPs, unlimited PDPs, 1-year logs); Enterprise custom (SSO, self-hosted Hub, custom retention, support SLA). Unit metric = monthly active principals (CERBOS-026).
- **Likely buyer:** Engineering/platform leadership; security/identity teams secondary. Not legal, not marketing (CERBOS-001 — inference from audience framing).
- **Implementation burden:** Real but engineer-shaped: model resources/actions, author policies, instrument every enforcement point with SDK calls, feed attributes (or deploy Synapse). Case studies indicate incremental service-by-service rollout (CERBOS-028, CERBOS-029 — inference).
- **Sales motion:** Open-source-led, self-serve product-led growth with enterprise upsell; seed-stage company (~$11M–15M raised; Crane, OMERS Ventures) (CERBOS-032, CERBOS-033).
- **Large-customer evidence:** UW (FTSE 250) — notably on the **free OSS tier**, illustrating the open-core monetization risk (CERBOS-028).

## 10. Strengths

- **Decision evidence is a first-class product feature:** decision logs carrying full inputs, outputs, and the exact policy revision (git SHA), centrally searchable in Hub, with retention tiers, masking, and encrypted export. This is the strongest decision-log/lineage implementation among the generic policy engines researched in this project's category (CERBOS-011, CERBOS-012, CERBOS-014).
- **Complete policy lifecycle control plane:** versioned stores, test-gated automated CI/CD, signed encrypted bundles, second-scale fleet distribution, immutable version pinning, rollback, environment deployments, fleet visibility (CERBOS-015, CERBOS-016, CERBOS-018).
- **Purpose-built policy ergonomics vs OPA:** application-authorization data model (principal/resource/action, derived roles, scopes) out of the box; YAML+CEL rather than Rego; strong testing framework; third parties consistently describe it as easier to adopt than OPA (CERBOS-008, CERBOS-017, CERBOS-044).
- **Deployment flexibility unmatched in category:** service, sidecar, daemonset, serverless, air-gapped, and in-process WASM at the edge/browser/mobile (CERBOS-043, CERBOS-020).
- **Transparent, low-friction commercial model:** Apache-2.0 core, public pricing from $0, standards support (AuthZEN) (CERBOS-032, CERBOS-026, CERBOS-021).
- **Enterprise-grade proof points:** FTSE 250 regulated customer across 4,500 services citing audit logs as a favorite feature (CERBOS-028).

## 11. Weaknesses / constraints

- **No decision semantics beyond allow/deny:** no review/escalate verdict, no standardized reason codes — reasons are DIY CEL outputs (CERBOS-004, CERBOS-005).
- **Stateless by design:** no counters, velocity, budgets, entry history, or any stored user state; everything must be supplied or fetched from customer systems (documented architecture; constraint for any eligibility logic requiring history).
- **No content:** zero regulatory, jurisdictional, or legal knowledge ships with the product; customers author 100% of policy substance (CERBOS-039, CERBOS-040 — reasoned absence).
- **Governance is engineer-centric:** approvals delegated to git PRs; Hub has no approval workflow, no custom roles, single-admin basic auth on the self-hosted Admin API; SSO gated to Enterprise (CERBOS-041, CERBOS-023, CERBOS-025, CERBOS-026).
- **No pre-rollout impact analysis:** tests and staging exist, but nothing quantifies how a policy change would have altered historical/production decisions (absence across CERBOS-015/016/017 — inference labeled).
- **Evidence-chain gaps at the edges:** embedded PDP logs are local-only; no documented tamper-evidence on audit logs; SOC 2 scope undefined in announcement (CERBOS-045, CERBOS-027).
- **Open-core monetization risk:** flagship-scale customers can (and do) run the free PDP self-hosted (CERBOS-028 — inference labeled).
- **Company stage:** seed-stage (~$11–15M raised) — small vendor risk for conservative enterprise/compliance buyers (CERBOS-033, third-party).

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,CERBOS-008;CERBOS-039
A02,0,CERBOS-008;CERBOS-039
A03,0,CERBOS-008;CERBOS-039
A04,0,CERBOS-008;CERBOS-039
A05,0,CERBOS-008;CERBOS-039
A06,0,CERBOS-008;CERBOS-039
A07,0,CERBOS-008;CERBOS-039
A08,0,CERBOS-008;CERBOS-039
A09,0,CERBOS-008;CERBOS-039
A10,0,CERBOS-008;CERBOS-039
B01,4,CERBOS-002
B02,4,CERBOS-002
B03,3,CERBOS-003;CERBOS-020;CERBOS-028
B04,2,CERBOS-004;CERBOS-005
B05,3,CERBOS-005;CERBOS-002
B06,4,CERBOS-006;CERBOS-035
B07,2,CERBOS-030;CERBOS-006
B08,3,CERBOS-034;CERBOS-009
B09,3,CERBOS-017;CERBOS-037
B10,2,CERBOS-011;CERBOS-012;CERBOS-016
C01,2,CERBOS-009
C02,1,CERBOS-008
C03,1,CERBOS-002;CERBOS-008
C04,2,CERBOS-010;CERBOS-042
C05,4,CERBOS-007;CERBOS-015;CERBOS-016
C06,0,CERBOS-039
C07,2,CERBOS-017;CERBOS-018
C08,1,CERBOS-019;CERBOS-041
C09,0,CERBOS-040
C10,0,CERBOS-039
D01,3,CERBOS-011;CERBOS-002
D02,4,CERBOS-011;CERBOS-014
D03,4,CERBOS-012;CERBOS-014;CERBOS-016
D04,4,CERBOS-011;CERBOS-013;CERBOS-014
D05,1,CERBOS-019;CERBOS-041
D06,3,CERBOS-012;CERBOS-015;CERBOS-016
D07,2,CERBOS-014
D08,3,CERBOS-011;CERBOS-014;CERBOS-026
D09,2,CERBOS-018;CERBOS-014;CERBOS-015
D10,3,CERBOS-014;CERBOS-023;CERBOS-025
E01,0,CERBOS-030
E02,0,CERBOS-006
E03,0,
E04,0,CERBOS-006
E05,0,
E06,0,
E07,0,
E08,0,
E09,0,
E10,2,CERBOS-030
F01,0,
F02,0,
F03,0,
F04,0,
F05,0,
F06,0,
F07,1,CERBOS-002
F08,0,
F09,0,
F10,1,CERBOS-030
G01,3,CERBOS-009;CERBOS-015;CERBOS-039
G02,3,CERBOS-025
G03,2,CERBOS-026
G04,2,CERBOS-019;CERBOS-041
G05,3,CERBOS-007;CERBOS-016
G06,4,CERBOS-017;CERBOS-018;CERBOS-037
G07,3,CERBOS-015;CERBOS-016;CERBOS-018
G08,?,
G09,2,CERBOS-026
G10,3,CERBOS-027;CERBOS-026
H01,4,CERBOS-002;CERBOS-021;CERBOS-036
H02,4,CERBOS-022
H03,?,
H04,3,CERBOS-037;CERBOS-026
H05,2,CERBOS-040;CERBOS-002
H06,2,CERBOS-023;CERBOS-002
H07,2,CERBOS-002;CERBOS-026
H08,3,CERBOS-031;CERBOS-011;CERBOS-016
H09,3,CERBOS-019;CERBOS-023;CERBOS-024
H10,3,CERBOS-043;CERBOS-024
I01,1,CERBOS-039;CERBOS-028
I02,4,CERBOS-001;CERBOS-028;CERBOS-032
I03,0,
I04,1,CERBOS-001
I05,3,CERBOS-028;CERBOS-029
I06,3,CERBOS-026;CERBOS-032
I07,1,CERBOS-026;CERBOS-029
I08,2,CERBOS-021;CERBOS-032
I09,2,CERBOS-022;CERBOS-036
I10,3,CERBOS-026
J01,2,CERBOS-007;CERBOS-009;CERBOS-010
J02,2,CERBOS-018;CERBOS-015;CERBOS-019
J03,1,CERBOS-019;CERBOS-041
J04,1,CERBOS-017;CERBOS-018
J05,3,CERBOS-002;CERBOS-028;CERBOS-038
J06,2,CERBOS-030
J07,3,CERBOS-011;CERBOS-012;CERBOS-014;CERBOS-016
J08,2,CERBOS-012;CERBOS-014;CERBOS-015
J09,1,CERBOS-037;CERBOS-039
J10,3,CERBOS-015;CERBOS-018;CERBOS-016
```

**Scoring notes (0/1/? rationale — inference is labeled as such):**

- **A01–A10 = 0 (reasoned inference, not mere non-mention):** the documented entity model is exclusively principal/resource/action authorization (CERBOS-008); the exhaustive use-case catalog (CERBOS-039) contains nothing promotion-related; a stateless decision engine architecturally cannot run entries, drawings, fulfillment, or tax workflows. Positive evidence of domain absence, not silence.
- **E01–E09 = 0 (reasoned inference):** Cerbos consumes attributes; it never verifies identity/age/address, geolocates, fingerprints devices, or scores fraud. Synapse fetches such data from *customer* systems (CERBOS-030), confirming signals originate elsewhere. E02/E04: policies can *evaluate* an age/location attribute supplied by the caller — that is enforcement, not verification.
- **E10 = 2:** Synapse is a genuine decision-time signal-orchestration layer (IdPs/DBs/APIs, custom WASM adapters, TTL caching), but it is new, marketing-documented, with unconfirmed GA status (CERBOS-030, MEDIUM confidence) — held below 3.
- **F01–F09 mostly 0 (reasoned inference):** stateless PDP; no ledger, balances, provenance, or value objects exist anywhere in docs. F07=1: a redemption *check* is just a generic action authorization if the caller supplies the facts (inference). F10=1: Synapse could fetch balance attributes from an external ledger at decision time (inference).
- **C-block content squares:** C01=2/C02=1/C03=1 are mechanism-only scores: scopes/resource-kinds/actions can *model* jurisdictions, product types, and legal actions, but Cerbos ships no regulatory semantics or content. C06/C09/C10=0: no monitoring, no legal provenance field in the policy schema (CERBOS-040), no legal content library — reasoned absence.
- **C08=1 / D05=1 / G04=2:** approvals exist only as the customer's git PR process (documented as the recommended workflow); nothing counsel-specific, no in-product approval records (CERBOS-019, CERBOS-041).
- **B04=2:** allow/deny only; "review" emulation via outputs is possible but not first-class (CERBOS-004 — inference).
- **B07=2:** stateless engine; context arrives via request or Synapse fetch; no stored user state.
- **B10=2 / J08=2:** all reconstruction ingredients are logged (inputs + policy revision + outcome) but replay/re-execution is a manual procedure, not a feature (inference).
- **G08/H03 = ?:** no webhook/notification documentation found for PDP or Hub; Kafka audit streaming exists as an adjacent push channel (CERBOS-011). Unresolved rather than 0 because Hub notification settings were not exhaustively verifiable.
- **G03=2:** SSO exists but only as an Enterprise-plan line item with no implementation docs reviewed (CERBOS-026).
- **I07=1 (direction note):** score expresses LOW professional-services dependency — adoption is engineering-self-serve; enterprise plan adds training (CERBOS-026, CERBOS-029).
- **I08=2 / I09=2 (direction note):** moderate switching cost (per-callsite SDK integration is sticky; open YAML policy format + AuthZEN standard cut lock-in — inference); moderate integration burden (SDKs and query-plan adapters reduce, but every enforcement point must be instrumented — inference).
- **I01=1 / I04=1:** compliance/security stakeholders benefit (audit logs) but the buyer and user is engineering; no legal-buyer or fraud-buyer motion exists (inference from CERBOS-001/028/039).
- **I03=0 (reasoned inference):** nothing addresses marketers anywhere in product or GTM.

## 13. White-space implications

1. **Which proposed Promotion OS capabilities are already solved?** The generic execution substrate: versioned executable policy (J01's mechanism half — policy `version`, scopes, CEL time logic); production deployment workflow with test gates, signed bundles, instant fleet rollout and rollback (J02's pipeline half); real-time cross-product allow/deny with reasons via a single PDP fleet (most of J05); decision logs with input capture and exact policy-revision lineage (the infrastructure core of J07/J08); and a working policy lifecycle control plane (J10's generic form). Also solved: policy testing (G06), environments (G05), decision APIs/SDKs (H01/H02).
2. **Which are partially solved?** J06 (Synapse orchestrates attribute fetching from external systems but does no risk-vendor normalization — no geo/fraud vendor semantics); J07/J08 (evidence-grade reconstruction lacks tamper-evidence, regulator packaging, and push-button replay); C04 (time-conditions exist; effective-dated policy activation does not); C07/J04 (tests + staging, but no quantified impact analysis over historical or live traffic); B04/B05 (no review verdict, no reason-code standard).
3. **Which appear unsolved?** All regulatory *content and semantics*: jurisdiction rule libraries (C10/J09), legal-source provenance (C09), regulatory change monitoring (C06), counsel-as-approver workflow and legal-readable authoring (C08/J03), and the entire promotion-administration and identity/geo/fraud signal layers (A, E blocks). Also: any stateful eligibility (entry counts, spend history), and a "review" decision path feeding case management.
4. **Could this vendor add the missing capability easily?** The *product mechanics* — approval workflow in Hub, a review verdict, effective-dating, decision-diff impact analysis — are plausible roadmap items (Hub already has roles, immutable versions, and central logs to build on). The *content* — maintained jurisdiction rules with legal provenance and counsel-grade review — is a different business (legal editorial ops, counsel relationships, liability posture) far from their open-source developer motion and current AI-authorization focus. Inference: mechanics = easy-to-moderate; regulated content and legal-buyer GTM = hard/unlikely.
5. **Could a customer assemble it using this vendor + internal engineering?** Substantially, yes — and this is the key threat finding. A sophisticated enterprise could encode jurisdiction rules as scoped Cerbos policies (`us.ca`, `eu.de`), pass geo/KYC/fraud vendor outputs as attributes (or fetch via Synapse), require counsel sign-off via protected-branch PR reviews, and get versioned rollout + decision logs tied to git SHAs out of the box — at $0–$933/month. What they must still build/buy: all legal research and rule maintenance, vendor signal normalization, review/case-management flow, stateful eligibility, impact analysis, and regulator-facing evidence packaging. UW's 4,500-service deployment proves the assembly pattern works at enterprise scale for generic authorization (CERBOS-028).
6. **What would make a customer buy a separate product instead?** (a) Maintained, warranted jurisdiction content with legal provenance and update monitoring — the part no engine vendor supplies; (b) a counsel-native workflow (legal-readable rules, in-product attestation/approval records) rather than YAML PRs; (c) quantified pre-rollout impact analysis; (d) evidence packaging that satisfies regulators (tamper-evident, human-approval history included); (e) domain state (entries, prizes, ledgers) and signal normalization across geo/IDV/fraud vendors; (f) a vendor who accepts regulatory-domain accountability. Conversely, if the buyer is engineering and the rules are authored in-house by counsel + engineers, Cerbos plus glue is a credible, much cheaper substitute.

## 14. Replacement risk

**MEDIUM**

Technically, the barrier is low: Cerbos already owns the engine, versioning, decision-log lineage, and control plane — roughly the entire infrastructure layer of the proposed product — and its scoped-policy model maps naturally onto jurisdiction hierarchies. If a "regulatory policy control plane" category emerged, Cerbos could ship the mechanical features (approval workflows, effective dating, impact analysis) on top of Hub with moderate effort, and it is already marching up-stack (Hub, Synapse, AI authorization) with credible enterprise logos.

Commercially, the barrier is high: Cerbos is a seed-stage (~$11–15M), horizontal, developer-led infrastructure company whose current strategic bet is AI-agent authorization, not regulated-industry content or legal-buyer GTM. Building jurisdictional content, counsel workflow, and compliance accountability is a different company muscle. The realistic threat vector is not Cerbos pivoting, but Cerbos being the free/cheap substrate on which customers (or a rival startup) assemble the proposed product — which caps the value of the infrastructure layer of the hypothesis.

## 15. Adjacent discoveries

Companies/substitutes surfaced during research that the project should consider (CERBOS-044 unless noted):

1. **Oso (osohq.com)** — developer-first authorization-as-a-service with the Polar policy language; the closest commercial analogue competing for the same "externalize authorization" budget; actively publishes against Permit/Cerbos.
2. **AuthZed / SpiceDB** — Google Zanzibar-style relationship-based (ReBAC) authorization at scale; the substitute architecture when decisions hinge on relationship graphs rather than policies.
3. **OpenFGA** — CNCF open-source Zanzibar implementation (originating from Auth0/Okta); the free ReBAC substitute an enterprise platform team would evaluate alongside Cerbos/OPA.
4. **PlainID** — enterprise "policy-based access management" platform selling policy administration/governance to large regulated enterprises (banks/insurers) — the closest existing thing to a business-facing policy control plane with a compliance buyer.
5. **Axiomatics** — veteran ABAC/dynamic-authorization vendor (XACML lineage) entrenched in regulated industries; evidence that policy-based authorization for compliance-heavy enterprises is an old, occupied category.
6. **Styra (OPA's commercial control plane)** — direct control-plane comparable for OPA (covered partly under assignment 12, but Styra DAS itself deserves distinct consideration).

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/14_cerbos.jsonl` (45 records). Condensed table:

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| CERBOS-001 | Platform = OSS PDP + Hub control plane + Synapse; "structured decision logs with policy version lineage, built in"; Zero Trust/AI positioning | https://www.cerbos.dev/ | official-marketing | 2026-08-18 | HIGH |
| CERBOS-002 | CheckResources main entrypoint (50×50 default), PlanResources, gRPC+REST, includeMeta (matchedPolicy/effectiveDerivedRoles), cerbosCallId | https://docs.cerbos.dev/cerbos/latest/api/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-003 | "Sub-millisecond policy evaluation", stateless, air-gapped deployable | https://www.cerbos.dev/product-cerbos-pdp | official-marketing | 2026-08-18 | MEDIUM |
| CERBOS-004 | Output model binary: EFFECT_ALLOW/EFFECT_DENY; no review verdict | https://docs.cerbos.dev/cerbos/latest/api/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-005 | Policy outputs: CEL expressions on ruleActivated/conditionNotMet returned in response; designed for explaining decisions | https://docs.cerbos.dev/cerbos/latest/policies/outputs.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-006 | CEL conditions over P/R/auxData(JWT, multi-token)/variables/constants/globals/runtime | https://docs.cerbos.dev/cerbos/latest/policies/conditions.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-007 | Policies uniquely identified by name+version; parallel versions (prod/staging); `default` fallback | https://docs.cerbos.dev/cerbos/latest/policies/resource_policies.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-008 | Six policy types: resource, principal, derived roles, role policies, exported variables/constants | https://docs.cerbos.dev/cerbos/latest/policies/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-009 | Scoped policies: hierarchical scopes, two scopePermissions modes; multi-tenant & regional customization use cases | https://docs.cerbos.dev/cerbos/latest/policies/scoped_policies.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-010 | Cerbos CEL time extensions now()/timeSince(); RFC3339 timestamps, durations | https://docs.cerbos.dev/cerbos/latest/policies/conditions.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-011 | Access + decision logs; backends local(7d default)/file/Kafka/Hub; cerbosCallId; JSONPath masking | https://docs.cerbos.dev/cerbos/latest/configuration/audit.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-012 | v0.33.0: store-specific policy revision metadata (git commit hash) in audit entries | https://docs.cerbos.dev/cerbos/latest/releases/v0.33.0.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-013 | v0.51.0: requestContext → audit logs; DeletePolicies integrity checks; PurgeStoreRevisions | https://www.cerbos.dev/blog/cerbos-pdp-v0-51-0-policy-lifecycle-management-audit-enhancements-and-scopes | official-marketing | 2026-08-18 | HIGH |
| CERBOS-014 | Hub audit collection: plan-based retention, filter UI, policy-to-source links, PDP-side masking, age-encrypted exports (Owner-only) | https://docs.cerbos.dev/cerbos-hub/audit-log-collection.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-015 | Hub concepts: versioned stores; validate+test on change; bundle pushed "within seconds"; failed tests block; encrypted versioned bundles; audit/rollback | https://docs.cerbos.dev/cerbos-hub/concepts.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-016 | Deployments: immutable store versions per attempt; revert; PDP fleet monitoring tab | https://docs.cerbos.dev/cerbos-hub/deployments.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-017 | cerbos compile: full YAML test framework (fixtures, matrix, pinned now, filters) + GitHub Actions/GitLab/Dagger CI | https://docs.cerbos.dev/cerbos/latest/policies/compile.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-018 | Hub "validates, tests, signs, and distributes every policy change… turnkey CI/CD" | https://docs.cerbos.dev/cerbos-hub/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-019 | Policy stores: git ("pull requests and reviews"), CI/CD, SDKs, CLI, browser upload; scoped client credentials | https://docs.cerbos.dev/cerbos-hub/policy-stores.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-020 | ePDP WASM: browser/edge/Node/React Native; 10–60s polling; no admin endpoints; logs via onDecision only | https://docs.cerbos.dev/cerbos-hub/deployments-epdp-rules.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-021 | OpenID AuthZEN endpoints implemented | https://docs.cerbos.dev/cerbos/latest/api/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-022 | SDKs: JS, Go, Python, Java, .NET, Rust, PHP, Ruby | https://docs.cerbos.dev/cerbos/latest/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-023 | Admin API: policy CRUD/disable, schemas, store reload, audit retrieval; single-admin basic auth; SQL stores required for mutation | https://docs.cerbos.dev/cerbos/latest/api/admin_api.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-024 | Storage drivers: disk, git, blob (S3/GCS), Hub, SQLite3/MySQL/Postgres, overlay circuit breaker | https://docs.cerbos.dev/cerbos/latest/configuration/storage.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-025 | Hub RBAC: org roles Owner/Developer/Analyst/Viewer/Member; workspace roles; Analyst views but cannot export audit logs | https://docs.cerbos.dev/cerbos-hub/user-management.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-026 | Pricing: OSS free; $0 PoC; from $25/mo Dev; from $933/mo Production (5,000 MAPs, 1yr logs); Enterprise = SSO, self-hosted Hub, custom retention, SLA | https://www.cerbos.dev/pricing | official-marketing | 2026-08-18 | HIGH |
| CERBOS-027 | SOC 2 Type II announced 2024-01-09 (scope/auditor unspecified) | https://www.cerbos.dev/news/cerbos-achieves-soc-2-type-ii-compliance | official-marketing | 2026-08-18 | HIGH |
| CERBOS-028 | Utility Warehouse: FTSE 250, 4,500 services, self-hosted OSS PDP; audit logs praised | https://www.cerbos.dev/customers/utility-warehouse | case-study | 2026-08-18 | HIGH |
| CERBOS-029 | 9fin: fintech; product packaging in 10 minutes; "strict compliance controls" | https://www.cerbos.dev/customers/9fin | case-study | 2026-08-18 | HIGH |
| CERBOS-030 | Synapse: decision-time enrichment from IdPs/DBs/APIs; WASM custom adapters; TTL caching | https://www.cerbos.dev/product-cerbos-synapse | official-marketing | 2026-08-18 | MEDIUM |
| CERBOS-031 | Prometheus /_cerbos/metrics; OTLP metrics + tracing | https://docs.cerbos.dev/cerbos/latest/configuration/observability.html | official-doc | 2026-08-18 | MEDIUM |
| CERBOS-032 | GitHub: Apache 2.0, ~4.5k stars, Go, open core | https://github.com/cerbos/cerbos | official-doc | 2026-08-18 | HIGH |
| CERBOS-033 | Funding: $3.5M seed 2021 (Crane) + $7.5M extended seed 2023 (OMERS); founders Baran & Ellawala; Zenauth Ltd | https://siliconangle.com/2023/04/12/cerbos-raises-7-5m-open-source-authorization-platform/ | third-party | 2026-08-18 | MEDIUM |
| CERBOS-034 | Deny-override conflict resolution; scope hierarchy modes | https://docs.cerbos.dev/cerbos/latest/policies/resource_policies.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-035 | JSON Schema validation of attributes; reject/warn enforcement; validationErrors | https://docs.cerbos.dev/cerbos/latest/policies/schemas.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-036 | PlanResources: ALWAYS_ALLOWED/ALWAYS_DENIED/CONDITIONAL AST; adapters (Prisma, Drizzle, Mongoose, SQLAlchemy…) | https://www.cerbos.dev/blog/filtering-database-results-with-cerbos-query-plans | official-marketing | 2026-08-18 | HIGH |
| CERBOS-037 | Hub playgrounds: collaborative IDE, Explore tab, permissions matrix; not auto-pushed to stores | https://docs.cerbos.dev/cerbos-hub/playground.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-038 | MCP/AI-agent tool-call authorization with full audit trail | https://www.cerbos.dev/ecosystem/mcp | official-marketing | 2026-08-18 | MEDIUM |
| CERBOS-039 | Use-case catalog (AI, multi-tenant SaaS, product packaging…); no promotions/marketing-compliance use case exists | https://www.cerbos.dev/use-cases | official-marketing | 2026-08-18 | HIGH |
| CERBOS-040 | apiVersion api.cerbos.dev/v1; documented policy format has no metadata/annotations (no legal-provenance field) | https://docs.cerbos.dev/cerbos/latest/policies/resource_policies.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-041 | Absence: no Hub-native policy approval workflow; approvals = customer git process | https://docs.cerbos.dev/cerbos-hub/user-management.html | official-doc | 2026-08-18 | MEDIUM |
| CERBOS-042 | Absence: no effective-date/scheduled policy activation; nearest = CEL time conditions, manual ePDP bundle activation | https://docs.cerbos.dev/cerbos-hub/deployments-epdp-rules.html | official-doc | 2026-08-18 | MEDIUM |
| CERBOS-043 | Deployment patterns: K8s service/sidecar/daemonset, serverless, systemd; ghcr.io images | https://docs.cerbos.dev/cerbos/latest/index.html | official-doc | 2026-08-18 | HIGH |
| CERBOS-044 | Third-party positioning vs AuthZed/SpiceDB, Oso, Permit.io, PlainID, OpenFGA, OPA, Axiomatics; "easier than OPA" | https://guptadeepak.com/tools/top-5-authorization-pbac-tools-2026/ | third-party | 2026-08-18 | MEDIUM |
| CERBOS-045 | ePDP audit logs are local-only via onDecision; no built-in transmission to Hub | https://www.cerbos.dev/blog/audit-logs-for-cerbos-hub-embedded-pdps | official-marketing | 2026-08-18 | HIGH |

## 17. Verdict

**MAJOR OVERLAP**

Cerbos is not a promotions, regulatory-content, or signals company — it will never compete on jurisdiction rules, counsel workflow, identity/geo verification, or promotion administration (A, C-content, E, F blocks are 0–2). But it already ships the technical core of the Promotion OS hypothesis as commodity infrastructure: versioned executable policies with jurisdiction-capable scope hierarchies, sub-millisecond cross-product allow/deny APIs, reason outputs, a test-gated legal-change-shaped CI/CD pipeline, immutable version pinning with rollback, and — most importantly — decision logs that reconstruct "why was this allowed?" down to the git commit of the policy, centrally searchable, exportable, and retained up to a year. That is J05/J07/J10 and most of B/D/G/H, available from $0 (Apache 2.0) to $933/month. Any Promotion OS must either build on such an engine or out-differentiate it purely on regulatory content, counsel workflow, impact analysis, signals, and domain state — because a capable enterprise can assemble the rest from Cerbos today.

