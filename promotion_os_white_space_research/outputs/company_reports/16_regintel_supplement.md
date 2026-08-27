# Supplemental Report 16 — Regulatory-Intelligence / Regulatory-Content Vendors

Researcher: Supplemental Research Agent 16 (RegIntel category)
Date: 2026-08-18
Assignment: Chief Synthesis §6.1 coverage gap — stress-test Candidate 2 ("jurisdictional policy content network", score 80, competitive gap 5) and Candidate 1 (counsel-governed policy lifecycle) against the regulatory-intelligence/content vendor class, plus the Avalara analogy (red-team question 2) and the content-side-entry question (red-team question 4).
Method: official product pages and docs via WebFetch, corroborating press via WebSearch; evidence ledger at `outputs/evidence/16_regintel_supplement.jsonl` (REGINTEL-001…037). The 100-square scoring and 17-section template do not apply to this supplement (per assignment). Inference is labeled as inference throughout.

**Headline finding (stated plainly up front):** The candidate's premise survives only in a narrowed form. As a *category* claim — "no vendor sells maintained, provenance-linked, machine-readable regulatory rules with runtime decisioning" — it is **wrong**: Droit (acquired by FIS, March 2026) sells exactly that shape for capital-markets conduct, and Apiax sells exactly that shape — a binary "is this action allowed in this jurisdiction?" API, including for **marketing/solicitation conduct** — across 190+ countries. What remains true, and verified here, is the *vertical* claim: no vendor ships executable regulatory content for promotional/sweepstakes/incentive conduct, and the gambling-vertical content incumbent (Vixio) is prose-plus-workflow with no API of any kind. Details per vendor below.

---

## Reading guide

| Vendor | Output type | Decision/authz API | Verdict |
|---|---|---|---|
| Vixio | Prose intelligence + structured obligations library + workflow tasks | No (none marketed) | MAJOR OVERLAP |
| Regology | AI law library + alerts + compliance workflows | No | COMPLEMENT |
| Compliance.ai (→ Archer Evolv) | Expert-validated obligations + RCM workflow; content API | No (content API only) | LOW RELEVANCE |
| Thomson Reuters Regulatory Intelligence | Prose alerts/analysis (divested to CUBE) | No | LOW RELEVANCE |
| CUBE (incl. TRRI, Oden, Reg-Room/Reg-Track) | AI-enriched regulatory content, alerts, mapping | No | LOW RELEVANCE (watch M&A) |
| Ascent / AscentAI | Obligations register + change impact | No | LOW RELEVANCE |
| Reg-Track (Reg-Room, now CUBE) | Tracking database + summaries + alerts | No | LOW RELEVANCE |
| **Droit (FIS)** — discovered | **Machine-executable regulatory logic; real-time decisions** | **Yes — API-first, traceable to source text** | MAJOR OVERLAP |
| **Apiax** — discovered | **Binary digital rules ("do's and don'ts without grey zones")** | **Yes — REST API + MCP** | MAJOR OVERLAP |
| Norm Ai — discovered | Regulations embedded into AI compliance agents | Unclear (agent workflow, not documented API) | COMPLEMENT (watch) |
| Avalara / Sovos / Vertex | Maintained tax content + real-time calculation engine | Yes (tax calc APIs) | LOW RELEVANCE as competitor; decisive precedent |

---

## 1. Vixio Regulatory Intelligence

**Q1 — Actual output.** Prose and near-prose: "Regulatory Updates" (horizon scanning), "Jurisdiction Reports," "Reg Analysis," "Requirements Extraction," "Regulatory Mapping," a "Technical Compliance" toolset, plus an **Obligations Library** and task/project-tracking workflow. Research deliverables are downloadable PDFs (e.g., *US Sweepstakes Guide 2024*, a prose state-by-state legality analysis for sweepstakes casinos). No machine-executable artifact of any kind is marketed. (REGINTEL-001, -003, -004)

**Q2 — Decision/authorization API.** **No.** No API, data feed, or machine-readable delivery is mentioned anywhere on the platform, gambling-compliance, or product pages checked; delivery is dashboards, reports, alerts, and task assignment. No roadmap or marketing claim of decisioning found. The closest structured motion is VIQ (AI assistant) doing "requirements extraction and regulatory mapping" — an on-ramp from prose to structure, not to execution. (REGINTEL-005, -001)

**Q3 — Content maintenance.** "Expert-led, AI-powered": **"20+ Domain specialist analysts"**, marketing cadence claim of **"1 update every 86 seconds"**, monitoring **"200+ jurisdictions in real time"** and "1,400+ regulatory authorities." Citation/provenance methodology is not published on the pages checked (analyst-curated; obligations presumably cite sources, unverified). (REGINTEL-002)

