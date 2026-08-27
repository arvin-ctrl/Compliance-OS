# Scout 10 — Review-Platform Gap Mining (`category_gap_analytics`)

**Access date for all evidence: 2026-08-27.**

## How I hunted (5-line summary)
Scanned ~15 software categories through review platforms, looking for dominant-but-hated leaders, "too enterprise/too expensive for us" complaints from definable segments, and structurally mediocre categories. WebSearch hit the session cap early, so per the brief I pivoted to direct WebFetch of Capterra/GetApp category grids, product review pages (with reviewer role/size/date), vendor pricing pages, and Bing-as-fallback; G2 and Reddit block direct fetch, so all quotes below are from fetchable review platforms and vendor/state pages. The richest vein by far: **PE/consolidator-owned incumbents repricing captive SMB bases** (insurance AMS duopoly, Katana/Cin7 inventory tier, Personify/WildApricot) and **mandated-but-mediocre platforms** (HHAeXchange EVV, 3.6★). Equally valuable: 8 categories I scanned and KILLED because review data shows the small segment is already well served (list at bottom) — this ground produces negative knowledge other scouts should not re-litigate. 5 candidates cleared the evidence bar; I chose not to pad to 6.

---

## S10-1: Small-agency squeeze in insurance agency management systems (AMS)
- **Who hurts:** 1–10 person independent P&C insurance agencies (owner-principal + a few CSRs; the office manager doubles as the "tech person"). US market widely cited at ~39–40k independent agencies, most under $3M revenue [inference — count not URL-verified this pass].
- **The pain:** Two incumbents (Applied Systems, Vertafore) own every mainstream AMS, including the former SMB favorites (Applied bought EZLynx; Vertafore owns QQCatalyst) [context, widely reported; not URL-verified this pass]. Reviewers report annual price increases (a 50% jump at EZLynx in 2023), multi-hour support holds, rigid multi-year contracts billed for unused seats, and a core built on a "Clunky DB2 database…developed 1989-92". Small principals say the flagship (Epic) is engineered for big brokerages and consumes admin time they don't have.
- **Frequency:** Daily — every policy service touch, quote, carrier download/reconciliation; contract pain recurs at each annual/multi-year renewal.
- **Economics today:** AMS360 ≈ $150–$300/user/mo plus $5,000–$25,000 one-time implementation; solo agent $275–$500/mo all-in; typical $1M–$3M-revenue agency $4,000–$7,000/yr (unlockedcrm.ai breakdown — vendor-adjacent source, labeled as such). One agency president reports being contractually forced to keep paying "over $1,000 per month" ($8,000 total) for capacity it no longer used (Capterra). EZLynx "Pricing increased 50% in 2023" (Capterra, agency principal).
- **Current solutions:** Applied Epic/TAM, Vertafore AMS360, EZLynx (Applied), QQCatalyst (Vertafore); liked-but-smaller independents HawkSoft, NowCerts, Jenesis; tiniest shops run carrier portals + spreadsheets. Sources: Capterra product pages listed in evidence; alternatives named in reviews.
- **Forcing function:** None — discretionary. (Switch windows open only at contract renewal; E&O documentation duties keep agencies captive to *some* AMS, which sustains the duopoly's pricing power.)
- **Why now:** 2021–2025 consolidation converted the affordable tier into duopoly property and repriced it (EZLynx +50% in 2023); reviews dated Dec 2025–Feb 2026 show the resentment is current, and none of the incumbents' AI moves target the 1–10 seat tier.
- **Evidence:**
  1. "the price was high and went up quite a bit every year" — Susan H., Office Manager, 2–10 employees, May 2022 — https://www.capterra.com/p/113472/Vertafore-AMS360/reviews/ (AMS360 overall 3.6/5, 58 reviews; Ease 3.2, Support 3.3)
  2. "when it comes time to get help...no one answers. Again, today, I have been on hold for more than 2 hours" — Kimberly C., Personal Lines Exec, Oct 2020 — same URL
  3. Contract rigidity cost agency "over $1,000 per month", "$8,000 total" — Farrell L., President, 2–10 employees, Oct 2023 — same URL; also "Clunky DB2 database...developed 1989-92 (before the internet)" — Kathryn T., Commercial Account Manager, Oct 2020
  4. "Pricing increased 50% in 2023." / "Support is slow, occurs over email mostly." — Jake I., Agency Principal, Apr 2023 — https://www.capterra.com/p/102928/EZLynx/reviews/ (EZLynx 3.7/5, 75 reviews; Support 3.3)
  5. "Policies were reverting to the pre-renewal info, and just not processing." — Kimberly B., Office Manager, Sep 2025 — same URL
  6. "Definitely more efficient for big business...When the broker/manager is also the tech person...there are lots left undone." — Laura B., Senior Account Manager, 2–10 employees, Dec 2025 — https://www.capterra.com/p/70671/Applied-Epic/reviews/ (Epic 4.2/5, 142 reviews); "It will waste your agency time, not save it." — Mark G., Agent, 11–50 employees, Feb 2024
  7. Price anchors: "~$150–$300/user/month", "$5,000–$25,000+ one-time" implementation, solo agent "$275–$500"/mo — https://unlockedcrm.ai/blog/how-much-does-vertafore-ams360-really-cost (third-party/vendor-adjacent pricing breakdown)
- **Scout's confidence:** HIGH — three separate products' review bases (10+ independent authors, 2020–2026) tell one coherent squeeze story with hard dollar figures; main caveat is that HawkSoft/NowCerts already contest the low end, so the gap is "modern + fairly-priced + no-contract", not "no option exists".

---

## S10-2: Mid-market extraction trap in SMB inventory / light-manufacturing software
- **Who hurts:** Product businesses with 2–20 employees (wholesale/distribution, light assembly, food & beverage and cosmetics makers needing batch/lot tracking) that outgrew QuickBooks/Excel but cannot justify NetSuite.
- **The pain:** All three mid-tier defaults punish the segment they were built for. Katana repriced captive customers ~5x in two years, moved previously included features (batch tracking) into a $199/mo add-on, and per a Feb 2026 reviewer "enforces punitive order-based pricing, changes terms mid-contract, and prioritizes larger customers." Cin7 Core runs a support carousel and raises fees unilaterally. Fishbowl is dated desktop-era tech with an unstable QuickBooks sync and hours of manual re-keying. The workflow is daily and unavoidable: orders in, POs out, BOMs, stock counts, shipping.
- **Frequency:** Continuous/daily operations; vendor repricing events roughly annually (2023, 2024, 2026 incidents quoted).
- **Economics today:** One Katana customer: "from around 100 USD to over 500 USD monthly – a fivefold increase in just two years" plus "batch tracking...an additional 199 USD per month"; another had their plan price doubled with features turned off "all without warning". Cin7: "They've increased fees by $72 per month." Fishbowl: reviewers reference paying "thousands" up front, then "It is getting a little expensive for how we are using it" (Apr 2026). The alternative ceiling is NetSuite-class ERP at tens of thousands per year [inference].
- **Current solutions:** QuickBooks + spreadsheets (what most graduate from — named in Fishbowl/Cin7 reviews); Katana, Cin7 Core (ex-DEAR), Fishbowl, inFlow, Zoho Inventory; NetSuite above. Reviewers report migrating between these repeatedly (Fishbowl reviewers came from QuickBooks Desktop, Excel, Acctivate; Cin7 reviewers from QuickBooks, NetSuite, Sage).
- **Forcing function:** None — discretionary; however the vendors' own mid-contract repricing acts as a recurring eviction notice that forces a migration decision.
- **Why now:** The 2023–2026 repricing wave across the whole tier (documented above) created a migration-ready cohort with fresh, dated receipts; incumbents' per-order/per-module pricing is structurally hostile to small-ticket, high-SKU businesses, and none of the 2024–2026 AI inventory startups target core SMB inventory ops (they sell forecasting to bigger retailers) [inference from category scan].
- **Evidence:**
  1. "they doubled the price of our plan, turned off a number of features we were using to run our business operations, and charged us for 'add-ons' all without warning." — Chris G., CEO, Electrical/Electronic Mfg, Feb 2024 — https://www.capterra.com/p/172888/Katana-MRP/reviews/ (Katana 4.6/5, 171 reviews)
  2. "our expenses on Katana's services skyrocketed from around 100 USD to over 500 USD monthly – a fivefold increase in just two years...batch tracking, previously included, was now a separate add-on costing an additional 199 USD per month...This pricing strategy feels like a trap...exorbitant fees that are unsustainable for a small business." — Monne D., Founder, Food & Beverages (~€300k revenue), Jan 2024 — same URL
  3. "enforces punitive order-based pricing, changes terms mid-contract, and prioritizes larger customers over long-time users." — Andrew M., Owner, 11–50 employees, Feb 2026; "The pricing is expensive and the cancellation policy is terrible." — Erik B., CTO, Machinery, Apr 2026 — same URL
  4. "We've ridden along with several price hikes but at one point enough is enough" — Janet, end user, Apr 2025 — https://softwareconnect.com/reviews/katana-mrp/ (second review platform)
  5. "constantly shuffled from one person to the next and we were never able to get actual answers" — Director of Supply Chain & Ops, Apparel, 11–50 employees, Aug 2025; "recent price hike is unacceptable. They've increased fees by $72 per month" — MD, Consumer Goods, Oct 2024 — https://www.capterra.com/p/133038/Cin7-Core/reviews/ (Cin7 Core 4.3/5, 738 reviews)
  6. "The system can feel a bit outdated and not as intuitive as newer inventory platforms." — Warehouse Manager, Mar 2026; "The mobile app is super slow...I have to spend hours retyping the bin locations." — Lead Product & Design Manager, Jun 2026; "the integration with QuickBooks is not that stable." — CIS Manager, Dec 2025 — https://www.capterra.com/p/123794/Fishbowl/reviews/ (Fishbowl 4.2/5, 1,129 reviews)
- **Scout's confidence:** HIGH — 10+ independent authors across two platforms and three products, with exact dollar deltas and 2024–2026 dates; the pain is priced, recurring, and the segment (small-ticket/high-SKU makers and wholesalers) is explicitly the one the incumbents say they are deprioritizing.

---

## S10-3: Volunteer-run membership organizations squeezed by their post-PE default (WildApricot)
- **Who hurts:** Volunteer-administered membership organizations — professional-association chapters, civic and social clubs, hobby/sports clubs, small education nonprofits — roughly 100–5,000 contacts, run by an unpaid membership manager/treasurer (US/Canada/ANZ).
- **The pain:** WildApricot is the long-standing category default for this segment and is now Personify-owned. Its own review base documents the squeeze: "Multiple large price increases" with "zero product improvement", support reduced to chat links ("Customer service is useless, all they do...is send links to articles"), no live support at all, and pressure toward in-house payments (external processors "may incur additional servicing fees" per the pricing page). The buyers are volunteers: every hour lost to workarounds comes out of evenings, and a $792+/yr bill for a 60-member club is a board-meeting agenda item.
- **Frequency:** Continuous membership ops (joins, renewals, dues chasing, event registration, newsletters); acute shock at each annual price-increase letter.
- **Economics today:** $66.00/mo at just 100 contacts on monthly billing ($59.40/mo annual) from WildApricot's own pricing page; reviewers report repeated large increases on top of prior years' rates; the alternative is a paid management company or more volunteer hours [inference].
- **Current solutions:** WildApricot; MemberClicks (also Personify) [context]; ClubExpress, Join It, Member Jungle, ClubRunner (named by leavers in reviews); many boards run spreadsheets + Mailchimp + PayPal instead.
- **Forcing function:** None — discretionary; the annual renewal/price letter is the recurring switch trigger.
- **Why now:** Post-2021 Personify consolidation degraded the default while its pricing tightened (evidence spans 2021→2025, still current in May 2025 reviews); volunteer admins are exactly the buyer AI-heavy products can serve at a price PE-owned seat/contact pricing can't follow.
- **Evidence:**
  1. "Since purchased by Personify, the support is HORRIBLE and lends itself only to electronic communications." — Dorris H., Webmaster, May 2025 — https://www.capterra.com/p/76116/WildApricot/reviews/ (WildApricot 4.4/5, 556 reviews)
  2. "Multiple large price increases" with "zero product improvement" and "Support is non-existent." — Skip P., Admin, Education Management, Jun 2023 — same URL
  3. "My main issue...is that there is no live support. I just can't accept that there is no way for your company to offer support personel for training." — Frances O., Membership Manager, Civic & Social Organization, Oct 2024 — same URL; also "No response to any of the registration action items that have been requested for YEARS" and "raising their prices!" — Tonya S., Executive Director, Non-Profit, May 2021
  4. "Customer service is useless, all they do when you finally get them on a chat is send links to articles." — Caryn G., Communications Director — https://www.getapp.com/nonprofit-software/a/wild-apricot/reviews/ (second platform)
  5. Pricing page: 100-contact tier = "$66.00/month" (monthly) / "$59.40/month" (annual prepay); "organizations using external payment processors may incur additional servicing fees" — https://www.wildapricot.com/pricing (accessed 2026-08-27)
- **Scout's confidence:** HIGH — two review platforms + the vendor's own price sheet; multi-year complaint arc from the exact segment. Caveat for Manager 1: overlaps ground 01 (PE squeeze); my addition is the review-documented segment definition and price anchor.

---

## S10-4: Independent optometry practices stuck between a payer-owned EHR (3.7★) and $319–365/user/mo alternatives
- **Who hurts:** 1–3 doctor independent optometry practices (2–10 staff) in the US — commonly estimated in the high-teens of thousands of locations [inference — count not URL-verified this pass].
- **The pain:** The category's migration path is owned by the practices' dominant vision payer: VSP's Eyefinity Encompass/EHR scores 3.7/5, with owners reporting "Endless updates that just glitch it further" and that "Ordering glasses is MUCH more time consuming than it was with Officemate" (Eyefinity's own legacy product). The liked specialty alternatives price per doctor at $319–$365/user/mo, and generalist medical PM/EHRs rate mediocre for optometry (DrChrono 3.9, Compulink 4.1, Sightview 4.0). Daily work — exam documentation, optical/lab orders, recalls, vision-plan claims — runs through whichever compromise the practice picked.
- **Frequency:** Per-patient, daily (charting, optical orders, claims); billing rework per encounter.
- **Economics today:** RevolutionEHR $319/user/mo; Crystal Practice Management $365/user/mo; MaximEyes $350/mo (Capterra category listing, accessed 2026-08-27) — i.e., a 2-OD practice pays ~$7.6k+/yr just for PM/EHR, before the staff time lost to glitchy ordering/billing documented in reviews.
- **Current solutions:** Eyefinity OfficeMate (legacy, VSP) and Encompass (cloud, VSP); RevolutionEHR; Crystal PM; MaximEyes; generalist tools (DrChrono, Compulink, Nextech); reviewers report evaluating/moving among RevolutionEHR, Uprise, Compulink, Crystal PM.
- **Forcing function:** Partial — payer-ecosystem dependence (the biggest vision plan owns the software), and cloud-migration pressure off OfficeMate; **no hard sunset deadline verified** (I could not confirm an OfficeMate EOL announcement — do not repeat that claim without a source).
- **Why now:** The forced-to-cloud wave is in progress (reviews compare Encompass unfavorably to the legacy product they left), and no 2024–2026 AI startup targets optometry-specific PM/optical/vision-plan billing [inference from category scan].
- **Evidence:**
  1. "Endless updates that just glitch it further." — Optician, 1–2 yrs use, Aug 2024 — https://www.capterra.com/p/156685/Eyefinity-EHR/reviews/ (Eyefinity Encompass 3.7/5, 68 reviews)
  2. "Ordering glasses is MUCH more time consuming than it was with Officemate." — Optometrist Owner, Aug 2024 — same URL
  3. "too delicate of an equilibrium to be useful, especially with billing." — Optometrist, Aug 2024; "Way too many tabs making it difficult to complete charting with ease." — Optometrist, Aug 2022 — same URL
  4. Category price/rating grid: RevolutionEHR 4.5/5 at $319/user/mo; Crystal PM 4.4/5 at $365/user/mo; MaximEyes 4.4/5 at $350/mo; DrChrono 3.9; Compulink 4.1; Sightview 4.0; Eyefinity Encompass 3.7 — https://www.capterra.com/optometry-software/ (accessed 2026-08-27)
