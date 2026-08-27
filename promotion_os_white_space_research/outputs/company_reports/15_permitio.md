# Company Report — Permit.io

Researcher: Research Agent 15 (Permit.io)
Date: 2026-08-18
Category: Generic policy infrastructure
Manager: Manager D

## 1. Executive summary

Permit.io is a venture-backed ($14M raised; $8M Series A, Feb 2024) full-stack **authorization-as-a-service** vendor. Its actual core product is a SaaS **policy control plane** — a no-code/low-code policy editor supporting RBAC, ABAC, and ReBAC that generates Rego (OPA) or Cedar policy code — paired with a **self-hostable decision plane**: open-source Policy Decision Point (PDP) containers kept in sync in real time by OPAL, Permit's widely adopted open-source policy/data distribution layer (~5.5k GitHub stars) [PERMITIO-001, 006, 009, 032].

The buyer is overwhelmingly **engineering/platform teams** who need application permissions (who can do what in our product) without building an in-house authorization system. Case-study customers include Maricopa County Recorder's Office (voter-data systems), Honeycomb Insurance, Hipp Health, Centauri AI (fintech), Salt Security, and Cisco/Epsagon [PERMITIO-028, 029]. The job it is hired to do: "implement and operate fine-grained application permissions in days instead of quarters, with a UI that non-engineers can read."

Since 2025, positioning has pivoted hard toward **AI-agent access control** (MCP Gateway, "four-perimeter" framework, human-in-the-loop approvals for agent actions) [PERMITIO-001, 035].

Relevance to the core question: Permit.io's policy-management/control-plane model is **mechanically the closest generic analog to the proposed regulatory decision infrastructure in this study's policy-infrastructure category** — versioned executable policy, environment promotion with review, real-time distributed decisioning, decision logs with reasons, and decision replay all exist. What is entirely absent is everything regulatory: legal content, jurisdiction intelligence, counsel workflow semantics, signal generation/normalization, and evidence-grade guarantees.

## 2. Product architecture

Core entities: **Workspace (org) → Project (one per product) → Environment (prod/staging/dev, each a policy+data silo with its own API key)**; inside an environment: **Resources** (protected object types, with actions and attributes), **Roles**, **Condition sets** (user sets/resource sets for ABAC), **Relationship tuples + role derivations** (ReBAC), **Users/Tenants** (end-customer orgs), and **Policies** connecting them [PERMITIO-011, 009, 010].

Concrete flow:

INPUT → An application calls `permit.check(user, action, resource[, tenant, context])` via SDK or the PDP's REST `/allowed` endpoint, optionally passing just-in-time attributes (e.g., `location: "England"`) [PERMITIO-002, 003].

DECISION → The check is evaluated **synchronously** by a PDP — either Permit's managed Cloud PDP (RBAC/ReBAC only) or a customer-deployed container PDP (required for ABAC/custom data), which holds all policies and data locally and answers in <10ms p95 [PERMITIO-004, 005]. Policy edits made in the SaaS editor compile to Rego/Cedar and propagate to every connected PDP as diffs via OPAL in ~100ms p95; with GitOps enabled the generated code is committed to the customer's git repo first [PERMITIO-009, 012, 032].

OUTPUT → A boolean allow/deny to the caller; a **decision log** (user, action, resource, tenant, result, human-readable reason; more detail in Debug Mode) recorded in Permit's cloud audit system, queryable/filterable via UI and API and replayable against test PDPs [PERMITIO-013, 014, 015].

Management-plane separation: policy configuration lives in Permit's cloud; the data plane (PDP + authorization data) can remain entirely in the customer's VPC — "No sensitive data leaves your network/cloud" — and decisions keep working if Permit's cloud is down [PERMITIO-032].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Policy Editor (RBAC/ABAC/ReBAC/PBAC) | No-code UI defining resources/actions/roles/conditions; generates Rego or Cedar on save | Engineering (readable by product/ops) | Core | PERMITIO-009, 007, 010 |
| PDP (decision point) | Self-hosted or cloud microservice answering `/allowed`, bulk, user-permissions, AuthZen queries; <10ms p95 local | Engineering/platform | Core | PERMITIO-002, 004, 005 |
| OPAL (open source) | Real-time policy+data sync from git/APIs/DBs/S3 to policy agents; the distribution backbone | Platform/infra | Core (also standalone OSS) | PERMITIO-006, 032 |
| Projects/Environments + env-copy APIs | Policy lifecycle: dev→staging→prod promotion, preview envs per policy PR, per-env API keys and member roles | Engineering | Core | PERMITIO-011, 017 |
| GitOps + Terraform provider | Policy-as-code in the customer's repo (branch per environment, PR review), full config as Terraform | Platform/DevOps | Core capability, config add-on | PERMITIO-012, 025 |
| Audit/decision logs + Debug Mode + Replay API | Per-check decision records with reasons; replay historical checks against a PDP to validate policy changes | Engineering (compliance-adjacent) | Core | PERMITIO-013, 014, 015 |
| Permit Elements | Embeddable UIs: user management, audit log viewer, access requests, operation approvals (Reviewer/Approved roles, webhooks) | Engineering (serving end users) | Add-on (included all tiers) | PERMITIO-018, 019, 043 |
| Policy Guard | Org-wide baseline policy rules enforced across projects/environments; Owner-only changes; API-only today | Platform governance | Add-on (early) | PERMITIO-021 |
| AI Access Control / MCP Gateway | Agent identities, prompt/RAG/action/response perimeters, human-in-the-loop approvals for agent actions | Engineering/AI teams | New strategic layer | PERMITIO-035 |

