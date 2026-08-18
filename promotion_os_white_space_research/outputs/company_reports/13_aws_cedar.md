# Company Report — AWS Verified Permissions / Cedar

Researcher: Research Agent 13 (AWS Verified Permissions / Cedar)
Date: 2026-08-18
Category: Generic policy infrastructure
Manager: Manager D

## 1. Executive summary

**What the product actually is.** Amazon Verified Permissions (AVP) is a fully managed, regional AWS service (GA June 13, 2023) that answers one question for a customer's own application: *"is this principal allowed to perform this action on this resource, in this context?"* Applications call `IsAuthorized` / `IsAuthorizedWithToken` / `BatchIsAuthorized` and receive a binary `ALLOW | DENY` decision plus the IDs of the policies that determined it [AWSCEDAR-001, -002]. Policies are written in **Cedar**, an AWS-created, Apache-2.0, formally verified policy language that became a CNCF Sandbox project on October 8, 2025 [AWSCEDAR-030, -031, -032]. AVP is the managed "policy store + decision endpoint" for Cedar; the language itself can be run self-hosted for free.

**Who buys it.** Engineering/platform teams (and secondarily security/audit teams) who would otherwise hand-roll authorization inside application code. Named customers include TELUS, Twilio (Flex), Stedi (700M requests/month), FIS, and Grosvenor Engineering [AWSCEDAR-020, -043]. It is bought self-serve, pay-per-request ($5/million single authorization requests after a 97% price cut in June 2025), with no minimums [AWSCEDAR-014, -015].

**What job it is hired to do.** Externalize *application permissions* (RBAC/ABAC: "can Alice edit this photo?", "can this agent in this Twilio Flex role see this queue?") from code into centrally managed, auditable, testable policy. It is **authorization infrastructure, not a compliance product**: it ships zero regulatory content, no jurisdiction awareness, no approval workflow, no decision-log store of record, no policy version history, and it "presumes that the principal has been previously identified and authenticated through other means" [AWSCEDAR-001, -022, -023, -024]. The core question for this study — can enterprise teams use managed authorization + Cedar for the regulatory action-authorization use case — is answered in Sections 5, 6, 13: the *decision engine* layer, yes, with real strengths (deterministic forbid-overrides-permit semantics, formal verification, SMT-based policy diffing); the *regulatory lifecycle* layers, no — everything above the engine must be built by the customer.

## 2. Product architecture

Core entities (all official-doc):

- **Policy store** — regional container for everything; one per application or per tenant is the recommended pattern; 30,000 per Region per account; aliases, tags, deletion protection [AWSCEDAR-021, -011, -026].
- **Schema** — optional-but-recommended declaration of entity types, attributes, and actions; with validation mode `Strict`, any policy that does not type-check against the schema is rejected at write time [AWSCEDAR-009].
- **Policies** — Cedar `permit`/`forbid` statements with scope constraints (`==`, `in`, `is`) and `when`/`unless` conditions over principal/resource attributes, hierarchies, and request context [AWSCEDAR-007]. Max 10,000 bytes each [AWSCEDAR-011].
- **Policy templates** — policies with `?principal`/`?resource` placeholders; instantiated as template-linked policies; editing the template updates every linked policy at once [AWSCEDAR-008].
- **Identity source** — optional link (1 per store) to a Cognito user pool or an OIDC IdP (Okta, Ping, CyberArk named) so JWTs can be evaluated directly [AWSCEDAR-029].

Concrete workflow:

```
INPUT                          DECISION/PROCESS                        OUTPUT
─────                          ────────────────                        ──────
principal + action + resource  Cedar evaluation over all policies      decision: ALLOW | DENY
+ context (free-form record)   in the policy store:                    + determiningPolicies[policyId]
+ entities (attributes,        - default deny                          + evaluation errors[]
  parent hierarchies), or      - any satisfied forbid overrides        (HTTP 200, signed AWS API)
  a Cognito/OIDC JWT             any satisfied permit
                               - policies that error are skipped
```

[AWSCEDAR-002, -003, -005, -006]

Critical architectural properties for this study:

1. **The caller supplies all facts.** "Additional context, entities, and attributes are not retrieved by default with this service" — AVP fetches nothing from anywhere; there are no data connectors [AWSCEDAR-022]. Every geolocation, KYC, or fraud signal must be resolved by the application *before* the call.
2. **Policies mutate in place.** `UpdatePolicy` replaces the statement; only `createdDate`/`lastUpdatedDate` survive; AWS's own guidance tells customers to track policy versions in their CI/CD because "application logic doesn't inherently perform this functionality" [AWSCEDAR-022, -023].
3. **Decision logging is opt-in plumbing, not a product.** Management events are CloudTrail-logged by default; the authorization calls themselves are CloudTrail **data events** "not logged by default", and the documented log entries carry principal/action/resource + decision but not determining policy IDs, context, or entity attributes [AWSCEDAR-012, -013].
4. **Eventual consistency** on policy changes (a few seconds to propagate) [AWSCEDAR-023].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| AVP policy store + authorization APIs (`IsAuthorized`, `IsAuthorizedWithToken`, `BatchIsAuthorized`/`WithToken`) | Managed Cedar evaluation returning ALLOW/DENY + determining policy IDs | Engineering/platform | Core | AWSCEDAR-002, -004, -005 |
| Schema + policy validation (Strict mode) | Type-checks every policy write against the declared authorization model | Engineering | Core | AWSCEDAR-009 |
| Policy templates / template-linked policies | Parameterized reuse; template edits propagate to all linked policies | Engineering | Core | AWSCEDAR-008 |
| Test bench (console) | Simulates authorization requests; shows decision + satisfied policies/errors | Engineering | Core (console) | AWSCEDAR-010 |
| Identity sources (Cognito / OIDC) | Evaluates JWTs directly; principal attributes from token claims | Engineering | Core | AWSCEDAR-005, -029 |
| Integrations: API Gateway Lambda authorizer, AppSync, Express.js middleware, console wizards | Packaged enforcement points that call AVP | Engineering | Add-on convenience | AWSCEDAR-028 |
| CloudTrail / EventBridge / IaC (CloudFormation, Terraform, CDK) | Change audit, event plumbing, GitOps deployment | Platform/security | Platform inheritance | AWSCEDAR-012, -025, -037 |
| **Cedar (open source)** — language, Rust/Go/Java engines, validator, symbolic compiler (Cedar Analysis), Lean formal model | Self-hostable evaluation + formal policy analysis (equivalence/permissiveness diffing with counterexamples) | Engineering | Separate OSS project, Apache-2.0, CNCF Sandbox | AWSCEDAR-030, -031, -032, -033 |
| Cedar ecosystem: AWS Verified Access, Bedrock AgentCore Policy (incl. time-based rules, NL policy generation), cedar-for-k8s, Dogwood (temporal/sequence extension, Aug 2026) | Cedar as AWS's cross-product policy language | n/a | Adjacent AWS products | AWSCEDAR-034, -035 |

