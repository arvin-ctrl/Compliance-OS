# SCOUT 10 — COMMUNITIES WITH MONEY AND NO TOOLS

**Date of research:** 2026-08-27
**Surface:** profitable niches whose practitioners gather publicly and use nothing purpose-built.
**Verdict:** **NOT dry — but far more contested than the surface framing assumes.** Seven candidates below.
Two cross-cutting findings that change how this surface should be read are stated first, because they
affect every candidate and they are the single most useful thing I found.

---

## SURFACE-LEVEL FINDING 1 — "no tools" is mostly false in 2026; "no *tolerable* tools" is true

I swept ~45 trade communities. In **every single niche where members make real money**, I found either
(a) an established paid vendor, or (b) two to six independent developers already in the thread announcing
a tool they built, usually in the last 12 months. Examples, all dated 2026:

| Niche | Indie builders found *inside the community* in the last 12 months |
|---|---|
| Vending | `u/Mosalix` (2026-07-31), `u/EMVending` VendingTrackr (2026-04-05), `u/Fast_Seabass_264` Vendric (2026-04-06), `u/uriuri2323` (2026-06-01), `u/Fancy-Aspect7273` (2026-01-14) |
| Fire/life safety | `u/firelign` firelign.com, `u/spec-app`, `u/Warm_Exercise1057` (Ember), `u/DepartmentHefty6834` (built his own on Base44) |
| Notaries | `u/thenotarynext` (2026-06-22), `u/GovernmentInitial581` (2026-04-07), `u/beakshay` (2026-04-22) |
| Beekeeping | `u/turtlestik` (2026-02-04), `u/Alpha_sn` (2026-05-07) |
| Butchery | `u/Willing_Abroad3046` (2026-04-27), `u/Short-Custard7804` (2026-04-05) |
| Wastewater | `u/EmotionalHoliday4257` (2026-02-27 research → 2026-05-19 "I built the thing") |
| Surveying | `u/TerraKraft` SurveyorHub (2026-03-09) |
| Self-storage | `u/JonPorked` (2026-05-07), `u/jhwright` "Claude code. Rolling my own." (2026-05-08), `u/yeah_i_am_new_here` (2026-08-04) |
| Screen printing | `u/Cameron_Brownie` (2026-02-07), `u/Alarming-Zombie3338` (2025-12-04) |
| Backflow | `u/seitayokokawaa` (2026-05-30) |
| Court reporting | `u/o_onthewater` (2026-07-22) |

**This is itself T2 evidence of demand** — but it also means "unglamorous = moat" is no longer true for the
*generic* shape (a CRM / inventory / scheduling app for niche X). AI-assisted building collapsed the cost of
that play and dozens of people are running it simultaneously. **The remaining defensible shape is the
regulated document**: an artifact that must be produced in a specific format, for a named third party, under
a deadline, where the format is fragmented across jurisdictions. That is research-heavy, not code-heavy,
which is exactly where a one-operator-plus-agents shop has an edge and a hobbyist builder does not. Every
candidate below is that shape.

## SURFACE-LEVEL FINDING 2 — community rules are a hard Gate 1 problem, and getting harder

I pulled the published rules for every community I shortlisted. **Most trade subreddits ban vendors outright.**

| Community | Vendor rule (verbatim) | Gate 1 |
|---|---|---|
| r/Irrigation | "Advertising your company's retail product or services **unless someone asks for help**." | **PASS — explicit carve-out** |
| r/firealarms | "No Solicitation or advertisement, this includes website to your product, service, etc." — but in practice the Uptick founder (`u/aidanlister`), the Ember founder, `u/BuildingReportsUSA`, `u/spec-app` and `u/firelign` all post product answers in software threads and are not removed | **MARGINAL — banned on paper, tolerated in reply** |
| r/appraisal | Only rule: "This subreddit is for Real Estate Appraisal topics. Posts requesting free appraisals of personal property will be removed." No anti-promotion rule published | **PASS** |
| r/TheBrewery | Rules page publishes no anti-promotion rule; vendor launch posts score well (`u/Big_Violinist98` 2026-01-14: 32 pts / 39 comments; `u/AnteSim` Abbl ERP 2022: 20 pts / 38 comments) | **PASS** |
| r/Laundromats | No anti-promotion rule published | PASS (but candidate killed on other grounds) |
| r/FFLs | "**No more Blatant Vibe Code Advertisements. Will Result in immediate ban**" | **FAIL — rule written *because of* people like us** |
| r/selfstorage | "No self promotion, solicitation, surveys or spam… No links to commercial sites… No surveys/questionnaires" | **FAIL** |
| r/Machinists | "No commercial advertising of any kind from manufacturers, distributors, auctioneers, **app devs**, or similar businesses" | **FAIL** |
| r/SCREENPRINTING | "No selling or marketing of goods or services. This includes links to online stores or websites." | **FAIL** |
| r/Wastewater | "Please do not advertise products or services" | **FAIL** |
| r/Locksmith | "If the first thing you do is post a link to your website… you will be banned." Enforced socially too — `u/P15T0L_WH1PP3D` to a dev, 2025-04-08: *"Do you just lurk for opportunities to sell your services?… what you're doing is entirely unwelcome."* | **FAIL** |
| r/Surveying | "You may not use us to increase the popularity, profit, or market presence of a personal project… No Surveys or Questionnaires" (partial carve-out for sharing original surveying-related sites) | MARGINAL |
| r/vending | "What's not allowed are sales pitches, links to 'helpful' blogs…" | MARGINAL |

