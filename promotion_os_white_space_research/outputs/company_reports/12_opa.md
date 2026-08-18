# Company Report — Open Policy Agent (OPA)

Researcher: Research Agent 12 (Open Policy Agent)
Date: 2026-08-18
Category: Generic policy infrastructure
Manager: Manager D

> **Note on subject type:** OPA is not a company. It is a CNCF-graduated, Apache-2.0 open-source policy engine (OPA-002, OPA-032). Per the assignment, the capability matrix is scored on **what OPA itself provides out of the box**; the commercial ecosystem (Styra DAS, Enterprise OPA, OPA Control Plane, Regal) is covered in the architecture/ecosystem discussion and Section 15, with explicit notes on what requires internal engineering to operationalize.

## 1. Executive summary

**What it is.** OPA is a general-purpose, domain-agnostic policy *decision engine*: services hand it JSON input, it evaluates declarative Rego policies against that input plus replicated data, and returns a decision — "simple yes/no answers or complex structured outputs" (OPA-001, OPA-005). It ships as a self-hosted daemon/sidecar, an embeddable Go library, a Wasm compile target, or an IR for other runtimes (OPA-006). Around the engine, OPA provides a "management" layer of agent-side APIs: **bundles** (versioned policy/data distribution with signing), **decision logs** (per-decision evidence events with a unique `decision_id`, input, result and policy revision), **status** (rollout health), and **discovery** (fleet configuration) (OPA-009, OPA-010, OPA-011, OPA-014, OPA-015).

**Who "buys" it.** Nobody buys OPA; platform/infrastructure engineering teams adopt it for free. Production adopters include Goldman Sachs, Netflix, Capital One, BNY Mellon, State Street, Pinterest (Kafka authorization at ~400K–8.5M QPS), Atlassian, T-Mobile, and Appsflyer — the last using OPA specifically for data-privacy-regulation and consent policies across hundreds of microservices (OPA-021).

**What job it is hired for.** Decoupling policy from application code: microservice/API authorization, Kubernetes admission control, CI/CD and IaC guardrails, and increasingly application-level entitlement logic (OPA-001, OPA-019).

**Critical 2025–2026 development.** Apple hired OPA's three creators and much of Styra's engineering team (Aug 2025). OPA itself remains actively maintained (v1.19.1 released 2026-08-17) with unchanged CNCF governance, but the commercial control-plane market around OPA collapsed: Styra DAS is winding down (styra.com is offline), Enterprise OPA was donated then **archived with no active maintainer (June 2026)**, and the open-source OPA Control Plane is an early-stage headless replacement (OPA-022, OPA-023, OPA-024, OPA-026, OPA-028).

**Answer to the core question (preview).** If a company builds domain policy on OPA, the engine, distribution, testing, and decision-evidence *primitives* are excellent and free. Everything the Promotion OS hypothesis calls a product remains to be built: regulatory content, legal authoring/approval workflow, impact analysis, evidence storage/packaging, signal normalization, and the governance control plane — and the vendor that used to sell most of that (Styra) just exited the market.

## 2. Product architecture

Core entities:

- **Policy (Rego module):** declarative, Datalog-inspired rules organized in packages; supports defaults, `else` chains, comprehensions, user functions, JSON-Schema-typed inputs, and metadata annotations (title, description, authors, `related_resources`, custom keys) (OPA-004).
- **Data:** JSON documents replicated into OPA (bundles, pushes, or fetched during evaluation via `http.send`) (OPA-018).
- **Input:** arbitrary JSON supplied per query by the calling service (OPA-005).
- **Bundle:** gzipped tarball of policies + data with a manifest carrying `revision`, `roots`, and `rego_version`; polled with ETag/long-polling; optionally JWT-signed and verified before activation (OPA-009, OPA-010).
- **Decision:** result of evaluating a package path; assigned a unique `decision_id` (OPA-011, OPA-016).

Concrete flow:

```
INPUT  (JSON from caller: user, action, resource, geo, risk attributes, ...)
  -> DECISION/PROCESS
     OPA evaluates Rego policy (from activated bundle revision R)
     against input + in-memory data (+ optional http.send call-outs)
  -> OUTPUT
     structured decision (e.g. {"allow": false, "reasons": [...]}) + decision_id
     side channels: decision-log event {decision_id, input, result, path,
     bundles{revision}, timestamp, metrics} -> POSTed to a log sink;
     status events {bundle revision, activation errors} -> status sink
```