## 4. API / developer capability

- **APIs**: Public REST API at `api.permit.io/v2/` (EU: `api.eu.permit.io`) covering schema (resources/roles/condition sets), facts (users/tenants/role assignments/relationship tuples), environments/projects, members, Elements, and audit logs; bearer auth with **three key scopes** (organization / project / environment) [PERMITIO-022]. PDP-side decision API: `/allowed`, `/allowed/bulk`, `/user-permissions`, `/authorized_users`, plus OpenID **AuthZen**-conformant endpoints [PERMITIO-002, 005, 034].
- **SDKs**: Node.js, Python, Go, .NET, Java, Ruby (+ beta PHP, Kotlin, Erlang, C++) [PERMITIO-024].
- **Webhooks**: Elements events (user created, approval decided) with shared-secret validation; PDP data-sync-error webhooks. No documented per-decision or policy-change webhooks [PERMITIO-036].
- **Sandbox**: free-forever tier plus unlimited projects/3+ environments; environments are cheap, copyable isolation units — preview environments per policy change are a documented pattern [PERMITIO-011, 017, 027].
- **Rules engine**: OPA (Rego) or Cedar under the hood; UI-generated code plus custom Rego/Cedar escape hatch [PERMITIO-009, 033].
- **Synchronous decisioning**: yes — `permit.check()` is the product [PERMITIO-002].
- **Latency claims**: <10ms p95 local PDP enforcement; ~100ms p95 policy-update propagation; homepage claims sub-millisecond decisions and "hundreds of millions of identities at sub-50ms" (marketing) [PERMITIO-004, 001].
- **Versioning**: versioned API base path (`/v2/`) [PERMITIO-022]. Policy versioning via git (GitOps) [PERMITIO-012].
- **Idempotency**: no idempotency-key mechanism documented (unresolved) [see Section 12 notes].
- **Rate limits**: documented — management API 1,000 req/min overall (schema writes 40/min); Cloud PDP `/allowed` 1,000 req/min per IP, bulk 200/min; container PDP uncapped [PERMITIO-022, 023].
- **Integration model**: SDK/PEP calls at every enforcement point in application code; PDP as sidecar/central service/cluster in customer infra; data synced from Permit cloud or fetched from customer sources via OPAL without touching Permit's cloud [PERMITIO-005, 030, 032].

## 5. Rules / decision model

- **Arbitrary attributes**: yes — typed user/resource/tenant/environment attributes with operators (equals, greater-than, between, in, ref-comparisons, e.g., `user.age > 40`, `environment.location in [US, Canada]`, `resource.time > "17:00"`), nested allOf/anyOf logic; attributes can be stored or passed JIT at check time [PERMITIO-003, 007, 041].
- **Customer/user state**: yes for authorization-relevant state — users, tenants, roles, resource instances, relationship tuples, attributes, synced to PDPs with "no practical limits on number of objects"; **no** event/aggregate store (no built-in counters like "3rd entry today"; computed state must be supplied as attributes) [PERMITIO-030].
- **Reason codes**: partial — the **check response is boolean**; human-readable reasons ("user '…' does not match any rule that grants him the 'delete' permission…") appear in decision logs, and richer per-decision explanation requires Debug Mode (latency cost, not recommended in production) [PERMITIO-002, 013, 014].
- **Allow/deny/review**: allow/deny natively; a "review" path exists only as an application-level pattern via the Operation Approval / Access Request Elements (auto-created Reviewer/Approved roles, approval webhooks) — not a third decision outcome from the PDP [PERMITIO-002, 018, 043].
- **Simulate policies**: partial — documented approach is testing against PDPs synced to dev/preview environments plus the **Audit Log Replay API** ("Verify that policy changes don't break existing permissions") replaying up to 30 days of real production checks against a test PDP; no one-click simulation/decision-diff report [PERMITIO-015, 016, 017].
- **Replay decisions**: yes, as above — replay of recorded check inputs against a chosen PDP; 30-day window, concurrency 10, test-PDPs-only guidance [PERMITIO-015].
- **Version policies**: yes — GitOps commits every editor change as Rego/Cedar to the customer's repo (branch per environment; git history = policy history; rollback via git), plus Terraform for config [PERMITIO-012, 025].
- **Deploy rules independently of app code**: yes — this is the core value proposition; policy changes propagate to all PDPs in ~100ms without app redeploys [PERMITIO-004, 032].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance**: none — no promotion/sweepstakes concepts anywhere in the documented product surface (inference from full docs enumeration) [PERMITIO-040].
- **Generic regulatory workflow**: nothing regulatory-specific; the generic machinery (policy editor → git review → environment promotion → enforcement → decision logs) could carry regulatory rules authored by the customer [PERMITIO-012, 017].
- **Jurisdiction restrictions**: mechanism only — documented ABAC examples are literally jurisdiction-shaped ("Employees based within the European Union can perform any action on GDPR Protected Document"; `environment.location in [US, Canada]`), but the customer authors every rule and supplies the location value [PERMITIO-007].
- **Location verification**: none — Permit consumes a location attribute passed by the caller; it has no geolocation, GPS, IP, or proxy/VPN detection (scope-boundary evidence: authorization-only positioning) [PERMITIO-031, 007].
- **Legal content/rules**: none — no legal content library, no citations, no counsel-facing features (inference) [PERMITIO-040].
- **Regulatory monitoring**: none (inference from full product surface) [PERMITIO-040].
- **Change management**: strong but generic — GitOps PR review, copy-env/preview-env CI flows, Policy Guard org baselines (Owner-only), activity audit logs of permission changes [PERMITIO-012, 017, 021, 013].
- **Counsel approval**: no counsel construct. Nearest substitutes: Workspace **Viewer** role (read-only policy visibility), git PR review (any reviewer, including counsel, via GitHub), and Elements approval flows — which govern **end-user actions at runtime**, not policy deployment [PERMITIO-020, 012, 018].
- **Historical policy state**: git history of all policy code with GitOps; environment copies; decision logs are time-stamped but are **not pinned to a policy version/commit** in any documented way [PERMITIO-012, 013, 014].

