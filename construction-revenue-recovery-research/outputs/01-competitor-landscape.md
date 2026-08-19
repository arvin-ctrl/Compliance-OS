# 1. Competitor Landscape

*Research window: August 2026. Every claim in the underlying reports carries a source URL; see `research/raw/`.*

## The map in one paragraph

Nobody sells the thesis pipeline. The market splits into six layers, each of which owns a
*fragment* of "contract → event → entitlement → evidence → value → claim package", and every layer
stops at the same place: **the point where somebody has to assert that one party owes another party
money.** That stop is consistent across five countries, six vendor categories and twenty-plus
products, which makes it a structural property of the market rather than a roadmap accident.

---

## Layer 1 — Platforms of record

| Company | Position | Relevance | Posture to a startup |
|---|---|---|---|
| **Procore** | $1.32B revenue FY2025, 17,850 customers, 27% of revenue to R&D | Richest contemporaneous record set in construction. Shipped **Change Analysis Agent** GA 23 Jul 2026 — scope impacts, cost exposure, schedule risk from changes/RFIs/drawings/specs | **Hostile.** Revoked Trunk Tools' API access Sept 2025; Developer Policy (30 Sep 2025) forbids parsing and database-building |
| **Autodesk Construction Cloud** | AECO $3,583M, +22% YoY | Deep PCO→RFQ→COR→OCO→SCO chain; native email Correspondence; RFI AI auto-populates cost/schedule impact | **Most open.** Data Connector exports the evidence graph as free CSV *including relationship edges* |
| **Oracle** (Aconex, P6, Unifier, Textura) | ~$1.2B paid for Aconex 2017; $9T project value claimed | Aconex is the best contemporaneous correspondence register on earth; deadline tracking scores a full 3 | **Structurally frozen.** Neutrality is the product ("there is no super user") |
| **Trimble** (e-Builder, Viewpoint, ProjectSight) | AECO ARR $1,577M, +14% organic | Owns both sides — contract text, job cost, subcontract ledger *and* the owner's PMIS | **Acquirer.** Bought Document Crunch for $246.4M, closed 4 Apr 2026 |
| **InEight** | 850+ companies, $1T+ of projects | Change + Document + Contract; mail with response-period tracking; FedRAMP Moderate | **Partner.** No marketplace, no AI surface shipped as of Aug 2026 |

## Layer 2 — Contract intelligence

| Company | What it does | The boundary |
|---|---|---|
| **Document Crunch** (Trimble, Apr 2026) | Clause extraction, playbooks, risk scoring, **agentic notice/RFI generation since Jun 2026**. 10,000+ projects, 500+ contractors | **Never crossed the data boundary.** Ingests contracts, specs, addenda, flow-downs, drawings — *and nothing else*. Its Procore app requests **zero data permissions** |
| **Trunk Tools** | $40M Series B, ~$70M raised, Gilbane 200+ projects. Document QA, Cortex (2M+ labelled artifacts) | Gives contract clause extraction away **free** as lead-gen. No email connector, no daily-log agent, no claims surface |
| **Horizontal CLM** (Icertis, Sirion, Agiloft, Luminance, Robin AI) | Obligation extraction + deadline alerting at full maturity, ~$88k median ACV | **Zero construction systems** in Icertis' integration list. No RFI, daily report or schedule ingestion anywhere |

## Layer 3 — Commercial workflow

| Company | What it does | The boundary |
|---|---|---|
| **Clearstory** (= Extracker; rebranded Jun 2023) | T&M tags, CORs, change order logs. **$2.1B/month** in CORs, 14,000+ contractors, 13 of NA's 25 largest GCs. $35M raised | Published doctrine refuses entitlement: a T&M tag *"only proves the work happened and the hours are correct."* COR Pricing Agent in closed beta 28 May 2026 |
| **Payments/AR/lien** (Siteline, Levelset, Handle, Built, Flashtract, GCPay) | Statutory deadline tracking, pay apps, compliance document collection | Levelset sold to Procore for **$484.1M** — but the **filing** was the revenue ($59/notice, $349/lien), not the alert |
| **Field capture** (HCSS, eSUB, Raken, Fieldwire) | Daily reports, time cards, production vs plan | **Zero contract ingestion, zero clause extraction, zero notice detection** across all seven vendors |

## Layer 4 — Schedule and delay

| Company | What it does | The boundary |
|---|---|---|
| **SmartPM** | Automated schedule analysis. Essentials $12,000/yr, Controls $25,000/yr | Open API gives away *"raw schedule data and all the metrics we calculate… No extra fees. No limits."* Stops exactly where entitlement begins |
| **nPlan** | ML on 750,000+ programme files, $2Tn spend. $16M Series B Oct 2025 | Owner buyers (HS2, Network Rail, Chevron, Shell) — i.e. the defendants |
| **Deltek Acumen, Steelray, Ron Winter** | AACE half-step arithmetic | Steelray states it outright: *"The tool does not attribute responsibility to parties"* |

## Layer 5 — AI-native claims (the direct cohort)

| Company | Reality check |
|---|---|
| **Gather** (UK, ex-Rail Diary) | Closest to the thesis anywhere. Detects NEC compensation events off diaries, drafts clause-cited notices, 10M+ records, £25bn+ project value. **But: does not do quantum ("to be calculated"), and across 11 case studies documents zero recovered CEs in £.** 10 staff, down from 14 |
| **CEMAR / FastDraft / Sypro / Contract Bee** | Mature NEC administration. CEMAR at **£435/licence/month** across £75bn of works. **All administer events after a human identifies one. None detects** |
| **Magra, Lexilio, ClaimMaster.ai, Aven-AI, Delay Claim Builder** | Demoware. Magra's headline moved **$240K → $17,824 per event**; all 8 integrations still "Upcoming"; zero named customers |
| **Contradic (FR), BauAgent (DE), ContraVault (IN)** | Real products, **all score 0 on quantum** |
| **Easyclaim (DE)** | €599/case, 21-page derivation across 26 cost categories. **The only good quantum engine found in any language — and it has no AI, no ingest, and runs as a single offline HTML file** |

## Layer 6 — The true incumbent: claims consultants

HKA, J.S. Held, Ankura, Secretariat, Exponent, BRG, FTI, RLB, Arcadis, Turner & Townsend, Diales.

- Score **3 across the entire recovery pipeline** — but as human-delivered work that starts *after* the loss.
- Published rates **$225–$1,375/hr**; FTI realised **$442/hr** at 57% utilisation.
- A full delay + quantum claim on a $5–25m dispute: **600–1,650 hours / $240k–$660k**, of which **200–600 hours is document review and chronology**.
- **Diales — the only listed pure-play — converts £43.0m of revenue into £1.4m of operating profit. A 3.3% margin.** That is what no product leverage looks like.
- HKA's CRUX dataset only counts a project once **30+ hours** of claim work exists. **They structurally cannot see the pre-dispute phase.**

---

## Five structural findings

1. **Two marketplaces, one void.** Procore lists 455–539 apps and Autodesk 194 partners. **Neither has a single claims, entitlement or delay vendor.**
2. **The front half is free.** Clause extraction and deadline listing are given away by Trunk Tools, shipped natively by Procore (May 2026), and owned by Trimble via Document Crunch. Notice drafting is commoditised at $18–30/user/month.
3. **The back half is empty everywhere.** Causation is standards-blocked. Quantum scores 0–1 across every product in every language.
4. **Nobody detects from passive project data.** German trade press names it a 2026 trend and credits no vendor with it.
5. **Everyone stops at the same line.** Datagrid (a Procore company) writes it down: *"entitlement and approval stay with the responsible project professionals."*
