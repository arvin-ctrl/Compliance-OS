# 17 — NON-ENGLISH MARKETS: Construction Claims / Change-Order / Entitlement Software

**Agent:** gap-fill 17 · **Date of research:** 19 Aug 2026 · **Assigned gap:** "non-English markets, especially German `Nachtragsmanagement`, are under-covered."

**Scope covered:** Germany (deep), Austria, Switzerland, France (deep), Spain/LatAm, Italy, Netherlands, Sweden, Norway, Poland, Turkey, GCC/Qatar, India, Japan, Korea, China.

**Search languages used:** German, French, Spanish, Italian, Swedish, Norwegian, Dutch, Polish, Turkish, Japanese, Korean, Chinese.

---

## 0. EXECUTIVE ANSWER TO THE THREE KEY QUESTIONS

### Q1. Does a mature non-English product already implement the full thesis pipeline?

**No — but the pipeline exists, split across two countries and three products, and nobody has assembled it.**

The single most important structural finding of this pass:

| Pipeline stage | Best non-English implementation | Country | Maturity |
|---|---|---|---|
| Event detection (from project data) | **Contradic** — cross-document detection of "événements clés, retards, changements de périmètre" | FR | Founded **1 Aug 2025**, pre-Series-A |
| Entitlement matching | **BauAgent.ai** — classifies a site message into §2 / §4 / §6 VOB/B | DE | **Closed beta** |
| Evidence / contemporaneous graph | **Contradic** (cross-doc chronology) + **SmartClaim** (blockchain-anchored site evidence) | FR | Beta |
| Recoverable-value estimation | **Easyclaim / Nachtragsmanager** (C. Abraham GmbH) | DE | **Shipping since 2017, court-tested** |
| Notice / claim package generation | **BauAgent.ai** (notices) + **Easyclaim** (21-page quantum submission) | DE | Shipping |

No single product spans more than roughly half of it. **The two halves are separated by a language border and by product philosophy**: France has the AI event/evidence layer with **zero quantum**; Germany has the world's best productised quantum engine with **zero event detection**.

> **Could they expand into the US/UK?** Contradic is the only real candidate and it is not trying: no English/US market signal found, the founder interview names energy and law firms (not BTP/construction) as the beachhead, and a funding round is only *planned* for 2026. Easyclaim is a one-man Sachverständigenbüro whose entire product is hard-coded to §642 BGB / §2 Abs. 3 VOB/B German cost law — it is **legally non-portable**. BauAgent.ai is hard-coded to VOB/B paragraph numbers and to WhatsApp (a channel that is not the German-market-equivalent default in US construction).

### Q2. Does the German VOB/B regime prove the wedge works ONLY where the contract form mandates the notice workflow?

**No — and this is the most thesis-relevant finding in the whole pass. Germany falsifies the simple version of that claim.**

Germany has a **stronger** mandated-notice regime than the US on paper — *three* separate statutory notice duties, one of which requires notice **before work starts** — and yet Germany has produced **no CEMAR, no Gather, no notice-deadline product at all**. The reason is precise and instructive:

**VOB/B mandates the notice but does not put a number on the clock.**

| | UK NEC4 | FIDIC 2017 | German VOB/B | US AIA A201 |
|---|---|---|---|---|
| Notice trigger | Compensation event | Claim event | 3 separate duties: §2(6) additional work, §4(3) concerns, §6(1) hindrance | Claim |
| **Deadline** | **8 weeks** (cl. 61.3) | **28 days** (cl. 20.2.1) | **"unverzüglich"** — *no day count* | 21 days (§15.1.3) |
| Deadline is countable by software | **YES** | **YES** | **NO** | YES |
| Strict condition precedent (lose the claim) | Yes | Yes, explicit | **No** — defeated by the `offenkundig` exception, §6(1) S.2 | Frequently waived in practice |
| Who administers | Named Project Manager, in-system | Engineer | No named administrator, no register | Architect |
| Register of events exists as a contractual object | **Yes** | Effectively | **No** | No |

Two consequences follow, and they are the load-bearing insight of this report:

1. **The countdown-clock product is contract-form-dependent.** CEMAR (£435/licence/month), Gather, FastDraft, Sypro, CALIM's Notice Deadline Calculator — every one of them exists in a regime with an **integer deadline** (8 weeks / 28 days / 84 days). Germany has no integer, so no German vendor built a clock. **This confirms the orchestrator's note that deadline alerting cannot be the wedge — it is not even buildable in the largest construction market in Europe.**

