# Category Summary — Manager D: Policy Infrastructure

Manager: Manager D (Policy Infrastructure)
Date: 2026-08-18
Reports reviewed: 12_opa.md, 13_aws_cedar.md, 14_cerbos.md, 15_permitio.md (+ evidence ledgers 12–15, 160 records total)

Category question: what remains to be built if an enterprise assembles the Promotion OS
hypothesis (J01–J10) on OPA, AWS Verified Permissions/Cedar, Cerbos, or Permit.io plus
internal engineering? This summary answers that question after per-report QC, targeted
re-verification of load-bearing claims, and cross-report score normalization.

---

## 1. QC review per report

### 12_opa.md — Open Policy Agent

**Verification performed.**
- All 26 scores of 3/4 traced to cited ledger records; every 3/4 rests on official docs
  (openpolicyagent.org/docs, GitHub org) rather than marketing. The report's discipline in
  labeling inference is the best of the four.
- Re-fetched https://www.openpolicyagent.org/docs/management-decision-logs (2026-08-18):
  confirmed decision-log event fields (decision_id, input, result, bundles[].revision,
  RFC3339 timestamp), masking, `max_decisions_per_second` event dropping, and that OPA
  ships events to a remote service and **stores nothing itself**. This confirms the report's
  "evidence stream, not evidence system" resolution and drives one normalization (D02).
- Re-fetched https://github.com/open-policy-agent/eopa: archive banner confirmed verbatim —
  "archived by the owner on Jun 26, 2026… now read-only", maintainers invited via OPA Slack.
  EOPA (and its Live Impact Analysis) is confirmed orphaned; C07/J04=1 stand.
- Attempted fetch of https://www.styra.com (2026-08-18): DNS timeout (ETIMEOUT), consistent
  with the report's claim that Styra's web presence is offline. The Styra wind-down claim
  (OPA-023, MEDIUM, third-party) is now triple-corroborated: third-party analysis + Oso
  post + my own failed fetch + the EOPA archive. Accepted as fact for synthesis, flagged
  as MEDIUM-confidence on the exact DAS shutdown timeline.

**Challenged claims and resolutions.**
- **D02=4 challenged and downgraded to 3.** Evidence (OPA-011/012/013) fully supports a
  rich, documented per-decision event emission — but OPA provides no storage, query,
  retention, or completeness guarantee (events droppable by config, verified). Cerbos earns
  4 on the same square with emission + central collection + search UI + retention tiers.
  Same rubric must apply: emission-only = 3.
