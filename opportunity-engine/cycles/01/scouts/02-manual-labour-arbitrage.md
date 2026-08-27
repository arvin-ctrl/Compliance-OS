# SCOUT 02 — MANUAL-LABOUR ARBITRAGE

**Surface:** freelance / productised-service marketplaces as a revealed-price, revealed-volume list of tasks.
**Collected:** 2026-08-27. All prices, review counts and delivery times below were read off the live pages on that date.
**Verdict:** surface is **wet**. 9 candidates submitted, 5 killed at the bench, 6 categories confirmed already collapsed.

---

## METHOD & ACCESS NOTES (so the next cycle doesn't repeat the work)

| Source | Access | Notes |
|---|---|---|
| **Fiverr** | ✅ via `r.jina.ai` text proxy | Direct curl → 403. `https://r.jina.ai/https://www.fiverr.com/search/gigs?query=X` returns gig title, star rating, **review count**, "From $X", and URL. Gig pages additionally return the **full 3-tier package table with delivery times** and **dated reviews with the buyer's price band**. This is the single richest source found. |
| **Upwork** | ❌ | Cloudflare CAPTCHA on both direct curl and the text proxy, incl. the `/freelance-jobs/` SEO pages. Demand-side (job-post) data unavailable this cycle. |
| **PeoplePerHour** | ⚠️ partial | `/services?q=` renders via proxy but offer cards are client-side. |
| **Freelancer.com** | ✅ | `/jobs/?keyword=` renders project text via proxy. |
| **Reddit** | ❌ | 403 on `.json`, `old.reddit`, and via the proxy. Could not name buyers from Reddit this cycle. |
| **Amazon Seller Forums** | ❌ | Publicly reachable but thread list renders client-side; no titles/usernames extractable. |
| **WebSearch tool** | ❌ | Session budget (200/200) already exhausted before this scout started. All corroboration below is direct-URL fetch. |

**Review counts ≠ order counts.** Fiverr review counts are a *fraction* of completed orders (typical review rate is well under 100%; the exact ratio is **UNVERIFIED**). Every count below is therefore a **floor** on orders, not an estimate of them. Reported verbatim, never scaled.

---

## THE HEADLINE FINDING

Marketplace pricing splits sharply into three regimes, and the split is the whole signal:

