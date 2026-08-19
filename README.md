# Freight Revenue Recovery — Venture Research

Is there a large, defensible business in automatically identifying and recovering freight revenue that carriers, brokers and logistics operators fail to bill or collect — detention, TONU, layover, accessorials, lumper fees, demurrage, shortages, damages and invoice mismatches?

**Verdict: PIVOT.** → [`outputs/10-go-pivot-kill-memo.md`](outputs/10-go-pivot-kill-memo.md)

---

## The finding in one paragraph

Detention alone is a **$15.1B** annual problem occurring on **39.3% of all US truck stops**, and **94.5% of fleets bill it while being paid on fewer than half their invoices** (ATRI, 2024). Total disclosed venture funding in carrier-side recovery: **$0** — while the *opposite* side, which profits by denying those same charges, raised **$75M in July 2026 alone**. That asymmetry looks like an open lane.

It mostly isn't, for a reason nothing in the market discusses. Four real broker-carrier agreements were read in full text, and every one extinguishes the entitlement **at the dock**: Arrive Logistics requires notice **30 minutes before detention begins**; TQL voids detention entirely for a lapsed GPS ping; Flock's language is *"Carrier hereby forfeits and waives any right to payment."* **A product that discovers unbilled detention six weeks later is not recovering a claim — it is requesting a favour from the party that wrote the forfeiture clause.**

The same engine pointed at a **broker's own unbilled receivables** — accessorials paid to a carrier and never billed to the customer — faces no forfeiture clause, no collection-agency licensing, no factoring assignment problem, and a deal roughly ten times larger. That is the pivot, and it is gated on one number nobody has ever published.

## The ten deliverables

| # | Document | What it answers |
|---|---|---|
| 1 | [Competitor landscape](outputs/01-competitor-landscape.md) | Who is here, and which side of the invoice they serve |
| 2 | [Capability matrix](outputs/02-capability-matrix.md) | 30 vendors × 25 dimensions ([CSV](data/capability-matrix.csv)) |
| 3 | [Substitute-stack matrix](outputs/03-substitute-stack-matrix.md) | What buyers actually assemble today, and what it costs |
| 4 | [Buyer / JTBD matrix](outputs/04-buyer-jtbd-matrix.md) | Which buyer feels this most — and the reframe that changes the job |
| 5 | [Top 5 wedges](outputs/05-top-5-wedges.md) | Seven candidates scored against nine survival criteria |
| 6 | [Red-team report](outputs/06-red-team-report.md) | Every wedge attacked along eight vectors |
| 7 | [Solo-founder MVP](outputs/07-solo-founder-mvp.md) | The narrowest sellable V1, and what it deliberately omits |
| 8 | [Pricing hypothesis](outputs/08-pricing-hypothesis.md) | Is percentage-of-recovery viable? |
| 9 | [First-20-customer plan](outputs/09-first-20-customers.md) | Channels, objections, milestones, kill triggers |
| 10 | [GO / PIVOT / KILL memo](outputs/10-go-pivot-kill-memo.md) | **The verdict** |

## Five things worth knowing before you read further

1. **Everyone who holds the timestamp is paid by the party who owes the money.** project44's carrier agreement §5.2 gives project44 ownership of any output *derived* from carrier data. FourKites §3.4 does the same for aggregate data, with distribution gated by the shipper. A carrier feeds the raw material for its own detention evidence and never receives a claim artefact it controls.
2. **Everyone who holds the invoice lacks the entitlement data.** TriumphPay engages 63% of all brokered freight and scores **0** on GPS/ELD timestamps, appointment ingestion, and biller-direction accessorial detection.
3. **Nobody reads the rules.** Rate-con *rule* extraction — free time, $/hr, increment, cap, notice window — is unclaimed across 40+ vendors. Vooma and Drumkit, the two best-funded rate-con ingestion products, both score 0. Everyone extracts fields; nobody extracts rules.
4. **Nobody prices on outcome except humans.** ClearLane (10–25%), Recoupex (20–50%), collection law firms (25–40%), Betachon (50%) — all human services. No software product in this market is priced on recovery.
5. **The strongest legal position in the study is in the ocean, not on the road.** 46 CFR §541.5: *"Failure to include any of the required minimum information… eliminates any obligation of the billed party to pay the applicable charge."* Twenty enumerated invoice fields, a 30-day clock, burden of proof on the carrier. Parked, with a stated trigger.

## Evidence standard

Every material claim is labelled **VERIFIED** (primary source), **CLAIMED** (vendor marketing), or **UNKNOWN** (could not establish). Derived figures show their arithmetic. ROI assumptions are individually marked CITED or ASSUMED. Where no rigorous data exists, the finding recorded is "NO RIGOROUS DATA FOUND" — treated as a research result, not a gap to fill with an invented number.

Three corrections to the original brief were found and are noted in place: the DOT OIG detention report is **ST2018019**, not ST-2018-002; FourKites has no "Fin AI" product; McLeod has no product called "Flowbot".

## Known limitations

- **Desk research only. No customer interviews.** Every conclusion about willingness to pay is inference.
- **The session's web-search budget was exhausted partway through.** Roughly half the agents completed later work via direct fetch only; several lanes are thinner than they appear.
- **Reddit, LinkedIn and TIA were unreachable** (domain-blocked / 429 / 403). **There are no primary practitioner voices here.** No quotes were fabricated to fill the gap, but "what operators actually say" is genuinely unvalidated.
- **ATRI's primary PDFs are lead-gated**, so the single most important statistic in the thesis reaches us through secondary reporting — and the agent that sourced it flagged that its two components may not be legitimately multiplicable.

## Repository map

```
00-MASTER-PROMPT.md      the brief, verbatim
METHODOLOGY.md           agent roster, evidence standard, scoring rubric
outputs/                 the ten deliverables
research/raw/            the fifteen unedited agent reports — the evidence base
research/economics/      hard numbers and three ROI models
research/legal/          contracts, statutes, licensing
data/                    capability matrix (CSV) + dimension definitions
scripts/                 helper to lift this tree into a standalone repo
```

This is research, not implementation. No product code is written unless the verdict becomes GO and a build is separately requested.
