# Agent 14 — Economics: hard numbers and ROI models

**Research date:** 2026-08-19

## Three corrections to the brief
1. **The DOT OIG report ID in the brief is wrong.** It is **ST2018019** (2018-01-31), not ST-2018-002. Verified by extracting text from the actual 76-page PDF.
2. **The OIG report is old data.** Its $1.1–1.3B figure rests on **2013** dwell data. The current authority is **ATRI's Sept 2024 study** (2023 data), which found detention nearly **twice as frequent** (39.3% vs 21% of stops).
3. **The strongest number for the thesis is the DERIVED $91–94 of lost revenue per detention hour** (two independent ATRI endpoints converge), against a typical detention fee of only ~$50/hr. **Carriers are underwater on detention even when they collect in full.**

## Detention frequency & duration

| Metric | Value | Year | Source |
|---|---|---|---|
| Stops with detention (>2 hrs), all sectors | **39.3%** | 2023 | ATRI 2024 |
| Refrigerated | **56.2%** | 2023 | ATRI 2024 |
| Dry van | ~1/3 of stops | 2023 | ATRI 2024 via Land Line |
| Flatbed | ~1/4 of stops | 2023 | ATRI 2024 via Land Line |
| Specialised | ~1 in 5 stops | 2023 | ATRI 2024 via Land Line |
| Spot-market fleets | **42.5%** | 2023 | ATRI 2024 |
| Women drivers | **49.1%** | 2023 | ATRI 2024 |
| Detention hrs per driver per year | **117–209 hrs** (by sector) | 2023 | ATRI 2024 |
| Total for-hire detention hours | **>135 million hrs** | 2023 | ATRI 2024 |
| Stops exceeding 2 hrs (earlier estimate) | **21%** | 2013 | DOT OIG ST2018019, Exh. C |
| Stops ≤1 hour | 46% | 2013 | OIG ST2018019 |
| Average dwell time | **113 minutes** | 2013 | OIG ST2018019, Fig. 1 |
| Waits of 2–4 hrs | 14% → **5%** | 2014→2023 | ATRI via Land Line |
| Waits >4 hrs | 8% → **5%** | 2014→2023 | ATRI via Land Line |

**Note the discontinuity:** OIG found 21% of stops >2 hrs (2013); ATRI found 39.3% (2023). Different samples and methods — **not a clean time series.** ATRI's own trend data shows long waits *shrinking* while total detention incidence rose: more stops tip past 2 hours, but the tail got shorter.

**DOT OIG ST2018019 findings:**
- Detention reduces driver earnings **$1.1B–$1.3B/yr** = **$1,281–$1,534 per driver per year**
- Reduces motor carrier net income **$250.6M–$302.9M/yr**
- A 15-minute increase in average dwell raises expected crash rate **6.2%**
- Mileage loss from detention: **2.5%–5.2%** of annual miles by haul-length segment
- **OIG's core finding: *"Accurate industrywide data on driver detention do not currently exist."***

**ATRI 2024 financial impact (2023 data):** $3.6B direct + $11.5B lost productivity = **$15.1B**; **$11,000–$19,000 lost revenue per driver/yr**; ~7,000 lost miles/driver; 15 days of HOS time.

**DERIVED — value of one detention hour:** $11,000 ÷ 117 hrs = **$94.02/hr**; $19,000 ÷ 209 hrs = **$90.91/hr**. Both endpoints converge on **~$91–94 of lost revenue per detention hour** — roughly **double** the typical detention fee charged.

## Accessorial rate norms

| Charge | Typical amount | Source | Status |
|---|---|---|---|
| Free time before detention | **2 hours** at each facility | Truckstop; OIG; FreightWaves | CITED |
| Detention $/hr | **$50–$85/hr** | Truckstop 2025 | CITED |
| Detention $/hr | **$30–$75/hr**, ½-hr or hourly increments | FreightWaves 2025-05-22 | CITED |
| Detention, average fee charged | **~$50/hr** | ATRI 2024 via Land Line | CITED |
| Detention, average fee charged | **$63.71/hr** (vs $66.65/hr operating cost) | ATRI 2019 via Land Line | CITED |
| Typical detention invoice | **~$100** per occurrence | Truckstop; ATRI 2024 | CITED |
| TONU | **$150–$300** | Truckstop | CITED |
| Layover | **$200–$500/day**; "$150/day common" as a cap | Truckstop; FreightWaves | CITED |
| Lumper | **$25–$458, median ~$146** | Truckstop | CITED |
| Stop-off | $75–$150/stop | Truckstop | CITED |
| Redelivery | ~$400/occurrence | Truckstop | CITED |
| **Claim submission window** | **24–48 hours** | FreightWaves | CITED |