- **B04=3 challenged and kept.** Unlike the other three engines, OPA's decision contract is
  documented as unconstrained structured output ("simple yes/no answers or complex
  structured outputs", OPA-005), so a tri-state allow/deny/review with reasons can be
  returned natively in the response. Cedar/Cerbos constrain the wire contract to a binary
  enum; Permit returns a boolean. The 3-vs-2 split is a real, documented contract
  difference, not researcher generosity. Kept deliberately; synthesis should not re-flag it.
- **I08=3 (switching cost)** is labeled inference resting on the DAS-migration disruption
  plus Rego spread; reasonable, retained as inference.
- 0-scores audited: all A/E/F/C06/C08/C10/D05/G03/G04/G09/I03 zeros rest on positive
  absence evidence (docs enumeration, ecosystem catalog, architecture) — none are
  "website didn't mention it" zeros. No suspicious 0s found.
- Marketing-vs-docs: homepage "audit capability" phrasing vs docs reality (droppable,
  unstored stream) — the report already resolved this in favor of docs. Correct.

**Status: APPROVED WITH CORRECTIONS** (1 score normalization).

### 13_aws_cedar.md — AWS Verified Permissions / Cedar

**Verification performed.**
- All 21 scores of 3/4 traced to cited records; the report's use of the full 34-operation
  API enumeration (AWSCEDAR-024) as positive-absence evidence is exemplary.
- Re-fetched https://aws.amazon.com/verified-permissions/pricing/ (2026-08-18): confirmed
  "$0.000005 per API request" single authorization, batch metered **per API call** (up to
  30 authorizations) at $0.00015/$0.000075/$0.00004 tiers, policy management $0.00004,
  "no upfront or minimum fees". The $5/M commoditization claim — the category's most
  strategically important pricing fact — is verified.
- G10=4 (SOC 1/2/3 + HIPAA + GovCloud/China + 35 regions), G09=3 (published SLA with
  credits), H07=4 (fully published quotas), H10=4 (CF/Terraform/CDK) all check out against
  official AWS pages; these anchor the "AWS-grade trust surface at commodity price" finding.
- C05=0 is the strongest 0 in the category: AWS's own prescriptive guidance assigns policy
  version tracking to customer CI/CD, and UpdatePolicy mutates in place (AWSCEDAR-022/023).
  Confirmed as documented absence, not inference.

**Challenged claims and resolutions.**
- **E04=1 downgraded to 0.** Evaluating a caller-supplied IP with the ipaddr extension is
  attribute expressiveness (already credited in B06), not geolocation capability. OPA and
  Cerbos scored the identical situation 0. Normalized for consistency.
- **F07=0 upgraded to 1.** "Redemption eligibility rules over caller-supplied facts are
  exactly what the engine evaluates" is the stated rationale for F07=1 at OPA, Cerbos, and
  Permit; it applies verbatim to Cedar. The 0 was an under-score relative to peers.
- **J02=0 upgraded to 1.** AVP has documented deployment rails (CloudFormation/Terraform/
  CDK, eventual-consistency propagation) with nothing legal-specific — the same situation
  scored J02=1 at OPA ("git-to-bundle rails exist but nothing legal-specific"). F10=0 was
  examined and NOT raised: unlike OPA (http.send), Cerbos (Synapse), and Permit (OPAL),
  AVP has no data-fetch mechanism at all ("additional context… not retrieved"), so the
  external-ledger-integration score legitimately differs from F07.
- **B03=3 kept** (not 4): "milliseconds" statements are official but unquantified, default
  quota is 200 RPS/store, and there is a network hop; correctly calibrated below the local
  sidecar engines.
- Adjacent competitors 1–4 in Section 15 are explicitly flagged by the researcher as
  uncorroborated leads from domain knowledge (search budget exhausted). Treated as leads;
  all four were independently corroborated by the other three reports' evidenced sightings
  (Oso, AuthZed/SpiceDB, OpenFGA/Auth0 FGA, PlainID/Axiomatics), so no return for
  correction is needed.

**Status: APPROVED WITH CORRECTIONS** (3 score normalizations).

### 14_cerbos.md — Cerbos

**Verification performed.**
- All 30 scores of 3/4 traced to cited records. The load-bearing D-row (D02=4, D03=4,
  D04=4, D08=3) rests on official Hub/PDP docs (audit.html, v0.33.0 release notes,
  audit-log-collection.html) and is the genuine category high-water mark: decision logs
  carrying full inputs + outcome + git-commit policy revision, centrally searchable,
  retention-tiered, mask-and-export controlled. Verified as documented.
- Re-fetched https://docs.cerbos.dev/cerbos/latest/configuration/observability.html
  (503'd during agent research, MEDIUM confidence): now fetched cleanly — Prometheus
  `/_cerbos/metrics` endpoint, OTLP push metrics, and OTLP distributed tracing confirmed
  verbatim. CERBOS-031 upgraded in effect to HIGH; H08=3 stands.
- Re-fetched https://www.cerbos.dev/product-cerbos-synapse: Synapse exists and is promoted
  as a core platform component (IdP/DB/gateway/Kafka/K8s connectors, WASM custom adapters,
  TTL caching) with **no explicit GA/beta status** and — decisive for J06 — **no mention of
  risk assessment, fraud detection, or vendor signal normalization**: attribute enrichment
  only. E10=2 stands (real but maturity-unclear orchestration); J06 is normalized (below).
- Re-fetched https://www.cerbos.dev/pricing: "Uptime SLA" / "Enterprise support SLA" are
  bare line items with no published percentages or SLA document; audit retention tiers
  (1 week / 3 months / 1 year / custom) confirmed. G09=2 and D08=3 stand.

**Challenged claims and resolutions.**
- **C07=2 downgraded to 1.** The cited evidence is the test framework plus staged
  deployment — the same evidence class scored C07=1 at OPA. The report's own weaknesses
  section concedes "nothing quantifies how a policy change would have altered
  historical/production decisions." 2 on this square is reserved for actual change-impact
  tooling (Cedar Analysis's formal diffs; Permit's traffic replay), which Cerbos lacks.
- **G04=2 downgraded to 1.** CERBOS-041 documents the absence of any Hub-native approval
  workflow; approvals are the customer's external git-PR process, and test gates are gates,
  not approvals. Permit keeps G04=2 because it ships in-product approval-flow features
  (Elements); Cerbos's situation is closer to OPA/Cedar's (0) than to Permit's, and lands
  at 1 because Hub's git-linked stores make the PR path a documented, supported route with
  identifiable human users.
- **D09=2 downgraded to 1.** Bundle signing protects policy distribution only; the report's
  own Section 7 states there is "no documented tamper-evidence (hash-chaining/WORM) on the
  audit log itself," and age-encryption of exports is confidentiality, not integrity. OPA
  scored 1 for the identical posture (bundle signing, no log integrity); Cedar keeps 2 for
  CloudTrail's actual signed digest chains.
- **J06=2 downgraded to 1.** Verified: Synapse does attribute fetching/enrichment from
  customer systems, not cross-vendor risk-signal normalization; evidence is a marketing
  page with maturity unconfirmed. Permit's equivalent (OPAL data fetchers + JIT
  attributes, GA and documented) scored J06=1. Parity applied.
- **J10=3 downgraded to 2.** Hub is the most complete generic lifecycle control plane in
  the category, but the square is the *regulatory* policy lifecycle control plane; every
  regulatory-specific element (counsel roles, effective-dating, legal content, impact
  analysis, attestation records) is absent — the identical situation the Permit researcher
  scored 2 with an explicit "mechanism present, regulatory substance absent" rule and the
  OPA researcher scored 2. One rule must govern the row; 2 is the mechanism-only ceiling.
- **G08 and H03 `?` resolved to 1.** Kafka audit streaming is a documented push channel
  (CERBOS-011, HIGH) and no webhook feature is documented anywhere in PDP or Hub docs
  reviewed; "minimal/peripheral" (1) is the accurate resolution for both squares.
- Kept after challenge: C05=4 (three-layer versioning with immutable store versions —
  documented and genuinely category-leading), D03=4/D06=3/J07=3 (git-SHA-pinned decision
  lineage is the strongest reconstruction story in the study), B03=3 (marketing sub-ms
  correctly held at 3), E10=2 (verified real).
- Marketing-vs-docs: "compliance-ready (SOC 2, HIPAA, GDPR…)" framing correctly resolved
  by the researcher as posture-level, not regulatory content. Confirmed.

**Status: APPROVED WITH CORRECTIONS** (7 score normalizations, incl. two `?` resolutions).

### 15_permitio.md — Permit.io

**Verification performed.**
- All 28 scores of 3/4 traced to cited records; docs-first evidence discipline is good and
  inference is consistently labeled (PERMITIO-039/040 carry explicit INFERENCE flags).
- Re-fetched https://docs.permit.io/how-to/use-audit-logs/audit-log-replay/: confirmed the
  Replay API re-executes recorded `permit.check()` traffic against a chosen PDP, 30-day
  window, concurrency 10, regression-testing use case, "always point to a test PDP"
  guidance. B10=3 (the only productized replay in the category) and the C07/J04=2 scores
  it supports are verified.
- Audit-log constraints verified from cited docs: 10,000-result API cap, plan-based
  retention (14 days free), Debug Mode latency warning. These support the report's
  "operational, not evidentiary" finding on the evidence layer.

**Challenged claims and resolutions.**
- **B03=4 downgraded to 3.** The <10ms p95 / ~100ms p95 propagation figures are
  vendor-published docs claims with no independent corroboration; the architecture (local
  container PDP) is the same class as Cerbos, which scored 3 on equivalent vendor claims.
  OPA keeps 4 because its claim is anchored by official performance-engineering docs plus
  extreme-scale named-adopter evidence (Pinterest 400K–8.5M QPS).
- **J05=4 downgraded to 3.** Real-time cross-product authorization is genuinely Permit's
  core product, but the decision contract is boolean-only, "review" exists only as the
  Elements application pattern, and no regulated-action semantics exist — the same
  situation scored 3 at OPA (with larger-scale production proof) and Cerbos. 4 would
  require the review outcome + action taxonomy the J05 differentiator describes.
- **G03=3 downgraded to 2.** SSO is an Enterprise-tier pricing line item with no
  implementation documentation cited — the identical posture scored 2 at Cerbos. Cedar
  keeps 3 (IAM Identity Center is fully documented platform SSO).
- **G09=3 downgraded to 2.** "Custom SLA options including 99.99%" is a pricing-page
  mention; no published SLA document exists. Identical posture to Cerbos (2); Cedar keeps
  3 for its published SLA with credit schedule.
- **E02=1 and E04=1 downgraded to 0.** Age- and location-conditioned *enforcement* over
  caller-supplied attributes is B06 expressiveness; OPA and Cerbos scored the identical
  capability 0 on the verification/geolocation squares, and the report itself concedes
  "verification/detection is absent." E09=1 is kept (Elements approval-management is a
  real, documented minimal review-queue surface no peer has).
- **H06 `?` resolved to 2.** The decision path is a stateless read and inherently
  idempotent — the same reasoning OPA and Cerbos used to score H06=2; no idempotency-key
  mechanism is documented for management writes. D09 stays `?` (genuinely unresolved for a
  closed SaaS; no enumeration proves absence).
- Kept after challenge: D02=4 (per-check decision logs with reasons + UI/API are core
  product; retention weakness is priced into D08=2), G01=4 (tenant-as-API-parameter is the
  most productized multi-tenancy in category), G05=4 (env copy/preview-env APIs), H09=4
  (GitOps exports the entire policy surface to customer git), B07=3 (genuine synced
  authorization-data store; peers hold 1–2).
- Marketing-vs-docs: homepage "sub-millisecond"/"hundreds of millions of identities"
  claims correctly discounted by the researcher in favor of docs p95 figures. Confirmed.

**Status: APPROVED WITH CORRECTIONS** (7 score normalizations, incl. one `?` resolution).

---

## 2. Score normalization block

Only changed squares are listed; agent scores stand everywhere else. `?`→n rows are
resolutions, not disagreements.

```csv
company,square,agent_score,normalized_score,reason
OPA,D02,4,3,"decision-log capability is emission-only: no storage/query/retention, events droppable under load (verified 2026-08-18); 4 reserved for emission+collection+search (Cerbos)"
AWS Cedar,E04,1,0,"evaluating caller-supplied ipaddr is B06 expressiveness, not geolocation; parity with OPA/Cerbos E04=0"
AWS Cedar,F07,0,1,"redemption-eligibility rules over caller-supplied facts are evaluable like any Cedar policy; parity with OPA/Cerbos/Permit F07=1"
AWS Cedar,J02,0,1,"documented IaC deployment rails (CFn/Terraform/CDK) equivalent to OPA git-to-bundle rails scored J02=1; nothing legal-specific in either"
Cerbos,C07,2,1,"cited evidence is tests+staging only, same class as OPA C07=1; no diff/replay impact tooling; report's own weaknesses section concedes absence"
Cerbos,D09,2,1,"bundle signing covers distribution only; no audit-log tamper-evidence documented (report Sec.7); parity with OPA D09=1; Cedar keeps 2 for CloudTrail digest chains"
Cerbos,G04,2,1,"no Hub-native approval workflow (CERBOS-041); approvals are external git PRs; Permit keeps 2 for in-product Elements approval flows"
Cerbos,J06,2,1,"Synapse verified as attribute enrichment only, no risk-vendor signal normalization, maturity unconfirmed; parity with Permit OPAL-based J06=1"
Cerbos,J10,3,2,"strong generic control plane but zero regulatory lifecycle semantics (counsel/effective-dating/content); mechanism-only ceiling of 2 applied uniformly (Permit/OPA=2)"
Cerbos,G08,?,1,"resolved: Kafka audit streaming is a documented push channel; no webhook feature documented in PDP or Hub docs"
Cerbos,H03,?,1,"resolved: same basis as G08"
Permit.io,B03,4,3,"vendor-published p95 figures without independent corroboration; same architecture/evidence class as Cerbos B03=3; OPA 4 anchored by perf docs + extreme-scale adopters"
Permit.io,J05,4,3,"core product but boolean-only contract, review only via Elements pattern, no regulated-action semantics; parity with OPA/Cerbos J05=3"
Permit.io,G03,3,2,"SSO is an Enterprise pricing line item without implementation docs; parity with Cerbos G03=2; Cedar keeps 3 (documented platform SSO)"
Permit.io,G09,3,2,"'custom SLA options incl. 99.99%' is a pricing-page mention, no published SLA doc; parity with Cerbos G09=2; Cedar keeps 3 (published SLA)"
Permit.io,E02,1,0,"age-conditioned enforcement over supplied attributes is not age verification; parity with OPA/Cerbos E02=0"
Permit.io,E04,1,0,"location-attribute evaluation is not geolocation; parity with OPA/Cerbos E04=0"
Permit.io,H06,?,2,"resolved: decision path is a stateless, inherently idempotent read (same reasoning as OPA/Cerbos H06=2); no key mechanism documented"
```

18 changes total (OPA 1, AWS Cedar 3, Cerbos 7, Permit.io 7). No other changes for any
company; all remaining scores are adopted as submitted.

**Deliberate non-changes** (audited, kept, so synthesis does not re-flag them):
OPA B04=3 vs peers' 2 (documented unconstrained structured-output contract vs binary wire
enums); Permit D02=4 (core-product logs; retention weakness priced into D08=2); Cerbos
C05=4 / D03=4 / J07=3 (verified category-leading version-pinned decision lineage); Cedar
F10=0 vs peers' 1 (AVP uniquely has no data-fetch path at all); Cedar C07=2 (Cedar
Analysis is genuine formal impact tooling); Cerbos E10=2 (Synapse verified real, held
below 3 for maturity); Permit E09=1 (only in-category review-queue surface); Permit
I06=4 vs Cerbos I06=3 (judgment spread on a commercial square, immaterial to synthesis).