**Q4 — Verticals/jurisdictions; promotions coverage.** Two verticals only: **gambling** (operators, suppliers, PSPs, regulators, law firms) and **payments/financial services**. Gambling coverage spans licensing, advertising, AML, responsible gambling across 180–200+ jurisdictions. **Sweepstakes are explicitly covered as a research topic** — the *US Sweepstakes Guide 2024*, a "Regulatory Review: Sweepstakes in the U.S." blog, and coverage of the Michigan Gaming Control Board's first cease-and-desist actions against sweepstakes operators (Sept 2023). This is the promotion-adjacent content the candidate needs — in prose. (REGINTEL-003, -004)

**Q5 — Buyer, pricing, traction.** Compliance/legal/regulatory-affairs teams at operators, suppliers, PSPs; also regulators and law firms. "500+ global customers"; named: **Bally's Corporation** (20 casinos), **Inpay** (45+ countries). No public pricing (subscription sales). (REGINTEL-003, -006)

**Q6 — Build-down threat.** Highest in class for Candidate 2's beachhead. Vixio owns the exact buyer, the exact vertical content ops, and already sells an obligations library and requirements-extraction AI — i.e., it is one product decision away from "machine-readable obligations packs." What it lacks: engineering/API DNA (no API of any kind today), executable-rule tooling, and a decisioning liability posture. *Inference:* a Vixio executable-content product is a 12–24-month build if prioritized; there is **no evidence it is moving that way** — its observable motion is prose → structured obligations → workflow, i.e., deeper into intelligence, not into execution. It is simultaneously the best acquisition/partnership target for the candidate and the fastest content-side entrant against it.

---

## 2. Regology

**Q1 — Actual output.** An AI-first regulatory platform: **Smart Law Library™** (curated primary-source law repository), Regulatory Change Agent (tracking + alerts), Compliance Agent (obligations → workflows, policies, risks, controls in GRC style), Regulatory Research Agent, and **Reggi**, a generative-AI assistant giving "plain-language summaries, multi-jurisdictional comparisons, and tailored insights." Outputs are library content, alerts, summaries, and workflow objects — not executable rules. (REGINTEL-007)

**Q2 — Decision/authorization API.** **No.** No decision API and no programmatic "is X allowed in Y" capability marketed; the product answers questions to humans (via Reggi) rather than to systems. No roadmap claim found. (REGINTEL-009)

**Q3 — Content maintenance.** "Built on proprietary, primary source regulatory data"; "continuously tracks and updates relevant regulatory content in real time"; AI-driven with an expert team assisting library curation. Scale claims: **135+ countries**, **10,000+ data sources**. Citation provenance to statutes is implied by the primary-source library model but not documented as a rule-level provenance chain. (REGINTEL-007)

**Q4 — Verticals/jurisdictions; gambling coverage.** Horizontal (banking, crypto, energy, healthcare, tech, government) **with a dedicated "Gaming & Sports Betting" vertical**: tracks "licensing, advertising, data, and responsible gaming" across US federal/state, online and land-based, "4,000+ data sources." Promotions/sweepstakes not named as a distinct domain. (REGINTEL-008)

**Q5 — Buyer, pricing, traction.** Compliance teams; logos include **KeyBank, First Citizens Bank, ServiceNow, Solventum, OSF Healthcare, North**. No public pricing. (REGINTEL-010)

**Q6 — Build-down threat.** Moderate-low. Its AI-agent architecture ("agents" for research/change/compliance) is rhetorically close to decisioning, and a "Reggi answers your system, not your analyst" pivot is conceivable (*inference*), but nothing in its positioning, buyer base (horizontal compliance teams), or gaming coverage (fin-reg-style tracking) points at runtime authorization or at promotional conduct specifically. More plausible as a content supplier/OEM or as sales-cycle noise ("we already have Regology").

---

## 3. Compliance.ai → Archer Evolv Compliance

**Q1 — Actual output.** Now "the regulatory change management and financial regulatory intelligence layer powering the Archer platform" (Compliance.ai was absorbed; existing users transitioned to **Archer Evolv Compliance**). Outputs: dashboards/alerts, **obligations extracted from raw regulatory text**, standardized RCM workflows with assigned tasks and certified reports. (REGINTEL-011, -012)

**Q2 — Decision/authorization API.** **No decision API.** It does market a **Developer Platform**: "the fastest and most comprehensive API accessible source of regulatory content" — i.e., programmatic delivery of *documents and obligations*, not of decisions. This is the only assigned regintel vendor with any API posture at all, and it is content-out, not decision-in. (REGINTEL-013)