Documentation norms (FreightWaves): GPS timestamps, in/out times on the BOL, shipper signature, ELD logs, broker-specific detention request forms. **This is the operational crux — the money is lost on evidence and deadlines, not on rate schedules.**

## Unbilled / uncollected evidence — and its weakness

**This is the load-bearing number for the thesis, and the evidence is thin but real.**

| Metric | Value | Year | Source |
|---|---|---|---|
| Fleets that charge detention fees | **94.5%** | 2023 | ATRI 2024 |
| Detention incidents actually billed | **~75%** | 2023 | ATRI 2024 via Land Line |
| Invoiced detention hours actually compensated | **fewer than 50%** | 2023 | ATRI 2024 |
| Fees actually paid | "only a little over half" | 2023 | ATRI 2024 via Land Line |
| Carriers who don't charge detention to stay competitive | **20%** | 2018 | ATRI 2019 |

**DERIVED end-to-end collection rate: 0.75 × 0.50 = 37.5% of economically eligible detention value is actually collected. Roughly 62.5% leaks — ~25% never billed, ~37.5% billed but unpaid.**

### WEAKNESSES — stated explicitly
1. **Self-selected survey.** ATRI's figures come from voluntary driver/carrier surveys distributed through trade channels. Respondents with a detention grievance are more likely to respond, biasing frequency and non-payment **upward**.
2. **Self-reported, not audited.** Nobody reconciled claimed detention against actual A/R ledgers or settlement data. No third-party verification of "fewer than 50%".
3. **The 75%/50% figures reach us through secondary reporting** (Land Line, DAT) of a lead-gated ATRI PDF. Exact definitions — per incident vs per hour vs per dollar — are ambiguous, **and the two figures may not be legitimately multiplicable.** Treat 37.5% as order-of-magnitude only.
4. **DOT OIG explicitly declined to model this**, stating it "did not account for an operator to potentially receive detention fees to offset lost wages or revenue."