**Terminology normalization for synthesis** (the reports use these words differently):
- *Decision log*: an emitted per-decision record. Only Cerbos and Permit also provide the
  *decision-log system* (collection + search + retention). OPA emits only; Cedar logs only
  via opt-in CloudTrail data events missing determining-policy/context linkage.
- *Replay*: Permit's Replay API re-executes recorded inputs against a **current/candidate**
  policy — a change-validation primitive (C07/J04-adjacent). **Point-in-time reconstruction**
  (J08: re-derive what version X decided and why) is push-button nowhere: Cerbos comes
  closest (logs pinned to git SHA + immutable store versions, manual re-execution), OPA has
  the ingredients (revision-stamped events + DIY archives), Cedar cannot do it at all
  (no version history exists to replay against).
- *Impact analysis*: three distinct partial mechanisms exist — formal/logical (Cedar
  Analysis permissiveness proofs), empirical/traffic (Permit replay, 30-day window; EOPA
  LIA now archived), and none (Cerbos/OPA proper: tests only).
- *Effective-dating*: in ALL FOUR products, temporal logic is condition-level and the clock
  is either engine-local (OPA/Cerbos) or caller-supplied (Cedar/Permit); **no product has
  scheduled activation/expiry of policy versions** (C04 uniformly capped at 2).