**Q3 — Content maintenance.** The strongest documented editorial process in the class: **"Expert-in-the-Loop (EITL)"** — "130+ in-house regulatory specialists supervise and validate every obligation extraction, regulatory summary, and change alert." "AI extracts obligations. Experts verify them." Scale: 8,000+ sources, 3,000+ agencies, 230+ jurisdictions, 21M+ documents. (REGINTEL-012, -014)

**Q4 — Verticals/jurisdictions.** Banks, financial services, insurance, fintech, energy/commodities. **No gambling/promotions coverage.** (REGINTEL-014)

**Q5 — Buyer, pricing, traction.** Compliance/risk at regulated financials: **PayPal, Bremer Bank, Bank of the West, Bank of Marin, Quantcast**, "100+ regulated enterprises." Pricing undisclosed; now sold within Archer's GRC motion. (REGINTEL-014)

**Q6 — Build-down threat.** Low. Its fate is the class pattern: independent regintel gets absorbed into a GRC platform as a *layer*. Archer's incentive is feeding its own workflow/risk suite, not runtime decisioning in customers' transaction paths. The 130-specialist EITL bench is, however, the proof that **obligation-grade editorial ops at scale is a fundable, sustainable function** — the operational muscle Candidate 2 must build (its feasibility-2 dimension).

---

## 4. Thomson Reuters Regulatory Intelligence + CUBE (RegPlatform / RegBrain), incl. Reg-Room / Reg-Track

These are now one company; treated together with per-asset answers.

**Q1 — Actual output.** TRRI (as sold by TR): prose regulatory alerts and analysis tracking **2,000 regulatory bodies across 20 countries**; Oden: automated compliance content for US state insurance rules. CUBE RegPlatform: AI-enriched content — "summarisation, linkage, ontological classification, data enrichment, computations, and specialised financial services translation," automated alerts, regulatory heatmaps, mapping of changes "to your frameworks, controls, and audits." Reg-Room's **Reg-Track**: a tracking database — daily capture of rules/guidance/enforcement with summaries, source links, filters, and email alerts. All of it is intelligence + mapping, none of it executable. (REGINTEL-015, -016, -017, -019)

**Q2 — Decision/authorization API.** **No** — none marketed for CUBE, TRRI, Oden, or Reg-Track. (REGINTEL-017, -019)

**Q3 — Content maintenance.** CUBE: "Our AI powered algorithms enrich and standardise content, while our team is on hand to ensure human expertise adds precision" — **10,000+ issuing bodies, 750 jurisdictions, 80 languages** (the largest coverage claim in the class). Reg-Room was an analyst shop ("expertly curated regulatory summaries," founder Nick Paraskeva, NYC). (REGINTEL-017, -018)

**Q4 — Verticals/jurisdictions.** Financial services and insurance only (banks, insurers, investment firms, fintechs). **No gambling/promotions coverage found.** Reg-Track covers financial regulators (SEC, CFTC, FCA, MAS…) exclusively. (REGINTEL-017, -019)

**Q5 — Buyer, pricing, traction.** ~**1,000 customers** post-TRRI acquisition, across banking, insurance, asset management, payments. Hg-backed. Pricing undisclosed. (REGINTEL-016)

**Q6 — Build-down threat.** Direct build-down: low (fin-serv DNA, no execution layer, no gambling). Structural threat: **high, via M&A** — CUBE is the category's consolidator: Reg-Room (May 2024), TRRI + Oden (completed Dec 31, 2024). *Inference:* if CUBE wanted the gambling/promotions vertical or an execution layer, it would buy them (a Vixio-class or Apiax-class asset), not build. The **TR divestiture itself is signal**: the world's largest legal-content company chose to exit prose regulatory intelligence — consistent with prose regintel being a mature, consolidating, low-growth layer while value migrates elsewhere (*inference from documented transactions*). Note TR retained Practical Law (human-readable legal know-how), the other precedent named in red-team Q2. (REGINTEL-015, -016, -018)

---

## 5. Ascent RegTech → AscentAI

**Q1 — Actual output (and status).** Alive: acquired by PE firm **Edgewater Equity Partners (Jan 18, 2024)**, acquired UK horizon-scanning vendor **Waymark (Feb 2024)**, rebranded **AscentAI (Mar 2025)**; site current (© 2026). Output is a structured **obligations register**: "high confidence regulatory register… a rock-solid inventory of your corporate obligations," rule-change impact identification against that inventory, and "automated change proliferation" into GRC policies/controls. Structured data about obligations — not executable rules. (REGINTEL-020, -021)

**Q2 — Decision/authorization API.** **No.** Integrations are into GRC platforms (LogicGate, Onspring, Resolver…), not decision paths. (REGINTEL-020)

