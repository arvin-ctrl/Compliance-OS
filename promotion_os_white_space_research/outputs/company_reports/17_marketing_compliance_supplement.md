# Supplemental Report 17 — Marketing-Compliance Monitoring & Review Software

Researcher: Supplemental Research Agent 17 (Marketing-Compliance Category)
Date: 2026-08-18
Assignment: Chief Synthesis Manager supplemental brief (Section 6.2 of `outputs/final/candidate_white_spaces.md`; red-team question 7)
Scope: PerformLine (deepest), Red Marker, Saifr, Luthor, plus material peers discovered (Red Oak Compliance, Sedric, Haast), comms-surveillance marketing modules (Proofpoint Patrol, Smarsh, Hearsay/Yext), and vertical archetypes (Veeva Vault PromoMats, AdComplyRx)
Evidence ledger: `outputs/evidence/17_marketing_compliance_supplement.jsonl` (MKTCOMP-001 … MKTCOMP-038)
Note: per assignment, the 100-square scoring and 17-section template do NOT apply. Candidate numbering follows the synthesis doc: **C1 = counsel-governed policy lifecycle, C2 = jurisdictional policy content network, C3 = evidence-grade decision archive, C4 = promotional-conduct authorization.** Where the assignment brief says "executable jurisdictional content (Candidate 1)", the synthesis doc's label for that shape is C2; both C1 and C2 are answered explicitly throughout.

---

## 0. Scope notes and corrections

1. **"4L Labs / CommsCompliance" could not be found.** Web search returns no vendor by either name in this category; the nearest hit is 4Comply (4Thought Marketing), a marketing *privacy/consent* tool, which is out of scope. Treated as a phantom/garbled reference and replaced with the material peers actually found: **Red Oak Compliance, Sedric, Haast** (AdClear.ai noted in landscape). [MKTCOMP-037]
2. **"Red Marker (Kaplan)" is outdated.** Kaplan sold Red Marker to **IntelligenceBank** (marketing-ops/DAM SaaS) on July 29, 2024. [MKTCOMP-017]
3. **Hearsay Systems belongs to Yext, not Smarsh** ($125M + up to $95M earnout, completed August 1, 2024). [MKTCOMP-034]
4. **Riskified/Signifyd: excluded as immaterial** to this category (ecommerce fraud/chargeback-guarantee vendors; no marketing-content review product in their positioning; riskified.com blocked direct fetch with 403). Labeled inference. [MKTCOMP-038]
5. Method: official product pages and docs prioritized per AGENT_BRIEF; WebSearch used for ownership/funding verification. All access dates 2026-08-18. Marketing metrics are flagged as such; absences are claimed only from enumerating pages (a page that lists its coverage), not from silence.

---

## 1. Per-vendor findings

### 1.1 PerformLine — the category incumbent (deepest dive)

**Q1 — What it reviews, and when.** Omni-channel marketing-content review in two phases. *Pre-publication:* draft assets — direct mail, emails, landing pages, blogs, draft social posts, video/audio, documents (Word/PDF/PPT/MP4/JPG) — submitted by upload or from workflow tools; automated scoring returns "near-instant feedback… corrected before it goes live." *Post-publication:* continuous discovery and monitoring of live web, social, email, calls, SMS/chat, partner channels, and (new) "AI responses" — "places you didn't know existed." The reviewed object is always a marketing **asset or conversation**; there is no transaction or user-event object anywhere in the product. [MKTCOMP-001, -006]

**Q2 — Rulebooks.** Vendor-curated in-house since 2007: "crafted from regulatory bulletins, acts, documents, settlements, and industry standards from governing bodies including the CFPB, FTC, FCC, SEC, ED, OCC, FINRA and more." Coverage is **federal-act based** — Dodd-Frank, UDAAP, CARD Act, TCPA, TILA, RESPA, FTC Act, MAP Rule/Reg N, ERISA, GLBA, FDCPA, SAFE Act, HEA, CARES, Patriot — plus built-in "UDAAP, CAN-SPAM, and Schumer Box / TILA rule packs" in pre-pub. Customers can add their own rules ("PerformLine staying in sync"). Provenance is claimed at the **corpus level** (rules derive from bulletins/settlements); findings cite "the regulatory basis" per violation — but no per-rule citation graph, no rule versioning, no update-cadence documentation, and no effective-dating is publicly exposed. **No US-state-level jurisdiction packs. No gambling/gaming industry. No sweepstakes/promotions-law coverage anywhere** — verified on the enumerating rulebooks page, the marketing-compliance learning hub (which lists its topics and contains none of: sweepstakes, contests, prize law, state promotional rules, gaming), and open web search. State Attorneys General are monitored as an enforcement-signal *source*, not as per-state rule packs. [MKTCOMP-003, -004, -005, -011, -012, -013]