- *Approval workflow*: only Permit ships an in-product approval feature, and it governs
  runtime end-user operations, not policy deployment. Policy-change approval is git-PR
  convention everywhere.

---

## 3. Category analysis

**Strongest incumbent.** *Open Policy Agent* — by adoption, scale-proof, and ecosystem
gravity (Goldman Sachs, Netflix, Capital One, BNY Mellon, Pinterest at 400K–8.5M QPS;
CNCF-graduated; free). It defines the engine layer this category commoditizes. The
strongest *packaged product* incumbent is **Cerbos Hub**, which ships the most complete
versioning + decision-lineage + lifecycle capability set of the four (C05=4, D02–D04=4/4/4,
git-SHA-pinned decisions, test-gated signed deployments with rollback). Neither incumbent
holds any position in the regulatory layer: across all four vendors, every content,
counsel, and legal-provenance square (C06, C08–C10, J03, J09) scores 0–1 after
normalization.

**Most dangerous substitute.** Not a vendor — the assembly path: *"enterprise platform team
+ Cerbos (or OPA) + outside counsel."* Cerbos is the sharpest version because $0–$933/month
buys versioned executable policy with jurisdiction-capable scope hierarchies, sub-10ms
decisions, decision logs pinned to policy git SHAs, and a working control plane — i.e., the
mechanism halves of J01/J02/J05/J07/J08/J10 out of the box, proven at FTSE-250 scale
(Utility Warehouse, 4,500 services, on the free tier). The distinct second threat is **AWS
Verified Permissions/Cedar as a price and procurement weapon**: $5/M formally verified
decisions inside an existing AWS agreement with SOC 1/2/3, HIPAA, GovCloud, and a published
SLA. AVP forecloses any engine-centric or per-decision-priced positioning even though its
lifecycle layer is the weakest of the four (no policy versioning at all). OPA is the
substitute-by-assembly for top-decile engineering organizations, though the Styra collapse
(verified: styra.com dark, EOPA archived June 2026) just raised the cost of that path by
removing its only mature commercial control plane.

