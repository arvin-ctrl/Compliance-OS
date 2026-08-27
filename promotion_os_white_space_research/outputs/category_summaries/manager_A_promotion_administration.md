# Category Summary — Manager A: Promotion Administration

Manager: Category Manager A (Promotion Administration)
Date: 2026-08-18
Companies reviewed: Votigo (01), Sweeppea (02), Realtime Media/RTM (03), ShortStack (04), ViralSweep (05)
Inputs: `outputs/company_reports/01–05_*.md`, `outputs/evidence/01–05_*.jsonl` (36 + 43 + 38 + 33 + 41 = 191 evidence records)

---

## 1. QC review per report

QC method applied to all five reports: every 3/4 score traced to its cited evidence records; all 0 scores checked for positive-absence reasoning (none are "website didn't mention it" zeros); inference-vs-documentation labeling audited; marketing-vs-docs contradictions resolved with docs winning; 8 targeted verifications performed against official sources on 2026-08-18 (WebFetch of URLs already in the ledgers, plus one snippet-corroboration search where the source blocks automated fetch).

### 01 — Votigo

**Verification performed.**
- Fetched `votigo.com/technology/platform-features`: SOC 2 wording verified as the ambiguous mix the agent recorded — "SOC 2 Certified" alongside "SOC 2–compliant hosting and encrypted data storage"; no trust center or attestation path. The agent's cap at G10=2 (not 3) is correct; the contradicting privacy policy ("commercially reasonable" security, VOTIGO-030) was properly weighted.
- Fetched `votigo.com/legal-admin/winner-administration`: "Certified Random Number Generation", "Complete Audit Trails", "Independent Verification", W-9/1099 workflows, affidavits/releases/deadline tracking all verified verbatim, and the page's odd "$2,000" 1099 threshold is real (agent correctly flagged it as a service-framing signal). Everything on the page is a managed service performed by Votigo, not customer-operable software — confirming the report's modality caveat.

**Challenged claims and resolutions.**
- A-row 4s (A01–A05, A07–A09): rest on official service pages corroborated by operational artifacts — live official rules naming Votigo as Sweepstakes Administrator on a votigo.com subdomain (VOTIGO-003, official-doc), the Kraft Heinz case study (VOTIGO-023), and the acquired US Sweepstakes & Fulfillment administration business (VOTIGO-025). Equivalently strong to docs for *service* capabilities; upheld. "Certified" RNG is self-description (no external certifier named) — upheld at 4 for the vertical, noted for synthesis.
- **B03=2 challenged and downgraded to 1.** The cited evidence is a marketing "<1s Response" stat for Votigo's own fraud layer (VOTIGO-018, MEDIUM) and instant-win prize logic inside hosted flows; VOTIGO-036 itself concedes there is "no documented externally callable decision endpoint." A 2 ("meaningful but incomplete" low-latency production decisioning) is not supported; peers with equivalent in-flow evaluation scored 0–1. Normalized to 1.
- **I09=3 direction error, normalized to 1.** The agent used 3 to mean "integration burden is low"; ShortStack/ViralSweep/RTM scored the same square as intensity (higher = heavier burden). Normalized to the intensity convention.
- 0 scores (C10, J04, J05, J06, J08, J10): all labeled inference with architecture-based positive-absence reasoning (campaign-scoped API, empty public developer footprint, services delivery model). Upheld.
- Inference labeling: consistently disciplined (private-docs inference, environments inference, small-team inference all labeled). LOW-confidence GetLatka revenue/headcount figures are used directionally and flagged — acceptable.

**Status: APPROVED WITH CORRECTIONS** (2 score overrides).

### 02 — Sweeppea