**Q3 — Content maintenance.** "RegulationAI"-branded automation; method opaque on current site. Claims: 1,000 data sources, **400,000 obligations, 98 countries**; US/EU/UK full coverage post-Waymark. (REGINTEL-020, -021)

**Q4 — Verticals.** Banks, broker-dealers, credit unions, mortgage, fintech, GRC providers. No gambling/promotions. (REGINTEL-020)

**Q5 — Buyer/traction.** Financial-services compliance; unnamed testimonials; PE-owned consolidation stage; once celebrated (2019-era awards), now quiet. Pricing undisclosed. (REGINTEL-020, -021)

**Q6 — Build-down threat.** Minimal. PE-owned, fin-serv scoped, register-shaped. Its relevance is cautionary: **"targeted obligations register" was this class's peak ambition a cycle ago, and it still plateaued short of execution** — supporting the finding that the content→execution seam is genuinely hard to cross from the content side (*inference from documented trajectory*).

---

## 6. Droit (acquired by FIS, March 2026) — discovered; critical

**Q1 — Actual output.** **Machine-executable regulatory rules driving production decisions.** Droit's Adept platform "encodes regulatory obligations as machine-executable logic that can determine whether a trade, product or activity complies with jurisdiction-specific market rules **in real time**." Now sold as **FIS Pre-Trade Compliance (formerly Droit)**, FIS ETD Reporting (formerly Droit), FIS Trade Transaction Reporting (formerly Droit): "computational law technology… interpreting complex regulations," delivering "**ready-to-trade decisions** to salespeople," automated "validation and eligibility checks," "real-time automation of complex global rules." (REGINTEL-022, -023)

**Q2 — Decision/authorization API.** **Yes — the product IS the decision API.** Official FIS pages: "**API-first automation**," "**High-performance API**." A customer's system programmatically asks, in effect, "can I trade this product, with this counterparty, in this jurisdiction, right now?" and receives a decision. This is the candidate's exact J05-shaped question in a different domain. (REGINTEL-023)

**Q3 — Content maintenance & provenance.** The load-bearing feature: "**tracing decisions back to source regulation text**," "data and policy references," "fully auditable records," "clear visualization of logic and adherence." Content originates in digitized regulatory text maintained as transparent, auditable logic models (Dodd-Frank origin, 2012; expanded to EMIR and "nearly every asset class"). Team/process details not public on pages checked; historically built with industry/dealer consensus review (*not re-verified this session — treat as background*). (REGINTEL-023, -024, -025)

**Q4 — Verticals/jurisdictions.** Capital markets only: OTC/listed derivatives reporting eligibility, **product eligibility, cross-border market access**, pre-trade permissibility; global regimes (Dodd-Frank, EMIR, CAT/FINRA, multi-asset). **No gambling/promotions.** (REGINTEL-023, -025)

**Q5 — Buyer, traction.** Tier-1 banks, trading venues, market infrastructure; investors historically included Goldman/UBS/DRW (*background*); exit: acquired by **FIS** (announced March 9, 2026, terms undisclosed) to "deliver embedded regulatory controls across trading, post-trade processing and reporting workflows" for FIS's 20,000+ clients. droit.tech now 301-redirects to fisglobal.com. (REGINTEL-022, -025, -026)

**Q6 — Build-down/expansion threat.** As a promotions competitor: negligible near-term — FIS bought it to embed in capital-markets plumbing (*inference*). As a thesis fact: decisive. It proves (a) judgment-heavy regulation compiles to executable logic with decision-level provenance; (b) customers (the most conservative buyers on earth — bank compliance) accept vendor-maintained executable regulatory content; (c) the endgame is acquisition by the infrastructure vendor that owns the transaction path — for promotions, the FIS-analog acquirers are GeoComply/Socure/FIS-like commerce rails, which sharpens the study's fast-follow concern.

---

## 7. Apiax — discovered; critical

**Q1 — Actual output.** **Binary digital compliance rules.** "Digital cross-border guidelines for **190+ countries** via an app, or seamlessly embed cross-border compliance rules into existing business processes **via an API**." "Highly granular structure with **precise do's and don'ts — and without grey zones**." A documented bank deployment gave "hundreds of account managers **yes-or-no answers** on their most frequent regulatory questions right in their existing tools." (REGINTEL-027, -031)

