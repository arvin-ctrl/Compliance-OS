# Manager B — Category Summary: Incentive & Loyalty Decisioning

Manager: Category Manager B (Incentive & Loyalty Decisioning)
Date: 2026-08-18
Reports reviewed: `outputs/company_reports/06_talonone.md`, `outputs/company_reports/07_voucherify.md`, `outputs/company_reports/08_openloyalty.md`
Evidence reviewed: `outputs/evidence/06_talonone.jsonl` (42 records), `outputs/evidence/07_voucherify.jsonl` (41 records), `outputs/evidence/08_openloyalty.jsonl` (47 records)

Verification method: every 3/4 score audited against its cited evidence records; suspicious 0s spot-checked; six independent WebFetch verifications of linchpin sources (Adyen acquisition page; Voucherify approval-requests doc; Voucherify docs security page + docs index; Talon.One revising-campaigns doc; Open Loyalty add-transaction doc; Open Loyalty fortune-wheel probability doc). All fetches succeeded and matched the reports' characterizations except where noted.

---

## 1. QC review per report

### 06 — Talon.One — **APPROVED WITH CORRECTIONS** (4 score normalizations)

**Verification performed.**
- WebFetch of `docs.talon.one/docs/product/campaigns/revising-campaigns` confirmed the report verbatim: Revised/Pending states, testing-API-key auto-dry requests, immediate or scheduled finalization, permission-gated "Request Finalization" → admin email, **no revision-history view**, and — an important governance hole the report correctly captured — changes to coupons, referrals, stores, and achievements **bypass revisions entirely** and apply to live campaigns immediately.
- WebFetch of the Adyen knowledge-hub page confirmed completion 2026-07-01 and the stated integration thesis ("combine Adyen's global payments infrastructure and proprietary transaction data with Talon.One's real-time decisioning capabilities... dynamically adjust promotions and pricing based on who the consumer is"). **No mention of compliance, regulation, or legal workflows anywhere in Adyen's stated plan.** The €750M figure and announcement date rest on multiple corroborating sources per the ledger note; accepted.
- All B-row 3/4s trace to official-doc evidence (Integration API effects, Talang, evaluation order). B03=3 correctly withholds a 4 because latency/uptime figures are marketing-grade (TALONONE-022, MEDIUM) — docs-over-marketing resolution done properly by the researcher.
- The A-row and C/E-row 0s rest on labeled enumeration inference (documented feature catalog + the telling financial-services industry page showing zero regulatory functionality for regulated-industry customers). Sound.

**Challenged claims / corrections.**
1. **D03=2 and C05=2 depend on an unlabeled-as-guarantee inference the report does label but synthesis must not miss:** the effect→`rulesetId` linkage and ruleset-retrieval endpoints are documented, but **ruleset immutability is inference, not documented behavior** (TALONONE-039). This is the only decision→policy-version linkage primitive in the entire category and it rests on an undocumented retention/immutability assumption plus contract-bound log retention. Scores stand; the caveat is flagged as load-bearing.
2. **C03 0→1.** Cross-report convention: Voucherify received C03=1 for generic action-scoped rule mechanics (redemption-context rules) with no legal semantics. Talon.One's rules scope to session/event action types the same way. Same substrate, same score.
3. **D01 1→2.** Sessions/events are stable-ID entities whose triggered effects are displayed per event in documented Sessions/Events views (TALONONE-036), beyond raw API logs. Comparable to Open Loyalty's execution-record D01=2. No immutability claims (true of all three vendors).
4. **H06 2→1.** Idempotency-Key exists on exactly one endpoint since March 2026, explicitly "a first step" (TALONONE-024). One endpoint is minimal, not "meaningful but incomplete"; Voucherify's session-lock-only protection scored 1 — parity.
5. **J03 0→1.** Verified: finalization is permission-gated and non-permitted users must request finalization from a named admin. An enterprise can configure "only legal holds finalization permission" — the same configurable approver-analog substrate that earned Voucherify J03=1. Neither vendor has counsel semantics or attestation; both are 1.

**Inference hygiene:** good — I08, D03 immutability, absence inferences, and post-Adyen roadmap speculation are all explicitly labeled. Marketing-vs-docs contradictions (latency, uptime) resolved toward docs.