**Verification performed.**
- Fetched the MCP validation README (`sweeppea-mcp-info`): the two-layer validation model verified exactly as reported — inviolable hardcoded legal guardrails (illegal lottery without AMOE, COPPA under-13, alcohol age gates) plus dynamic declarative rules **editable by Sweeppea only**, with structured rejection payloads (`blocked_by`, `error_code` e.g. `ALCOHOL_AGE_GATE_REQUIRED`, `error_message`, `rule_id` e.g. `age_gate_must_be_21_when_active_v1`). QC nuance the agent may pass to synthesis: the `_v1` suffix in rule ids shows embryonic *vendor-internal* rule versioning — still zero customer-facing policy lifecycle. No decision logs, replay, or audit records documented. B04=1/B05=1/J01=1 upheld.
- Fetched the entry-page tools doc: the report's single most load-bearing negative finding verified verbatim — GeoLocation is "For physical location boundaries (e.g., store radius), **NOT for state-level restrictions**"; state eligibility is handled via the `states` parameter in the rules wizard, i.e. in legal text, not runtime enforcement. Age gate "ONLY ... 21+ (alcohol/cannabis)". This anchors the category-wide runtime-enforcement gap.

**Challenged claims and resolutions.**
- A04=4 (rules wizard), A06=4 (AMOE as first-class software), A07=4, A01=4: all traced to the published OpenAPI 3.1 spec and MCP docs (official-doc, HIGH). Upheld — A06=4 is the category's only software AMOE and is legitimately category-leading.
- C01=3 upheld: FL/NY/RI thresholds, filing windows, Quebec RACJ, ABC states are genuinely *software-encoded* (wizard options, automatic warnings, hard guardrails) — one point above Votigo/RTM's human-held C01=2 is a meaningful, defensible productization differential.
- **C02=3 challenged and downgraded to 2.** Product-type coverage is a short list (alcohol/cannabis age gates, COPPA refusal, prohibited-category list) enforced only at platform-setup time, plus a human ABC filing service. RTM's human coverage of alcohol/pharma/financial services scored 2; Sweeppea's narrower setup-time guardrails do not support a higher score.
- **I09=3 direction error, normalized to 1** (same convention fix as Votigo).
- Marketing-vs-docs contradictions: correctly resolved by the agent in favor of docs throughout — webhooks claimed/undocumented (H03=1), sandbox claimed/undocumented (H04=1, G05=1), "certified drawing" marketing vs no certification schema in winner tools (A08=3, not 4), SOC 2 wording scoped to AWS/custom development (G10=1). Exemplary handling.
- 0 scores: the strongest absence-evidence in the category — the full API surface is enumerated in a published OpenAPI spec and an 83-tool MCP catalog, so B03/B08–B10, D03/D05, E10, F06/F08–F10, G04/G06, H06, J02/J04–J06/J08/J10 = 0 are positively grounded. Upheld, including B03=0 (Sweeppea explicitly instructs customers to enforce eligibility client-side, SWEEPPEA-028).
- ~3-employee headcount is a MEDIUM directory estimate; the report labels it and uses it appropriately for procurement-risk framing.

**Status: APPROVED WITH CORRECTIONS** (2 score overrides).

### 03 — Realtime Media (RTM)

