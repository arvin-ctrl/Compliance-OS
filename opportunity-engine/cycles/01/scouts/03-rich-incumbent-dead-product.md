# SCOUT 03 — RICH INCUMBENT, DEAD PRODUCT

**Scout surface:** software with real revenue + a dead changelog + angry recent reviews + published pricing.
**Date of research:** 2026-08-27. All URLs fetched that day unless noted.
**Headline verdict: THE SURFACE IS MOSTLY DRY FOR THIS OPERATOR — and I can name the structural reason.**

I return **6 candidates**, none above confidence 5/10, plus **7 explicit kills** and one structural
finding that I think is worth more to the engine than any single candidate below.

---

## 0. THE STRUCTURAL FINDING (read this first)

I scanned four platform marketplaces exhaustively and machine-readably. **All four are structurally
incapable of hosting the "rich incumbent, dead product" pattern**, because the platform landlord
either forces updates or delists the app. The pattern only survives in *independent* web/desktop
software with no platform landlord.

| Surface | What I pulled | Stale + paid + angry? |
|---|---|---|
| **WordPress.org** plugin API | 600 most-popular plugins w/ `active_installs` + `last_updated` | **No.** Only 12 plugins are >18mo stale with ≥100k installs, and **all 12 are free** (no revenue). Paid WP products don't live on .org. |
| **Atlassian Marketplace** REST API | 613 unique apps across `top-grossing` + `popular`, all 3 hosting types, with `totalInstalls` + version release dates | **No.** Every stale app is either **Server** (EOL Feb 2024 — staleness is expected, not a signal) or **free**. Paid *Cloud* apps are all current because Atlassian forces API migrations. |
| **iOS + Mac App Store** (iTunes Search API) | 6,193 unique apps across 115 B2B/prosumer search terms, w/ price, rating count, `currentVersionReleaseDate` | **No.** 165 apps are stale with ≥300 ratings but they are overwhelmingly free consumer apps and games. B2B mobile apps are *companions* to a web product and carry no pricing. |
| **Shopify App Store** | 25,412 app slugs from sitemap; sampled 6,000; 583 with ratings; pulled recent 1–2★ reviews for the 30 worst-rated high-volume apps | **No.** Top apps rate 4.2–5.0. Recent 1★ reviews complain about *support and billing*, not abandonment. Shopify garbage-collects: an app that stops tracking API changes becomes "unsupported" after 9 months ([help.shopify.com](https://help.shopify.com/en/partners/help-support/faq/unpublished-app-deprecation)). |

**Implication for the engine:** stop hunting this pattern inside marketplaces. It lives in
independent vertical SaaS with a founder who moved on. My scaled detector for *that* is described
in §8 and it works — it is the reusable asset from this cycle.

**Second structural finding, and the one that kills most candidates:** in essentially every niche
where I found a dead incumbent, there is already a **healthy, cheap, well-rated competitor**
serving the stranded users. A dead incumbent is not an opening if the refugees already have
somewhere good to go. This killed 4 of my 7 kills below and it is why no candidate scores above 5.

---

## 1. Marmalead — Etsy keyword/SEO research tool

**One sentence:** A 260,000-shop Etsy SEO tool charging $19/mo whose customers publicly rate it 2.1/5.

**The artifact:** Etsy keyword research + listing-quality grading — the seller receives ranked
keyword suggestions with search/engagement/competition scores and a per-listing SEO score.

**Evidence — T1 (money is moving now):**
- Pricing, verbatim from https://www.marmalead.com/pricing:
  `"$19 USD paid monthly"` · `"$53 USD paid quarterly"` (Save 7%) · `"$190 USD paid annually"`
  (Save 16%) · `"$300 USD paid ONCE"` (Save 73%, marked best value).
- User base claim, verbatim, same page: **`"Join over 260,503 other Etsy Shops that trust Marmalead!"`**
- Trustpilot https://www.trustpilot.com/review/marmalead.com — **TrustScore 2.1 / 5**, 10 reviews,
  **80% one-star**. Verbatim, dated:
  - Olivia, **2026-04-29**: *"they charged me! No free trial at all, and the tool is not very good."*
  - Denise, **2026-03-21**: *"It gave me misinformation about my shop, told me to edit a listing that was still in draft mode"*
  - AAD, **2025-11-23**: *"they refuse to issue a full refund even though I cancelled in less than 14 days."*

**The dead-product half is NOT proven.** Their blog is *active* (latest post 2026-07-27,
https://blog.marmalead.com/). `/changelog`, `/releases`, `/whats-new` all return the SPA shell,
so there is no public release history to read. **Staleness: UNVERIFIED.** The $300 lifetime tier is
a soft signal (lifetime deals are what products stop investing in sell), but that is inference, not evidence.

**The clock:** Etsy's search ranking changed materially with the "Etsy Insider"/relevancy shifts and
the 2025–26 push on personalisation; a keyword tool whose data model predates that decays. I could
**not** pin this to a dated primary source — **UNVERIFIED**.

**First ten users:** Mechanism is unusually strong — every Etsy shop is a public storefront with a
public contact form, and the Trustpilot reviewers above are self-identified unhappy payers.
**But I did not name ten actual shops.** Reddit was unreachable from this environment and the
session's web-search budget was exhausted. **Gate 1 mechanism: strong. Gate 1 execution: unproven.**

**Gate check:**
- G1 distribution — **PASS (mechanism), UNPROVEN (named users).** Public storefronts + public seller communities; no sales motion; card payment.
- G2 observable demand — **PASS.** 260,503 claimed shops at $19/mo, published.
- G3 buildable — **PASS.** Keyword/rank data is scrapeable + Etsy has a public API; this is a data pipeline, our strength.
- G4 self-verifiable in 14 days — **PASS.** We can rebuild the keyword-scoring core and compare against Marmalead's own output with no stranger's help.
- G5 the clock — **UNVERIFIED.** Could not date the change.

**What already exists:** eRank (last content 2026-08-26 — **active**), Alura, EverBee, Sale Samurai.
**This is the problem.** eRank is cheaper and actively maintained. The refugees have somewhere to go.

**Price signal:** $19/mo, $190/yr, $300 lifetime.
**Confidence: 5/10.** Best money evidence on my surface; weakest staleness evidence.

---

## 2. Tokeet / Advance.cm — short-term-rental property management

**One sentence:** A $135/mo vacation-rental channel manager whose paying hosts publicly report double
bookings and unauthorised plan changes.

**The artifact:** Calendar/channel sync across Airbnb/Vrbo/Booking.com, reservations, guest messaging, invoicing.

**Evidence — T1:**
- Pricing verbatim, https://www.tokeet.com/pricing: **`"$134.90/month"`** for up to 10 rentals, monthly
  billing, "15 Days Free Trial", "No credit card required". GetApp lists starting price **$9.99/month**.
- Capterra https://www.capterra.com/p/155340/Tokeet/reviews/ — **3.7/5, 147 reviews.** Verbatim, dated:
  - Ross O., Business Owner, **2025-08-27**, 1.0★ — *"Paid for a Year, Tokeet Cancelled Without Authorisation to Increase the Price"*
  - Amir M., Director, Hospitality, **2025-06-25**, 1.0★ — *"use other platforms if you can. I had so many issues wit them in the ast too. they are not very reliable"*
  - Turyan R., Partner, Hospitality, **2024-11-30**, 2.0★ — *"A trillion glitches starting from double bookings, bookings not showing un in the calendars, very bad API connections with Vrbo and Booking.com"*
- Trustpilot https://www.trustpilot.com/review/tokeet.com — **4.3/5, 295 reviews, 12% one-star.** Verbatim, dated:
  - Amanda Ridgway (GB), **2026-07-22**, 1★ — *"If I could give 0 stars I would for their suite of products...the support staff are unhelpful sarcastic and rude."*
  - Jonathan Pfeifer (US), **2026-04-09**, 1★ — *"Tokeet (Advance.cm) is unfortunately riddled with bugs, making it unstable and in some cases unusable."*
  - TN (US), **2026-02-05**, 1★ — *"For a company operating in property distribution, this lack of basic verification, accountability, and responsiveness is unacceptable."*

**Staleness: FAILS THE BAR.** Last blog post 2025-09-03 (~12 months), and they are actively
rebranding to Advance.cm. This is a *bad* product, not a *dead* one. The brief's bar is 18–24 months.

**Gate check:** G1 **PASS** (STR hosts are self-serve, card-paid, and congregate publicly) · G2 **PASS** ·
G3 **PARTIAL — the bottleneck is access, not skill**: Airbnb's official API is partner-gated, and
channel-manager status with Booking.com/Vrbo requires certification. That is exactly the Procore
failure mode already in the LEDGER. · G4 **FAIL** — we cannot prove sync reliability without
marketplace credentials we don't hold · G5 no dated change identified.

**What already exists:** OwnerRez, Lodgify, Hostaway, Uplisting, Smoobu — all actively shipping
(all showed 2026-08 content in my scan). Adequate.

**Price signal:** $134.90/mo at 10 rentals.
**Confidence: 3/10. Recommend KILL on G3/G4** — same API-gatekeeper trap as Procore.

---

## 3. Rigbooks — owner-operator trucking bookkeeping

**One sentence:** Per-mile cost accounting for one-truck owner-operators, $19–$149/mo, whose public
content stopped in May 2021.

**The artifact:** Load-by-load profitability — the driver enters loads and expenses and receives
true cost-per-mile and per-load margin, plus IFTA-ready mileage.

**Evidence:**
- **T1 pricing**, verbatim from https://www.rigbooks.com/pricing:
  Basic Entry **`"$19 mo"`** (1 truck) · Leased O/O **`"$29 mo"`** (1 truck) · Independent O/O
  **`"$49 mo"`** (1 truck) · Small Fleet **`"$149 mo"`** (5 trucks). Additional trucks $19–$29/mo.
  Homepage: `"Starts at $19 a month. No credit card upfront. Cancel anytime."`
- **Staleness (my scan):** latest dated content anywhere on the blog/feed = **2021-05-14**
  (https://www.rigbooks.com/feed/, https://www.rigbooks.com/rss). **5.3 years.** Cleanest staleness
  signal I found on a product with published, self-serve pricing.
- **No review evidence found.** No Capterra/Trustpilot/G2 page located. **This is a real gap** — I have
  the "dead" half and the "published pricing" half but **not the "angry customers" half**, and
  therefore not proof anyone is still paying.

**The clock:** The FMCSA English-language-proficiency enforcement (2025) and the post-2023 freight
recession squeezed owner-operator margins hard, which raises the value of per-load costing. Named,
but I did not verify a dated primary source — **UNVERIFIED**.

**First ten users:** Channels are real and public (TruckersReport forums, owner-operator Facebook
groups, r/Truckers). **I could not name ten** — Reddit was unreachable and search budget was gone.

**Gate check:** G1 **PASS (mechanism) / UNPROVEN (named)** · G2 **WEAK — published pricing but zero
evidence of an installed base** · G3 **PASS** — bookkeeping math + document parsing is squarely our
capability · G4 **PASS** — we can build the costing engine and validate on public rate data alone ·
G5 **UNVERIFIED**.

**What already exists:** TruckingOffice, Truckstop, plus generic QuickBooks. TruckingOffice returned
no dated content in my scan (inconclusive). Genuinely thin competition — the best of my candidates on that axis.

**Price signal:** $19–$149/mo.
**Confidence: 4/10.** Kill unless G2 (does anyone actually pay?) can be established.

---

## 4. Music Teacher's Helper → "Duet" — private music studio management

**One sentence:** A studio-management product for private music teachers whose live homepage still
advertises a promotion that expired on 31 Aug 2024.

**The artifact:** Lesson scheduling, invoicing, student/parent portal for a private teacher's studio.

**Evidence — the single best "dead product" artifact I found:**
- https://www.musicteachershelper.com/ , fetched **2026-08-27**, renders verbatim:
  **`"Free until September 1st when you sign up in July or August* *Participants will receive free
  access from time of sign-up until 08/31/2024. Charges will begin starting 09/01/24."`**
  A live, top-of-page promotional banner **two years past its own expiry**. Nobody is minding this site.
- The same page carries a **`"Legacy Login"`** link beside the normal login — Music Teacher's Helper
  customers were migrated to "Duet" and the old cohort is stranded on a legacy system.
- musicteachershelper.com blog RSS: last post **2023-07-10** (3.1 years).
- duetpartner.com: latest dated content **2025-11-10**, and it is a *blog post*, not a release note —
  there is no public changelog.

**Pricing: UNVERIFIED.** https://www.musicteachershelper.com/pricing/ renders the tier structure
(Basic 1–20 students · Plus 21–40 · Premium 41–100 · Unlimited 101+) but the **prices are injected by
JavaScript and I could not capture the numbers.** I will not invent them.

**Gate check:** G1 **PASS (mechanism)** — private music teachers are individually findable via public
teacher directories (MTNA chapter listings, Lessons.com, Thumbtack) and pay by card; **UNPROVEN (named)**
· G2 **PARTIAL** — a real product with real tiers, but no revenue figure and no review corpus found ·
G3 **PASS** — scheduling/invoicing is core competence · G4 **PASS** · G5 **no dated change**.

**What already exists:** **My Music Staff — actively shipping (2026-07-30) and cheap. This is fatal.**
The stranded MTH cohort already has an obvious, well-regarded destination.

**Price signal:** UNVERIFIED.
**Confidence: 4/10. Recommend KILL** — competitor is adequate.

---

## 5. a la mode "TOTAL" — residential appraisal form software

**One sentence:** The dominant desktop appraisal-forms product, owned by CoreLogic, whose public
newsroom stopped in July 2022.

**Evidence:**
- Staleness: https://www.alamode.com/news — latest dated item **2022-07-17** (4.1 years).
- Ownership: a la mode was acquired by CoreLogic (2019); CoreLogic was taken private by Stone Point
  Capital and Insight Partners (2021) — the PE-roll-up shape the brief asked me to hunt.
- **Pricing: UNVERIFIED.** `/products/total/pricing` 404s; `/store` exists but I could not extract prices.
- **No review corpus captured.**

**Gate check:** G1 — appraisers are individually findable (state licence rosters are public), self-serve,
card-paid: **PASS on mechanism** · G2 **UNVERIFIED** · G3 **FAIL (probable)** — appraisal output is
locked to the UAD/MISMO form standard and lender delivery via UCDP; the artifact is a *regulated form*,
and getting it accepted is an access problem, not a skilled-work problem. This is the same shape as the
already-killed AACE/standards-blocked candidate in the LEDGER · G4 **FAIL** — cannot self-verify
acceptance without lender cooperation.

**Confidence: 3/10. Recommend KILL on G3/G4.** Flagging it only because the staleness + PE-ownership
signal is textbook and someone may want it on the WATCHLIST.

---

## 6. BarnManager — equestrian barn management

**One sentence:** Horse-barn record keeping at $400–$700/year whose content stopped in early 2024.

**Evidence:**
- **T1 pricing**, verbatim from https://www.barnmanager.com/pricing: Essentials **`"$400 / year"`**
  (also `$40` monthly); higher tier **`"$700"`** / year (`$70` monthly). "Save 20% With a Yearly
  Subscription", "14 Day Free Trial", "Unlimited Users", "Unlimited Horses".
- Staleness: blog feed last post **2023-10-17**; site feed **2024-03-06** (~2.4 years).
- **No review corpus found.** No install/user count published.

**Gate check:** G1 **PASS (mechanism)** — show barns and trainers are publicly listed (USEF/USHJA member
directories, show entry lists) and pay by card · G2 **WEAK** — published pricing, but no evidence of
scale · G3 **PASS** · G4 **PASS** · G5 none identified.

**Price signal:** $400–$700/yr.
**Confidence: 3/10.** Thin market; no proof of an installed base.

---

## 7. KILLS — do not re-research

| Candidate | Why killed |
|---|---|
| **Precise Petcare** (pet-sitting software) | Perfect staleness (blog dead since **2018-05-23**, 8.3 yrs) and perfect published pricing (**$20 / $45 / $90 / $160 / $200 / $250 / $315 / $390 per month** by active-staff band, verbatim). **Killed anyway: competitor is adequate.** Capterra: Precise Petcare **4.2★ / 17 reviews**; Time To Pet **4.9★ / 278 reviews, $50/mo**; Pet Sitter Plus **4.8★ / 140**; Scout **4.8★ / 88** — all actively maintained. The refugees already have three good homes. |
| **ProPet** (kennel/daycare software) | **Gate 1 fail.** No published pricing — site is demo-gated ("Book Live Demo", phone number, `info@` address). Sales motion required. Blog dead 2023-12-11 but irrelevant. |
| **PawnMate** (pawn shop software) | **Gate 1 fail.** Stale (2023-12-02) but pawn is ATF/state-regulated, rep-sold, no published self-serve pricing. |
| **Sprout Studio** (photography studio mgmt) | Staleness excellent (feed dead **2021-12-21**, 4.7 yrs) but site sits behind a bot wall so pricing is unverifiable, and the category is crowded with actively-shipping rivals (ShootProof 2026-08-19, Iris Works 2026-08-25, Studio Ninja 2026-08-01, Táve, Pixieset, HoneyBook). **Competitor adequate.** |
| **PokerTracker 4** | Blog RSS last post **2012-11-28** (13.7 yrs) — the most extreme staleness I measured. Killed: store page 403s so **pricing unverifiable**; the market is *structurally shrinking* (HUDs are banned or restricted on most major sites); and Hand2Note/DriveHUD are active. |
| **Ham Radio Deluxe** | My prior candidate. **Falsified:** blog shows content to **2025-10-14** (10 months) — it is not dead. Removed. |
| **Hootsuite** | Best-known instance of the pattern, but every claim I could find (the $5.99→$99 Pro-tier move, "1.5 Trustpilot score", "40% price rise") traces only to **SEO-farm secondary pages**, not primary sources — **T3 at best**. And the competitor field (Buffer, Later, Publer, Metricool) is enormous and healthy. Killed on evidence quality + adequate competitors. |

---

## 8. METHOD — the reusable asset

The thing worth keeping from this cycle is a **scaled staleness detector**. For a list of vendor
domains it probes `/changelog`, `/release-notes`, `/whats-new`, `/updates`, `/news`, `/blog`,
`/blog/feed/`, `/feed/`, `/rss`, extracts every date on the page in three formats, and returns the
**maximum date found anywhere**. A domain whose newest public dated artifact is >18 months old is a
candidate. Run against **259 independent vertical-SaaS domains**, it produced the ranked list that
generated every candidate above.

Scripts: `stale.py`, `stale2.py`, `shop2.py`, `shop3.py`, `ddg.sh` in the session scratchpad.

**Caveat that limits every candidate above:** a dead *blog* is weaker evidence than a dead
*changelog*. Most small vendors publish no changelog at all, so "no dated public content since X"
is the best proxy available — but it can be wrong in both directions (a vendor may ship steadily
while never blogging). **Every staleness claim in this report is of that weaker kind unless stated otherwise.**
The Music Teacher's Helper expired-banner artifact (§4) is the one exception — that is direct evidence
of neglect, not a proxy.

---

## 9. WHAT I COULD NOT DO — and what it cost

Be aware of these when weighing my confidence scores:

1. **Reddit was unreachable** from this environment (403 on both `reddit.com` and `old.reddit.com`
   JSON, and WebFetch is blocked for the domain). This is why **no candidate has named first-ten-users**.
   Gate 1 is therefore *unproven*, not passed, everywhere I say "mechanism".
2. **The session's web-search budget (200/200) was exhausted** partway through by other scouts.
   DuckDuckGo HTML worked for exactly one query before rate-limiting; Bing returned junk.
3. **Cloudflare/bot walls** blocked CodeCanyon (which publishes literal *sales counts* — the single
   best public revenue signal I know of, and the biggest missed opportunity here), Sprout Studio,
   and PokerTracker's store.

**If this surface is re-run, do these three things first:** (a) get Reddit access, (b) get CodeCanyon
access — public per-item sales counts × published price is the only place I know where incumbent
revenue is *directly observable*, and (c) budget search calls to the scout rather than the session.

---

## 10. RECOMMENDATION

**Do not spend a full-time month on any candidate in this report.** Against the brief's own quality
bar, the honest answer is that this surface did not produce one.

The two findings actually worth carrying forward:

1. **Marketplaces cannot host this pattern** (§0). The landlord forces updates or delists. Four
   exhaustive scans, zero hits. Don't re-run them.
2. **"Dead incumbent" is not by itself an opening.** In 5 of 7 kills, the incumbent was genuinely
   dead *and it didn't matter*, because a healthy cheap competitor was already absorbing the
   refugees. The brief warned that "expensive" alone is not an opening; the sharper rule this cycle
   produced is: **an opening requires the refugees to have nowhere good to go.** That test should be
   applied *before* evidence-gathering in future cycles, because it is cheap and it kills fast.

If one candidate must go forward, it is **Marmalead (5/10)** — solely because it is the only one with
a verified large paying base (260,503 shops), verified published pricing, and verified recent public
anger. But its "dead product" half is unproven and eRank is actively maintained, so I expect it to
die at the competitor test.
