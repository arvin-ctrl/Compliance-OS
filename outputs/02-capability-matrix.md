# 2. Capability Matrix

**Scale:** 0 = absent · 1 = partial (manual, services-heavy, or reporting-only) · 2 = strong (native, automated, productised). Dimension definitions and the test for each score are in [`data/capability-dimensions.md`](../data/capability-dimensions.md). Machine-readable version: [`data/capability-matrix.csv`](../data/capability-matrix.csv).

**Provenance note.** Scores were assigned by the lane agent that researched each vendor, against a shared rubric. Totals are computed from those scores. Two agents independently scored Denim and reached **19** (as a factoring product) and **27** (as a post-acquisition broker back-office product) — the divergence is real and instructive: **capability depends on which job you score against, and this whole matrix should be read as directional, not precise.**

## Master matrix

Abbreviations: rate_con = rate confirmation ingestion · rules = rate-rule extraction · gps = GPS/ELD timestamps · appt = appointment ingestion · pod = POD/BOL ingestion · det = detention · acc_det = accessorial detection (**biller direction**) · evid = evidence package · inv = invoice creation · claim = claim submission · coll = collection tracking · disp = dispute workflow · tms = TMS integration · eld = ELD integration · email = email/SMS ingestion · acct = accounting integration · rev_an = recovered-revenue analytics · perf = performance pricing · cust = customer-specific rules · multi = multi-party support

| Vendor | rate_con | rules | gps | appt | pod | det | tonu | layover | lumper | demur | **acc_det** | **evid** | inv | claim | **coll** | disp | portal | tms | eld | email | acct | rev_an | **perf** | cust | multi | **Total** |
|---|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| **3PL claims desk (human)** | 2|1|1|2|2|2|2|2|2|1|1|2|2|2|2|2|1|2|1|2|2|1|0|2|2| **41** |
| **Trimble** | 2|2|2|1|1|2|1|1|1|2|1|1|2|0|1|1|1|2|2|2|2|1|0|2|2| **37** |
| **McLeod PowerBroker** | 2|2|2|2|2|1|1|1|1|1|1|1|2|1|2|1|2|2|2|1|2|0|0|2|2| **36** |
| **McLeod LoadMaster** | 1|0|2|1|2|2|1|1|1|0|1|2|2|0|2|1|2|2|2|2|2|1|0|2|2| **34** |
| **FAP category (Cass/AFS/Trax/nVision)** | 2|2|0|0|2|1|0|0|1|2|2|1|0|2|1|2|2|2|0|1|2|2|2|2|2| **33** |
| **FourKites** | 1|2|2|2|2|1|0|0|0|2|1|1|0|0|0|1|2|2|2|2|1|1|0|2|2| **30** |
| **Transporeon** | 1|0|2|2|2|1|0|0|0|1|0|1|2|2|1|2|2|2|2|1|2|0|0|2|2| **30** |
| **Loop** | 1|2|0|0|2|1|0|0|2|1|2|2|0|1|0|2|2|2|0|1|2|2|0|2|2| **29** |
| **Turvo** | 1|1|2|1|2|1|1|1|1|0|0|1|2|0|1|1|2|2|2|1|2|0|0|1|2| **28** |
| **Intelligent Audit** | 2|2|0|0|1|1|0|0|0|1|2|1|0|2|1|2|2|2|0|1|1|2|1|2|2| **28** |
| **Infios (ex-MercuryGate)** | 0|0|1|1|1|0|0|0|0|0|1|1|2|2|2|2|2|2|1|0|2|1|0|2|2| **27** |
| **Oracle OTM** | 2|1|0|1|2|1|0|1|1|1|1|0|2|1|1|1|2|2|0|0|2|1|0|2|2| **27** |
| **Denim / Truckstop** (broker lens) | 2|1|0|0|2|1|1|1|1|0|1|1|2|0|2|1|2|2|0|1|2|0|1|1|2| **27** |
| **TriumphPay** | 2|2|0|0|2|1|0|0|1|0|**0**|1|1|1|2|2|2|2|0|1|1|1|0|2|2| **26** |
| **Descartes** | 1|0|2|2|2|1|0|0|0|1|1|1|2|0|1|1|2|2|2|1|1|0|0|1|2| **26** |
| **project44** | 1|1|2|2|0|1|0|0|0|2|1|1|0|0|0|1|2|2|2|1|1|1|0|2|2| **25** |
| **Generic carrier TMS** | 1|0|1|1|1|1|1|1|1|0|1|1|2|0|1|0|1|2|1|1|2|1|0|1|1| **23** |
| **Blue Yonder TMS** | 2|1|0|1|1|1|0|0|0|0|2|0|1|0|0|1|1|2|0|0|2|1|0|2|2| **21** |
| **OTR Solutions** | 2|0|0|0|2|1|0|0|1|0|**0**|1|2|1|2|1|2|1|0|1|1|1|0|0|1| **20** |
| **myEZClaim (Infios)** | 0|0|0|0|1|0|0|0|0|0|0|2|2|1|2|2|1|2|0|0|1|2|0|1|2| **19** |
| **Broker's Excel + AR clerk** | 1|1|0|0|1|1|1|1|1|1|1|1|1|1|1|1|0|1|0|1|1|0|0|1|1| **19** |
| **Drumkit** | 2|**0**|1|2|1|0|0|0|0|0|0|0|0|0|0|0|2|2|1|2|0|0|0|1|2| **16** |
| **Motive** | 0|0|2|2|1|1|0|0|0|0|0|1|0|0|0|0|1|2|2|0|0|0|0|0|1| **15** |
| **Vooma** | 2|**0**|1|2|0|0|0|0|0|0|0|0|0|0|0|0|2|2|1|2|0|0|0|1|2| **15** |
| **Terminal49** | 0|0|0|1|1|0|0|0|0|2|1|1|0|0|0|0|2|2|0|1|0|0|0|1|2| **14** |
| **Opendock** | 0|0|0|2|1|1|0|0|0|0|0|1|0|0|0|0|2|1|0|1|0|1|0|1|2| **13** |
| **Expedock** | 1|0|0|0|2|0|0|0|0|0|0|0|1|0|0|0|1|2|0|2|1|0|0|1|1| **12** |
| **Loadsure** | 1|0|0|0|1|0|0|0|0|0|0|1|0|1|0|1|2|2|0|0|0|0|0|1|2| **12** |
| **Samsara** | 0|0|2|1|1|1|0|0|0|0|0|1|0|0|0|0|1|2|2|0|0|0|0|0|0| **11** |
| **Container xChange** | 0|0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|2|0|0|0|0|0|0|0|1| **4** |