### 07 — Voucherify — **APPROVED WITH CORRECTIONS** (1 score normalization)

**Verification performed.**
- WebFetch of `docs.voucherify.io/manage/approval-requests.md` confirmed the category's strongest approval feature exactly as reported: gates creation/updates of campaigns, vouchers, **and validation rules**; approvers must be Admin users; up to 5 approvers but **one approval suffices**; five statuses; new objects hidden and updates unapplied until approved; Enterprise-only. Also confirmed the report's gaps: **no approval-history retention documented, no API support documented, no counsel/legal role.** G04=3, C08=2, D05=2 stand.
- WebFetch of the docs index (`llms.txt`) plus `docs.voucherify.io/guides/security.md` resolved the one place the researcher was arguably *too conservative on evidence class*: the report scored G10=3 citing only marketing pages, but an official **docs** security page exists stating "ISO-27001-certified product" plus AES-256 at rest/TLS 1.2, third-party penetration tests, PCI scans, WAF/DDoS, daily cross-account backup snapshots. **G10=3 is confirmed on docs-grade evidence** (still no SOC 2 anywhere — consistent). G03=2 also stands: the SAML mention on the security page concerns internal access controls; customer SSO configuration docs remain unlocated.
- B-row 4s (qualifications/validations/redemptions) trace to deep official API docs including the honest caveats: qualification returns no ineligibility reasons, ignores several budget rules, and caches 5 minutes; geofencing is coordinate-based, merchant-supplied, and **fails open** ("If no location is sent, geofencing rules are skipped") — all documented, all correctly carried into scoring.
- The marketing claim "Full audit trails log every decision for compliance" (VOUCHERIFY-035) was correctly overridden by docs: validations retained 30 days, API logs 6–12 months, no policy-version linkage on the decision record, no integrity guarantees. Exemplary docs-win resolution.

**Challenged claims / corrections.**
1. **E03 1→0.** Storing merchant-supplied, unverified addresses is not address verification. Talon.One and Open Loyalty both store addresses and both scored 0. Category convention (applied consistently in section 2): E-row verification squares score verification capability; unverified declared-attribute *gating constructs* score at most 1 (Voucherify keeps E02=1 for documented birthdate/audience gating and E04=2 for the real geofencing feature); bare storage scores 0.
2. Noted, not overridden: F08=3 and F02=3 rest partly on a support article retrieved via snippets (VOUCHERIFY-026, MEDIUM); content is corroborated by the List Voucher Transactions API. F10=1 is arguably a point conservative given webhooks + Kafka connectors + transaction exports; left standing (does not affect category conclusions). B09=2/G06=2 vs Talon.One's 3s is a real capability difference, not inconsistency: Voucherify has no dry-run mode, no time-travel parameter, and no way to test a draft rule against production data — its "simulation" is sandbox QA plus live qualification probes.

**Inference hygiene:** good — idempotency absence, I08/I09, and replacement-risk reasoning labeled as inference; retention numbers and schema gaps documented positively.

### 08 — Open Loyalty — **APPROVED WITH CORRECTIONS** (12 score normalizations)

**Verification performed.**
- WebFetch of the add-transaction guide confirmed the report's central architectural claim: the API response acknowledges ingestion and campaign effects apply **asynchronously**, surfaced via the `CampaignEffectWasApplied` webhook. There is no decision in the request path. This validates the B02=1/B04=0/J05=0/J10=0 cluster — these 0s are *architecture-precludes* 0s, exactly what the matrix rules require, and they are approved as scored.
- WebFetch of the fortune-wheel probability doc confirmed A03=3: genuine native instant-win mechanics (independent per-spin probability with a "Business Logic Layer that overrides the probability engine" blocking wins on inventory/budget/member limits) and — a finding for synthesis — **zero mention of odds disclosure, official rules, or sweepstakes law** around a chance-based prize mechanic marketed with "lotteries" on the homepage.
- The report's 0-scoring method (OPENLOYALTY-043: full sitemap enumeration of 238+67+302 doc pages, labeled inference) is the most rigorous absence methodology of the three reports.

