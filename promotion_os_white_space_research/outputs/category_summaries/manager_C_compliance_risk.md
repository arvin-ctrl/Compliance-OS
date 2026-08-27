# Category Summary — Manager C: Compliance Signals & Risk Platforms

Manager: Manager C (Compliance Signal & Risk Platforms)
Date: 2026-08-18
Reports reviewed: `outputs/company_reports/09_geocomply.md`, `10_persona.md`, `11_socure.md`
Evidence reviewed: `outputs/evidence/09_geocomply.jsonl` (36 records), `10_persona.jsonl` (42), `11_socure.jsonl` (47)

Method note: every 3/4 score was audited against its cited claim IDs; suspicious 0s and all
load-bearing/contested claims were spot-verified by direct WebFetch of the official URLs cited in the
ledgers (10 fetches performed this session; WebSearch not needed). Corrections are recorded in
Section 2 only; raw reports were not edited.

---

## 1. QC review per report

### 09 — GeoComply

**Verification performed.**
- Fetched `geocomply.com/anti-fraud-and-geolocation-solutions/geocomply-core/`: confirmed verbatim
  "enhanced troubleshooter messages," "in milliseconds," "1.2 billion geolocation checks monthly,"
  and dashboards — supports B02/B03/B05 evidence — and confirmed the page contains **no**
  customer-facing rule authoring, versioning, simulation, or approval features (supports the
  report's central absence findings and the C10/J02/J03 zeros).
- Attempted `integrationdocs.geocomply.com`: DNS does not resolve publicly (ENOTFOUND), matching the
  researcher's reduced-confidence note. Attempted `trust.geocomply.com`: JS-shell portal with no
  public content (SOC 2 report under NDA, consistent with GEOCOMPLY-022).
- **? -square resolution check (16 squares: B08, B09, C05, C07, C09, D03, G02, G03, G06, G08, H03,
  H05, H06, H07, H09, J04):** none is resolvable from public sources. Official integration docs are
  auth-gated and license-gated; the trust portal exposes nothing; marketing pages are silent. The ?s
  are correctly assigned and must stay ?. Guidance to synthesis: treat these squares as
  *not-demonstrated* for differentiation purposes (do not credit GeoComply with them), but as
  *possibly-present* for competitive-response risk (several — env credentials, some form of internal
  rule versioning — plausibly exist behind the gate).

**Challenged claims and resolutions.**
- B02/B03/B05 = 3 rest partly on marketing ("milliseconds") plus third-party integration writeups,
  because official docs are gated. Accepted at 3: the synchronous, low-latency, reason-coded
  allow/block behavior is corroborated by deployment reality that is itself documented (real-time
  wager gating at >90% of the US market, 2.6M checks in 24h at Missouri launch, a court order naming
  the product as the required control). This is "equivalently strong" evidence in the brief's sense.
- G09 = 3 (Enterprise SLA) is **not** supported: the evidence is achieved-uptime marketing
  (99.999% in PR vs 99.9999% on homepage — the report itself flags the discrepancy), not SLA terms.
  Downgraded to 2 (positive uptime commitments in regulated environments justify more than the ?
  given to peers, but 3 requires documented SLA terms). See Section 2.
- Marketing-vs-docs contradictions: uptime figures (resolved: treat 99.9999% as marketing);
  "Chameleon" product name (resolved by the researcher — traces to SBTech Chameleon360, not a
  GeoComply product; good catch, prevents a phantom capability).
- A-row/F-row/C10/H10/I03/J02/J03 zeros: all are enumeration-based reasoned absences, correctly
  labeled as inference, grounded in the fully enumerated six-product suite (GEOCOMPLY-001). Not
  mere non-mention. Accepted.
- Inference hygiene: good throughout — vendor-internal rules engine vs customer-facing policy is
  consistently distinguished; Section 7's "facts vs decision-logic" evidence split is the report's
  best analytical contribution and survives verification.

**Verdict: APPROVED WITH CORRECTIONS** (1 score normalization; MAJOR OVERLAP verdict endorsed).

### 10 — Persona

**Verification performed.**
- Fetched `help.withpersona.com/articles/6YBOe6MD4R9WrwEuQND6jA/` (workflow versions): verified
  "Published versions are locked from further editing," version history + revert, percentage
  rollouts splitting traffic between latest and previous version, and — stronger than the report
  states — "Each individual Workflow run is permanently linked to the version that was active at
  the time it was executed." Confirmed **no** approval gate on publishing exists (supports C08=1,
  J02=1, J03=1).