## What the matrix actually says

### 1. The highest score belongs to a human

A 3PL's internal claims desk scores **41/50** — higher than any software product in the study. A person can do everything; what they cannot do is scale. **The competitor is an underwater clerk, not a product.** That reframes the sale: you are not displacing software, you are giving throughput to someone drowning.

### 2. Four columns are near-universally zero

| Column | Vendors scoring 2 | Reading |
|---|---|---|
| **`acc_det`** (biller direction) | **Zero.** FAP/Loop/Blue Yonder/IA score 2 in the **payer** direction — the mirror image | Nobody detects a charge the carrier *failed* to bill |
| **`evid`** as a deliverable | Loop (2), myEZClaim (2), McLeod (2), 3PL desk (2) — and all four mean *document checklist*, not assembled argument | No one builds a timestamp + clause + correspondence rebuttal packet |
| **`coll`** by accessorial type | Several score 2 for generic AR aging | **Nobody can answer "what % of billed detention did we collect from Customer X, and why did we lose?"** |
| **`perf`** (contingency pricing) | **FAP category only (2)** — and that is human contingency audit, not software | **No software product in this market is priced on recovery** |

### 3. The two halves of the problem are owned by different, opposed parties

| Holds the **entitlement data** (timestamps, appointments) | Holds the **money data** (rate con, invoice, POD, AR) |
|---|---|
| Samsara, Motive, project44, FourKites, Descartes, Transporeon, Opendock, Trimble | TriumphPay, Cass, Loop, OTR, McLeod, Turvo, Denim |
| Paid by shippers/brokers, or bound by ToS that forbids third-party transfer | Paid by carriers/brokers, but **0 on `gps` and `eld` almost without exception** |

**Trimble is the only vendor that genuinely holds both** — which is why it scores highest among software (37) and why it is the most serious incumbent threat. **And even Trimble scores 0 on `claim`, `perf`, and 1 on `coll` and `evid`.**

### 4. `rules` is the sharpest single differentiator

Scoring 2 on `rate_rule_extraction`: **Trimble, McLeod PowerBroker, FAP category, Loop, FourKites, Intelligent Audit, TriumphPay.** Every one of them either points the rules at the *payer's* side (FAP, Loop, IA, TriumphPay, FourKites) or requires **manual per-customer configuration** that decays (Trimble, McLeod).

**Nobody parses a per-load rate confirmation for that shipper's actual free time, grace, rounding, cap and notice window and computes entitlement per load.** Vooma and Drumkit — the two best-funded rate-con ingestion products — score **0** here. They extract fields; they do not extract rules.

### 5. Score inflation warning

A score of 2 on `detention` means "auto-detects and calculates". **Trimble and McLeod both earn it.** That is the single most important defensive fact in this document: **for a carrier already running TMW.Suite or LoadMaster with the mobile-comms and detention modules licensed, the core detection pitch is largely answered.**

The gap that survives is not detection. It is **rule ingestion, evidence assembly, submission inside the contractual window, dispute rebuttal, and collection accounting** — the columns where those same incumbents score 0 and 1.