**Verification performed.**
- Fetched `rtm.com/sweepstakes-legal-administration/data-security`: the page claims "SOC2, Type 2 Attestation" with "Independent audits validate our commitment..." and footer badges for SOC 2/GDPR/ISO 27001; no trust center or report-request path. This is a *specific completed-attestation claim* on a dedicated official page (vs. Votigo's ambiguous wording), consistent with an enterprise clientele that includes DraftKings/Disney/Netflix. G10=3 upheld, with the caveat for synthesis: attestation claimed, report not publicly accessible — procurement would need to request it.
- Fetched `rtm.com/api-promotions`: verified the API's claimed scope (validate registrations, trigger time-seeded instant-win results, power game logic, real-time behavior tracking — plus "entry rules enforcement, prize logic, and fraud checks" language), the 2–4 week file / 6–8 week API integration tiers, docs gated behind sales contact, and the Sling case (entries/plays per 30 minutes watched, streaks, Winners Wall). B01=2, H01=2, B07=2, and the Sling assembly pattern all upheld.

**Challenged claims and resolutions.**
- A-row 4s: upheld on official service pages plus operational winner-facing FAQs (official-doc) and 30-year track record; A06=3 and A10=3 appropriately held back for thin documentation.
- E07=3: upheld — unlike Votigo's marketing-stat fraud page (E07=2), RTM's proprietary scoring system is described in an operational FAQ (official-doc) with a deployment scope statement; the one-point differential is evidence-based. Opacity ("discreet", no reason codes) is correctly recorded in B05=?.
- J03=2 (highest J score in category): verified as genuinely structural — in-house sweepstakes lawyers on every project — but as headcount, not workflow software. Correctly calibrated.
- ?-heavy B/D/H rows: correct given the closed developer surface; the report properly refuses to score what cannot be seen, and its two reasoned H-row 0s (H07: public rate limits cannot exist without public docs; H10: nothing customer-deployable exists) are logically airtight.
- Inference labeling: RTM-037 (synchronous evaluation) is explicitly marked INFERENCE and only supports a 2; D08 left ? after the privacy-policy PDF 503'd twice — honest handling.

**Status: APPROVED** (no score overrides).

### 04 — ShortStack

**Verification performed.**
- Help center is Cloudflare-blocked (verified: direct fetch of the Teams article returns 403, exactly as the agent disclosed; the agent's snippet-corroboration fallback with MEDIUM confidence caps followed the brief).
- Corroborated the G02=3 anchor via search snippets of the official Teams article: four main roles with per-member custom permissions including **Approve Entries** and **Publish** — confirming RBAC materially richer than ViralSweep's two roles. G02=3 upheld with the confidence caveat.
- Fetched `shortstack.com/rules-generator/`: jurisdiction touches verified (state selection, NY/FL registration-and-bonding warning, Canada skill-testing question, Quebec exclusion), disclaimers verified ("not a law firm", "AS IS", attorney review strongly recommended), and confirmed the generator is a **standalone document tool with no connection to campaign enforcement** — anchoring A04=2, C09/C10=0, and the category's rules-text-vs-runtime gap.

**Challenged claims and resolutions.**
- A01/A02/A07=4, A03/A08=3: upheld on official docs + pricing + the Live Nation case study (HIGH) showing daily enterprise use.
- A10=0 (tax workflows) and the other reasoned 0s: upheld — SHORTSTACK-031 documents a targeted-search absence methodology (AMOE, affidavit/W-9/1099, SSO, certified drawing, management API each searched and absent), and the architecture (read-only Entries API + single outbound webhook event) positively precludes B03/B10/J05/J08/H10.
- Audit-relevant negative findings verified in the ledger and worth elevating: fraud-filter rejects are invisible to the customer (silent rejection with a fake "thanks" page, SHORTSTACK-012) and entries are admin-deletable (SHORTSTACK-018) — i.e., the evidence layer fails at exactly the "denied decision" boundary the J-hypothesis cares about.
- The Live Nation "compliance features" case-study framing was correctly deflated to what it is: customer-improvised legal gating via publish permissions, with no sign-off records (C08/J02/J03=1).

**Status: APPROVED** (no score overrides).

### 05 — ViralSweep

**Verification performed.**
- Fetched `viralsweep.com/api`: verified the complete surface is exactly 7 data endpoints (brands/promotions/entries GET+POST/points/validate/winners) with `x-api-key` auth, **no campaign-creation or configuration endpoints**, and no versioning, rate limits, idempotency, sandbox, webhooks, or decision endpoints on the page — confirming the support-page claim ("build, run, and manage your own promotions outside of your platform") overstates the product, and confirming the reasoned 0s across H04/H05/H07/H10 and J05.

**Challenged claims and resolutions.**
- A01/A02=4, A03=3, A07=4, A08=3: upheld on official docs (58-article feature enumeration, draw docs) and marketplace footprint.
- A05=3: upheld — a real managed service (rules drafting, registration/bonding, affidavits, 1099s, PO-box AMOE) consistent with Sweeppea's A05=3; the report correctly documents the tension between "we'll ensure your promotion complies with the law" (marketing) and the T&C's "we do not provide any legal advice" + customer compliance warranty (docs win; liability stays with the sponsor).
- **G01=3 challenged and downgraded to 2.** Multi-brand is real but brand-capped (max 6) with only two roles and no per-promotion permissions — materially below Votigo (unlimited brands at enterprise + 500-agency white-label machine) and ShortStack (client folders, permission tags, full white label), both scored 3.
- Evidence-hostile behaviors verified in the ledger and correctly scored (D09=0): entries editable post-hoc, invalid entries irreversibly auto-purged at 180 days, test entries live in production.
- The implausible third-party cert list (SOC 2/ISO/HIPAA/FedRAMP from an aggregator) was correctly rejected as LOW-confidence noise against the official site's silence; G10=1 upheld (no current trust page — the /security URL serves the homepage).
- C02/C03=0: upheld — grounded primarily in the T&C's contractual exclusion of gambling/lotteries/crypto (official-doc, HIGH), with the competitor comparison used only as corroboration.

**Status: APPROVED WITH CORRECTIONS** (1 score override).

---

## 2. Score normalization block

Terminology/convention notes applied across the category (for the master matrix):
- **Delivery-mode annotation:** A-row and C-row highs at Votigo/RTM (and partially Sweeppea/ViralSweep) are managed-service capabilities (humans + platform), not customer-operable software. Scores stand per "capability as delivered," but synthesis must not read A04=4 (human drafting at Votigo/RTM) and A04=4 (software wizard at Sweeppea) as the same thing.
- **I-row direction convention:** I07/I08/I09 are normalized as intensity of the named attribute (higher = more PS dependency / higher switching cost / heavier integration burden). Votigo and Sweeppea scored I09 inverted; fixed below. All other I-row scores already follow the intensity convention.

Changed squares only (downstream synthesis applies agent scores + these overrides):

```csv
company,square,agent_score,normalized_score,reason
Votigo,B03,2,1,"latency evidence is a marketing '<1s' stat for Votigo's own fraud layer; no externally callable decision endpoint (VOTIGO-036 concedes sync evaluation exists only inside hosted flows); 2 unsupported vs peers scored 0-1 for equivalent in-flow evaluation"
Votigo,I09,3,1,"direction normalization: agent used 3 to mean LOW integration burden; category convention is intensity (higher=heavier); hosted microsite/iframe model = minimal burden"
Sweeppea,C02,3,2,"product-type rules limited to alcohol/cannabis/COPPA setup-time guardrails plus a prohibited-category list and human ABC filing service; calibrated to RTM C02=2 whose human coverage (alcohol/pharma/financial) is at least as deep"
Sweeppea,I09,3,1,"direction normalization: agent used 3 to mean LOW integration burden; intensity convention = 1 (hosted pages / turnkey embed)"
ViralSweep,G01,3,2,"multi-brand real but capped at 6 brands with a two-role model and no per-promotion permissions; materially below Votigo/ShortStack multi-brand implementations scored 3"
```

**No score changes for RTM (03) or ShortStack (04)** — all audited 3/4s traced to sufficient evidence and all 0s carried positive-absence reasoning.

---

## 3. Category analysis

**Strongest incumbent: Realtime Media (RTM).** Deepest enterprise administration bundle in the category: in-house sweepstakes counsel on every project (the only structural counsel-in-the-loop, J03=2), a verified SOC 2 Type 2 attestation claim on a dedicated official page, a Fortune-500 roster including regulated-adjacent DraftKings, physical-world obligations covered (bonds, PO-box AMOE, warehousing, 1099s), and the category's only production API proven inside a major streaming service's always-on loyalty program (Sling). Votigo is the breadth runner-up (20+ mechanics + administration + 190-country fulfillment + 500-agency channel) but with a ~25-person org, a gated undocumented API, and a weaker verifiable security posture.

**Most dangerous substitute: the administrator-of-record service model as a class** (RTM, Votigo, Sweeppea, plus Merkle/HelloWorld, PrizeLogic, Marden-Kane, PromoVeritas and the long tail). It does the one thing software cannot: it **transfers liability itself** (named Administrator / "Independent Administrator = legal shield"), bundled with physical-world obligations, at per-campaign prices ($3–15K at Sweeppea; quotes elsewhere). It doesn't compete with the J01–J10 architecture — it suppresses demand for it in the promotions vertical. The most architecturally forward-deployed variant is **Sweeppea's API/MCP-wrapped "Compliance-as-a-Service"**: liability transfer embedded via API into other platforms, with reason-coded server-side guardrails — proof the services class can reach the platform/engineering buyer the wedge would target, years before any of them builds policy infrastructure.

**Capabilities already commoditized.**
- Promotion creation mechanics (A01–A03) and entry management (A07): 3–4 at all five vendors, self-serve from $0–$166/mo, with a long tail (Gleam, Woobox, SweepWidget, Rafflecopter…) anchoring prices near zero.
- Basic winner drawing (A08 at 3 for the DIY tier): weighted random pickers are table stakes; certified/third-party drawings are cheaply unbundled (randomdraws.com, Odds On).
- Template official-rules generation: free tools at ShortStack and ViralSweep (disclaimered, standalone) put a $0 anchor under any "rules generation" feature.
- IP-based country/state geo-gating, entry-time dedupe/spam filtering, CAPTCHA: present everywhere, marketing-grade everywhere.
- Multi-brand/agency white-labeling (G01 2–3 across the board).

**Capabilities partially covered.**
- Legal administration (A04–A06, A09, A10) as *human services*: strong at RTM/Votigo, mid at Sweeppea/ViralSweep (absent at ShortStack). Software share: only Sweeppea's rules wizard and AMOE plumbing.
- Jurisdiction intelligence (C01–C03): held in staff expertise and templates; Sweeppea is the only vendor that software-encodes thresholds/filing windows/guardrails — and even there it is vendor-internal, setup-time, unversioned to customers.
- Counsel involvement (C08/J03): headcount at RTM; accommodated by email/docs at Votigo/Sweeppea/ViralSweep; improvised by the *customer* via publish permissions at ShortStack (Live Nation).
- Promotion-scoped fraud (E07/E08): real engines at RTM/Votigo but opaque (no reason codes, no customer-facing scores; RTM's is explicitly "discreet" and tied to RTM-hosted properties).
- Evidence (D02/D05/D07): document-grade custody — drawing files, DocuSign declarations, affidavits, filed winner lists — designed to defend a drawing or survive a state inquiry, not to reconstruct decisions.
- Promotion-scoped synchronous evaluation (B01/B02): instant-win results, receipt validation, purchase-to-enter ingestion; RTM's API (registrations, time-seeded results, behavioral events, streaks) is the deepest, and it is RTM-operated with sales-gated docs.

**Apparent gaps (verified across all five).**
- **Runtime jurisdiction enforcement:** state-level eligibility lives in rules *text*, not in runtime checks — Sweeppea's own docs say geolocation is "NOT for state-level restrictions"; ShortStack/ViralSweep offer IP-country/state allowlists with manual exception handling; no VPN/proxy detection anywhere in the category (E06 = 0/? everywhere).
- **Customer-authorable, versioned policy:** C05/C10 ≈ 0–1 everywhere; no vendor exposes rule objects, versions, effective dates, or provenance (C09 ≈ 0).
- **Counsel approval as software:** no sign-off records, approval history, or legal-to-production workflow anywhere (J02 ≤ 1, J03 ≤ 2 and human).
- **Impact analysis / simulation:** C07/J04/B09 ≈ 0–1; the closest analog is RTM's manual pre-launch risk assessment.
- **Decision-grade evidence:** no immutable decision IDs, no policy-version linkage to any record, and — decisive — *denied* events are unlogged or destroyed (ShortStack silent rejects invisible; ViralSweep entries mutable and invalid entries irreversibly purged at 180 days; Votigo/RTM evidence is per-drawing paperwork).
- **Reason codes as an API contract:** only Sweeppea's MCP rejection payloads, scoped to platform-management calls, vendor-authored.
- **Replay / "why was this allowed?":** B10/J08 = 0/? at all five. Nothing exists to replay.
- **Cross-product authorization and signal normalization (J05/J06):** 0 across the category; Sweeppea explicitly delegates runtime eligibility to the customer's front end.
- **Regulatory change monitoring as product (C06):** ≤1 everywhere; blogs and vendor-maintained internal knowledge only.

**Gaps probably too small to monetize.**
- Certified-drawing-as-an-API: already unbundled at commodity prices by randomdraws.com/Odds On.
- AMOE digitization/mail-in processing: PO boxes are cheap; Sweeppea already productized the software half.
- Better rules generators: free tools anchor this at $0; counsel review remains the paid step.
- Winner tax workflow software (W-9/1099): episodic, low-frequency, already bundled into every service tier.
- Developer-platform hygiene for promotions APIs (sandboxes, idempotency, webhook retries, SSO for campaign tools): real deficiencies everywhere, but no promotions buyer pays for hygiene alone.

**Gaps worth passing to synthesis.**
1. **Runtime, evidence-linked jurisdiction eligibility enforcement** — nothing in the category enforces at runtime what the official rules promise on paper; the seam between the legal document and runtime behavior is unowned (anchor evidence: SWEEPPEA-021, verified).
2. **Decision-grade evidence and replay for promotion/incentive decisions** — the category is document-grade at the top and actively evidence-hostile at the bottom (mutable entries, invisible rejects, forced purges); "why was this entry allowed/denied" cannot be answered by any vendor.
3. **Counsel-in-the-loop policy lifecycle as software** — Live Nation *improvised* a legal review gate out of ShortStack publish permissions, and RTM sells it as headcount: demand signal exists at both ends, but willingness-to-pay for it as software is unproven and must be tested against the services price point.
4. **The frequency wedge** — always-on, in-product promotion/incentive mechanics (the Sling pattern: entries and plays as continuous product features, 6–8-week integrations, RTM-operated backend) is the only place per-campaign service economics structurally break; this is where a decisioning/evidence product is not competing with a $3–15K service fee.
5. **The regulated-adjacency seam** — DIY tools contractually exclude gambling/crypto (ViralSweep) and push all liability to the sponsor (ShortStack terms); administrators handle alcohol/pharma/financial as bespoke services. Sweepstakes-casino operators, fintech incentives, and gaming-adjacent promotions have no software path in this category at all.
6. **Carry this caveat with the gaps:** the J-row is empty (max J03=2, human), so the architectural white space is confirmed within this category — but so is demand suppression: the services class already monetizes the pain *and absorbs the liability*. Any Promotion OS thesis must be justified on frequency, cross-product reach, and evidence rigor — never on promotion administration, which is solved.

---

## 4. Internal-build / stack-substitute assessment

Question: can this category's buyer base (brand marketing at consumer enterprises, their agencies, and platform teams embedding promotions) cover the J01–J10 hypothesis with these vendors + internal engineering + counsel?

**Three assembly patterns observed in evidence:**
- **Pattern A — Enterprise + administrator (RTM/Sling; Votigo enterprise):** administrator runs backend mechanics and compliance services; internal engineering owns the front end and streams behavioral events; counsel = vendor's in-house lawyers plus client legal. Delivers compliant *campaigns* at scale. Produces zero J-capabilities: no versioned policy, no reason codes, no replay, evidence split between vendor paperwork and internal logs.
- **Pattern B — Enterprise DIY + internal legal gate (ShortStack/Live Nation):** $166/mo tool + free rules template + attorney review + publish-permission gating. Marketing-grade evidence, no sign-off records, denied entries invisible. Proves the "good enough" ceiling is high even for a large enterprise — the strongest demand-suppression data point in the category.
- **Pattern C — Platform embed + liability outsourcing (Sweeppea CaaS):** platform embeds sweepstakes via API; Sweeppea takes the Independent Administrator role, rules, draws, 1099s; the customer is *explicitly instructed* to implement age/geo eligibility client-side. The decisioning and evidence layer is 100% internal build; the vendor contributes liability transfer and back-office.

**Verdict: substitution is credible for the outcome, not for the capabilities.** For episodic promotions (the vast majority of this buyer base), vendor + counsel + light internal engineering covers the *job* better than software could — because the assembly includes liability absorption and physical-world obligations (bonds, PO boxes, drawings, 1099s, fulfillment) that software cannot absorb, at per-campaign prices below any infrastructure TCO. But no assembly of these five vendors plus internal engineering yields the J01–J10 *capabilities*: there is no policy substrate, decision API, evidence store, or approval workflow anywhere in the stack to build on — internal engineering would build the entire decision/evidence layer from zero, with the vendor contributing nothing to it (Votigo/RTM have no callable decision surface; Sweeppea/ShortStack/ViralSweep APIs are entry-data plumbing). The substitution argument therefore fails exactly where the gaps-for-synthesis live: continuous in-product decisioning, multi-jurisdiction/multi-product programs, and audit-exposed verticals.

**Vendor-fragility qualifier (cuts both ways):** the category runs on 3–57-person companies; two of five make unverifiable or ambiguous security claims, one has no trust page at all, and none has a hardened public developer platform. This caps their ability to move up into infrastructure (replacement risk LOW at all five — unanimous and, after QC, correct), but it equally caps an enterprise's willingness to put any of them in a production decision path — which mildly *strengthens* the case that production-path authorization, if wanted, gets built in-house or bought from a different kind of vendor.

---

## 5. Adjacent competitor appendix

Deduplicated across the five reports (source reports in brackets). **Bold** = materially changes the landscape.

**Enterprise-scale promotions platform+services (the tier above the studied five):**
- **Merkle / HelloWorld (formerly ePrize, dentsu)** — enterprise promotions technology + administration at scale; the one promotions incumbent with plausible resources and enterprise relationships to productize compliance if anyone does. [01, 03]
- **PrizeLogic** — enterprise promotions/loyalty/rebate execution for major CPG/retail; deepest services+platform hybrid overlap with RTM. [01, 03, 05]
- **PromoVeritas** — global promotion-compliance services agency (90+ countries, legal drafting, registrations, independent draws, winner/tax management); shows the services substitute is global, not US-only. [04]

**US administrator/service-bureau class (substitutes on the administration wedge; collectively material, individually not):**
- Marden-Kane (since 1957) [01, 02, 03] · National Sweepstakes Company [01, 02, 03, 05] · Don Jagoda Associates [01, 03] · Ventura Associates [01, 03] · Brandmovers [01] · Promosis [03, 04] · Odds On Promotions [02] · randomdraws.com (unbundled certified draws) [02]
- **Dedup correction:** *US Sweepstakes & Fulfillment Co.* was listed by the Sweeppea agent as an independent competitor, but Votigo acquired it in November 2020 (VOTIGO-025, corroborated by Votigo's own announcement). Treat as part of Votigo, not a separate entrant.
- **Promotion-law boutiques + bonding agents** (e.g., Klein Moynihan Turco) — the incumbent "workflow" for J02/J03 is licensed counsel + an administrator + a surety agent; any counsel-workflow product competes with this labor market first. [02, 03]

**DIY long tail (price anchors; confirms front-end commoditization):**
- Gleam [04, 05] · Woobox [02, 04, 05] · SweepWidget [01, 04, 05] · Easypromos (EU depth) [04] · Rafflecopter, Vyper, Wishpond, Woorise, KickoffLabs [04, 05]

**Context entries:**
- Clearer.io / AppHub — ViralSweep's owner; portfolio logic (reviews, returns, address validation, conversion apps) points its roadmap at e-commerce, away from compliance. [05]
- Manager addition (from category knowledge, not researched in this pass): **Marigold Grow (formerly Cheetah Experiences / Wayin)** — enterprise interactive-experiences/promotions module inside a martech suite; worth a synthesis-stage check as an enterprise software peer to Merkle/HelloWorld. Not landscape-changing on current evidence.

---

## 6. Approval line

REPORTS APPROVED: 01_votigo.md, 02_sweeppea.md, 03_rtm.md, 04_shortstack.md, 05_viralsweep.md
