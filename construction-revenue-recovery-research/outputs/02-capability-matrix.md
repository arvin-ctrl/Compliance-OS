# 2. Capability Matrix

Scale: **0** absent · **1** marginal/adjacent · **2** partial, or needs heavy config/services/3rd party ·
**3** strong native capability, marketed and evidenced.

Scores were assigned independently by 17 research agents against the same rubric, then adjudicated by
Category Manager A where agents disagreed. Corrections applied: Procore and InEight
`recoverable_dollar_estimation` 2→1 (both price a *change order*, not a *claim*; the differentiation against
Autodesk/Trimble was spurious); Autodesk `claim_identification` 0→1 (its RFI AI auto-populates Cost Impact
and Schedule Impact from free text).

Full data including categories not shown below: [`research/SCORES.csv`](../research/SCORES.csv).
`Max` is the highest score achieved by **any** of the 23 scored entities, not just those in the table.

| # | Dimension | Procore | Autodesk | Oracle | Trimble | InEight | Clearstory | Doc Crunch | Trunk | Gather | SmartPM | Easyclaim | Consultants | DIY stack | LegalTech | Pay/AR/Lien | Field cap. | Max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | contract ingestion | 3 | 2 | 2 | 3 | 2 | 1 | 3 | 3 | 2 | 1 | 1 | 3 | 2 | 3 | 1 | 1 | **3** |
| 2 | clause extraction | 3 | 1 | 0 | 3 | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 3 | 2 | 3 | 0 | 0 | **3** |
| 3 | notice detection | 1 | 0 | 1 | 2 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 2 | 1 | 2 | 3 | 0 | **3** |
| 4 | deadline tracking | 2 | 2 | 3 | 2 | 2 | 1 | 1 | 2 | 3 | 1 | 0 | 1 | 1 | 3 | 3 | 1 | **3** |
| 5 | rfi event ingestion | 3 | 3 | 3 | 3 | 3 | 1 | 1 | 3 | 1 | 0 | 0 | 3 | 3 | 1 | 0 | 3 | **3** |
| 6 | email ingestion | 3 | 3 | 2 | 2 | 3 | 1 | 0 | 1 | 1 | 0 | 0 | 3 | 2 | 3 | 1 | 1 | **3** |
| 7 | daily report ingestion | 3 | 2 | 2 | 3 | 3 | 1 | 0 | 2 | 3 | 0 | 0 | 3 | 3 | 1 | 0 | 3 | **3** |
| 8 | schedule integration | 2 | 3 | 3 | 2 | 3 | 0 | 1 | 2 | 3 | 3 | 1 | 3 | 2 | 1 | 0 | 1 | **3** |
| 9 | change order workflow | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 2 | 1 | 0 | 2 | 1 | 3 | 1 | 2 | 3 | **3** |
| 10 | claim identification | 2 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 3 | 1 | 1 | 3 | 1 | 0 | 1 | 1 | **3** |
| 11 | delay detection | 2 | 1 | 2 | 1 | 1 | 0 | 0 | 1 | 2 | 3 | 0 | 3 | 1 | 0 | 0 | 2 | **3** |
| 12 | responsibility attribution | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 0 | 3 | 2 | 1 | 1 | 1 | **3** |
| 13 | contemporaneous evidence graph | 2 | 3 | 2 | 2 | 3 | 2 | 1 | 2 | 3 | 1 | 0 | 2 | 1 | 1 | 1 | 2 | **3** |
| 14 | evidence completeness | 1 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 3 | 1 | 1 | 2 | 0 | 1 | 3 | 1 | **3** |
| 15 | recoverable dollar estimation | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 1 | 0 | 3 | 3 | 2 | 2 | 2 | 2 | **3** |
| 16 | claim package generation | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 2 | 1 | 3 | 3 | 2 | 1 | 2 | 1 | **3** |
| 17 | notice drafting | 2 | 1 | 2 | 2 | 1 | 1 | 3 | 1 | 3 | 0 | 0 | 2 | 2 | 2 | 3 | 1 | **3** |
| 18 | schedule impact analysis | 2 | 1 | 2 | 1 | 2 | 0 | 0 | 2 | 2 | 3 | 1 | 3 | 2 | 0 | 0 | 1 | **3** |
| 19 | procore integration | 3 | 2 | 1 | 3 | 0 | 3 | 2 | 2 | 2 | 3 | 0 | 0 | 2 | 0 | 3 | 3 | **3** |
| 20 | autodesk integration | 1 | 3 | 2 | 2 | 2 | 2 | 0 | 3 | 2 | 3 | 0 | 1 | 2 | 0 | 3 | 2 | **3** |
| 21 | outlook gmail integration | 3 | 2 | 2 | 1 | 3 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 2 | 3 | 1 | 1 | **3** |
| 22 | mobile workflow | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 0 | 0 | 0 | 3 | 2 | 2 | 3 | **3** |
| 23 | audit trail | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | **3** |
| 24 | portfolio risk | 3 | 3 | 2 | 2 | 2 | 2 | 2 | 1 | 3 | 3 | 0 | 2 | 1 | 3 | 3 | 2 | **3** |
| 25 | performance pricing compatibility | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 2 | 0 | 2 | 1 | **3** |
| 26 | consultant replacement potential | 1 | 0 | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 3 | 0 | 1 | 1 | 2 | 1 | **3** |
\* Magra's scores are **claimed, not verified** — its headline moved from $240K to $17,824 per event and all
eight integrations remain "Upcoming" with zero named customers. Included for completeness; treat as vapour.