- Fetched `help.withpersona.com/articles/2Luxrdu3Cdg6pcecKBJxvs/` (inquiry templates): verified
  verbatim "Each Inquiry is permanently linked to the version of the Inquiry Template that was live
  when it was generated," compare/revert documented, no publish approval gate.
- Fetched `docs.withpersona.com/webhooks`: verified verbatim the recommendation to poll the API
  "if your application requires instant updates, such as making real-time decisions" — the
  load-bearing evidence for B02=1/B03=1 (no synchronous authorization). Also verified retries,
  30-day event retention, per-webhook versioning, attribute blocklists, IP allowlists. (HMAC
  signature and OAuth-outbound details sit on adjacent doc pages; PERSONA-021 is a composite claim
  — substance verified, G08=4 stands on the verified feature set plus the Persona-Signature HMAC
  mechanism cited in PERSONA-003.)

**Challenged claims and resolutions.**
- E04 = 3 (geolocation) overstates against the category scale. Documented capability is GPS+IP
  collection with VPN/proxy/Tor flags and geo/country lists — real, but the report itself concedes
  "not certified-grade geolocation compliance." Normalized to 2 so the cross-report scale reads
  GeoComply 4 / Persona 2 / Socure 1. See Section 2.
- B04/B06/B07/E09/E10/G08/H01/H03/H05 = 4: all verified as core-product, official-doc capabilities.
  Accepted.
- G10 = 3 on MEDIUM evidence (bot-blocked marketing site): certifications corroborated across press
  and blog announcements; accepted with the confidence caveat already noted in the report.
- The A/F-row zeros and C09/H10 zeros rest on a keyword scan of the full published OpenAPI surface
  (172 paths) — the strongest absence methodology in this category. Accepted.
- Inference hygiene: exemplary. The async-model finding (PERSONA-034), the counsel-approval gap, and
  the switching-cost trajectory are all labeled inference with documented bases.
- One nuance the report gets right and synthesis should not lose: Persona's "simulation" (B09=2) is
  live traffic-splitting plus sandbox stubs — there is **no backtest against historical traffic**;
  that capability exists in this category only at Socure.

**Verdict: APPROVED WITH CORRECTIONS** (1 score normalization; MAJOR OVERLAP verdict endorsed).

### 11 — Socure

**Verification performed** (all against official help.socure.com docs cited in the ledger):
- `manage-workflow-lifecycle.md`: verified Draft/Published/Live, major/minor versions, history with
  view/restore and author attribution, Move-to-Live permission gating; confirmed **no** maker-checker
  approval chain and **no** scheduled/effective-date activation (supports C04=?, C08=1, J02=1).
- `reason-code-lists.md`: verified the governance gap **verbatim**: "Editing a reason code list will
  have an immediate effect on the workflow, without creating a new workflow version" and "Changes to
  reason code lists will not show up in the audit logs." This documented integrity hole is real.
- `decision-path.md`: verified the trace records each executed step/branch/decision "for internal
  governance or external audits"; confirmed the page documents **no workflow-version linkage** on
  the trace and **no re-run under a historical policy version** — it is a post-hoc record, not replay.
- `workflow-testing.md`: verified backtesting re-executes historical records against a draft with
  original-vs-updated comparison; verified limitations verbatim (async workflows untestable, live
  workflows must be cloned first, "Test results cannot currently be exported or downloaded").
- `age-assurance.md`: verified verbatim (stated twice) "Socure remains neutral on regulatory policy
  and doesn't decide which rules apply to your business"; customers configure state rules,
  thresholds, escalation paths. The regulatory-content-neutrality finding is rock-solid.
- `role-permission.md`: verified Move-to-Live is held only by Account Owner and Administrator;
  Compliance Officer/Supervisor/Analyst approvals apply to **cases**, not policy publishing; no
  counsel/legal role, no custom-role creation documented. C08=1/J03=1 are accurate (adaptable
  permission gating, no approval workflow).

**Challenged claims and resolutions.**
- B10 = 3 (decision replay) not supported at 3. Verified: the Decision Path Trace is reconstruction
  (already credited at D06=3), re-evaluation runs a *fresh* evaluation under current logic
  (SOCURE-042), and no as-of-version replay exists. Normalized to 2. See Section 2.
