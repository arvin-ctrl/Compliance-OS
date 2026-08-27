# 7. Solo-Founder MVP Definition

## The question the brief asked

> *Can V1 work with one contract upload + project document upload/email forward + event extraction +
> deadline warnings + evidence linking + notice/claim generation, without direct Procore integration?*

**Yes on ingestion. No on scope.** Upload-first is not merely viable — it is *strictly better* than
integration, for four independent reasons. But four of the six named capabilities must be cut, because they
are commoditised, standards-blocked, or legally hazardous.

---

## Why upload beats integrate (four independent reasons)

1. **Access can be revoked.** Procore denied **Trunk Tools** API access in Sept 2025 and refunded its
   conference booth — a $70M-funded, Insight-backed company running 200+ Gilbane projects. A solo founder has
   no better standing.
2. **Parsing is contractually forbidden.** Procore's Developer Policy (eff. 30 Sep 2025) forbids developers
   to *"Scrape, parse, harvest, build databases, bulk export, or otherwise create copies of any API Data"*
   without consent, and forbids using API data to train or benchmark AI.
3. **The files are already mandated.** Contracts require monthly **XER** deliverables; Oracle publishes the
   field mappings; prior art (XER Schedule Toolkit, Schedule Auditor, ScheduleLens) shipped real products with
   zero Oracle relationship. Autodesk's **Data Connector** exports the evidence graph as free CSV *including
   relationship edges*.
4. **There is no evidential penalty.** Forensic delay analysis runs on **dated snapshots** regardless. Upload
   loses nothing that matters to the artefact.

**Bonus asymmetry:** because incumbents cannot legally read each other's data for AI, a file-upload/email-
forward V1 has *better* commercial-record coverage than the best-funded competitor. Trunk Tools has **no
email connector and no daily-log agent** — the two richest sources of contemporaneous commercial record sit
outside its corpus.

---

## The narrowest sellable V1

**DAY 20 — a Caltrans Supplemental PCR pack generator.**

### Ships

| Component | Detail |
|---|---|
| **Ingestion** | Contract PDF (Division 00 + Standard Specs reference), dated **XER/MPP** snapshots, daily reports (PDF/CSV/export), cost/labour records. Drag-and-drop. No API, no OAuth, no IT involvement |
| **Windows TIA** | Between dated snapshots, per SCL/AACE windows method. Presents *what the schedule shows*, never *who is responsible* |
| **Itemised cost estimate** | Per §5-1.43C.3, with **the derivation stated on the face of the output** — labour, equipment, materials, markup, each traceable to a source record |
| **Evidence index** | Every asserted fact linked to the daily report, photo, RFI or email that supports it, with date and document ID |
| **The pack** | Completed PCR form as PDF, for **a human to review, sign and file** |
| **Gap analysis** | **In-session, ephemeral, never persisted, never exported** |

### Deliberately excluded — and why

| Excluded | Reason |
|---|---|
| **Responsibility attribution** | **Standards-blocked.** AACE RP 29R-03 §1.2(f): *"Schedules… do not demonstrate root causation or responsibility for delays."* §1.1 exists to *"minimize… 'black-box' or 'voodoo' analyses."* An automated verdict hands opposing counsel a prepared attack |
| **Notice detection / deadline alerting** | Commoditised eight ways. **Caltrans already runs ePCR with email reminders — alerting is free** |
| **Clause extraction as a product** | Free from Trunk Tools; native in Procore since May 2026; owned by Trimble via Document Crunch |
| **Notice drafting as a product** | Document Crunch ships it agentically; Copilot does it at $30/user/month |
| **Any Procore/ACC integration** | Revocable, forbidden, and unnecessary |
| **Persisted missing-evidence schedule** | Discovery exposure. *Alta Refrigeration*, *G.M. Harston*: contractually-required and routine subscription output **held not protected** |
| **Contacting the owner** | Contractors **deliberately suppress notice to protect relationships.** Auto-contact guarantees rejection |
| **A "you are owed $X" verdict** | SCL Core Principle 12: **EOT ≠ money.** Naive delay-days × rate is wrong by construction for non-compensable Employer Risk Events. Separate time from money, always |

### The output must say what it is

The product presents **"here is what the record supports"** — never **"you are owed $412,000."** Time and
money are separated. The derivation is visible. A credentialed human signs it.

---

## Three purchases before the first line of code

1. **A named PSP / CCP / PE** to sign every TIA. The founder has no claims credential; a consultancy will not
   buy a chronology tool from someone who has never built one, and a board will not accept an unsigned TIA.
2. **A one-page written discovery answer**, from a construction litigator, that a project executive can hand
   to their general counsel. GC/risk is buyer #11 and holds a veto.
3. **UCON associate membership** (~$1,000) — the distribution channel, since inbound is falsified five ways.

---

## Build sequence

| Phase | Weeks | Work | Gate |
|---|---|---|---|
| **0 — Evidence** | 0–6 | File the CPRA request. Run the free Write-Off Autopsy on 30–50 anonymised closed matters. Interview 10 PXs and 5 consultancy partners. **No code** | G1–G3, G6 |
| **1 — Artefact** | 7–14 | XER diff + windows TIA + cost derivation + evidence index → PDF pack. Single-tenant, no accounts, files purged on session end | First signed pack |
| **2 — Repeatability** | 15–26 | Second and third customers. Template the 3–5 Caltrans districts' local variations | 3 paying by 31 Mar 2027 |
| **3 — Adjacency** | 27–44 | Entitlement layer on top of aiR/Everlaw for consultancies at $2,500–4,000/matter | 5 paying by 30 Jun 2027 |

## What makes this genuinely solo-feasible

No proprietary dataset is required — **nPlan's 750,000-schedule moat guards the wrong door**, because
causation is per-project document reasoning, not cross-project statistics, and both governing standards
(SCL free, AACE free to members) are public. No integrations. No procurement — it is job-costed at $3,500 a
pack. No 24/7 staffing: the clock is 20 days, not 20 minutes.

**The one thing that is not solo-feasible is the credential.** Budget for it, or the artefact cannot be
signed.
