# SCOUT 04 — REGULATORY CLOCK

**Surface:** new rules with a compliance date between Aug 2026 and late 2028 where the obligation is documentary/data-based, the population is enumerable, and the buyer is small enough to self-serve.
**Date of research:** 27 Aug 2026
**Returned:** 8 candidates · 11 explicit kills · 1 dry-surface report (e-invoicing)

---

## HEADLINE FINDING

The best regulatory-clock plays are not the famous ones. CSRD, EUDR, PPWR, the AI Act and e-invoicing all have enormous populations and enormous deadlines — and every one of them is either (a) already saturated by incumbents giving the artifact away, or (b) gated behind a state accreditation we cannot obtain.

The plays that survive all five gates share one specific property: **the regulator publishes the list of who must comply.** A downloadable public register of named obligated entities *is* the cold-start distribution channel. It converts Gate 1 from a marketing problem into a data problem, which is the one kind of problem this operator is unusually good at.

Three of the eight candidates below are register-backed (CA data brokers, SEC RIAs, EU financial entities). Those are the ones I would actually spend a month on. The rest are graded honestly and several are thin.

---

## VERDICT TABLE

| # | Candidate | Compliance date | Population | Register public? | Evidence | Conf. |
|---|---|---|---|---|---|---|
| 1 | **DROP 45-day deletion pipeline** (CA Delete Act) | **LIVE 1 Aug 2026** | 581 named data brokers | ✅ CSV | T1+T2 | **8** |
| 2 | **Reg S-P evidence pack for small RIAs** | 3 Jun 2026 (passed; exam cycle now) | ~16,544 SEC RIAs | ✅ CSV | **T1** | **7** |
| 3 | **DORA Register of Information filer** | ~Mar–Apr 2027 annual | EU financial entities incl. tiny PIs/EMIs | ✅ (EBA/national) | T2 | **6** |
| 4 | **CCPA risk assessment + ADMT notice pack** | 1 Jan 2027 / 1 Apr 2028 | CCPA-threshold businesses | Partial | T2 | **5** |
| 5 | **CRA Art. 14 reporting + tech-doc pack** | **11 Sep 2026** / 11 Dec 2027 | Every PDE manufacturer selling into EU | ❌ | T2 | **5** |
| 6 | **EUDR due-diligence statements, small operators** | 30 Dec 2026 / 30 Jun 2027 | EU importers/traders of 7 commodities | ❌ | T1 (enterprise) | **5** |
| 7 | **Multi-country EPR volume declarations** (marketplace sellers) | **LIVE 12 Aug 2026** | EU marketplace sellers | Scrapeable | **T1** | **4** |
| 8 | **FSMA 204 traceability plan + KDE/CTE records** | 20 Jul 2028 | FTL food handlers | Partial (state) | **T1** | **4** |

---

# CANDIDATE 1 — "DROP Cycle": 45-day deletion processing for small California data brokers

### 1. One sentence
Every one of the 581 companies on California's data broker registry must, every 45 days forever, pull a deletion list from a state platform, match it against their own database, delete, and report back — and most of them are 3-to-20-person lead-gen and people-search firms with no engineering capacity to do it.

### 2. The artifact
A closed-loop compliance run: (a) pull the current DROP deletion list; (b) hashed/normalised match against the broker's own records; (c) generate the deletion work order and the suppression list that stops deleted consumers reappearing on the next data ingest; (d) post per-request status back to DROP; (e) emit a timestamped, immutable **evidence file** — per request, per cycle, per record — plus the July 1 privacy-policy metrics disclosure, pre-formatted.

The evidence file is the product. The deletion is the commodity; the provable record that you deleted on time is what a broker hands to CalPrivacy.