**Capabilities already commoditized** (do not build, do not price against):
- Synchronous, low-latency, arbitrary-attribute decision evaluation (B01–B03, B06):
  all four score 3–4; priced from $0 (OSS) to $5/M (managed, SLA-backed).
- Policy deployed/updated independently of application code (all four; seconds-scale
  propagation at Cerbos/Permit).
- Policy-as-code languages and testing frameworks (Rego/Cedar/CEL; OPA and Cerbos G06=4;
  Cedar adds machine-checked formal semantics).
- Developer platform table stakes: APIs, 6–10-language SDKs, IaC/GitOps deployment
  (H01/H02 = 4 across the board; H09/H10 3–4).
- Basic decision logging with reasons (every vendor emits per-decision records; two
  provide managed collection/search).
- Git-based policy version history (Cerbos natively + Permit via GitOps; OPA via bundles;
  only AVP lacks it).

**Capabilities partially covered** (mechanism exists somewhere, never the full concept):
- Decision→policy-version lineage: Cerbos category-leading (git SHA per decision);
  OPA revision-stamped events; Permit needs Debug Mode/GitOps correlation; Cedar none.
- Replay/reconstruction: Permit has productized 30-day input replay (change validation);
  Cerbos has version-pinned manual reconstruction; nobody has push-button historical
  "why was this allowed?" (J08 ≤ 2 everywhere).