**Q2 — Decision/authorization API.** **Yes.** "Easily integrate digital Cross-border Compliance rules through **REST API or MCP** into your existing applications" — i.e., a customer system (or now an AI agent, via MCP) programmatically asks whether an activity is permitted for a client type in a jurisdiction and gets a deterministic answer. Domains include pre-trade checks (docs.apiax.io article exists; page 403'd this session). The question it answers — "may I **market** / solicit / onboard this client for this product in this country, in this scenario?" — is structurally the candidate's question, aimed at financial-services conduct instead of promotions. (REGINTEL-028, -027)

**Q3 — Content maintenance & provenance.** Hybrid content network: rules derive from "**digitised country manuals from leading legal content firms**" (law-firm-sourced), sold as "always up-to-date rules from premium content partners," alongside customer-maintained in-house rules; "detailed monitoring logs and audit trails on all regulatory changes." This is the exact liability structure Candidate 2 proposes — vendor digitizes, named legal-content partners stand behind substance, customer compliance adopts. (REGINTEL-029)

**Q4 — Verticals/jurisdictions.** Financial institutions: cross-border rules for wealth/asset management, CIB, retail banking, across "all types of activities (**socialising, marketing, onboarding**, etc.) and all offering scenarios (fly-in, remote meeting, professional/retail customers…)"; also product/content compliance, suitability & tax, policy compliance. 190+ countries. **No gambling/promotions.** (REGINTEL-030, -027)

**Q5 — Buyer, traction.** Compliance and front-office enablement at banks ("leading financial institutions"; documented global universal bank in Singapore). Swiss origin; scale/pricing not public. Materially smaller than Droit was (*inference from public footprint*). (REGINTEL-031)

**Q6 — Build-down threat.** Apiax itself entering promotions: unlikely — its content network is banking law firms (*inference*). The threat is the **playbook**: law-firm country manuals → binary rules → REST/MCP API is public, proven, and replicable for promotional conduct by anyone with the vertical's legal-content relationships (a promotion-law boutique consortium, Vixio, or a funded entrant). Apiax's MCP delivery also shows this class is already retooling for AI-agent consumption — the delivery surface Candidate 2 should assume, not roadmap.

---

## 8. Norm Ai — discovered; watch item

**Q1/Q2.** "Agentic law is the embedding of law into AI agents… powers the automation of legal and compliance tasks" — regulations converted into computational representations executed by AI agents (marketing-content review is its publicized use case). Public site documents no decision API; delivery is agent workflows over content/tasks, closer to PerformLine-with-teeth than to runtime action authorization. (REGINTEL-032)

**Q3–Q5.** Encoding method (legal engineers building regulation graphs) is its known model (*background; site pages fetched were thin*). Traction/capital are the story: investors include **Vanguard, Blackstone, Bain Capital, Citi, TIAA, Coatue, Khosla**; "trusted by institutions managing over $35T in combined assets"; **$1.2B valuation (June 2026 Series C)** per site. Fin-serv focus. (REGINTEL-032)

**Q6.** The best-capitalized "regulation-to-computation" company in existence. If it broadened from content review to action authorization, or from fin-serv to consumer promotions, it would be the fastest-moving mirror of all (*inference*; no evidence of either today). Red team should track it.

---

## 9. The Avalara analogy (Avalara, Sovos, Vertex) — how executable legal content became durable companies

**What the tax trio actually is.**
- **Avalara AvaTax**: real-time calculation API, "<10 ms," "12,000+ U.S. sales and use tax jurisdictions and 190+ countries," "**more than 900,000 tax rules**" maintained, "54B+ transactions processed in a year," 1,400+ signed partner integrations, entry pricing "$699 per state, per year." (REGINTEL-033)
- **Avalara Tax Research** (the content face): "fast, plain-language answers **with citations**," "**law-backed taxability answers**" with "statutory references," "links to source content," maintained by Avalara tax researchers with "government-approved changes." Provenance is a first-class product feature. (REGINTEL-034)
- **The liability structure**: Avalara's **Accuracy Guarantee** — if an incorrect AvaTax result causes a negative audit finding, Avalara pays the uncollected tax, penalties and interest, **capped at the lesser of the assessed amount or the prior 12 months' AvaTax fees**. Executable legal content is warrantable because the downside is monetary, quantified by the authority's own assessment, and cappable. (REGINTEL-035)
- **Sovos**: ~200 countries, 100K+ customers, 16B transactions/FY, "**150+ tax experts** influence regional authorities," half the Fortune 500. **Vertex**: 4,500 customers (60% of Fortune 500), 195 countries, "**20K+ jurisdictions**," "**1B+ governed rates and rules**," real-time calculation. Three durable companies on the same tripod: editorial content ops + provenance + calculation engine in the transaction path. (REGINTEL-036, -037)

**What they needed to work** (the checklist for any "Avalara of regulated conduct"):
1. **A mandatory computation point** — an invoice cannot issue without a tax amount, so the API is called on *every* transaction (54B/yr), independent of anyone's risk appetite.
2. **A single calculable quantity** — a number, not a judgment; disagreement is rare and adjudicated by the authority's assessment.
3. **Bounded, insurable liability** — the Accuracy Guarantee, cappable at fees because errors are monetized by the taxing authority.
4. **Distribution via pre-integration** — 1,400+ platform integrations; Avalara won the checkout, not the tax director's bookshelf.
5. **Editorial ops as a permanent cost center** — hundreds of researchers (150+ at Sovos alone) tracking ~20K jurisdictions forever.

---

## Category-level answers

### A. Does any vendor already combine maintained regulatory content with runtime decisioning — the top candidate's exact shape?

**Yes — and the synthesis must say so.** Two vendors, outside the studied 15 and outside this class's prose incumbents, already ship it:
- **Droit/FIS** (capital markets): vendor-maintained regulatory content compiled to machine-executable logic, a real-time high-performance decision API ("ready-to-trade decisions"), and decision-level provenance ("tracing decisions back to source regulation text"). That is Candidate 2 + Candidate 1's compile-down + Candidate 3's traceability, productized, at tier-1-bank grade, since ~2012 — and just acquired by a core infrastructure vendor (March 2026).
- **Apiax** (cross-border financial conduct, **including marketing/solicitation activities**): law-firm-sourced binary rules, 190+ countries, consumed by customer systems via REST API and MCP.
- **Avalara/Sovos/Vertex** (tax) remain the at-scale proof (900K–1B+ maintained rules behind real-time APIs).

**Consequence for Candidate 2's scores:** the "gap 5 — defended by documented refusal" claim is correct **only within the promotions/gambling conduct vertical and the studied vendor set**. At category level the shape exists, is purchasable, and its playbook is public. Competitive gap for the *shape* is ≤3; the gap that remains genuinely open is **vertical**: nobody maintains executable content for promotional/sweepstakes/bonusing conduct, and the vertical's content incumbent (Vixio) has no API at all. This *strengthens* feasibility (the shape is proven buildable and buyable — Candidate 2's weakest dimension, feasibility 2, should arguably rise) while *weakening* uniqueness (a funded team copying the Apiax playbook with promotion-law boutiques reaches parity with the candidate's core mechanism in quarters, not years). Net: the white space is real but it is a **vertical-content race**, not a category invention.

### B. Why does an "Avalara of regulated conduct" not already exist?

**Mostly structural-economic — but the "rules are too judgment-heavy to compile" version of the structural argument is now disproven.** Grounded in the checklist above:
1. **No mandatory computation point.** Tax is computed to *complete* every transaction; promotional conduct is checked only when someone fears enforcement. Demand is risk-driven and discretionary, so no vendor inherits Avalara's 54B-calls/yr economics. This is the deepest structural reason, and it is why Droit exists in capital markets: Dodd-Frank *created* a mandatory computation point (reporting eligibility/pre-trade checks banks could not legally skip) simultaneously for every dealer. Promotions has never had its Dodd-Frank moment; the sweepstakes-casino enforcement wave (Michigan C&Ds 2023 onward, per Vixio's own coverage) is the nearest analog and is exactly what would convert discretionary demand into mandatory checking.
2. **No single calculable quantity — partially true, fully survivable.** Conduct answers are conditional judgments, not numbers. But Droit compiles Dodd-Frank/EMIR and Apiax sells conduct answers "without grey zones" with law-firm backing: heterogeneous, interpretation-heavy law compiles when a named legal authority stands behind the interpretation and every answer carries provenance. The quantity problem is a liability-design problem, not a computability problem.
3. **Liability is harder to cap — the real remaining structural gap.** Avalara can warrant because tax errors are monetized by the authority's assessment and capped at 12 months' fees. A wrong "this sweepstake is legal in FL" can cost a license or trigger an AG action — not cappable the same way. The working answers, per this class: Droit (traceability + auditability instead of indemnity), Apiax (law-firm content partners carry interpretive weight), Avalara (bounded guarantee), Candidate 2's own design (customer-counsel adoption). UPL/liability is thus a solved-in-principle, unsolved-in-this-vertical design constraint — consistent with the red team owning it, not with abandoning it.
4. **No integration surface.** Avalara rode 1,400+ commerce-platform integrations; there is no standard "promotion checkout" to pre-integrate into. The nearest equivalents are GeoComply/Socure/Talon.One-class positions — which is why the fast-follow threat from those vendors (main study) and the acquisition endgame (FIS-Droit) are the same fact seen twice.
5. **Historical accident, secondarily.** Capital markets got computational law because 2010–2012 regulation was sudden, uniform, deadline-driven, and hit ~30 identical global dealers at once. Promotions law is old, accreted, state-fragmented, and enforced sporadically across thousands of heterogeneous operators — so no synchronized buying moment ever formed. That is changing at the sweeps-casino seam now, which is an argument for timing, not against the gap.