### 3. Evidence — **T1 + T2**
- **581 registered data brokers, "the highest number of registrants since the registry was established in 2020"** — CalPrivacy announcement, 2 Jun 2026. https://privacy.ca.gov/2026/06/privacy-momentum-builds-300000-californians-sign-up-for-drop-as-registered-data-brokers-hit-a-record-high/
- **"more than 300,000 Californians signing up for the free tool since its launch just five months ago"** — same source. This is the size of the queue landing on brokers on day one.
- **"Beginning August 1, all data brokers will be required to access DROP and begin processing deletion requests."** — same source.
- Statutory penalty: **"$200 (plus expenses) per request per day for each day of noncompliance"** — Alston & Bird, https://www.alstonprivacy.com/drop-is-coming-due-what-californias-delete-act-means-for-data-brokers-in-august/ . With 300k requests in the pool, a broker that misses a cycle is not fined, it is annihilated.
- **Budget already proven:** the 2026 annual registration fee is **$6,000 plus payment processing**, non-refundable, non-prorated. A firm that already writes a $6,000 cheque to be *allowed* to be a data broker will pay four figures to not be destroyed by it.
- **A worse version already exists and is free:** Drop45 (https://drop45.org) ships a browser-only matcher — *"Upload a DROP consumer deletion list and your own records; standardization, SHA-256 hashing and matching all run in your browser… Free for up to 500 records per run."* It explicitly scopes itself: *"Drop45 does the matching half of this."* That is the market telling us where the gap is — nobody is doing the **other half** (status reporting, suppression persistence, evidence trail, cycle scheduling).
- **Enterprise incumbents are present and mis-sized:** Ketch, DataGrail, Transcend all published DROP guides in 2026. These are six-figure privacy platforms sold to enterprises. They will not sell to a 6-person people-search site.
- Registration-services market exists: Captain Compliance sells "Data Broker Registration Services."

### 4. The clock
- Delete Act (SB 362) signed Oct 2023.
- DROP opened to consumers **1 Jan 2026**; broker registration deadline **31 Jan 2026**; API access spring 2026.
- **Processing obligation switched on 1 Aug 2026 — 26 days ago.** The first 45-day cycle closes mid-September 2026. The first *missed* cycle is a September event.
- **SB 361 (Defending Californians' Act)** expanded disclosure obligations effective Jan 2026, pulling in businesses that did not previously consider themselves brokers.
- Second clock behind it: **Connecticut and New Jersey data broker registries take effect 2027** (CT $2,500/yr, NJ tiered $5,000–$1.5M); CT launches its own deletion mechanism **1 Jul 2028**. Texas ($300), Oregon ($600), Vermont ($100) are already live. Source: DataGrail 2026 field guide, https://www.datagrail.io/blog/data-privacy/data-broker-compliance/ . The product generalises from one state to six on a known schedule.

### 5. First ten users
**The regulator publishes the list.** The California Data Broker Registry is a public, downloadable CSV at https://cppa.ca.gov/data_broker_registry/ with a "Download Registration Information" button, plus separate archived CSVs for 2020–2025. Registration fields include business information and **contact information**.

**Honest caveat:** I confirmed the register exists, is public, is downloadable as CSV, contains contact fields, and holds 581 registrants. **I did not pull the CSV and enumerate individual company names this cycle.** That is a sub-hour task and is verification step #1. I am not naming ten companies I have not actually read off the file — per the standing rule against invented specifics.

What makes this pass Gate 1 anyway: the first ten users are not a population I have to *find*, they are a file I have to *download*. There is no audience requirement, no warm intro, no ad spend. 581 named entities, each under a $200/request/day gun, each with a published contact address.

### 6. Gate check
- **G1 distribution — PASS (strongest of the cycle).** Public CSV of 581 named obligated entities with contact fields. Cold outreach to a statutorily-obligated list is not "content marketing."
- **G2 observable demand — PASS.** 300k consumer requests already queued; free competitor shipped and self-describes as half a solution; enterprise vendors publishing; $6k/yr registration fee proves budget.
- **G3 buildable — PASS.** Hashing, matching, scheduling, API posting, evidence logging. No credential needed to run a deletion cycle. **Boundary:** California and Connecticut mandate an **independent third-party audit every three years** (first CA audit 2028). We cannot be that auditor and must never imply we are. We build the record the auditor reads. Say this in the marketing, do not sell around it.
- **G4 self-verifiable in 14 days — PASS.** Download the registry, segment by size, build the matcher + evidence file against the published DROP schema, and cold-email the list. Whether small brokers reply is answerable by us alone in under two weeks. No stranger's cooperation required to run the test.
- **G5 clock — PASS.** 1 Aug 2026, twenty-six days ago, with the first cycle closing in September.

### 7. What already exists
**Drop45** — free, browser-only, matching only, capped at 500 records/run, no persistence, no status reporting, no evidence trail. Inadequate by its own description. **Ketch / DataGrail / Transcend** — enterprise privacy platforms; correct functionality, wrong customer, wrong price. **Captain Compliance** — registration services, not the recurring cycle. Nobody is selling the recurring 45-day machine to the bottom 400 of the registry.

### 8. Price signal
Registration alone: **$6,000/yr California**, $2,500 Connecticut (2027), $5,000+ New Jersey (2027), $600 Oregon, $300 Texas, $100 Vermont. Penalty exposure: $200/request/day. A $200–600/month product is a rounding error against both. UNVERIFIED: I have no published price for a DROP-processing product because none appears to exist yet.

### 9. Confidence: **8/10**
Docked two points because (a) I have not yet read the registry CSV to confirm contact fields are usable emails rather than registered-agent addresses, and (b) some fraction of the 581 are subsidiaries of large enterprises already covered by DataGrail/Ketch. The addressable slice is the long tail, and I have not sized it.

---

# CANDIDATE 2 — Reg S-P compliance pack for small SEC-registered investment advisers

### 1. One sentence
Every SEC-registered adviser under $1.5B AUM had to have a written incident response program, vendor breach agreements and a compliance recordkeeping trail in place by 3 June 2026 — the SEC has named it a 2026 exam priority, and the going rate for the paperwork is $3,000–$25,000.

### 2. The artifact
A firm-specific Reg S-P bundle: written incident response program; customer notification procedure (30-day rule); service-provider oversight policy with the 72-hour notification clause plus a tracked register of every vendor and its contract status; updated FAST Act privacy notice; risk matrix; and — the part the templates omit — the **maintained recordkeeping file** the rule actually demands: copies of the policies, the vendor agreements, the log of unauthorised-access incidents, and the written determinations about whether customers had to be notified.

### 3. Evidence — **T1 (published prices, multiple tiers)**
- **$599** — Cybersecurity Readiness Program, *"an easily customizable Microsoft Word template,"* including a Written Information Security Program and Cybersecurity Incident Response Plan. **$799** bundled with a one-hour consulting session. (RIA Compliance Consultants.)
- **Attorney: $3,000 to $15,000**, four to twelve weeks. **Compliance consultant: $5,000 to $25,000** project-based, or **$1,000 to $5,000 per month** ongoing. Source: https://mrfixitgeeks.com/blog/reg-sp-compliance-cost-comparison-ria/ — which also reports *"law firms serving the RIA compliance space are seeing increased demand as the June 3 deadline approaches."*
- Same source: *"The time cost is 47 to 90 hours minimum for a principal with no prior compliance writing background."*
- **"The SEC's Examinations Division has specifically identified Regulation S-P compliance as a 2026 examination priority."** — Corporate Compliance Insights, https://www.corporatecomplianceinsights.com/smaller-investment-advisers-june-deadline-reg-s-p/
- Required records, verbatim: *"copies of written policies, service provider agreements, unauthorized access incidents, and determinations about customer notifications"* — same source.
- **16,544 investment advisers in 2025**, a record; **87.3% have under $5B AUM.** Investment Adviser Association 2026 Industry Snapshot, https://www.investmentadviser.org/wp-content/uploads/2026/06/Snapshot-2026.pdf
- A visible cottage industry has formed: Omega Systems, Venminder, AdeliaRisk, SecureWealthIT, NetSys, Advisor Armor, BlackSheep, ARS Compliance all published Reg S-P offerings in 2026.

### 4. The clock
Amended Reg S-P adopted May 2024. Larger entities complied 3 Dec 2025. **Smaller entities (RIAs under $1.5B RAUM): 3 June 2026 — twelve weeks ago.** The clock is not the deadline, it is the exam. Deficiency letters from the 2026 exam cycle land through late 2026 and 2027. Related: the SEC has separately proposed redefining "small entity" at a $1B AUM line, which re-opens the question for a slice of firms.

### 5. First ten users
**The regulator publishes the list, again.** SEC Form ADV complete dataset, free CSV, historical from Jan 2001 to the most recent quarter: https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers and https://adviserinfo.sec.gov/adv . Form ADV Part 1 carries firm name, business address, phone, RAUM (so you can filter to under $1.5B directly), and the **Chief Compliance Officer's name, phone and email** in Item 1.J. That is a filtered, targeted, contact-complete list of roughly fourteen thousand named buyers.

**Same honest caveat as Candidate 1:** I confirmed the dataset is public, free, in CSV, and contains CCO contact details. I did not download it and enumerate names this cycle.

### 6. Gate check
- **G1 — PASS.** Public CSV including the compliance officer's own email address, filterable by the exact AUM threshold the rule uses.
- **G2 — PASS, T1.** Money is visibly moving at $599, $799, $3k–15k and $5k–25k for the identical artifact.
- **G3 — PASS.** No licence is needed to write compliance policies; the firm's own CCO adopts them. Compliance consultants are unlicensed. **Watch:** do not offer to *be* the CCO or to conduct the independent testing.
- **G4 — PASS.** Build the generator, pull 200 sub-$1.5B firms from Form ADV, cold-email the CCOs. Fully self-run.
- **G5 — PASS.** 3 Jun 2026 + 2026 exam priority designation.

### 7. What already exists
A **$599 Word template** is the leading self-serve product. That is the whole opportunity: a Word template cannot maintain the vendor register, cannot log incidents, cannot produce the written notification determinations, and cannot show an examiner a dated record of ongoing compliance — all of which the rule requires and the exam will ask for. The template sells the *document*; the rule demands the *file*. Above it, $5k–25k consultants are correct but priced out of reach for a two-person RIA.

### 8. Price signal
$599 / $799 (template) · $3,000–15,000 (attorney) · $5,000–25,000 project or $1,000–5,000/mo (consultant). A $49–99/month maintained-evidence product sits in an empty band.

### 9. Confidence: **7/10**
Docked because the headline deadline has passed — the buying trigger becomes an exam letter, which is lumpier and less predictable than a date. Also the most crowded of the register-backed three.

---

# CANDIDATE 3 — DORA Register of Information filer for small EU financial entities

### 1. One sentence
Every EU financial entity — including payment institutions, e-money firms, small insurers, intermediaries and crypto-asset service providers with three staff — must file an annual machine-readable register of every ICT contract in xBRL-CSV across fifteen interlinked templates, and in the regulators' own dry run only 6.5% of firms got it right.

### 2. The artifact
A validated xBRL-CSV submission package: templates B_01.01 → B_07.01 correctly cross-linked on the contractual-arrangement reference number, LEI resolution for every provider, subcontractor chains populated, dropdown codes rather than free text, plus a pre-submission validation report run against all 116 published data-quality checks, and a diff against last year's filing.

### 3. Evidence — **T2, strong**
- **"Only 6.5% of nearly 1,000 firms across the EU passed all 116 data quality checks during the 2024 ESA dry-run exercise."** — fscom, https://fscom.co/blog/preparing-for-the-2026-dora-reporting-deadline-lessons-from-2025-every-firm-should-know/
- Named failure modes from the same source: *"using incorrect file formats (submissions must use xBRL-CSV); including free text entries instead of required drop-down codes; leaving mandatory fields and supply chain subcontractor details blank; duplicating unique identifiers like contract reference numbers."* Every one of those is a validator's job, not a consultant's.
- Same source: *"many organizations underestimated the effort required."*
- Deadlines are real and staggered per national authority: **31 March 2026** headline; **Netherlands (DNB) 22 March**; **Austria 16 Feb–13 Mar**; **Luxembourg CSSF eDesk opened 11 Feb 2026**. Data as of 31 Dec. The 2027 cycle repeats on the same rhythm.
- A small-firm-focused vendor market already exists: **DoraPass** publishes "DORA Register of Information: What Payment Institutions Need to Know"; also RegReportingDesk, regulation-dora.eu, Orbiq, 10punto10 (explicitly "for Italian SMEs").
- Scope is explicitly the long tail: *"banks, insurers, investment firms, payment institutions, crypto-asset service providers."* Further institutions come into scope from **1 January 2027**.

### 4. The clock
DORA applied 17 Jan 2025. First RoI submissions Apr 2025 (mass failure). Second cycle Mar 2026 with proportionality relief. **Third cycle ~Mar–Apr 2027**, and a new tranche of institutions enters scope **1 Jan 2027**. Annual, forever, with a format that punishes spreadsheets.

### 5. First ten users
Public registers again: the **EBA credit institutions / payment institutions / e-money registers**, national competent authority registers of authorised PIs and EMIs, and **EIOPA insurance intermediary registers** — all published with entity name, jurisdiction and address. Filter to entities with fewer than ~50 staff.

**Caveat:** I did not pull these registers this cycle, and contact detail quality varies by member state (some publish only a registered address). Gate 1 here is one notch weaker than Candidates 1 and 2.

### 6. Gate check
- **G1 — PASS (weaker).** Public authorisation registers exist per country; contact quality unverified.
- **G2 — PASS.** 6.5% pass rate against 116 published checks is about as clean a demand signal as a regulator ever emits, and vendors are already selling to payment institutions specifically.
- **G3 — PASS.** xBRL-CSV generation and validation is exactly the kind of deterministic data engineering this operator is strongest at. No credential; the firm signs its own filing.
- **G4 — PASS.** The ITS templates and the 116 validation rules are public. Build the validator, run it against the published rules, and the technical assumption is proven or killed in days, alone.
- **G5 — PASS.** Annual cycle + new entities in scope 1 Jan 2027.

### 7. What already exists
DoraPass and RegReportingDesk target this. Big-four and boutique consultancies (fscom, KPMG, Baker Tilly) sell it as a project. **Adequacy unresolved — this is the main gap in my research.** DoraPass's pricing page returned HTTP 503 on fetch; I could not establish whether a self-serve product at SME price already exists. **If DoraPass is a working self-serve product at €50–200/month, this candidate is probably dead on Gate 2 and should be killed rather than built.** That is verification step #1.

### 8. Price signal
**UNVERIFIED.** No published price obtained for any DORA RoI product or consultancy engagement. Do not build a model on a guessed number.

### 9. Confidence: **6/10**
The pain is the best-evidenced of any candidate here (6.5%). The competitive picture is the least-evidenced. Those cancel out.

---

# CANDIDATE 4 — CCPA risk assessment + ADMT pre-use notice pack

### 1. One sentence
From 1 January 2027 any CCPA-covered business using automated decision-making for a significant decision must publish a pre-use notice and honour opt-outs, and by 1 April 2028 must file an attestation and summary of privacy risk assessments covering all of 2026 and 2027 — meaning the assessments must be being written *right now*, retroactively.

### 2. The artifact
A dated risk-assessment record per processing activity (selling/sharing PI, sensitive PI, ADMT for significant decisions, AI training), in the CPPA's required structure; the pre-use notice text and the access-explanation and human-appeal flows for ADMT; and the **April 2028 attestation + summary package** pre-assembled from the record.

### 3. Evidence — **T2**
- Regulations finalised: CPPA announcement 23 Sep 2025, https://www.cppa.ca.gov/announcements/2025/20250923.html
- **"Businesses subject to risk assessment requirements must begin compliance by January 1, 2026."** The retroactive trap: assessments conducted during 2026 and 2027 must be summarised in the **1 April 2028** filing. A business that starts in 2027 has already lost a year of records.
- **ADMT: "applicable businesses must comply by January 1, 2027."** Pre-use notice, access explanations, opt-out, human appeal.
- Cybersecurity audit certifications phase by revenue: **1 Apr 2028** (>$100M), **1 Apr 2029** ($50–100M), **1 Apr 2030** (<$50M).
- Coverage from White & Case, Morrison Foerster, Skadden, Baker McKenzie, Wiley, Alston & Bird, FTI within weeks of finalisation — the law-firm alert density is itself the panic signal. Commercial tooling appearing (Hyperproof).

### 4. The clock
Finalised Sept 2025 · risk assessments start 1 Jan 2026 · **ADMT 1 Jan 2027** · first CPPA filing 1 Apr 2028.

### 5. First ten users
**The 581-name California data broker registry again** — every registered data broker sells or shares personal information and is therefore squarely inside the risk-assessment trigger. This is the same list as Candidate 1, which is why these two should be considered as one wedge with two products rather than two businesses.

Beyond that list, enumerating "CCPA-covered businesses using ADMT" is genuinely hard and I could not solve it. That is the honest Gate 1 weakness.

### 6. Gate check
- **G1 — CONDITIONAL PASS.** Passes only if sold into the data-broker list. Fails as a standalone play — I cannot name a general list of ADMT users.
- **G2 — PASS (marginal).** Law-firm alert density and Hyperproof/FTI activity, but no published price for a self-serve product found.
- **G3 — PASS** for risk assessments and ADMT notices. **PARTIAL FAIL** for the cybersecurity audit — that requires an independent auditor. Do not touch the audit.
- **G4 — PASS.** Regulation text is public; build the assessment generator and test it on the broker list.
- **G5 — PASS.** 1 Jan 2027.

### 7. What already exists
Hyperproof, FTI and the enterprise GRC field. Nothing self-serve identified at small-business price.

### 8. Price signal
**UNVERIFIED.** No prices obtained.

### 9. Confidence: **5/10** as a standalone; **7/10** as the second product sold to Candidate 1's customer list. Recommend treating it as the latter.

---

# CANDIDATE 5 — Cyber Resilience Act: Art. 14 reporting + technical documentation for small PDE makers

### 1. One sentence
From 11 September 2026 — fifteen days from now — every manufacturer of a product with digital elements sold into the EU must report an actively exploited vulnerability to ENISA within 24 hours, including in products shipped years ago, and by 11 December 2027 must hold a full technical file, SBOM and EU declaration of conformity.

### 2. The artifact
Two things. Near-term: a monitoring-to-notification pipeline — SBOM ingest, watch against EUVD/CISA KEV/NVD, and the **pre-filled ENISA early-warning notification** ready to submit inside the 24-hour window, plus the 72-hour and 14-day follow-ups. Long-term: the Annex VII technical documentation pack, SBOM in the required format, and the EU DoC.

### 3. Evidence — **T2**
- **ENISA's own SME survey**, 194 organisations across 31 countries, conducted Feb–Mar 2026: **66% had heard of the CRA**; **142 of 194 respondents said they need financial support**; *"incident response and product lifecycle management emerged as particularly problematic, especially for microcompanies"*; and decisively — **"over 70% requesting technical documentation and secure development templates."** https://www.enisa.europa.eu/news/where-do-smes-stand-in-preparing-for-the-cyber-resilience-act
- That last line is a regulator reporting that the affected population has explicitly asked for exactly the artifact we would sell.
- Crowell & Moring published a countdown alert: "11 September 2026 incident/vulnerability reporting deadline is less than 100 days away."
- Scope is total: *"Company size is irrelevant: if you develop it yourself, you're the manufacturer — the role with the most obligations,"* and *"the reporting obligations from September 2026 apply to all products on the market — including those already shipped."*
- Vendor activity: sbomify, Cloudsmith, HeroDevs, ArmorCode, Visure, checkfix.io, Distr, OpenSSF all publishing CRA material in 2026.

### 4. The clock
CRA in force 10 Dec 2024 · **Art. 14 reporting 11 Sep 2026** · full application 11 Dec 2027.

### 5. First ten users
**Could not find them.** This is the candidate's fatal weakness. There is no register of PDE manufacturers. Plausible enumerable slices — IoT/hardware brands on Kickstarter, commercial open-core vendors on GitHub, firms already publishing a security.txt — are all inference, not a list. I am not going to dress that up as distribution.

### 6. Gate check
- **G1 — FAIL, unresolved.** No enumerable list. Everything I can think of is a scraping heuristic, not a register.
- **G2 — PASS.** ENISA survey plus a live vendor field.
- **G3 — PASS** for the default self-assessment class. Notified body needed only for important/critical Class II products — say so and stay out of it.
- **G4 — PASS.** Schemas and reporting requirements are public.
- **G5 — PASS.** 15 days.
- **Additional headwind:** ENISA states **"SMEs and micro-enterprises cannot be financially sanctioned for failing to meet Article 14 notification deadlines."** The deadline does not do the selling for the smallest firms — which is precisely the property this surface was supposed to guarantee. And **ENISA ships a free Excel maturity tool.**

### 7. What already exists
sbomify, Cloudsmith, HeroDevs, ArmorCode, Visure, checkfix.io — a crowded and well-funded field, plus a free ENISA tool.

### 8. Price signal
**UNVERIFIED.** No CRA product pricing obtained despite direct search.

### 9. Confidence: **5/10.** Correct clock, correct artifact, wrong gate. G1 has no answer and the SME fine exemption blunts the forcing function. **I would not start here.** Included because the clock is two weeks out and the parent may want it on the watchlist.

---

# CANDIDATE 6 — EUDR due-diligence statements for small operators and traders

### 1. One sentence
From 30 December 2026 (medium/large) and 30 June 2027 (micro/small), anyone placing coffee, cocoa, timber, rubber, soy, palm or cattle products on the EU market must file a geolocated due-diligence statement in TRACES per consignment.

### 2. The artifact
A submitted DDS with its reference number, backed by geolocation polygons per plot, supplier documentation, a risk assessment and a risk-mitigation record — plus the lot-to-batch-to-bag traceability chain that lets an inspector be answered in minutes.

### 3. Evidence — **T1, but priced at the wrong altitude**
- Deadlines confirmed by the Council: revision *"postpones the application of the regulation for all operators until 30 December 2026, with an extra six-month cushion for micro and small operators."* Council press release 18 Dec 2025, https://www.consilium.europa.eu/en/press/press-releases/2025/12/18/deforestation-council-signs-off-targeted-revision-to-simplify-and-postpone-the-regulation/
- Small operators defined as *"fewer than 50 employees and annual turnover below €10 million,"* compliance from **30 June 2027**.
- Live commercial market: TraceX, IntegrityNext, Coolset, Trusty, Bindu, ImpactBuying, Anthesis, **Coffee Lab** (roaster-specific: stores DDS reference numbers on green-coffee lots, lot→batch→bag QR traceability, structured export for inspections — https://coffeelab.app/en/fuer-roestereien/eudr/).
- **Claimed but UNVERIFIED:** "73% of coffee roasters in the EU still don't understand what deforestation-free means" and "89% have done zero work on supply chain traceability." I found these repeated on vendor blogs and could not trace them to a primary survey. **Treat as unverified vendor marketing. Do not build a case on them.**

### 4. The clock
Applied → delayed → simplified. **30 Dec 2026 / 30 Jun 2027.**

### 5. First ten users
**Weak.** TRACES publishes no operator list. Specialty-coffee and timber-trade association directories exist but are membership lists, not obligation lists. I could not construct an enumerable population.

### 6. Gate check
- **G1 — FAIL/WEAK.** No public register of operators.
- **G2 — PASS.** Real vendors, real money, real deadline.
- **G3 — PASS.** The operator's own authorised representative signs the DDS. No licensed professional.
- **G4 — PASS.** TRACES schema is public.
- **G5 — PASS.**
- **G2 erosion to note:** the simplification specifically gutted the small-operator segment — *"micro and small primary operators from low-risk countries… will be required to submit a simple, one-off declaration"* and *"where relevant information is already available in Member State databases, no further action will be required."* The regulator removed the pain from precisely the population we were targeting. The remaining pain sits with small **traders and importers** (roasters, chocolate makers, furniture importers), not primary producers.

### 7. What already exists
Coffee Lab is the closest analogue and is aimed at exactly the right customer. Pricing not published.

### 8. Price signal
**UNVERIFIED.** No EUDR pricing obtained (search budget exhausted before this query completed).

### 9. Confidence: **5/10.** Good clock, good artifact, no list, and the EU deliberately removed the burden from the small end.

---

# CANDIDATE 7 — Multi-country packaging EPR volume declarations for EU marketplace sellers

### 1. One sentence
Since 12 August 2026 Amazon verifies a valid packaging EPR registration number in **every** EU country a seller ships to or stores in — not just Germany and France — and each of those national schemes then wants recurring packaging-weight declarations by material.

### 2. The artifact
Not the registration (see price problem below) — the **recurring per-country, per-material packaging weight declaration**, computed from the seller's SKU catalogue and sales data, formatted per scheme (LUCID/ZSVR, Citeo, CONAI, etc.), with the filing calendar and the evidence file.

### 3. Evidence — **T1, and it cuts both ways**
- Enforcement is live and brutal: *"Sellers without valid EPR registration numbers uploaded to Seller Central risk immediate listing deactivation — not warnings, not grace periods, just deactivation."*
- The scope change: *"Until now, most Amazon sellers got away with two EPR registrations: Germany and France… That ends on 12 August 2026."* Verification expands to Italy, Netherlands, Austria, Belgium, Poland, Ireland, Sweden and the rest. https://geteuready.com/guides/amazon-epr-verification-2026/
- Ongoing obligation confirmed: *"every scheme then wants periodic packaging weight reports."*
- A dense agency market exists: AVASK, Staxxer, ekoniq, geteuready, Lappa, Minefield Navigator, Westwood Sourcing, Acumen, Eldris.
- **The problem — published freelance prices:** Fiverr gigs for "EPR registration in Germany France for Amazon seller" at **$50** (ginnachen), **$20** (mercymergan, business_akins), and **$5** (shafqat125b). Upwork carries the same work.

### 4. The clock
PPWR (EU 2025/40) general application **12 Aug 2026** — fifteen days ago. New national registers from **October 2027**.

### 5. First ten users
Enumerable by scraping. Under the Omnibus Directive, Amazon EU seller profile pages display the seller's legal business name and address. Cross-reference against the national EPR registers (Germany's LUCID register is publicly searchable) to find sellers who are *missing* from a country's register while actively selling there. That produces a targeted list of provably non-compliant, provably at-risk sellers. That is a real, buildable Gate 1 answer — the best in the non-register group.

### 6. Gate check
- **G1 — PASS.** Scrapeable seller identities + publicly searchable national registers = a computed list of the non-compliant.
- **G2 — PASS on volume, FAIL on price.** Money is visibly moving, but the market price for the registration half has been set at **$5–50 by Fiverr**. Anything we build competes against that anchor.
- **G3 — PASS.** Registration and volume declarations need no credential.
- **G4 — PASS.** Build the LUCID-vs-Amazon gap detector in days and see whether the sellers it flags will pay.
- **G5 — PASS.** 12 Aug 2026.

### 7. What already exists
A saturated agency layer (AVASK et al.) plus a $5 Fiverr floor. The one thing neither does well is the **recurring multi-country volume declaration** computed from actual sales data — agencies do it manually and annually, freelancers do not do it at all.

### 8. Price signal
**$5–$50** per registration on Fiverr (published, verbatim). Agency pricing UNVERIFIED — geteuready's page quotes no figures.

### 9. Confidence: **4/10.** Genuinely enumerable population and genuine enforcement panic, undone by a $5 price anchor on the visible half of the work. Only viable if the recurring volume declaration turns out to be a separate, higher-value purchase — which I did not verify.

---

# CANDIDATE 8 — FSMA 204 traceability plan and KDE/CTE record system for small food makers

### 1. One sentence
By 20 July 2028 anyone who manufactures, processes, packs or holds a food on the FDA's Food Traceability List must keep key data elements at every critical tracking event and produce a sortable electronic spreadsheet to the FDA within 24 hours — and their grocery buyers are demanding the data years early.

### 2. The artifact
The written traceability plan, the CTE/KDE record schema mapped to the firm's actual process, and — the thing the rule really tests — the **sortable electronic spreadsheet produced on 24-hour demand**.

### 3. Evidence — **T1**
- Compliance date: **20 July 2028** (FDA extended by 30 months). Federal Register, 7 Aug 2025, https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension
- **Published software prices:** *"Some basic traceability software plans start at $3,000 per year, while more advanced systems can cost $30,000, $120,000, or even more per year."*
- **Buyer-side pull is already live:** *"National grocers, foodservice distributors, and chain buyers are already requiring FSMA 204-ready data elements from suppliers — even for product that will not ship until 2027."* This is the thing that rescues a 2028 deadline from being a pure timing bet.
- A consultancy market exists with named firms: Trustwell, FoodReady.ai, Kellerman Consulting, Afya Food Safety.

### 4. The clock
Rule final Nov 2022 · compliance extended to **20 Jul 2028** · buyer mandates flowing through supply contracts from 2026–27.

### 5. First ten users
Partially solvable. State food-processor and food-establishment licence registries are public in many US states and list name, address and product category. The FDA's own food facility registration database withholds facility names, so the federal list is not usable. **I did not verify which states publish usable contact data.**

### 6. Gate check
- **G1 — WEAK PASS.** State licence registries are the route; unverified.
- **G2 — PASS.** $3,000/yr floor price published, named consultancies, buyer-side mandates already in contracts.
- **G3 — PASS.** No licensed professional signs a traceability plan. (Distinct from a HACCP/food-safety plan, which needs a PCQI — stay out of that.)
- **G4 — PASS.** The FTL and the KDE/CTE requirements are public; build the record schema and test it.
- **G5 — WEAK.** 20 Jul 2028 is 23 months out. **This is the Gate-1 timing risk the brief warned about**, offset only by the buyer-side pull.

### 7. What already exists
Trustwell, inecta, TrueCommerce, FoodReady.ai and a $3,000/yr entry price. The gap is below $3,000/yr: the single-facility maker who needs a plan and a spreadsheet, not an ERP.

### 8. Price signal
**$3,000/yr** basic software floor; $30k/$120k+ advanced (published). Consultancy pricing UNVERIFIED — Trustwell, FoodReady and Kellerman all quote on enquiry.

### 9. Confidence: **4/10.** Real money, real artifact, but the deadline is too far out and the population list is the least verified of the eight.

---

# SPECIAL REPORT — E-INVOICING IS A DRY SURFACE FOR THIS OPERATOR

The brief flagged e-invoicing for particular attention. I researched it hardest and it is the clearest **kill** in the set. The obligation is perfect on paper — dated, purely data-format, binds every business — and it fails anyway, for two structural reasons that repeat country by country.

**Reason 1 — the intermediary position is accreditation-gated (Gate 3).**

| Country | Date | Gate |
|---|---|---|
| **France** | 1 Sep 2026 receive (all) · 1 Sep 2027 issue (SME) | Invoices must flow through a state-registered **Plateforme de Dématérialisation Partenaire**. We cannot become a PDP. |
| **UAE** | ASP appointment by **30 Oct 2026** · go-live **1 Jan 2027** · smaller firms 1 Jul 2027 | Requires an **Accredited Service Provider**. Same wall. |

**Reason 2 — where the position is open, the artifact is already free (Gate 2).**

| Country | Date | Why it fails |
|---|---|---|
| **Germany** | 1 Jan 2027 (>€800k prior-year turnover) · **1 Jan 2028 all businesses** | The largest population on the surface (~every German B2B firm) and the most saturated market: DATEV owns German SMB accounting, and lexoffice, sevDesk, Claribill, Certiscan, ClearTax, TaxLayer are all shipping XRechnung/ZUGFeRD today. Kleinunternehmer are exempt from *issuing* under §34a UStDV. |
| **Poland (KSeF)** | Large 1 Feb 2026 · most VAT firms 1 Apr 2026 · **micro-entrepreneurs 1 Jan 2027** | Government ships free KSeF tooling. |
| **Spain (Verifactu)** | Companies 1 Jan 2026 · **autónomos moved from 1 Jul 2026 → 1 Jul 2027** | ~3.4M autónomos and fines to €50,000/yr — but the AEAT provides a free application and every Spanish invoicing tool has shipped compliance. Note the deadline *moved*, which is its own warning about regulatory-clock timing bets. |
| **Belgium** | 1 Jan 2026, big bang, all VAT-registered | Already passed; Peppol; government-listed cheap tools. |

**The one corner I did not fully close:** counterparty-readiness data — "which of my suppliers and customers are e-invoice ready, on which network, under which national mandate." The Peppol directory is public and queryable and no one appears to sell this as a product. I judge willingness to pay to be low and did not pursue it. Flagging it rather than dropping it.

**Verdict: e-invoicing is a real regulatory clock that someone else will monetise.** Either the state picks the intermediaries, or the incumbent accounting suite bundles it to zero. Both outcomes are visible today in the pricing pages above. Recommend the engine stop spending cycles here.

---

# KILLED ON SIGHT

| Rule | Date | Gate | Reason |
|---|---|---|---|
| **Colorado AI Act (SB 24-205)** | was 30 Jun 2026 | **G5 — clock removed** | **SB 189, signed 14 May 2026**, delayed to 1 Jan 2027 *and gutted it*: eliminated the duty of care, deployer risk-management programs, **impact assessments** and AG reporting. The artifact we would have sold no longer exists. A clean example of why a regulatory clock is not a business until the rule survives its own amendment cycle. |
| **NYC Local Law 144 bias audits** | live | **G3** | Requires an **independent auditor**. We cannot sign it. Kill. |
| **UK Companies House identity verification (ECCTA)** | phased through 2026 | **G3** | Verification must run through GOV.UK One Login or an **Authorised Corporate Service Provider**, which requires AML supervision. Kill. |
| **CBAM annual declaration** | first annual declaration 2027 | **G3** | Embedded-emissions data in the definitive-regime declaration must be checked by an **accredited verifier**. The core artifact needs a credential we cannot hold. (The 31 Mar 2026 authorised-declarant application deadline has also passed.) Kill. |
| **GPSR EU Responsible Person** | live | **G3** | Requires an **EU-established legal entity that accepts product liability**. That is a licensed-agent service, not software. Kill the core; the technical-file half is contested by EaseCert, euverify, eugpsr.eu, EARP, ShieldMyShop. |
| **MDR / IVDR** | phased | **G3** | Notified body. Kill. |
| **Australia mandatory climate reporting, Group 3** | 1 Jul 2027 | **G1 + G3** | Report requires assurance by a registered company auditor, and the population (>AU$50m revenue) buys through procurement. Kill. |
| **European Accessibility Act** | enforceable 28 Jun 2025 | **G2** | Adequate competitors. accessiBe, UserWay, AudioEye, Level Access, plus a dense audit-tool field. Fines are real (€60k Ireland to ~€900k Sweden) but the market is served. Kill. |
| **EU AI Act Art. 50 transparency** | **2 Aug 2026** | **G2** | The artifact is a disclosure notice — a banner and a line of text. No willingness to pay for something a developer ships in an afternoon. (Note the AI Act's other deadlines were themselves extended in 2026 — another moved clock.) Kill. |
| **MTD for Income Tax (UK)** | Apr 2026 £50k · **Apr 2027 £30k** · Apr 2028 £20k | **G2** | Enormous population (**436,000 already signed up** per GOV.UK) but HMRC states free software options exist, and Sage/Xero/QuickBooks/FreeAgent own the channel through accountants. Kill. |
| **EU Battery Passport** | **18 Feb 2027** | **G1** | EV and industrial >2kWh batteries — large manufacturers with procurement. The LMT slice (e-bikes, e-scooters) is the only small-buyer corner and I could not enumerate it. Kill for now. |

## Did not clear the evidence bar — NOT submitted as candidates

Per the T3/T4 rule, these had a real date and a real population but **no T1 or T2 evidence**, so they are recorded rather than proposed:

- **EU Machinery Regulation 2023/1230 — 20 Jan 2027.** Technical file + DoC + digital instructions for every machine placed on the market; explicitly hits SMEs (*"a 30-person SME building special-purpose machinery"*); the DoC becomes a data record that must stay reachable for a decade. I found **zero** pricing, zero freelance gigs, zero competitor products. Absence of competitors is a verdict, not an opening.
- **EU Pay Transparency Directive — transposed 7 Jun 2026, first reports 7 Jun 2027.** Only **4 of 27** Member States met the transposition deadline (Slovakia, Italy, Lithuania, Malta), so the obligation is not yet uniform. Population is 100+/150+/250+ employee firms — i.e. has an HR function and procurement. No pricing evidence obtained.
- **FinCEN Investment Adviser AML rule — 1 Jan 2028.** ~20,000 RIAs/ERAs, and the Form ADV register makes them enumerable. But FinCEN did not merely delay it — it **reopened the rule** to *"review and tailor"* it to different business models. Building against a rule the regulator has announced it is rewriting is the definition of a timing bet.
- **CFPB Section 1071 small-business lending** — first register due 1 Jun 2029, and the CFPB narrowed the rule in May 2026. Too far, too unstable.

---

# WHAT I WOULD DO WITH THIS

**Build Candidate 1.** It is the only one where Gate 1 — the binding constraint — is solved by a download rather than by a marketing plan, and where the deadline is not approaching but already twenty-six days past with the first cycle closing in September. Candidate 4 is its natural second product to the same 581 names. Candidate 2 is the fallback with the same register-backed shape and better price evidence but a softer trigger.

**The generalisable rule this cycle produced:** on a regulatory surface, *do not ask which rule is biggest. Ask which regulator publishes the list.* CalPrivacy publishes 581 names with contact fields. The SEC publishes 16,544 with the compliance officer's email. Those two facts are worth more than every market-size estimate on this surface combined.

---

# HONEST LIMITATIONS

1. **Web search budget exhausted at 200 calls.** Three price questions died unanswered: EUDR consultancy rates, DORA RoI product pricing, and CRA product pricing. All three are marked UNVERIFIED and none is load-bearing for Candidate 1.
2. **I did not download either flagship register.** I verified that the CPPA registry CSV and the SEC Form ADV dataset are public, free, downloadable and contain contact fields — I did not pull them and read off names. Under the no-invented-specifics rule I would rather report this than list ten plausible-sounding companies. **This is verification step #1 and it takes under an hour.**
3. **DoraPass returned HTTP 503.** Candidate 3's competitive picture is genuinely unknown and it may be dead on Gate 2.
4. **The "73% / 89% of coffee roasters" figures are unverified vendor marketing.** I could not trace them to a primary survey. Do not use them.
5. **Two clocks moved during the research window** — Colorado AI Act (delayed *and* gutted) and Spain's Verifactu for autónomos (2026 → 2027) — and the AI Act's own deadlines were extended. On this surface the rule itself is a moving target, and any candidate whose value depends on an unamended rule text should be discounted accordingly.
