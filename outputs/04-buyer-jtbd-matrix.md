# 4. Buyer / Jobs-To-Be-Done Matrix

Answers research question 2: **which buyer feels this most?**

## The matrix

| | **Owner-op / 1–10 trucks** | **Carrier 11–100** | **Carrier 100+** | **Broker / 3PL $50–500M** | **Enterprise shipper** | **NVOCC / forwarder** |
|---|---|---|---|---|---|---|
| **Population (US)** | 710,386 | 56,715 | 5,062 | 28,351 brokers | ~few thousand | UNKNOWN |
| **Functional job** | "Get paid for the 4 hours I sat at that dock" | "Stop writing off detention we earned" | "Collect what we already billed" | "Stop absorbing accessorials I paid my carrier" | "Don't overpay accessorials" | "Don't eat D&D I was wrongly billed" |
| **Emotional job** | Fairness. Anger. | Not looking incompetent to the owner | Board-level margin defence | Explaining a margin miss to the CFO | Hitting a cost-reduction target | Not being the middle of a cascading clock |
| **Social job** | Respect from brokers | "We run a tight shop" | Benchmark against peers | Carrier-of-choice without giving margin away | Shipper-of-choice | Compliance-clean |
| **Who has budget** | The owner (is the driver) | Owner / Controller | VP Finance, CFO | **CFO / Controller / VP Finance** | Transportation procurement (rules) + AP (money) | Ops director |
| **Feels the pain** | The driver | The billing clerk | AR department | Account managers, silently | Nobody acutely | Ops, acutely |
| **Pain–budget alignment** | Perfect (same person) | Good | Moderate | **Good** | **Broken** — the person who feels it has no budget | **Good** |
| **ACV at 20–30% of recovery** | <$1K | **$9.8K (25tr) → $65K (150tr)** | $100K+ | **~$49K at $80M revenue** | n/a (savings, not recovery) | UNKNOWN, likely $10–50K |
| **Sales cycle** | Self-serve, minutes | Days–weeks | 3–6 months | **2–8 weeks** | **9–15 months + SOC 2 Type II** | Weeks |
| **Can a solo founder reach them?** | Only self-serve | **Yes** | Barely | **Yes** | **No** | **Yes** |
| **Substitute quality** | Nearly free, bad | **One overloaded clerk** | Real TMS module | TMS + Excel + absorption-by-policy | Excellent (for their goal) | **Nearly nothing** |
| **Structural blocker** | ACV below cost of sale | Factoring may own the claim | Already bought detection | **No published leakage magnitude** | Wrong side of the value transfer | Defect density unknown |

## Buyer-by-buyer verdict

### Owner-operator / 1–10 trucks — **NO**
Pain is highest and most emotional; **90.3% of all US carriers.** But ROI Model A caps ACV at ~$9,800 for a *25*-truck fleet — a 5-truck fleet is under $2,000. The floor is anchored by a $12.99/mo iOS app and a $299 Google Sheet. **Reachable only through the factor or the ELD, as an embedded feature, not a company.**

### Carrier 11–100 trucks — **YES, primary**
**The strongest economic argument in the study.** ROI Model B: $297,000 incremental recovery, $65,340 price, $231,660 net gain — against ATRI's finding that **truckload operating margins are below 1.0%**. The recovery is larger than the whole operating profit.

The buyer is the owner or controller, reachable by one person, and the substitute is a single clerk who is already failing silently.

**But three blockers are real:** the entitlement may have been extinguished at the dock (see wedge analysis); a factored carrier may not own the supplemental claim (UCC §9-406); and the 37.5%→60% collection uplift underlying every ROI figure is **ASSUMED, not measured.**

### Carrier 100+ trucks — **NO as a beachhead**
Has McLeod or Trimble with a working detention module. Selling detection is selling a feature they own. **A year-2 upsell on evidence packaging and short-pay recovery, not a first customer.**

### Broker / 3PL $50–500M — **YES, strongest deal size**
1 point of gross margin = $500K–$10M; recovered dollars carry no cost of sale; the CFO can approve $30–150K without a board. **The pain is live and public** — RXO 13.3%→11.4%, CHRW cutting headcount 7.1%, **Hub Group's Item 4.02 non-reliance restating two years.**

Buy the objection list from the research verbatim: *"my customer won't pay a 90-day-old rebill"* (so run weekly), *"I chose not to bill that"* (so support absorb-by-policy), *"my TMS already does this"* (it doesn't, but it sounds like it), *"I'm not giving you my rate data"*, *"prove it first"* (free retro run).

**The disqualifying unknown: nobody has published a magnitude for broker paid-but-not-billed leakage. If it is 0.05% of revenue rather than 0.5%, only the $500M+ tier works — ~200 companies, not a venture market.**

### Enterprise shipper — **NO. Year-3 at the earliest**
Four independent disqualifiers, each sufficient: wrong side of the value transfer (a neutral evidence standard is a *transfer* from shipper to carrier); the evidence sits behind the buyer's own firewall; **9–15 months and SOC 2 Type II before first dollar**; and Oracle/Blue Yonder score 0 on `gps_eld_timestamps` and `evidence_package` because **timestamp-level adjudication is a demand gap, not a supply gap.**

### NVOCC / freight forwarder (ocean D&D) — **YES, and structurally the cleanest**
46 CFR §541.7(b)–(c) makes them **simultaneously billed party and billing party** with a cascading 30-day clock. They are directly liable (Peloton v. Flexport, Giti Tire v. Flexport). Their own invoices to customers must independently satisfy §541.6. **They have compliance budget *and* recovery upside.**

And the buying case is a federal rule, not a pitch: **§541.5 — "Failure to include any of the required minimum information… eliminates any obligation of the billed party to pay the applicable charge."**

## The JTBD reframe that changes everything

The brief's hypothesis assumes the job is **"recover money I failed to bill."**

The contract evidence says the real job is **"don't lose the entitlement in the first place."**

Verified across four real broker agreements:

| Broker | The condition that kills the claim |
|---|---|
| Arrive Logistics | Notify **30 minutes *before*** detention starts; signed BOL with **in and out** times within 48 hrs; else **50% reduction at Arrive's sole discretion** |
| Dray Alliance | **60 minutes** before detention accrues; **and** accessorial pay-if-paid |
| TQL | **1 GPS ping per 15 minutes** or *"no detention or layover"*; docs within 3 days |
| Flock Freight | POD within 24 hrs, 90-day outer limit — *"Carrier hereby forfeits and waives any right to payment"* |

**A product that discovers unbilled detention six weeks later is not recovering a live claim. It is asking for a discretionary gratuity from the party that wrote the forfeiture clause.**

That single finding relegates post-hoc recovery to a secondary motion and promotes a different job to primary:

> **"Fire the notice before free time expires, force the in/out signature onto the BOL, and keep the tracking alive — so the claim is still alive when I bill it."**

**Same data, same buyer, same dollars — but it is a real-time workflow product, not a recovery product.** Every wedge in the next document is scored against that reframe.