- Pre-rollout impact analysis: Cedar Analysis (formal permissiveness diffs, OSS CLI,
  not integrated); Permit replay (empirical, no diff report); EOPA LIA (the only true
  live-traffic what-if) archived unmaintained. C07/J04 ≤ 2 everywhere.
- Temporal rules: condition-level everywhere; effective-dated/scheduled policy activation
  nowhere (C04=2 across all four — a strikingly uniform mechanical gap).
- Human approvals: Permit's Elements approve/deny flows with webhooks (runtime operations
  only); everyone else delegates to git. No product records policy-approval history as
  evidence (D05 ≤ 2).
- Environments/change management: strong generic pipelines at Cerbos (test-gated signed
  bundles, rollback) and Permit (env copy, preview envs, Policy Guard baselines).
- Attribute-fetch orchestration: Cerbos Synapse (maturity unclear) and Permit OPAL
  fetchers move data to decisions; neither normalizes risk-vendor semantics (J06 ≤ 1).
- Multi-tenancy/brand: productized at Permit (tenant is an API parameter), pattern-level
  at Cedar/Cerbos, DIY at OPA.
- Retention: Cerbos to 1 year/custom (D08=3); Permit plan-based from 14 days; OPA/Cedar
  sink-dependent.

**Apparent gaps** (0–1 across ALL FOUR vendors after normalization — the candidate white
space):
1. Regulatory/jurisdictional content in any form: no legal rule libraries, no provenance
   model, no regulatory change monitoring (C06, C09, C10, J09 ≤ 1 everywhere; mostly 0).
2. Counsel-facing workflow: no legal-reviewer role, no attestation/approval records in the
   deployment path, no non-engineer authoring surface for regulated rules (C08, J03,
   D05-as-policy-approval ≤ 1).
3. Evidence-grade guarantees: no tamper-evident decision logs (best is inherited CloudTrail
   digests at Cedar, D09=2; peers 1/?), no retention SLAs framed for regulators, no
   evidence-package/export-for-regulator product (D07 ≤ 2).
4. Tri-state decision semantics: no engine returns allow/deny/REVIEW with a standard reason
   vocabulary; review queues/case handoff absent (B04 ≤ 3, E09 ≤ 1).
5. Stateful eligibility: no counters, velocity, entry history, or per-user accumulators in
   any engine (B07 ≤ 3; the Permit 3 is entity/attribute state, not event aggregation).
6. Signal generation and cross-vendor normalization: nothing verifies identity/age/
   location or normalizes geo/IDV/fraud vendor outputs (E01–E08 = 0 everywhere; J06 ≤ 1).
7. Effective-dated policy activation (C04=2 uniformly): "this rule takes force on the
   statute's effective date" is unsupported product-wide.
8. Entire promotion-administration and ledger domains (A, F blocks ≈ 0 everywhere).

**Gaps probably too small to monetize standalone:**
- A "review" outcome API shim, reason-code taxonomy, or webhook/eventing gap-fillers —
  any vendor could ship these in a quarter; no defensibility.
- Effective-dating/scheduled activation alone — real gap, but roadmap-sized for
  Cerbos/Permit and already solved by AgentCore's `context.system.now` pattern at AWS.
- Longer log retention or a replay tool as a product — feature-sized; Cerbos sells
  retention tiers today, Permit ships replay today.