## 4. API / developer capability

- **APIs**: 34 operations total — 4 authorization (data plane) + CRUD for policies, templates, schema, policy stores, identity sources, aliases, tags, `BatchGetPolicy` [AWSCEDAR-024]. Signed AWS API (SigV4), wire version 2021-12-01.
- **SDKs**: 10+ languages (.NET, C++, Go, Java, JavaScript, Kotlin, PHP, Python, Ruby, Rust) + CLI/PowerShell + CDK L2 construct [AWSCEDAR-027].
- **Webhooks**: none. Events reach EventBridge only "via AWS CloudTrail" (best-effort API-call events); no service-native notifications [AWSCEDAR-037].
- **Sandbox**: no formal sandbox; a dev policy store costs nothing to create (no minimum fees) and the console test bench simulates requests [AWSCEDAR-010, -014].
- **Rules engine**: Cedar 4.7 (per user guide) — permit/forbid, hierarchies, ABAC conditions, extension types (decimal, ipaddr, datetime/duration) [AWSCEDAR-007, -034, -042].
- **Synchronous decisioning**: yes — the entire product is a synchronous decision API; batch = up to 30 decisions/call, metered as one billable request [AWSCEDAR-004, -014].
- **Latency claims**: "evaluate access requests in milliseconds" (Prescriptive Guidance/FAQ); Cedar designed for "bounded latency"; no published p99 SLOs. Stedi reports "low latencies" at 700M req/month using batching + client-side caching [AWSCEDAR-036, -020].
- **Throughput**: default 200 RPS per policy store for `IsAuthorized` (adjustable), 30 RPS batch — modest defaults sized for app authorization, raised via Service Quotas [AWSCEDAR-011].
- **Versioning**: stable AWS API version; Cedar language version upgraded by AWS (4.5 → 4.7 announcements). No *policy* versioning (see Section 5) [AWSCEDAR-042, -023].
- **Idempotency**: `ClientToken` on create operations (visible in documented request examples) [AWSCEDAR-012].
- **Integration model**: app-embedded PEP calling a regional endpoint; packaged enforcement for API Gateway (Lambda authorizer, 120s cached), AppSync, Express [AWSCEDAR-028]. All decision inputs pushed by caller; no callbacks, no data fetch [AWSCEDAR-022].

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Yes — schema-defined entity attributes, parent hierarchies, and a free-form context record; strings, longs, booleans, sets, records, entity references, decimal/ipaddr/datetime extension types [AWSCEDAR-003, -007, -034]. **Strong.**
- **Store customer/user state?** No — AVP stores policies and schema only. Principal attributes come from the JWT (identity source) or from caller-supplied entities per request; "additional context, entities, and attributes are not retrieved by default" [AWSCEDAR-005, -022]. **Stateless by design.**
- **Return reason codes?** Partially — `determiningPolicies` returns the policy IDs that decided the outcome, plus evaluation errors. No human-readable reason strings; an implicit deny returns an *empty* list (no "why not" explanation) [AWSCEDAR-002, -006].
- **Output allow/deny/review?** No review/escalate outcome — strictly `ALLOW | DENY` [AWSCEDAR-002]. A "review" disposition would have to be encoded by convention (e.g., a permit on a `review` action), i.e., built by the customer.
- **Simulate policies?** Console test bench simulates single requests pre-deployment [AWSCEDAR-010]; open-source Cedar Analysis proves how two policy sets differ (equivalent / more / less permissive, with counterexamples) [AWSCEDAR-033]. No production shadow mode, no traffic replay.
- **Replay decisions?** No. No decision store, no replay API [AWSCEDAR-024]. CloudTrail data events (opt-in) capture request PAR + decision, but not determining policies/context, and the policies themselves can be mutated in place afterward — so faithful historical re-evaluation requires the customer to have archived policy text and full inputs themselves [AWSCEDAR-012, -013, -023].
- **Version policies?** No native version history. `UpdatePolicy` overwrites; AWS explicitly tells customers to track versions via CI/CD [AWSCEDAR-022, -023].
- **Deploy rules independently of app code?** Yes — this is the core value proposition ("decouple your business logic from the authorization logic"); policies deploy via console/API/CloudFormation/Terraform/CDK without app releases, with ~seconds eventual consistency [AWSCEDAR-001, -025, -023].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance**: none. No promotion, sweepstakes, or marketing constructs anywhere in the product [AWSCEDAR-024, -043]. (Notably, AWS's *AgentCore* docs use a Cedar "Promotional period policy" example — allow refunds only during January 2025 — showing the language expresses such windows; the product supplies no promotional/legal semantics [AWSCEDAR-034].)
- **Generic regulatory workflow**: none. AVP is content-free infrastructure.
- **Jurisdiction restrictions**: expressible, not provided. A policy can say `forbid(...) when { context.state == "FL" }` if the application computes and passes the state — Cedar evaluates whatever attributes the caller defines [AWSCEDAR-003, -007]. AVP has no notion of jurisdictions, no jurisdiction data, no location resolution.
- **Location verification**: none; the ipaddr extension can test caller-supplied IPs against ranges, but AVP performs no geolocation [AWSCEDAR-001, -007] (inference from documented scope: authN/data collection out of scope).
- **Legal content/rules**: none shipped. Cedar annotations (`@id`, arbitrary `@key("value")`) could carry citation metadata by convention but "have no impact on policy evaluation" [AWSCEDAR-007].
- **Regulatory monitoring**: none [AWSCEDAR-024] (inference from full API/product enumeration).
- **Change management**: CloudTrail change audit ("who made changes and when"), Strict validation, deletion protection, IaC pipelines — but no staged rollout, no diff/preview in the service, no approvals [AWSCEDAR-040, -009, -026, -025].
- **Counsel approval**: nothing. Write access to policies is gated by AWS IAM permissions; any approval chain (e.g., a CodePipeline manual-approval stage in front of `CreatePolicy`) is customer-built [AWSCEDAR-024, -022].
- **Historical policy state**: not retained. In-place mutation; version tracking delegated to customer CI/CD; CloudTrail events do not show policy statement text in documented examples [AWSCEDAR-023, -022, -040].
- **Temporal/effective-date rules**: Cedar datetime/duration types support date-window and business-hours conditions — but only if the application passes the current time in context (no engine clock; "datetime conditions silently fail" if omitted — the AgentCore product solved this with a system-injected `context.system.now`, which AVP does not provide); no scheduled policy activation/expiration [AWSCEDAR-034, -024].

## 7. Audit / evidence

Can a customer reconstruct a past decision?

- **Exact inputs?** Partially, if they enabled CloudTrail data events (off by default, extra cost): principal/action/resource + policyStoreId are logged; context and entity attributes are not shown in documented log entries — the application must log its own full request payloads for completeness [AWSCEDAR-012, -013].
- **Exact rule/policy?** At decision time the API returns determining policy IDs [AWSCEDAR-002], but those IDs are *not* in the CloudTrail record [AWSCEDAR-013], and the policy body behind an ID can be silently rewritten later [AWSCEDAR-023]. So policy-at-decision-time reconstruction requires customer-side archival (git/IaC).
- **Exact version?** No policy versioning exists to reference [AWSCEDAR-022, -023].
- **Exact output?** Yes — decision is in `additionalEventData` of the data event [AWSCEDAR-012].
- **Exact timestamp?** Yes — `eventTime` per CloudTrail event [AWSCEDAR-012].
- **Human approvals?** Only "who called which management API when" (CloudTrail userIdentity); no approval records because no approval feature [AWSCEDAR-040, -024].
- **Source/legal authority?** Nothing; at best inert policy annotations by customer convention [AWSCEDAR-007].
- **Integrity/retention**: inherited from CloudTrail — SHA-256/RSA-signed digest chains make tampering detectable; retention is whatever the customer configures in S3/Glacier [AWSCEDAR-038].

Bottom line: AVP provides *audit-friendly plumbing* (attributed change log, opt-in decision events, tamper-evident trails) but not evidence-grade decision reconstruction. "Why was this allowed on March 3rd?" is answerable only if the customer built the logging, policy archival, and correlation layer themselves.

## 8. Enterprise readiness

- **SSO/RBAC**: administration is governed by AWS IAM (action-level permissions, e.g., `verifiedpermissions:IsAuthorized`, resource ARNs) and workforce SSO via IAM Identity Center — platform-inherited, mature [AWSCEDAR-004, -001]. End-user identity via Cognito/OIDC identity sources [AWSCEDAR-029].
- **Multitenancy / multi-brand**: documented SaaS pattern — policy store per tenant (30,000/Region), per-tenant custom roles, namespaces for disambiguation, cross-tenant guardrail policies [AWSCEDAR-021, -022, -011]. No tenant/brand management UI; the tenancy model is assembled by the customer.
- **Environments**: no first-class environments; separate policy stores/accounts per stage plus IaC promotion is the working pattern (inference from policy-store container model + IaC support) [AWSCEDAR-021, -025].
- **Security certifications**: SOC 1/2/3 in scope; HIPAA eligible (Oct 2024); available in GovCloud (US) and China Regions; 35 Regions total (Aug 2025) [AWSCEDAR-018, -017, -019].
- **SLA**: published; credits below 99.9% monthly uptime measured on the authorization APIs [AWSCEDAR-016].
- **Support / professional services**: standard AWS Support tiers and partner network; nothing AVP-specific observed (inference).
- **Customer scale examples**: Stedi 700M requests/month; Grosvenor 45,000 buildings; Twilio Flex; FIS Prophet (insurance, "compliance requirements"); TELUS smart home [AWSCEDAR-020].

## 9. Commercial model

- **Pricing (fully public)**: $0.000005 per single authorization request ($5/M, after the June 2025 ~97% cut); batch calls $0.00015 → $0.000075 → $0.00004 per *API call* by monthly tier, each call carrying up to 30 decisions ("metered as one request, irrespective of the number of authorizations"); policy management $0.00004/request; "no upfront or minimum fees" [AWSCEDAR-014, -015]. Effective cost of a batched decision can approach ~$5/M even at tier-1 batch pricing — decisioning is being priced as a commodity.
- **Likely buyer**: engineering/platform teams; security/audit as influencers [AWSCEDAR-043]. No legal, marketing, or fraud-ops motion.
- **Implementation burden**: real — the customer designs the schema, authors Cedar, instruments every enforcement point, and pushes all decision data per request; wizards (API Gateway/Cognito) and Express middleware reduce the first mile [AWSCEDAR-028, -022].
- **Sales motion**: pure AWS self-serve/consumption; lands inside existing AWS bills and enterprise agreements — zero procurement friction for AWS shops [AWSCEDAR-014].
- **Large customers**: yes (Section 8), though public case depth is thin [AWSCEDAR-020].

## 10. Strengths

1. **Formally verified decision core.** Cedar's semantics (default deny, forbid overrides permit) are modeled in Lean with machine-checked proofs and differentially tested against the production Rust engine — an assurance story no promotion/loyalty rules engine in this study can match, and directly relevant to regulated use [AWSCEDAR-006, -032].
2. **Analyzable policies.** Cedar Analysis (SMT/cvc5, proven sound and complete) can *prove* whether a policy change makes the system more permissive, with counterexamples — the logical half of "impact analysis before rollout" already exists as OSS [AWSCEDAR-033].
3. **Commodity price at AWS scale + trust surface**: $5/M decisions, 99.9% SLA, SOC 1/2/3, HIPAA, GovCloud/China, 35 Regions, IaC everywhere [AWSCEDAR-014–019, -025].
4. **Clean externalized-authorization architecture**: schema-validated policies, templates with propagating updates, test bench, deterministic conflict resolution, decisions with determining-policy attribution [AWSCEDAR-008, -009, -010, -002].
5. **Cedar as an emerging standard**: Apache-2.0, CNCF Sandbox, Go/Java ports, and AWS itself re-using it across Verified Access, AgentCore (agent tool-call governance incl. time-window policies and NL policy generation), Kubernetes, and Dogwood's temporal/sequence extension [AWSCEDAR-030, -031, -034, -035].

## 11. Weaknesses / constraints

All evidence-backed unless labeled inference:

1. **No policy lifecycle.** No version history, no rollback, no staged rollout, no approvals; AWS's own guidance assigns version tracking to customer CI/CD [AWSCEDAR-022, -023, -024].
2. **Binary outcomes, thin reasons.** `ALLOW | DENY` only; implicit deny returns no explanation; no review/escalation disposition; no reason-code vocabulary [AWSCEDAR-002].
3. **Decision evidence is DIY.** Decision logging off by default; logged events omit determining policies/context; no decision store, query, or replay [AWSCEDAR-012, -013, -024].
4. **No data plane for facts.** Every signal (geo, identity, fraud, ledger state) must be fetched and pushed by the app per request; no connectors, no orchestration [AWSCEDAR-022].
5. **Stateless temporal support.** Datetime conditions require the caller to supply the clock; forgetting it makes time conditions silently fail (documented in the AgentCore context); no effective-date scheduling [AWSCEDAR-034].
6. **Content-free.** Zero jurisdictional, legal, or domain policy content; no counsel-facing surfaces [AWSCEDAR-024, -043].
7. **Operational ceilings**: 200 RPS default per store (adjustable), 10KB policies, 1 identity source/store, regional single-store scope (multi-region resilience is customer-architected) [AWSCEDAR-011, -019] (last point inference from regional service model).
8. **Token caveat**: revoked tokens remain valid to AVP until expiry — a real gap for instant-block scenarios unless the app compensates [AWSCEDAR-005].

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,AWSCEDAR-001;AWSCEDAR-024
A02,0,AWSCEDAR-001;AWSCEDAR-024
A03,0,AWSCEDAR-001;AWSCEDAR-024
A04,0,AWSCEDAR-001;AWSCEDAR-024
A05,0,AWSCEDAR-001;AWSCEDAR-024
A06,0,AWSCEDAR-001;AWSCEDAR-024
A07,0,AWSCEDAR-001;AWSCEDAR-024
A08,0,AWSCEDAR-001;AWSCEDAR-024
A09,0,AWSCEDAR-001;AWSCEDAR-024
A10,0,AWSCEDAR-001;AWSCEDAR-024
B01,4,AWSCEDAR-002;AWSCEDAR-003;AWSCEDAR-004
B02,4,AWSCEDAR-001;AWSCEDAR-006;AWSCEDAR-036
B03,3,AWSCEDAR-011;AWSCEDAR-020;AWSCEDAR-036
B04,2,AWSCEDAR-002
B05,2,AWSCEDAR-002;AWSCEDAR-006
B06,4,AWSCEDAR-003;AWSCEDAR-007;AWSCEDAR-009
B07,1,AWSCEDAR-005;AWSCEDAR-022
B08,3,AWSCEDAR-006
B09,2,AWSCEDAR-010;AWSCEDAR-033
B10,1,AWSCEDAR-012;AWSCEDAR-013;AWSCEDAR-024
C01,1,AWSCEDAR-003;AWSCEDAR-007
C02,1,AWSCEDAR-007
C03,1,AWSCEDAR-007;AWSCEDAR-009
C04,2,AWSCEDAR-034;AWSCEDAR-007
C05,0,AWSCEDAR-022;AWSCEDAR-023;AWSCEDAR-024
C06,0,AWSCEDAR-024;AWSCEDAR-043
C07,2,AWSCEDAR-033;AWSCEDAR-010
C08,0,AWSCEDAR-024;AWSCEDAR-022
C09,1,AWSCEDAR-007
C10,0,AWSCEDAR-024;AWSCEDAR-043
D01,1,AWSCEDAR-012;AWSCEDAR-013
D02,2,AWSCEDAR-012
D03,1,AWSCEDAR-002;AWSCEDAR-013;AWSCEDAR-023
D04,2,AWSCEDAR-012;AWSCEDAR-013
D05,1,AWSCEDAR-040;AWSCEDAR-012
D06,1,AWSCEDAR-012;AWSCEDAR-022;AWSCEDAR-023
D07,1,AWSCEDAR-012;AWSCEDAR-038
D08,1,AWSCEDAR-012;AWSCEDAR-038
D09,2,AWSCEDAR-038
D10,2,AWSCEDAR-039;AWSCEDAR-040;AWSCEDAR-020
E01,0,AWSCEDAR-001
E02,0,AWSCEDAR-001
E03,0,AWSCEDAR-001
E04,1,AWSCEDAR-003;AWSCEDAR-007
E05,0,AWSCEDAR-001;AWSCEDAR-022
E06,0,AWSCEDAR-001;AWSCEDAR-022
E07,0,AWSCEDAR-001;AWSCEDAR-024
E08,0,AWSCEDAR-001;AWSCEDAR-024
E09,0,AWSCEDAR-024
E10,0,AWSCEDAR-022
F01,0,AWSCEDAR-001;AWSCEDAR-024
F02,0,AWSCEDAR-001;AWSCEDAR-024
F03,0,AWSCEDAR-001;AWSCEDAR-024
F04,0,AWSCEDAR-001;AWSCEDAR-024
F05,0,AWSCEDAR-001;AWSCEDAR-024
F06,0,AWSCEDAR-001;AWSCEDAR-024
F07,0,AWSCEDAR-001;AWSCEDAR-024
F08,0,AWSCEDAR-001;AWSCEDAR-024
F09,0,AWSCEDAR-001;AWSCEDAR-024
F10,0,AWSCEDAR-001;AWSCEDAR-024
G01,3,AWSCEDAR-021;AWSCEDAR-011;AWSCEDAR-022
G02,3,AWSCEDAR-004;AWSCEDAR-024
G03,3,AWSCEDAR-029;AWSCEDAR-001
G04,0,AWSCEDAR-024;AWSCEDAR-022
G05,2,AWSCEDAR-021;AWSCEDAR-025;AWSCEDAR-022
G06,3,AWSCEDAR-009;AWSCEDAR-010;AWSCEDAR-033
G07,2,AWSCEDAR-040;AWSCEDAR-026;AWSCEDAR-023;AWSCEDAR-025
G08,1,AWSCEDAR-037
G09,3,AWSCEDAR-016
G10,4,AWSCEDAR-017;AWSCEDAR-018;AWSCEDAR-019
H01,4,AWSCEDAR-024;AWSCEDAR-027
H02,4,AWSCEDAR-027
H03,1,AWSCEDAR-037
H04,2,AWSCEDAR-010;AWSCEDAR-014
H05,3,AWSCEDAR-027;AWSCEDAR-042
H06,3,AWSCEDAR-012
H07,4,AWSCEDAR-011
H08,2,AWSCEDAR-012;AWSCEDAR-039
H09,3,AWSCEDAR-024
H10,4,AWSCEDAR-025
I01,1,AWSCEDAR-043;AWSCEDAR-020
I02,4,AWSCEDAR-043;AWSCEDAR-020;AWSCEDAR-001
I03,0,AWSCEDAR-043
I04,1,AWSCEDAR-043
I05,3,AWSCEDAR-020;AWSCEDAR-019
I06,4,AWSCEDAR-014;AWSCEDAR-001
I07,1,AWSCEDAR-043;AWSCEDAR-022
I08,2,AWSCEDAR-030;AWSCEDAR-028
I09,2,AWSCEDAR-022;AWSCEDAR-028
I10,4,AWSCEDAR-014;AWSCEDAR-015
J01,1,AWSCEDAR-001;AWSCEDAR-007
J02,0,AWSCEDAR-022;AWSCEDAR-024
J03,0,AWSCEDAR-024
J04,1,AWSCEDAR-033
J05,2,AWSCEDAR-001;AWSCEDAR-021
J06,0,AWSCEDAR-022
J07,1,AWSCEDAR-012;AWSCEDAR-013;AWSCEDAR-023
J08,1,AWSCEDAR-002;AWSCEDAR-012
J09,1,AWSCEDAR-008;AWSCEDAR-024
J10,1,AWSCEDAR-001;AWSCEDAR-022;AWSCEDAR-024
```

**Scoring notes (0s and 1s are reasoned, not "unmentioned"):**

- **A01–A10 = 0 (inference, labeled):** AVP's documented purpose is application authorization only [AWSCEDAR-001, -043]; the complete 34-operation API surface [AWSCEDAR-024] contains no promotion, entry, drawing, fulfillment, or tax constructs. Architecture and enumerated feature set preclude these; this is positive absence, not silence.
- **B04/B05 = 2:** binary ALLOW/DENY with determining policy IDs is meaningful but there is no review outcome and no reason-code system; implicit deny is unexplained [AWSCEDAR-002].
- **B07 = 1:** the only "state" AVP holds about a subject is what a JWT carries or what the caller pushes per request [AWSCEDAR-005, -022].
- **B10 = 1:** manual re-execution of a logged request against *current* policies is possible; true replay against historical policy state is not [AWSCEDAR-012, -013, -023].
- **C01–C03 = 1 (inference, labeled):** Cedar can express jurisdiction/product/action-conditional logic over caller-supplied attributes — pure expressiveness, no jurisdictional content, data, or semantics supplied.
- **C04 = 2:** datetime/duration conditions are real language features, but there is no engine clock (caller must pass time; silent failure if omitted) and no scheduled effective-dating of policies [AWSCEDAR-034, -024].
- **C05/C08/C10/C06 = 0:** explicit official statements assign version tracking to the customer [AWSCEDAR-022, -023]; no approval, monitoring, or content library anywhere in the enumerated product [AWSCEDAR-024].
- **C07 = 2:** Cedar Analysis provides genuine logical pre-rollout impact analysis (permissiveness diffs with counterexamples) but as an external OSS CLI, with no data-driven impact estimation and no AVP integration [AWSCEDAR-033].
- **D-row:** decision logging exists only as opt-in CloudTrail data events missing policy-ID/context linkage [AWSCEDAR-012, -013]; D09=2 is CloudTrail's tamper-evidence inherited by AVP logs [AWSCEDAR-038].
- **E-row ≈ 0:** the service "presumes that the principal has been previously identified and authenticated through other means" and retrieves no external data [AWSCEDAR-001, -022]; E04=1 only because policies can evaluate caller-supplied IP/location attributes (ipaddr extension) — expressiveness, not capability (inference, labeled).
- **F-row = 0 (inference, labeled):** no ledger/balance/entitlement constructs in the enumerated product [AWSCEDAR-024].
- **G04 = 0:** no approval workflow feature exists [AWSCEDAR-024]; approvals are achievable only by wrapping AVP's write APIs in customer pipelines [AWSCEDAR-022].
- **G05 = 2:** environment separation is well supported *by pattern* (separate stores + IaC promotion) but there is no product concept of environments (inference on pattern, labeled).
- **I07 = 1** means low professional-services dependency (self-serve) but substantial in-house engineering; **I08 = 2** reflects moderate switching cost — Cedar's open-source engine makes policies portable off AVP (inference, labeled).
- **J05 = 2 (inference, labeled):** centralized multi-application policy management is a supported architecture (shared or per-app stores, guardrail policies), but nothing normalizes actions across products; each app integration is bespoke.

## 13. White-space implications

**1. Which proposed Promotion OS capabilities are already solved?**
The *decision engine substrate* (J05's mechanical core): synchronous, deterministic, schema-validated, attribute-based allow/deny with policy attribution, deployed independently of app code, at $5/M requests with AWS-grade compliance posture (SOC/HIPAA/GovCloud) and formal-verification assurance [AWSCEDAR-002, -006, -009, -014, -017, -032]. Policy-as-code in an analyzable, open, CNCF-governed language (J01's *executable* half, minus all regulatory content) [AWSCEDAR-030, -031].

**2. Which are partially solved?**
- **J04 impact analysis**: Cedar Analysis proves permissiveness deltas between policy sets with counterexamples — the logical half; no data/traffic-based impact simulation [AWSCEDAR-033].
- **J07/J08 evidence & replay**: opt-in decision events + tamper-evident trails + determining-policy IDs at decision time exist as parts; the assembled capability (decision store keyed to policy versions and full inputs, historical re-evaluation) does not [AWSCEDAR-012, -013, -023].
- **C04 temporal rules**: datetime conditions yes; effective-date lifecycle no [AWSCEDAR-034].
- **G01 multi-tenant/brand governance**: per-tenant stores and guardrails as pattern, no management layer [AWSCEDAR-021].

**3. Which appear unsolved?**
Everything regulatory and workflow-shaped: jurisdictional/legal content (C01–C03, C10, J09), regulatory change monitoring (C06), counsel approval and legal-to-production workflow (C08, J02, J03), policy version history and historical reconstruction (C05, D06, J07/J08 as products), signal normalization/orchestration (E-row, J06), review/escalation outcomes (B04), and any lifecycle control plane semantics (J10). AWS documents several of these as explicitly the customer's job [AWSCEDAR-022].

**4. Could this vendor add the missing capability easily?**
Mechanical layers — yes, plausibly: policy versioning, approval gates, decision logging as a feature, effective dating are natural service increments (AWS has adjacent precedents: CloudTrail, Config, CodePipeline approvals; AgentCore already added system-time injection and NL policy generation on Cedar [AWSCEDAR-034, -035]). Regulatory *content*, counsel-facing workflow, and cross-vendor signal normalization — historically off-pattern for AWS, which ships primitives and lets partners/customers build domain layers (inference from AWS product strategy; labeled inference).

**5. Could a customer assemble it using this vendor + internal engineering?**
A sophisticated platform team could credibly assemble the *authorization core* of Promotion OS on AVP/Cedar: schema for regulated actions, jurisdiction attributes in context, per-brand policy stores, git-based policy versioning + CodePipeline approvals (counsel as an IAM-gated approver), CloudTrail data events + app-side logging into a decision lake, Cedar Analysis in CI for change impact. Every piece is documented [AWSCEDAR-021, -022, -025, -033]. The assembly is nontrivial: the customer owns the legal-content pipeline, counsel UX, evidence store schema, signal fetching, review workflows, and cross-app action taxonomy — realistically a multi-quarter platform-team build, permanently maintained, with counsel still working in engineering tools (inference).

**6. What would make a customer buy a separate product instead?**
(a) Maintained jurisdictional/legal policy content with provenance — AVP will never ship "Texas sweepstakes rules"; (b) counsel-grade authoring/approval UX (legal teams do not review Cedar in pull requests); (c) evidence-grade decision reconstruction as a turnkey store of record (AVP's is opt-in, incomplete, and version-blind); (d) review/escalation outcomes and case handoff; (e) cross-vendor signal normalization; (f) regulatory change monitoring feeding policy updates. Conversely, AVP's $5/M pricing and AWS-native procurement mean a separate product must win on these layers, not on decisioning itself — reselling a decision engine against a ~free managed one is not viable (inference).

## 14. Replacement risk

**MEDIUM**

AWS has overwhelming capability at the infrastructure layer and is actively extending Cedar's reach (temporal/sequence rules via Dogwood, agent tool-call governance with time-window "promotional period" examples and natural-language policy generation in AgentCore) [AWSCEDAR-034, -035]. If "Promotion OS" were merely a policy engine with versioning and approvals, AWS could absorb it with routine feature releases — and its pricing already commoditizes the engine [AWSCEDAR-015]. But the proposed product's differentiating mass is regulatory *content*, counsel workflow, evidence packaging, and vendor-signal normalization — domain layers AWS historically leaves to partners and customers (it ships primitives; three years post-GA, AVP still lacks even policy versioning) [AWSCEDAR-022, -024] (strategy characterization is inference). The sharper risk is not AWS *entering* the space but AVP/Cedar being the substrate that makes credible in-house builds cheaper every year, shrinking the buyable surface to the domain layers. Rated MEDIUM for entry, with HIGH substitution pressure on any engine-centric positioning.

## 15. Adjacent discoveries

Competitors/substitutes encountered that the study should consider (beyond assigned OPA #12, Cerbos #14, Permit.io #15):

1. **Oso (osohq.com / Oso Cloud)** — authorization-as-a-service with the Polar policy language and managed decisioning; the closest independent-vendor analog to AVP's "externalized app authorization" job, with stronger developer-workflow tooling. (Identified from domain knowledge; not deep-researched here.)
2. **Authzed / SpiceDB** — managed Google-Zanzibar-style relationship-based authorization (ReBAC); the main architectural alternative to Cedar-style policy evaluation for fine-grained permissions at scale.
3. **Okta FGA / OpenFGA (CNCF)** — Auth0/Okta's managed fine-grained authorization on the open-source OpenFGA (Zanzibar-derived) engine; CNCF-governed like Cedar, distributed through an identity-platform sales motion.
4. **PlainID / Axiomatics** — enterprise "policy-based access management"/ABAC platforms that explicitly market *policy lifecycle management* (authoring UX, workflows, governance) to security and compliance organizations — the closest existing products to the J10 "policy lifecycle control plane" concept, albeit for access control rather than regulatory actions.
5. **Amazon Bedrock AgentCore Policy + Dogwood** — AWS's own Cedar-based governance layer for AI-agent tool calls with time-based rules, prior-action (sequence) conditions, and natural-language policy generation [AWSCEDAR-034, -035]; worth tracking as AWS's most "control-plane-like" Cedar product.

(1–4 are named from researcher domain knowledge for manager follow-up — the session's search budget was exhausted before corroborating fetches; treat as leads, not evidenced claims. 5 is evidenced.)

## 16. Evidence ledger

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| AWSCEDAR-001 | AVP = managed fine-grained authorization for custom apps; Cedar-based; authN/identity explicitly out of scope | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-002 | IsAuthorized returns ALLOW\|DENY + determiningPolicies + errors; implicit deny has empty policy list | https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-003 | Request carries context + caller-supplied entities (attributes, parents) referenced by policy conditions | https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-004 | Batch: ≤30 requests/call, ≤100 principals + 100 resources; shared principal or resource; IAM action-level permissions | https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-005 | IsAuthorizedWithToken: JWT-based principal; signature/expiry validated; revocation has no effect until expiry | https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-006 | Cedar: default deny; forbid overrides permit; skip-on-error; deterministic | https://docs.cedarpolicy.com/auth/authorization.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-007 | Cedar syntax: permit/forbid, ==/in/is scope, when/unless conditions, inert annotations | https://docs.cedarpolicy.com/policies/syntax-policy.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-008 | Templates (?principal/?resource); template edits propagate to all linked policies | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-009 | Schema + Strict validation rejects nonconforming policies at write time | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-010 | Console test bench simulates requests; shows decision + satisfied policies/errors | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/test-bench.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-011 | Quotas: 200 RPS IsAuthorized/store (adj.), 30 RPS batch, 10KB policy, 100KB schema, 30k stores/Region, 1 identity source/store | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/quotas.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-012 | CloudTrail: mgmt events default; authorization calls = data events, off by default; decision in additionalEventData | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-cloudtrail.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-013 | Documented data-event examples lack determining policy IDs, context, entity attributes | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-cloudtrail.html | official-doc | 2026-08-18 | MEDIUM |
| AWSCEDAR-014 | Pricing: $0.000005/single request; batch call = one metered request (≤30 authz), tiered; policy mgmt $0.00004; no minimums | https://aws.amazon.com/verified-permissions/pricing/ | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-015 | June 12, 2025: single-request price cut up to 97% to $5/million | https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-verified-permissions-reduces-price/ | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-016 | SLA credits below 99.9/99.0/95.0% monthly uptime, measured on authorization APIs | https://aws.amazon.com/verified-permissions/sla/ | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-017 | HIPAA eligible since Oct 14, 2024 | https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-verified-permissions-hipaa-eligible/ | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-018 | In scope for AWS SOC 1, 2, 3 | https://aws.amazon.com/compliance/services-in-scope/SOC/ | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-019 | 35 Regions (Aug 2025) incl. GovCloud; China Regions Sept 2025 | https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-verified-permissions-additional-regions | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-020 | Customers: TELUS, Grosvenor (45k buildings), Stedi (700M req/mo), Twilio Flex, FIS | https://aws.amazon.com/verified-permissions/customers/ | case-study | 2026-08-18 | MEDIUM |
| AWSCEDAR-021 | One policy store per app or per tenant recommended; namespaces; aliases; deletion protection | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-022 | Official guidance: customer CI/CD must track policy versions; no external data retrieved by the service | https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-023 | UpdatePolicy mutates in place; effect/principal/resource immutable; eventual consistency; no version history | https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-024 | Full API = 34 CRUD + authorization ops; no decision-log/replay/simulation/approval/versioning/webhook APIs | https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Operations.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-025 | IaC: CloudFormation resources, Terraform (aws + awscc), CDK L2 construct | https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-verifiedpermissions-policystore.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-026 | Policy store deletion protection (Apr 2025); console default-on | https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-verified-permissions-policy-store-deletion-protection | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-027 | SDKs in 10+ languages; CLI/PowerShell; API version 2021-12-01 | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-028 | API Gateway Lambda authorizer (120s cache), AppSync, Express middleware, console wizards | https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-lambda-authorizer-verified-permissions.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-029 | Identity sources: Cognito or OIDC (Okta, Ping, CyberArk); nonhuman principals supported | https://aws.amazon.com/verified-permissions/faqs/ | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-030 | Cedar OSS: Apache-2.0; Rust core; Go/Java ports; designed for automated-reasoning analysis; bounded latency | https://github.com/cedar-policy/cedar | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-031 | Cedar accepted to CNCF Sandbox on October 8, 2025 | https://www.cncf.io/projects/cedar/ | third-party | 2026-08-18 | HIGH |
| AWSCEDAR-032 | Verification-guided development: Lean formal model + proofs + differential testing vs Rust engine | https://www.amazon.science/blog/how-we-built-cedar-with-automated-reasoning-and-differential-testing | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-033 | Cedar Analysis (Jun 16, 2025): SMT symbolic compiler + CLI; policy-set permissiveness diffs w/ counterexamples; OSS only | https://aws.amazon.com/blogs/opensource/introducing-cedar-analysis-open-source-tools-for-verifying-authorization-policies/ | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-034 | Cedar datetime/duration; caller-supplied clock (silent failure if omitted); AgentCore context.system.now w/ "Promotional period policy" example; UTC only | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-time-based.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-035 | Cedar across AWS: Verified Access, AgentCore Policy, cedar-for-k8s; Dogwood (Aug 6, 2026) adds temporal/sequence clauses | https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/ | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-036 | Latency: "evaluate access requests in milliseconds"; no published p99 SLOs | https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp.html | official-doc | 2026-08-18 | MEDIUM |
| AWSCEDAR-037 | No native webhooks; EventBridge events only via CloudTrail (best-effort) | https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-verifiedpermissions.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-038 | CloudTrail log integrity validation: SHA-256 + RSA-signed digest chains (inherited tamper-evidence) | https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-039 | AVP monitoring docs list only CloudTrail; no service CloudWatch metrics documented | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-overview.html | official-doc | 2026-08-18 | MEDIUM |
| AWSCEDAR-040 | FAQ: CloudTrail = audit trail of policy changes (who/when) | https://aws.amazon.com/verified-permissions/faqs/ | official-marketing | 2026-08-18 | MEDIUM |
| AWSCEDAR-041 | GA June 13, 2023 | https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-verified-permissions-generally-available/ | official-marketing | 2026-08-18 | HIGH |
| AWSCEDAR-042 | AVP runs Cedar 4.7 (user guide); Cedar 4.5 support announced Aug 2025 | https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html | official-doc | 2026-08-18 | HIGH |
| AWSCEDAR-043 | Positioning: developers + security/audit; app-permission use cases; no legal/marketing/fraud motion | https://aws.amazon.com/verified-permissions/ | official-marketing | 2026-08-18 | HIGH |

## 17. Verdict

**SUBSTITUTE**

AVP/Cedar is not a competitor to a regulatory action-authorization product — it sells no regulatory content, no counsel workflow, no evidence reconstruction, no signal orchestration, and only binary allow/deny. But it is the strongest "build" option in the build-vs-buy decision this study must survive: a formally verified, CNCF-governed policy language plus a managed decision endpoint at $5/M requests, SOC/HIPAA/GovCloud-cleared, inside the buyer's existing AWS agreement. A sophisticated enterprise can assemble the decisioning core of the hypothesis on it, leaving a separate product to justify itself purely on the unsolved layers: jurisdictional content, legal-to-production workflow, versioned evidence-grade reconstruction, and review outcomes — all documented as absent or explicitly the customer's job. It is simultaneously the natural substrate a Promotion OS could be *built on* (complement), and its pricing forecloses any engine-centric positioning. Verdict: SUBSTITUTE (infrastructure for in-house builds), with complement potential.
