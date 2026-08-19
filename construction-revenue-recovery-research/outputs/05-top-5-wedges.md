# 5. Top 5 Wedges

Eight wedges were generated; the red team killed five and inverted the ranking. Shown here are the five
highest-scoring, each with its post-red-team status. Full specifications (13 fields each) are in
[`research/SYNTHESIS-wedges.md`](../research/SYNTHESIS-wedges.md); the attacks are in
[`research/REDTEAM-report.md`](../research/REDTEAM-report.md).

| Rank | Wedge | Synthesis score /90 | Red-team verdict | Final standing |
|---|---|---|---|---|
| 1 | Matter Zero | 72 | **WOUNDED** | Demoted — repriced entitlement layer |
| 2 | **Day 20** | 70 | **WOUNDED — strongest survivor** | **PROMOTED TO FUNDED PICK** |
| 3 | Write-Off Autopsy | 68 | **KILLED as paid work** | Survives free, as data acquisition |
| 4 | The Defensible Price | 65 | **KILLED** | Dead |
| 5 | Backup Pack | 49 | **KILLED** | Dead |

---

## Wedge 2 — DAY 20 *(the funded pick)*

**One line.** The Caltrans Supplemental PCR engine: an itemised cost estimate and a time impact analysis
produced inside the 20-day statutory window, from daily reports and schedule snapshots the contractor is
already required to produce.

**The problem.** Caltrans Standard Specifications §§5-1.42–5-1.43D require an Initial Potential Claim Record
within **5 business days**, and a Supplemental with an **itemised cost estimate and a TIA within 15 more**.
Failure means *"Waiver of the potential claim… Bar to arbitration (Pub Cont Code §10240.2)."* Public Contract
Code §9204 **expressly exempts Transportation**, so the regime is not statutorily displaced.

**Why this and not notice alerting.** Caltrans already runs ePCR with email reminders — **alerting is free.**
The mandated *artefact* — a costed estimate plus a TIA in 20 days — is what nobody produces. It is, almost
literally, a written specification for a quantum engine, published by the counterparty.

**Buyer.** Project executive at a $50–300M California heavy-civil DOT contractor. Reached through UCON
(800+ member firms, ~$1,000 associate access).

**Artefact.** The PCR pack: itemised cost estimate with its derivation stated, windows TIA on dated XER
snapshots, evidence index, and the completed form as a PDF for a human to sign and file. **Gap analysis is
in-session, ephemeral, never persisted. No responsibility verdict. No filing. No Caltrans contact.**

**Why add it when they have software, staff and consultants?** Because the counterparty wrote the
specification and set the clock. Procore/ACC hold the records but produce no costed estimate; a consultant
costs $240k–660k and arrives after the loss; and the in-house Change Order Engineer cannot produce a TIA in
15 days across concurrent jobs. This is the strongest add/switch rationale in the set — *the buyer's own
spec book answers the "GC 101" objection.*

**Incumbent coverage.** Nobody exceeds 1 on evidence completeness, quantum, or claim package. The substitute
scores 2/10 at day 20.

**Solo-founder V1.** XER/MPP snapshot upload + daily-report upload + contract PDF. No Procore API. No email
integration required at V1.

**Price.** **$3,500/pack + $600/project/month readiness base**, job-costed, never per seat.

**Defensibility — this is where it fails.** Date arithmetic is trivially copyable and checkable in 30
seconds. Fifty spec books is depth, not a moat. **The wedge does not pass the defensibility criterion and
this should not be glossed over.**

**Kill conditions.** CPRA returns <1.5 waived-or-unsupplemented PCRs per contract per year; ≥7 of 10 PXs say
they already comply on time; ≥2 of 3 lawyers veto a machine-generated pack; a platform ships a DOT claim
module.

---

## Wedge 1 — MATTER ZERO *(demoted)*

**One line.** Same-day linked chronology, entitlement register and missing-evidence schedule from a raw
document dump, sold per matter to claims consultancies.

**Why it was funded.** The only wedge where the pain is an **already-invoiced line item** — 200–600 hours per
matter — rather than a modelled leak. Buyer signs same-week and rebills as a disbursement.

**How it was wounded — three separate hits.**
1. **The moat had already shipped.** Relativity **aiR for Case Strategy**, GA 12 Jan 2026, builds fact
   chronologies with citations *and evidence-gap analysis*, **included in RelativityOne at no extra cost.**
2. **The rate basis was wrong.** Diales derives at **£165–200/hr**, not $400. *(The red team then
   over-corrected: for a US buyer the correct analyst basis is $175–275/hr → **$3,000–5,000/matter**. The
   price was never the real problem.)*
3. **The channel rebuttal is arithmetically false.** The tool removes **13–22% of matter hours**. A matter
   uneconomic at $240K is still uneconomic at $190K — so "bid the sub-$5m matters you turn away" fails.

**The real kill: the fee model.** Consultancies bill time-and-materials (*"In most instances… time-and-
materials"* — CRA 10-K). Removing hours is **revenue-negative**, and *"nobody's compensation plan rewards
that."*

**What survives.** Not the chronology — **the entitlement layer on top of aiR/Everlaw** at $2,500–4,000/matter.
aiR is eDiscovery-framed: no notice register, no EOT/compensable split, no Division 00 awareness.

---

## Wedge 3 — WRITE-OFF AUTOPSY *(killed as paid work, survives free)*

**One line.** Send last year's closed jobs and write-off ledger; get back which write-offs had the evidence
to bill.

**The kill.** As a paid engagement the artefact is a CFO-commissioned, portfolio-wide catalogue of the
buyer's own record failures — **a business audit, not work product** — usable against them in every future
claim.

**What survives.** Run it **free, anonymised, counsel-mediated, verbal readout only**, as Phase-0 data
acquisition. It builds the record-quality-vs-outcome dataset that **nobody in the industry has**. You can be
paid or safe, not both.

---

## Wedge 4 — THE DEFENSIBLE PRICE *(killed)*

Productivity-loss quantum using published MCAA/ELECTRI factors cited on the face of the output. Attacks
**disputed pricing** — the *larger* cause of short-payment (66% vs 53%).

**The kill.** MCAA factors are *"based on contractor opinions not empirical studies"*; boards prefer the
measured mile; **Ankura publishes the attack**. Handing a claimant a citable factor table arms the payer,
who will cite the critique.

---

## Wedge 5 — BACKUP PACK *(killed)*

Every COR ships with indexed substitution attached, first time. Deliberately boring, no AI in the pitch.

**The kill.** **Clearstory's COR Pricing Agent** entered closed beta 28 May 2026 — drafts the COR, prices it,
assembles backup — with GA later in 2026, on $2.1B/month of change-order evidence and 14,000 contractors.

---

## The three that never got close

**Notice Sentinel** (35) — the obvious idea, **falsified eight independent ways**: Aconex already tracks
response deadlines at a full 3; Levelset proved the *filing* was the revenue; Trunk Tools gives extraction
away free; Procore shipped Contract Review; Document Crunch ships agentic notices; Caltrans runs ePCR
reminders; contractors deliberately suppress notice; and Copilot Researcher answers it at $30/user/month.

**Deficiency Schedule** (47) — owner-side. Copyable, neutrality-price-capped, procurement-gated, and a
one-way door that forecloses the contractor market.

**Portfolio Risk Radar** (34) — the deliberate control case. A verified uncontested gap at all five
incumbents with **zero paid-for-pain evidence** — exactly what the brief's rule is designed to reject. It
scored last, which is a check that the rule was applied.