**Challenged claims / corrections.** The blanket-absence method, while rigorous about *product features*, produced systematic inconsistency with how the other two reports credited **generic configurable substrate** at score 1. Normalized (all with the same logic — same substrate class, same score as peers):
1. **E02 0→1** — age-range segment conditions are documented (OPENLOYALTY-033); same declared-data age-gating substrate as Voucherify's E02=1.
2. **E04 0→1** — `customer.address.country/province/postal` in expressions, country/city/postal segment conditions, per-country tenants (OPENLOYALTY-008/-019/-033); same customer-supplied-location-in-rules substrate as Talon.One's E04=1.
3. **E07 0→1** — campaign frequency caps, unit budgets, fortune-wheel win limits (OPENLOYALTY-006/-035) are the same deterministic anti-abuse control class scored 1 at both peers.
4. **E10 0→1** — admin-defined custom event schemas + webhooks (OPENLOYALTY-045/-042) can carry third-party signal payloads as data, the substrate credited 1 at both peers.
5. **J01 0→1** — Symfony-expression rules over country/consent/tier attributes are as customer-authorable into pseudo-regulatory rules as Talang or validation rules, both scored 1.
6. **J04 0→1** — the campaign simulator is a documented pre-go-live testing feature (OPENLOYALTY-009), the same peripheral-substrate class as Talon.One's dry requests (J04=1). Voucherify stays J04=0 — it genuinely has no pre-rollout what-if capability.
7. **J06 0→1** — same reasoning as E10.
8. **H10 0→1** — API-manageable configuration plus per-module config exports (OPENLOYALTY-037/-021) equals Talon.One's H10=1 substrate.
9. **G02 3→2** — documented ACL has exactly two permission levels (View/Modify) and roles are global, not tenant-scoped (OPENLOYALTY-019/-021); materially below the peers' 3-grade RBAC (Talon.One: role templates + campaign access groups with four permission levels; Voucherify: per-project roles + custom roles).
10. **G08 4→3** — webhook retry policy and delivery guarantees are undocumented (noted in OPENLOYALTY-013); Voucherify's fully documented delivery contract (HMAC + 12 retries/24h backoff + auto-disable + monitoring) scored 3. A 4 with undocumented delivery semantics on the channel that *carries the product's decisions* is unsupported.
11. **H03 4→3** — same evidence, same reasoning as G08.
12. **I05 4→3** — the enterprise roster (JTI 18 countries, BAT two continents, ALDO, banks/insurers) is real but "100+ enterprise brands" is marketing; parity with Voucherify's comparable roster at 3. Category-leading 4 is reserved for Talon.One's tier (300+ merchants incl. Adidas/Sephora/Nordstrom, €750M acquisition validation).

Also noted, not overridden: D02=3 stands on content richness (execution records carry triggering `contextData` and per-effect results — the richest decision-record raw material in the category) but synthesis should know delivery is **daily batch to customer storage**, not on-demand query. G09=3 stands despite the documented 99.9%-docs vs 99.99%-marketing SLA discrepancy (docs number still supports 3; discrepancy recorded by the researcher — docs win).

**Inference hygiene:** excellent — the strongest labeling discipline of the three reports.

### Cross-report consistency findings (normalization rationale)