Deployment is per-service (sidecar/host daemon) or in-process (Go SDK, Wasm, IR, Swift OPA); the documented rationale is that local evaluation keeps decisions "fast and highly-available" (OPA-006, OPA-034). Fleet configuration can be centralized via discovery bundles (OPA-015). Everything server-side — bundle storage, log storage, dashboards, authoring UI, approvals — is out of scope for OPA itself and must be assembled from cloud storage, git, and observability tooling, or from a control-plane product (Section 3).

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| OPA engine (opa run/eval/exec) | Evaluates Rego policies against JSON input + data; REST Data/Policy/Query/Compile APIs; partial evaluation; SQL/UCAST data-filter compilation | Platform engineering (free adoption) | Core | OPA-001, OPA-016 |
| Rego language + tooling | Policy language; `opa test` (mocks, coverage, benchmarks), `opa fmt`, profiler, REPL, Rego Playground | Policy authors (engineers) | Core | OPA-004, OPA-017, OPA-003 |
| Management APIs: bundles | Versioned, signed policy/data distribution from any HTTP/S3/GCS/Azure/OCI backend; delta bundles | Platform engineering | Core | OPA-009, OPA-010 |
| Management APIs: decision logs | Per-decision evidence events (decision_id, input, result, revision, timestamp, metrics) with masking, buffering, sinks | Platform engineering / security | Core | OPA-011, OPA-012, OPA-013 |
| Management APIs: status + discovery | Rollout health reporting per instance; centralized fleet configuration | Platform engineering / SRE | Core | OPA-014, OPA-015 |
| Integration surface | Go SDK/API, Wasm, IR, Swift OPA; donated TS/React/C#/Java SDKs; Envoy/Spring/Kafka/Terraform/K8s (Gatekeeper) integrations | Engineering | Core/ecosystem | OPA-006, OPA-034, OPA-022, OPA-030 |
| Regal | Linter, language server, debugger for Rego; custom org rules; CI hooks | Engineering | Add-on (OSS, beta) | OPA-027 |
| OPA Control Plane (OCP) | OSS headless control plane: bundles from multiple git repos, env promotion via git, build-time datasources, push to cloud storage | Platform engineering | Add-on (OSS, early: 65 stars) | OPA-026 |
| Enterprise OPA (EOPA) | Data-heavy OPA distribution (SQL/DynamoDB/Neo4j datasources, data filtering, Live Impact Analysis) | Was: Styra enterprise customers | **Archived June 2026, unmaintained** | OPA-024, OPA-025 |
| Styra DAS | Was: commercial SaaS control plane (authoring, versioning, deployment, decision-log storage for OPA fleets) | Was: enterprises | **Winding down; company offline** | OPA-023, OPA-036 |

## 4. API / developer capability

- **APIs:** Full REST API — Data API (`GET/POST /v1/data/{path}`) for decisions; Policy API (CRUD of modules); Query API (ad hoc); Compile API (`/v1/compile`) for partial evaluation and SQL/UCAST data-filter generation; `/health`, `/health/live|ready` (policy-definable), `/metrics`, `/v1/config`, `/v1/status` (OPA-016, OPA-020). API paths are versioned (`/v0`, `/v1`) (OPA-016).
- **SDKs:** Go SDK (config/bundles/decision-logs handled) and low-level Go `rego` package; Wasm compilation for any Wasm runtime; IR for custom runtimes; Swift OPA; donated TypeScript/React/C#/Java SDKs now in the CNCF org (OPA-006, OPA-034, OPA-022). Post-transition maintenance of the donated SDKs is a watch item (inference from OPA-022/OPA-024).
- **Webhooks:** None inbound; OPA *pushes* decision-log and status events to configured HTTP services — webhook-like outbound reporting for ops/evidence, not a general event system (OPA-011, OPA-014).
- **Sandbox:** Rego Playground (play environment linked from homepage), local REPL, `opa eval`/`opa test` offline (OPA-003, OPA-017).
- **Rules engine / synchronous decisioning:** The product *is* a synchronous rules engine; decisions are computed per request in-process or over local HTTP (OPA-001, OPA-006).
- **Latency claims:** Official performance docs target API-authorization budgets "in the order of 1 millisecond," with rule indexing, early exit, and a near-constant-time "linear fragment"; profiling (`--profile`) and benchmarking (`opa bench`, p90/p99) built in (OPA-007). Adopter scale: Pinterest Kafka authorization ~400K QPS uncached / ~8.5M QPS cached (OPA-021).
- **Versioning:** Bundle manifests carry `revision` (git SHA/semver) and `rego_version`; OPA 1.0 (Dec 2024) stabilized Rego v1 with compatibility handling (OPA-009, OPA-029).
- **Idempotency:** Decision evaluation is read-only/side-effect-free, so retries are inherently safe; no idempotency-key machinery exists or is needed for queries; Policy/Data PUTs are last-write-wins configuration (OPA-016; inference).
- **Integration model:** You run OPA (sidecar/daemon/embedded); you build or source the server side: bundle storage (S3/GCS/Azure/OCI/git pipeline or OCP), log sink, dashboards (OPA-009, OPA-026). Memory constraint for replicated data: ~20x JSON expansion in memory (OPA-008).

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Yes — arbitrary JSON input and data; JSON-Schema type checking optional (OPA-005, OPA-004).
- **Store customer/user state?** Partially — data can be replicated in (bundles/push) and held in memory, but OPA cannot write state as a decision side effect; there are no counters, profiles, or per-user accumulators. State systems remain external (OPA-018, OPA-008, OPA-016; inference labeled).
- **Return reason codes?** Yes, if the author writes them — structured outputs (e.g., reason arrays) are first-class; `explain` traces exist for debugging. No standard reason-code vocabulary (OPA-005, OPA-016).
- **Output allow/deny/review?** Expressible as structured output; no built-in tri-state review/queue semantics (OPA-005; inference labeled).
- **Simulate policies?** Strong offline simulation: `opa test` with mocking (`with`), coverage, benchmarks; `opa eval` with `explain`. **Production-traffic what-if analysis (Live Impact Analysis) was an EOPA feature and is now archived/unmaintained** (OPA-017, OPA-016, OPA-025, OPA-024).
- **Replay decisions?** Ingredients recorded (decision_id, full input, result, bundle revision, timestamp) but no replay tool; reconstruction = re-evaluate the logged input against the archived bundle for that revision, all DIY (OPA-011, OPA-009; inference labeled).
- **Version policies?** Bundle `revision` metadata is stamped on every decision and status report; storage/history of versions lives in git/bundle servers, not OPA (OPA-009, OPA-011, OPA-014).
- **Deploy rules independently of app code?** Yes — this is OPA's core philosophy and mechanism: policies "updated at any time without recompiling or redeploying" via bundle distribution (OPA-019, OPA-009).

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance:** None. No sweepstakes/contest/AMOE/prize concepts anywhere in docs or ecosystem (OPA-001, OPA-030).
- **Generic regulatory workflow:** None built in. OPA's philosophy explicitly targets encoding compliance knowledge as policy (OPA-019), and Appsflyer demonstrably runs data-privacy/consent policy on OPA (OPA-021), but the workflow around it (drafting, review, sign-off, publication) happens in git and CI, outside OPA (OPA-026; inference labeled).
- **Jurisdiction restrictions:** Fully *encodeable* (packages/data keyed by jurisdiction; the pattern is idiomatic Rego) but zero jurisdictional content is provided (OPA-004; inference labeled).
- **Location verification:** None. OPA evaluates whatever geo attributes callers supply; it cannot determine or verify location (OPA-018; architectural absence).
- **Legal content/rules:** None shipped; ecosystem policy libraries are infrastructure-oriented (Kubernetes/Terraform), not legal (OPA-030).
- **Regulatory monitoring:** None — no content or monitoring services of any kind (OPA-001, OPA-030; enumerated absence).
- **Change management:** Primitives only — bundle revisions, signing, activation status/failure reporting per instance (OPA-009, OPA-010, OPA-014). No change-approval workflow.
- **Counsel approval:** Nothing resembling roles, approvals, or workflow exists in OPA; the community pattern is git PR review, which is generic engineering tooling (OPA-001, OPA-026; architectural absence, labeled inference).
- **Historical policy state:** Every decision is stamped with the bundle revision, so *which* version decided *what* is recoverable — provided the adopter archives bundles/git history and stores the logs (OPA-011, OPA-009; assembly required).
- **Notable near-miss:** Rego metadata annotations (`related_resources`, authors, custom fields) are a documented hook where legal citations could be attached to rules — a convention, not a provenance system (OPA-004; inference labeled).