1. **Collapsed** — mechanical work that software already does end-to-end. Price floor $5–$25, 1-day delivery, 600–900 reviews. Transcription, nutrition labels, blog articles, vectorising. *Nothing to build here.*
2. **Arbitrage band ($95–$600, 1–5 day delivery, 100–520 reviews)** — work that is document-shaped and rule-governed, where **the paid labour is the intake, not the judgement**. Someone reads a PDF, extracts structured facts, and reformats them against a published ruleset. This is the band worth attacking.
3. **Relationship-mediated ($1,500–$20,000, or no published price at all)** — SOC 2, CMMC, Amazon reinstatement *agencies*. Riverbend Consulting publishes **no price at all** on its services page (verified 2026-08-27, https://riverbendconsulting.com/services/ — "Standard Appeal: Appeal letter delivery: Four business days or less"; pricing is quote-only via phone 877-289-1017). Unreachable cold.

**The cleanest tell for band 2:** where a *self-serve software tool already exists and is 4–10× cheaper than the human service*, and people still pay the human. That gap is pure intake labour and it is exactly what an agent can eat.

> **Cool Calc** (ACCA Manual J software): "**$50 /user/mo**" Pro with "Unlimited Manual J", or Personal "**$45 /project**" (verified 2026-08-27, https://www.coolcalc.com/).
> **Fiverr Manual J service** for the same deliverable: **$200 / $280 / $400**, 496 reviews.
> The software is not the bottleneck. Typing the house into the software is the bottleneck. That $155–$355 delta is the arbitrage, and it is a vision-model problem.

---

# SUBMITTED CANDIDATES

---

## 1. USPTO Trademark Office-Action Response Pack

**One sentence:** A small-business owner who filed their own trademark and got refused pastes in their serial number and receives a filing-ready Office Action response with the argument, the evidence exhibits and the amended goods/services description already assembled.

**The artifact:** A TEAS-ready response document set — (a) the substantive argument keyed to the exact statutory ground the examiner cited, (b) an amended identification of goods/services conformed to the USPTO ID Manual, (c) a disclaimer/specimen-substitute block where applicable, (d) an evidence exhibit PDF. Delivered as a paste-and-file package plus a one-page "here is what the examiner actually asked for" explainer.

**Evidence — T1 (marketplace, published prices + revealed volume).** All verbatim, all read 2026-08-27:

| Gig title (verbatim) | Price | Reviews | Delivery | URL |
|---|---|---|---|---|
| "I will file response to trademark or patent office action" | **From $95** (Basic $95 / Standard $250 / Premium $350) | **232** · 5.0★ | **5 days** (2 days +$20) | https://www.fiverr.com/rehan87/file-response-to-trademark-or-patent-office-action |
| "I will respond to a uspto trademark office action" | **From $275** (Basic $275 / Standard $500 / Premium $995) | **163** · 4.9★ | **4 days** / 14 days / 90 days | https://www.fiverr.com/lawyer4u/respond-to-a-uspto-office-action |
| "I will respond to uspto office actions" | **From $125** | **121** · 5.0★ | — | https://www.fiverr.com/arabicfantasy/respond-to-uspto-office-actions |
| "I will deal with trademark office action refusals" | **From $95** | **120** · 5.0★ | — | https://www.fiverr.com/rehan87/deal-with-trademark-office-action-refusals |
| "I will fix your trademark office action" | **From $375** (Basic $375 "Minor USPTO Procedural Response" / Standard $500 / Premium **$600** "Refusal Response") | **106** · 4.9★ | **3 days** / 5 days / 7 days | https://www.fiverr.com/dmorganlaw/respond-to-your-uspto-trademark-procedural-response |
| "I will help in responding to trademark office actions or objections" | **From $40** | **105** · 5.0★ | — | https://www.fiverr.com/shahabghori2/help-in-responding-to-uspto-trademark-office-actions |
| "I will respond to uspto trademark office action professionally" | **From $150** | **92** · 5.0★ | — | https://www.fiverr.com/shahmas/write-legal-contracts-and-terms-of-service |
| "I will file responses to office actions from US trademark office" | **From $250** | **20** · 4.9★ | — | https://www.fiverr.com/trademarkguy/respond-to-office-actions-from-us-trademark-office |

Verbatim package-table row from `dmorganlaw`: `| Package | $375 **Basic****Minor USPTO Procedural Response** | $500 **Standard****Several USPTO Procedural Response** | $600 **Premium****Refusal Response** |` — and the tier text: *"I will fix your minor procedural response and fix deficiencies. **No representation. US only.**"* That last phrase is the product boundary already drawn by the market: **document preparation without representation is a sellable product.**

`lawyer4u` dated reviews with buyer price bands: "3 weeks ago … $400-$600", "4 weeks ago … $400-$600", "1 month ago … $200-$400". Money moved this month.

**T1 corroboration — productised service with a published flat fee:**
> **Trademark Engine**: "Office Action responses start at **$599**, depending on the complexity of the issues raised by the USPTO. Additional USPTO filing fees may apply in some cases." — verified 2026-08-27, https://www.trademarkengine.com/office-action-response

The adjacent market is also thick, which tells you the buyer population is large: "I will file your trademark with the uspto" **From $375, 228 reviews** (https://www.fiverr.com/lawyer4u/file-your-trademark-with-the-uspto-f66a); "I will perform comprehensive trademark searches with clear risk reports" **From $35, 540 reviews** (https://www.fiverr.com/shahabghori2/search-your-trademark-and-advice-you-on-its-registrability); "I will help with trademark registration USA, UK, eu or canada and search" **From $90, 494 reviews** (https://www.fiverr.com/alinagh/register-your-trademark-in-the-uk-and-eu).

**The clock:**
- **18 January 2025** — USPTO's restructured trademark fees took effect: base application **"$350 per class"**, plus a **"$100"** surcharge for insufficient information, **"$200"** for using the free-form text box, and **"$200 each"** for additional character groups (verified 2026-08-27, https://www.uspto.gov/dashboard/trademarks/). These surcharges specifically penalise non-standard identifications of goods — the single most common trigger for a procedural office action. The fee structure now charges you *at filing* for the thing that later gets you refused, which raises both the salience and the cost of getting the ID wrong.
- **First Action Pendency target: "5 months from filing"**, total pendency **"11 months or less, on average"** (same source). A refusal lands ~5 months after filing, when the applicant has already spent money and is emotionally committed — a good moment to sell a fix.
- **USPTO developer platform consolidated onto `data.uspto.gov`** — `https://developer.uspto.gov/api-catalog/tsdr-data-api` now returns **301 → https://data.uspto.gov/home** (verified 2026-08-27). The public data surface was re-platformed inside the last ~24 months.

**First ten users — named, and the list refreshes weekly:**
This is the strongest Gate-1 story on the whole surface. **The USPTO publishes, by name, every applicant who has just been refused.** Every application's prosecution history — including the office-action mailing event, the mark, the goods/services, the refusal ground, the correspondent's name and address, and *whether an attorney of record exists* — is public in TSDR. The exact ICP is **US-domiciled applicants with no attorney of record who received an office action in the last 30 days**; they are the ones legally permitted to act pro se and the ones with no lawyer already billing them.
- TSDR API endpoint confirmed live and key-gated: `https://tsdrapi.uspto.gov/ts/cd/casestatus/sn########/info.xml` returned **HTTP 401** on 2026-08-27 (i.e. it exists and needs a free registered key, not that it's closed).
- Public search front end: https://tmsearch.uspto.gov/ · data platform: https://data.uspto.gov/home
- **UNVERIFIED:** whether applicant *email addresses* are exposed or masked in TSDR (USPTO restricted email visibility at some point after the 2019 mandatory-email rule; I could not confirm current state without search). Postal correspondent address and applicant name are public regardless, and the mark itself hands you the business's website. **This must be checked in hour one** — it changes the outreach channel but not the targeting.
- Named individual sellers proving the demand exists, reachable today: `rehan87`, `lawyer4u`, `dmorganlaw`, `arabicfantasy`, `trademarkguy`, `shahabghori2`.

**Gate check:**
- **G1 cold-start distribution — PASS (strong).** A public, government-maintained, weekly-refreshing list of named people who *just* acquired the exact problem, filtered to those with no lawyer. No audience, no ads, no intro required.
- **G2 observable demand — PASS.** 8 sellers, 959+ reviews between them, $40–$995, reviews dated within the last month. Plus a $599 published flat fee from a productised competitor.
- **G3 buildable by us — PASS with one real risk.** Public data + document generation, squarely in our wheelhouse. **Risk: unauthorised practice of law.** The product must be sold as *document preparation the applicant files themselves*, never as representation — which is exactly the line `dmorganlaw` already draws in its own $375 tier ("No representation"). Foreign-domiciled applicants are required to use a US attorney (2019 USPTO rule) and must be excluded from the funnel. **This is a legal-structuring problem, not an access problem** — it does not fail G3, but it is the thing most likely to kill the candidate on closer inspection.
- **G4 self-verifiable in 14 days — PASS (strong).** Pull N office actions from TSDR, generate N responses, and grade them against the *actual responses that were later filed and are also public in TSDR*, plus the recorded outcome. A closed-loop, ground-truthed accuracy test needing zero strangers. This is the best 14-day test on the board.
- **G5 the clock — PASS.** Fee restructure 18 Jan 2025; data platform migration to data.uspto.gov within 24 months.

**What already exists:** Trademark Engine at $599 (attorney-mediated, slow, upsell-driven); LegalZoom (page 404'd on the URL I tried — its current office-action offering is **UNVERIFIED**); dozens of $95–$600 Fiverr freelancers. **Why inadequate:** all of them are *reactive* — they wait for a refused applicant to go looking. None of them ingest the office action and pre-compute the response. Nobody is using the public refusal feed as a demand feed. The incumbent's price is 6× the marginal cost of the artifact.

**Price signal:** **$95–$600** for the worse, hand-typed version. Productised flat fee $599. Modal Fiverr tier ~$275.

**Confidence: 8/10.** Deducted for the UPL question and for not having verified office-action *volume* (see below).

**Unverified and load-bearing:** the number of office actions issued per year. USPTO publishes pendency and quality targets on the dashboard but not a raw office-action count in the content I could retrieve. **This is a one-hour check and must be done before any build.** Do not let this become the postmortem's "foundational number that did not exist."

---

## 2. Marketplace Account-Reinstatement Appeal Pack (Amazon / Walmart / TikTok Shop / Google Ads)

**One sentence:** A seller whose account or listing just got suspended uploads their suspension notice and their order/invoice records, and gets back a root-cause analysis and Plan of Action written in the exact structure the platform's appeal reviewer is scoring against.

**The artifact:** Root Cause Analysis + Corrective Actions + Preventative Measures document in the platform's expected format, an evidence index mapping each claim to a supplied invoice/screenshot, and a standing SOP annex (which is what the top seller upsells as the Premium tier).

**Evidence — T1, verbatim, 2026-08-27:**

| Gig title (verbatim) | Price | Reviews | Delivery | URL |
|---|---|---|---|---|
| "I will write amazon appeal letter plan of action suspension reinstatement" | **From $295** — Basic **$295** "Amazon Appeal + POA" / Standard **$340** "Priority Reinstatement Appeal" / Premium **$370** "Complete Reinstatement Package" | **517** · 5.0★ | **3 days / 2 days / 1 day** | https://www.fiverr.com/tscharr22/write-a-amazon-suspension-appeal-letter-and-plan-of-action |
| "I will write amazon appeal letter and plan of action for suspension and asin" | **From $180** | **171** · 4.9★ | — | https://www.fiverr.com/seooptimisation/help-you-reinstate-or-reactivate-your-amazon-account |
| "I will write amazon suspension reinstatement appeal letter" | **From $190** | **150** · 4.3★ | — | https://www.fiverr.com/ivorycapsuk/write-amazon-suspension-reinstatement-appeal-letter-poa |
| "I will write appeal,poa for amazon account suspension reinstatement" | **From $45** | **139** · 4.7★ | — | https://www.fiverr.com/hannanhanif443/write-amazon-deactivated-suspended-appeal-letter-poa-to-reinstate-your-account |
| "I will write amazon suspension appeal letter plan of action account asin reinstatement" | **From $100** | **53** · 4.5★ | — | https://www.fiverr.com/amazonics1/write-amazon-suspension-appeal-letter-plan-of-action-account-asin-reinstatement |

**The category generalises across platforms — same seller, same artifact, different logo.** From `tscharr22`'s own gig list (verbatim "From$" values, same page, 2026-08-27):
- TikTok Shop suspension appeal — **From $255** (https://www.fiverr.com/tscharr22/write-tiktok-shop-suspension-appeal-letter-tiktok-account-reinstatement-appeal)
- Walmart account suspension appeal — **From $190** (https://www.fiverr.com/tscharr22/write-walmart-account-suspension-appeal-letter)
- Amazon withheld-funds release appeal — **From $180** (https://www.fiverr.com/tscharr22/appeal-to-release-withheld-funds-from-amazon-account)
- Google Ads / AdWords account suspension appeal — **From $150** (https://www.fiverr.com/tscharr22/appeal-google-ads-adwords-account-suspension)
- Counterfeit / hijacker / IP-infringement report — **From $150** (https://www.fiverr.com/tscharr22/report-counterfeit-amazon-listing-hijacker-infringement-brand-protection)

Dated review, verbatim, "2 days ago", buyer price band **$200-$400**: *"Tyler did an outstanding job on my Amazon reinstatement appeal. I've dealt with account issues before and written appeals myself, but I've never seen this level of depth and structure — a full root cause analysis, a precise timeline of every invoice and communication, a detailed compliance control matrix…"* — **that review is a product spec.** Timeline-of-invoices assembly and a compliance control matrix are both mechanical given the seller's own data.

A second dated review, "2 weeks ago", is the counter-argument and should be read as such: *"Writing an Amazon appeal is not a big deal—anyone can write a Root Cause and Corrective Actions. What really matters is knowing how to approach each situation, understanding what Amazon expects…"* — i.e. the seller himself claims the value is tacit pattern-knowledge, not the document.

**T1 corroboration — the agency layer refuses to publish a price.** Riverbend Consulting lists "Amazon 3P Seller Account Suspension Appeal", "ASIN Suspension Appeal", "Brand Registry Appeal", "Kindle Direct Publishing Appeal", "Standard Appeal — Appeal letter delivery: Four business days or less", "Rapid Appeal — As quickly as 1 business day", and **no pricing whatsoever** (verified 2026-08-27, https://riverbendconsulting.com/services/). Quote-only, phone-gated. That is the relationship-mediated tier this candidate would undercut.

**The clock: UNVERIFIED.** I could not establish a dated change in Amazon's enforcement or appeal process within 24 months without search access. **This is the candidate's weakest gate and it is not a small weakness** — a category with no clock is a category someone could have built at any point in the last eight years.

**First ten users — WEAK, and I will say so plainly.** Suspended sellers are, by construction, *not publicly listed anywhere*. I could not extract a single named buyer:
- Amazon Seller Forums (https://sellercentral.amazon.com/seller-forums/discussions/t/account-health) is publicly readable but renders thread titles client-side — nothing extractable.
- Reddit (r/AmazonSeller, r/FulfillmentByAmazon) returned **403 on every access path** including the text proxy.
- The only names I can hand you are **sellers of the service**, not buyers: `tscharr22`, `seooptimisation`, `ivorycapsuk`, `hannanhanif443`, `amazonics1`.
There is a plausible route — a suspended ASIN disappears from search while the brand's own site still lists it, which is externally detectable — but that is **an untested inference, T4, and I am not counting it.**

**Gate check:**
- **G1 — FAIL as it stands.** Cannot name ten buyers. Demand is real and urgent; the buyers are invisible. Recoverable only if the "suspended-listing detection" idea survives contact with reality, which is itself a 14-day test.
- **G2 — PASS (strong).** 517 reviews at $295–$370 on one gig; ~1,030 reviews across the five listed; a whole product line replicated across four platforms.
- **G3 — PASS.** Document generation from seller-supplied invoices and a suspension notice. No access barrier.
- **G4 — PARTIAL.** We can generate appeals in 14 days; we **cannot** learn whether they get accepted without real suspended sellers, because the ground truth lives inside Amazon. Outcome quality is unverifiable alone.
- **G5 — FAIL (unverified).** No dated change identified.

**What already exists:** Riverbend, eGrowth Partners and a long tail of Fiverr freelancers. **Why inadequate:** priced at agency rates or quote-gated; 1–4 day turnaround on a problem where every day is lost revenue. **But the incumbents are adequate enough** — a $295 3-day human service with a 5.0 rating over 517 orders is not obviously a bad deal.

**Price signal:** **$45–$370** (Amazon), **$150–$255** (Google Ads / TikTok / Walmart).

**Confidence: 5/10.** Best raw demand signal on the surface; worst distribution story. G1 and G5 both fail. **My recommendation is to hold this on the watchlist rather than build it**, unless the suspended-listing-detection idea proves out.

---

## 3. Manual J / S / D Load Calculation From an Uploaded Floor Plan

**One sentence:** An HVAC contractor uploads the PDF floor plan they were given and gets back a permit-ready ACCA Manual J load calculation, Manual S equipment selection and Manual D duct layout — without anyone re-typing the house into load-calc software.

**The artifact:** A permit-submittable Manual J/S/D report PDF: room-by-room heating and cooling loads, envelope assembly schedule, equipment selection against the load, and a duct layout drawing.

**Evidence — T1, verbatim, 2026-08-27:**

| Gig title (verbatim) | Price | Reviews | Delivery | URL |
|---|---|---|---|---|
| "I will do manual j d and s load calculations with duct design" | Basic **$200** (<2000 sq ft) / Standard **$280** (2000–3500) / Premium **$400** (3500–5000) | **496** · 5.0★ | **4 days**, "Revisions: Unlimited" | https://www.fiverr.com/moman327/manual-j-d-s-duct-hvac-system-design-load-calculation-layout-heating-cooling-ac-41b6 |
| "I will do a manual j and s block load calculation" | **From $100** | **156** · 5.0★ | — | https://www.fiverr.com/moman327/do-hvac-block-load-calculations |
| "I will perform hvac acca manual j, d and s calculations" | **From $190** | **137** · 4.9★ | — | https://www.fiverr.com/hvac_report/perform-manual-j-d-and-s-calculations |
| "I will calculate hvac manual j heating and cooling loads for your residential" | **From $75** | **109** · 5.0★ | — | https://www.fiverr.com/engr_usama_khan/design-infinity-edge-swimming-pool-plumbing-heating-and-filtration-system |
| "I will do manual j and s load calculations" | **From $100** | **78** · 5.0★ | — | https://www.fiverr.com/jorge4816/do-manual-j-s-and-d |
| "I will do hvac acca manual j d and s load calculations with duct design" | **From $85** | **66** · 4.9★ | — | https://www.fiverr.com/anas_aav/do-hvac-design-with-manual-j-d-and-s-load-calculation |
| "I will do manual j, manual d, and manual s **for city permit**" | **From $20** | **62** · 4.9★ | — | https://www.fiverr.com/engr_muzi/do-manual-j-manual-d-and-manual-s-for-city-permit |
| "I will perform hvac manual j d s load calculations **for city permit**" | **From $75** | **61** · 5.0★ | — | https://www.fiverr.com/engr_usama_khan/calculate-hvac-cooling-and-heating-loads-using-hap-for-commercial-residential |
| "I will provide a manual j using wrightsoft" | **From $200** | **25** · 5.0★ | — | https://www.fiverr.com/tiffanymorri226/provide-an-acca-approved-manual-j-and-s |
| "I will do manual j load calculation **for permit in 24 hours**" | **From $90** | **3** · 5.0★ | — | https://www.fiverr.com/dmitriyre/do-manual-j-load-calculation-acca-certified-and-permit-ready |

Note the Basic/Standard/Premium tiers are **priced purely by square footage** — $200 / $280 / $400 for identical scope. That is the seller pricing *intake labour by volume of geometry to re-type*, which is precisely the confession we are looking for. `hvac_report` dated reviews: "3 weeks ago … $100-$200", "1 month ago … $100-$200", "1 month ago … $400-$600".

**The adjacent energy-compliance work is the same shape and the same buyer:** "I will do rescheck comcheck for energy code compliance for permits" **From $100, 36 reviews** (https://www.fiverr.com/nauman_mep/do-rescheck-comcheck-for-energy-code-compliance-for-permits); "I will make commcheck and rescheck energy compliance certificate" **From $90, 15 reviews**; "I will prepare california title 24 energy reports for city permit approval" **From $250, 4 reviews** (https://www.fiverr.com/arifkhan226/do-hvac-design-for-offices-and-restaurants); "I will do title 24 energy compliance report for california" **From $150** (https://www.fiverr.com/nauman_mep/title-24-t24-energy-compliance-report-for-residential-buildings). Same contractor, same permit packet, three more line items.

**T1 corroboration — the software/service price gap, which is the entire thesis:**
> Cool Calc: Pro "**$50 /user/mo**" with "Unlimited Manual J"; Personal "**$45 /project**" including "Manual J". "built on ACCA's trusted Manual J, S, and D - the gold standard for HVAC design." — verified 2026-08-27, https://www.coolcalc.com/

**Software: $45/project. Human doing the same job: $200–$400.** The 4–9× spread is the takeoff labour. A vision model reading a floor-plan PDF into a geometry schedule collapses it.

**The clock: PARTIALLY UNVERIFIED.**
- ✅ Verified today: multi-modal document-to-structured-geometry extraction is newly reliable — that is the capability change, and it is squarely within the last 24 months.
- ❌ **UNVERIFIED:** the specific code adoption that makes Manual J mandatory at permit. The gigs themselves say "**for city permit**" in the title (three separate listings above), which is strong circumstantial evidence that AHJs are demanding it — but I could not pin a dated code cycle without search. **Verify the IECC/IRC adoption timeline before building.**

**First ten users — NAMED and reachable, with a caveat.** HVAC contractors are a *publicly enumerated population*: every US state maintains a searchable licensed-contractor registry, and many municipal permit portals publish the applicant name on every issued mechanical permit. You can build a list of contractors who pulled a residential mechanical permit last month, by name, from public records.
- Named individuals proving the trade exists today: `moman327` (496 reviews), `hvac_report`, `jorge4816`, `engr_usama_khan`, `tiffanymorri226`, `dmitriyre`, `anas_aav`, `nauman_mep`.
- **Caveat against the brief's discriminator:** the contractor is the payer and the submitter, but is buying *on behalf of* a homeowner's permit. It is not agency-mediated — the contractor personally needs the artifact to get their own job inspected — but it is one step removed from "the person whose problem it is."

**Gate check:**
- **G1 — PASS (moderate).** Public licence registries and permit records name the buyers. Requires outbound to a trade that is not natively online; not a fail, but not free either.
- **G2 — PASS (strong).** 496 reviews at $200–$400 on one gig; 1,190+ reviews across ten; the whole category is priced by square footage.
- **G3 — PASS.** Floor-plan PDF → geometry schedule → Manual J calculation. Vision + arithmetic + a published standard. Exactly our shape.
- **G4 — PASS.** Take 30 published floor plans, extract geometry, run the load calc, and reconcile against Cool Calc / an existing report at $45/project. Ground truth is purchasable for pocket change. No strangers.
- **G5 — PARTIAL.** Capability clock verified; regulatory clock unverified.

**What already exists:** Wrightsoft/MiTek, Elite RHVAC, Cool Calc, LoadCalc.net — all of which *do the calculation* and none of which *do the takeoff*. **Why inadequate:** they present the contractor with an empty room-by-room data-entry form. That form is why 496 people paid $200 instead of $45. **Risk:** ACCA operates a software-approval programme and some AHJs require an approved-software output — whether our report is accepted, or whether we must generate *into* an approved tool, is **UNVERIFIED and is the single most likely killer.**

**Price signal:** **$75–$400** human; **$45/project or $50/user/month** software.

**Confidence: 7/10.**

---

## 4. Licensure Policy-and-Procedure Manual Pack (Home Care / Residential Care / Healthcare)

**One sentence:** Someone opening a home-care or residential-care agency needs a state-specific policy-and-procedure manual to get licensed, and today pays a freelancer $25–$350 to write one.

**The artifact:** A state-specific, licence-application-ready policy and procedure manual, employee handbook, job descriptions, and the required forms/checklists set — generated against the actual state licensing regulation text.

**Evidence — T1, verbatim, 2026-08-27:**

| Gig title (verbatim) | Price | Reviews | URL |
|---|---|---|---|
| "I will write home care policy and procedures manual ndis employee handbook health care" | **From $15** | **61** · 4.9★ | https://www.fiverr.com/zainjadoon545/home-care-policy-and-procedures-manual-ndis-employee-handbook-health-care |
| "I will write a detailed home, healthcare policy, and procedure manual for your company" | **From $60** | **30** · 4.7★ | https://www.fiverr.com/perepinae/write-a-detailed-home-healthcare-policy-and-procedure-manual-for-your-company |
| "I will write policy and procedure manuals for homecare and residential care **licensure**" | **From $50** | **16** · 4.7★ | https://www.fiverr.com/crownie_o/write-a-perfect-policy-and-procedure-manual-for-your-company |
| "I will write expert home care policy and procedure manual **for licensing purpose**" | **From $25** | **11** · 4.7★ | https://www.fiverr.com/onacreatives/write-expert-home-care-policy-and-procedure-manual-for-licensing-purpose |
| "I will write home care, healthcare, policy and procedure manual, employee handbook" | **From $50** | **8** · 4.9★ | https://www.fiverr.com/remtee01/write-unique-home-care-employee-handbook |
| "I will do medicaid certification, hipaa compliance, medical billing, home care license" | **From $30** | **7** · 4.5★ | https://www.fiverr.com/jos_elizabeth/do-medicaid-certification-medical-billing-hipaa-compliance-plan-homecare-license |

**The generic SOP market above it sets the price ceiling** — verbatim package table from `jeffreydjm`, 2026-08-27:
`| Package | $125 Basic "Essential SOP Documentation" | $245 Standard "Department SOP Framework" | $300 Premium "Business Operations Manual" |`, delivery **2 / 3 / 4 days**, scoped as "up to 10 pages / up to 20 pages / up to 30 pages", **87 reviews** · 5.0★ (https://www.fiverr.com/jeffreydjm/write-company-sops-and-standard-operating-procedures). Also: "I will write custom policies, procedures, operations and HR manuals" **From $350, 30 reviews** (https://www.fiverr.com/mrandyzig/create-professional-procedures-policies-and-operations-manuals); "I will write your employee handbook" **From $100, 133 reviews** (https://www.fiverr.com/toziel/write-your-employee-handbook).

**The clock: UNVERIFIED.** No dated regulatory change identified.

**First ten users:** State licensing agencies publish **lists of newly licensed and pending home-care agencies**, and business-formation registries publish new LLCs by NAICS/purpose. A new agency in its licensure window is publicly identifiable. **I did not verify a specific state's list URL this cycle** — that is a one-hour check. Named service providers: `zainjadoon545`, `perepinae`, `crownie_o`, `onacreatives`, `remtee01`.

**Gate check:** G1 PASS-provisional (public new-licensee lists, unverified) · G2 PASS-moderate (133 reviews on the generic handbook, 61+30+16+11+8 on the licensure-specific ones — thinner than candidates 1–3) · G3 PASS (regulation text → document, our shape exactly) · G4 PASS (generate a manual against one state's regs and check it clause-by-clause against that state's published licensing checklist — pure desk work) · G5 FAIL (no clock).

**What already exists:** the freelancers above, plus paid template packs. **Why inadequate:** templates are not state-specific, and freelancers are selling a template with the state name search-replaced. A genuine regulation-derived manual is a real quality jump.

**Price signal:** **$25–$350.**

**Confidence: 5/10.** Real, buildable, defensible-ish, but demand is an order of magnitude thinner than candidates 1–3 and there is no clock.

---

## 5. HACCP / Food-Safety Plan Pack

**One sentence:** A small food producer or restaurant that needs a written food-safety plan to pass inspection or get on a retailer's shelf buys one for $10–$100 today.

**The artifact:** Product description, process flow diagram, hazard analysis, CCPs with critical limits, monitoring and verification procedures, plus the record-keeping forms — matched to the applicable scheme (FDA Preventive Controls, CFIA PCP, FSSC 22000, BRCGS, SQF).

**Evidence — T1, verbatim, 2026-08-27.** Verbatim package table from `food_technlogst`:
`| Package | $10 Basic "FOOD SAFETY SOP" | $75 Standard "CLEANING PROGRAM" | $100 Premium "ONE FULL HACCP/ FOOD SAFETY PLAN" |`, Premium scope: `1-PRODUCT DESCRIP. 2-FLOW DIAGRAM 3-HAZARD ANALYSIS 4-CCPs & CLs 5-MONITORING & VERIFICATION`, delivery **1 / 2 / 3 days**, "Revisions: Unlimited", **149 reviews** · 5.0★ — https://www.fiverr.com/food_technlogst/make-haccp-or-food-safety-plans-sops-record-keeping-forms
Dated review "**2 days ago**", buyer price band **$600-$800**. Also "2 months ago … $200-$400", "3 weeks ago … $200-$400" — so the realised order values run well above the $10 headline.

| Other gigs (verbatim) | Price | Reviews | URL |
|---|---|---|---|
| "I will design haccp food safety plans, procedures checklists and traceability forms" | **From $10** | **85** · 4.5★ | https://www.fiverr.com/saylmayn/design-haccp-food-safety-plans-procedures-checklists-and-traceability-forms |
| "I will make haccp plan , haccp and food safety plans, procedures, record keeping forms" | **From $20** | **81** · 4.7★ | https://www.fiverr.com/drshani31/create-haccp-plan-for-restaurant-and-food-industry |
| "I will make cfia haccp, pcp import, pcp domestic, pcp export for canadian food business" | **From $50** | **23** · 4.9★ | https://www.fiverr.com/food_technlogst/create-complete-pcp-food-safety-plan-and-recall-plan-for-food-businesses |
| "I will develop your fssc 22000 food safety system" | **From $15** | **16** · 5.0★ | https://www.fiverr.com/certified_csco/develop-your-fssc-22000-food-safety-system |
| "I will create haccp and food safety plans for audit or inspection" | **From $75** | **11** · 5.0★ | https://www.fiverr.com/alexander_k7/create-haccp-plan-prp-ghp-gmp-assessement-criteria |
| "I will craft food safety plan and label verification program for amazon food business" | **From $15** | **14** · 5.0★ | https://www.fiverr.com/food_technlogst/craft-food-safety-plan-and-label-verification-program-for-amazon-food-business |
| "I will write full haccp plan food safety plan hazard analysis and allergen control" | **From $80** | **2** · 5.0★ | https://www.fiverr.com/victoria_will09/write-full-haccp-plan-food-safety-plan-hazard-analysis-and-allergen-control |

**The clock: UNVERIFIED.** No dated change identified.

**First ten users:** FDA maintains a **public Food Facility Registration** regime and publishes inspection results; state health departments publish new food-establishment permits. New facilities are publicly identifiable. **Not verified this cycle.** Named providers: `food_technlogst`, `saylmayn`, `drshani31`, `alexander_k7`, `foodcert`.

**Gate check:** G1 PASS-provisional · G2 PASS-moderate (149 + 85 + 81 reviews; realised order values $200–$800 per the dated reviews, well above headline) · G3 PASS (hazard analysis is a lookup against published hazard tables plus a process flow — highly structured) · G4 PASS (generate a plan for a known product category and check against the FDA/FSPCA published model plans, which are public) · G5 FAIL.

**Why I'm cautious:** the headline price is $10 and the sellers are competing to the floor. The *realised* prices in the dated reviews ($200–$800) tell a much better story, but the listing price is what a new entrant has to beat.

**Price signal:** listed **$10–$100**; realised order bands **$200–$800**.

**Confidence: 5/10.**

---

## 6. Chargeback Representment Letter Generator

**One sentence:** A merchant who just got a chargeback uploads the dispute notice and their order record, and gets back a processor-formatted rebuttal with the evidence assembled against the specific reason code.

**The artifact:** A compelling-evidence rebuttal letter mapped to the card network reason code, with an indexed evidence bundle (order confirmation, delivery proof, AVS/CVV result, terms acceptance, prior-transaction history).

**Evidence — T1, verbatim, 2026-08-27.** Verbatim package table from `sarasandoval89`:
`| Package | $50 Basic "1 Chargeback Rebuttal Letter" | $130 Standard "1 Complex Chargeback Case" | $450 Premium "Audit and Rebuttal Templates" |`, delivery **3 / 4 / 5 days**, **165 reviews** · 4.9★ — https://www.fiverr.com/sarasandoval89/create-a-chargeback-rebuttal-letter-adb5
Premium scope verbatim: `✅Audit of 1 acc ✅Optimization ✅Policies and Prevention strategies ✅ Rebuttal Letter Templates DIY`.

| Other gigs | Price | Reviews | URL |
|---|---|---|---|
| "I will professionally manage and win your paypal, stripe, and shopify chargebacks" | **From $15** | **37** · 5.0★ | https://www.fiverr.com/rana_adeel21/manage-and-win-all-chargebacks-disputes-stripe-paysafe-gateway |
| "I will prepare compelling response for shopify, paypal, stripe and card disputes" | **From $175** | **30** · 4.5★ | https://www.fiverr.com/bibekg/fight-your-chargebacks-frauds-and-save-your-hard-earned-money |
| "I will work as chargeback specialist and dispute consultant" | **From $200** | **2** · 5.0★ | https://www.fiverr.com/bibekg/be-your-ecommerce-consultant-chargeback-card-dispute-and-fraud-analyst |

**A warning in the data:** `sarasandoval89`'s most recent dated reviews are **"8 months ago", "9 months ago", "9 months ago", "10 months ago", "10 months ago"** — the *only* gig among all finalists whose recent-review timeline is stale. Either the seller stopped taking work, or **the category is being absorbed by the processors themselves.** Stripe, Shopify Payments and PayPal have all shipped built-in dispute-evidence assembly. This may already be a collapsed category and I have flagged it as such rather than talk myself into it.

**The clock: UNVERIFIED**, and the arrow may be pointing the wrong way.

**First ten users:** Not identified. Merchants with chargebacks are not publicly listed.

**Gate check:** G1 FAIL (no nameable buyers) · G2 PASS-weak (165 reviews but the recency signal is bad; only 10 gigs in the whole search) · G3 PASS · G4 PARTIAL (win-rate is unverifiable without real merchants) · G5 FAIL.

**Price signal:** **$15–$450.**

**Confidence: 3/10.** Submitted for completeness and because the stale-review finding is itself worth recording. **I would not build this.**

---

## 7. EU / UK Marketplace Compliance Pack (Declaration of Conformity + GPSR Responsible Person + EPR)

**One sentence:** A small seller shipping into the EU/UK needs a Declaration of Conformity, an EU Responsible Person and EPR registrations to keep their listings live, and buys each piece separately for $15–$205 today.

**The artifact:** A signed-ready EU/UKCA Declaration of Conformity naming the correct harmonised standards for the product category, a GPSR-compliant product technical file, and the EPR/WEEE/packaging registration paperwork per member state.

**Evidence — T1, verbatim, 2026-08-27:**

| Gig title (verbatim) | Price | Reviews | URL |
|---|---|---|---|
| "I will design ce compliant user manual for amazon or bol com with safety chapter" | **From $160** | **107** · 5.0★ | https://www.fiverr.com/filipdevaere/design-or-redesign-your-user-manual-for-bol-com-in-dutch |
| "I will do epr for germany and france extended producer responsibility" | **From $25** | **99** · 5.0★ | https://www.fiverr.com/abdulxam/do-france-epr-extended-producer-responsibility-registration |
| "I will create an eu certificate of conformity" | **From $205** | **40** · 4.9★ | https://www.fiverr.com/stephenmalli251/create-an-ec-certificate-of-conformity |
| "I will create a ce declaration of conformity certificate ec" | **From $50** | **37** · 4.9★ | https://www.fiverr.com/jacopo_scalbi/create-an-ec-declaration-of-conformity-certificate |
| "I will draft **in 24h** eu declaration of conformity doc for bol com compliance" | **From $100** | **37** · 5.0★ | https://www.fiverr.com/filipdevaere/create-a-eu-declaration-of-conformity |
| "I will classify european chemical clp hazard label into all european language" | **From $20** | **43** · 4.8★ | https://www.fiverr.com/sigge232/european-chemical-clp-hazard-label |
| "I will create a ukca certificate of conformity" | **From $205** | **11** · 5.0★ | https://www.fiverr.com/stephenmalli251/create-a-ukca-certificate-of-conformity |
| "I will be your eu responsible person for amazon listings, gpsr compliance" | **From $100** | **12** · 5.0★ | https://www.fiverr.com/samrudha2020/eu-responsible-person-for-amazon-listings-gpsr-compliance |
| "I will create eu declaration of conformity for amazon" | **From $65** | **10** · 5.0★ | https://www.fiverr.com/ujshark/create-eu-declaration-of-conformity-for-amazon |
| "I will register you eu wide with epr, weee, batteries, packaging" | **From $190** | 0 | (listing in `epr_registration_germany_packaging` results) |

**The clock — this is the one category with a live, visible clock, and the evidence for it is the gig list itself.** The GPSR-specific gigs are **overwhelmingly zero-review or single-review listings** — sellers have rushed in to build supply for a demand event that has only just happened. Verbatim examples with **no reviews yet**: "I will be your eu and uk responsible person, do eu gpsr compliance label, cosmetic report" **From $150**; "I will do gpsr compliance, eu responsible person, cpnp registration and product label" **From $25**; "I will be your eu responsible person for gpsr and amazon compliance" **From $95**; "I will provide gpsr, mdr, msr and fbo compliance for eu products" **From $35**; "I will audit your amazon eu product for gpsr compliance and safety" **From $15**.

**A wall of freshly-created, zero-review gigs at a coherent price point is a supply-side response to a regulatory event.** That is a genuine clock signal — but it is also the reason this candidate scores low: **the demand has not yet been proven to convert.** The sellers are betting, not earning.

**Specific dated regulation — UNVERIFIED-TODAY.** The EU General Product Safety Regulation is the obvious driver and I believe it began applying in December 2024, but I could not confirm the date without search access and **I am not going to assert it as fact.** Verify before use.

**First ten users:** Amazon EU / eBay / Etsy sellers whose listings carry no Responsible Person are, in principle, publicly enumerable by scraping marketplace listing pages — the GPSR responsible-person field is displayed on the listing. **This is a genuinely attractive Gate-1 story and it is unverified.** If that field is scrapeable at scale, you can name every non-compliant seller in a category. **Highest-value single check on this whole report.**

**Gate check:** G1 PASS-provisional (contingent on the listing-field check) · **G2 FAIL for GPSR specifically** — near-zero reviews on every GPSR gig means no proven money yet; PASS-weak for the adjacent DoC work (107 + 99 + 40 + 37 + 37 reviews) · G3 PASS · G4 PASS (generate a DoC for a known product and check it against the published harmonised-standards list) · G5 PASS-provisional.

**Price signal:** DoC **$50–$205**; EPR **$15–$190**; EU Responsible Person **$95–$150**.

**Confidence: 4/10.** Great clock, unproven demand. **This belongs on the watchlist with a 90-day re-check** — if those zero-review gigs have 50 reviews each in December, it becomes a top-three candidate.

---

## 8. Grant Proposal / Letter-of-Intent Drafting

**One sentence:** A small nonprofit pays $160–$900 for a written grant proposal today.

**The artifact:** Funder-matched LOI or full proposal — executive summary, needs assessment, organisational background, objectives and methodology, evaluation plan, budget narrative.

**Evidence — T1, verbatim, 2026-08-27.** Verbatim package table from `ruyakoman`:
`| Package | $160 Basic | $600 Standard | $900 Premium |` — Basic: "COVER LETTER/LOIs: You will receive a grant cover letter or letter of intent (500-750 words)"; Standard: "one (1) well-written grant proposal (up to 3,000 words)"; Premium: "up to 5,000 words". Delivery **14 / 21 / 30 days** (rush to 10/14/21 days for +$95/+$160/+$190). **241 reviews** · 5.0★ — https://www.fiverr.com/ruyakoman/write-your-grant-proposal-and-provide-grants-research
Dated reviews: "3 weeks ago … $400-$600", "3 weeks ago … $200-$400", "1 month ago … $200-$400", "2 months ago … $200-$400".

| Other gigs | Price | Reviews | URL |
|---|---|---|---|
| "I will do grant opportunities grant proposal grant writing grant application" | **From $15** | **361** · 4.9★ | https://www.fiverr.com/sara5911/write-your-grant-proposal |
| "I will write grant, do grant writing research, be grant rfp writer" | **From $15** | **152** · 4.9★ | https://www.fiverr.com/boluxy99/prepare-your-grants-and-proposals |
| "I will do grant proposal, grant research, grant application, nonprofit grant writing **in 24 hours**" | **From $10** | **112** · 4.8★ | https://www.fiverr.com/thegrantoracle/do-your-grant-research-grant-application-grant-proposal-writing-in-24-hours |
| "I will do grant writing, grant proposal, grant research, and grant application" | **From $20** | **104** · 4.8★ | https://www.fiverr.com/jane_writes70/do-grant-writing-grant-proposal-grant-application |
| "I will research and write persuasive grant proposal, apply for grant, funding, 501c3" | **From $195** | **54** · 4.9★ | https://www.fiverr.com/tscharr22/research-and-write-persuasive-grant-proposal-apply-for-grant-funding-501c3 |
| "I will write a compelling grant proposal and business plan with financial projections" | **From $100** | **46** · 5.0★ | https://www.fiverr.com/sallyllysa_/grant-writing-grant-writers-grant-proposal-writing-grant-research-grant-editing |

**Note the 14–30 day delivery times on the $600–$900 tiers.** Long turnaround at high price is normally a good arbitrage sign. But here it reflects *funder research*, not typing.

**The clock: UNVERIFIED.**

**First ten users:** 501(c)(3) organisations are fully public (IRS Business Master File, Form 990 filings including revenue and program descriptions). You can name every small nonprofit in a state with revenue in a target band. **Genuinely strong Gate-1 raw material.**

**Gate check:** G1 PASS (IRS BMF is public and complete) · G2 PASS (241 + 361 + 152 + 112 + 104 reviews) · G3 PASS-weak — the artifact is prose whose quality is *unverifiable until the funder decides*, which is the same failure mode the postmortem flagged · G4 **FAIL** — we cannot grade a grant proposal in 14 days without a funder's decision, and the funder is a stranger · G5 FAIL.

**What already exists:** Instrumentl, Grantable and several AI grant-writing tools (**pricing UNVERIFIED — not checked this cycle**), plus a very deep freelancer bench at $10–$20. The $15 gig with **361 reviews** sitting alongside the $160 gig with **241 reviews** says this market has already bifurcated into commodity and premium, with the commodity end at AI-generated prices.

**Price signal:** **$10–$900**, bimodal.

**Confidence: 4/10.** Fails G4 outright, which the postmortem says is disqualifying. Included for completeness.

---

## 9. WCAG / ADA Accessibility Audit & VPAT Report

**One sentence:** A small site owner buys a written accessibility conformance report for $40–$300.

**The artifact:** A WCAG 2.x conformance audit with per-criterion findings and remediation code, and/or a VPAT / Section 508 accessibility conformance report.

**Evidence — T1, verbatim, 2026-08-27:**

| Gig title (verbatim) | Price | Reviews | URL |
|---|---|---|---|
| "I will perform accessibility and wcag on wordpress website" | **From $75** | **125** · 4.9★ | https://www.fiverr.com/yasirfarooq786/make-your-wordpress-website-accessibility-compliant |
| "I will ada compliance your shopify website to protect you from hefty lawsuits" | **From $100** | **29** · 5.0★ | https://www.fiverr.com/mohitadacomply/ada-compliance-your-ecommerce-website |
| "I will ada compliance website manually code wcag , aoda section 508" | **From $10** | **29** · 4.9★ | https://www.fiverr.com/kashifaws/ada-compliant-your-website-wcag-section-508-a-aa |
| "I will fix ada and wcag compliance issues on your website" | **From $50** | **27** · 4.9★ | https://www.fiverr.com/abdullahxdev/fix-accessibility-issues-for-ada-and-wcag-compliance |
| "I will create wcag vpat report ada section 508 compliance" | **From $300** | **23** · 4.8★ | https://www.fiverr.com/ritvik_qa/create-wcag-vpat-report-ada-section-508-compliance |
| "I will make your PDF accessible section 508 and wcag compliance service" | **From $10** | **12** · 5.0★ | https://www.fiverr.com/royraviprakash/make-your-pdf-accessible-section-508-and-wcag-compliance-service |
| "I will create wcag vpat report ada section 508 compliance" | **From $40** | **6** · 4.9★ | https://www.fiverr.com/archanakalbhor/ada-website-accessibility-testing |

Note the fear-based framing in the seller's own title — *"to protect you from hefty lawsuits"* — which is the actual purchase driver.

**The clock: UNVERIFIED-TODAY.** The European Accessibility Act is the obvious candidate and I believe it began applying in mid-2025, but **I could not confirm the date and will not assert it.**

**First ten users:** Fully nameable and **self-generating** — you can crawl any list of small e-commerce sites, run an automated axe-core scan, and produce a named list of sites with specific failures *and the evidence attached*. Shopify/WooCommerce store directories, BuiltWith-style tech lists, and simple sitemap crawls all supply the population. **This is a genuinely excellent Gate-1 story: the outreach artifact and the product are the same object.**

**Gate check:** G1 PASS (strong — audit-first outreach where the audit is the lead magnet and the product) · G2 PASS-weak (125 reviews is the only substantial count; the rest are 6–29) · G3 PASS (axe-core + LLM remediation is well-trodden) · G4 PASS · G5 UNVERIFIED.

**What already exists:** accessiBe, UserWay, AudioEye (overlay vendors, widely criticised); axe DevTools; WAVE. **The tooling here is mature and free at the bottom end** — the paid layer is the *written report with a human's name on it*, which is partly a liability-transfer product we cannot sell.

**Price signal:** **$10–$300**; VPAT specifically **$40–$300**.

**Confidence: 4/10.** Best distribution story on the board, weakest differentiation.

---

# KILLED AT THE BENCH (do not spend cycle-2 time here)

| Category | Evidence | Why killed |
|---|---|---|
| **SOC 2 / ISO 27001 policy packs** | Top gig **36 reviews** at $10; "I will prepare soc 2 security policies" **From $3,000** with **4 reviews**; "I will provide soc 2 compliance" **From $20,000** with **2 reviews**; https://www.fiverr.com/uri_iothreat/prepare-soc2-security-policies | Category has been fully captured by Vanta/Drata/Secureframe — two gigs literally sell *"implement iso 27001 and soc 2 compliance using vanta and drata"* ($250, 2 reviews) and *"manage your ISO 27001 framework on Drata, Vanta and Secureframe"*. The freelancers are now **operators of the incumbent software**. G2 fail. |
| **FinCEN BOI report filing** | Top gig **49 reviews** at **$25**; whole category $10–$40; https://www.fiverr.com/kadirtncer/file-your-beneficial-owner-information-report-to-fincen | $25 ceiling on a form-filling task, and the underlying US reporting obligation was substantially narrowed during 2025 (**exact scope UNVERIFIED**). Dead either way on price. |
| **Commercial lease abstraction** | Best gig **66 reviews** at $30; next real one **11 reviews** at $20; https://www.fiverr.com/vin2007/do-lease-abstract-for-us-commercial-real-estate-leases | Thin, cheap, and the buyer is an asset manager or brokerage — agency-mediated, not the payer-user we want. G1 + G2 fail. |
| **Provider credentialing / CAQH** | Top gig **46 reviews** at $90; then 27/26/21/20 reviews at $10–$40; https://www.fiverr.com/sbilal6/do-credentialing-and-provider-enrollment-for-us-healthcare-providers | Priced as offshore BPO ($10–$40), months-long payer-side cycle times, and the bottleneck is *waiting on insurers* — not document production. G3 fail (the constraint is access, not skilled work). |
| **IFTA / DOT / FMCSA filings** | Only ~5 relevant gigs in the whole search; best is **6 reviews** at $75 (https://www.fiverr.com/javedakhtar_91/file-mcs-150-biennial-update-ifta-kyu-nm-ny-hut-ucr-irp-apportioned-plate); most have **zero reviews** | Surface is dry. Owner-operators buy this bundled with dispatch, not standalone. G2 fail. |
| **Certified payroll / Davis-Bacon (WH-347)** | **7 gigs total**, best is **9 reviews** at $60 (https://www.fiverr.com/ejazahmed78/do-calculation-of-certified-payroll-form-wh-347); the rest zero-review | Genuinely mechanical and genuinely required, but **no observable money on this surface**. Buyers use LCPtracker (enterprise, agency-mandated) instead. G2 fail on the freelance surface — may be alive elsewhere. |
| **Google Business Profile reinstatement** | **344 reviews** at $100/$200/$300 (https://www.fiverr.com/jigneshkadam/reinstate-and-fix-google-my-business-profile-and-listing), 292 at $30, 238 at $65, 126 at $100 | Big volume, and I wanted to like it. Killed on **21-day delivery** across all three tiers — that is not a document being written, that is a human waiting on Google's opaque appeal queue. The deliverable is an *outcome we don't control*. G3 fail (bottleneck is Google's discretion) and G4 fail (unverifiable alone). |

---

# ALREADY COLLAPSED — the inverse signal

These categories are done. The price floor has met the cost of AI generation, volume is enormous, and delivery is measured in hours. **Knowing they are closed is worth as much as knowing what is open.**

| Category | The collapse, verbatim | URL |
|---|---|---|
| **Transcription** | "I will transcribe audio video interviews podcast transcripts" — **From $5**, **872 reviews** | https://www.fiverr.com/flamboyant222/do-transcripts-for-you-for-3-hours |
| **FDA nutrition facts labels** | "I will create your fda nutrition facts label" — **$15 / $20 / $25**, **1-day delivery** on all three tiers, **647 reviews**. Next: 380 reviews at $20, 170 at $20, 148 at $15, 102 at $30, 94 at $30, 93 at $30. | https://www.fiverr.com/helcioferreira/design-your-fda-nutrition-facts-label |
| **SEO blog / article writing** | Bifurcated and hollowing: **718 reviews at $10**, 580 at $10, 578 at $15, 860 at $15 — against a premium tier that now has to *advertise being human*: "I will write **human first** blogs", 961 reviews at $100; "I will write your **human written** SEO blog posts", 622 reviews at $70; "I will write **human** SEO blog posts and articles", 576 reviews at $100 | https://www.fiverr.com/si_writer24/engaging-surfer-seo-articles-with-jarvis · https://www.fiverr.com/georgiaeaustin/be-your-content-writer-for-blog-articles |
| **Logo vectorising / raster-to-vector** | "I will vectorize image or logo in **1 hour**" — **From $10**, **482 reviews**; 520 reviews at $15; 359 at $25; 242 at $10 | https://www.fiverr.com/inshaalali/do-low-resolution-to-high-resolution-raster-to-vector-in-2-hours |
| **KDP book formatting** | 375 reviews at $20; 272 at $45; 66 at $25; 34 at $10 | https://www.fiverr.com/naveed0007/do-children-book-formatting-for-paperback-book-kdp-amazon-and-ingramspark |
| **Chargeback representment** *(suspected — see candidate 6)* | Category leader's most recent review is **8 months old**; only **10 gigs** exist in the entire search | https://www.fiverr.com/sarasandoval89/create-a-chargeback-rebuttal-letter-adb5 |

**The pattern that separates collapsed from live:** collapsed categories deliver in **1 hour to 1 day** and cost **$5–$25**. Live arbitrage categories deliver in **3–5 days** and cost **$95–$600**. The delivery time *is* the intake labour. Any category where a human still needs 3+ days to produce a rule-governed document is a category where the intake has not been automated — and that is the whole map.

**Corollary worth carrying into cycle 2:** the "human written" premium tier in article writing is a *transitional* price, not a stable one. Do not build anything whose defence is "a human touched it."

---

# SUMMARY TABLE

| # | Candidate | Price signal (verbatim) | Best volume proof | G1 | G2 | G3 | G4 | G5 | Conf |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **USPTO trademark office-action response** | $95–$600 Fiverr · **$599** Trademark Engine | 232 + 163 + 121 + 120 + 106 reviews | ✅✅ | ✅ | ⚠️ UPL | ✅✅ | ✅ | **8** |
| 3 | **Manual J/S/D from a floor plan** | $75–$400 · software $45/project | **496 reviews** @ $200–$400 | ✅ | ✅ | ✅ | ✅ | ⚠️ | **7** |
| 2 | Marketplace reinstatement appeal pack | $45–$370 · $150–$255 other platforms | **517 reviews** @ $295–$370 | ❌ | ✅✅ | ✅ | ⚠️ | ❌ | 5 |
| 4 | Licensure policy-and-procedure manuals | $25–$350 | 133 + 61 + 30 reviews | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | 5 |
| 5 | HACCP / food-safety plan pack | $10–$100 listed; $200–$800 realised | 149 + 85 + 81 reviews | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | 5 |
| 7 | EU/UK marketplace compliance pack | DoC $50–$205 · EPR $15–$190 | 107 + 99 + 40 reviews (GPSR itself ~0) | ⚠️ | ❌ | ✅ | ✅ | ✅ | 4 |
| 8 | Grant proposal drafting | $10–$900 (bimodal) | 361 + 241 + 152 reviews | ✅ | ✅ | ⚠️ | ❌ | ❌ | 4 |
| 9 | WCAG / VPAT accessibility report | $10–$300 | 125 reviews | ✅✅ | ⚠️ | ✅ | ✅ | ⚠️ | 4 |
| 6 | Chargeback representment | $15–$450 | 165 reviews, **stale** | ❌ | ⚠️ | ✅ | ⚠️ | ❌ | 3 |

---

# WHAT I WOULD DO NEXT (one hour each, all desk work, no strangers)

1. **Verify USPTO office-action volume.** The single number candidate 1 rests on. If it is not publicly published, that is a red flag of exactly the kind the postmortem describes — treat it as a kill signal, not a research task.
2. **Verify whether TSDR exposes applicant email, and whether attorney-of-record is filterable.** Changes candidate 1's outreach channel entirely.
3. **Verify the UPL boundary** for preparing (not filing, not signing) a trademark office-action response for a US-domiciled pro-se applicant. `dmorganlaw` already sells a "No representation" tier, which suggests the line exists and is known.
4. **Check whether Amazon EU listing pages expose the GPSR Responsible Person field to a scraper.** If yes, candidate 7's Gate 1 becomes best-in-class and it jumps the queue.
5. **Verify ACCA software-approval requirements** for permit acceptance of a Manual J report. Most likely killer of candidate 3.
6. **Re-check the GPSR gig cohort in ~90 days.** If the zero-review listings have accumulated reviews, candidate 7 has converted and becomes a top-three candidate.

## Access debt for the next scout
Upwork (demand-side job posts), Reddit (buyer voice) and the Amazon Seller Forums were all inaccessible this cycle. **Every candidate whose Gate 1 I marked FAIL failed for want of buyer-side visibility, not for want of demand.** A cycle-2 scout with working access to job-post data would materially change the ranking of candidates 2 and 6 — and might resurrect them.