- **Scout's confidence:** MEDIUM — pain artifacts are multiple independent authors but effectively one platform (Capterra product + category pages); Reddit/ODwire corroboration was unreachable through available tooling. Recommend a validator pull r/optometry + ODwire threads before promotion.

---

## S10-5: Small home-care agencies bleeding cash inside state-mandated EVV aggregators (HHAeXchange)
- **Who hurts:** Small licensed home-care agencies (Medicaid personal care / home health services), roughly 2–200 caregivers, in states that designated HHAeXchange as the EVV aggregator or state system (Texas, Pennsylvania MCO network, and others; reviews also name payer mandates via Humana, Wellcare, Sunshine Health, Molina).
- **The pain:** Federal law (21st Century Cures Act) makes electronic visit verification mandatory for Medicaid personal care; many states route ALL of it through HHAeXchange — a platform rated 3.6/5 (customer service 3.1). Agencies report visits that "don't confirm" (double-billing exposure), shifts that vanish so caregivers go unpaid, "Lost over $18000 dollars because of a syntax error in the software", "We didn't get paid for over 4 months", and 3-hour support holds. Billing/coordination staff reconcile every visit between their scheduling system and the mandated portal.
- **Frequency:** Per-visit, daily; caregiver payroll weekly; Medicaid claims each billing cycle — every one gated by EVV match.
- **Economics today:** Direct quotes put single-incident losses at $18,000 and revenue delays at 4+ months; the standing cost is the billing/coordinator labor dedicated to portal reconciliation (typical US billing-coordinator salary $40–55k/yr [inference — not URL-verified]); the aggregator itself is "free" (state-sponsored), which is why agencies can't just leave it.
- **Current solutions:** The free HHAeXchange state portal (mandated); agency-side management systems (AxisCare, WellSky Personal Care, AlayaCare) with varying EVV integrations; manual double-entry between the two; some agencies outsource billing to services [inference].
- **Forcing function:** HARD — federal EVV mandate + state aggregator designation. Non-compliant visits don't get paid. This is the strongest forcing function I found in this ground.
- **Why now:** Aggregator-model rollouts completed across big states in 2023–2025 (Texas: TMHP "partnered with HHAeXchange" as the state-sponsored portal for all Texas providers — vendor/state page below), so the pain is newly universal, structural, and documented; incumbent agency software competes on features, not on making the mandated pipe survivable.
- **Evidence:**
  1. "You can enter visits but it doesn't confirm most times so you are stuff double billing" — Bobbie G., Director of Nursing, 1★ — https://www.capterra.com/p/140366/eXchange-Suite/reviews/ (HHAeXchange 3.6/5, 100 reviews; Customer Service 3.1)
  2. "Lost over $18000 dollars because of a syntax error in the software" — Valerie P., President, 1★ — same URL
  3. "We didn't get paid for over 4 months the beginning of January 2021" — Linda M., CEO — same URL
  4. "I have been on the line for over 3 hrs and also waiting on the chat for a representative for the same amount of time" — Pascual M., Director of Nursing; "Impossible to get someone over the phone, they create tickets and resolve nothing" — ADIS P., Admin, 1★ — same URL
  5. "Shifts worked don't show up so they are not paid" — Kim T., Co-owner, Individual & Family Services, 201–500 employees — same URL; page also references Pennsylvania MCOs, Humana, Wellcare, Sunshine Health, Molina as mandating the platform for EVV
  6. "Texas Medicaid & Healthcare Partnership (TMHP) has partnered with HHAeXchange to help Texas homecare service providers remain compliant with state and federal Electronic Visit Verification (EVV) laws" — state-sponsored, no-cost portal for all Texas providers — https://www.hhaexchange.com/texas (accessed 2026-08-27)