## 7. Audit / evidence

Can a customer reconstruct, per decision:

- **Exact inputs?** Yes — decision-log events carry the full `input` (subject to configured masking and size/rate drop settings) (OPA-011, OPA-012, OPA-013).
- **Exact rule/policy?** Indirectly — events carry the queried `path` and `bundles{revision}`; resolving revision → policy text requires the adopter's archived bundles or git history (OPA-011, OPA-009; inference labeled).
- **Exact version?** Yes — `revision` per event; also available synchronously via the `provenance` query parameter (OPA-011, OPA-016).
- **Exact output?** Yes — `result` per event (OPA-011).
- **Exact timestamp?** Yes — RFC3339 timestamp, plus W3C trace/span IDs and OTel spans carrying `opa.decision_id` (OPA-011, OPA-020).
- **Human approvals?** No — no approval concept exists; approval history would live in git/CI systems outside OPA (architectural absence; inference).
- **Source/legal authority?** No — unless the adopter builds a convention on metadata annotations (OPA-004; inference).

**Assessment (labeled inference):** OPA emits the best raw decision-evidence stream of any general-purpose OSS policy engine — but it is a *stream*, not a system of record. Storage, retention, immutability/tamper-evidence of logs, query/replay tooling, and regulator-ready packaging are all the adopter's engineering problem. Events can be dropped by configuration under load (`max_decisions_per_second`), which an evidence-grade system would have to prevent (OPA-013). Bundle signing protects policy *distribution* integrity, not log integrity (OPA-010).

## 8. Enterprise readiness

- **SSO/RBAC:** None in the product — OPA is headless with no user accounts. Its own APIs are protected by TLS, bearer-token or client-cert authentication, and (dogfooding) a Rego `system.authz` policy that can restrict which identities may update policies vs query decisions (OPA-033). Management-plane RBAC/SSO was Styra DAS's job and is now gone (OPA-023).
- **Multitenancy / multi-brand:** Achievable via package namespacing, multiple bundles with disjoint `roots`, and per-instance discovery configuration; no tenant management layer (OPA-004, OPA-009, OPA-015; inference labeled).
- **Environments:** No built-in concept; assembled via per-environment bundle sources/discovery labels, or OCP's git-based environment promotion (OPA-015, OPA-026).
- **Security certifications:** Not applicable as SaaS. Project-level assurance: Cure53 security audit, public disclosure process, signed releases culture, CNCF graduation (OPA-032, OPA-002). Adopters must certify their own deployments (inference).
- **SLA / support:** No vendor SLA. Support page lists two small third-party consultancies with an explicit "not vetted" disclaimer (OPA-031). Styra's enterprise support is no longer available (OPA-023, OPA-036).
- **Professional services:** None first-party; ecosystem consultancies exist (OPA-031).
- **Customer scale examples:** Goldman Sachs, Netflix, Intuit (~50 clusters), Pinterest (400K–8.5M QPS), T-Mobile, BNY Mellon, Capital One, State Street, Atlassian, Appsflyer, Cloudflare (OPA-021).

## 9. Commercial model

- **Pricing:** Free (Apache-2.0). Fully transparent in the trivial sense; there is currently **no first-party commercial tier at all** — Styra's paid offerings (DAS, EOPA support) are discontinued/wound down (OPA-002, OPA-023, OPA-024).
- **Likely buyer:** Platform/infrastructure engineering leadership (adoption decision, not procurement). Compliance/legal are downstream consumers at best (OPA-021; inference).
- **Implementation burden:** Meaningful. Engine adoption is easy; production operationalization requires building/assembling bundle pipelines, log storage/analytics, data replication, dashboards, and governance conventions. The external-data patterns doc makes clear the data-plumbing burden sits with the adopter (OPA-018, OPA-026; inference labeled).
- **Sales motion:** None — pure open-source self-serve; monthly releases; large community (OPA-028, OPA-002).
- **Evidence of large customers:** Extensive (OPA-021, OPA-002). Note these are overwhelmingly *infrastructure authorization* use cases, with Appsflyer's consent/privacy policy the closest analog to regulatory decisioning (OPA-021).

