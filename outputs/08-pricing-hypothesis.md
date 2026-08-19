# 8. Pricing Hypothesis

Answers research question 9: **is percentage-of-recovery pricing viable?**

## The evidence: yes for services, never yet for software

| Precedent | Rate | Label |
|---|---|---|
| **ClearLane** (freight accessorial recovery) | **10–25% of recovered revenue** — *"If the audit finds nothing, you pay nothing"* | VERIFIED |
| **Recoupex** (cargo claims recovery) | **20–50% success fee**, deducted from compensation, no upfront | VERIFIED (published) |
| Freight collection law firms | **25–40% contingency**, scaling with debt age | CLAIMED |
| **Betachon** (freight audit recovery) | *"Our standard fee is **50% of the savings recovered**"* | CLAIMED (published) |
| Contingency freight audit norm | Provider keeps **25–50%** | CLAIMED |
| **AFS** ocean audit | Gainshare — *"if we don't find billing errors, you don't pay"* | CLAIMED |
| **Freehand.ai** | Performance-based, with a $500K-in-30-days-or-$10K-credit guarantee | CLAIMED |
| iNymbus | **$0.40–$0.70 per claim** (per-transaction, not contingency) | CLAIMED |
| **Loop** | **Explicitly refuses gain-share** — SaaS platform fee + volume | CLAIMED |

**Contingency is thoroughly normalised in freight recovery. Every instance above is a human service.** Across 30 vendors scored, `performance_pricing` is 2 only for the human freight-audit category. **No software product in this market is priced on recovery.**

That is both the opportunity and the warning: **it is unoccupied because software companies have found it hard to make work, not because nobody thought of it.**

## The counter-anchor that constrains everything

The freight market's mental model for a recovery-adjacent fee is **percent of invoice face value**, not percent of recovery:

- Factoring: **1.37%** (Triumph, SEC-filed) to 5% (OTR, CLAIMED)
- Freight audit processing: **~$1.92 per invoice** (derived from Cass FY2025: $66.13M ÷ 34.45M invoices)
- Broker TMS: Truckbase **$290/mo**; Rose Rocket **from $2,080/mo**; Tai $995–$7,925/mo; Turvo ~$5,000/mo

**A 20–30% contingency is an unfamiliar shape here.** Expect the first reaction to be sticker shock at the percentage, not arithmetic on the dollars. **The answer is always to quote the net: "you keep 75–80% of money you were going to write off entirely."**

## Recommended structure

### Phase 1 (customers 1–10): pure contingency, no floor

**25% of collected dollars. Zero upfront. Zero minimum. You are paid only when the customer is paid.**

Rationale:
- It removes the only objection that matters at this stage — *"prove it before I pay"*
- **It is the measurement instrument.** Every ROI model in this study rests on an **ASSUMED** 37.5%→60% collection uplift. Pure contingency forces you to discover the real number.
- It clears procurement entirely: a fee taken from recovered dollars often needs no budget line at all
- 25% sits mid-range of every precedent (10–50%) and well below Betachon's 50%

**Bill on *collected*, not *invoiced*.** Given ATRI's sub-50% payment rate, invoicing is not the product — **collection is.** Pricing on invoiced dollars prices you on the wrong event.

### Phase 2 (customers 11–40): floor plus contingency

**$1,500/month platform fee + 15% of collected.**

The floor is not for revenue — it is for **qualification.** Pure contingency attracts customers whose data is a mess and whose recovery is marginal, and each one costs a fixed amount of your attention. A modest floor filters them, and 15% keeps the alignment story intact.

### Phase 3 (scale): tiered SaaS with a recovery guarantee

**$2,500–$8,000/month by load volume, with a written guarantee: recover at least 3× the fee in year one or the next year is free.**

This is the transition every contingency business must eventually make — service margins do not compound, and a recovery percentage caps your revenue at a fraction of a pool that shrinks as you succeed. **The guarantee preserves the risk-reversal that made contingency work while converting to predictable, valuable recurring revenue.**

## Price points against the ROI models

| Segment | Recoverable | 25% price | Customer net | Verdict |
|---|---|---|---|---|
| 25-truck carrier | $39,375 | **$9,844** | $29,531 | **Below the cost of one sales touch.** Self-serve or embedded only |
| 150-truck carrier | $297,000 | **$74,250** (or $65,340 at 22%) | $222,750 | **Works.** And exceeds the carrier's entire operating profit at ATRI's sub-1% margins |
| $80M brokerage | $194,535 | **$48,634** | $145,901 | **Works.** Equivalent to winning ~$1.3M of new freight at 15% margin |
| $200M brokerage | ~$486,000 (scaled) | **~$121,500** | ~$364,500 | **Works well.** Approaching the ceiling of CFO discretionary authority |

**The floor is hard: below ~50 trucks, contingency pricing does not clear the cost of acquiring the customer.** Only ~61,777 US carriers have 11+ trucks; 710,386 have ten or fewer. **That is the binding TAM constraint, and no pricing structure fixes it — only self-serve or embedded distribution does.**

## Three pricing risks worth naming

1. **The floor is anchored at $12.99.** A $299 Google Sheet, a $12.99/mo iOS app and a $49/mo mobile product all attack this job. Anyone selling to owner-operators competes against those anchors. **Do not sell there.**
2. **Contingency invites licensing scrutiny.** *"We recover your money for a percentage"* is precisely the fact pattern in WA RCW 19.16.100 (*"any obligation for the payment of money… arising out of any agreement or contract"* — not consumer-limited), NC G.S. §58-70-15 and Minn. Stat. §332.31. Freight is commercial, so **there is no FDCPA safe harbour to fall back on.** Structure the fee as **invoice preparation on original billing**, not collection of delinquent debt — and get an opinion rather than an assumption.
3. **Success shrinks your own pool.** Every recovered dollar teaches the customer to bill better, and every facility that adopts a YMS reduces detention 40–80%. **A contingency business on a shrinking base needs the Phase 3 conversion planned from day one, not improvised in year three.**

## The pricing sentence

> **"You pay us 25% of what we collect. If we collect nothing, you pay nothing. Last quarter we found $312,000 you had already paid your carriers and never billed your customers — with 41 days left to bill it."**

Every clause does work: the percentage is the ask, the guarantee removes risk, the dollar figure makes it concrete, and **the deadline is what actually forces the meeting.**