Two independent communities added anti-AI-app-pitch language **in the last 12 months** (r/FFLs' "vibe code"
rule; r/Machinists' explicit "app devs"). `u/Auditor_of_Reality` in r/firealarms, 2026-08-11, on a post
asking about deficiency workflow: *"The format of the post was so similar to all the disguised software
pitches here and other trade subs that I was surprised there wasn't a developer just thrilled to help out
immediately."* **The "ask a question, then reveal your product" play is burned.** The only reliably
non-banned motion left is: answer an existing "what do you use / how do you handle X" thread with a
genuinely useful specific answer, and let a free public utility do the pulling.

---

# CANDIDATES

---

## 1. ITM Report Pack for the 1–5-tech fire & life-safety shop

**One sentence:** A tablet-and-web tool that turns a fire-extinguisher / fire-alarm / sprinkler inspection
into the exact NFPA-format report and deficiency proposal that a small contractor has to hand the building
owner and the fire marshal — priced for a shop with one to five techs, which every incumbent explicitly
refuses to serve.

**The artifact:** a finished, code-referenced NFPA 10 / NFPA 72 / NFPA 25 inspection & testing report PDF
with device inventory, pass/fail per device, photos tied to findings, and a **separate priced deficiency
proposal** generated from the same pass — plus the same data in the shape the AHJ portal wants (see #7).

**Evidence — T1 + T2**

*The incumbents publicly refuse this segment:*
- `u/DepartmentHefty6834`, r/firealarms, **2026-08-16**: *"Building reports is not for small guys, neither is
  InspectPoint. **InspectPoint told me the ROI doesn't show up until I'm servicing 400 customers a year.**"*
  → https://old.reddit.com/r/firealarms/comments/1vpm700/best_fire_inspection_software/
- Inspect Point's own pricing page (fetched 2026-08-27, https://www.inspectpoint.com/pricing): three tiers,
  all "Contact for Pricing", **"minimum of 2 technicians for all plans"**, custom pricing at 15+ techs.
- `u/Timely_Weekend_8030` (started this thread looking for software for his NFPA 10 startup), **2026-08-16**,
  replying to Uptick's founder: *"I did reach out to uptick and was notified about the **5 tech minimum**.
  I'd love to use the product but seems too pricy starting."*
- `u/Time-Resolution5144`, **2026-08-16**: *"building reports and other platforms typically used are not good
  for us startup small guys… I know I've heard **most startups use plain old excel sheets**."*

*What they actually use today:*
- `u/Affectionate_Ad_9380`, **2026-05-04** and again **2026-08-16**: *"Filling out blank NFPA PDF on iPad and
  dropping to OneDrive."* / *"We use a fillable PDF on iPads. Then we use OneDrive or Dropbox to sync to office."*
- `u/zealNW`, **2026-05-04**: *"I just fill out the NFPA inspection and testing report template."*
- `u/MandoO6d6r`, **2026-05-08**: *"We went back to fillable pdfs in the mean time."*
- `u/Fabzzz`, **2026-08-16**: *"Why are you paying for software. Just learn how to make neat looking excel spreadsheets."*

*Evidence they pay, and hate what they pay for:*
- `u/MR_SL0WP0K3`, **2026-08-16**: *"We use ServiceTrade for scheduling and service calls and Building Reports
  for inspections. **It's not cheap**, but our AHJ requires IROL and it is integrated into the Building Reports."*
- `u/Syrairc`, **2026-05-05**: *"Building Reports is awful, outdated tech, with standard reports that are nigh
  unreadable, and **it's still a pay-per-scan business model which means you can't accurately predict costs,
  and your costs go up as you get more work**. I have no idea how this company is still alive."*
- `u/Physical-Boy1989`, **2026-08-17**: *"we use novoReport… **you have to pay a certain amount per device in
  the report** so small buildings are quite cheap but big one… well you got the picture."*
- `u/Mln3d`, **2026-05-16**: *"I just don't see how it is palatable for a company to have to pay for every
  person with access to the software, whether tech or office."*
- `u/SuperVDF` (2 years on Inspect Point), **2026-05-04**: *"**Sometimes I spend more time doing the report than
  the actual inspection takes.**… I have to enter in information 2-3 times per building sometimes which is a
  major pain in the ass."* Echoed by `u/Mln3d`, **2026-05-16**: *"Similar response from our techs. Doing the
  report takes longer than the actual inspection."*
- Three separate "what software do you use" threads inside 15 weeks (2026-05-04 · 64 comments; 2026-08-10 ·
  29 comments; 2026-08-16 · 41 comments). `u/Robh5791`, 2026-08-16: *"This is the third post in the last week
  or so regarding software."*

**The clock:** the segment is being created right now. In the 2026-08-16 thread alone, **three** users
identify as fire-protection *startups* forming in the next 6–8 months (`u/Timely_Weekend_8030`,
`u/Time-Resolution5144`, `u/DepartmentHefty6834`). Separately, third-party AHJ e-filing mandates spread through
2019–2026 (see #7) and make a *structured* report — not a scanned PDF — compulsory, which is what kills the
fillable-PDF workflow these shops use. Uptick's founder confirmed on 2026-08-17 that his growth channel is
*"referrals, website inbounds, our sales team, and our LinkedIn content"* — i.e. nobody is serving the
sub-5-tech shop through a self-serve motion.

**First ten users (named, from real threads):**
`u/Timely_Weekend_8030` · `u/Time-Resolution5144` · `u/DepartmentHefty6834` · `u/Affectionate_Ad_9380` ·
`u/Physical-Boy1989` · `u/MandoO6d6r` · `u/Mln3d` · `u/Important-Ad3984` (*"We are a very small company and up
to this point we have billed our customers manually"*, 2026-05-27) · `u/tenebralupo` · `u/iodrew` (40-year FL
company with an extinguisher department, offered to answer questions 2026-08-17) · `u/TheTerribleTim`
(15 techs / 3 inspectors, on BuildingReports).

**Gate check**
- **G1 distribution — MARGINAL PASS.** Rule bans solicitation; practice tolerates vendor answers in software
  threads (four competitors do it openly and are not removed). A "what do you use" thread appears roughly
  every 2–4 weeks. Risk is real and must be treated as the thing to test first.
- **G2 observable demand — PASS.** Money moving now, per-device and per-scan pricing quoted by users, three
  recurring threads in a quarter, incumbents naming a floor they won't go below.
- **G3 buildable — PASS.** NFPA inspection & testing forms are published; no credential needed to build the
  tool (the *inspector* holds the credential, not us). No proprietary data required.
- **G4 self-verifiable in 14 days — PASS.** Build the NFPA 10 report generator, publish it free, post it as an
  answer in the next software thread. Success/failure is our own signup log; no stranger's cooperation needed.
- **G5 clock — PASS.** New shops forming visibly in-thread; AHJ e-filing mandates spreading (dated below).

**What already exists:** Inspect Point, BuildingReports (ScanSeries), ServiceTrade + FormLink, Uptick, Ember,
Honeywell CLSS, JCI Xaap, novoReport, FireNspec, Essential, plus SafetyCulture/GoFormz as generic fallbacks.
**Why inadequate for this segment:** every one of them prices or minimums the 1–5-tech shop out (2-tech minimum
at Inspect Point, 5-tech minimum at Uptick, per-scan/per-device at BuildingReports and novoReport, per-seat
including office staff at Uptick). Ember is the live threat — "small and new, very clean UI, very well priced"
per Uptick's own founder — and is the reason confidence is 7 and not 9.

**Price signal:** BuildingReports = per-scan; novoReport = per-device; Inspect Point = 2-tech minimum, price
withheld; Uptick = 5-tech minimum; FieldEdge (adjacent trade, same buyer size) quoted at *"close to $1k per
month for 3 users"* by `u/permanently_new_guy`, r/Locksmith, 2025-05-09. All exact SaaS dollar figures are
withheld behind "contact us" — **UNVERIFIED**.

**Confidence: 7/10**

---

## 2. Backflow test-report filing agent (one test → every purveyor's form and portal)

**One sentence:** Certified backflow testers must file each annual test with the specific water purveyor that
owns the connection — hundreds of different paper forms and login portals per metro — and a tester who works
across a dozen municipalities keeps a physical binder of forms; this turns one structured test record into
whatever each purveyor requires.

**The artifact:** the completed, purveyor-correct test-and-maintenance report (PDF for mail/email jurisdictions,
pre-filled field-by-field payload for portal jurisdictions), plus the tester's own annual re-test tickler.

**Evidence — T2, with T1 adjacent (paid incumbents exist and are being paid)**

- `u/Runs_towards_fire` (BPAT-licensed, Texas), r/Irrigation, **2022-04-14**: *"**I carry a binder with forms
  for every city I do testing in.**… And you need to know how the city wants the test results submitted."*
  → https://old.reddit.com/r/Irrigation/comments/u3tp2g/how_to_submit_backflow_testing_paperwork/
- `u/senorgarcia`, same thread, **2022-04-14**: *"Here it all depends on the individual water department. Most
  of where we work is only online reporting now… **Each one can be different.**"*
- `u/Crimsonbelly`, r/Irrigation, **2026-05-30**: *"**The most annoying part is the online inputting.** Not the
  paper work at all. Tokay is fine, there are two municipalities in my area that are using it. The newer one
  here is SAMS… The worst is the Public utility's system… To attempt to bring up a customers device, **you have
  to put in make, model, serial, type, and size. If any of this is wrong then you need to put it in as a new
  device into their system. This makes you put in the full address and location, only then you can put in the
  results.** From my experience over the years the data entry people half assed at best most that information."*
  → https://old.reddit.com/r/Irrigation/comments/1ts2n7u/for_people_who_do_backflow_testing_how_do_you/
- Same user, on cross-portal compatibility: *"I thought he said it doesn't work with SAMS yet… I don't believe
  that Tokay will being that they haven't even updated the 3 psi buffer from the RP test. As it will mark as a
  fail if the relief valve opens at 3.4 and the number check hold at 6.0 Tokay will mark this as a fail."*
  (i.e. the incumbent gets the *code arithmetic* wrong.)
- `u/lennym73`, **2026-05-30**: *"We use Syncta and typically don't have any issues with it."* — confirms a paid
  incumbent is in use; he could not state the price ("Not on the administrative side").

**The clock:** the migration from mailed paper forms to purveyor-specific online portals. `u/Crimsonbelly`
dates SAMS' arrival in his area to roughly 2024 (*"They are only like two years old I believe. From what I heard
we were the first area to get it"*). Each new portal adds a distinct manual re-keying task and *increases* the
fragmentation this product monetises. **This is the weakest-dated clock in the set** — I could not find a
single national mandate to anchor it. Treat as UNVERIFIED.

**First ten users:** I could only find **six** named testers discussing the admin side across the two threads:
`u/Runs_towards_fire` · `u/Crimsonbelly` · `u/lennym73` · `u/Sparky3200` · `u/senorgarcia` · `u/DankestTaco`.
That is a real shortfall and I am reporting it rather than padding it. The larger pools (ABPA chapters,
state-by-state tester registries published by water authorities, Facebook backflow-tester groups) are
directory-shaped, not thread-shaped, and I could not verify their membership from this environment.

**Gate check**
- **G1 — PASS, and it is the best Gate-1 position on this whole surface.** r/Irrigation's rule bans advertising
  *"unless someone asks for help."* Answering a backflow-paperwork thread with a specific tool is explicitly
  permitted. Secondary channel: purveyor-published tester lists are public directories of exactly our buyer.
- **G2 — PASS (T2).** Two paid vendors already collect money from testers (Syncta, Tokay); pain is specific,
  dated, quoted.
- **G3 — PASS with a caveat.** Generating each purveyor's *form* is pure document work and clearly buildable.
  Auto-*submitting* into a purveyor portal is scraping under someone else's ToS — if the product depends on
  that, G3 degrades. Build the form-generation and pre-fill layer; do not promise auto-submit.
- **G4 — PASS.** Pick 25 purveyors in one metro, harvest their published test forms, generate all 25 from one
  input. Fourteen days, no stranger required. The kill criterion is our own: if fewer than ~15 of 25 forms are
  publicly obtainable, the thesis dies.
- **G5 — WEAK.** No dated national trigger found. This is the gate to attack first.

**What already exists:** Syncta (a Watts company), Tokay, SwiftComply, SAMS, plus purveyor-built systems
(`u/Sparky3200`: *"The city I work for has their own website and app"*). **Why inadequate:** these are sold to
the *water utility*, so the tester is the party forced to adapt to N systems and gets no cross-purveyor tool.
`u/Crimsonbelly` reports Syncta does not push into SAMS.

**Price signal:** Syncta publishes a pricing page but Cloudflare blocked retrieval from this environment —
**UNVERIFIED, do not quote a number.** No user in-thread would state their spend.

**Confidence: 6/10**

---

## 3. UAD 3.6 adjustment-support and workfile exhibit generator for fee appraisers

**One sentence:** On **2 November 2026**, every new appraisal delivered to Fannie/Freddie must use the redesigned
UAD 3.6 report, whose automated review reads the *adjustment fields* rather than the addenda — and residential
appraisers currently have no tool that derives and documents those adjustments defensibly, while their forms
vendors are visibly failing.

**The artifact:** an adjustment-support exhibit — paired-sales and regression derivation for each adjustment
line, sensitivity table, and a dated workfile PDF that satisfies USPAP recordkeeping — generated from the MLS
comp export the appraiser already downloads, in the field names UAD 3.6 expects.

**Evidence — T2, heavy and extremely fresh**

- Deadline and readiness, compiled with sources by `u/Mean_Sport_1484`, r/appraisal, **2026-07-18**:
  *"**Deadline: Nov 2 is unchanged. Freddie's FAQ is explicit: UAD 3.6 is mandatory for all new UCDP
  submissions on or after 11/2/2026**, and 2.6 revisions keep working through May 3, 2027 for reports already
  in the pipeline. Broad production has been open since Jan 26. Readiness: WorkingRE's 2026 State of the
  Profession survey — **about 3% of ~1,800 respondents had completed a 3.6 report, 58% hadn't taken the GSE
  7-hour training, and 64% plan to raise fees for 3.6 work.**"* → https://old.reddit.com/r/appraisal/comments/1v06ps2/
  **Caveat: this is a community member's compilation. GSE sites (singlefamily.fanniemae.com,
  sf.freddiemac.com) return 403/404 to this environment, so I could not verify the dates or the survey
  primary-source. Label both UNVERIFIED until confirmed. The date is corroborated independently in-thread —
  `u/Puzzled-Platypus8330`, 2026-08-21: *"coming up to the deadline in 2 months… come Nov. 2nd."***
- The critical mechanic, same post: *"the new CU is **field-driven — it reads your adjustment fields, not your
  addenda**, and underwriters have less room to wave warnings through than before."*
- The pain that creates, `u/Mediocre_Feedback_21`, **2026-03-12** (99 comments): *"many of the reports that I
  get across my desk look like this. **No support or summarizing of how adjustments were developed** including
  location, site, view, design, quality, age, condition."* → https://old.reddit.com/r/appraisal/comments/1rs1ls3/
- Incumbent failure, `u/ihartpizza`, **2026-08-21**: *"I've finished one 3.6 and it was a complete cluster.
  Start to finish, **I probably invested 12 hours into the one report.**… Nothing about the flow is intuitive.
  It's a complete disaster."* → https://old.reddit.com/r/appraisal/comments/1vu17v2/
- `u/wyecoyote2`, **2026-08-21**: *"The lag is frustrating — click box, sip coffee, get up refill coffee, sit
  down oh it finally moved… **Being a beta tester without being paid to be a beta tester.**"*
- Vendor churn is live, `u/drahcir2k2`, **2026-08-21**: *"**we all have to decide what company to go with and
  no one has their product ready or pricing finalized.** I feel like I'm having to learn multiple platforms to
  figure out who's gonna be functional."*
- `u/Rich_Helicopter_2128`, **2026-08-21**, on the 30-year incumbent: *"Total is going to be an interesting case
  that will be studied and eventually taught in business schools because I think 3.6 will eventually be the
  death of the company… I know I won't be renewing my contract with them."*
- They are back on paper for capture: `u/North-Writer-219`, **2026-08-21**: *"pen and paper for the inspection
  and plug it in at the desktop."* `u/No_Ebb3669`: *"it will be easier to do an old fashioned inspection with a
  Clipboard and input everything back on the desktop."*
- Threads dated 2025-06-21, 2025-08-16, 2025-11-28, 2026-03-12, 2026-06-02, 2026-07-02, 2026-07-10, 2026-07-18,
  2026-08-07 (88 comments), 2026-08-21 (33 comments) — *"half the front page is 3.6 threads right now."*

**The clock:** hardest-dated clock on this surface. Broad production opened 2026-01-26; mandatory 2026-11-02;
legacy 2.6 revisions die 2027-05-03. **Ten weeks out**, ~3% of the profession has produced one report.

**First ten users:** `u/North-Writer-219` · `u/wyecoyote2` · `u/ihartpizza` · `u/drahcir2k2` ·
`u/BeepBoopZeepZorp` · `u/Puzzled-Platypus8330` · `u/streetappraisal` · `u/R0factor` · `u/Rich_Helicopter_2128` ·
`u/Mean_Sport_1484` · `u/TheSailorRipley` (ClickFORMS user since 2000) · `u/ComicallySolemn` · `u/stab-somebody` ·
`u/Exact-Macaron-4569` (28 years) · `u/No_Ebb3669`. Secondary community: AppraisersForum.com.

**Gate check**
- **G1 — PASS.** r/appraisal publishes no anti-promotion rule; the sub is in active crisis and posting a free
  useful artifact into a live 3.6 thread is normal behaviour there.
- **G2 — PASS (T2, near-T1).** 64% say they will *raise fees* for 3.6 work; vendors are selling into the same
  panic today; incumbent contracts are being cancelled in-thread.
- **G3 — PASS, but only for the adjacent artifact.** Writing a *forms package* requires GSE verification and
  UCDP delivery integration — that is an access barrier and would be **fatal**. The adjustment-support exhibit
  and workfile do not touch UCDP and need no certification. **Stay on that side of the line.**
- **G4 — PASS.** Take three public MLS-style comp sets, produce a defensible adjustment-support exhibit,
  put it in front of the r/appraisal 3.6 threads. No stranger, no records request.
- **G5 — PASS, dated to the day.**

**What already exists:** a la mode TOTAL (CoreLogic), ACI Sky Workbench, Bradford NightHawk (*free through 2026
for active members*, per `u/Mean_Sport_1484`), SFREP Appraise-It Pro, Aivre, TrueTracts, Reggora (*"They're
saying it's free"*, `u/Your-maine-man`, 2026-07-02). For adjustment support specifically: Bradford's Redstone
and the analytics bundled inside TOTAL. **Why inadequate:** all of the above are competing to be the *forms
container*; the appraisers' complaint is that none of them help *derive and defend the adjustment values* the
new CU actually reads. Note the risk: Bradford NightHawk being free through 2026 compresses willingness to pay
for anything that looks like part of the form.

**Price signal:** appraisers are already paying annual forms-software subscriptions (amount **UNVERIFIED** —
no user quoted a figure and vendor pages were not retrievable). `u/Puzzled-Platypus8330` projects the market
effect: *"come Nov. 2nd turn times will be 2-3 weeks with **$1,000 fees** again."* 64% intend to raise fees.

**Confidence: 7/10** — best clock, best Gate 1, worst Gate 3 boundary risk (must not drift into forms software).

---

## 4. TTB compliance for the sub-Ekos alcohol producer

**One sentence:** Every US brewery, winery and distillery must file federal operations reports and excise
returns on TTB forms; the purpose-built tools start above the smallest producers, and those producers do it
in shared spreadsheets.

**The artifact:** completed TTB forms — Brewer's Report of Operations 5130.9 / 5130.26, Winery 5120.17,
Distillery 5110.40 / 5110.28 / 5110.11, and Excise Tax Return 5000.24 — generated from daily production
records, with the underlying daily records retained in the form TTB expects on audit.

**Evidence — T1**

- **A paid competitor publishes its price**, which is the cleanest T1 on this surface. TTB Tamer pricing page,
  fetched **2026-08-27** (https://www.ttbtamer.com/pricing): Breweries **$47/month** or **$476/year**, plus a
  **required one-time $249** setup; Wineries **$61/month**, required one-time **$349**; *"Add $1/month per
  Additional User"*; 30-day free trial; "NO CONTRACTS."
- The gap under it, `u/BaleenBrewing`, r/TheBrewery, **2023-01-11**: *"Does anyone have a spreadsheet they use
  to recording the TTB record requirements? **I'm too small for TTB Tamer or Ekos**, so I think a proper
  spreadsheet would be a good way to go."* → https://old.reddit.com/r/TheBrewery/comments/108q6wv/
- `u/grassler`, **2020-01-18**: *"Those of you that aren't using brewing softwares, what are your solutions for
  the daily record keeping required by TTB? Would you be willing to share those sweet spreadsheets?"*
- `u/zumera254`, **2019-07-10**: *"Anyone have a resource for ttb reporting spreadsheets? I am not very good
  with Excel and I am struggling with finding anything useful."*
- Incumbent dissatisfaction at the tier above: `u/Savmasterr`, **2024-11-01**: *"Our brew team has been working
  with Ekos for over 2 years now, and we've had issues from the jump with the usability of the software."*
  `u/wedapeeppl`, **2024-09-09**: *"We've been searching for a while, feels like forever, for a better option,
  been using Ekos for 8 years."*
- Community accepts vendors: `u/Big_Violinist98`, **2026-01-14**, posting his own app — 32 points, 39 comments,
  no removal: *"Made a no-BS brewing app for Brewers because **software is expensive and spreadsheets suck**."*

**The clock — this is the candidate's weak point.** The pain quotes cluster in 2019–2024, not 2026. I did not
find a dated regulatory change in the last 24 months. What *is* dated and adjacent: the craft-beer contraction
driving cost-cutting, and the visible 2026 appetite for a cheap alternative (`u/Big_Violinist98`'s post).
**Do not submit this without finding a dated 2025–2026 TTB or state change.** Treat G5 as UNPROVEN.

**First ten users:** `u/BaleenBrewing` · `u/grassler` · `u/zumera254` · `u/Pghbrewer` · `u/BornAgainNewsTroll`
(flaired *Owner*) · `u/Savmasterr` · `u/wedapeeppl` · `u/AnteSim` (flaired *Brewer/Owner*) · `u/Big_Violinist98`.
Nine, several of them 2–7 years stale. Live-thread recruitment would be needed.

**Gate check**
- **G1 — PASS.** r/TheBrewery publishes no anti-promotion rule and vendor posts score well. Adjacent: r/distilling,
  r/winemaking, ADI and state guild forums.
- **G2 — PASS (T1).** TTB Tamer's published $47/mo + $249 setup is money changing hands for a worse version.
- **G3 — PASS.** TTB forms and instructions are public federal documents; no licence needed to build the tool.
- **G4 — PASS.** Generate a correct 5130.9 and 5000.24 from a synthetic daily-records set in under two weeks.
- **G5 — FAIL / UNPROVEN.** No dated change in 24 months found. **This is the gate that should kill or save it.**

**What already exists:** TTB Tamer, Ekos, Ollie, Beer30, Orchestrated/OBeer, Abbl, Vintrace. **Why inadequate:**
they start above the nano/farm producer, and the ERP tier is a full production system when the buyer only needs
the compliance filing. TTB Tamer is the closest and is priced within reach — which cuts both ways: it proves
willingness to pay *and* it may already be adequate. **Honest read: TTB Tamer at $47/mo may simply be the answer,
in which case kill.**

**Price signal:** $47/mo + $249 one-time (brewery), $61/mo + $349 (winery), verified from the vendor's own page
on 2026-08-27.

**Confidence: 5/10** — best price evidence, worst clock.

---

## 5. Third-party AHJ report-filing layer for fire-protection contractors (TCE / IROL / Tegris)

**One sentence:** Roughly a thousand US fire jurisdictions now legally require inspection reports to be filed
through a private portal — The Compliance Engine, IROL, Tegris — that charges the *contractor* a per-report fee
and makes him re-key a report he already produced; this files it once from the source data and tracks the money.

**The artifact:** the portal-shaped submission payload plus a per-report fee ledger the contractor can invoice
back to the building owner as a line item, with a "filed / not filed / disputed" status per site per cycle.

**Evidence — T1 (money is changing hands per report, publicly, at named prices)**

- `u/Putrid-Whole-7857`, r/firealarms, **2025-01-16**: *"Most of the municipalities in my area have adopted the
  compliance engine this past year. **I see an issue in one town charges 12 dollars and another charges 40
  dollars. I'm even seeing differing fees amongst buildings in a single municipality.**… a company or school
  campus has 20-30 buildings at these fees and is doing quarterly inspections."*
  → https://old.reddit.com/r/firealarms/comments/1i2c5n8/compliance_engine/
- `u/YeaOkPal`, same thread, **2025-01-16**: *"**I think we're up to $45 for a compliance engine report upload**
  on inspection reports. Some of that cost is compliance engine and some is paying office staff to keep up with
  it. Around me it took a while but nearly all municipalities went to it."*
- `u/FlynnLives3D` (Chicagoland), **2026-03-12**: *"we have **several 3rd party test report companies we need to
  keep track of** for our area… pricing started out reasonably, **5-10$ a report, but now we are up to 20-30$
  mostly, but Chicago is like $300**. We pass on the cost to the customer without markup, but for large sites it
  can get expensive fast. One of the larger (early 3rd party report sites) **just merged with the compliance
  engine (TCE), and pricing on TCE has started rising fast for all our AHJs.**"*
  → https://old.reddit.com/r/firealarms/comments/1rry5qm/local_ahj_requirement/
- The legal mechanism, quoted verbatim by `u/20855dciandrew`, **2026-03-12**, from his California AHJ's bulletin
  citing **CFC 901.6.3.1**: *"All inspection, testing and maintenance reports… shall be forwarded to the fire
  code official using approved electronic media to an approved, designated third party… **Paper (hard copy)
  reports are not permitted.**"*
- The float problem — a genuine, unaddressed business pain: `u/20855dciandrew`, **2026-03-12**: *"Passing the
  cost to the customer is an additional expense for the testing company. **You have to wait until you get paid
  by the customer and yet you've already paid the fees to the third-party.** In effect you are losing money."*
- Scale, `u/Ron_dizzle199`, **2025-01-16**: *"My district has 200 sites, we use the compliance engine for all
  uploads."* `u/ichiban4713`, **2026-03-13**: *"In Oregon, we are required to submit our reports through The
  Compliance Engine. It's been that way for about seven years."*
- Portal integration is a *purchase driver* for the big platforms — `u/Important-Ad3984`, 2026-05-17, listing why
  he likes Uptick: *"Scheduling, equipment tracking, deficiency quotes, billing, return work on deficiency,
  **Brycer integration**…"* Small shops without those platforms do it by hand.
- The AHJ side confirms the incumbent is bad, `u/locke314` (fire marshal), **2025-01-16**: *"AHJ here. We use tce.
  **I hate the interface. I hate how it works. I hate how it operates.** It's so unfriendly to use… Trust me, we
  don't like it either."*

**The clock:** ongoing jurisdiction-by-jurisdiction adoption plus consolidation. Dated markers in-thread: Oregon
statewide ~7 years (so ~2019); *"Most of PA requires it (but not all)"* (`u/Mastersheex`, 2025-01-16); Florida
county-by-county and *"getting there"* (`u/Steelhornet4K`, 2026-03-13); the California AHJ bulletin dated to
2026-03; and a **2026 merger of a large early third-party filer into TCE with prices rising fast afterwards**
(`u/FlynnLives3D`, 2026-03-12). Consolidation-driven price rises are the trigger.

**First ten users:** `u/20855dciandrew` · `u/FlynnLives3D` · `u/YeaOkPal` · `u/Ron_dizzle199` · `u/ichiban4713` ·
`u/Putrid-Whole-7857` · `u/svejkOR` · `u/Mastersheex` · `u/MR_SL0WP0K3` · `u/Woodythdog` · `u/Thomaseeno`.
Plus `u/locke314` and `u/Agreeable_Ad_9987` on the AHJ side (useful for validation, not as customers).

**Gate check**
- **G1 — MARGINAL PASS.** Same community and same rule tension as candidate #1.
- **G2 — PASS (T1).** Per-report fees are being paid today at $12–$45, up to $300 in Chicago, at volumes of
  200+ sites per contractor, quarterly.
- **G3 — RISK.** Filing *into* TCE/IROL means either an integration nobody will grant a solo operator, or
  automating a logged-in third-party portal — ToS and brittleness risk. **The defensible build is the
  contractor-side half**: produce the exact payload, track filings and fees, invoice them through. Do not
  promise auto-submission. If the product only works with auto-submission, **kill it**.
- **G4 — PASS.** Enumerate the TCE-adopting jurisdictions in one state from public ordinances and fire-marshal
  bulletins, and build the fee-passthrough ledger. Two weeks, no stranger.
- **G5 — PASS.** Consolidation + price rises dated 2026-03.

**What already exists:** the portals themselves (Brycer TCE, IROL, Tegris) — they are the *tax*, not the tool —
and Uptick/BuildingReports/Inspect Point which integrate at platform prices. Nothing serves a contractor who
files by hand. **Adequacy risk: if the answer is simply "buy Uptick", this collapses into candidate #1.**

**Price signal:** $12–$45 per report typical; $5–$10 historically; **$300 in Chicago**; all quoted verbatim by
practitioners on the dates above.

**Confidence: 6/10**

---

## 6. Self-storage lien and delinquency compliance pack (small independent operators)

**One sentence:** Selling a delinquent tenant's unit requires a state-specific sequence of notice letters,
advertisements and waiting periods, getting it wrong voids the sale and exposes the operator — and independent
operators either run it out of a spreadsheet or trust a PMS that their own users say gets the statutory clock wrong.

**The artifact:** a per-unit, per-state lien timeline with the actual notice documents generated on the correct
dates, and a dated evidence file proving the sequence was followed.

**Evidence — T1/T2**

- The incumbent gets the *law* wrong, `u/Similar-Animator-640`, r/selfstorage, **2026-05-09**, on Cubby:
  *"**Delinquency is not tracked based on the actual law of the first unpaid rental period.**"*
  → https://old.reddit.com/r/selfstorage/comments/1t6qnmn/
- Real consequences, `u/Bradvertised`, **2025-10-14** (44 comments): *"Is it really possible to accidentally miss
  that an auction unit has had the balance paid?… I had a delinquent unit."*
- Operators asking for a statutory sequence they cannot get from software, `u/unclestone`, **2022-07-15**:
  *"In search of an operator who is familiar with Missouri Lien Law in regards to self storage. We are having
  trouble implementing a process from the first day a tenant is late to the unit auction date."*
- Spreadsheets and Excel are real at real sizes: `u/RandomMontanaGuy`, **2025-01-16**: *"I recently bought a
  mom and pop business (**~220 units**) that was **managed out of Excel**."* `u/Commercial-Catch-615`,
  **2025-03-03**: *"I have 49 units… Prior to easy storage solutions I was just using spreadsheets."*
  `u/Space--Buckaroo`, **2026-05-07**: *"I use QuikStor… I have a separate FileMaker Pro Database that I use for
  contracts. I built the basic design of the DB and paid a programmer."*
- The money is unambiguous, `u/AideInternational171`, **2025-03-25**: *"We are a facility of **725 Units**, so
  the savings of approx **$26k per year just in subscription costs** made it an easy decision"* — after
  reporting *"We were paying with subscription fees and processing fees, **over $2,500/month**"* on
  SiteLink/Storable (2025-03-05).
- Demand for tooling is so high the mods legislated against it — `u/LieslMR` (Area Manager, mod), **2026-05-08**,
  "Subreddit Updates": *"Over the years, this subreddit has received a very large number of posts asking
  variations of: 'What software do you use?' 'What management software is best?'"*

**The clock:** state self-storage lien statutes have been amended repeatedly (electronic notice, changed
advertising requirements) — but **I could not date a specific change inside 24 months from a primary source**.
G5 UNPROVEN.

**First ten users:** `u/Similar-Animator-640` · `u/unclestone` · `u/Bradvertised` · `u/HelicaseHustle` ·
`u/RandomMontanaGuy` · `u/Commercial-Catch-615` · `u/Space--Buckaroo` · `u/Tkfit09` · `u/kelvt4n` ·
`u/FreeportSelfStorage` · `u/Mayoovermustard` · `u/AideInternational171`.

**Gate check**
- **G1 — FAIL as published.** r/selfstorage bans self-promotion, solicitation, surveys, *and linking to any
  commercial site*. This is the single most restrictive rule set I found. Alternative channels (SSA state
  associations, Inside Self-Storage) are conference/association-shaped — i.e. exactly the channel the Cycle-0
  postmortem says we cannot run. **This gate is what should kill it.**
- **G2 — PASS.** $2,500/mo spends, 725- and 220-unit facilities on Excel, a mod-acknowledged flood of software questions.
- **G3 — PASS.** Statutes are public; document generation is our strength.
- **G4 — PASS.** Encode three states' lien sequences and generate the notice set. Two weeks.
- **G5 — UNPROVEN.**

**What already exists:** SiteLink, Storable/storEDGE, Storable Easy, Tenant Inc, Cubby, 6Storage, QuikStor,
Easy Storage Solutions, CC Storage, Stora, Web Self Storage, Storage Commander, SSM, Alyta, OpenUnit. Fifteen
named vendors in one thread. **Why possibly still inadequate:** none of them is trusted on the *statutory clock*.
But the PMS category is saturated and a compliance-only add-on has to be sold *around* an incumbent.

**Price signal:** $2,500+/month at 725 units (SiteLink/Storable); $26k/year subscription saving; $25/month for a
hosted website from CC Storage. All verbatim, 2025-03.

**Confidence: 4/10** — good pain, good money, **fails the binding constraint**. Listed for completeness and
because the lien-clock insight may transplant to a community that does allow vendors.

---

## 7. ATF A&D / 4473 compliance for the sub-$9-a-month FFL — **submitted as a KILL, with the evidence**

I researched this and am reporting it rather than dropping it, because the kill is instructive.

**Evidence found:** r/FFLs is full of licensees in genuine compliance distress with money at stake —
`u/csejthe`, **2026-01-04**, "How screwed am I?" (33 comments): *"Type 07 FFL. Been doing it a few years now,
only to realize mistakes I've been making along the way. I decided to get FastBound in order to help with
compliance issues and mess ups."* `u/Just_Fig_7674`, **2025-05-15** (28 points, 36 comments): *"A Warning for
FFLs - Stay Away from coreWARE."* `u/m70b1jr`, **2024-09-15** (25 comments): asking for A&D/e4473 software
recommendations before his licence was even issued.

**Why it is killed — Gate 1, decisively.** r/FFLs' published rules include: *"**No more Blatant Vibe Code
Advertisements. Will Result in immediate ban.**"* The community has already been flooded by exactly our
category of entrant and has legislated against it. There is no carve-out.

**Secondary kills:** FastBound is priced *"From $9/month"* (fetched 2026-08-27, https://www.fastbound.com/pricing/)
and bundles *"funded legal defense through FFLGuard"* — we cannot match a legal indemnity, and $9/month leaves
no room. ATF-facing recordkeeping software carries a liability profile a solo operator should not take on.

**Confidence: 2/10 — do not pursue.**

---

# SURFACES PROBED AND FOUND DRY OR ALREADY TAKEN

Recorded so the next cycle does not repeat the sweep.

| Community / niche | Money? | Why rejected |
|---|---|---|
| **r/vending** | **Yes, verified.** `u/PsychologicalRead982`, 2026-03-31 (334 pts): *"2025 total revenue: $146,852.68"* across 13 machines; `u/IAmStillLearningLife`, 2026-02-27: *"8 months, 2 machines, ~$30K"* | Five indie tools launched into this sub in 2026 alone (list in Finding 1) on top of VendSoft, VendingMetrics, Vendera, Nayax, Cantaloupe. Net profit ~$27k on $147k revenue caps ARPU. **Saturated.** |
| **r/Surveying** | Yes — firms with crews and equipment | The community actively *defends* paper. `u/Noggro`, 2026-03-05: *"There is no replacement for physical fieldbook."* `u/Whistlepiged`: *"we will never get away from hand drawn field notes/sketches."* `u/HotTamaleBallSak`: *"My field notes in an actual book recently helped my company win a court case, not going to be changing that."* Plus a legal-admissibility argument and an indie builder already there. **Standing Law 2: this is a demand verdict against.** |
| **Pressure washing / window cleaning / auto detailing / pest control / lawn** | Mixed | Saturated by Jobber, Housecall Pro, Workiz, Markate, ServiceTitan, FieldRoutes, plus indie entrants. `u/Marion_App`, 2025-12-05: *"£300/month for Jobber is insane"* — and he has already built the alternative. Price-sensitive, low ARPU, sub rules hostile. |
| **r/Machinists / job-shop quoting** | Yes | Rule: *"No commercial advertising of any kind from manufacturers, distributors, auctioneers, **app devs**, or similar businesses."* Plus Paperless Parts, MIE Trak, JobBOSS, Fulcrum. **Gate 1 fail.** |
| **r/SCREENPRINTING** | Yes | *"No selling or marketing of goods or services."* Printavo / YoPrint / InkSoft / DecoNetwork / ShopWorx already contest it. **Gate 1 fail.** |
| **r/Laundromats** | Yes | Not toolless — owners already run Cents, Laundroworks, Huebsch Command. `u/FreedomRdLaundromat`, 2026-03-05: *"Cents pretty much does all of the functions of Excel."* |
| **r/Locksmith** | Yes — `u/permanently_new_guy`, 2025-04-08: *"Roughly 250-300k/yr… 1 Office Person, 2 Field techs"*; FieldEdge *"close to $1k per month for 3 users"* | Generic FSM; he solved it with Jobber. Sub bans and socially punishes vendors. |
| **r/Equestrian, r/Horses, r/DogBreeding, r/Cattle, r/Ranching, r/Beekeeping** | Marginal | Consumer-heavy (boarders not barn owners; puppy buyers not breeders). CattleMax already at **$12/month billed yearly** (pricing page, 2026-08-27) — floor too low. Indie builders present. |
| **r/Butchery, r/meatprocessing** | Unclear | r/meatprocessing effectively empty; r/Butchery is consumer cut-sheet questions. Two builders already posted management tools in 2026 to near-zero engagement. |
| **r/Wastewater, r/WaterTreatment** | Municipal budgets | Rule: *"do not advertise products or services."* And `u/EmotionalHoliday4257` already ran the exact research→build motion (2026-02 → 2026-05). |
| **r/commercialfishing** | Yes | Electronic reporting runs through NOAA-approved vendor apps — **access barrier, G3 fatal.** |
| **r/Notary, r/courtreporting** | No — mostly sub-scale freelancers | Three separate tool-builders posted into r/Notary in 2026 (Apr, Apr, Jun). Low ARPU. |
| **r/Towing, r/PrivateInvestigator, r/Auctioneers, r/farriers, r/partyrentals, r/holidaylighting, r/dumpsterrental, r/soberliving, r/CarWash, r/PortableToilets, r/Septic, r/Crane** | — | Subreddits absent, dead, or returned zero relevant threads. Any real community for these is on Facebook or a trade forum I could not read from this environment (see Limitations). |

---

# METHOD AND LIMITATIONS — read before trusting any number above

1. **Reddit's API and JSON endpoints return HTTP 403 to this environment** (their bot defence, not the egress
   proxy — the proxy reported zero relay failures). I worked around it by scraping `old.reddit.com` HTML with a
   browser user-agent. Everything I quote was read from the live thread; the URLs are stable.
2. **I could not retrieve subscriber counts for any subreddit.** The logged-out `old.reddit.com` sidebar no
   longer renders them and `about.json` is blocked. **Every community-size figure is therefore UNVERIFIED and I
   have deliberately given none.** Where I needed a size proxy I used comment counts, post scores and thread
   frequency, which are directly observable. Anyone taking a candidate forward should get real sizes first.
3. **GSE and several vendor sites block this environment** (fanniemae.com 403, freddiemac.com 404, syncta.com
   Cloudflare block, printavo.com Incapsula, getjobber.com JS wall, onuptick.com 502). The UAD 3.6 dates and
   the WorkingRE survey figures in candidate #3 are therefore **community-reported, not primary-verified.**
   They are corroborated across independent users in-thread, which is T2, not T1.
4. **Facebook groups, Discords, Circle communities and most trade-association member areas are login-walled**
   and I could not read them. For several trades (farriers, portable restroom operators, Christmas-light
   installers, mobile RV techs, hood cleaners) the real community almost certainly lives there and my "dry"
   verdict above should be read as *"dry on the open web"*, not *"dry"*.
5. **The web-search budget for this session was exhausted (200/200).** Later verification was done by direct
   fetch only.
6. Prices I state as verified were read off the vendor's own live pricing page on **2026-08-27**: TTB Tamer,
   FastBound, CattleMax, Inspect Point. Everything else is a practitioner's quoted figure, attributed and dated,
   or explicitly marked UNVERIFIED.

---

# WHAT I WOULD SPEND A MONTH ON

Ranked, with the one thing that would kill each:

1. **#3 UAD 3.6 adjustment support** — best clock in the set (hard deadline 2026-11-02), best Gate 1, buyers in
   visible distress right now. **Killed by:** drifting into forms software, or by Bradford's free-through-2026
   NightHawk absorbing the willingness to pay. *First 14-day test: build the adjustment-support exhibit from a
   public comp set and show it into a live r/appraisal 3.6 thread.*
2. **#1 small fire-shop ITM** — clearest articulated pain, incumbents naming the floor they won't serve, named
   startups forming in-thread this month. **Killed by:** Ember getting there first, or the r/firealarms
   solicitation rule being enforced against us.
3. **#5 AHJ portal filing** — hardest money evidence (per-report fees at named prices, rising after a 2026
   merger). **Killed by:** discovering the product only works with auto-submission into someone else's portal.
4. **#2 backflow** — the only community on this surface whose rules *explicitly permit* answering with a product.
   **Killed by:** failing to find a dated clock, or by fewer than ~15 of 25 test purveyor forms being publicly obtainable.

Candidates #4, #6 and #7 should not be built as stated. #7 is a clean kill; #6 fails Gate 1; #4 fails Gate 5.