## 10. Strengths

- **Category-defining decision engine:** synchronous, sub-ms-to-low-ms evaluation, arbitrary structured decisions, proven at extreme scale in regulated enterprises (OPA-007, OPA-021, OPA-005).
- **Policy-as-code lifecycle primitives that most vendors still lack:** versioned + signed bundles, per-decision logs binding `decision_id` + input + result + policy revision, status/rollout health, fleet discovery (OPA-009, OPA-010, OPA-011, OPA-014, OPA-015).
- **Best-in-class policy testing/tooling:** `opa test` with mocking/coverage/benchmarks, profiler, Regal linter/LSP/debugger, Playground (OPA-017, OPA-027, OPA-003).
- **Deployment flexibility:** sidecar, embedded Go, Wasm, IR, Swift; language-agnostic (OPA-006, OPA-034).
- **Neutral, durable governance:** CNCF-graduated, Apache-2.0, 450+ contributors, active monthly releases even after the maintainer transition (OPA-002, OPA-029, OPA-028).
- **Observability:** Prometheus by default, OpenTelemetry spans carrying decision IDs (OPA-020).

## 11. Weaknesses / constraints

- **No product above the engine.** Authoring UI, approvals, review states, RBAC/SSO, evidence storage, impact analysis, content — all absent by design (OPA-001, OPA-033; architectural, labeled inference where noted).
- **Commercial control-plane vacuum (2025–2026).** Styra DAS winding down with the company's web presence offline; EOPA archived and unmaintained (its data-filtering, SQL/Kafka datasources, and Live Impact Analysis now orphaned code); OCP is early (65 stars) and headless (OPA-023, OPA-024, OPA-025, OPA-026). Enterprises wanting managed OPA governance must now build it or leave the OPA ecosystem (inference).
- **State and data limits.** Policies cannot write state; replicated data is memory-bound (~20x JSON expansion); fresh per-decision data needs `http.send` with network availability risk (OPA-016, OPA-008, OPA-018).
- **Evidence stream, not evidence system.** Logs can be dropped by config under load; no retention, integrity, or packaging features (OPA-013, OPA-010; inference).
- **Rego skill curve and lock-in.** A bespoke language with real learning cost; once policies span many services, migration cost is significant (inference; supported by ecosystem tooling investment OPA-027 and DAS-migration disruption OPA-023, OPA-036).
- **Key-person/agenda risk flagged by community** after the Apple acqui-hire, partially mitigated by CNCF governance and continued releases (OPA-022, OPA-028, OPA-036; third-party commentary).

## 12. Capability matrix scores

Scores reflect **vanilla OPA out of the box** (engine + management APIs + first-party CLI tooling). Ecosystem/commercial adjuncts are noted but not scored in.

```csv
square,score,claim_ids
A01,0,OPA-001;OPA-030
A02,0,OPA-001;OPA-030
A03,0,OPA-001;OPA-030
A04,0,OPA-001;OPA-030
A05,0,OPA-001;OPA-030
A06,0,OPA-001;OPA-030
A07,0,OPA-001;OPA-030
A08,0,OPA-001;OPA-030
A09,0,OPA-001;OPA-030
A10,0,OPA-001;OPA-030
B01,4,OPA-016;OPA-001;OPA-021
B02,4,OPA-016;OPA-006
B03,4,OPA-007;OPA-006;OPA-021
B04,3,OPA-005;OPA-016
B05,3,OPA-005;OPA-016;OPA-003
B06,4,OPA-005;OPA-004;OPA-018
B07,2,OPA-018;OPA-008;OPA-016
B08,2,OPA-004;OPA-009
B09,3,OPA-017;OPA-016;OPA-025
B10,2,OPA-011;OPA-016
C01,2,OPA-004;OPA-021;OPA-019
C02,2,OPA-004;OPA-005
C03,2,OPA-004;OPA-021
C04,2,OPA-004;OPA-009
C05,2,OPA-009;OPA-011
C06,0,OPA-001;OPA-030
C07,1,OPA-017;OPA-025;OPA-024
C08,0,OPA-001;OPA-031
C09,2,OPA-004
C10,0,OPA-030
D01,3,OPA-011;OPA-016
D02,4,OPA-011;OPA-012;OPA-013
D03,3,OPA-011;OPA-016
D04,3,OPA-011;OPA-013
D05,0,OPA-001;OPA-026
D06,2,OPA-011;OPA-009
D07,1,OPA-011;OPA-013
D08,1,OPA-013
D09,1,OPA-010;OPA-011
D10,1,OPA-014;OPA-020
E01,0,OPA-001;OPA-018
E02,0,OPA-001;OPA-018
E03,0,OPA-001;OPA-018
E04,0,OPA-001;OPA-018
E05,0,OPA-001;OPA-018
E06,0,OPA-001;OPA-018
E07,0,OPA-003;OPA-018
E08,0,OPA-001;OPA-018
E09,0,OPA-001;OPA-030
E10,1,OPA-018;OPA-004
F01,0,OPA-001;OPA-016
F02,0,OPA-001;OPA-016
F03,0,OPA-001;OPA-016
F04,0,OPA-001;OPA-016
F05,0,OPA-001;OPA-016
F06,0,OPA-001;OPA-016
F07,1,OPA-005;OPA-018
F08,0,OPA-001;OPA-016
F09,0,OPA-001;OPA-016
F10,1,OPA-018
G01,2,OPA-004;OPA-009;OPA-015
G02,1,OPA-033
G03,0,OPA-033
G04,0,OPA-001;OPA-026
G05,2,OPA-015;OPA-026;OPA-009
G06,4,OPA-017;OPA-027
G07,2,OPA-009;OPA-014;OPA-010
G08,2,OPA-014;OPA-011
G09,0,OPA-031;OPA-022
G10,1,OPA-032;OPA-010
H01,4,OPA-016
H02,3,OPA-006;OPA-034;OPA-022;OPA-030
H03,2,OPA-014;OPA-011
H04,3,OPA-003;OPA-017
H05,3,OPA-016;OPA-029;OPA-009
H06,2,OPA-016
H07,1,OPA-013
H08,4,OPA-020;OPA-014;OPA-011
H09,3,OPA-016;OPA-009
H10,3,OPA-009;OPA-026;OPA-030
I01,1,OPA-021
I02,4,OPA-001;OPA-021
I03,0,OPA-001;OPA-030
I04,1,OPA-003
I05,4,OPA-021;OPA-002
I06,4,OPA-002;OPA-028;OPA-003
I07,2,OPA-031
I08,3,OPA-023;OPA-004
I09,2,OPA-018;OPA-026;OPA-030
I10,4,OPA-002;OPA-032
J01,2,OPA-019;OPA-021;OPA-004
J02,1,OPA-026;OPA-009
J03,0,OPA-001;OPA-031
J04,1,OPA-017;OPA-025;OPA-024
J05,3,OPA-021;OPA-007;OPA-001
J06,1,OPA-018
J07,2,OPA-011;OPA-010;OPA-012
J08,2,OPA-011;OPA-009
J09,1,OPA-030
J10,2,OPA-009;OPA-014;OPA-015;OPA-026;OPA-023
```