**Q3 — Runtime enforcement / decision API.** None. Pre-pub verdicts are tri-state on **content** — a 0–100 score mapping to "Pass, Warning, or Fail… with client-configurable thresholds," plus a "suggested compliant rewrite" — advisory, human-consumed (inference from absence of any blocking claim: the gate's enforcement is organizational, not technical). Integrations are workflow plumbing: "out-of-the-box connectors, webhooks, and APIs that bring discovery, review, and evidence into your existing stack" (Jira/Workfront/monday/Aprimo/Figma/Zapier "or any API-driven tool"; Five9/NICE/Twilio/Genesys for calls). No public developer portal, no synchronous decision endpoint, no transaction-time anything. [MKTCOMP-006, -007, -009]

**Q4 — Workflow & audit story.** Remediation notices sent from the platform to "non-compliant partners, agents, or reps," responses "recorded within the workflow for one seamless trackable history"; alert states from "not reviewed through resolved"; "Archive for the length you require, a complete history of discovery through remediation for any audit situation." Pre-pub keeps "a complete, timestamped record from submission through resolution" with findings, approval history, scores. So: **asset-review lineage with configurable retention** — solid for marketing-compliance exams. It stops there: no policy-version binding of decisions, no counsel-attestation semantics, no as-of replay, no tamper-evidence claims, no regulator-package export beyond archive access. [MKTCOMP-006, -008]

**Q5 — Buyer, verticals, traction, pricing.** Buyer: compliance teams/CCOs at consumer-finance enterprises (marketing compliance function; Acima VP of Compliance is the featured voice). Verticals: banks, credit cards, fintech, mortgage (site nav); rulebook industries add BNPL, alt lending, gig, education, tech, healthcare. Traction: "**Trusted by 6 of the top 10 U.S. banks**"; founded 2007 (Alex Baydin, Morristown NJ); First Round → M33 Growth (May 2021) → **additional funding January 2026 "to accelerate AI product expansion plans."** Runs the COMPLY conference/community (category-building). No public pricing; enterprise SaaS motion. [MKTCOMP-002, -010]

**Q6 — Expansion threat (inference, labeled).** Toward **C4 (action authorization): LOW.** No transaction rails, no identity/geo signals, no eligibility state, no synchronous API — an architectural rebuild, and 19 years of DNA point at content. Toward **C1/C2: REAL and the highest in this category.** PerformLine already operates the exact editorial+software hybrid C2 requires — a paid team converting regulator output into machine-applied rules, sold as subscription to compliance buyers at the same bank/fintech accounts — and fresh AI capital. Extending rulebooks from ad language to promotional-*conduct* propositions (state registration/bonding thresholds, AMOE, prize limits) is an editorial-ops extension, not a technology leap; what it lacks is state-granular legal content, counsel-attestation workflow, and any engine to execute in. It would also collide with UPL exposure the moment rules become conduct rather than copy. Most likely first move: deepen AI review and "AI response monitoring," not conduct authorization.

---

### 1.2 Red Marker (IntelligenceBank; ex-Kaplan)

**Q1.** Pre-publication and during-authoring review of advertising/marketing content: document scanning (PDF/docx/etc.), Word and Figma plug-ins, email-in review, an Approvals module, and web-page reports — "ensure only compliant content reaches the market." Post-publication footprint is limited (web reports); no continuous discovery claims at PerformLine's level. [MKTCOMP-014, -015, -016]

**Q2.** Vendor-maintained rule libraries at **regulator/country granularity**: "FINRA Marketing Compliance," "FCA Marketing Compliance," an "Australian Retail Banking" risk rule library; multi-language (ES/FR/IT/DE). Rules are applied and customized by Red Marker's own "Client Success and Implementation teams… training the AI model on the triggers." Flags include "misleading phrases and unsubstantiated claims," "incorrect or missing disclaimers and disclosures," and — notably — "**unclear promotions**" (promotional ad-copy checks exist). No public per-rule statutory citation/provenance. [MKTCOMP-014, -015]

**Q3.** None at runtime. The public API (redmarkertech.github.io) is an **asynchronous asset-review pipeline** — resources: Assets, Reviews, Webhooks; output includes a "Review PDF." Content scanning only; structurally unsuited to action authorization. [MKTCOMP-016]

**Q4.** Approvals module plus risk-detection reporting; audit-trail depth not publicly documented. Post-acquisition, the audit story rides on IntelligenceBank's marketing-ops platform ("a single platform to ensure all marketing content… is brand and legally approved"). [MKTCOMP-014, -017]

**Q5.** Buyers: legal/compliance teams and marketing teams (both have dedicated use-case pages); verticals: financial services, insurance, automotive, telecom, F&B, pharma, healthcare; customers shown: BizCover, eToro, LG, Nationwide, Kaplan; US/UK/AU footprint. Founded by Matt Symons; Kaplan-owned 2017–2024; **acquired by IntelligenceBank July 29, 2024.** Pricing page exists (gated). [MKTCOMP-014, -017]

**Q6 (inference).** Toward C4: negligible — new owner is a marketing-operations/DAM company; the integration direction is INTO the marketing workflow (brand + legal approval of assets), away from conduct authorization. Toward C2: it is the proof-of-concept that **regulator-scoped, vendor-maintained rule libraries sell** (FINRA/FCA/AU-banking packs), including promotions-adjacent copy rules — but country-level ad-language packs, not state-level conduct law, and the Kaplan exit suggests the regulatory-content owner saw better returns selling the asset than scaling it.

---

### 1.3 Saifr (born in Fidelity Labs)

**Q1.** In-workflow, creation-time and pre-publication review of financial-services marketing content — text, images, video — via add-ins ("Run compliance scans as content is created"), a centralized review workspace, and document submission; adjacent products for e-comms and AML screening (SaifrScreen, Saifr eComms). Post-publication: adverse-media/internet scanning exists but marketing review is pre-pub-centric. [MKTCOMP-018]

**Q2.** Named regulatory scope: **FINRA 2210, SEC 482, SEC Modernized Marketing Rule**; risk detections: "promissory, misleading, exaggerated, or unwarranted" language, performance claims, testimonials, comparisons. The rule source is a **learned model**, "trained on 20+ years of proprietary, industry-unique data from regulatory and compliance experts" — i.e., Fidelity's institutional review corpus — maintained by Saifr's own regulatory/AI team. Provenance is institutional experience, not exposed statute citations. [MKTCOMP-018, -019]

**Q3.** No action-time enforcement, but the **most API-first posture in the category**: "API: Build compliance risk scanning into your processes," distribution in the **Microsoft Azure AI model catalog**, partnerships with Adobe and ServiceNow. The API returns content-risk findings on submitted material — a scanning service, not an authorization verdict. [MKTCOMP-020]

**Q4.** Collaboration/commenting, approval status, "detect up to 90% of what a human would," "10x faster" to market (marketing claims). Audit-trail/retention/versioning depth not publicly documented — the workflow story is thinner than Red Oak's or Veeva's; Saifr sells the detection brain more than the system of record. [MKTCOMP-018, -021]

**Q5.** Buyers: compliance teams at broker-dealers, asset managers, banks, insurers/annuity issuers (banking and insurance variants shipped); named customer: Nasdaq. Backed/incubated by Fidelity (offices Boston/NY/TX/Dublin/Chennai/Bangalore). [MKTCOMP-019, -021]

**Q6 (inference).** Toward C4: low-to-moderate mechanically — an embeddable risk-scan API inside Azure's catalog is one integration away from being called in-flow by someone else's gate — but Saifr's scope is US securities-marketing language, not conduct or state law. Toward C1/C2: moderate; Fidelity's balance sheet and the "regulatory experts + 20 years of data" editorial muscle could fund a content-network play, but everything shipped is model-weights, not citable rules — the opposite of C2's provenance requirement.

---

### 1.4 Red Oak Compliance — the workflow-volume incumbent (discovered)

**Q1.** Pre-publication **advertising review workflow** for financial services: submission → review queues → approvals of marketing/advertising materials, plus AI Review, Internet/social supervision and website monitoring modules. The system of record for "should this go out, and who said so." [MKTCOMP-024, -025]

**Q2.** **Customer-authored substance, vendor-supplied process.** Public pages claim no curated statutory rulebook; review logic is the firm's own compliance manual applied through configurable workflow, now augmented by "AI Review" using "Large Language Models (LLMs) and sophisticated prompt engineering." (Inference from enumerating product pages — labeled.) This is the opposite pole from PerformLine's curated-rulebook model. [MKTCOMP-025, -026]

**Q3.** None. No decision API in public materials; "Integrations & APIs" exists as a resource section for workflow integration. [MKTCOMP-025]

**Q4.** The strongest pure-workflow audit story in the category: centralized tracking, approval chains, "books and records compliant" retention, **"Seamless FINRA integration"** (filing/registration workflows), disclosure management. Built to survive FINRA/SEC exams of the *ad-review control* itself. [MKTCOMP-025]

**Q5.** "**1800+ Firms Globally**," "Partner to Over Half of the Top 20 Asset Managers," 84 NPS; buyers: broker-dealer/RIA/bank/insurance compliance departments. [MKTCOMP-024]

**Q6 (inference).** Toward C4: none — no runtime surface at all. Toward C1: this is the vendor whose *shape* most resembles C1's approval-workflow half (regulated submission→review→approval→attestation-ish records→regulator filing), proving that compliance buyers pay eight-figure-aggregate SaaS for **governed approval pipelines** — but its object is a document, its reviewers are compliance officers not counsel-as-code-approvers, and it compiles to nothing. A C1 pitch to financial services will be heard as "Red Oak for policies" — useful analogy, real perception-level substitute.

---

### 1.5 Sedric — fintech comms+marketing guardrails (discovered)

**Q1.** "Real-time guardrails on all of your content" for regulated financial firms: **pre-publication marketing review** ("Review and approve marketing content before it goes live"), post-hoc interaction QA ("automatically review every interaction"), **Real Time Agent Assist** ("guide agents in real time" during live conversations), partner-content monitoring. [MKTCOMP-027]

**Q2.** Two-source model: customer policies — "ingests and structures your policies, translating them into preventive, detective, and corrective controls" — plus vendor-shipped "**built-in regulation libraries**" spanning UDAAP, Reg Z, TILA, ECOA, FTC, CFPB, SEC, FINRA, FCA, ESMA, MiFID, MiCA, FDCPA. Framework-level, not state-level; no public per-rule provenance. [MKTCOMP-028]

**Q3.** Closest approach to runtime in the category — but on **human conversations**, not transactions: agent-assist intervenes mid-call/chat; enforcement of review outcomes is applied "manually and automatically." No transaction/decision API; no promo/entitlement objects. [MKTCOMP-027, -028]

**Q4.** "Every override is logged with reasoning, and every resolution is exam-ready by design" — an explicitly exam-oriented audit posture (closed-loop detection→remediation→enforcement). Depth (retention guarantees, versioning) not publicly documented. [MKTCOMP-028]

**Q5.** Buyer: fintech/neobank/crypto/collections/trading compliance leaders; customers **eToro, WebBank, NinjaTrader, Coastal Bank, Exness, Capital.com**; **$18.5M Series A** (Foundation Capital, American Express). [MKTCOMP-029]

**Q6 (inference).** The fastest-moving flanker vocabulary-wise: "policies → preventive/detective/corrective controls" is one rhetorical step from executable policy, its customer list is exactly C4's fintech/trading regulated-adjacency profile, and agent-assist proves an in-path intervention muscle. But its objects are content and conversations; adding transaction authorization means building an engine, signal ingestion, and eligibility state from scratch. More plausible near-term expansion: absorb more of the marketing+comms compliance budget at C4's target accounts, raising the "we already have a compliance platform" objection.

---

### 1.6 Haast — pre+post review with jurisdictional agents, including gambling (discovered)

**Q1.** Both phases: "reviewing content and communications before they go live" and post-publication monitoring of "all live assets and channels… including partners, influencers, and anyone linked to your brand"; broad file-type coverage including audio/video. "Full compliance lifecycle, from intake to decision to audit trail." [MKTCOMP-030]

**Q2.** Vendor-shipped, framework-scoped "agents": FINRA, FTC, FCA, UDAAP, Consumer Duty (finserv); CCPA/GDPR (retail); Ofcom/PECR (telecom); FDA/HIPAA (pharma); and — unique in this supplement — **Gaming: "Gambling Commission LCCP, Age Verification, Responsible Gaming."** Configured "attorney-led" by Haast's in-house legal team, then tuned to customer risk tolerance. Counsel-in-the-loop at SETUP, not per-change attestation. [MKTCOMP-030, -031]

**Q3.** None for actions; API + native integrations (Figma, Office365, Workfront, Google Docs, monday.com) for content flows. [MKTCOMP-030]

**Q4.** "Intake to decision to audit trail" is claimed; public depth is thin (no retention/versioning/exam-package specifics). [MKTCOMP-030]

**Q5.** Enterprise positioning ("world's largest enterprises"), AU-origin, US/UK expansion; metrics are vendor-reported (80% review-time reduction). Funding not stated on site. [MKTCOMP-030]

**Q6 (inference).** Toward C4: the most interesting *content* adjacency — it already maintains **gambling advertising rule content** (UK LCCP marketing/social-responsibility codes, age verification, RG) as product. That is jurisdiction-scoped promotional-marketing law, productized — but at the ad-copy layer, UK-regulator-scoped, with no conduct/transaction surface. A Haast that added US state sweeps/gaming packs would be walking C2's beachhead path from the content side; watch it the way the synthesis watches Vixio.

---

### 1.7 Luthor — AI-native entrant (YC, 2024)

**Q1.** Pre-publication only: scans "every asset before publication, from internal drafts to customer content across every channel" (text, image, video, audio, SMS, social, URLs). [MKTCOMP-022]

**Q2.** Built-in framework checks (FINRA 2210, FTC, FCA, UDAAP, GDPR; SEC/FinCEN per YC profile) + customer policies + the firm's "approved knowledge base, product specs, and historical claims"; **human oversight from former SEC attorneys** (per YC/third-party profiles). [MKTCOMP-022, -023]

**Q3.** None; no public API. [MKTCOMP-022]

**Q4.** "Clear evidence for every decision," risk-leveled findings, claimed 3× faster approvals. Homepage stat counters render as placeholders ("$0+ AUM Protected") — quantified claims LOW confidence. [MKTCOMP-022]

**Q5.** Founded 2024, SF, Y Combinator; ~$500K reported raised (Drive Capital, Tribe Capital, TQ Ventures et al. listed by trackers); clients are RIAs/broker-dealers/credit unions totaling ~$5.7B AUM — small-firm traction. [MKTCOMP-023]

**Q6 (inference).** Ambition is C1-flavored ("AI compliance infrastructure for regulated marketing," "real-time governance for enterprise communications") but the company is seed-stage with SMB-RIA traction. Relevance today: demonstrates that new entrants see the same white space *name* ("compliance infrastructure") while still building content review — i.e., even the newest money in this category attacks words, not actions.

---

### 1.8 Comms-surveillance incumbents' marketing modules

**Proofpoint Patrol.** Social/text/mobile content compliance with "**Pre-review or post-review options**"; ships "compliance policy templates, covering FCA, FINRA, SEC, IIROC and more"; the only automated **enforcement** found in this category — "Automatically or manually remove content directly from monitored social media accounts" — i.e., deletion of published content, with everything archived "for storage and e-discovery." Enforcement acts on content, post-hoc; no action prevention, no decision API. Buyer: financial-services comms-supervision/archiving teams. [MKTCOMP-032]

**Smarsh.** Product line is Capture / Archive / Surveillance / Discovery / Supervision. Third-party competitive analysis (AdClear blog — competitor source, MEDIUM confidence, consistent with Smarsh's own product nav): "Smarsh does not review marketing before it publishes" — it sits in the archiving/surveillance camp, publishing SEC-Marketing-Rule thought leadership that routes to supervision products. No pre-publication ad-review module found. Relevance to C3: Smarsh-class WORM comms archiving is the ledger-grade evidence that **compliance-evidence budgets exist** — for communications records, not decisions. [MKTCOMP-033]

**Hearsay Systems (Yext).** Compliant field-engagement for financial services (Hearsay Social/Relate): advisers publish from pre-approved libraries with supervision and books-and-records capture; upgraded supervision for testimonials/endorsements under the SEC Marketing Rule. Acquired by **Yext** for $125M + up to $95M earnout, completed 2024-08-01 — consolidated into digital-presence management, not compliance infrastructure. [MKTCOMP-034]

---

### 1.9 Vertical archetypes

**Veeva Vault PromoMats (pharma — the hard-gate archetype).** "A regulated content management application that supports the full lifecycle of promotional content": creation, **MLR (medical-legal-regulatory) review**, claims management (claim-to-reference linking), DAM, and controlled distribution — "easily publish and **withdraw** content to digital channels"; "**automatically generates eCTD compliance packages for post-marketing and pre-clearance submission to the FDA**." Customers: Moderna, J&J, Gilead, GSK; industry standard across hundreds of biopharmas. This is the ceiling of the category: a genuinely **hard** pre-publication gate, counsel/regulatory reviewers in the loop, provenance from claim to substantiating reference, versioned lifecycle including withdrawal, and regulator-facing evidence packaging — all of it scoped to promotional **materials**. Pharma proves every C1 workflow mechanic is buildable and mandatory-budget-fundable in a vertical where the regulator demands it — and still nobody authorizes actions. [MKTCOMP-035]

**AdComplyRx (pharma SEM micro-vertical).** 2–10-person NYC firm; post-publication monitoring of live pharma paid-search/social ads against FDA standards ("Over 60 major Rx brands are inadvertently running non-compliant ads on Google and Bing"), Chrome extension for ad-hoc checks; explicitly positions around the delay of "long CMLR/PRC/PRT/PromoMats reviews" — it orbits the Veeva-style gate rather than replacing it. Demonstrates how thin the long tail of this category runs. [MKTCOMP-036]

---

## 2. Category-level answers

### 2.1 Does this category already absorb the budget and the "counsel bottleneck" pain that C1/C3/C4 assume is unserved? Where exactly does it stop?

**The budget line exists, is large, is mature, and is owned — for words.** PerformLine (6 of top-10 US banks, founded 2007, new AI capital Jan 2026), Red Oak (1,800+ firms, half the top-20 asset managers), Veeva PromoMats (industry-standard in pharma with FDA submission packaging), Sedric ($18.5M A, Amex money, eToro/WebBank), Saifr (Fidelity-incubated, Azure-distributed) — "marketing compliance" is a named, funded, decades-old budget line at exactly the enterprises C1/C2/C4 target, and vendor-curated rulebooks applied by software are **already bought** there. The bottleneck it absorbs is real and adjacent to the project's pain narrative: pre-publication review queues, review latency ("10x faster," "3× faster approvals"), partner-channel sprawl, exam-ready records of *who approved this asset*. [MKTCOMP-002, -010, -024, -029, -035]

**Where it stops — the seam, stated precisely.** Four boundaries, consistent across all eleven vendors examined:

1. **Object:** the unit of review is a marketing asset, page, ad, post, call, or conversation — never a transaction, entry, bonus grant, or person-action-jurisdiction tuple. No vendor has promo/entitlement objects, eligibility state, or identity/geo signal ingestion. [MKTCOMP-001, -016, -027]
2. **Verdict semantics:** outputs are risk flags/scores on content (PerformLine's Pass/Warning/Fail is tri-state but advisory and human-consumed; Saifr/Red Marker APIs return findings, asynchronously in Red Marker's case). Nothing returns an allow/deny/review verdict that *binds an action at runtime*. The only automated enforcement found (Proofpoint Patrol) is post-hoc deletion of published content. [MKTCOMP-006, -007, -016, -020, -032]
3. **Rule content:** rulebooks encode *communication* law — disclosure, fair-balance, misleading-claims, UDAAP language — mapped to **federal acts and regulator regimes** (CFPB/FTC/FINRA/FCA/LCCP). Nowhere: US state-granular conduct law (sweepstakes registration/bonding, AMOE, prize thresholds, state bonusing restrictions), effective-dated rules, per-rule statute citations exposed as product, or counsel attestation per rule change. PerformLine's promotions/sweepstakes coverage is **verified absent** (rulebooks page + learn hub + open search). [MKTCOMP-004, -011, -013, -028, -031]
4. **Evidence:** audit trails cover the asset-review workflow (submission→approval→remediation, archived; Veeva even packages for FDA). None of it is decision evidence for actions — no policy-version-pinned decision records, no as-of replay, no tamper-evidence claims. [MKTCOMP-008, -025, -035]

**Consequence for the candidates.** C3 and C4 are **not absorbed** — they sit entirely on the far side of the words/actions seam; no vendor here touches their object model. C1 is **partially shadowed**: the approval-workflow muscle (governed submission→review→approval→books-and-records) demonstrably sells (Red Oak, Veeva), but it governs assets, not executable policy, and compiles to nothing — C1's differentiation must therefore be stated as "governs the *policy that decides*, not the *copy that persuades*," or procurement will map it onto the existing ad-review line. The real absorption risk is **budget-name collision**: a GC/CCO pitched "promotional compliance" will point at PerformLine/Red Oak/Sedric line items and ask why this isn't that. The counsel bottleneck this category relieves is the *content-approval* bottleneck; the *legal-change-to-production* bottleneck (counsel position → running rules) remains untouched by every vendor examined.

### 2.2 Does any vendor maintain jurisdiction-specific promotional-law rulebooks as a product (the C2 shape — assignment brief's "Candidate 1 shape" — even if only for ad copy)?

**At regulator/country granularity for ad copy: yes, three.** Red Marker sells regulator-scoped libraries ("FINRA Marketing Compliance," "FCA Marketing Compliance," "Australian Retail Banking"), maintained by vendor implementation teams, including "unclear promotions" checks. Haast ships framework agents including **UK Gambling Commission LCCP / age verification / responsible gaming** — gambling-advertising law as maintained product content. Sedric ships built-in regulation libraries across 14 named US/UK/EU frameworks. PerformLine's rulebooks are the deepest editorial operation but are organized by federal act and industry, not by jurisdiction. [MKTCOMP-004, -014, -028, -031]

**At US-state granularity, for promotional conduct, with provenance and effective-dating: no vendor, anywhere.** No state sweepstakes/prize-law packs, no bonusing-rule packs, no registration/bonding logic, no per-rule citations exposed, no effective dates, nothing executable by an engine. The C2 gap survives this category intact — **but the category proves the business model**: compliance buyers demonstrably pay recurring subscriptions for vendor-curated regulatory rulebooks applied automatically by software (PerformLine at top-10-bank scale since 2007; Red Marker sustained three owners; Haast attracting enterparts). The editorial+software hybrid works commercially; what no one has done is point it at conduct law, state granularity, or an execution engine.

### 2.3 Which vendor is the most dangerous flanker to the surviving candidates, and why?

**PerformLine — against C1/C2** (not C4). It owns the adjacent budget line at the exact target accounts (6 of top-10 US banks, fintech/BNPL/mortgage), it is the only vendor that has proven curated-rulebook-subscription economics at enterprise scale, it already claims corpus-level provenance ("crafted from regulatory bulletins… settlements") and per-finding "regulatory basis," it monitors State AGs as a signal source, and it just raised (Jan 2026) explicitly for AI expansion. If PerformLine extended its editorial operation to state promotional-conduct packs and bolted a counsel-approval step onto its existing workflow engine, it would be selling a C2-lite to installed buyers before a new entrant finishes its first jurisdiction pack. Its constraints — no engine, no runtime, content-DNA, UPL exposure the moment rules become conduct — keep this a flank, not an occupation. [MKTCOMP-002, -003, -010, -012]

Runner-up: **Sedric** — fastest vocabulary convergence ("policies → preventive/detective/corrective controls," "exam-ready by design"), C4-overlapping customer list (eToro, WebBank), real-time intervention muscle (agent assist), fresh capital. It crowds C4's *sales conversation* ("we already have a compliance platform") without crowding its object model. Against **C4 specifically, no vendor in this category flanks** — the dangerous C4 flankers remain GeoComply/Socure from the main study. Against **C3**, none: this category's archives hold content-review history, not decision evidence. [MKTCOMP-027, -028, -029]

---

## 3. Verdicts (per vendor, ≤100 words each)

| Vendor | Verdict |
|---|---|
| PerformLine | **MAJOR OVERLAP** (budget/buyer/model overlap with C1/C2) |
| Red Marker (IntelligenceBank) | **COMPLEMENT** |
| Saifr (Fidelity) | **COMPLEMENT** |
| Red Oak Compliance | **SUBSTITUTE** (perception-level, for C1's workflow half) |
| Sedric | **MAJOR OVERLAP** (C4 accounts, C1 vocabulary) |
| Haast | **COMPLEMENT** (watch for C2-side entry) |
| Luthor | **LOW RELEVANCE** (watch) |
| Proofpoint Patrol | **LOW RELEVANCE** |
| Smarsh / Hearsay (Yext) | **LOW RELEVANCE** |
| Veeva Vault PromoMats | **LOW RELEVANCE** (as threat; high value as archetype) |
| AdComplyRx | **LOW RELEVANCE** |
| Riskified / Signifyd | **LOW RELEVANCE** (excluded — out of category) |

**PerformLine — MAJOR OVERLAP.** Owns the "marketing compliance" budget at C1/C2's target buyers (6 of top-10 US banks), and has run the curated-rulebook-plus-automated-application model profitably since 2007 — the commercial proof AND the incumbent objection for C2. Stops precisely at the seam: federal-act ad-language rules, advisory content verdicts, no state packs, no promotions/sweepstakes coverage (verified absent), no runtime, no counsel attestation. Not a C4 threat. The most credible fast-follower into conduct-content if a C2 wedge shows the budget — and the first name procurement will raise. [MKTCOMP-002, -004, -011, -013]

**Red Marker — COMPLEMENT.** Proves regulator-scoped, vendor-maintained rule libraries (FINRA/FCA/AU-banking, "unclear promotions" checks) sell across three owners — validating C2's editorial model at country granularity. Async asset-scanning API, approvals module, marketing-ops owner (IntelligenceBank) pulling it deeper into the asset workflow. No conduct rules, no state granularity, no provenance product, no runtime. Kaplan's exit is mild negative signal on regulatory-content economics at this scale. Poses no displacement risk to any candidate; useful as pattern evidence and a potential rule-content partner. [MKTCOMP-014, -015, -016, -017]

**Saifr — COMPLEMENT.** Fidelity-incubated detection brain for securities-marketing language (FINRA 2210/SEC 482/Marketing Rule), trained on 20+ years of institutional review data; the category's most embeddable asset (scanning API, Azure model catalog, Adobe/ServiceNow). Its rules are model weights, not citable propositions — the inverse of C2's provenance requirement — and its scope is communication law, not conduct. Relevance: proves regulated-industry buyers accept vendor-maintained regulatory judgment delivered as software; a plausible acquirer/partner for content-layer plays; no candidate overlap in object model. [MKTCOMP-018, -019, -020]

**Red Oak — SUBSTITUTE (perception-level, C1 only).** 1,800+ firms and half the top-20 asset managers buy its governed submission→review→approval→FINRA-filing pipeline with books-and-records retention — the closest existing analog to C1's approval workflow, priced and procured. It governs documents, not executable policy; rules are the customer's own; nothing compiles to an engine. Threat is in the sales conversation: financial-services buyers will map C1 onto "our Red Oak" until the executable-policy difference is demonstrated. Also strong evidence that governed-approval-workflow WTP is real. [MKTCOMP-024, -025, -026]

**Sedric — MAJOR OVERLAP.** Occupies C4's exact fintech/trading accounts (eToro, WebBank, NinjaTrader) with a compliance platform whose language — policies translated into "preventive, detective, and corrective controls," "exam-ready by design," real-time agent guidance — is one step from C1's pitch, backed by $18.5M. Object model is still content and conversations; no transaction rails, no eligibility state, no jurisdictional conduct content. Raises C4's sales bar ("we already have a compliance platform") and could credibly add marketing-adjacent conduct features; watch its roadmap more closely than any peer except PerformLine. [MKTCOMP-027, -028, -029]

**Haast — COMPLEMENT (watch).** Pre+post review with vendor-shipped framework agents, uniquely including gambling advertising law (UK LCCP, age verification, responsible gaming), configured attorney-led. That is jurisdiction-scoped promotional-marketing content productized — the C2 pattern proven in C4's vertical, at the ad-copy layer, UK-only. No US state packs, no conduct rules, no runtime, thin public audit depth. If Haast built US state sweeps/gaming content, it would be entering C2's beachhead from the content side; today it is pattern evidence and a flank to monitor. [MKTCOMP-030, -031]

**Luthor — LOW RELEVANCE (watch).** Seed-stage (YC 2024, ~$500K reported), RIA-scale traction (~$5.7B client AUM), pre-publication scanning against FINRA/FTC/FCA/UDAAP/GDPR plus customer policies, ex-SEC-attorney oversight. Its "AI compliance infrastructure for regulated marketing" framing shows new entrants reaching for the infrastructure *name* while still building content review. No API, no conduct scope, placeholder-grade public metrics. Re-check at Series A. [MKTCOMP-022, -023]

**Proofpoint Patrol / Smarsh / Hearsay (Yext) — LOW RELEVANCE.** The comms-governance camp: capture, archive, supervise, and (Patrol only) auto-delete published content, with FCA/FINRA/SEC/IIROC policy templates. Post-hoc, content-object, e-discovery-oriented. Smarsh confirmed as not reviewing marketing pre-publication (third-party, consistent with its own product nav); Hearsay consolidated into Yext's digital-presence suite. Value to the project: WORM comms archiving is ledger evidence that compliance-evidence budgets exist — supporting C3's WTP analogy — while leaving decision evidence entirely unowned. [MKTCOMP-032, -033, -034]

**Veeva Vault PromoMats — LOW RELEVANCE as threat; the category's proof-ceiling.** Pharma runs a mandatory, hard, pre-publication gate — MLR review, claim-to-reference provenance, versioned lifecycle with withdrawal, automatic eCTD packages to the FDA — as industry-standard software (Moderna, J&J, GSK). Every C1 mechanic (counsel-grade reviewers in-path, provenance, regulator packaging) is proven buildable and fundable where a regulator compels it — and even here, the object never becomes an action. No presence in the candidates' verticals; zero displacement risk; maximal precedent value. [MKTCOMP-035]

**AdComplyRx — LOW RELEVANCE.** 2–10-person pharma SEM ad-verification firm: post-publication monitoring of live paid-search ads against FDA standards plus a Chrome extension, positioned around the latency of PromoMats-style MLR reviews. Demonstrates the category's long tail is channel-sliver monitoring orbiting the big gates. No rulebook product, no workflow depth, no runtime, no candidate overlap. [MKTCOMP-036]

**Riskified / Signifyd — LOW RELEVANCE (excluded).** Ecommerce fraud/chargeback-guarantee/policy-abuse decisioning; no marketing-content compliance product in their positioning (inference; direct fetch blocked 403). Their runtime-decisioning precedent was already priced into the main study's fraud-stack analysis; nothing here changes it. [MKTCOMP-038]

---

## 4. Implications for the red team

1. **RT question 7 is now answered on evidence.** Bull half confirmed: curated-rulebook + automated-review is bought at top-10-bank scale (PerformLine), across three owners (Red Marker), with mandatory-budget hardness in pharma (Veeva) — the editorial+software hybrid C2 needs is commercially proven. Bear half *narrowed, not eliminated*: the "promotional compliance" line item is spoken for **only at the content-review layer**; PerformLine's rulebooks verifiably exclude promotions/sweepstakes conduct law and all state-level packs [MKTCOMP-011, -013]. Buyer interviews should still ask the budget-mapping question verbatim — the collision is over the budget *name*, not the capability.
2. **C1 must be positioned against Red Oak/Veeva perception** ("approval workflow already exists") by leading with what no ad-review tool has: executable policy as the approved object, compile-to-engine, effective-dated activation, attestation of *rule* changes rather than *asset* approvals.
3. **C3 gains an analogy upgrade:** the comms-archiving budget (Smarsh-class WORM retention, Patrol's archive-everything) is now ledger evidence, not manager knowledge [MKTCOMP-032, -033] — but decision evidence remains unowned by every vendor in both studies.
4. **C4's flank map is unchanged** — nothing in this category touches actions; GeoComply/Socure remain the threats. One addition: Haast's LCCP content shows gambling-marketing rule packs are already a product; a C4/C2 build should expect ad-copy-layer content vendors in gaming accounts and design the conduct-layer boundary crisply. [MKTCOMP-031]
5. **Two watchlist entries:** PerformLine's Jan-2026 AI war chest pointed at expansion [MKTCOMP-010]; Sedric's policy-to-controls trajectory at C4's accounts [MKTCOMP-028, -029].

---

## 5. Evidence index

38 records in `outputs/evidence/17_marketing_compliance_supplement.jsonl`: PerformLine MKTCOMP-001–013; Red Marker 014–017; Saifr 018–021; Luthor 022–023; Red Oak 024–026; Sedric 027–029; Haast 030–031; Proofpoint 032; Smarsh 033; Hearsay/Yext 034; Veeva 035; AdComplyRx 036; category/scope 037–038. Source mix: official product/marketing pages (majority), one official API doc (Red Marker), press/tracker third-party for ownership and funding (Yext/Hearsay, IntelligenceBank/Red Marker, Luthor). All accessed 2026-08-18. Inferences are labeled inline (PerformLine advisory-gate, Red Oak rule-authorship, Riskified exclusion, all Q6 expansion judgments).