---

## Where nobody scores 3

Twelve of twenty-six dimensions have **no incumbent at 3**. Applying the brief's rule — *a missing feature is
not white space* — only six survive as genuine opportunity:

| Dimension | Status | Why |
|---|---|---|
| **14 evidence completeness** | **SURVIVES** | Nobody exceeds 1. Scores **0** in the DIY stack. *"Nothing on earth checks whether a claim's proof is complete before a human submits it."* The only gap the industry admits to |
| **15 recoverable dollar estimation** | **SURVIVES** | Nobody exceeds 1 among incumbents; 0 across every AI-native product in every language. Paid for at €599/case and $240k–660k/matter |
| **16 claim package generation** | **SURVIVES** | Nobody exceeds 1. Consultants charge 600–1,650 hours to produce it |
| **26 consultant replacement** | **SURVIVES** | 200–600 chargeable hours per matter is the displaceable block |
| **25 performance pricing** | **SURVIVES** as pricing architecture | Legal for claim *preparation*; barred only for testifying experts |
| **10 claim identification** | **SURVIVES on a clock** | Procore shipped Change Analysis 23 Jul 2026 — closing fast |
| 3 notice detection | **KILLED** | Commoditised — free from Trunk Tools, native in Procore |
| 17 notice drafting | **KILLED** | Document Crunch ships it agentically; Copilot does it at $30/user/mo |
| 11 delay detection | **KILLED** | Served at $2,750–$25,000 by Acumen, SmartPM, Steelray |
| 18 schedule impact analysis | **KILLED** | Same |
| 12 responsibility attribution | **KILLED** | **Standards-blocked.** AACE RP 29R-03 §1.2(f): *"Schedules… do not demonstrate root causation or responsibility for delays"* |
| 24 portfolio risk | **KILLED** | Real gap, **zero paid-for-pain evidence**. Adjacent budget already spent on Briq |

## The shape of the void

Reading the matrix by column rather than by row: **every product builds up to the number and stops at the
number.** Five companies with different owners, ICPs, geographies and business models make the identical
stop. Not one of them — Procore, Autodesk, Oracle, Trimble, InEight — has a field for **clause reference,
notice date, notice deadline, or entitlement basis** on its change object.

That schema change is roughly one quarter of engineering with no liability tail, which makes it the cheapest
leading indicator available. Watch **Procore Groundbreak, 21–22 October 2026**.