1. **The synchronous decision path is real at exactly two of three vendors, and the scores now reflect it.** Talon.One (session update → effects inline, verified docs) and Voucherify (qualify→validate→redeem with statuses/reason keys, verified docs) are genuine synchronous authorizers of incentive actions — B01/B02=4 justified at both. Open Loyalty is an **async fulfillment engine**: it cannot gate anything in the request path; its only synchronous evaluation is a single-member simulator. The researchers did not falsely equalize these — the async distinction was correctly carried through B02–B05, J05. No normalization needed on the sync cluster itself.
2. **Terminology normalized for synthesis:** (a) "approval workflow" in this category always means *configuration-change maker-checker*, never decision-path review — no vendor has a review/hold verdict state; (b) "audit log" means three different things — Talon.One: config-change log (+ separate Integration API traffic logs); Voucherify: API-traffic log capturing decision requests/responses; Open Loyalty: admin/member *action* log (decision records live in batch exports instead); (c) "simulation" everywhere means single-scenario dry-run — **no vendor can replay historical traffic or evaluate a rule change against historical decisions**.
3. **Convention applied for E-row and J-substrate scoring** (stated above under Voucherify #1 and Open Loyalty #1–7) so that identical substrate earns identical scores across all three reports.

---

## 2. Score normalization block

```csv
company,square,agent_score,normalized_score,reason
Talon.One,C03,0,1,"consistency: Voucherify scored 1 for generic action-scoped rule mechanics without legal semantics; Talon.One rules scope to session/event action types identically (TALONONE-004/-014)"
Talon.One,D01,1,2,"sessions/events are stable-ID entities with per-event effect records in documented Sessions/Events views (TALONONE-036); parity with Open Loyalty execution-record D01=2; immutability unclaimed at all vendors"
Talon.One,H06,2,1,"Idempotency-Key on one endpoint only, shipped 2026-03 as explicit first step (TALONONE-024); minimal, parity with Voucherify=1 (session locks only)"
Talon.One,J03,0,1,"verified: finalization is permission-gated with Request Finalization flow (TALONONE-013); configurable approver-analog substrate identical in class to Voucherify approval requests scored J03=1; neither has counsel semantics"
Voucherify,E03,1,0,"storing merchant-supplied unverified addresses is not address verification; Talon.One and Open Loyalty equivalent storage scored 0; convention: verification squares require verification capability"
Open Loyalty,E02,0,1,"age-range segment conditions documented (OPENLOYALTY-033); same declared-data age-gating substrate as Voucherify E02=1"
Open Loyalty,E04,0,1,"country/province/postal expression + segment conditions and per-country tenants (OPENLOYALTY-008/-019/-033); same substrate as Talon.One E04=1"
Open Loyalty,E07,0,1,"campaign caps, unit budgets, win limits (OPENLOYALTY-006/-035) are the deterministic anti-abuse class scored 1 at both peers"
Open Loyalty,E10,0,1,"custom event schemas + webhooks can carry third-party signals as data (OPENLOYALTY-045/-042); substrate credited 1 at both peers"
Open Loyalty,G02,3,2,"ACL has only View/Modify levels and roles are global not tenant-scoped (OPENLOYALTY-019/-021); materially below peers' 3-grade RBAC"
Open Loyalty,G08,4,3,"webhook retry/delivery guarantees undocumented (OPENLOYALTY-013 note); Voucherify's fully documented delivery contract scored 3; 4 unsupported"
Open Loyalty,H03,4,3,"same evidence and reasoning as G08"
Open Loyalty,H10,0,1,"API-manageable config + per-module configuration exports (OPENLOYALTY-021/-037) equals Talon.One H10=1 substrate"
Open Loyalty,I05,4,3,"real enterprise roster but '100+ brands' is marketing; parity with Voucherify roster at 3; category-leading 4 reserved for Talon.One tier"
Open Loyalty,J01,0,1,"expression engine over country/consent/tier attributes is customer-authorable substrate; parity with Talon.One/Voucherify J01=1"
Open Loyalty,J04,0,1,"documented pre-go-live campaign simulator (OPENLOYALTY-009); same peripheral-substrate class as Talon.One dry requests J04=1"
Open Loyalty,J06,0,1,"same substrate reasoning as E10"
```

17 overrides total (Talon.One 4, Voucherify 1, Open Loyalty 12). All other scores across the three reports are approved as submitted; downstream synthesis should apply agent scores plus these overrides.

---

## 3. Category analysis

**Strongest incumbent: Talon.One.** Deepest synchronous decisioning stack (inline session evaluation, Talang generic expression engine, evaluation-order/stacking control, budgets), the category's best change-safety tooling (staged revisions with auto-dry testing keys, time-travel dry runs, scheduled finalization, range-locked templates), the only decision→rule-version linkage primitive (rulesetId-stamped effects), best enterprise trust posture (SOC 2 Type II + ISO 27001, SAML/SCIM, per-customer VPC), and the largest proven enterprise base — now with Adyen's balance sheet and merchant distribution behind it.

**Most dangerous substitute: the pattern "incumbent engine + internal engineering + counsel kept offline" — instantiated most powerfully by post-Adyen Talon.One, and most cheaply by Voucherify.** Talon.One is the strongest total-capability substitute for the enforcement half of the wedge, and Adyen materially raises that threat on two axes: distribution (bundled into payments contracts at the exact transaction moment a Promotion OS would authorize) and data (payment-verified consumer identity partially closing the verified-signals gap for incentive use cases — Adyen's stated thesis is "dynamically adjust promotions and pricing based on who the consumer is"). At the same time the acquisition *lowers* the probability Talon.One itself builds the counsel/evidence layer: Adyen's stated integration plan contains no compliance ambition at all (verified), and the roadmap now points at transaction economics. Voucherify is the substitute that most directly undercuts the wedge's *governance narrative*: it is the only vendor in the category with a documented approval workflow gating rules, an API-call-level audit log capturing decision traffic, public pricing, and a self-serve trial — the cheapest path for an enterprise to tell counsel "we already have approvals and an audit trail."

**Capabilities already commoditized** (no differentiation available; at least two vendors at 3–4 with docs-grade evidence): synchronous rule evaluation APIs over arbitrary custom attributes with stateful customer context (B01/B02/B06/B07); budget/limit guardrails, stacking and priority/conflict resolution (B08); deny-reason codes scoped to domain objects (B05); wallet/points/gift-card ledgers with expiration regimes, promotion-linked credits, and redemption eligibility (F01–F05, F07); multi-tenant/multi-brand/multi-market scoping (G01); sandbox/staging environments and single-scenario simulation (G05/G06/B09); RBAC + SSO baseline (G02/G03); webhooks (G08/H03); public APIs, SDKs, versioning, documented rate limits (H-row); config-change audit logging (D02-as-ops-log).

**Capabilities partially covered** (present, but stopping short of the regulatory job): configuration-change approvals (Voucherify 3 / Talon.One 2 / Open Loyalty 0 — admin semantics, one-approver-suffices, no attestation, undocumented approval-history retention, and Talon.One's revision pipeline has verified bypass paths for coupons/referrals/stores/achievements); decision logging with input capture (all three) **without policy-version binding** (only Talon.One links decisions to a rule-version ID, and its immutability is inference); historical policy state (Talon.One rulesets + audit archaeology; Voucherify/Open Loyalty audit archaeology only, retention-bounded); temporal validity windows (C04 — commercial scheduling, not legal effective-dating); geographic scoping (per-country Applications/projects/tenants; Voucherify geofencing is real but trusts client coordinates and fails open); raw data exports (D07 — no regulator packaging anywhere); retention (contractual at Talon.One, fixed 30-day/6–12-month windows at Voucherify, undocumented at Open Loyalty — never a customer-controlled evidence policy).

**Apparent gaps** (absent across all three, with positive evidence of absence): a review/hold verdict state and human-adjudication queue in the decision path; decision↔policy-version binding as a product guarantee; tamper-evidence/log integrity (D09 unresolved at all three — no vendor even claims it); counsel-as-approver semantics, attestation records, and legal sign-off models; legal content, legal-source provenance, machine-readable policy libraries, and regulatory change monitoring (C06/C09/C10 = 0 across the category); population-level impact analysis of a rule change (all simulation is single-scenario); decision replay against historical rules (B10=1 everywhere); verified identity/age/location signals (every vendor consumes integrator-declared attributes; the category's one location feature fails open); a cross-product/cross-market single decision plane (Application/project/tenant isolation is structural at all three); regulator-facing evidence export.

**Gaps probably too small to monetize alone:** idempotency and API-hygiene gaps (Talon.One is already shipping it incrementally); webhook delivery-contract polish; a revision-history/version-diff UI (a feature vendors will ship, not a product); richer reason codes; approval-workflow polish (Voucherify already sells approvals as an enterprise add-on — an incremental feature for them, not a wedge for anyone else); simulation ergonomics; export/reporting tooling.

**Gaps worth passing to synthesis** (see the pass-list at the end of section 4 for the internal-build framing):
1. **Evidence-grade decision reconstruction** — decision records immutably bound to policy version + input facts + approval lineage, with customer-controlled retention and integrity guarantees. No vendor has it; none shows groundwork; the closest primitive (Talon.One rulesetId) rests on undocumented immutability and contract-bound retention.
2. **Allow/deny/REVIEW verdict model for regulated actions** — no review state exists anywhere in the category, and the one async vendor's architecture precludes it. Everything is binary-plus-skip, scoped to incentive objects.
3. **Counsel-approver lifecycle above engines the buyer already owns** — the category proves maker-checker demand (Voucherify monetizes approvals as an enterprise gate; Talon.One gates finalization by permission), but everything stops at admin semantics: no counsel role, no attestation, no quorum/sequenced sign-off, no approval-history guarantees, documented bypass paths.
4. **Verified-signal normalization (J06)** — all three engines structurally *trust* integrator-supplied identity/age/location data; fail-open geofencing is the emblematic weakness. Post-Adyen, payment-verified identity may close part of this gap for incentives specifically — synthesis should treat J06 as narrowing at the payment moment but open everywhere else.
5. **Maintained jurisdiction/policy content packs (J09/C10)** — pure whitespace: template/duplication mechanics exist at all three, content operations at none.
6. **Cross-silo authorization plane (J05 beyond incentives)** — per-country Applications, isolated projects, per-country tenants mean even the incumbent stacks cannot give one answer across brands/markets/products without duplicating rules.
Supporting demand datapoint for synthesis: Open Loyalty ships native chance-based prize mechanics ("fortune wheels," "Scratch & Win," "lotteries") with — verified — zero legal apparatus (no odds disclosure, official rules, or drawing certification anywhere in its docs), while Voucherify explicitly delegates chance UX to partners (Wyng/Brame/Odicci). Incentive engines are drifting into promotion-law-exposed territory with no compliance surface, which is evidence the pain the wedge targets is being actively created.

---

## 4. Internal-build / stack-substitute assessment

**Question:** can this category's buyers (enterprise marketing/loyalty/digital orgs with strong platform engineering — the Adidas/Trainline/JTI class) cover J01–J10 with these vendors + internal engineering + counsel?

**What is genuinely coverable today (the credible substitution):**
- **J05 mechanical core, incentive-shaped actions only.** Talon.One or Voucherify already provide synchronous allow/deny with reasons, stateful context, budgets, and guardrails for any action expressible as a coupon/discount/points/redemption decision. Encoding jurisdiction constraints is straightforward: per-country Applications with range-locked templates (Talon.One) or metadata validation rules + Areas & Stores scoping (Voucherify), gated on customer-supplied eligibility attributes. This is the real, existing substitute — and it caps willingness-to-pay wherever the regulated action *is* an incentive.
- **J02-lite.** Voucherify approval requests (rules + campaigns gated, hidden until approved) or Talon.One permission-gated finalization with staged, auto-dry-tested revisions gives a defensible "no unreviewed change ships" story at SOX-ops grade, with counsel participating as an Admin approver by convention.
- **Fragments of J07/J08.** Talon.One: rulesetId-stamped effects + Integration API request/response logs + config audit log. Voucherify: permanent redemption records + 6–12-month API-call audit log. Open Loyalty: daily execution/effect exports with triggering context into the customer's own warehouse. An internal team can archive these into an evidence lake before retention lapses.

**What remains a net-new internal build, per J-square, and why it rarely gets built:**
- **J01 (regulatory rules as versioned product):** rule *authoring* is easy; rule *content and maintenance* is a standing legal-operations function. No vendor supplies content, provenance, or updates; counsel must hand-translate law into Talang/validation-rule/expression constructs per market, forever. Nobody's roadmap moves here (Talon.One → Adyen payments thesis; Voucherify → Vincent AI offer optimization; Open Loyalty → gamification).
- **J02/J03 full:** counsel semantics, attestation, quorum, and durable approval history do not exist. Voucherify's one-approver-suffices model and Talon.One's revision bypass paths (verified) mean the enterprise must build policy *around* the tool and cannot prove sign-off *from* the tool.
- **J04:** no population-level impact analysis exists anywhere; internal build = replaying warehouse data against re-implemented rule logic — i.e., building a second rules engine to test the first.
- **J06:** engines accept whatever attributes the integrator sends; verification means buying IDV/geo/device vendors and piping results in as metadata — feasible, but the *engine* provides no normalization, no signal provenance, and fails open (Voucherify geofencing, documented).
- **J07/J08 evidence-grade:** the binding problem is unsolved — Voucherify decision records reference no rule version at all; Open Loyalty has no config versioning; Talon.One's linkage relies on inferred ruleset immutability. Retention is contractual or fixed. Replay does not exist. An internal build must intercept/wrap every decision call, snapshot config, and store both immutably — a real system, owned by nobody (marketing owns the engine; legal owns no engineers).
- **J09/J10:** template/duplication mechanics ≠ maintained packs; no lifecycle control plane exists (Open Loyalty has no approvals at all; none have counsel lifecycle).
- **Cross-product J05:** Application/project/tenant silos are structural. Authorizing non-incentive regulated actions (account gating, prize award, age/geo-gated features) through these engines means abusing customEffect/webhook outputs (Talon.One), or cannot be done in-path at all (Open Loyalty, async — it would sit *behind* an authorization layer as fulfillment, per its own report, which I endorse).

**Verdict:** "Vendor + internal engineering" is a **credible substitute for incentive-only enforcement plus ops-grade change control — roughly the J05-mechanics + J02-lite slice — and that slice is enough to kill a thin version of the wedge** (any pitch reducible to "real-time rules with reasons + approvals + audit" loses to installed Talon.One/Voucherify). It is **not credible for the counsel/evidence/content/verified-signal layers (J01, J03, J04, J06, J07/J08 evidence-grade, J09, J10)**: those are net-new builds with continuing operating cost, owned by a buyer (legal/compliance) that has no engineering budget in these accounts. The realistic competitor synthesis must price against is therefore not these vendors but **inertia** — counsel-in-email + Jira + vendor guardrails currently passes most audits. The wedge must beat "good enough," and must position the incumbent engines as enforcement rails underneath it rather than trying to displace them.

---

## 5. Adjacent competitor appendix

Deduplicated from the three reports; **bold = materially changes the landscape.**

| Competitor | Found by | Relevance (one line) |
|---|---|---|
| **Adyen (post-acquisition parent)** | 06 | Payments-bundled, payment-verified-identity promotion decisioning at the transaction moment — the future default substitute for transaction-time incentive authorization; also narrows J06 for incentives. **Material.** |
| **Eagle Eye (AIR)** | 06, 07 | Proves real-time incentive authorization at physical-POS scale (Tesco/Woolworths/Carrefour; "1.7B offers/week"); the up-market execution substitute any decisioning claim must survive. **Material.** |
| **Antavo** | 06, 07, 08 | The no-code pole of the same enterprise loyalty/promotion decisioning budget (Gartner/Forrester-cited; KFC/PUMA/Hyatt); shows how crowded the engine layer is. **Material as crowding evidence.** |
| **Salesforce Loyalty Management** | 08 | Suite-bundled loyalty inside enterprise CRM — the bundling threat that compresses standalone engine pricing from above. **Material as bundling pressure.** |
| **commercetools native discounting** (and commerce-platform-native promo generally) | 06 | The build-adjacent free alternative inside commerce platforms; compresses the category from below. **Material as substitution floor.** |
| White Label Loyalty | 08 | Event-driven API-first loyalty engine (PepsiCo, Burger King EMEA); architectural twin of Open Loyalty — evidence the event-rules pattern is commoditizing. |
| Wyng / Brame / Odicci | 07 | Voucherify's chance-mechanic UX partners; the seam between incentive engines (this category) and promotion administration (category A) — where sweepstakes-law exposure enters stacks with no legal tooling. Worth a cross-category note, not a threat. |
| Braze (and CDPs/ESPs) | 06, 07, 08 | Engagement layer through which incentive decisions are distributed (Trainline stack; official Open Loyalty partner); complement and channel, not competitor. |
| Capillary Technologies | 06, 08 | Enterprise loyalty suite, APAC-strong; watchlist only. |
| Comarch Loyalty | 06, 08 | Legacy enterprise loyalty suite; watchlist only. |
| SAP Emarsys | 06 | Engagement suite absorbing promotion targeting; minor. |
| Punchh (PAR) | 06 | Vertical QSR loyalty; minor. |
| LoyaltyLion | 06 | SMB/ecommerce loyalty; not material. |
| Uniqodo | 06 | Promotion-code delivery/experience layer; not material. |
| Annex Cloud, TrueLoyal, Smile.io, Yotpo | 08 (third-party lists) | Alternative-list filler at or below mid-market; not material. |

No material competitor was found omitted by the agents; my addition is the explicit elevation of **Adyen itself** from a footnote in report 06 to a first-class landscape actor, per the verified acquisition thesis.

---

## 6. Approval line

REPORTS APPROVED: 06_talonone.md, 07_voucherify.md, 08_openloyalty.md