- **Scout's confidence:** HIGH on the pain (multiple independent operator-authors + mandate documentation + hard dollar losses). One structural caveat for validation: the mandated aggregator itself cannot be displaced — the attackable surface is the agency-side layer (scheduling/billing/reconciliation that makes EVV survivable), where the incumbent agency systems are competing on breadth, not on this wound. Overlaps grounds 02/05 — my contribution is the review-documented severity and the platform-monopoly framing.

---

## Categories scanned and KILLED (negative knowledge — do not re-litigate without new evidence)
| Category | Why killed (review data, accessed 2026-08-27) |
|---|---|
| Self-managed HOA software | PayHOA 4.7/5 with 715 reviews — purpose-built, liked, cheap. Segment served. |
| Small pest-control operators | GorillaDesk 4.8/5 (278) at $49/mo + Jobber 4.6 (1,475) at $39/mo. Low end served; PestPac (3.9) hate is real but escape routes exist. |
| Campground/RV park mgmt | Campspot 4.5, CampLife 4.9, ResNexus 4.8, affordable indies (RoverPass, Firefly ~$3.50/mo). Healthy category. |
| Consignment/resale POS | SimpleConsign 4.7 (355), ConsignPro 4.6 (434), Ricochet 4.7 — active and liked. |
| Self-storage small operators | SiteLink 4.7 (452), Easy Storage Solutions 4.8 (703), storEDGE 4.4 — Storable rollup has NOT (yet) degraded ratings. |
| Mental-health group practices | SimplePractice complaints real (price raises "with very little notice", outages) but TherapyNotes 4.7 (969) + funded billing networks serve the segment. |
| Auction software | Charity side saturated with 4.7–4.8 options; live-auctioneer tools (AuctionFlex/HiBid) invisible to review platforms — evidence unreachable, not necessarily absent. |
| Funeral home software | Osiris 4.7, Gather 4.9, Halcyon 4.8, Parting Pro 4.6 — fragmented but healthy. |
| Machine-shop ERP | JobBOSS² 4.2 (866) is mediocre, but ProShop + well-funded Fulcrum already attack it (anti-pattern: swarmed). |
| Portable sanitation/roll-off (ServiceCore 4.0/51) | Complaints are 2021-vintage; funded entrants (Hauler Hero, Docket) now target adjacent waste niches. Watchlist, not candidate. |

## Cross-ground leads for the director (found here, belongs elsewhere)
1. **Ground 02:** US fire-incident reporting NFIRS→NERIS transition (claimed 2025–2026 mandate wave for ~29k fire departments) — surfaced repeatedly but I could NOT verify the deadline through available tooling; needs an official usfa.fema.gov check. Fire RMS side likely swarmed (First Due), but the reporting-migration compliance angle may not be.
2. **Ground 02/11:** Unverified lead that Avalara sunset its "Avalara for Beverage Alcohol" DTC product, which would leave Sovos ShipCompliant near-monopoly for small-winery state filings — could not verify; worth one authoritative check before anyone builds on it.
3. **Ground 01:** WildApricot/Personify (S10-3) and EZLynx/Applied (S10-1) are clean, review-documented specimens of the PE-squeeze pattern that ground hunts.