## 7. Audit / evidence

Can a customer reconstruct:

- **Exact inputs?** Largely — decision logs capture user, action, resource, tenant, result; JIT attribute payloads are captured in replayable form (the Replay API re-executes "the exact request patterns"); full input detail is richest with Debug Mode on [PERMITIO-013, 015, 14].
- **Exact rule/policy?** Partially — Debug Mode records "which policy was taken into consideration" and environment policy configuration, but it is latency-costly and discouraged in production; otherwise the rule must be inferred from the reason string [PERMITIO-014, 013].
- **Exact version?** Not natively — no documented decision→policy-version/commit linkage. With GitOps, a customer can correlate a decision timestamp to the git commit history of the environment branch (assembly, labeled inference) [PERMITIO-012, 013].
- **Exact output + timestamp?** Yes — result and timestamp are core decision-log fields [PERMITIO-013].
- **Human approvals?** Partially — Elements approval/denial events exist with webhooks (customer can persist them); workspace activity logs record permission changes; no documented long-term, signed approval record [PERMITIO-018, 043, 013].
- **Source/legal authority?** No — no legal-provenance model exists [PERMITIO-040].

Constraints that matter for evidence-grade use: audit-log query API caps at 10,000 results; retention is plan-based (14 days on free tier; "contact support" for extended; enterprise custom); replay window is 30 days; no tamper-evidence/integrity sealing is documented (unresolved) [PERMITIO-013, 015, 027].

## 8. Enterprise readiness

- **SSO/RBAC**: SSO on Enterprise tier; workspace RBAC (Owner/Editor/Viewer) assignable at workspace, project, or environment granularity [PERMITIO-027, 020].
- **Multitenancy / multi-brand**: first-class — tenants are a core decision parameter (per-tenant roles for the same user); projects separate products/brands; Policy Guard enforces cross-project baselines [PERMITIO-002, 011, 021].
- **Environments**: unlimited projects, environments per plan; copy/create-env APIs; per-env keys and member access [PERMITIO-011, 017, 027].
- **Security certifications**: SOC 2 Type II (renewed Jan 2026), HIPAA with BAA, GDPR/CCPA support, AWS KMS-managed encryption; reports gated to Enterprise [PERMITIO-026, 027].
- **SLA**: Enterprise custom SLAs "including 99.99%"; free tier best-effort [PERMITIO-027].
- **Support / professional services**: community Slack (free tier) → dedicated CSM + professional services (Enterprise) [PERMITIO-027].
- **Customer scale examples**: Maricopa County ("millions of... voters"), Cisco/Epsagon, Accenture, Schneider Electric, SignifyHealth; homepage claims "hundreds of millions of identities" (marketing) [PERMITIO-028, 029, 001].
- **Resilience posture**: decisions are local to customer-hosted PDPs; control-plane outage does not stop decisioning; hybrid "data never leaves your VPC" model [PERMITIO-032].

## 9. Commercial model

- **Pricing (public)**: Community free forever (1,000 MAU, 20 tenants, 3 environments, 14-day audit retention, all policy models + Elements); Startup from **$150/month up to 10,000 MAU** (Nov 2024); Enterprise custom (no limits, SSO, custom SLA, compliance suite, PS). "No Blackout Features" — quota-based, not feature-gated [PERMITIO-027, 044].
- **Likely buyer**: engineering/platform leadership (CTO, platform team lead); security/IAM leaders increasingly targeted via AI-agent positioning [PERMITIO-001, 035].
- **Implementation burden**: light for basic RBAC (case studies: "one day to implement", "two weeks... to production"), but grows with enforcement-point count — every guarded action needs a `permit.check()` call wired into app code, plus PDP operation for ABAC [PERMITIO-028, 005] (burden characterization partly inference).
- **Sales motion**: product-led self-serve (free tier, docs-first, community Slack) with enterprise sales overlay [PERMITIO-027, 044].
- **Large-customer evidence**: real but thin — press-reported logos (Accenture, Cisco, Schneider Electric) and mid-size case studies; company is startup-stage ($14M raised) [PERMITIO-028, 029].

## 10. Strengths