**Scoring notes (0/1/2 rationale and inference labels):**

- **A01–A10 = 0 (reasoned absence, not "unmentioned"):** OPA is a domain-agnostic decision engine with no promotion/campaign/entry/prize/tax objects. The docs enumerate its use cases (authorization, admission control, CI/CD) and the official ecosystem catalog enumerates integrations; nothing promotion-related exists in either (OPA-001, OPA-030). Inference from architecture, labeled as such.
- **B04/B05 = 3 not 4:** allow/deny/review and reason codes are fully expressible as structured decisions (official docs), but there is no opinionated tri-state model, review-queue semantics, or standard reason vocabulary — that layer is authored per deployment.
- **B07 = 2:** data can be replicated in and evaluated, but OPA cannot mutate state per decision; no per-user accumulators; memory-bound (~20x). Stateful context systems remain external.
- **B08 = 2:** `default`/`else` and bundle `roots` provide intra-policy ordering and ownership; there is no cross-policy priority/conflict-resolution framework; conflicting complete rules error at evaluation (inference from language docs).
- **B10 = 2:** all replay ingredients are logged (input, result, revision); no replay tool ships — reconstruction is a documented-primitives DIY exercise (inference).
- **C01–C05/C09 = 2:** these are "meaningful but incomplete" because the *mechanism* is genuinely strong (jurisdiction-keyed packages/data, time built-ins, revision stamping, metadata annotations for source references) while the *content and semantics* are 100% adopter-supplied. Labeled inference: scores reflect encodability demonstrated by official language docs plus Appsflyer's regulatory-policy production use.
- **C04 = 2:** temporal logic via `time.*` built-ins is authored in policy; there is no first-class effective-dating or scheduled activation of policy versions — bundles activate on download.
- **C06/C08/C10 = 0 (reasoned absence):** no content services, no workflow/approval constructs, no legal policy libraries anywhere in docs or the enumerated ecosystem (OPA-001, OPA-030, OPA-031). Inference labeled.
- **C07/J04 = 1:** offline tests/coverage only in OPA proper; traffic-based Live Impact Analysis existed only in EOPA, which is archived and unmaintained (OPA-025, OPA-024).
- **D05 = 0:** no approval concept exists to record (architectural absence; approvals live in git/CI outside OPA).
- **D07/D08/D09/D10 = 1:** raw log shipping exists but packaging, retention, log integrity, and audit UX are absent; bundle signing covers distribution only; events droppable by config (OPA-013, OPA-010).
- **E01–E09 = 0 (reasoned absence):** OPA consumes identity/geo/risk attributes as caller-supplied input; it performs no verification, detection, or scoring and has no case tooling (OPA-018, OPA-001). The homepage's risk example evaluates *provided* scores (OPA-003). E10 = 1 for the generic `http.send` pull-during-evaluation pattern — a peripheral orchestration path, not a connector framework.
- **F01–F09 = 0, F07/F10 = 1:** policies are side-effect-free; no wallet/ledger constructs exist (OPA-001, OPA-016). F07 = 1 because eligibility *rules* over supplied balance data are exactly what OPA evaluates; F10 = 1 via generic `http.send`/data replication. Inference labeled.
- **G02 = 1 / G03 = 0:** OPA's own API access control is policy-based (`system.authz`) with token/cert identities — real but minimal; there are no user accounts for SSO/SAML to attach to (OPA-033; architectural absence).
- **G04 = 0:** no approval workflow anywhere in OPA; OCP's model is git workflows, i.e., approvals live in GitHub/GitLab, not the product (OPA-026).
- **G09 = 0:** no vendor SLA exists; support page disclaims vetting of the two listed consultancies; the former commercial vendor exited (OPA-031, OPA-022).
- **G10 = 1:** project-level security posture (Cure53 audit, disclosure process) but no service attestations (SOC 2 inapplicable to self-hosted software); compliance burden transfers to the adopter.
- **H06 = 2:** evaluations are inherently idempotent (read-only); no idempotency-key mechanism documented (inference).
- **H07 = 1:** self-hosted, so no platform rate limits; only decision-log `max_decisions_per_second` is configurable.
- **I01/I03/I04:** engineering-led adoption; legal/marketing/fraud teams are not buyers of OPA (I03 = 0 reasoned absence; I01/I04 = 1 as beneficiaries at most). Inference labeled.
- **I07 = 2 (interpretation note):** scored as "degree of services/engineering dependence": no first-party PS exists, but production operationalization requires substantial internal engineering or third-party consultants (OPA-031; inference).
- **I08 = 3 (labeled inference):** Rego lock-in across many embedded enforcement points plus the demonstrated pain of DAS-dependent customers forced to migrate (OPA-023) indicate high switching costs.
- **I09 = 2 (interpretation note):** rich integration surface, but assembling the full platform (control plane, log storage, data replication) is the adopter's burden.
- **J02 = 1:** git-to-bundle deployment rails exist (OCP/bundles) but nothing legal-specific — no counsel roles, no legal review states.
- **J05 = 3 not 4:** cross-product action authorization is OPA's proven core use (central authz for hundreds of services at Netflix/Atlassian/Appsflyer), but the *regulated-action* semantic layer (action catalogs, review outcomes, obligations) must be designed per adopter.
- **J09 = 1:** community policy libraries exist for infrastructure (Gatekeeper/Terraform); none for legal/regulatory domains (OPA-030).
- **J10 = 2:** agent-side control-plane primitives (bundles/status/discovery/logs) are excellent; the governance side is OCP-early or gone-with-DAS (OPA-026, OPA-023).
- **No `?` scores:** OPA is fully open source with complete public documentation; every square was resolvable to positive evidence or reasoned architectural absence.