**NO RIGOROUS DATA FOUND** for: claim *approval* rates by broker; dispute/chargeback rates; days-to-pay on accessorials; drayage-specific detention frequency (absent from ATRI's segmentation); any audited study of detention A/R. **No FMCSA data collection was ever implemented** — OIG's 2018 recommendation produced no public dataset in the eight years since.

## Back-office labour costs

| Metric | Value | Year | Source |
|---|---|---|---|
| Billing & Posting Clerks (SOC 43-3011), median annual | **$47,170** | May 2024 | BLS OOH |
| Employment, Billing & Posting Clerks | 429,800 | 2024 | BLS |
| Financial Clerks, median | $48,650 / **$23.39/hr** | May 2024 | BLS |
| Bookkeeping/Accounting/Auditing Clerks (43-3031) | $49,210 / **$23.66/hr** | May 2024 | BLS OOH |
| Cass freight invoices processed | **34.45 million** | 2025 | Cass 10-K |
| Cass processing fee revenue | $66.13M | 2025 | Cass 10-K |

**DERIVED loaded clerk cost:** $47,170 × 1.30 (benefits multiplier — **ASSUMED**) = **$61,321/yr ≈ $29.48/hr**.

**DERIVED cost per invoice:** $66.13M ÷ 34.45M = **$1.92 per invoice** — an upper bound (Cass fees include its facility segment). **The single best real-world anchor for what freight invoice processing is worth: roughly $1–2 per invoice.**

**NO RIGOROUS DATA FOUND** for loads processed per clerk per day in trucking. Any such figure would be fabricated.

## Market structure & TAM inputs

FMCSA MCMIS census, snapshot 2023-12-29 (Pocket Guide 2024, RRC-24-002):

| Fleet size | Carriers | Share |
|---|---|---|
| 1 power unit | **418,526** | 53.2% |
| 2 power units | **123,353** | 15.7% |
| 3–10 | **168,507** | 21.4% |
| 11–100 | **56,715** | 7.2% |
| >100 | **5,062** | 0.64% |
| No PU/unreported | 15,026 | 1.9% |
| **Total active carriers** | **787,189** | 100% |

- Power units **5,421,013**; total drivers **5,790,793** (2023)
- **Property brokers registered: 28,351** (2023); household goods brokers 1,078
- ATA: ~580,000 active carriers (June 2025); **91.5% operate ≤10 trucks**; **99.3% operate ≤100 trucks**; **$906B gross freight revenue (2024)**; 11.27B tons; 3.58M drivers
- Average transportation invoice: **$1,717** (Triumph Financial FY2025 10-K)

**TAM read: only ~61,777 carriers have 11+ trucks — the entire population capable of supporting a seat-based or per-truck SaaS sale. Everything below is a 1–10 truck long tail of 710,386 carriers reachable only by self-serve or embedded distribution.**

## Software & contingency pricing anchors

| Anchor | Price | Source |
|---|---|---|
| Truckbase TMS, minimum | **$290/month** (billed annually) | truckbase.com/pricing |
| Rose Rocket, Full Service Platform | **from $2,080/month**, unlimited users | roserocket.com/pricing |
| Freight audit processing | **~$1.92/invoice** (DERIVED, Cass FY2025) | Cass 10-K |
| Factoring yield on avg net funds employed | **14.87%** (2025), 16.72% (2024), 16.46% (2023) | Triumph 10-K |

**NO RIGOROUS DATA FOUND** — could not verify with a citable primary source: freight-audit contingency percentages, freight claims-recovery contingency rates, or commercial collections agency contingency percentages. The commonly repeated "15–35%" for commercial collections is **UNVERIFIED here**. **Do not put a collections percentage in an investor deck on this authority.** (Note: agents 06 and 09 independently sourced contingency anchors — Betachon 50% of savings, Recoupex 20–50% success fee, freight collection law firms 25–40%, AFS gainshare, ClearLane 10–25% of recovery. Use those, with their own labels.)

## ROI Model A — 25-truck dry van carrier

| Line | Value | Status |
|---|---|---|
| Trucks | 25 | GIVEN |
| Annual miles/truck | 100,000 | ASSUMED |
| Avg length of haul | 500 mi | ASSUMED |
| Loads/yr = 25 × (100,000÷500) | **5,000** | DERIVED |
| Stops/yr = loads × 2 | **10,000** | DERIVED |
| Dry van detention rate | 33% | CITED (ATRI 2024) |
| Detained stops/yr | **3,300** | DERIVED |
| Billable hrs/detained stop | 1.06 | DERIVED |
| Billable detention hrs/yr | **3,500** | CITED-anchored |
| Detention rate | $50/hr | CITED |
| **Gross eligible detention value** | **$175,000** | DERIVED |
| Currently collected @ 37.5% | $65,625 | DERIVED |
| Post-product collection @ 60% | $105,000 | **ASSUMED uplift** |
| **Incremental recovery** | **$39,375/yr** | DERIVED |
| Product price @ 25% of recovery | **$9,844/yr** ($820/mo, $32.81/truck/mo) | ASSUMED |
| **Carrier net gain** | **$29,531/yr** | DERIVED |
| Payback | Immediate — contingency self-funds from month 1 | DERIVED |

*Billable hrs reconciliation:* ATRI 117–209 hrs/driver/yr; dry van sits low-mid. 25 × 140 = 3,500 hrs. 3,500 ÷ 3,300 detained stops = **1.06 hrs each** — consistent with ATRI's finding that 2–4 hr waits (0–2 hrs billable) dominate.

## ROI Model B — 150-truck regional carrier

| Line | Value | Status |
|---|---|---|
| Trucks | 150 | GIVEN |
| Detention hrs/truck/yr (regional = more stops) | 160 | ASSUMED (within ATRI 117–209) |
| Billable detention hrs/yr | **24,000** | DERIVED |
| Detention rate | $55/hr | CITED (midpoint) |
| **Gross eligible detention value** | **$1,320,000** | DERIVED |
| Currently collected @ 37.5% | $495,000 | DERIVED |
| Post-product @ 60% | $792,000 | ASSUMED |
| **Incremental recovery** | **$297,000/yr** | DERIVED |
| Price @ 22% of recovery | **$65,340/yr** ($5,445/mo, $36.30/truck/mo) | ASSUMED |
| **Carrier net gain** | **$231,660/yr** | DERIVED |
| Payback | Immediate under contingency; ~2.6 months as flat SaaS | DERIVED |

**Context that makes this the sharpest argument in the thesis:** ATRI's 2026 cost report puts truckload/reefer operating margins **below 1.0%** and flatbed at **−0.5%**. On ~$30M of revenue for 150 trucks, **$231,660 of near-pure-margin recovery is larger than the carrier's entire operating profit at a 0.8% margin.**

## ROI Model C — $80M/yr freight brokerage

| Line | Value | Status |
|---|---|---|
| Gross revenue | $80,000,000 | GIVEN |
| Revenue per load | $2,000 | ASSUMED (vs $1,717 carrier-side invoice, CITED) |
| Loads/yr | **40,000** | DERIVED |
| Stops/yr | **80,000** | DERIVED |
| Detention rate, all sectors | 39.3% | CITED (ATRI 2024) |
| Detained stops | **31,440** | DERIVED |
| Share where broker bears/passes detention | 50% → 15,720 stops | ASSUMED |
| Billable hrs @ 1.1 hr/stop | **17,292** | DERIVED |
| Rate $50/hr → **gross eligible** | **$864,600** | DERIVED |
| Currently recovered @ 37.5% | $324,225 | DERIVED |
| Post-product @ 60% | $518,760 | ASSUMED |
| **Incremental recovery** | **$194,535/yr** | DERIVED |
| Price @ 25% | **$48,634/yr** | ASSUMED |
| **Broker net gain** | **$145,901/yr** | DERIVED |

At a ~15% brokerage gross margin, $194,535 of recovered accessorial is equivalent to winning **~$1.3M of new freight** — a far cheaper path to the same margin.

## Hard economic warning from these models

**At 20–30% of recovery, ROI A yields only ~$9,800 ACV.** That will not support a sales-led motion (below the cost of a single AE touch), and it is only ~2.8× a Truckbase TMS seat. **The 25-truck tier must be self-serve or embedded in an existing TMS/factoring relationship.**

**Only the 150-truck tier (~$65K ACV) and the brokerage tier (~$49K ACV) support direct sales — and there are only ~61,777 carriers with 11+ trucks plus 28,351 brokers in that reachable universe.**

## Data gaps and what could not be verified
- **NO RIGOROUS DATA FOUND:** audited detention claim submission/approval/payment rates. **The entire "62.5% leaks" thesis rests on one self-selected ATRI survey reaching us through secondary reporting.**
- **NO RIGOROUS DATA FOUND:** drayage detention frequency; loads per billing clerk per day; commercial collections/freight-audit/claims-recovery contingency percentages (from this agent — see note above).
- **Could not open** the primary ATRI PDFs (2024 detention study; 2026 Operational Costs) — both lead-gated. All ATRI figures are from ATRI's press release plus Land Line/DAT/Fleet Owner reporting.
- **ATRI operating cost per hour for 2025 is unverified.** The $90.89/hr figure surfaced only in a search snippet; excluded. Used the DERIVED $91–94/detention-hour instead.
- **BLS OEWS detailed tables (SOC 43-3011 by NAICS 484) were 403-blocked**; used BLS OOH national medians, which are not trucking-specific.
- **FMCSA never implemented** the detention data collection OIG recommended in 2018. Eight years on there is still no authoritative federal detention dataset — **simultaneously the biggest risk to this thesis and the reason no incumbent has priced the problem.**
- **The 37.5% → 60% collection uplift is ASSUMED throughout. It is the single most important unvalidated variable; every ROI figure scales linearly with it. At a 45% post-product rate, ROI A's incremental recovery falls to $13,125/yr and the 25-truck tier becomes uninvestable.**

## Sources
1. DOT OIG **ST2018019** (2018-01-31) — oig.dot.gov/library-item/36237 · oig.dot.gov/sites/default/files/FMCSA%20Driver%20Detention%20Final%20Report.pdf
2. ATRI, *Costs and Consequences of Truck Driver Detention*, Sept 2024 — truckingresearch.org/2024/09/costs-and-consequences-of-truck-driver-detention-a-comprehensive-analysis/
3. ATRI press release 2024-09-10 — truckingresearch.org/2024/09/new-research-documents-substantial-financial-and-safety-impacts-from-truck-driver-detention/
4. Land Line 2024-11-01 — landline.media/magazine/detention-time-new-study-outlines-true-costs-consequences/
5. Land Line 2024-09-13 — landline.media/study-shines-a-spotlight-on-costly-cascading-effects-of-detention-time/
6. Land Line (ATRI 2019) — landline.media/detention-issue-getting-worse-atri-study-finds/
7. ATRI *Operational Costs of Trucking: 2026 Update* — truckingresearch.org/2026/07/new-atri-report-details-accelerating-costs-and-low-profitability-despite-cuts/
8. HDT — truckinginfo.com/news/trucking-fleets-faced-record-operating-costs-during-third-year-of-freight-recession
9. Truckstop — truckstop.com/blog/accessorial-charges/
10. FreightWaves 2025-05-22 — freightwaves.com/news/understanding-detention-pay-clauses
11. FreightWaves 2025-05-15 — freightwaves.com/news/how-to-read-your-rate-con-like-a-pro
12. DAT — dat.com/blog/trucker-detention-is-still-a-15-billion-problem
13. FMCSA *Pocket Guide 2024* (RRC-24-002) — fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/FMCSA%20Pocket%20Guide%202024-v6%20508%20.pdf
14. ATA — trucking.org/economics-and-industry-data
15. BLS OOH Financial Clerks — bls.gov/ooh/office-and-administrative-support/financial-clerks.htm
16. BLS OOH Bookkeeping Clerks — bls.gov/ooh/office-and-administrative-support/bookkeeping-accounting-and-auditing-clerks.htm
17. Triumph Financial 10-K FY2025 — sec.gov/Archives/edgar/data/1539638/000153963826000007/tfin-20251231.htm
18. Cass Information Systems 10-K FY2025 — sec.gov/Archives/edgar/data/708781/000070878126000010/cass-20251231.htm
19. truckbase.com/pricing · 20. roserocket.com/pricing · 21. fleetowner.com/operations/article/55392569/...