- **Complete policy-lifecycle control plane**: editor → generated code → git version history → environment promotion with preview envs → real-time distribution → decision logs → replay. This is the most fully assembled generic policy SDLC in its category per official docs [PERMITIO-009, 012, 015, 017].
- **Real-time, low-latency, resilient decisioning** at the edge with clean control/data-plane separation and a "data stays in your VPC" story attractive to regulated customers [PERMITIO-004, 032].
- **Three policy models (RBAC/ABAC/ReBAC) in one system**, dual-engine (OPA Rego and Cedar), with a custom-code escape hatch [PERMITIO-009, 033].
- **Open-source gravity**: OPAL (~5.5k stars) and open PDP/SDKs reduce adoption fear and lock-in objections; AuthZen standard conformance [PERMITIO-006, 034].
- **Human-in-the-loop approval primitives** (access requests, operation approvals with Reviewer roles and webhooks) — rare among policy-infra vendors and directly relevant to "review" decision paths [PERMITIO-018, 043].
- **Accessible commercial model**: generous free tier, transparent $150 startup tier, no feature blackouts [PERMITIO-027, 044].

## 11. Weaknesses / constraints

- **Boolean decision contract**: no native review/escalate outcome; no reason codes in the response payload (reasons live in logs; detailed explanations require latency-costly Debug Mode) [PERMITIO-002, 013, 014].
- **Evidence layer is operational, not evidentiary**: plan-based retention (14 days free; extended "via support"), 10k-result API cap, 30-day replay window, no documented decision→policy-version pinning, no tamper-evidence [PERMITIO-013, 015, 027; absence of integrity features unresolved].
- **Temporal logic is caller-supplied**: even `current_time` must be passed as an attribute; no native effective-dating of rules [PERMITIO-008].
- **Allow-based managed model**: deny-overrides, rule priority, and conflict resolution require hand-written Rego/Cedar "at your own risk" [PERMITIO-033, 039 — partly inference].
- **Cloud PDP cannot do ABAC** — attribute-based policies force customers to operate container PDPs [PERMITIO-005].
- **No domain content of any kind**: no jurisdictional/legal/promotional semantics, no signal generation (identity/geo/fraud), no regulatory monitoring [PERMITIO-031, 040 — inference-labeled].
- **Startup-stage vendor** ($14M raised) with R&D visibly pivoting to AI-agent access control — competing priorities for any regulatory-domain roadmap (inference from funding + positioning) [PERMITIO-029, 035].

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,PERMITIO-040
A02,0,PERMITIO-040
A03,0,PERMITIO-040
A04,0,PERMITIO-040
A05,0,PERMITIO-040
A06,0,PERMITIO-040
A07,0,PERMITIO-040
A08,0,PERMITIO-040
A09,0,PERMITIO-040
A10,0,PERMITIO-040
B01,4,PERMITIO-002;PERMITIO-022
B02,4,PERMITIO-002;PERMITIO-004
B03,4,PERMITIO-004;PERMITIO-005
B04,2,PERMITIO-002;PERMITIO-018
B05,2,PERMITIO-013;PERMITIO-002
B06,4,PERMITIO-003;PERMITIO-041
B07,3,PERMITIO-030;PERMITIO-011
B08,1,PERMITIO-039;PERMITIO-033
B09,2,PERMITIO-016;PERMITIO-017
B10,3,PERMITIO-015
C01,2,PERMITIO-007;PERMITIO-041
C02,1,PERMITIO-009
C03,1,PERMITIO-009;PERMITIO-002
C04,2,PERMITIO-008;PERMITIO-041
C05,3,PERMITIO-012
C06,0,PERMITIO-040
C07,2,PERMITIO-015;PERMITIO-017
C08,1,PERMITIO-012;PERMITIO-020
C09,0,PERMITIO-040
C10,0,PERMITIO-040;PERMITIO-042
D01,2,PERMITIO-013
D02,4,PERMITIO-013
D03,2,PERMITIO-014;PERMITIO-012
D04,3,PERMITIO-013;PERMITIO-014
D05,2,PERMITIO-018;PERMITIO-043
D06,2,PERMITIO-015;PERMITIO-014
D07,2,PERMITIO-013;PERMITIO-037
D08,2,PERMITIO-013;PERMITIO-027
D09,?,
D10,3,PERMITIO-013;PERMITIO-019;PERMITIO-037
E01,0,PERMITIO-031
E02,1,PERMITIO-041;PERMITIO-031
E03,0,PERMITIO-031;PERMITIO-040
E04,1,PERMITIO-007;PERMITIO-031
E05,0,PERMITIO-031;PERMITIO-040
E06,0,PERMITIO-031;PERMITIO-040
E07,0,PERMITIO-031;PERMITIO-040
E08,0,PERMITIO-031;PERMITIO-040
E09,1,PERMITIO-018;PERMITIO-043
E10,1,PERMITIO-030;PERMITIO-006
F01,0,PERMITIO-040
F02,0,PERMITIO-040
F03,0,PERMITIO-040
F04,0,PERMITIO-040
F05,0,PERMITIO-040
F06,0,PERMITIO-040
F07,1,PERMITIO-002;PERMITIO-010
F08,0,PERMITIO-040
F09,0,PERMITIO-040
F10,1,PERMITIO-006;PERMITIO-030
G01,4,PERMITIO-011;PERMITIO-002;PERMITIO-027
G02,3,PERMITIO-020
G03,3,PERMITIO-027
G04,2,PERMITIO-018;PERMITIO-012
G05,4,PERMITIO-011;PERMITIO-017
G06,3,PERMITIO-016;PERMITIO-015
G07,3,PERMITIO-012;PERMITIO-017;PERMITIO-021
G08,2,PERMITIO-036
G09,3,PERMITIO-027
G10,3,PERMITIO-026
H01,4,PERMITIO-022
H02,4,PERMITIO-024
H03,2,PERMITIO-036
H04,3,PERMITIO-011;PERMITIO-027
H05,3,PERMITIO-022
H06,?,
H07,3,PERMITIO-022;PERMITIO-023
H08,3,PERMITIO-037;PERMITIO-014
H09,4,PERMITIO-012;PERMITIO-025
H10,3,PERMITIO-025;PERMITIO-012
I01,1,PERMITIO-026;PERMITIO-028
I02,4,PERMITIO-001;PERMITIO-024;PERMITIO-022
I03,0,PERMITIO-040
I04,1,PERMITIO-018;PERMITIO-035
I05,3,PERMITIO-028;PERMITIO-029
I06,4,PERMITIO-027;PERMITIO-044
I07,1,PERMITIO-027
I08,2,PERMITIO-006;PERMITIO-012
I09,2,PERMITIO-028;PERMITIO-002
I10,3,PERMITIO-027;PERMITIO-044
J01,2,PERMITIO-009;PERMITIO-012;PERMITIO-007
J02,2,PERMITIO-017;PERMITIO-012
J03,1,PERMITIO-020;PERMITIO-012
J04,2,PERMITIO-015
J05,4,PERMITIO-002;PERMITIO-004;PERMITIO-011
J06,1,PERMITIO-003;PERMITIO-030
J07,2,PERMITIO-013;PERMITIO-014
J08,2,PERMITIO-015;PERMITIO-012
J09,1,PERMITIO-042
J10,2,PERMITIO-011;PERMITIO-012;PERMITIO-017;PERMITIO-021
```

**Scoring notes (reasoned 0s, low scores, and ?s):**

- **A01–A10 = 0 (labeled inference, PERMITIO-040)**: the complete documented product surface (docs IA, homepage, pricing, customers) is domain-neutral authorization infrastructure; no promotion/sweepstakes/contest/fulfillment/tax concept exists anywhere. This is enumeration-of-feature-set evidence, not mere absence of a single mention.
- **B04/B05 = 2**: allow/deny is native and reasons exist in decision logs; but no third "review" outcome in the decision API (approval flows are a separate Elements pattern) and no machine-readable reason codes in the check response.
- **B08 = 1 (partly inference, PERMITIO-039)**: allow-grant UI model; deny/priority only via custom Rego/Cedar "at your own risk."
- **C02/C03 = 1**: resource-type and action granularity are generic modeling primitives; nothing product-type- or legally-aware about them; scored 1 rather than 0 because rules can be keyed to product/action types manually.
- **C06/C09/C10 = 0 (labeled inference)**: no regulatory monitoring, legal provenance, or legal policy library anywhere in the enumerated product surface (PERMITIO-040); CLI templates (PERMITIO-042) are technical scaffolding, not legal content.
- **C08 = 1**: counsel could be given Workspace Viewer or review git PRs, but there is no approver construct in the deployment path itself.
- **D09 = ?**: no evidence for or against tamper-evidence/integrity sealing of logs; no cryptographic anchoring documented, but no enumeration proves absence either.
- **E-series 0s (PERMITIO-031 + 040)**: positive scope-boundary — Permit states it does authorization only and delegates identity to auth providers; it generates no identity/geo/device/fraud signals. E02/E04 = 1 because age- and location-conditioned *enforcement* is documented (operators/examples) even though verification/detection is absent. E09 = 1: approval-management queue is a minimal review inbox, not case management. E10 = 1: OPAL data fetchers + JIT attributes can wire third-party signals into decisions, but there is no vendor-signal normalization layer.
- **F-series 0s (PERMITIO-040, labeled inference)**: no wallet/ledger/stored-value semantics in the enumerated surface. F07 = 1 because "can this user redeem X" is expressible as an authorization check over instances/attributes; F10 = 1 because OPAL can pull external ledger data into decisions. F05 note: temporal *access* patterns exist (PERMITIO-008) but credit-expiration semantics do not.
- **H06 = ?**: idempotency keys not documented anywhere located; cannot prove absence.
- **I03 = 0 (inference, PERMITIO-040)**: nothing addressed to marketing buyers in the entire surface.
- **I07 = 1**: scored as *low professional-services dependency* (self-serve product; PS exists only as optional Enterprise add-on). Note the scale direction for this square when aggregating.
- **I08/I09 = 2 (partly inference)**: open formats (Rego/Cedar/OPAL/AuthZen) cap lock-in, but per-enforcement-point SDK integration and synced authorization data create real switching/integration work.
- **J05 = 4**: cross-product, real-time action authorization is the core product (check API + multi-project/multi-tenant + documented latency); the hypothesis's "review" outcome exists only via the Elements approval pattern — noted, but the square's substance is category-leading here.
- **J01/J02/J04/J07/J08/J10 = 2**: in each case the *mechanism* is genuinely present (versioned executable policy; env-promotion workflow; replay-based change validation; decision logs; a policy lifecycle control plane) while the *regulatory substance* (legal content, counsel roles, evidence-grade guarantees, point-in-time version pinning) is absent.

## 13. White-space implications

1. **Already solved by Permit.io**: real-time cross-product action authorization (J05) as decoupled infrastructure — event/action API, synchronous low-latency evaluation, custom attributes, multi-tenant/multi-product scoping (B01–B03, B06, G01); the generic policy lifecycle: environments, git-versioned policy history, CI promotion, testing patterns, org-baseline guardrails (G05–G07, C05); developer platform table stakes (H-series); decision logging with reasons and 30-day replay (D02, B10).
2. **Partially solved**: allow/deny/review with reasons (boolean + logs + Elements approvals, no native review outcome or response reason codes); pre-rollout impact analysis (replay validates changes against ≤30 days of real traffic but produces no decision-diff report); decision reconstruction (logs + Debug Mode + git correlation, but no version pinning, short retention, no tamper-evidence); temporal rules (hand-built ABAC pattern, caller-supplied clock); human approvals (runtime operation approvals exist; policy-deployment approval is delegated to git tooling).
3. **Unsolved (absent entirely)**: jurisdictional/legal content and provenance (C06, C09, C10, J09); counsel-as-approver semantics in the deployment path (J03); identity/geo/fraud signal generation or normalization (E-series, J06); promotion-domain objects (A-series, F-series); evidence-grade guarantees (retention SLAs for logs, integrity sealing, regulator export packages).
4. **Could Permit add the missing capability easily?** The *workflow* pieces, yes — a "legal reviewer" role gating environment merges, decision-diff reports on replay, longer retention, and version-pinned decision logs are incremental engineering on existing primitives (inference). The *content and signal* pieces, no — jurisdictional rule libraries, legal monitoring, counsel UX, and vendor-signal normalization are a different product, buyer, and liability posture, far from their developer/AI-agent focus (inference from PERMITIO-035, 040).
5. **Could a customer assemble it on Permit + internal engineering?** Substantially, for the decisioning backbone: encode jurisdiction rules as ABAC condition sets/custom Rego, pass geo/KYC/fraud vendor outputs as JIT attributes, use GitOps PRs for counsel review, environments for staged rollout, replay for change validation, and Elements for manual-review paths. The customer would still own all legal content and its maintenance, build signal integration and normalization, build evidence-grade archival (export logs to their own store), and accept that reasons/version-pinning/effective-dating are DIY. This is exactly the "sophisticated enterprise adapts it" path the assignment asks about — it is credible for a strong platform team, and Permit's free/startup pricing makes the experiment cheap.
6. **What would make a customer buy a separate product instead?** (a) Maintained jurisdictional rule content with legal provenance and change monitoring — the part Permit will not own; (b) counsel-grade workflow and sign-off records that survive audits (vs. git PRs); (c) evidence-grade decision archives (long retention, integrity, version-pinned replay) vs. 14-day/plan-based logs; (d) normalized multi-vendor identity/geo/fraud signals; (e) a decision contract richer than boolean (allow/deny/review + machine-readable reasons); (f) accountability — a vendor whose product carries regulatory semantics rather than a toolkit the customer must keep legally current.

## 14. Replacement risk

**MEDIUM.**

Mechanically, Permit.io already ships most of the proposed product's skeleton — real-time authorization, versioned policy lifecycle, environments/approvals-by-git, decision logs, replay — so the *infrastructure* half of the thesis is one roadmap quarter away for them (they even market human-in-the-loop approvals and audit trails for AI-agent actions). But entering the *regulatory* space requires legal content operations, counsel-facing workflow, evidence-grade guarantees, and signal-vendor integrations — a different buyer (legal/compliance), different liability posture, and different GTM than their developer-led, AI-agent-focused strategy, on a $14M-raised startup's budget. The realistic threat is not Permit building Promotion OS; it is Permit (or its open-source OPAL/OPA stack) being the platform a prospect's engineering team uses to build the backbone in-house, shrinking the buyable surface to content, counsel workflow, and evidence [inference from PERMITIO-015, 017, 029, 035, 040].

## 15. Adjacent discoveries

- **Oso (osohq.com)** — direct authorization-as-a-service competitor (Polar language, managed authz); publishes Permit-alternatives content; belongs in any build-on-generic-authz substitute analysis.
- **Styra DAS / Open Policy Agent commercial arm** — the OPA creators' commercial control plane (policy lifecycle, impact analysis, decision logs for OPA at enterprise scale); the closest enterprise-grade comparable for "policy control plane as product."
- **Auth0 FGA / OpenFGA (Okta)** — Zanzibar-style fine-grained authorization service with an open standard; competes for the same ReBAC workloads and enterprise buyers.
- **Aserto** — authorization platform (also AuthZen-conformant) with decision logs; another assemble-it-yourself substrate.
- (Also noted: **Cedar/AWS Verified Permissions** and **Cerbos** are already covered as assignments 13–14; Permit's dual Rego/Cedar support makes it partially a superset/aggregator of those models.)

## 16. Evidence ledger

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| PERMITIO-001 | Core product: authorization-as-a-service (policy editor + PDPs + OPAL); 2025-26 repositioning to AI-agent access control; RBAC/ABAC/ReBAC; sub-ms latency claims; SOC 2 | https://www.permit.io/ | official-marketing | 2026-08-18 | HIGH |
| PERMITIO-002 | permit.check(user, action, resource, tenant, context) synchronous boolean authorize; /allowed, /allowed/bulk, /user-permissions, /authorized_users endpoints | https://docs.permit.io/how-to/enforce-permissions/check | official-doc | 2026-08-18 | HIGH |
| PERMITIO-003 | JIT attributes passed dynamically in check (location/hasApproval example) | https://docs.permit.io/how-to/enforce-permissions/check | official-doc | 2026-08-18 | HIGH |
| PERMITIO-004 | Local PDP enforcement <10ms p95; policy updates ~100ms p95 | https://docs.permit.io/concepts/differentiator-checklist/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-005 | Cloud PDP (RBAC/ReBAC only, no ABAC) vs edge/container PDP (sidecar/central/cluster/shard); AuthZen endpoints; caching | https://docs.permit.io/concepts/pdp/overview/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-006 | OPAL: Apache-2.0 OSS (~5.5k stars), real-time policy+data sync from git/APIs/DBs/S3 to OPA/Cedar agents | https://opal.ac/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-007 | Documented jurisdiction-shaped ABAC examples (EU employees / GDPR docs; environment.location in [US, Canada]) | https://docs.permit.io/how-to/build-policies/abac/overview/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-008 | Time-based access = ABAC pattern; current_time must be passed by caller in check() | https://docs.permit.io/how-to/build-policies/abac/time-based-role/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-009 | Policy editor (resources/actions/roles) generates Rego or Cedar on save; committed to git with GitOps | https://docs.permit.io/how-to/build-policies/policy-basics | official-doc | 2026-08-18 | HIGH |
| PERMITIO-010 | ReBAC: instance roles, relationship tuples, role derivations, hierarchies | https://docs.permit.io/how-to/build-policies/rebac/overview | official-doc | 2026-08-18 | HIGH |
| PERMITIO-011 | Workspace > project > environment hierarchy; env copy; per-env API keys; per-env member roles | https://docs.permit.io/manage-your-account/projects-and-env | official-doc | 2026-08-18 | HIGH |
| PERMITIO-012 | GitOps: generated policy code saved to customer git repo pre-deployment; branch per environment; PR review/tests; git versioning/rollback | https://docs.permit.io/integrations/gitops/overview | official-doc | 2026-08-18 | HIGH |
| PERMITIO-013 | Decision logs per check (user/action/resource/tenant/result/reason); filtering; 10k API cap; periodic log removal, extended retention via support | https://docs.permit.io/how-to/use-audit-logs/types-and-filtering | official-doc | 2026-08-18 | HIGH |
| PERMITIO-014 | Debug Mode adds why/which-policy/config context to decision logs; latency impact; discouraged in production | https://docs.permit.io/how-to/use-audit-logs/debug-mode/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-015 | Audit Log Replay API: re-execute historical checks vs a PDP ("verify policy changes don't break existing permissions"); 30-day window; concurrency 10; test PDPs only | https://docs.permit.io/how-to/use-audit-logs/audit-log-replay/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-016 | AuthZ testing: unit (OPA CLI), integration vs dev PDP, CI/CD-gated merges | https://docs.permit.io/how-to/sdlc/authz-testing/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-017 | CI/CD lifecycle: staging flow and preview-branch flow (create-env + copy-env per policy PR), review/approval then merge; auto-deploy to PDPs via OPAL | https://docs.permit.io/how-to/sdlc/ci-cd/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-018 | Operation Approval element: request-with-reason, auto-created Reviewer/Approved roles, approve/deny UI, webhook on decision; bank-transfer example | https://docs.permit.io/embeddable-uis/element/operation-approval/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-019 | Elements suite: user management, audit-log viewer, approval flows; embeddable, brandable, webhook-enabled | https://docs.permit.io/embeddable-uis/overview | official-doc | 2026-08-18 | HIGH |
| PERMITIO-020 | Workspace roles Owner/Editor/Viewer, assignable per workspace/project/environment | https://docs.permit.io/manage-your-account/workspace-settings/ | official-doc | 2026-08-18 | MEDIUM |
| PERMITIO-021 | Policy Guard: org-wide baseline policies across projects; Owner-only changes; API-only | https://docs.permit.io/how-to/policy-guard/policy_guard/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-022 | REST API api.permit.io/v2 (EU region option); org/project/env API key scopes; rate limits (40/min schema writes, 1000/min overall, 429) | https://docs.permit.io/api/api-with-cli/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-023 | Cloud PDP per-IP rate limits: /allowed 1000 req/min, bulk 200 req/min | https://docs.permit.io/concepts/pdp/cloud-pdp-capabilities/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-024 | SDKs: Node/Python/Go/.NET/Java/Ruby (+4 beta); Terraform provider "not a full SDK" | https://docs.permit.io/sdk/sdks-overview | official-doc | 2026-08-18 | HIGH |
| PERMITIO-025 | Terraform provider manages resources/roles/condition sets/relations/attributes as code | https://docs.permit.io/integrations/infra-as-code/terraform-provider | official-doc | 2026-08-18 | HIGH |
| PERMITIO-026 | SOC 2 Type II (renewed Jan 2026), HIPAA BAAs, GDPR/SCCs, AWS KMS encryption | https://www.permit.io/trust | official-marketing | 2026-08-18 | HIGH |
| PERMITIO-027 | Pricing: free Community (1,000 MAU, 14-day audit retention, no SSO); Enterprise custom (no limits, SSO, 99.99% SLA options, compliance reports, PS); "No Blackout Features" | https://www.permit.io/pricing | official-marketing | 2026-08-18 | HIGH |
| PERMITIO-028 | Case studies: Maricopa County Recorder, Honeycomb Insurance, Hipp Health, Centauri AI, Salt Security, Rivulis; Cisco/Epsagon, TechSource testimonials | https://www.permit.io/customers | case-study | 2026-08-18 | MEDIUM |
| PERMITIO-029 | $8M Series A (Feb 2024), ~$14M total; 20+ customers incl. Accenture, Cisco, Schneider Electric, SignifyHealth | https://www.finsmes.com/2024/02/permit-io-raises-8m-in-series-a-funding.html | third-party | 2026-08-18 | MEDIUM |
| PERMITIO-030 | Data loading: UI/API/JIT; OPAL Scope Config fetches external data straight to PDPs (bypassing Permit cloud); no practical object limits; sharding | https://docs.permit.io/how-to/manage-data/loading-data | official-doc | 2026-08-18 | HIGH |
| PERMITIO-031 | Scope boundary: Permit does authorization only; integrates with any authN provider; performs no identity verification | https://docs.permit.io/authentication/permit-and-authentication/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-032 | Control plane (Permit cloud) vs data plane (customer VPC, "no sensitive data leaves your network"); OPAL pushes diffs in real time | https://docs.permit.io/overview/how-does-it-work/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-033 | Custom Rego/Cedar alongside generated code (deny overrides, time windows); "at your own risk" | https://docs.permit.io/integrations/gitops/custom_policy | official-doc | 2026-08-18 | HIGH |
| PERMITIO-034 | AuthZen interop conformance (OpenID Foundation, May 2024); early backers | https://openid.net/authorization-interop-results/ | third-party | 2026-08-18 | MEDIUM |
| PERMITIO-035 | AI Access Control: four-perimeter framework, MCP Gateway, auditable human-in-the-loop approvals for agent actions | https://www.permit.io/ai-access-control | official-marketing | 2026-08-18 | HIGH |
| PERMITIO-036 | Webhooks: Elements events + PDP sync-error notifications; no per-decision/policy-change webhooks documented | https://docs.permit.io/embeddable-uis/webhooks/ | official-doc | 2026-08-18 | MEDIUM |
| PERMITIO-037 | Observability: OpenTelemetry, structured logging, Datadog integration; dual audit surfaces | https://docs.permit.io/concepts/differentiator-checklist/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-038 | Perception: praised ease of use/policy editor/community; criticized limited flexibility for dynamic permissions | https://www.stackinsight.net/permitio-platform-review/ | user-report | 2026-08-18 | LOW |
| PERMITIO-039 | INFERENCE: allow-based managed model; deny/priority/conflict resolution only via custom code | https://docs.permit.io/how-to/build-policies/policy-basics | official-doc | 2026-08-18 | MEDIUM |
| PERMITIO-040 | INFERENCE (surface enumeration): no promotion, marketing, ledger, legal-content, or regulatory-monitoring features anywhere in the documented product | https://docs.permit.io/ | official-doc | 2026-08-18 | MEDIUM |
| PERMITIO-041 | ABAC operators: equals/greater-than/between/in/ref + allOf/anyOf nesting; age and location examples | https://docs.permit.io/api/working-with-abac/operators/ | official-doc | 2026-08-18 | MEDIUM |
| PERMITIO-042 | Permit CLI policy bootstrapping from templates/AI/OpenAPI; technical templates only, no domain packs | https://docs.permit.io/how-to/permit-cli/permit-cli-policy/ | official-doc | 2026-08-18 | MEDIUM |
| PERMITIO-043 | Access Request element: user requests access; admin/Level-1 approves or denies; grants permissions on approval | https://docs.permit.io/embeddable-uis/element/access-request/ | official-doc | 2026-08-18 | HIGH |
| PERMITIO-044 | Startup tier from $150/month up to 10,000 MAU (introduced Nov 2024) | https://www.businesswire.com/news/home/20241126651183/en/Permit.io-Introduces-New-Pricing-Bringing-Accessible-Fine-Grained-Authorization-to-Startups | official-marketing | 2026-08-18 | MEDIUM |

## 17. Verdict

**SUBSTITUTE**

Permit.io does not compete in the regulatory domain — it has zero legal content, no counsel workflow, no signal generation, and no promotion semantics. But it is the most complete generic substrate examined in this category for assembling the proposed product's mechanical core: real-time cross-product action authorization (its core product), git-versioned executable policy, environment-based deployment with review, decision logs with reasons, and replay-based change validation. A capable enterprise platform team could credibly build the Promotion OS decisioning backbone on Permit (or its open-source OPAL/OPA stack) plus outside counsel — making "assemble on Permit" the realistic build-side alternative a Promotion OS sale must beat. What the assembly path cannot supply is exactly the unsolved layer: maintained jurisdictional content with provenance, counsel-grade approval records, evidence-grade retention/integrity, version-pinned historical replay, and vendor-signal normalization. Threat of Permit itself entering that layer: moderate at most, given its developer-led, AI-agent-focused strategy and startup scale.