- J07 = 3 (evidence-grade decision reconstruction) not supported at 3 once the verified governance
  gaps are priced in: reason-code-list edits change live decisioning with no version and no audit
  entry; decision→workflow-version linkage undocumented; backtest results not exportable; retention
  unresolved (D08=?). "Evidence-grade" specifically is what these holes break. Normalized to 2,
  which also restores parity with Persona (J07=2 with stronger version pinning but
  assembly-required export) and GeoComply (J07=2, facts-only). See Section 2.
- E10 = 4 (third-party signal orchestration) rests on 14 documented partners plus reseller
  contracting; the 50+/200+ figures are launch/marketing counts that include Socure's own modules
  (the ledger's own note says so). Persona's ~90+ documented integrations define the 4 bar here.
  Normalized to 3. See Section 2.
- B02=4, B04=4, B05=4, C05=3, C07=3, D02=4, E01/E02/E07/E09=4, G-row and H-row 3s: verified or
  well-evidenced in official docs. Accepted. (D02=4 stands: per-evaluation persistence plus
  18-field-category Transaction Details compliance exports is the strongest decision log of the
  three.)
- Marketing-vs-docs contradictions resolved correctly by the researcher: "<150ms" and ">1,000 QPS"
  treated as marketing while synchronous behavior comes from docs; "200+ data products" reconciled
  against 14 documented partners; SAR/CTR/UAR generation flagged as a launch claim not yet found in
  docs (scores correctly do not lean on it).
- I08 = 3 is inference-based (embedded workflows, fraud-feedback loops training Socure models) —
  acceptable as labeled judgment on a degree-present square.
- A/F-row zeros: llms.txt full-tree enumeration basis, labeled. Accepted.

**Verdict: APPROVED WITH CORRECTIONS** (3 score normalizations; MAJOR OVERLAP verdict endorsed).

---

## 2. Score normalization block

Only the squares changed by this review. All other agent scores stand as submitted.

```csv
company,square,agent_score,normalized_score,reason
GeoComply,G09,3,2,"SLA evidence is achieved-uptime marketing (99.999% PR vs 99.9999% homepage, inconsistent); no SLA terms public; regulated-environment uptime commitments justify 2, not 3"
Persona,E04,3,2,"documented geolocation is GPS+IP collection with VPN flags and geo lists; report itself concedes not certified-grade; scale normalization vs GeoComply=4, Socure=1"
Socure,E10,4,3,"documented third-party orchestration is 14 partners + reseller contracting (SOCURE-034); 50+/200+ are marketing counts incl. first-party modules; Persona's ~90+ documented integrations set the 4 bar"
Socure,B10,3,2,"verified: Decision Path Trace is post-hoc reconstruction (credited at D06), no workflow-version linkage documented, re-evaluation runs fresh current-policy logic (SOCURE-042); no as-of replay"
Socure,J07,3,2,"evidence-grade claim broken by verified gaps: reason-code-list edits alter live behavior with no version and no audit-log entry (SOCURE-020, verified verbatim), decision-to-workflow-version link undocumented, backtests not exportable, retention unresolved (D08=?)"
```

- GeoComply: 1 change; all other scores (including all 16 ?s) stand.
- Persona: 1 change; all other scores stand.
- Socure: 3 changes; all other scores stand.

**Terminology normalization for synthesis** (the three reports use these words differently):
- *Synchronous decisioning* = rules evaluated inline in the request path with the decision in the
  response. True of GeoComply Core and Socure RiskOS; **not** true of Persona (poll/webhook, ~5s).
- *Replay* = re-executing a past decision under the policy version in force at the time. **None of
  the three has it.** Socure's "replay the flow" language is trace *reconstruction*; GeoComply's GCI
  is *fact* reconstruction; Persona reconstruction is *assembly* across pinned objects.
- *Policy pack* = GeoComply's vendor-managed per-market configs, Persona's Solution Library, and
  Socure's Launch solutions are all *technical* packs. None contains legal content, citations, or
  effective dates. J09=2 across all three means "technical packaging exists, legal packs do not."
- *Counsel approval* = none of the three has any approval workflow on policy publishing; all three
  have role-based *permission gating* that could crudely emulate one (C08/J03 = 0–1 everywhere).

---

## 3. Category analysis

These three are the closest incumbents to the compliance-decisioning hypothesis. The normalized
picture of "counsel-approved, evidence-grade, jurisdiction-aware action authorization" — who has
which third — is:

| Layer of the hypothesis | GeoComply | Persona | Socure RiskOS |
|---|---|---|---|
| Jurisdiction-aware real-time action gating | **Yes** (ms allow/block + reasons, 30+ jurisdictions) — but vendor-black-box rules, geo/identity scope only | No (async, ~5s; jurisdiction logic customer-built) | Partial (sync allow/deny/review over customer-authored state rules; no shipped jurisdiction content) |
| Customer-authorable versioned policy | No (none exposed) | **Yes** (immutable versions, per-decision pinning, staged rollouts) | Yes (draft/published/live, restore) — with unversioned side-artifacts (reason-code lists, watchlist policies) |
| Pre-rollout impact analysis | ? (not public) | Partial (live %-rollout w/ control; no backtest) | **Yes** (historical backtest + 100%-traffic shadow experiments; not exportable) |
| Counsel-as-approver deployment gate | No | No (RBAC publish rights only) | No (Move-to-Live permission only; case approvals ≠ policy approvals) |
| Evidence-grade decision reconstruction | Facts only (GCI, bank-accepted; no rule/version provenance) | Version-pinned but assembly-required; short forensic windows (2wk/30d/6mo) | Best trace, but no version linkage, audit-bypassing edits, unknown retention |
| As-of-date replay | No | No | No |
| Legal content / provenance / effective dates | Internal-only (managed service; Gov Relations team) | None (deliberately no legal claims) | None (documented regulatory neutrality, stated twice) |

**Strongest incumbent: GeoComply** — in regulated gaming it already *is* the jurisdiction-aware
action-authorization layer: it sits in the transaction path of >90% of the US sports-betting market,
encodes and operates per-jurisdiction rules as a managed service, is itself licensed by regulators,
and gets named in court orders as the required control. It owns the exact budget line and buyer
(CCO/VP Compliance) the hypothesis targets, in the vertical where the pain is most acute. Its
structural limitation is equally clear and verified: the policy layer is a black box — customers
cannot author, version, simulate, approve, or replay anything, and its evidence product reconstructs
facts, never decision logic. (Platform-mechanics runner-up: Socure RiskOS, the strongest *general*
decisioning incumbent across 3,000+ regulated enterprises.)

**Most dangerous substitute: "Socure RiskOS + internal rules + outside counsel"** (with Persona as
the equivalent assembly for async use cases). This is not a future threat; it is how sophisticated
regulated enterprises operate today. RiskOS supplies synchronous allow/deny/review with reason
codes, custom JSON attributes, entity/velocity state, versioned no-code workflows, historical
backtesting, shadow experiments, case management, RBAC with compliance roles, audit logs, and
CSV compliance exports — i.e., ~80% of the *mechanics* of J05/J04/J07/J10. The enterprise then
encodes state-by-state eligibility as workflow rules and keeps counsel sign-off in email/Jira.
Every Promotion OS sales conversation in this buyer base starts from "we already run
Socure/Persona/GeoComply and can build the rules ourselves." Secondary substitute: Alloy, which is
architecturally the same decisioning-over-200+-vendors play aimed at bank/fintech policy teams.

**Capabilities already commoditized** (do not build; integrate or ignore):
- Identity verification, document/selfie/liveness, age-verification *methods* (E01/E02): 4-level
  strength at Socure/Persona, orchestrated by GeoComply, plus a long tail (Jumio, Onfido, Veriff…).
- Watchlist/sanctions/PEP screening data and monitoring (Socure 1,400+ lists; Persona reports).
- KYC vendor waterfalls / multi-vendor orchestration behind one API (IDComply, Marketplace,
  Partner Ecosystem, Alloy) — J06's *identity* slice is a solved, competitive market.
- Allow/deny/review output models with reason codes; no-code workflow builders with versioning;
  case management with SLAs and queues; webhooks/sandboxes/RBAC/SSO. All three (plus Unit21,
  Sardine, Sumsub) ship these; they are table stakes, not differentiators.

**Capabilities partially covered** (real but incomplete somewhere material):
- Policy-version-to-decision provenance: Persona has true per-decision pinning; Socure has versions
  without documented decision linkage; GeoComply has nothing customer-visible. Nobody extends
  provenance to *all* policy artifacts (Socure's reason-code lists and watchlist policies bypass it).
- Impact analysis: Socure backtests (not exportable, sync-only); Persona does live splits only.
- Evidence packaging: GCI produces bank-accepted *fact* packages; Socure produces CSV compliance
  reports; Persona produces PDFs + SAR e-filing. None produces a regulator package joining facts +
  policy version + human approvals + legal citation.
- Jurisdiction rules: GeoComply ships real jurisdiction rule *content* — but only for
  geolocation/KYC dimensions, only as an opaque managed service, only where mandates exist.
- Temporal semantics: recurring re-screening exists (Persona 1–365-day monitoring); effective-dated
  policy activation exists nowhere (verified absent at Socure; C04 ≤1 or ? everywhere).
- Human governance: case-level approvals are strong everywhere; config-level approvals exist nowhere.

**Apparent gaps** (absent across all three, verified where checkable):
1. Counsel-as-approver / legal-to-production deployment workflow (C08, J02, J03 ≤1 everywhere; no
   maker-checker on publishing exists in any of the three — verified at Persona and Socure docs).
2. Legal-source provenance and machine-readable legal policy libraries (C09: ?/0/1; C10: 0/1/1).
   Socure documents its refusal in writing; Persona deliberately avoids legal claims; GeoComply
   keeps the content proprietary and unexposed.
3. Regulatory change monitoring as a product (C06 ≤2): GeoComply does it as an internal service
   (Gov Relations team), Socure only detects watchlist-data changes, Persona publishes blog posts.
4. Effective-dated policy + as-of-date decision replay (C04/J08): forward-only semantics everywhere.
5. Statute-linked decision reasons ("denied under NJ rule X, version Y, approved by Z"): no vendor
   can emit this; reason codes are operational, not legal.
6. The regulated *action* domain itself: A-row and F-row are ~0 across all three. All object models
   orbit identities; none models a promotion, entry, prize, wager-bonus, or entitlement.
7. Neutral cross-vendor normalization ABOVE these vendors: each normalizes only its own partner set;
   nobody normalizes GeoComply+Socure+Persona+Xpoint signals under one policy layer — newly relevant
   since the patent invalidation made multi-geo-vendor strategies real.

**Gaps probably too small to monetize alone:**
- A formal "review" output state for geolocation checks (GeoComply B04 gap) — operators handle it.
- Longer forensic log retention windows (Persona's 2wk/30d/6mo) — a feature request, not a product.
- Config-as-code / IaC / full config export (H09/H10 weak everywhere) — dashboard-first is accepted
  in this buyer base; valuable only as part of a larger governance story.
- Idempotency/SLA documentation gaps; backtest-result export (Socure) — roadmap items the incumbents
  will close incidentally.
- Standardized reason-code taxonomy across vendors — real annoyance, no standalone budget.

**Gaps worth passing to synthesis** (each is absent in all three AND survives the "would the
incumbent just add it?" test because it conflicts with their model or DNA):
1. **Counsel-governed policy lifecycle** (J02+J03+C08): approval-gated, evidence-logged
   legal-to-production deployment. Persona/Socure could add approval gates in a quarter — but the
   *counsel semantics* (attestation, citation, defensibility record) are an editorial/legal-ops
   muscle none has; GeoComply's model actively resists exposing the pipeline.
2. **Jurisdictional legal content as maintained, provenance-linked, executable product**
   (J01-content + C09 + C10 + C06): Socure has declared neutrality in its docs; Persona avoids
   legal claims; GeoComply monetizes the content by keeping it opaque. This is the deepest and most
   defended-by-refusal gap in the category.
3. **Effective-dated policy + as-of replay for regulator defense** (C04 + J08 + D03 hardening):
   even the best-in-category implementation (Socure) has verified audit-bypassing edit paths and
   fresh-logic-only re-evaluation. "Show me the rule as of March 12 and re-run the decision" is
   answerable by no one.
4. **Evidence-grade regulator package joining facts + policy version + approvals + legal authority**
   (J07 full): GeoComply proves evidence productization sells (GCI, 70+ processors) — but only for
   facts. The decision-logic half of the package is unowned.
5. **Cross-vendor signal + policy normalization above the incumbents** (J06 generalized): a neutral
   layer normalizing geo/identity/fraud vendors *and* applying one versioned policy across them —
   attractive precisely because each incumbent's normalization stops at its own walled garden.
6. **Regulated-action authorization for non-identity domains** (J05 beyond identity + A/F-row
   adjacency): the decision subject everywhere is "this person"; nobody authorizes "this promotion
   / this incentive / this entitlement in this jurisdiction." Identity platforms' pricing
   (per-verification/attempt) and object models are structurally wrong for it.

---

## 4. Internal-build / stack-substitute assessment

**Question: is "Persona or Socure (or GeoComply) + internal engineering + counsel" already a
credible assembly of the J01–J10 hypothesis for a regulated-commerce enterprise?**

**Answer: credible for the rails (roughly J05 mechanics, J06 identity-slice, and the operational
halves of J04/J07/J10); not credible for J01–J03, J08, J09, or the evidence/content layer — those
remain manual, and the manual versions are exactly the pain the hypothesis targets.** Square by
square:

- **J01 (regulatory rules as executable product):** Half-buildable. On Socure, state eligibility
  rules become Decision Rules over custom fields; on Persona, Workflow conditionals + country/geo
  Lists. But the *content* — knowing what the rule is, per jurisdiction, per product type, kept
  current — is supplied by counsel memos and encoded by engineers with no provenance link. GeoComply
  ships real content but only for geolocation/KYC and only as a black box. The build produces
  executable rules; it does not produce *regulatory* rules with maintenance and citations.
- **J02/J03 (legal-to-production workflow, counsel-as-approver):** Not buildable on any of the
  three; only emulatable. Verified: no publish-approval workflow exists at Persona or Socure;
  Move-to-Live/publish rights can be restricted to a compliance role, but there is no attestation
  record, no draft-diff review artifact for counsel, no evidence chain from legal opinion to live
  policy. Enterprises bridge this with email/Jira/DocuSign — undocumented in the decision system,
  which is precisely the audit weakness.
- **J04 (impact analysis):** Buildable on Socure (historical backtests + shadow experiments are
  genuinely strong; limits: async workflows untestable, results not exportable, no regulatory
  framing such as "impact of the NY rule change"). Weakly buildable on Persona (live %-rollouts
  only). Unknown on GeoComply.
- **J05 (cross-product action authorization):** Substantially buildable on Socure for identity-gated
  actions — the evaluation API is synchronous, takes arbitrary custom JSON, and returns
  allow/deny/review with reasons. Persona can model arbitrary actions as Transactions but decisions
  are async (~5s, poll/webhook) — disqualifying for in-transaction gating. GeoComply already *does*
  this across an operator's whole product line, but only on the location/identity/fraud dimension
  and only in mandate-driven verticals. Caveats that keep this "substantial" rather than "solved":
  attempt-based/per-verification pricing is economically wrong for high-volume non-identity
  authorization calls, and custom fields are second-class (Socure: stored not indexed; ≤20–25
  recommended).
- **J06 (cross-vendor signal normalization):** Already sold to them three ways (IDComply waterfall,
  Persona Marketplace, RiskOS Partner Ecosystem + reseller contracting). What no vendor sells:
  normalization across *competing* platforms (e.g., GeoComply + Xpoint + Socure under one policy),
  which is exactly what a multi-vendor procurement strategy post-patent-invalidation wants.
- **J07 (evidence-grade reconstruction):** Partially buildable, with verified holes an internal team
  cannot patch from outside: Socure's unversioned reason-code-list edits and missing
  decision→version linkage; Persona's 2-week API-log window; GeoComply's absent rule provenance.
  The enterprise ends up warehousing decision payloads itself — an internal build of exactly the
  proposed product's evidence layer.
- **J08 (as-of replay):** Not buildable on any vendor. Requires the enterprise to snapshot policy
  and inputs itself and maintain a replay harness — nobody does this well.
- **J09 (policy packs):** Not buildable — packs without legal content are templates; each enterprise
  re-derives the same NJ/NY/CA rules with its own counsel. (This duplication across enterprises is
  the network-effect opening.)
- **J10 (lifecycle control plane):** The config-lifecycle half exists (Persona best-in-class
  versioning; Socure lifecycle + AI change summaries). The regulatory half (obligations →
  policies → approvals → deployments → evidence, with effective dates) exists nowhere; OneComply is
  the closest cousin and it does *licenses*, not policies.

**Who can actually execute the assembly:** FanDuel/DraftKings-scale operators and top-20 banks
demonstrably do (in-house rules engines wired to GeoComply/Socure outputs — documented pattern).
Mid-market regulated commerce (retail promotions, fintech incentives, gaming-adjacent consumer
brands) generally cannot: no counsel-workflow tooling, no replay, no content maintenance. **The
substitution threat is therefore real at the top of the market and weak in the middle — the wedge
must be the content + counsel-governance + evidence layers, because the decisioning rails are
already owned by this category and will not be displaced.**

---

## 5. Adjacent competitor appendix

Deduplicated across the three reports (12 named by agents, consolidated; 1 manager addition).
**Bold = material to the landscape.**

| Competitor | Relevance | Material? |
|---|---|---|
| **Alloy** | Named in all 3 reports. Identity-risk decisioning/orchestration over 200+ data vendors with policy workflows for banks/fintechs; the closest architectural analog to the proposed decisioning layer and a Socure/Persona substitute at the policy tier. | **Yes — the fourth incumbent this category analysis must assume.** |
| **Sardine** | Named in 2 reports. Device/behavior-first fraud + compliance with rules engine, case management, AI agents; closer to synchronous transaction-time risk decisioning than Persona. | **Yes** — competes directly with RiskOS-style unified decisioning. |
| **Unit21** | Named in 2 reports. No-code fraud/AML risk-ops (rules + alerts/cases + SAR e-filing); proves non-engineer rule authoring and regulator-filing workflows are already productized. | **Yes** — substitutes the Workflows/Cases slice. |
| **Sumsub** | Named in 2 reports. Full-cycle verification + workflow builder + case management, aggressive per-country compliance packaging (country-specific KYC/age presets). | **Yes — flag for synthesis: the closest existing behavior to "regulatory content + decisioning" in one product.** Its packs are still technical presets, not provenance-linked legal content, but it is the vendor most likely to cross that line; verify depth before treating gap #2 as open in its geographies. |
| **Xpoint** | Geolocation-compliance competitor that invalidated GeoComply's patent (affirmed Fed. Cir. 2024); proves the geo signal layer is legally contestable and multi-vendor. | **Yes** — enables the neutral-policy-layer play (gap #6/J06). |
| **Radar** | Developer-first geofencing entering gaming geo-compliance with MTU pricing and self-serve DX (Sleeper, Fliff, Everi); the "modern DX + transparent pricing" attack vector against GeoComply. | **Yes** — validates the buying motion a new entrant would use. |
| **Vixio** (GamblingCompliance) | Regulatory-change monitoring / obligation intelligence for gambling & payments — the content half (C06/J04) as data, with no decisioning. | **Yes** — natural content supplier, partner, or acquisition in any policy-lifecycle play; its existence shows content and decisioning are sold separately today. |
| Trulioo | Global KYC/KYB orchestration; IDComply substitute outside gaming; commodity pressure on E-row. | Secondary. |
| LocationSmart | Carrier/IP location verification; lower-assurance geo substitute. | Secondary. |
| Footprint (onefootprint.com) | Newer IDV + onboarding with rules playbooks + vaulting; evidence the configurable-verification pattern is commoditizing downmarket. | Secondary. |
| Middesk / SentiLink / Prove / Mastercard Identity / LexisNexis | Signal suppliers inside Persona/Socure marketplaces; simultaneously partial substitutes for specific slices. | Secondary (supply side). |
| Jumio / Onfido / Veriff / IDnow / Shufti / ComplyCube / iDenfy / Ondato | Commodity IDV cross-shop set from Socure buyer research. | No — commodity tier. |
| Taktile *(manager addition — not in agent reports; flagged for verification, not evidence-backed this session)* | Horizontal risk-decisioning platform (versioned policies, A/B testing, data marketplace) sold to fintech credit/fraud teams; if Manager B's category doesn't cover it, synthesis should — it is the generic-decision-engine substitute with no identity data moat, i.e., the closest thing to "Promotion OS minus regulatory content." | Flag for synthesis to place (B or C). |

Landscape-changing note: **no competitor found by any of the three agents combines maintained,
provenance-linked regulatory content with decisioning and counsel workflow.** Sumsub (packaging)
and Vixio (content) each hold one piece; Alloy/Sardine/Unit21/Taktile hold rails only. Gap list in
Section 3 stands after dedup.

---

## 6. Approval line

REPORTS APPROVED: 09_geocomply.md, 10_persona.md, 11_socure.md