- Policy-format converters/migration tooling (Rego↔Cedar↔CEL) — services business at best.
- A managed OPA control plane to replace Styra DAS — the market just demonstrated
  (Styra's failure to survive independently; $5/M AVP pricing) that engine-adjacent
  governance alone does not sustain a company; OCP/Cerbos/Permit are filling it at ~$0.

**Gaps worth passing to synthesis** (category recommendation):
1. **Maintained jurisdictional/legal policy content with provenance and change monitoring**
   (C06+C09+C10+J09). Uniformly absent; every report independently concludes no
   engine vendor will build it (content requires licensed legal editorial operations, a
   different liability posture, and a legal buyer none of them serves — I01 ≤ 1
   everywhere).
2. **Counsel-native authoring/approval with attestation records in the deployment path**
   (C08+J02+J03+D05). The category's change pipelines are excellent and entirely
   engineer-shaped; "legal reviews YAML in a pull request" is the universal, conceded
   anti-pattern.
3. **Evidence-grade decision archive as a product**: version-pinned, tamper-evident,
   retention-guaranteed, regulator-exportable reconstruction (J07/J08/D06–D09). Cerbos
   proves demand for decision lineage (customers cite audit logs as a favorite feature);
   nobody offers integrity, packaging, or accountability on top of it.
4. **Regulatory impact analysis as a supported product** (C07/J04): the only true
   live-traffic implementation (EOPA LIA) is orphaned code — verified archived — while
   Cedar Analysis and Permit replay prove the two component techniques work. Assembling
   formal + empirical impact analysis over *regulatory* rules is unclaimed.
5. **Cross-vendor risk-signal normalization feeding policy decisions** (J06/E10): the
   engines' data layers (Synapse/OPAL/http.send) fetch attributes but assign all semantic
   normalization to the customer; no one owns "geo/IDV/fraud vendor outputs → normalized
   decision facts."
6. **Tri-state regulated-action contract + review/case handoff** (B04/B05/E09): only
   fragments exist (Permit Elements; OPA's expressible-but-unauthored structured outputs).
7. Cross-cutting packaging insight for synthesis: the wedge should **embed** these engines
   (Cedar/OPA/CEL are open, and AVP/Cerbos/Permit all accept generated policy code), not
   compete with them. The engine layer is commoditized to ~$0–$5/M with the strongest
   trust surfaces in software (AWS SOC/HIPAA/SLA; CNCF governance); all four reports
   independently reach the same conclusion, and the Styra outcome is the cautionary
   proof for engine-adjacent-only monetization.

---

## 4. Internal-build / stack-substitute assessment

Question: can this category's buyer base cover J01–J10 with these vendors + internal
engineering + counsel? Answer: **the mechanism layers yes — credibly and cheaply; the
regulatory layers no — not without standing up a permanent legal-operations function that
no engineering budget contains.** This is the category's core finding for synthesis, and it
cuts both ways: the wedge cannot be the engine, and the wedge must beat a real, cheap
assembly path on the layers assembly cannot reach.

**What a competent platform team gets on day one (per stack):**
- *Cerbos*: jurisdiction-shaped scoped policies (`us.ca`, `eu.de`), CEL time conditions,
  test-gated signed deployment with rollback, decision logs pinned to policy git SHAs with
  1-year retention, AuthZEN API — $0 (OSS) to $933/mo. Closest to J02/J07/J10 mechanics
  out of the box.
- *AVP/Cedar*: formally verified decisions at $5/M inside the existing AWS agreement, with
  SOC 1/2/3, HIPAA, GovCloud, published SLA; Cedar Analysis for formal change diffs;
  IaC-only versioning (the team must build history, logging, and correlation themselves —
  AWS documents this as the customer's job).
- *Permit.io*: no-code editor readable by non-engineers, GitOps PR review, env-copy/preview
  environments, 30-day traffic replay for change validation, runtime approval Elements —
  free to $150/mo to start.
- *OPA*: everything Appsflyer/Netflix/BNY Mellon demonstrably run — central decisioning
  across hundreds of services, versioned signed bundles, revision-stamped decision events —
  plus, post-Styra, the obligation to self-operate the entire control plane (OCP is early,
  65 stars; EOPA archived).

**What remains after the assembly, regardless of stack chosen** (the un-assembled
residue, consistent across all four reports' Section 13 answers):
1. *Legal content and its maintenance* — sourcing, encoding, and continuously updating
   jurisdiction-specific promotional/regulatory rules with provenance. This is a licensed-
   professional editorial operation, not an engineering artifact; it is the one layer no
   stack choice even dents. Internal builds put this on the GC's office as an unfunded,
   permanent mandate.
2. *Counsel workflow and attestation* — every stack routes legal review through git PRs
   over YAML/Rego/Cedar (Permit's UI narrows but does not close this); no approval record
   survives as audit evidence tied to the decision path.
3. *Evidence-grade archive* — schema design, WORM/integrity, retention policy, regulator
   packaging, and (on AVP especially) even basic decision→version correlation: a 2–4
   quarter build plus permanent ownership.
4. *Signal plumbing and normalization* — per-vendor geo/IDV/fraud integrations and a
   normalization layer the engines explicitly leave to the caller.
5. *Review/case flow and stateful eligibility* — a review-outcome convention, queues, case
   handoff, and an event/counter store the stateless engines cannot host.
6. *Accountability* — after Styra's exit, no vendor in this category will contract for
   regulatory-domain correctness; the enterprise's own counsel carries the entire
   interpretation risk of self-encoded rules.

**Credibility gradient.** For top-decile engineering organizations (the OPA adopter class:
banks, big tech) the substitute is credible for J05 plus the mechanism halves of
J01/J02/J07/J08/J10 — they already run these engines in production and the marginal cost is
low. It is NOT credible, at any engineering strength, for the content half of J01, J03,
J04-as-product, J06, or J09 without hiring a legal-editorial capability. For mid-market
enterprises without a dedicated platform team, even the mechanism assembly (enforcement-
point instrumentation, evidence store, signal plumbing) is a multi-quarter program with
permanent maintenance — the realistic outcome is partial builds with unversioned evidence
and stale rules, which is precisely the compliance exposure a product would sell against.
Pricing implication for synthesis: the buy-side alternative is not zero — it is roughly
"Cerbos Hub ($0–$933/mo) or AVP ($5/M) + 1–3 platform engineers permanently + outside
counsel retainer per jurisdiction per year + un-transferred liability." A Promotion OS
must be priced and argued against that stack, and differentiated exclusively on layers
1–6 above.

---

## 5. Adjacent competitor appendix

Deduplicated from Sections 15 of all four reports (sighting count in parentheses).
**Material** = changes the category landscape for synthesis.

| Competitor | Sightings | Relevance | Material? |
|---|---|---|---|
| **Oso / Oso Cloud** (osohq.com) | 4/4 reports | Commercial authorization-as-a-service (Polar language); actively positioning as the vendor-backed alternative amid the Styra wind-down; publishes against Permit/Cerbos. The "engine with a company behind it" substitute. | **Yes** — include in any build-vs-buy landscape; it is where post-Styra commercial demand is being courted. |
| **OpenFGA / Auth0-Okta FGA** | 3/4 | CNCF Zanzibar-style ReBAC engine + Okta's managed service; the free/managed relationship-graph substitute platform teams evaluate alongside OPA/Cerbos. | Marginal — material for entitlement-graph workloads, immaterial for jurisdiction-rule decisioning (no policy/temporal semantics). |
| **AuthZed / SpiceDB** | 2/4 | Managed Zanzibar ReBAC at scale; same family as OpenFGA with a stronger commercial motion. | Marginal — same reasoning. |
| **PlainID** | 2/4 | Enterprise "policy-based access management" sold to security/compliance orgs in banks/insurers, marketing policy lifecycle/governance — the closest *existing product shape* to J10, but for access control, not regulated business actions. | **Yes** — synthesis must check PlainID (and Axiomatics) before declaring the J10 control-plane shape novel; they prove a compliance-adjacent policy-governance buyer exists. |
| **Axiomatics** | 2/4 | Veteran ABAC/XACML dynamic-authorization vendor entrenched in regulated industries; evidence the "policy governance for compliance" category is old and occupied on the access-control side. | **Yes** — same reason as PlainID (treat the pair as one check). |
| **Styra DAS** (residual) | 3/4 | The only mature OPA control plane; winding down post-Apple-acqui-hire (verified: styra.com unreachable 2026-08-18; EOPA archived 2026-06-26). | **Yes, as a market datum, not a competitor** — simultaneously removes the incumbent governance layer (helps a new entrant) and is the cautionary case that engine-adjacent governance alone did not sustain a company (warns the wedge must carry domain value). |
| **Aserto / Topaz** | 2/4 | Small commercial authorization control plane + OSS engine (AuthZEN-conformant, decision logs); another assembly substrate. | No — crowded-field evidence only. |
| **OPAL** | 2/4 | Permit.io's OSS policy/data sync layer (~5.5k stars); already inside the category via report 15. | No (internal to category). |
| **HashiCorp Sentinel** | 1/4 | Proprietary policy-as-code embedded in Terraform/Vault; IaC governance domain. Flagged by the OPA researcher as an unverified, no-ledger-record lead; not corroborated here. | No — IaC-scoped; unverified lead; does not touch business-action authorization. |
| **OPA Gatekeeper / Kyverno** | 1/4 | Kubernetes-native policy packagings of/alongside OPA. | No — but note the pattern: domain-specific packaging of a generic engine repeatedly beats the raw engine (the strategic template for a Promotion OS). |
| **AWS Bedrock AgentCore Policy + Dogwood** | 1/4 (evidenced) | AWS's Cedar-based AI-agent action-governance layer: system clock injection, time-window "promotional period" policy examples, NL policy generation, temporal/sequence rule extensions (Dogwood, Aug 2026). | **Yes, as a watch item** — the clearest signal that AWS is building control-plane/temporal semantics on Cedar; if pointed at regulated business actions rather than agent tool calls, it would be the platform-giant entry path. |
| **Mondoo** | 1/4 | Infra-compliance scanning positioning against Styra-era OPA. | No — infrastructure compliance, different job. |

**Manager addition check:** I looked for material competitors the agents missed. Access-
governance/visibility vendors (e.g., Veza) and consent-management platforms border the
space but do not authorize regulated business actions in-line; no material omission
identified beyond the flagged watch items above. The two names synthesis must actively
clear before declaring white space: **PlainID/Axiomatics** (does their "policy lifecycle
for compliance buyers" motion already cover regulated-action authorization? Current
evidence says access control only) and **AWS AgentCore/Dogwood** (trajectory risk).

---

## 6. Approval line

REPORTS APPROVED: 12_opa.md, 13_aws_cedar.md, 14_cerbos.md, 15_permitio.md