### C. Which vendor is the most dangerous mirror-threat to Candidate 1/2, and how fast could they move?

**Vixio, for the beachhead; CUBE, by M&A; the Apiax playbook, for the mechanism.**
- **Vixio** is the only vendor owning all three of: the gambling/promotions buyer (500+ customers incl. Bally's), a 20+-analyst content operation across 200+ jurisdictions, and existing sweepstakes-specific research. Its Obligations Library + VIQ requirements-extraction is prose already halfway to structure. *Inference:* if it decided to ship "executable obligations packs + API," the content half would take it 12–24 months; the engineering/liability half is foreign to it (no API of any kind today, no execution motion visible). It is simultaneously Candidate 2's best supplier/partner/acquirer and its fastest content-side attacker. Speed rating: fastest in class, gated by strategic will, not capability.
- **CUBE** will not build into gambling/promotions (fin-serv DNA, no vertical coverage) but has bought its way to 750 jurisdictions and ~1,000 customers in under two years (Reg-Room, TRRI, Oden). *Inference:* the moment executable content in any vertical shows revenue, CUBE (Hg-backed) is the consolidator that buys it — a threat to the candidate's independence, and equally its exit.
- **The Apiax playbook** is the mechanism-level threat: digitize the promotion-law boutiques' 50-state manuals into binary rules behind a REST/MCP API. Apiax proves the model works and even how to price the trust problem (named legal-content partners). Anyone — including Vixio, a law-firm consortium, or a new entrant — can now run this play in the promotions vertical; Candidate 2's defensibility must come from getting the vertical's content network locked up first, not from the mechanism.
- (**Norm Ai** is the wildcard: $1.2B of capital pointed at "embedding law into AI agents," today in fin-serv content review. Watch, not fear, for now.)

---

## Verdicts (≤100 words each)

**Vixio — MAJOR OVERLAP.** Owns Candidate 2's beachhead content and buyer wholesale: gambling/payments regulatory intelligence, 20+ analysts, 200+ jurisdictions, 500+ customers including Bally's, explicit sweepstakes state-by-state research. Ships prose, obligations, and workflow only — no API, no executable artifacts, no visible execution roadmap. It is the fastest plausible content-side entrant against the candidate, its most natural supplier/partner/acquirer, and the incumbent every sales call will name. Overlap is on the content asset, not the product shape; the seam (executable delivery, decisioning, provenance-to-runtime) remains unowned by it. (REGINTEL-001…-006)

**Regology — COMPLEMENT.** Horizontal AI regulatory-intelligence platform (Smart Law Library, Reggi assistant, change/compliance agents) with a real gaming & sports-betting vertical tracking licensing/advertising/responsible-gaming across US jurisdictions. No decision API, no executable rules, no promotions-specific depth. Plausible content/OEM supplier for jurisdiction packs and a mild sales-cycle confuser ("we already track gaming rules"), not a competitor for the executable layer. Fortune-500-adjacent logos (KeyBank, ServiceNow) prove horizontal budget, not vertical conduct budget. (REGINTEL-007…-010)

**Compliance.ai / Archer Evolv — LOW RELEVANCE.** Financial-services RCM absorbed into Archer's GRC platform; obligations extraction validated by 130+ in-house specialists; content API only, no decisioning; no gambling/promotions coverage. Matters as (a) proof that expert-in-the-loop editorial ops scale commercially, and (b) the class's default fate — becoming a layer inside someone's GRC suite. (REGINTEL-011…-014)

**Thomson Reuters Regulatory Intelligence — LOW RELEVANCE.** Divested: sold with Oden to CUBE (completed 2024-12-31); its URL now redirects to cube.global. Was prose alerts/analysis over 2,000 regulatory bodies in 20 fin-serv countries. TR exiting prose regintel while keeping Practical Law is signal that the standalone prose layer is mature/consolidating. No bearing on promotions except as precedent. (REGINTEL-015, -016)

**CUBE (RegPlatform, incl. Reg-Room/Reg-Track) — LOW RELEVANCE (watch M&A).** Largest coverage claim in class (10,000+ issuing bodies, 750 jurisdictions, 80 languages; ~1,000 customers), AI-enriched prose and mapping, no decision API, no gambling. Direct threat: none. Structural threat: it is the category's consolidator (Reg-Room May 2024; TRRI/Oden Dec 2024) and the most likely acquirer of whichever vendor first proves executable-content revenue — including the candidate. (REGINTEL-016…-019)

**Ascent / AscentAI — LOW RELEVANCE.** Alive but PE-owned (Edgewater, Jan 2024; Waymark bolt-on; AscentAI rebrand Mar 2025). Obligations registers and change impact for fin-serv; 400K obligations, 98 countries; no decision API. Cautionary datapoint: the class's most-hyped "targeted obligations" innovator a cycle ago still stopped short of execution — evidence the content→execution seam resists crossing from the content side. (REGINTEL-020, -021)

**Reg-Track (Reg-Room) — LOW RELEVANCE.** Fin-serv regulatory tracking database (summaries, source links, alerts) with no API, no gambling coverage; acquired by CUBE May 2024. Covered within the CUBE verdict. (REGINTEL-018, -019)

**Droit / FIS — MAJOR OVERLAP (existence proof, adjacent vertical).** Ships the candidate's exact shape since ~2012: regulatory text maintained as machine-executable logic, real-time API-first permissibility decisions ("ready-to-trade"), every decision traceable to source regulation text — for capital markets, at tier-1 banks, now embedded in FIS infrastructure (acquired March 2026). Not a promotions competitor and unlikely to become one; but it falsifies "no one ships executable regulatory content," proves conservative buyers accept vendor-maintained executable law, and demonstrates the endgame: acquisition by the vendor owning the transaction path. (REGINTEL-022…-026)

**Apiax — MAJOR OVERLAP (mechanism-identical, adjacent vertical).** Sells binary "may I do X in jurisdiction Y for client type Z" digital rules — explicitly covering **marketing** and onboarding activities — across 190+ countries, delivered via REST API and MCP, built from digitized law-firm country manuals with audit trails. This is Candidate 2's product mechanism and liability structure, live in financial services. Its own entry into promotions is improbable (banking-law content network), but it collapses the "conduct rules can't compile" defense and hands every would-be entrant a public playbook. (REGINTEL-027…-031)

**Norm Ai — COMPLEMENT (watch).** "Agentic law": regulations embedded into AI agents automating legal/compliance tasks (fin-serv content review focus). No documented decision API; not in promotions. But $1.2B valuation (June 2026), investors including Vanguard/Blackstone/Citi, customers managing $35T — the best-capitalized regulation-to-computation company anywhere. A pivot toward action authorization or consumer-conduct domains would make it the fastest mirror; no evidence of either today. (REGINTEL-032)

**Avalara / Sovos / Vertex — LOW RELEVANCE (as competitors); decisive precedent.** Maintained tax content (900K–1B+ rules, 12K–20K+ jurisdictions) behind real-time calculation APIs at 16B–54B transactions/year, with citation-linked research products and a bounded Accuracy Guarantee (penalties/interest capped at 12 months' fees). Proves executable legal content sustains multi-billion-dollar companies when there is a mandatory computation point, bounded liability, and pre-integrated distribution — the three conditions promotions conduct lacks today and the candidate must engineer substitutes for. (REGINTEL-033…-037)

---

## Implications for the candidate set (summary for red team)

1. **Candidate 2's gap-5 must be restated as a vertical gap.** "No vendor sells maintained, provenance-linked, machine-readable rules" is false at category level (Droit, Apiax; tax trio). True statement: *no vendor sells them for promotional/incentive/gambling-adjacent conduct, and the vertical's content incumbents are prose-only with no API.* Gap for the shape: proven and replicable; gap for the vertical content network: still open and still defended mainly by incumbent disinterest.
2. **Feasibility should rise, defensibility should fall.** Droit/Apiax prove compilability of judgment-heavy conduct law (Candidate 2's feasibility-2 was scored against a fear that is now disproven); the same proof means the mechanism confers no moat — only locked-up vertical content relationships (promotion-law boutiques, Vixio-class ops) do.
3. **The UPL/liability gate has three working precedents** (Droit traceability, Apiax law-firm partners, Avalara bounded guarantee) — none is customer-counsel adoption exactly, but together they show the gate is a design problem with known solutions, not a category killer.
4. **The consolidation clock is running.** Prose regintel is rolling up (CUBE×3, Archer, Edgewater); the one executable vendor was just taken by FIS at the infrastructure layer. Whoever builds executable promotions content should expect Vixio/CUBE/GeoComply-class interest within one product cycle — as threat and as exit.
5. **Timing argument strengthened, not weakened.** Capital markets got its computational-law company only after a synchronizing regulatory shock. The sweeps-casino enforcement wave is the promotions vertical's first such shock; Vixio is documenting it in prose while nobody ships it as rules.

*End of supplemental report 16.*