## 13. White-space implications

1. **Already solved by OPA (adopt, don't rebuild):** J05's engine layer — real-time, low-latency, cross-product decision evaluation with structured outputs (B01–B06); policy-independent-of-code deployment with versioned, signed distribution (partial J02 rails); decision telemetry binding decision → input → result → policy revision (the raw substrate of J07/J08); policy unit testing/coverage (base of J04); fleet management primitives (part of J10) (OPA-005–OPA-017).
2. **Partially solved:** historical version linkage (C05/D03 — revision stamping exists; archives are DIY); reconstruction/replay (D06/B10/J08 — ingredients logged, no tooling); jurisdiction/temporal rule *mechanics* (C01–C04 — encodable, no content); provenance annotation hooks (C09); environments/change management (G05/G07 via git + status); control plane (J10 — OCP is early, headless).
3. **Unsolved (in OPA and its current ecosystem):** regulatory content and its maintenance (C06, C10, J09 for legal domains); counsel-facing authoring/approval workflow (C08, J03, D05, G04); pre-rollout impact analysis as a product (C07/J04 — LIA is orphaned in archived EOPA); evidence-grade log storage, integrity, retention, and regulator packaging (D07–D10, J07); identity/geo/fraud signal generation and cross-vendor normalization (E01–E10, J06); all promotion administration (A) and ledger/entitlement state (F); any legal/compliance buyer motion (I01).
4. **Could this "vendor" add the missing capability easily?** There is no vendor. The community *could* — and the code proximity is real (EOPA's LIA and data features exist as archived code; OCP could grow approvals) — but the entities that monetized this exact roadmap (Styra) exited, and Apple hired the team for internal purposes (OPA-022–OPA-026). A community-built counsel-workflow/regulatory-content product is implausible as OSS because content requires licensed legal maintenance (inference). Risk of OPA itself absorbing the domain layer: low.
5. **Could a customer assemble it with OPA + internal engineering?** The decision engine, distribution, and telemetry layers — yes, demonstrably (Appsflyer's consent policies; BNY Mellon's context-aware authz; Atlassian's S3-distributed policies). The full Promotion OS scope — only partially: an enterprise would still need to source/maintain jurisdictional legal content, build counsel workflow and evidence systems, integrate signal vendors, and now also self-operate the control plane Styra used to sell. That is a multi-team, multi-year platform program, realistic only for top-decile engineering organizations (inference from OPA-018, OPA-023, OPA-026).
6. **What would make a customer buy a separate product instead?** (a) Maintained regulatory/jurisdictional content with legal provenance — never available in the OPA ecosystem; (b) counsel-grade workflow and attestation, which git PRs don't provide for non-engineers; (c) evidence-grade retention/integrity/packaging out of the box; (d) accountability: a vendor with SLAs and (ideally) shared regulatory posture — precisely what the OPA world lost in 2025–2026 (OPA-023, OPA-031); (e) traffic-based impact analysis as a supported feature; (f) signal-vendor integrations. Notably, a Promotion OS could *embed* OPA/Rego as its engine rather than compete with it (inference).

## 14. Replacement risk

**MEDIUM.**

OPA will not productize the Promotion OS scope itself: it is a community-governed engine, its philosophy deliberately stops at general-purpose decisioning, and the commercial actors who were closest to the control-plane/governance layer (Styra) have exited while EOPA sits archived (OPA-019, OPA-022–OPA-026). No entity currently exists with both the incentive and the asset base to extend OPA into regulatory content, counsel workflow, and evidence products.

The risk is nonetheless MEDIUM, not LOW, because OPA is the strongest *substitute-by-assembly* in the study: a sophisticated enterprise's platform team can stand up the engine, versioned distribution, decision logging, and testing for free, then argue the remaining gap is "just" content and workflow. Regulated-industry adopters (Goldman Sachs, Capital One, BNY Mellon, State Street, Appsflyer) already run OPA in production, so the "build on OPA" option is on every platform architect's whiteboard (OPA-021). A Promotion OS pitch must beat internal-build-on-OPA on content, counsel workflow, evidence packaging, and accountability — not on decisioning mechanics.

## 15. Adjacent discoveries

Companies/substitutes encountered that should be considered (beyond the existing 15-company set):

1. **Oso (osohq.com)** — commercial application-authorization vendor (Polar language; RBAC/ReBAC/ABAC models) actively marketing itself as the commercially supported alternative amid the Styra wind-down; represents the "authorization-as-a-service with a vendor behind it" substitute (OPA-036).
2. **OpenFGA (openfga.dev)** — CNCF-incubating, Zanzibar-style relationship-based access control with millisecond checks; the stateful-graph alternative to OPA's stateless rule evaluation for entitlement-like decisions (OPA-035).
3. **Aserto / Topaz** — commercial authorization control plane and its OSS engine, listed in OPA's own ecosystem as OPA-adjacent management tooling (OPA-030).
4. **OPAL (Open Policy Administration Layer)** — OSS real-time policy/data update layer for OPA fleets (maintained by Permit.io, already company #15); relevant as the de-facto OSS answer to live policy/data sync (OPA-030).
5. **HashiCorp Sentinel** — proprietary embedded policy-as-code framework inside the Terraform/Vault ecosystem; the main non-OPA policy-as-code incumbent for IaC governance (knowledge-based identification; flagged for manager verification — no ledger record).
6. Also noted: **OPA Gatekeeper / Kyverno** (Kubernetes-native policy, shows how domain-specific packaging wins over raw engines) and **Mondoo** (positioning against Styra-era OPA for infra compliance) (OPA-030; search-encountered).

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/12_opa.jsonl` (36 records).

| Claim ID | Claim (abbreviated) | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| OPA-001 | General-purpose policy engine; decouples decision from enforcement; JSON in → decision out | https://www.openpolicyagent.org/docs | official-doc | 2026-08-18 | HIGH |
| OPA-002 | CNCF graduated 2021-02-04; 150+ org survey; GS/Netflix/Pinterest/T-Mobile production | https://www.cncf.io/announcements/2021/02/04/cloud-native-computing-foundation-announces-open-policy-agent-graduation/ | official-marketing | 2026-08-18 | HIGH |
| OPA-003 | Homepage positioning incl. audit capability; risk-score example; adopter logos; Playground | https://www.openpolicyagent.org/ | official-marketing | 2026-08-18 | HIGH |
| OPA-004 | Rego language: rules, comprehensions, time/JWT/http.send built-ins, schemas, metadata annotations incl. related_resources | https://www.openpolicyagent.org/docs/policy-language | official-doc | 2026-08-18 | HIGH |
| OPA-005 | Decisions are arbitrary structured outputs, not just yes/no | https://www.openpolicyagent.org/docs | official-doc | 2026-08-18 | HIGH |
| OPA-006 | Integration modes: REST/sidecar, Go SDK, Wasm, IR; local eval for speed/HA | https://www.openpolicyagent.org/docs/integration | official-doc | 2026-08-18 | HIGH |
| OPA-007 | ~1ms decision budgets; linear fragment; indexing; profiling; opa bench p90/p99 | https://www.openpolicyagent.org/docs/policy-performance | official-doc | 2026-08-18 | HIGH |
| OPA-008 | In-memory data ~20x JSON size; 100k rules ~1.1GB; GOMEMLIMIT guidance | https://www.openpolicyagent.org/docs/policy-performance | official-doc | 2026-08-18 | HIGH |
| OPA-009 | Bundles: ETag polling, manifest revision/roots/rego_version, persistence, S3/GCS/Azure/OCI | https://www.openpolicyagent.org/docs/management-bundles | official-doc | 2026-08-18 | HIGH |
| OPA-010 | Bundle signing (JWT over file hashes) verified before activation; delta bundles unsigned | https://www.openpolicyagent.org/docs/management-bundles | official-doc | 2026-08-18 | HIGH |
| OPA-011 | Decision log event fields: decision_id, input, result, path, bundles.revision, timestamp, metrics, trace IDs | https://www.openpolicyagent.org/docs/management-decision-logs | official-doc | 2026-08-18 | HIGH |
| OPA-012 | Policy-driven masking (erase/upsert) of decision-log fields | https://www.openpolicyagent.org/docs/management-decision-logs | official-doc | 2026-08-18 | HIGH |
| OPA-013 | Log buffering/size limits; max_decisions_per_second drops events; retention is sink's job | https://www.openpolicyagent.org/docs/management-decision-logs | official-doc | 2026-08-18 | HIGH |
| OPA-014 | Status API: per-bundle revision, activation errors, plugin state, metrics to remote endpoint | https://www.openpolicyagent.org/docs/management-status | official-doc | 2026-08-18 | HIGH |
| OPA-015 | Discovery bundles centrally generate per-instance config (bundles, logs, status) | https://www.openpolicyagent.org/docs/management-discovery | official-doc | 2026-08-18 | HIGH |
| OPA-016 | REST API: Data/Policy/Query/Compile APIs; decision_id, provenance, explain; health; token auth | https://www.openpolicyagent.org/docs/rest-api | official-doc | 2026-08-18 | HIGH |
| OPA-017 | opa test: mocks (with), coverage, bench, data-driven tests, CI flags | https://www.openpolicyagent.org/docs/policy-testing | official-doc | 2026-08-18 | HIGH |
| OPA-018 | Five external-data patterns and tradeoffs (JWT, input, bundle, push, http.send) | https://www.openpolicyagent.org/docs/external-data | official-doc | 2026-08-18 | HIGH |
| OPA-019 | Philosophy: manage/version/distribute policy separate from services; compliance consistency | https://www.openpolicyagent.org/docs/philosophy | official-doc | 2026-08-18 | HIGH |
| OPA-020 | Prometheus /metrics default; OTel spans with opa.decision_id; health APIs | https://www.openpolicyagent.org/docs/monitoring | official-doc | 2026-08-18 | HIGH |
| OPA-021 | Adopters: GS, Netflix, Intuit, Pinterest (400K–8.5M QPS), BNY Mellon, Capital One, State Street, Atlassian, Appsflyer (privacy/consent policy) | https://github.com/open-policy-agent/opa/blob/main/ADOPTERS.md | official-doc | 2026-08-18 | HIGH |
| OPA-022 | 2025-08-20: creators + Styra engineers join Apple; governance/licensing unchanged; EOPA/OCP/Regal/SDKs to CNCF org | https://www.openpolicyagent.org/blog/note-from-teemu-tim-and-torin-to-the-open-policy-agent-community-2dbbfe494371 | official-doc | 2026-08-18 | HIGH |
| OPA-023 | Styra wound down; DAS access expected to end within ~12 months of Aug-2025; styra.com/docs.styra.com offline on access date | https://paclabs.substack.com/p/opa-announcement-and-consequences | third-party | 2026-08-18 | MEDIUM |
| OPA-024 | EOPA (data-heavy OPA, data filtering, SQL/DynamoDB/Neo4j) donated then archived 2026-06-26; seeking maintainers | https://github.com/open-policy-agent/eopa | official-doc | 2026-08-18 | HIGH |
| OPA-025 | EOPA Live Impact Analysis: compare new vs deployed policy on sampled live traffic pre-deployment | https://docs.styra.com/enterprise-opa/tutorials/testing/live-impact-analysis | official-doc | 2026-08-18 | MEDIUM |
| OPA-026 | OPA Control Plane: multi-git bundle builds, env promotion via git, cloud-storage distribution; early maturity | https://github.com/open-policy-agent/opa-control-plane | official-doc | 2026-08-18 | HIGH |
| OPA-027 | Regal: Rego linter/LSP/debugger; custom org rules; Atlassian/Boeing/Miro users | https://github.com/open-policy-agent/regal | official-doc | 2026-08-18 | HIGH |
| OPA-028 | Active releases: v1.19.1 (2026-08-17), v1.19.0, v1.18.2; ~monthly cadence | https://github.com/open-policy-agent/opa/releases | official-doc | 2026-08-18 | HIGH |
| OPA-029 | OPA 1.0 (2024-12-20); Rego v1; 450+ contributors | https://www.openpolicyagent.org/blog/announcing-opa-1-0-a-new-standard-for-policy-as-code-a6d8427ee828 | official-doc | 2026-08-18 | HIGH |
| OPA-030 | Ecosystem catalog: control planes (Styra, Permit.io, Aserto, Topaz, OPAL), Envoy/Spring/Kafka, Gatekeeper, Terraform; no legal/regulatory entries | https://www.openpolicyagent.org/ecosystem | official-doc | 2026-08-18 | HIGH |
| OPA-031 | Support page: two unvetted third-party consultancies; no project SLA | https://www.openpolicyagent.org/support | official-doc | 2026-08-18 | HIGH |
| OPA-032 | Cure53 security audit; disclosure process; 12.1k stars; Apache-2.0 | https://github.com/open-policy-agent/opa | official-doc | 2026-08-18 | HIGH |
| OPA-033 | OPA API security: TLS, token/cert authn, system.authz Rego authorization of own APIs | https://www.openpolicyagent.org/docs/security | official-doc | 2026-08-18 | HIGH |
| OPA-034 | Swift OPA: native in-process evaluation via IR (2025-05-14) | https://www.openpolicyagent.org/blog/introducing-swift-opa-native-policy-evaluation-for-swift-d5136c8a662e | official-doc | 2026-08-18 | HIGH |
| OPA-035 | OpenFGA: CNCF-incubating Zanzibar-style ReBAC; adjacent substitute | https://openfga.dev/ | official-marketing | 2026-08-18 | HIGH |
| OPA-036 | Oso analysis: acqui-hire; DAS no longer actively developed; Oso positions as commercial alternative | https://www.osohq.com/post/opa-maintainers-join-apple-oss-community-to-maintain-styra-products | third-party | 2026-08-18 | MEDIUM |

## 17. Verdict

**COMPLEMENT** (with substitute-by-assembly risk).

OPA is not a competitor to a Promotion OS — it is the strongest available *foundation* for one. It category-leads exactly the squares Promotion OS should not rebuild: sub-millisecond synchronous decisioning, arbitrary structured allow/deny outputs, versioned/signed policy distribution, per-decision evidence events linking input, result and policy revision, and best-in-class policy testing. It provides none of the proposed differentiators as products: no regulatory content, no counsel workflow, no impact analysis (orphaned in archived EOPA), no evidence packaging/retention, no signal normalization, no compliance buyer motion. The 2025–2026 Styra collapse removed the only mature commercial governance layer, leaving enterprises to self-assemble control planes — which strengthens the case for a domain product built *on* OPA/Rego while proving that engine-layer monetization alone failed as a business. Main residual threat: sophisticated platform teams using free OPA as the internal-build substrate.

(~140 words)