2. **But the demand does not disappear — it relocates to detection.** Because German notice is due *"same day or at latest the next working day"* ([source](https://www.bauagent.ai/blog/behinderungsanzeige-vob-muster-vorlage)), the German buyer has no use for a 28-day countdown and an acute need for *"did something happen on site today that I must notify today?"* That is exactly why the one German AI claims product with traction (**BauAgent.ai**) is built as an **event-capture-to-notice pipeline in 30 seconds**, not as a calendar.

> **Therefore: the contract form does not manufacture the demand. It manufactures the SHAPE of the product.**
> - Integer deadline → sell a **register + clock** (NEC/FIDIC: CEMAR, Gather, CALIM).
> - "Unverzüglich" / no integer → sell **detection + instant drafting** (Germany: BauAgent.ai).
> - No enforced regime at all (US AIA) → **neither has been built**, and the field-tool vendors sell logging instead (Clearstory, and its exact Swedish twins Next/ByggLog/Bygglet).
>
> The US is not "the market where the wedge doesn't work." The US is the market where **no one has yet chosen which of the two shapes to sell**, because the contract does not choose for you. That is a positioning problem, not a demand problem — and it is *also* why the US buyer will not arrive by searching, exactly as the Procore agent found.

**Third regime type found that the program has not yet considered — the Italian `riserve`:** Italian public works impose the harshest regime of all. The contractor must inscribe a *riserva* on the **first available accounting document** and then repeat it in the *registro di contabilità*, or the claim is extinguished (*decadenza*). MIT parere 4241/2026 (2026) tightened this further: waiting for the accounting moment is no longer enough ([LavoriPubblici, 2026](https://www.lavoripubblici.it/news/riserve-appalti-primo-atto-idoneo-registro-contabilita-mit-4241-2026-38126)). **And Italy has still produced no entitlement product** — only accounting software (STR Vision PBM / TeamSystem Construction) that records the riserva as a bookkeeping entry. This is a fourth independent datapoint that **a mandated notice regime is neither necessary nor sufficient to produce a product.**

### Q3. Is there a transplantable product idea, or a foreign incumbent worth partnering with?

**Transplantable idea: YES, and it is the one the whole program has been circling — but the German version proves it commercially in a way nothing English-language does.**

**Easyclaim (C. Abraham GmbH)** is a one-man expert practice that turned its own forensic method into software, and sells it two ways simultaneously:
- **€599 net per case**, done-for-you, output = a **21-page court-ready derivation** ([source](https://bauzeitnachtrag-leichtgemacht.de/));
- **or** a perpetual software licence (price disclosed only in the demo), with **payment plans up to 12 months**.

That is the *chargeable artefact* the Levelset analysis said contractual notice lacks. Germany found one: **the artefact is not a filing, it is a quantum submission that survives judicial scrutiny.** The customer list is public and is a list of famously litigated German public projects — **Beethovenhalle Bonn, Oberlandesgericht Stuttgart, Zoo Leipzig, Zoo Gelsenkirchen, Flughafen Paderborn**, multiple university hospitals ([source](https://nachtragsmanager-leichtgemacht.de/)).

**Foreign incumbent worth partnering with rather than competing: NONE is large enough to matter, but two are worth watching.**
- **Thinkproject (Munich)** already owns the NEC wedge — it acquired **CEMAR** in 2018 and is rebranding it as *Thinkproject | CONTRACTS* ([source](https://www.thinkproject.com/products/thinkproject-cemar/)). Note the strategic tell: **a German company has owned the leading NEC notice-workflow product for eight years and has never built a VOB/B equivalent for its home market.** That is the single strongest piece of evidence that the German regime does not support the register-and-clock product shape.
- **CALIM (Doha)** is the cleanest example of a claims consultancy productising: free **Notice Deadline Calculator**, **LD Exposure Estimator**, **Claim Readiness Score**, plus a "CALIM 360" monitoring platform, wrapped around a FIDIC advisory practice across Qatar/KSA/UAE/India/USA ([source](https://www.calim.ai/fidic-claims-management/)).

---

## 1. SNAPSHOT — THE NON-ENGLISH CLAIMS-SOFTWARE LANDSCAPE

**What it is:** Not a category. There is no "construction claims software" market in any non-English language. **Capterra Germany has no `Nachtragsmanagement` directory category at all** (checked 19 Aug 2026) — mirroring the program's earlier finding that G2/Capterra have no English "construction claims" category. What exists instead is four disconnected clusters:

1. **Logging tools** (largest, commoditised): a Nachtragsmanagement/ÄTA/meerwerk *tab* inside a general site-documentation product. Germany: Capmo, PlanRadar, BauMaster, 123erfasst. Sweden: Next, ByggLog, Bygglet. **Functionally identical to Clearstory.** Price €15–39/user/month.
2. **Construction ERPs** with a Nachtrag module: RIB iTWO, NEVARIS, BRZ. **6–18 month implementations** ([gaim-solutions, 2026](https://gaim-solutions.com/de/blog-system/kostentransparenz-bauprojekte-software-2026)).
3. **Specialist quantum calculators** (Germany only, and this is the unique German asset): Easyclaim/Nachtragsmanager/Massenclaim, CAC NAM.
4. **AI claims products** (all founded 2023–2026, all sub-scale): Contradic (FR), SmartClaim (FR), BauAgent.ai (DE), Handwai (DE), BlackSwanAI (DE), Ronayz (TR), ContraVault (IN).

**Who they sell to:** Clusters 1–2 sell to the *Bauleiter* / site manager as tooling. Cluster 3 sells to the *Geschäftsführer* or the firm's expert witness, per claim. Cluster 4 splits: Contradic sells to **law firms and legal departments** first (not contractors), BauAgent.ai and Handwai sell to **SME contractors and trades** (Handwerk / Nachunternehmer).

**Ownership / funding / scale:**
- Contradic — SAS, active since **1 Aug 2025**, Neuilly-sur-Seine. Founder **Tristan Agaësse** (CentraleSupélec, PhD physics, data/AI career); co-founder **Alain Brunet** (contract-management author). Funding round **planned for 2026**, none raised yet. [pappers.fr](https://www.pappers.fr/entreprise/contradic-990129330) · [founder interview, 22 Jan 2026](https://www.contractence.fr/blog/2026/01/22/contradic-presente-par-son-fondateur-tristan-agaesse/)
- Contracktime — **Forest CM**, founder **Nicolas Forest**, contract manager with 20 years' field experience. Self-funded, no disclosed raise.
- SmartClaim — founders **Alexis Deborde** (founded Smartpreuve, digital-evidence) and **Pierre Marchès** (founded Prime Conseil, contract/claim consultancy). Beta at app.smartclaim.fr.
- BauAgent.ai — founder **Michael Hilgers** (timber construction + software). **Closed beta**, pilot firms only.
- Easyclaim / Nachtragsmanager — **C. Abraham GmbH · Sachverständigenbüro**, Gieboldehausen. **Carsten Abraham**, expert practice founded 1999; programs developed 2015–2017 from his own manual calculations; current suite since 2017. Effectively a **one-person company**.
- CAC NAM — **Dipl.-Ing. Johannink**, "über 30 Jahre Erfahrung", Windows desktop, most recent site content **Nov 2021**.
- conmeet — Borken, founded 2023 by Benedikt Kisner, Leandro Ananias, Lennart Eckerlein. **€1.3M pre-seed (Feb 2026)** then **€6M seed** from **Reimann Investors + Smedvig Ventures**. General DACH construction/trades ERP; Nachtragsmanagement is one module of many.
- ContraVault AI — India. "Trusted by 200+ Enterprises"; 30+ named logos.
- CALIM — Doha (Pearl Towers), offices KSA/UAE/India/USA. A **consultancy**, not a software company.

**ICP and geography:** Germany's addressable base is the *Bauhauptgewerbe*, which turned over **€171.9bn in 2025 (+5.3% nominal, +2.4% real — the first real increase since 2020)**, with order intake of **€113.0bn (+9.2%)** and year-end backlog **+10.2%** ([ZDB, 2026](https://www.zdb.de/meldungen/solides-baujahr-2025-starke-branche-bereit-fuer-draengende-aufgaben)). Europe's construction-software market is put at **USD 1.20bn (2025) → USD 1.31bn (2026)**, with Germany the largest single share at ~USD 0.65bn, UK ~0.53bn, France ~0.33bn ([marketdataforecast](https://www.marketdataforecast.com/market-reports/europe-construction-software-market) — *market-research vendor, LOW confidence, cite with caution*).

---

## 2. PRODUCT SURFACE — EVERY PRODUCT FOUND, BY COUNTRY

### 🇩🇪 GERMANY

#### BauAgent.ai — *the most on-thesis German product*
URL: https://www.bauagent.ai/ · Founder: Michael Hilgers · Status: **closed beta** (Aug 2026)

| What it does | Evidence |
|---|---|
| Site team sends a **WhatsApp** message/photo/voice note; AI agent "Felix" recognises the event and **prepares the formal notice** | "Felix erkennt die Behinderung und bereitet das Dokument vor." — [funktionen/behinderungsanzeige](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| Generates a formal **§6 VOB/B Behinderungsanzeige** as a PDF in company letterhead, **in 30 seconds** | [bauagent.ai](https://www.bauagent.ai/) |
| Also generates **§4 VOB/B Bedenkenanzeige** and **§2 VOB/B Nachtragsanmeldung** from site | [funktionen/bedenkenanzeige](https://www.bauagent.ai/funktionen/bedenkenanzeige) · [muster/nachtragsanmeldung](https://www.bauagent.ai/muster/nachtragsanmeldung) |
| **Human stays in the loop:** "Du prüfst und entscheidest ob es versendet wird" | [funktionen/behinderungsanzeige](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| Explicitly warns the WhatsApp message is **not itself** the legal notice: "Die WhatsApp-Meldung allein genügt nicht als formale Anzeige" | ibid. |
| Reminds the user of the **mandatory Abmeldung** when the hindrance ends (also required by §6 VOB/B) | "Felix erinnert dich an die formale Abmeldung – ebenfalls Pflicht nach §6 VOB/B" |
| Exact timestamp on every hindrance; dashboard of status + history | ibid. |
| **Pricing: value-anchored** — custom by company size, with the framing that *one Nachtrag typically finances the annual subscription* | [bauagent.ai](https://www.bauagent.ai/) |
| Integrations: WhatsApp (live); M365/Outlook, OneDrive, Google Calendar/Drive, M-Files, Exchange; **email-analysis add-on and calendar/mail integration "coming mid-2026"** | ibid. |
| **Not present:** cost or time impact computation, schedule integration (Gantt "coming"), quantum | ibid. |

**Read:** this is *Document Crunch's Notice Builder + a site-capture front end + VOB/B entitlement classification*, at solo-founder scale, in closed beta. It solves **notice triggering** — the exact step the program identified as "not taken" — but only for events a human already thought worth messaging about. It does **not** watch passive project data.

#### Easyclaim / Nachtragsmanager / Massenclaim / EFB 221 / Kündigungsabrechnung — *the world's best productised construction quantum engine*
URLs: https://bauzeitnachtrag-leichtgemacht.de/ · https://nachtragsmanager-leichtgemacht.de/ · Vendor: C. Abraham GmbH · Sachverständigenbüro, Gieboldehausen

**Easyclaim** (Bauzeitnachtrag — prolongation/disruption cost):
1. **Reverse-engineers the original bid** from the contract sum and markup rates to isolate cost components (works even where no documented *Urkalkulation* exists)
2. Computes **working days** for target vs actual construction periods, excluding weekends and federal holidays
3. Distributes costs across **26 cost categories** (Allgemeine Geschäftskosten and Baustellengemeinkosten)
4. **Separates standstill costs from operating costs by cost type**
5. Converts markup percentages into **daily rates** so compensation is time-based rather than turnover-based
6. Handles **unlimited disruption periods, automatically consolidating overlaps**
7. Emits a **21-page documentation pack**: cover page, table of contents, cost breakdown by category and working day, methodology with legal citation, **fully traceable arithmetic with consistent rounding at every stage**, presented under *both* the combined-markup and the **Opitz** methods

Legal bases handled: **§ 642 BGB** (Entschädigung for Annahmeverzug), **§ 6 Abs. 6 VOB/B** (Schadensersatz), **§ 2 Abs. 3 VOB/B** (quantity deviation, via *Massenclaim*).

**Pricing (published, high confidence):**
- **€599 net per case**, done-for-you — the firm submits data, Easyclaim staff produce the complete documentation
- **Full software licence** — price disclosed in consultation; unlimited calculations; training included; **payment plans up to 12 months**

**Technical shape (highly relevant to the solo-founder constraint):** the product is a **single HTML file, run by double-click, no installation, fully offline, no server, no account, Windows/Mac/Linux**. Data is a local user-controlled file.

**Named customers:** Beethovenhalle Bonn, Oberlandesgericht Stuttgart, Zoo Leipzig, Zoo Gelsenkirchen, Flughafen Paderborn, multiple university hospitals. Named testimonials: Claus Hausinger (Hausinger Innenausbau und Trockenbau), Michael Kuhnert (Kutter HTS), Matthias Stein (B.R.A.S.S.T. Bau GmbH), Heinrich Raum.

**Explicit disclaimer:** "Easyclaim functions as a calculation and presentation tool; it neither replaces legal counsel nor constitutes an expert opinion." **No AI is used** — and for the done-for-you tier the vendor markets that as a *feature*: the document is "not created by an automaton."

#### CAC NAM — the legacy incumbent
URL: https://cacnam.de/ · Vendor: Dipl.-Ing. Johannink · Windows desktop · **no AI**

VOB *Ausgleichsrechnung* and Nachtragsmanagement; decomposes unit prices into price and cost elements **to the cent** where no documented *Urkalkulation* exists; handles LVs from a few positions to several thousand; **GAEB-90 standard interface** for exchange with other calculation/billing programs; trial as unrestricted full version at **10% of list price for three months**. Most recent site content dated **Nov 2021** — flag as **possibly dormant**.

> ⚠ **Obsolescence risk worth noting:** CAC NAM's core premise (price the Nachtrag off the *Urkalkulation*) is the doctrine the **BGH abandoned in 2019** in favour of *tatsächlich erforderliche Kosten* (§ 650c BGB), extended again in **November 2024** to *Mehrmengen*. A product hard-coded to the old doctrine is a liability, not an asset.

#### Handwai — the most-adopted German AI VOB product
URL: https://handwai.io/ · Germany (+49 6571)

"KI-System für Unternehmer im Baugewerbe" — digitises the VOB process end-to-end: LV (bill of quantities) cost analysis at offer phase, automated documentation during execution, invoicing and Nachtrag processes, VOB-compliant correspondence. Exports **Bedenkenanzeigen** off the LV analysis. Positions around *"verborgene Renditepotenziale"* (hidden margin potential) in the specification.

**Vendor-claimed numbers — ALL UNVERIFIED, no third-party source found:**
- "Over 600 construction firms" use Handwai
- **4,000+ completed VOB projects**
- **86% repurchase rate**
- **+7% average margin gain** (headline claim: "+10% Rendite")

Named references: SE.SERVICE GmbH, DK Brandschutz GmbH, ONI-Wärmetrafo GmbH, IP Steuerungstechnik GmbH. Pricing: by number of projects analysed, quote only.

#### BlackSwanAI — tender-stage claim-potential detection
URL: https://blackswanai.de/de · Erlangen, Germany · Products: **auftragr** (bidders), **prüfr** (contracting authorities, MVP)

Analyses **tender and contract documents** to identify *Nachtragspotential* before award — risks, opportunities, open questions, go/no-go, **"Nachtragspotential-Identifikation"**, department routing, bid positioning. Output is a **structured register with VOB/B references** that a lawyer or claims manager can work from directly. Hosted on **Open Telekom Cloud (Frankfurt)**, EU-only LLM processing, no third-party data sharing, GAEB and VOB standard compatibility. Pricing: "Individualisierte Preise nach Anwendungsfall und Volumen — auf Anfrage."

**Its own competitive claim (useful market intel):** AI analysis returns within **24 hours of upload**; the comparable manual analysis by a *Baujurist* takes **5–10 working days** ([source](https://blackswanai.de/de/nachtragsmanagement-software-vergleich)). It names only **InEight** and **Handwai** as contract-management competitors, and DTAD/Vergabe24/Subreport as complementary tender-search platforms — a telling indication of how thin the German competitive set is.

#### Formilo — bespoke digital notice forms with AI narrative
URL: https://www.formilo.com/vordrucke/behinderungsanzeige/ · Berlin

A **done-for-you forms agency**, not SaaS: fixed price, up to three revision rounds, **full ownership transfer post-delivery, no recurring licence**. Captures hindrances by dropdown + voice dictation on site + up to seven photos, offline-capable with auto-sync, on-site digital signature. Its AI turns keywords about cause, affected works and duration into a **"konkrete, bauablaufbezogene Darstellung"** instead of vague generalities — i.e. it targets the exact evidential standard the BGH requires (below). Feeds ERP/contract/construction-management systems via API/webhooks as the starting point for time claims and Nachträge. Claims thousands of firms across DACH.

#### Others (Germany/DACH), briefly
| Product | What it actually is | Pricing |
|---|---|---|
| **Capmo** (Munich) | General site documentation; AI does contextual search, auto reports, dictation, and **Nachtragsprüfung** — i.e. *checking* an incoming claim, the owner's side | from **€39/user/month** Pro |
| **PlanRadar** (Vienna, 28+ countries) | The "Nachtragsmanagement" page is **marketing for the general documentation product** — no event detection, no VOB/B entitlement matching, no deadline tracking, no valuation, no claim package | n/d |
| **conmeet** (Borken) | Full construction/trades ERP+CRM with a Nachtragsmanagement module and AI agents (assistant, autonomous agent, AI telephony) | n/d; **€6M seed** |
| **RIB iTWO / NEVARIS / BRZ** | Construction ERPs with Nachtrag modules; **6–18 month implementations** | enterprise |
| **rsmc EasyClaim** (rsmc-easyclaim.de) | Tiefbau SME claims app: photo + description capture → storage → distribution → **automatic claim offer generation**. **"Noch in finaler Fertigstellung"** — pre-launch, collecting emails | n/d |
| **ORCA AVA** | AVA software with workflow + Nachtragsmanagement (since 2013) | n/d |

#### German claims-consulting industry — is it productising?
**Barely, and the largest players are not.**
- **Drees & Sommer** built **Dreso.AI**, an internal platform — PDF chat, tender-document analysis, Azure OpenAI — for **its own consultants' productivity**. There is **no external claims product**. ([Dreso press](https://www.dreso.com/de/unternehmen/presse/presseinformationen/details/kluge-koepfe-smarte-konzepte-wie-eigenentwickelte-ki-bei-drees-sommer-aufwand-reduziert) · [immobilienmanager, 30 Jan 2025](https://www.immobilienmanager.de/drees-und-sommer-testet-eigene-ki-plattform-dreso-ai-30012025))
- **HKA** is the rebranded Hill International Construction Claims Group (with Knowles, Cadogans, BCA, McLachlan Lister). Services only.
- A long tail of pure-services firms: **Claimscale GmbH**, **Primestone Consulting** (Stuttgart), **MCE-Consult**, **Duhatschek + Winkler**, **claim.m GmbH**, **CEM Consultants**, **INA-BAU**. None ships software.
- **Prof. Dr. Thomas Heilfort** — the German authority on disruption proof, author of the **Bauablauf-Differenzverfahren** (introduced in *BauR*, 2003). He has **not productised it**. He teaches it, and executes it in **MS Excel, MS Project, Asta Powerproject and iTWO**. ([heilfort.de](https://heilfort.de/30-nachweis-haftungsbegruende-haftungsausfuellende-terminliche-kausalitaet-bauablaufstoerungen-bauablauf-differenzverfahren/))

> **The single cleanest German white-space statement:** the country's hardest, most valuable claims task — *bauablaufbezogene Darstellung* of disruption — is performed by named professors and expert witnesses **inside generic scheduling software**, at consulting rates, and the only vendor addressing it (**Easyclaim**) attacks the *cost* half and leaves the *causation* half to the human.

### 🇫🇷 FRANCE

#### Contradic — *the closest thing to the full thesis pipeline in any language*
URL: https://contradic.com/ · SAS, Neuilly-sur-Seine, **active since 1 Aug 2025**

> "une plateforme d'intelligence contractuelle dédiée à l'exécution des contrats complexes" — [jurishop.fr](https://www.jurishop.fr/Contradic)

What it does (from the founder interview and the independent review):
- Ingests **contracts, correspondence, emails, notices, meeting minutes, schedules** ("plannings, comptes rendus, e-mails")
- **"gérer l'avalanche de documents non structurés générés pendant l'exécution d'un projet"**
- Cross-document logic: *"relie les informations entre elles, restitue le contexte contractuel global"* — **highlights applicable obligations, critical deadlines, inconsistencies, points of tension, potential risks**
- **Detects key events, delays and scope changes**; **reconstructs project chronologies**
- **Generates claim drafts automatically**
- **30+ specialised AI agents**, explicitly not a ChatGPT wrapper — *"une IA métier"* — running **GPT-5 via Azure AI (EU)**
- Chatbot for natural-language queries over the corpus

**Pricing (published by the reviewer, high confidence):**
- **Team: €199/user/month or €1,990/year**
- **Enterprise: from €349/user/month or €3,490/year**, with custom integrations and SSO
- **Single feature set across all tiers** (tiers differ by integrations/support, not capability)

**Traction:** one energy-sector client *"réduit le temps de constitution d'un dossier de réclamation de trois semaines à seulement cinq jours"*. Target: **specialised law firms and mid-sized structures first**, then SMEs, then large enterprises. **BTP/construction is not named as the focus.** Funding round **planned 2026**.

**Reviewer-stated weaknesses (verbatim-sourced):** immature UX/UI with responsive-design problems and French/English translation gaps; **hallucinations on highly technical, jargon-heavy documents**; limited AI-agent templates and customisation; **not yet multi-LLM**; integrations (CRM, ERP, SSO) are **future** capability. Characterised as *"une solution jeune mais prometteuse."* ([contractmanagement.fr review](https://contractmanagement.fr/avis/contradic/))

#### Contracktime — the human-triggered, email-native, solo-founder shape
URL: https://www.contracktime.com/ · Vendor: **Forest CM** · Founder: **Nicolas Forest**, 20 years a contract manager · FR/EN/NL

- Event capture by **tagging emails inside Outlook** via an add-in from the Microsoft Store (also listed on **Google Workspace Marketplace**) — deliberately no new mail client: the reviewer calls native Outlook integration rather than a dedicated interface *"une décision intelligente."*
- Rebuilds the **complete, classified, dated exchange history for each aléa** (hazard/event)
- **Automatic impact reports on cost** (hours, rates, totals) **and schedule** — simulates task delay and delivery-date shift
- Meeting-report capture and archiving; real-time task progress from the field
- **Supports "litigation and claim file preparation"**
- Integrations: **Outlook add-in, MS Project (plan import), Excel (cost list import)**
- **No AI**

**Pricing (published, high confidence):** **Free** — 2 active users, unlimited projects, 2 GB. **Premium — €15/month for 5 users**, 25 GB, **+€5/user/month**. **Enterprise** — custom, on-premises available.

**Reviewer weaknesses:** *"quelques bugs d'affichage, onboarding perfectible, fonctionnalités encore en construction"*; "less optimal usage outside the Microsoft environment"; meeting records import only via Excel (not Word/PDF); **nascent contract-type reference library**. ([contractmanagement.fr review](https://contractmanagement.fr/avis/contracktime/))

> **This is the single most instructive product in the report for the solo-founder constraint.** A one-man vendor built email-native event capture + evidence chronology + cost/schedule impact + claim-file prep, shipped it into two app marketplaces, and priced it at **€15/month for five users**. It proves the V1 is buildable solo. It also proves that **without entitlement reasoning and without quantum, the product commands tooling prices, not recovery prices** — a 13x–23x price gap against Contradic for the same underlying data.

#### SmartClaim — evidence-first, consultancy-backed
URL: https://smartclaim.fr/ · Founders: **Alexis Deborde** (Smartpreuve, digital evidence) + **Pierre Marchès** (Prime Conseil, contract/claim consultancy) · Hosted in France · **beta** (app.smartclaim.fr)

Three-step: **Collection** (photos, videos, documents, voice notes from site) → **Analysis** (multi-agent AI cross-referencing *three* knowledge bases: the client's contracts, **10,000+ vectorised legal sources**, and Prime Conseil's encapsulated expertise) → **Generation** (draft claim letter + stakeholder notification + real-time case tracking). Evidence is **geolocated, timestamped and blockchain-anchored** via Smartpreuve. Cites an example analysis touching *"47 contractual articles and 12 jurisprudences."* Claims **5x faster** than traditional methods. **On-demand escalation to a human Prime Conseil expert.** No pricing, no named customers, no contract regime named (CCAG/FIDIC/NEC not mentioned). **Valuation is absent.**

**Also listed in French comparisons** but out of scope or foreign: **ClaimControl** (Alphatec), **Aclaimant** (US risk/incident), **Mastt** (AU capital-projects).

### 🇦🇹 AUSTRIA / 🇨🇭 SWITZERLAND
**ÖNORM B 2110** is the Austrian standard works contract. A deviation from the *Bau-Soll* — whether an ordered *Leistungsänderung* or a *Störung der Leistungserbringung* not attributable to the contractor — is asserted through a formal **MKF (Mehrkostenforderung)**, a demand for schedule and/or price adjustment ([bw-b GmbH](https://www.bw-b.com/bauwirtschaft-infobox/bauvertrag-mehrkosten-oenorm-b-2110-bauablaufstoerungen-und-entgeltanpassung/)). **No dedicated MKF software was found.** PlanRadar and BauMaster (both Austrian) offer *Behinderungsanzeige* templates and generic documentation. Switzerland (SIA 118) similarly produced only consultancy sites.

### 🇸🇪 SWEDEN / 🇳🇴 NORWAY / 🇩🇰 DENMARK
Sweden's **AB 04 / ABT 06 chapter 2** governs **ÄTA-arbeten** (Ändrings-, Tilläggs- och Avgående arbeten). The contractor must notify the client **"utan dröjsmål"**; failure can forfeit the right to compensation. A **new standard, AB 25 / ABPU 25**, is now replacing ÄTA with *"Ändring av entreprenaden"* and a revised *underrättelse* mechanism ([Rättsakuten](https://rattsakuten.se/ata-ar-dott-leve-andring-av-entreprenaden/)) — a live regime change worth tracking.

Norway's **NS 8405 / NS 8407** impose layered *varsel* duties for irregular change orders, time extensions and price adjustment, with **deemed acceptance if the client fails to respond in time** ([CMS Norway](https://cms.law/no/nor/publikasjon/praktisk-entrepriserett/varsling-og-frister)). A commonly-cited failure mode: *"the contractor discusses the change orally but does not formally notify and document it"* ([Proanbud](https://proanbud.no/artikler/ns-8405-ns-8407-endringshandtering)).

**Products found: logging only.** **Next** (ÄTA module: document all ÄTA in real time with text and images), **ByggLog** (document on mobile, **customer approval on site via BankID/e-signature**, auto-linked to project), **Bygglet** (create and manage ÄTA, routed to the right project for client approval). All auto-generate a PDF and **auto-create the invoice once approved**.

> **The Nordics are the strongest single test of the "contract form manufactures demand" hypothesis, and they fail it.** Norway and Sweden have *deemed-acceptance* and *forfeiture-on-silence* notice regimes at least as strict as NEC4's — and the entire product response is a mobile approval-and-invoice flow. **No entitlement engine, no valuation, no claim package, in either country.**

### 🇳🇱 NETHERLANDS
**UAV 2012** §35 sets out **five situations** in which *meerwerk* may be settled; commentary notes that payment arrangements and the handling of *meer- en minderwerk* are the **two subjects that cause the most conflict in Dutch construction practice**, and that the UAV provisions are *"far from unambiguous"* in application ([flux.partners](https://flux.partners/kennisbank/contractvormen/uav/)). **No dedicated claims product found** — only law firms and consultancies.

### 🇮🇹 ITALY
The **riserve** regime (Codice degli appalti, D.Lgs. 36/2023) is the strictest notice regime found in this pass. The contractor must contest the prejudicial fact **immediately, on the first suitable available document** (*primo atto idoneo*) and then carry the riserva into the **registro di contabilità** — MIT parere **4241/2026** confirms that waiting for the accounting moment alone is now insufficient ([LavoriPubblici](https://www.lavoripubblici.it/news/riserve-appalti-primo-atto-idoneo-registro-contabilita-mit-4241-2026-38126) · [A.I.FERR.](https://aiferr.it/riserve-negli-appalti-il-mit-chiarisce-quando-il-registro-di-contabilita-non-basta/)). Failure = *decadenza* (extinguishment).

**Products: accounting only.** **STR Vision PBM** and **TeamSystem Construction Lavori Pubblici** manage *contabilità lavori*, *varianti in corso d'opera* and the registro as bookkeeping objects; **Primus** (ACCA) similarly. **No entitlement, causation, evidence-sufficiency or claim-package capability found in any Italian product.**

### 🇪🇸 SPAIN / LATAM
Only training and consultancy: Mayo Educación Ejecutiva ("Gestión de Reclamaciones (Claims) en los Contratos de Construcción"), Atenos, Estudio Mallma (Peru). The regional CLM tools cited are **Webdox** and **Comforce**, which are generic contract lifecycle, not construction claims. One market-side claim worth noting: *"la gestión digital de las reclamaciones en obra puede acortar los plazos de construcción entre un 10% y un 30%"* ([ecoconstruccion](https://www.ecoconstruccion.net/noticias/la-gestion-digital-de-las-reclamaciones-en-obra-puede-acortar-los-plazos-de-construcc-8occO)) — **UNVERIFIED, no methodology given.** **No Spanish-language claims product found.**

### 🇵🇱 POLAND
FIDIC is the default for Polish public infrastructure, and there is a substantial **training and consulting** industry around claims — **SIDiR** ("Roszczenia i Spory według Warunków Kontraktowych FIDIC"), Lazarski CKP, budownictwo.org, IIST. Commentary stresses **"harmonogram jako narzędzie dowodowe"** (the schedule as the evidential instrument). **No Polish claims software found.**

### 🇹🇷 TURKEY
**Ronayz** — https://www.ronayz.com/ — Istanbul. AI assistant for construction contract management, **trained on FIDIC standard forms** (Red Book, Yellow Book explicitly) and custom contracts. Analyses penalty clauses, time-extension rights, termination conditions, warranty provisions; archives correspondence; **prepares draft responses / claims-notices in seconds**; natural-language query across contracts and correspondence. **TR / EN / FR.** Partners: BeInsights (AI infrastructure), Evreqa (commercialisation), Haluk Rona (sector expertise). **Appears pre-launch** — "Request a Meeting" is the only conversion path. No pricing, no customers.

### 🇶🇦 GCC (Qatar / KSA / UAE) — the FIDIC heartland
**CALIM Consultancy Services** — https://www.calim.ai/ — Doha (Pearl Towers), with offices in KSA, UAE, India, USA.

A **claims consultancy that is productising at the edges.** Services: variation & claims management, FIDIC claims prosecution (1999 and 2017), **delay analysis and concurrent delay**, LD defence, dispute resolution, contract close-out, QS/commercial management, and **outsourced contract management (BPO)**.

Productised assets: **CALIM 360** (contract monitoring platform), plus free lead-gen tools — **Notice Deadline Calculator**, **LD Exposure Estimator**, **Claim Readiness Score**.

Its own description of what it maintains for clients is the cleanest statement of the FIDIC-regime product shape found anywhere: *"a live claims and notice calendar tracking every potential claim event against the applicable deadline — 28-day, 84-day, or shorter where GCC amendments apply"*, plus *"a records discipline from mobilisation through daily diaries, site correspondence logs, RFI tracking, and labour allocation records."*

**The regime it operates in:** FIDIC 2017 sub-clause **20.2.1** makes the **28-day notice an express condition precedent** — miss it and the contractor loses time and money **regardless of the merits** ([LexisNexis UK](https://www.lexisnexis.com/en-gb/legal/guidance/fidic-contracts-2017-contractor-employer-claims) · [Howard Kennedy](https://internationalconstructionknowledgehub.com/no-notice-no-claim-conditions-precedent-in-fidic-contracts/)).

### 🇮🇳 INDIA
**ContraVault AI** — https://www.contravault.com/

The **claims module**: "manage claim-related letters, notices, emails, and contract records in one place"; **Claim Repository** (organised by project, topic, date, counterparty); **automatic timeline structuring** by date/topic/party; **evidence compilation** (supporting records with dates, correspondence, impacts); **"Generate first-draft replies for common claim scenarios (EOT, variations, delays, disruptions)"** with **citation trails** ([features/construction-claims-ai](https://www.contravault.com/features/construction-claims-ai)).

But the **core** of the company is pre-award: Bid Intelligence (go/no-go, RFP synopsis, risk), Takeoff & Estimation (theTakeoff.ai), Vendor Sourcing, Forms AI, Contextual Search, **Contradiction Finder**.

**Named customers (30+ logos):** Adani, Tata, Toyo Engineering, thyssenkrupp, NTPC, Shapoorji Pallonji, Kalpataru, ISGEC, Bajel, NGSL, Voltas, GE, HTL, Bajaj Electricals, BPCL. Site claims "Trusted by 200+ Enterprises."
**Vendor-claimed metrics (UNVERIFIED):** 95%+ requirement-extraction accuracy; 5–15 min typical RFP analysis; 90% faster than manual review; 70% estimation time saving; **$630M+ project value processed; 200K+ RFPs analysed; 10M+ pages parsed; 25K+ RFI clarifications drafted.**
**Integrations:** Procore, Autodesk Construction Cloud, PlanGrid, MS Project, plus API. **No pricing disclosed.**

### 🇯🇵 JAPAN / 🇰🇷 KOREA / 🇨🇳 CHINA
- **Japan:** No claims/entitlement product. The adjacent stack is **ANDPAD** (project management with AI automation), **Kencopa 工程AIエージェント** (AI schedule generation/simulation), and **LegalOn Cloud / LegalForce** — an AI legal platform that added **建設工事請負基本契約** (construction works contract) to its contract-risk review types ([LegalOn](https://legalontech.jp/8639/)). Japanese practice guidance is procedural — negotiate promptly, document the change and its schedule effect, execute a 変更契約書 or 工期延長合意書 ([KENTEM](https://www.kentem.jp/blog/construction-period-extension-tst/)).
- **Korea:** Claims are taught as a CM discipline — 비용보상클레임 (cost) vs 공기연장클레임 (EOT) ([cmkorea.org](https://cmkorea.org/10-%ED%81%B4%EB%A0%88%EC%9E%84-%EA%B4%80%EB%A6%ACclaim-management/)). Construction AI coverage is dominated by safety, CCTV/drone monitoring and generative design. **No claims product found.**
- **China:** 变更 (change), 签证 (site confirmation) and 索赔 (claims) are a recognised discipline, delivered as **全过程工程咨询** consulting and implemented on **智慧工地** platforms or **AI low-code** builders (e.g. 搭贝) with dynamic 签证单 forms and 变更管理闭环 workflows. Photogrammetry/heat-map evidence capture is marketed **for 索赔/签证取证** (evidence-gathering for claims). **No entitlement engine found.**

---

## 3. CAPABILITY MATRIX — 26 SCORES

### 3.1 CONTRADIC (France) — the most on-thesis single product in any language

`SCORES| 3,3,2,3,1,3,1,1,1,3,2,2,3,2,0,3,2,0,0,0,1,0,2,1,1,3`

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | 3 | Contracts are the primary corpus; "intelligence contractuelle dédiée à l'exécution des contrats complexes" | [jurishop](https://www.jurishop.fr/Contradic) |
| 2 | clause_extraction | 3 | "met en évidence les obligations applicables"; deep, contextual contractual reading positioned against CLM tools | [jurishop](https://www.jurishop.fr/Contradic) |
| 3 | notice_detection | 2 | Detects "événements clés" and surfaces "délais critiques", but no per-contract-form notice-obligation register (no NEC/FIDIC/VOB model) | [review](https://contractmanagement.fr/avis/contradic/) |
| 4 | deadline_tracking | 3 | Explicit: helps "respecter les échéances contractuelles"; critical deadlines surfaced across documents | [comparateur](https://contractmanagement.fr/comparateur/logiciels-claim-management/) |
| 5 | rfi_event_ingestion | 1 | Generic document ingestion; no RFI object or construction-specific event type | [review](https://contractmanagement.fr/avis/contradic/) |
| 6 | email_ingestion | 3 | Emails named as a first-class input ("contrats, courriers, e-mails, notifications, comptes rendus") | [jurishop](https://www.jurishop.fr/Contradic) |
| 7 | daily_report_ingestion | 1 | Meeting minutes yes; site diaries / daily reports not evidenced | [jurishop](https://www.jurishop.fr/Contradic) |
| 8 | schedule_integration | 1 | "plannings" analysed as documents; no P6/MSP connector evidenced | [interview](https://www.contractence.fr/blog/2026/01/22/contradic-presente-par-son-fondateur-tristan-agaesse/) |
| 9 | change_order_workflow | 1 | Detects scope changes; no CO raise/price/approve workflow | [review](https://contractmanagement.fr/avis/contradic/) |
| 10 | claim_identification | 3 | Core purpose: "construire des dossiers de réclamation plus solides", anticipate disputes | [interview](https://www.contractence.fr/blog/2026/01/22/contradic-presente-par-son-fondateur-tristan-agaesse/) |
| 11 | delay_detection | 2 | Detects "retards" from the document corpus; not schedule-analytic | [review](https://contractmanagement.fr/avis/contradic/) |
| 12 | responsibility_attribution | 2 | Surfaces "points de tension" and helps "sécuriser ses positions"; not a causation engine | [jurishop](https://www.jurishop.fr/Contradic) |
| 13 | contemporaneous_evidence_graph | 3 | **Strongest evidence-graph claim found in any language:** cross-document logic, "relie les informations entre elles", "restitue le contexte contractuel global", reconstructs chronologies | [jurishop](https://www.jurishop.fr/Contradic) |
| 14 | evidence_completeness | 2 | "identifier rapidement les preuves"; no completeness/sufficiency scoring | [interview](https://www.contractence.fr/blog/2026/01/22/contradic-presente-par-son-fondateur-tristan-agaesse/) |
| 15 | recoverable_dollar_estimation | **0** | **No quantum anywhere in the product.** Not mentioned on any page or in the independent review | [review](https://contractmanagement.fr/avis/contradic/) |
| 16 | claim_package_generation | 3 | Generates claim drafts; energy client cut dossier build from 3 weeks to 5 days | [interview](https://www.contractence.fr/blog/2026/01/22/contradic-presente-par-son-fondateur-tristan-agaesse/) |
| 17 | notice_drafting | 2 | Claim drafting evidenced; notice drafting per contractual mechanism not separately evidenced | [review](https://contractmanagement.fr/avis/contradic/) |
| 18 | schedule_impact_analysis | 0 | Absent | — |
| 19 | procore_integration | 0 | None; integrations are "future capability" | [review](https://contractmanagement.fr/avis/contradic/) |
| 20 | autodesk_integration | 0 | None | — |
| 21 | outlook_gmail_integration | 1 | Emails ingested but no evidenced mail connector; CRM/ERP/SSO listed as future | [review](https://contractmanagement.fr/avis/contradic/) |
| 22 | mobile_workflow | 0 | Reviewer flags responsive-design failures | [review](https://contractmanagement.fr/avis/contradic/) |
| 23 | audit_trail | 2 | "renforcer la traçabilité des événements" is a headline benefit; no immutable-log claim | [comparateur](https://contractmanagement.fr/comparateur/logiciels-claim-management/) |
| 24 | portfolio_risk | 1 | Per-contract risk highlighting; no cross-project portfolio view evidenced | [jurishop](https://www.jurishop.fr/Contradic) |
| 25 | performance_pricing_compatibility | 1 | Straight per-seat SaaS (€199 / €349 per user per month); no outcome or per-claim option | [review](https://contractmanagement.fr/avis/contradic/) |
| 26 | consultant_replacement_potential | 3 | Sells **to law firms**; replaces the manual dossier build (3 weeks → 5 days) | [interview](https://www.contractence.fr/blog/2026/01/22/contradic-presente-par-son-fondateur-tristan-agaesse/) |

### 3.2 BAUAGENT.AI (Germany) — the VOB/B notice engine

`SCORES| 1,1,2,2,0,1,3,0,2,2,1,1,2,1,0,2,3,0,0,0,2,3,3,1,2,2`

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | 1 | Works from **statutory VOB/B**, not from the project contract document | [bauagent.ai](https://www.bauagent.ai/) |
| 2 | clause_extraction | 1 | Maps events to VOB/B paragraph numbers (§2/§4/§6); does not extract project-specific clauses | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 3 | notice_detection | 2 | "Felix erkennt die Behinderung" — but from a human-initiated WhatsApp message, not from passive project data | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 4 | deadline_tracking | 2 | Reminds about the mandatory **Abmeldung** at hindrance end; no day-count regime exists in VOB/B to track | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 5 | rfi_event_ingestion | 0 | Absent (no RFI object in German practice) | — |
| 6 | email_ingestion | 1 | M365/Outlook/Exchange listed; **email-analysis add-on is "coming mid-2026"** | [bauagent.ai](https://www.bauagent.ai/) |
| 7 | daily_report_ingestion | 3 | Core capability: WhatsApp photos/voice → Bautagebuch, Mängel, Zeiterfassung | [bauagent.ai](https://www.bauagent.ai/) |
| 8 | schedule_integration | 0 | Gantt-Ansicht listed as "coming" | [bauagent.ai](https://www.bauagent.ai/) |
| 9 | change_order_workflow | 2 | Nachtragsanmeldung raised from site "noch während die Änderung besprochen wird"; no pricing/approval loop | [muster](https://www.bauagent.ai/muster/nachtragsanmeldung) |
| 10 | claim_identification | 2 | Classifies an event into §2 / §4 / §6 VOB/B claim types — real entitlement matching, but within a fixed statutory taxonomy | [funktionen/bedenkenanzeige](https://www.bauagent.ai/funktionen/bedenkenanzeige) |
| 11 | delay_detection | 1 | Records hindrances; no delay analysis | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 12 | responsibility_attribution | 1 | Notice names a cause; no analytic attribution | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 13 | contemporaneous_evidence_graph | 2 | "Jede Behinderung wird mit exaktem Zeitstempel dokumentiert" + photos tied to the event; not cross-document | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 14 | evidence_completeness | 1 | Not evidenced beyond capture | — |
| 15 | recoverable_dollar_estimation | 0 | Absent — no cost or time impact computation | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 16 | claim_package_generation | 2 | Formal PDF notice in company letterhead; not a substantiated claim package with quantum | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 17 | notice_drafting | **3** | The core capability: three distinct statutory notice types, generated in ~30 seconds, VOB-compliant, own letterhead | [bauagent.ai](https://www.bauagent.ai/) |
| 18 | schedule_impact_analysis | 0 | Absent | — |
| 19 | procore_integration | 0 | Absent | — |
| 20 | autodesk_integration | 0 | Absent | — |
| 21 | outlook_gmail_integration | 2 | Microsoft 365 / Outlook / Exchange / OneDrive / Google Calendar & Drive / M-Files listed | [bauagent.ai](https://www.bauagent.ai/) |
| 22 | mobile_workflow | **3** | WhatsApp-native: "kein Formular, keine App, kein Papierkram" — zero-install field workflow | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 23 | audit_trail | 3 | Exact timestamp on every event, dashboard of status and history, PDF as the formal record | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 24 | portfolio_risk | 1 | Per-site dashboard only | [funktionen](https://www.bauagent.ai/funktionen/behinderungsanzeige/) |
| 25 | performance_pricing_compatibility | 2 | Value-anchored: pricing framed as *one Nachtrag typically finances the annual subscription*; still a subscription | [bauagent.ai](https://www.bauagent.ai/) |
| 26 | consultant_replacement_potential | 2 | Replaces the Bauleiter's writing time and the template-lawyer; does not replace the claims consultant | [bauagent.ai](https://www.bauagent.ai/) |

### 3.3 EASYCLAIM / NACHTRAGSMANAGER SUITE (Germany) — the quantum engine

`SCORES| 1,0,0,0,0,0,0,1,2,1,0,0,0,1,3,3,0,1,0,0,0,0,3,0,3,3`

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | 1 | Takes contract sum and markup rates as **numbers**, not the contract document | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 2 | clause_extraction | 0 | Absent | — |
| 3 | notice_detection | 0 | Absent | — |
| 4 | deadline_tracking | 0 | Absent | — |
| 5 | rfi_event_ingestion | 0 | Absent | — |
| 6 | email_ingestion | 0 | Absent — runs fully offline, no server, no account | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 7 | daily_report_ingestion | 0 | Absent | — |
| 8 | schedule_integration | 1 | Takes Soll-Bauzeit and Ist-Bauzeit and unlimited disruption windows as **manual inputs**; auto-consolidates overlaps | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 9 | change_order_workflow | 2 | *Nachtragsmanager* computes the Nachtrag line-by-line against the Urkalkulation; no approval workflow | [nachtragsmanager](https://nachtragsmanager-leichtgemacht.de/) |
| 10 | claim_identification | 1 | The human identifies the claim; the tool prices it | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 11 | delay_detection | 0 | Absent | — |
| 12 | responsibility_attribution | 0 | Absent | — |
| 13 | contemporaneous_evidence_graph | 0 | Absent | — |
| 14 | evidence_completeness | 1 | The 21-page derivation is fully auditable, but that is arithmetic traceability, not evidence sufficiency | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 15 | recoverable_dollar_estimation | **3** | **Best in the program, in any language.** Reverse-engineers the bid, 26 cost categories, standstill/operating split, markup→daily-rate conversion, both combined-markup and **Opitz** methods, under §642 BGB / §6(6) VOB/B / §2(3) VOB/B | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 16 | claim_package_generation | **3** | **21-page** submission: cover page, ToC with page refs, cost breakdown by category and working day, methodology with legal citation, full arithmetic derivation | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 17 | notice_drafting | 0 | Absent — the notice is assumed already given | — |
| 18 | schedule_impact_analysis | 1 | Computes working days excluding weekends and federal holidays for Soll vs Ist; consolidates overlapping disruptions. No CPM/critical path | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 19 | procore_integration | 0 | Absent | — |
| 20 | autodesk_integration | 0 | Absent | — |
| 21 | outlook_gmail_integration | 0 | Absent | — |
| 22 | mobile_workflow | 0 | Single HTML file, double-click, desktop, offline | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 23 | audit_trail | 3 | Every figure derived and traceable with consistent rounding at each stage — designed for judicial and expert scrutiny | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 24 | portfolio_risk | 0 | Absent | — |
| 25 | performance_pricing_compatibility | **3** | **€599 net per case, done-for-you** — the closest thing to per-claim pricing found in any market | [easyclaim](https://bauzeitnachtrag-leichtgemacht.de/) |
| 26 | consultant_replacement_potential | **3** | Literally a Sachverständigenbüro's practice sold as software; the service tier competes with the expert-witness engagement it came from | [Carsten Abraham](https://bauzeitnachtrag-leichtgemacht.de/carsten-abraham/) |

### 3.4 CONTRAVAULT AI (India) — reference row, LOWER CONFIDENCE

`SCORES| 3,3,2,2,1,2,1,1,1,2,1,1,2,2,0,2,2,0,2,2,1,1,2,1,0,2`

Justification in brief: strong document ingestion and clause work (bid-side heritage, Contradiction Finder); claim repository with automatic timeline structuring by date/topic/party (13, 14 = 2); first-draft replies for EOT/variations/delays/disruptions **with citation trails** (16, 17 = 2); Procore/ACC/PlanGrid/MS Project integrations (19, 20 = 2); **no quantum (15 = 0)**; no published pricing so no per-claim option (25 = 0). Confidence is lower than the three rows above because the claims module has a single marketing page and the company's centre of gravity is pre-award bidding and estimation. [features/construction-claims-ai](https://www.contravault.com/features/construction-claims-ai)

---

## 4. PRICING

**Published numbers (HIGH confidence — vendor or independent reviewer, current):**

| Product | Country | Price | Basis |
|---|---|---|---|
| **Contradic** Team | FR | **€199/user/month** or **€1,990/year** | Independent review, 2026 |
| **Contradic** Enterprise | FR | **from €349/user/month** or **€3,490/year** | Independent review, 2026 |
| **Easyclaim** per-case service | DE | **€599 net per case** | Vendor page |
| **Easyclaim** software licence | DE | Quote in demo; **payment plans up to 12 months** | Vendor page |
| **Contracktime** Free | FR | **€0** — 2 active users, unlimited projects, 2 GB | Vendor + review |
| **Contracktime** Premium | FR | **€15/month for 5 users**, 25 GB, **+€5/user/month** | Vendor + review |
| **Capmo** Pro | DE | **from €39/user/month**, volume-based, all features included | Vendor pricing page |
| **KI-Syndikat** implementation guidance | DE | **€50–100/month** entry (Claude/ChatGPT); **€300–800/month** integrated | Consultancy page |
| **CAC NAM** trial | DE | **10% of list price for 3 months**, unrestricted full version | Vendor |
| **Nachtragsmanager** | DE | "Den Preis nennen wir in der Vorführung, weil er vom Umfang abhängt" | Vendor |
| **BauAgent.ai** | DE | Custom by company size; framed as *one Nachtrag pays the year* | Vendor |
| BlackSwanAI, Handwai, SmartClaim, Ronayz, ContraVault, CALIM | — | **Not disclosed** | — |

**Method and confidence:** all HIGH-confidence figures come from vendor pricing pages or from contractmanagement.fr, an independent French comparison site that publishes tested pricing. Nothing was inferred from resellers.

**The pricing finding that matters:**

```
€15/user/mo   Contracktime  — evidence capture only, no AI, no entitlement, no quantum
€39/user/mo   Capmo         — logging + AI search
€199/user/mo  Contradic     — event detection + evidence graph + claim drafting, no quantum
€349/user/mo  Contradic Ent.
€599/CASE     Easyclaim     — quantum + court-ready package, no detection
£435/licence/mo CEMAR       — (from prior agent) register + clock under NEC
```

Two independent regimes (French general contracts, UK NEC) have independently converged on the **€200–500 per seat per month** band the moment the product does entitlement-adjacent reasoning; and **Germany independently discovered per-claim pricing at €599**. The €15 and €39 tiers are logging. **The 13x price step happens exactly at the point where the product stops recording and starts reasoning.**

---

## 5. INTEGRATIONS & API — DATA EGRESS REALITY

| Product | Open | Closed | Notes |
|---|---|---|---|
| Contracktime | **Outlook add-in (MS Store)**, **Google Workspace Marketplace**, MS Project import, Excel import | No public API found | "Less optimal outside the Microsoft environment" |
| Contradic | — | CRM/ERP/SSO listed as **future**; no public API | Azure AI (EU) hosting |
| BauAgent.ai | WhatsApp (live); M365/Outlook, OneDrive, Google Calendar/Drive, M-Files, Exchange | Mail/calendar integration **mid-2026** | EU-hosted, DSGVO |
| Easyclaim / Nachtragsmanager | **None by design** — offline single HTML file, no server, no account, local file storage | Everything | This *is* the product's security pitch |
| CAC NAM | **GAEB-90** standard interface (LV, calculation, billing exchange) | — | The German file-exchange standard, analogous to XER's role in scheduling |
| BlackSwanAI | **GAEB** and VOB standard compatibility | — | Open Telekom Cloud Frankfurt, EU-only LLM processing, no third-party data sharing |
| Handwai | "Works as an extension to existing construction software via industry standards" | No specifics disclosed | — |
| ContraVault AI | **Procore, Autodesk Construction Cloud, PlanGrid, MS Project**, plus API | — | The only non-English product with Procore/Autodesk connectors |
| Formilo | API/webhooks into ERP, contracting and construction-management systems | — | Bespoke, ownership transferred to client |

> **Strategically important:** **GAEB** is Germany's mandated open exchange format for Leistungsverzeichnisse, calculations and billing — and CAC NAM and BlackSwanAI both consume it. This is the German equivalent of the program's XER finding: **a contractually-produced, openly-documented file that a solo founder can parse without any vendor relationship.** GAEB (specifically GAEB DA XML / GAEB-90) is the strongest upload-first ingest path in the German market, and it carries the priced bill of quantities — i.e. it carries the *quantum baseline*, which XER does not.

---

## 6. WEAKNESSES AND EXPLICIT GAPS — DELIBERATE OR UNATTENDED?

| Gap | Where | Deliberate or unattended? |
|---|---|---|
| **No quantum in any AI claims product, in any language** (Contradic 0, SmartClaim 0, BauAgent 0, ContraVault 0, Ronayz 0) | Global | **Unattended → opportunity.** German cost law makes it hard (below), but nobody has even attempted it inside an AI product. The one product that does it well (Easyclaim) has no AI at all. |
| **No event detection from passive project data** anywhere in Germany | DE | **Unattended.** Both German AI products require a human to initiate (a WhatsApp message; an LV upload). The German trade press asserts AI "kann aus Bautagebüchern, Protokollen und Schriftverkehr automatisch potenzielle Nachtragstatbestände vorschlagen" — but **credits no vendor with the capability**, presenting it as a 2026 trend ([gaim-solutions](https://gaim-solutions.com/de/blog-system/kostentransparenz-bauprojekte-software-2026)). |
| **No disruption/causation analysis in any European product** | EU | **Structurally deliberate.** The evidential bar (BGH 21 Mar 2002: an indispensable *"konkrete bauablaufbezogene Darstellung"* of each hindrance) is high enough that the market has settled on **professors and expert witnesses working in MS Project/Asta/Excel**. This is the deepest moat and the deepest gap simultaneously. |
| **No German notice-deadline product** | DE | **Deliberate and correct.** "Unverzüglich" is not countable. A clock cannot be built. |
| **Consultancies not productising** | DE | **Deliberate.** Drees & Sommer's Dreso.AI is expressly internal-productivity, not a product. HKA, Claimscale, Primestone, MCE-Consult, claim.m — pure services. Heilfort teaches rather than ships. |
| **Contradic sells to law firms, not contractors** | FR | **Deliberate (for now).** Founder names legal departments and specialised firms as the beachhead, energy as the reference sector, SMEs and large enterprises as later ambitions. **BTP is not the wedge.** Leaves the contractor-side of French construction open. |
| **No Nordic/Dutch/Italian/Spanish/Polish claims product at all** | EU | **Unattended, but note the warning:** three of these (SE, NO, IT) have *stricter* notice regimes than the US and still produced nothing. Absence here is **not** validated pain. |
| Contradic: hallucinations on jargon-heavy technical documents; no multi-LLM; immature UX | FR | Unattended (early-stage) |
| Contracktime: no AI at all; Excel-only meeting import; nascent contract-type library | FR | Unattended — and it caps the product at tooling price |
| CAC NAM: built on the pre-2019 *Urkalkulation* doctrine the BGH has since displaced; site content stale since 2021 | DE | Unattended → the legacy incumbent is exposed |
| Easyclaim: no ingest of anything, no detection, desktop-only, one-person company | DE | **Deliberate** — offline-by-design is its trust pitch to expert witnesses and courts |

---

## 7. ADJACENCY TEST — HOW HARD FOR THEM TO SHIP THE FULL PIPELINE?

**Contradic (FR): MEDIUM.**
Data access is already solved — it ingests contracts, emails, minutes and schedules, and it has the hardest piece (the cross-document evidence graph, scored 3). Org incentive is right: it is a claims-native company with no owner-side franchise to protect, so **it can take a side** — the structural constraint that blocks Procore, Trimble, Oracle and Clearstory. What it lacks is quantum, and quantum is where the hard part sits: it would need a cost model, and its beachhead (law firms) is precisely the customer least able to supply cost data. Its GTM motion (legal departments) also fights against the construction commercial buyer. Rate **MEDIUM**, 12–24 months, and only if it pivots the ICP toward contractors.

**BauAgent.ai (DE): MEDIUM-HARD.**
It owns the notice artefact and the field capture channel. To reach quantum it must model German cost law after the BGH's 2019 turn to *tatsächlich erforderliche Kosten* (§650c BGB) as extended in Nov 2024 — a moving target that ARGE Baurecht says practitioners routinely get wrong. To reach true detection it must ingest email and calendar, which is on the roadmap for **mid-2026**. Closed beta, single founder. Rate **MEDIUM-HARD**.

**Easyclaim / C. Abraham (DE): HARD.**
The company is one expert and a deliberately offline HTML program. It has no ingest, no server, no account system, and its market credibility rests on the fact that *"das Dokument wurde nicht von einem Automaten erstellt."* Adding AI detection would attack the very trust position that sells the €599 service. Rate **HARD** — and note that this makes it a **partner, not a competitor**.

**The German ERPs (RIB iTWO / NEVARIS / BRZ): HARD.** 6–18 month implementations, ERP incentives, no claims-AI shipping behaviour observed.

**Thinkproject (DE, owns CEMAR): MEDIUM but unwilling.** It has the NEC/FIDIC contract-event engine, a Munich HQ and eight years of German market access — and has never shipped a VOB/B product. That is a revealed preference, not a capability gap.

**CALIM (QA): MEDIUM.** It already performs the whole pipeline manually and has begun productising the cheap end (calculators, readiness score). The blocker is that it is a consultancy: productising the full pipeline cannibalises billable hours. Classic innovator's dilemma.

---

## 8. STARTUP POSTURE

| Entity | Posture | Why |
|---|---|---|
| **Contradic (FR)** | **ROADKILL if you fight it in France; irrelevant elsewhere** | It is a direct thesis competitor with better funding prospects and the evidence-graph capability. But it is not in construction-first, not in English, and not in the US. Do not enter France. |
| **Easyclaim / C. Abraham (DE)** | **PARTNER — highest-value partner found in this pass** | It holds the one capability nobody else has (defensible construction quantum) inside a one-person company with no distribution, no ingest, no AI, and a 2017-era delivery model. The complementarity is near-perfect: **you bring detection + evidence, they bring the number that survives court.** A licensing or white-label conversation is available to a solo founder in a way that a conversation with Procore is not. |
| **BauAgent.ai (DE)** | **Competitor-in-waiting, but in a different language and channel** | Closed beta, WhatsApp-native, VOB/B-hardcoded. Its *pricing framing* — "one Nachtrag finances the annual subscription" — is the single most transplantable idea in this report and should be copied verbatim into US positioning. |
| **Contracktime (FR)** | **PROOF OF FEASIBILITY, not a competitor** | One contract manager shipped email-native event capture into two app marketplaces. It proves the V1 is solo-buildable and simultaneously proves that stopping there caps you at €15/month. |
| **CALIM (QA)** | **CHANNEL** | A FIDIC consultancy with GCC + India + USA offices already giving away notice calculators as lead-gen. The natural distributor for a quantum/evidence engine into FIDIC markets. |
| **ContraVault (IN)** | **PARTNER or CHANNEL** | It has Procore and Autodesk connectors and 30+ Indian enterprise logos, but its claims module is thin and quantum is absent. It is a distribution asset in a market you would otherwise never reach. |
| **Thinkproject / CEMAR (DE→UK)** | **ROADKILL in NEC, irrelevant in VOB** | Do not enter NEC. Confirmed by two agents now. |
| **Nordic / Dutch / Italian / Spanish / Polish vendors** | **NON-ENTITIES** | Nothing to partner with, nothing to fear. Also: nothing to learn from, except the negative lesson. |

---

## 9. TOP CUSTOMER COMPLAINTS RELEVANT TO THE THESIS

⚠ **Material limitation, stated honestly: independent customer complaints for non-English claims software are essentially non-existent.** Capterra Germany has **no Nachtragsmanagement category**. GetApp DE lists an "EasyClaim" entry but it is a different product (insurance claims), not the construction Bauzeitnachtrag tool. German and French vendors publish testimonials, not reviews. The closest thing available is **professional independent review criticism**, which I quote verbatim rather than inventing user complaints:

1. **On Contradic (independent French review, 2026):** *"une solution jeune mais prometteuse"* — with named defects: responsive-design failures, French/English translation gaps, **hallucinations on highly technical/jargon-heavy documents**, limited agent templates, **not yet multi-LLM**. — https://contractmanagement.fr/avis/contradic/
2. **On Contracktime (independent French review, 2026):** *"quelques bugs d'affichage, onboarding perfectible, fonctionnalités encore en construction"*; usage is **"less optimal outside the Microsoft environment"**; meeting records can only be imported via Excel, not Word or PDF; the contract-type reference library is **nascent**. — https://contractmanagement.fr/avis/contracktime/
3. **On the German claims-calculation problem (ARGE Baurecht, the German construction-law bar association):** *"Die vom BGH postulierte auskömmliche Vergütung ergibt sich also nicht per se dadurch, dass auf die Selbstkosten ein Aufschlag von 15 bis 20 Prozent vorgenommen wird."* — i.e. the industry's standard markup practice **systematically under-recovers**. — https://www.arge-baurecht.com/service/presse/pressemitteilungen/artikel/nachtragskalkulation
4. **On Norwegian NS 8405 practice (Proanbud):** the common failure is that *"the contractor discusses the change orally but does not formally notify and document it."* The pain is articulated as a **behavioural** failure, not a software gap. — https://proanbud.no/artikler/ns-8405-ns-8407-endringshandtering
5. **On Dutch UAV 2012 (flux.partners):** payment arrangements and *meer- en minderwerk* are *"the two subjects that lead to the most conflicts in construction practice"*, and the UAV's provisions, though detailed, are **"far from unambiguous"** in application. — https://flux.partners/kennisbank/contractvormen/uav/

> ⚠ **Read the pattern, not the quotes.** In four languages the pain is articulated as *legal complexity* and *behavioural discipline* — never as *"my software doesn't warn me."* This is the **third independent confirmation** (after the Procore and NEC agents) that **the buyer does not describe this problem as a software gap** and therefore will not arrive via search. Inbound/SEO GTM is falsified again, now in German, French, Norwegian and Dutch.

---

## 10. HARDEST FACTS

1. **Contradic charges €199/user/month (€1,990/yr) Team and from €349/user/month (€3,490/yr) Enterprise** for AI event detection + evidence graph + claim drafting — **with no quantum at all**. Proves the €200–350/seat/month band exists outside the NEC regime. → https://contractmanagement.fr/avis/contradic/
2. **Easyclaim sells a complete Bauzeitnachtrag as a €599-net per-case service**, delivering a **21-page** derivation covering **26 cost categories** under §642 BGB / §6(6) VOB/B. **Per-claim pricing for a claims artefact is a shipping, paid-for business model** — the chargeable artefact the Levelset analysis said contractual notice lacks. → https://bauzeitnachtrag-leichtgemacht.de/
3. **German VOB/B §6 Abs. 1 imposes a mandatory written hindrance notice with NO day count** — *"unverzüglich"* = *ohne schuldhaftes Zögern*, in practice same day or next working day — **and §6 Abs. 1 S. 2 forgives the omission entirely where the facts and their hindering effect were *offenkundig* to the client.** The largest construction market in Europe has a mandated notice regime that is **structurally unclockable and not a strict condition precedent** — unlike FIDIC 20.2.1 (28 days, express condition precedent) or NEC4 61.3 (8 weeks). → https://dejure.org/gesetze/VOB-B/6.html · https://www.bauagent.ai/blog/behinderungsanzeige-vob-muster-vorlage · https://www.lexisnexis.com/en-gb/legal/guidance/fidic-contracts-2017-contractor-employer-claims
4. **VOB/B § 2 Abs. 6 requires the contractor to announce the claim BEFORE starting the additional work** — *"Er muss jedoch den Anspruch dem Auftraggeber ankündigen, bevor er mit der Ausführung der Leistung beginnt"* — and **§ 4 Abs. 3 requires a written Bedenkenanzeige "unverzüglich – möglichst schon vor Beginn der Arbeiten."* Germany mandates **three** distinct pre-emptive notices and **still produced no notice product**. → https://dejure.org/gesetze/VOB-B/2.html · https://dejure.org/gesetze/VOB-B/4.html
5. **German Bauhauptgewerbe 2025: €171.9bn revenue (+5.3% nominal, +2.4% real — first real increase since 2020), €113.0bn order intake (+9.2%), backlog +10.2%.** The market is large and, for the first time in five years, growing in real terms. → https://www.zdb.de/meldungen/solides-baujahr-2025-starke-branche-bereit-fuer-draengende-aufgaben
6. **Handwai claims 600+ construction firms, 4,000+ completed VOB projects, 86% repurchase rate and a +7% average margin gain** from AI VOB automation. **UNVERIFIED — vendor-stated only, no third-party corroboration found.** If even directionally true it is the largest adoption figure for a claims-adjacent AI product in any non-English market. → https://handwai.io/
7. **A German court expert's own worked example: €15.90/h gross wage + €14.19/h payroll overhead = €30.09/h self-cost against a €50.00/h market rate — a required markup of 166%** — while the industry habitually applies 15–20%. → https://www.arge-baurecht.com/service/presse/pressemitteilungen/artikel/nachtragskalkulation
8. **BGH 21 March 2002 made a *"konkrete bauablaufbezogene Darstellung"* of each hindrance indispensable for a §6(6) VOB/B claim** — and the German market's answer, 24 years later, is a professor teaching the *Bauablauf-Differenzverfahren* (published in *BauR*, 2003) executed by hand in MS Project, Asta Powerproject and Excel. → https://heilfort.de/30-nachweis-haftungsbegruende-haftungsausfuellende-terminliche-kausalitaet-bauablaufstoerungen-bauablauf-differenzverfahren/

---

## 11. UNKNOWNS — AND WHAT WOULD SETTLE THEM

| Unknown | What would settle it |
|---|---|
| **Easyclaim's software licence price** and unit volume | A demo call, or a German reseller quote. Only the €599 service tier is published. |
| **Whether Handwai's 600 firms / 86% repurchase / +7% margin are real** | An independent case study, a German trade-press profile, or a Handelsregister filing showing revenue. Currently vendor-stated only. |
| **BauAgent.ai's actual price point and beta size** | Exit from closed beta, or a published pricing page. "One Nachtrag finances the year" is a framing, not a number. |
| **Whether Contradic has any construction (BTP) customers at all** | A named case study. The only reference disclosed is an energy client. If BTP adoption is zero, French construction is still open. |
| **Whether Contradic is planning English/US entry** | The 2026 funding round announcement, or an English-language site. No signal found either way. |
| **Whether Thinkproject intends to bring CEMAR's event-register model to VOB/B** | Thinkproject Live London, 3 Nov 2026, or a German product-page launch. Eight years of silence is strong evidence against. |
| **Whether the new Swedish AB 25 / ABPU 25 standard creates a product window** | The published AB 25 text and the first commentary on its *underrättelse* mechanics. A regime change is the one moment a new register product can be sold. |
| **Whether any German insurer/surety pays for claim-readiness** (the German analogue of the US surety angle) | Interviews with VHV / R+V Bauversicherung, the two dominant German construction insurers. |
| **Actual size of the German Nachtragsmanagement consulting spend** | No public figure found. Would need a Lünendonk study or BDU (Bundesverband Deutscher Unternehmensberater) segment data. This is the number that would size the consultant-replacement opportunity. |
| **Whether Italian *riserve* practice creates any software demand** | ANAC or MIT data on riserve volumes and outcomes; interviews with Italian general contractors. The regime is the strictest found and the software response is zero — the reason matters. |
| **CALIM 360's actual capability** | It is behind a contact form. A demo would establish whether the consultancy has built a real platform or a client portal. |

---

## APPENDIX A — THE REGIME COMPARISON TABLE (the central strategic artefact)

| | 🇺🇸 AIA A201 | 🇩🇪 VOB/B | 🇬🇧 NEC4 | 🌍 FIDIC 2017 | 🇸🇪 AB 04 | 🇳🇴 NS 8405 | 🇮🇹 riserve |
|---|---|---|---|---|---|---|---|
| Notice mandated by the form? | Yes (§15.1.3) | **Yes ×3** (§2(6), §4(3), §6(1)) | Yes (cl. 61.3) | Yes (cl. 20.2.1) | Yes | Yes | **Yes** |
| **Countable deadline** | 21 days | **NO — "unverzüglich"** | **8 weeks** | **28 days** (+84 for detailed claim) | "utan dröjsmål" | "uten ugrunnet opphold" | **"primo atto idoneo"** |
| Strict condition precedent | Weak in practice | **No** — *offenkundig* exception | Yes | **Yes, express** | Can forfeit | Deemed acceptance on client silence | **Yes — *decadenza*** |
| Named contract administrator in-system | Architect | **None** | Project Manager | Engineer | None | None | Direttore dei lavori |
| Contractual register of events | No | **No** | **Yes** | Effectively | No | No | **Registro di contabilità** |
| Mature notice/register software exists | **No** | **No** | **Yes** (CEMAR, Gather, FastDraft, Sypro, Contract Bee) | **Partly** (CALIM 360, Ronayz) | **No** | **No** | **No** |
| Mature quantum software exists | No | **YES (Easyclaim, CAC NAM)** | No | No | No | No | Accounting only |
| Mature detection software exists | No | **Partly (BauAgent.ai, beta)** | **Yes (Gather)** | No | No | No | No |

**What this table says, in one line:** *the register-and-clock product appears if and only if the contract supplies both an integer deadline and a named administrator; the quantum product appears if and only if the law supplies a computable cost methodology (Germany's §650c BGB / §2(3) VOB/B); and the detection product has appeared nowhere at scale, in any regime.*

**The strategic implication for the US:** the US supplies neither an integer that matters nor a computable statutory cost method — which is why neither product type exists there. But it does supply the largest pool of unrecovered dollars and the highest tolerance for outcome-based pricing. **The transplant is not the German product. The transplant is the German pricing model (per-claim, artefact-anchored, €599) applied to the French capability (cross-document event detection and evidence chronology) — with the quantum step built, because that is the step every AI product in every language has skipped.**

## APPENDIX B — GERMAN TERMS FOR FUTURE RESEARCH

| German | Meaning | Why it matters |
|---|---|---|
| Nachtrag / Nachtragsmanagement | Change order / claim, and its management | The market's own name for the category |
| Nachtragsanmeldung | The §2(6) pre-notice of a claim | Required **before** starting the work |
| Behinderungsanzeige | §6(1) notice of hindrance | The German "early warning" |
| Abmeldung der Behinderung | Notice that a hindrance has ended | **Also mandatory** — a second, widely-missed obligation |
| Bedenkenanzeige / Bedenkenanmeldung | §4(3) notice of concerns about the client's design, materials or preceding trades | Third mandated notice; shifts liability |
| Bauablaufstörung / gestörter Bauablauf | Construction-process disruption | The disruption-analysis discipline |
| Bauablaufbezogene Darstellung | Process-related presentation of each hindrance | **The BGH-mandated evidential standard** |
| Bauzeitnachtrag | Time-related claim (prolongation/disruption cost) | What Easyclaim computes |
| Urkalkulation | The original build-up of the tender price | The historic basis of Nachtrag pricing, displaced by BGH 2019 |
| Tatsächlich erforderliche Kosten | "Actually required costs" (§650c BGB) | The **current** legal basis for pricing changes |
| Mehrkostenforderung (MKF) | Austrian equivalent claim under ÖNORM B 2110 | Austria's term |
| ÄTA-arbeten | Swedish changes/additions/omissions (AB 04 ch. 2) | Sweden's term |
| Meerwerk / minderwerk | Dutch additional/reduced work (UAV 2012 §35) | Netherlands' term |
| Riserve | Italian reservations inscribed in the accounting register | Italy's term — strictest regime found |
| GAEB / GAEB DA XML | German open exchange standard for LVs, calculations, billing | **The German XER-equivalent: the free path in** |
| EFB 221 / Formblatt 221 | German public-procurement price-breakdown form | Machine-readable cost structure, already produced by contract |
