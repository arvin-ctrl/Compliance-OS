# SCOUT 01 — CAPABILITY OVERHANG

**Cycle:** 01 · **Date:** 2026-08-27 · **Surface:** work that was impossible or uneconomic 18 months ago,
is cheaply possible now, and whose incumbents have not repriced.

**Method note / limitation, stated up front:** this session exhausted its shared web-search budget
(200/200 calls) partway through. Roughly the last third of the work was done with direct page fetches
against known URLs. Reddit, Fiverr and the EFA rate page are all bot-blocked from this environment, so
three numbers I wanted (Fiverr gig order counts, r/genealogy thread volume, the EFA rate table read
first-hand) are marked **UNVERIFIED** below rather than asserted. Everything else carries a URL.

---

## HEADLINE FINDING — the shape of the overhang on this surface

The naive version of this surface ("a capability shipped and nobody built the product") is **mostly dry**.
Every 2025-2026 capability I probed already has entrants. What is *not* dry, and what I did not expect, is
the **price** overhang:

> **Vendors adopted the model and kept the human price.**

The cleanest instance: PDF/document accessibility. Continual Engine's own vendor round-up
(published 2025-09-24, updated 2026-08-21) lists ten remediation providers and describes **seven of the ten
as already "AI + human"** — and the per-page prices on those same vendors' pricing pages are still
**$4.00–$11.50 per page** (Accessible.org's live page today: *"PDFs start at $7.50/page"*). Mistral's OCR,
launched **2025-03-06**, reads a page for **$0.001–$0.002**. That is a 3,000–10,000× gap held open not by a
missing capability but by an unchallenged price.

So the operative question for this surface is not "what can a machine now do?" It is:
**"where is the human price still being charged, and can we reach the payer without a sales motion?"**
Gate 1 is what kills almost everything here — the biggest, best-evidenced price gaps (government document
remediation, lease/title abstraction, VPATs) sit behind procurement.

The candidates below are ordered by how well they survive Gate 1, not by size of gap.

### The clock, in one table (dated price collapses this surface runs on)

| What changed | When | Verified figure | Source |
|---|---|---|---|
| Per-page document OCR/structure extraction | **2025-03-06** | Mistral OCR launches at **~$1 per 1,000 pages** (batch: 2,000 pages per $1) | [pureai](https://pureai.com/articles/2025/03/11/mistral-ai-launches-aipowered-ocr.aspx) |
| Same, next generation | **Dec 2025** | Mistral OCR 3 at **"$2 per 1,000 pages"**, **"$3 per 1,000 annotated pages"**, 50% batch discount | [VentureBeat](https://venturebeat.com/technology/mistral-launches-ocr-3-to-digitize-enterprise-documents-touts-74-win-rate) · [mistral.ai/pricing](https://mistral.ai/pricing) ("Batch processing, for high-volume work, reduces the price by 50%") |
| Real-time voice | **Oct 2024 → Aug 2025** | $100/$200 per 1M audio tok (Oct-24 beta) → $40/$80 (Dec-24) → **"$32 / $64 with cached input at $0.40"** at Aug-2025 GA ≈ **$0.05/conversation-minute** | [forasoft](https://www.forasoft.com/blog/article/openai-realtime-api-pricing) |
| Whole-corpus context | current | Claude Opus 5 / Sonnet 5 both **1M context**, $5/$25 and $2/$10 per MTok; Batch API 50% off; prompt caching | `claude-api` skill model table, cached 2026-06-24 |
| A US legal deadline that makes exhaustiveness mandatory | rule published **2024-04-24** | DOJ Title II web rule adopts **"WCAG 2.1, Level AA"**; compliance **April 26, 2027** (pop ≥50,000) and **April 26, 2028** (<50,000 / special districts) | [ada.gov](https://www.ada.gov/resources/2024-03-08-web-rule/) |

---

# CANDIDATES

---

## C-01 · Exhaustive parish/civil-register indexes from 18th–19th c. handwriting

**One sentence:** Machine-read an entire handwritten parish or civil register — all 500–2,000 pages of
Kurrent, Sütterlin, secretary hand or ecclesiastical Latin — and sell the complete, searchable, translated
index of every entry in it, a thing no human would produce at any price.

### 1. The artifact
A per-register product: every baptism/marriage/burial entry as a structured row (date, names, ages, parents,
godparents, occupations, residences, marginalia), each row linked to a cropped image of the source line, plus
a plain-English translation of the entry and a downloadable CSV/GEDCOM. Sold per register (or per
surname-slice of a register). Secondary artifact: single-document transcription+translation, $5–15, which is
the acquisition funnel.

### 2. Evidence — **T1 + T2**
- **T1, money moving for the worse version.** Cyndi's List "Languages & Translations — Professionals,
  Volunteers & Other Research Services" carries **48 links**, of which the fetched page names commercial
  services incl. *Germanology Unlocked*, *EK Translations*, *Entziffer-mich* ("Transcription and translation
  of old handwritten documents (letters, diaries, certificates etc.)"), *Genealogy Translations* ("Translate
  any genealogy record in any language for you in 24 hours or less"), *Esther Bauer Ph.D*, *Charter Oak
  Genealogy*, *Ann Sherwin*. https://www.cyndislist.com/languages/professionals/ (fetched 2026-08-27)
- **T1, published unit prices.** Live Fiverr gigs, price in the listing title:
  `archivium` **$10** (transcribe old German handwriting),
  `linguistdani` **$10** (per page, max 200 words),
  `fivetonsofflaxx` **$10** (Kurrentschrift/Sütterlin),
  `clarawinter` **$20**, `sjdonaldson` **$25**, `fabiank_` **$30**.
  URLs e.g. https://www.fiverr.com/archivium/transcription-of-old-german-handwriting ·
  https://www.fiverr.com/fabiank_/transcribe-old-german-text-and-handwriting
  **Order/review counts UNVERIFIED** — Fiverr returns HTTP 403 to this environment.
- **T2, demand visibly exceeds supply, and is *rationed*.** PolishOrigins' translation guidelines instruct
  requesters to post **"no more than 5 translation requests a month and no more than 25 a year in given
  language."** https://polishorigins.com/records-translations-guidelines/ — a queue-management rule is
  direct evidence of unmet demand.
- **T1, the incumbent tool still meters by the page.** Transkribus: Free = **"50 credits every month at no
  cost"**; Scholar **"€99 / year"**; Team **"€449 / year"**; **"Handwritten Text Recognition 1 credit /
  page"**; 250-credit top-up **"59,50 €"**. https://www.transkribus.org/pricing (fetched 2026-08-27).
  That is ~€0.24/page for *raw text only* — no translation, no structure, no entry-level parsing.

### 3. The clock
Transkribus's model — the pre-2025 state of the art — requires a **model trained per hand/collection** to
work well, which is why full-register indexing never happened: the setup cost exceeded the value for any one
family. General-purpose VLMs read arbitrary period hands zero-shot as of the 2025 model generation, and at
Opus-5/Sonnet-5 pricing (1M context, $2–5 per MTok input, **50% off via Batch**) a 1,500-page register costs
single-digit dollars end to end. The *exhaustive* version became possible in 2025; it was flatly impossible
in 2024.

### 4. First ten users — **named**
- The 48 services in the Cyndi's List category above: they are both the demonstrated demand *and* a
  wholesale channel (they currently do this by hand at $10–30/doc).
- The FamilySearch Community **"Germany Research"** group, which runs a continuous queue of translation
  requests: https://community.familysearch.org/en/group/discussions/88-germany-research/ (specific request
  thread: https://community.familysearch.org/en/discussion/101762/help-translate-german-record)
- PolishOrigins' translation forum (the rationing rule above tells you the queue exists).
- Fiverr itself: you can list the exhaustive-register product on the same search surface where the $10
  per-page gigs sit. No audience required — Fiverr and Etsy search *is* the distribution.
- I could not verify r/genealogy volume (Reddit blocks this environment). Do not plan on it until checked.

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **PASS** — Fiverr/Etsy search demand + 48 named existing suppliers + FamilySearch/PolishOrigins queues. Buyer is an individual paying out of pocket; no sales call. |
| **G2 observable demand** | **PASS** — T1 published prices from ~7 Fiverr sellers and a 48-entry professional directory; T2 rationed volunteer queues. |
| **G3 buildable by us** | **PASS** — VLM + a locator/QA harness + image cropping. No credential, no licence. Source images are free (FamilySearch, Matricula, regional archives). |
| **G4 self-verifiable in 14 days** | **PASS** — pick one published register with an existing human-made index, run ours, measure entry recall and name accuracy against it. Zero strangers involved. |
| **G5 the clock** | **PASS** — zero-shot period-hand reading is a 2025 capability; Transkribus still charges 1 credit/page for text only. |

### 6. What already exists, and why it is inadequate
Transkribus (text only, per-hand model training, no translation, no entry parsing). FamilySearch/Ancestry
indexes (name-only, incomplete coverage, high error, no marginalia, and locked to their platform).
Forty-eight human services (per-document, $10–30, 24h+, will not do a whole register at any price).
**Nobody sells the exhaustive artifact** — because until 2025 nobody could.

### 7. Price signal
$10–$30 per document, human. A 1,500-page register = $15,000–$45,000 at that rate. Our cost: single-digit
dollars. The gap is the product.

### 8. Confidence: **7/10**
Docked for: the Fiverr order-count blind spot, and consumer price points (this is a $20–$200 product, so it
needs volume). Raised by: the only candidate here where the *exhaustive* version is genuinely unbuilt.

---

## C-02 · Condo/HOA governing-document review inside the statutory buyer window

**One sentence:** A buyer under contract uploads the 400–1,500 page HOA/condo document dump they were just
handed and gets, within minutes, the specific findings that decide whether to walk — pending special
assessments, reserve shortfalls, litigation, rental/pet caps, lender-disqualifying provisions.

### 1. The artifact
A dated report per property: red-flag list with page citations into the source documents, reserve-funding
math, every assessment mentioned anywhere in minutes or budgets, rental-cap and leasing-restriction
extraction, and a lender-warrantability checklist. Delivered inside the contractual review period.

### 2. Evidence — **T1**
- **What people pay a human today:** **"$300 to $1,500 is the typical 2026 attorney fee to review HOA
  documents."** (surfaced via search of PropFusion / GoverningDocs material, 2026)
- **A product already charges for the machine version and is priced 10-40× under the lawyer:**
  GoverningDocs — **"First full property report free with sign-up · $39 each after · No subscription"**
  https://governingdocs.dev/ (fetched 2026-08-27). No testimonials, no customer counts, no launch date on
  the page — an early solo entrant, not an incumbent.
- **Adjacent spend proving the documents matter:** Florida SIRS/reserve studies run
  **"$1,650 to $11,000"** standard and **"$5,500–$16,500+"** for a Structural Integrity Reserve Study.
  https://fpat.com/reserve-study-cost-florida/

### 3. The clock
Two things. (a) Long context: a 1,200-page CC&R + bylaws + 5 years of minutes + budget + reserve study is
~600k–1M tokens; it fits in one Opus-5/Sonnet-5 context window today and did not fit anywhere in 2024.
(b) Statute: **"Since January 1, 2026, Florida condos can no longer waive funding for structural
reserves"** — which is turning latent deferred maintenance into cash assessments that appear in minutes and
budgets, i.e. exactly the thing a buyer must find and can't.

### 4. First ten users
**Partially unnamed — this is the weak spot.** I can name the channel shape but not ten handles:
Florida/California condo buyer communities, buyer's agents (who currently either eat the review or send the
client to a lawyer), and FSBO/investor forums. GoverningDocs' existence proves someone thinks the channel
works; it does not prove it does. **Treat "can we reach buyers at contract-signature time" as the riskiest
assumption.**

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **MARGINAL** — consumer, self-serve, high commercial intent at a moment of fear, but I could not name ten specific people/threads. This is the gate to test first. |
| **G2 observable demand** | **PASS** — $300–$1,500 attorney fee is money moving now for the worse version; a $39 competitor exists. |
| **G3 buildable by us** | **PASS** — documents are supplied by the buyer. No data access problem. Caution: do not render legal advice; the artifact is extraction + citation, not opinion. |
| **G4 self-verifiable in 14 days** | **PASS** — condo docs are public in many FL/CA listings and estoppel packages; run against 30 real packages and score red-flag recall against the documents themselves. |
| **G5 the clock** | **PASS** — 1M context + FL structural-reserve non-waiver from 2026-01-01. |

### 6. What already exists
**GoverningDocs at $39/report** is the closest, and it is *not obviously inadequate* — it is simply early and
undistributed. Verdict: the moat here is distribution, not product. That is a real risk given our profile.

### 7. Price signal
$300–$1,500 (attorney) → $39 (first mover). Our realistic price: $39–$99.

### 8. Confidence: **6/10**

---

## C-03 · The film-festival deliverable pack (SDH / CC / open-caption / foreign subs)

**One sentence:** An indie filmmaker with an accepted festival submission uploads a cut and gets back the
exact accessibility deliverables the festival's tech spec demands, in the exact formats, by the deadline.

### 1. The artifact
Per title: an SDH track built to festival convention (speaker IDs, non-speech sound cues, on-screen-text
spotting, shot-change-aware timing), a closed-caption sidecar **and** a burned-in open-caption version,
DCP-compatible formats (.scc / .stl / .itt / .xml), plus translated subtitle tracks. Delivered against a
named festival's spec sheet.

### 2. Evidence — **T1**
- **The mandate, per festival, with dates.** Sundance: **"English (SDH)"** required; a **"Closed Caption
  version and an Open Caption version"** for DCP; deadlines **January 5, 2026** (features) and
  **December 19, 2025** (shorts). SXSW: **"Closed captions required for all screening formats"**, SDH
  **"strongly recommended"**. Berlinale deadline **January 28, 2026**; audio-description versions
  "should be flagged" (GRETA app). TIFF: CC and SDH "strongly recommended."
  https://www.gothamlab.com/film-festival-subtitle-requirements-the-complete-guide-for-2026/
- **Published human prices per minute.** FEPSS: **"$14 per video minute"** for subtitles, **"$16 per video
  minute"** EN↔ES. https://fepss.org/service/subtitle-services/ · Gotham Lab: **"starting from $6 per
  minute for translated subtitles"** · Vanan: **"starts at $1 per minute for captions in English and $7 per
  minute for other languages"** https://vananservices.com/captioning-services/film-captioning.php ·
  general market **"$4–$15 per minute"** for human transcription + translation + timing on
  "indie features and festival-ready subtitles."
- A 100-minute feature therefore costs **$400–$1,600** for one language pass, paid by an individual.

### 3. The clock
ASR + translation cost per minute is now rounding error; the 2025-2026 change that matters is that models
became good enough at **shot-change-aware timing, on-screen text spotting and non-speech event description
from the video track**, not just the audio track — the parts that make an SDH file festival-acceptable
rather than merely a transcript. Festivals also hardened the mandate: Sundance's requirement is now a
deliverable, not a courtesy.

### 4. First ten users
**Named channel, unnamed individuals.** FilmFreeway is the single funnel every submitting filmmaker passes
through, and acceptance→deliverable-deadline is a ~3-week panic window with a hard date (see the Jan 5 2026 /
Dec 19 2025 dates above). Festival-specific submitter Discords and r/Filmmakers are the obvious secondary.
I could not enumerate ten specific filmmakers within budget.

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **PASS (conditional)** — buyer is an individual, self-serve, with a hard external deadline and searchable intent ("Sundance SDH deliverable"). Conditional on FilmFreeway/festival-adjacent placement being reachable without ad spend. |
| **G2 observable demand** | **PASS** — $1–$16/min published prices across at least four vendors, and a festival mandate that creates the purchase. |
| **G3 buildable by us** | **PASS** — video in, sidecar formats out. The hard part is format/spec compliance, which is exactly the kind of fiddly deterministic work we are good at. |
| **G4 self-verifiable in 14 days** | **PASS** — take 10 public-domain/festival features with existing professional SDH, regenerate, and diff against the human file on timing, cue density and sound-event coverage. |
| **G5 the clock** | **PASS** — mandate dates Dec 2025/Jan 2026; the video-aware SDH capability is 2025-2026. |

### 6. What already exists
Rev/Descript (transcripts and generic captions, **not** DCP deliverables or festival conventions);
Gotham Lab, FEPSS, Capital Captions, Vanan (human, per-minute, the incumbents we are underpricing).
Inadequacy: the generic tools do not produce a festival-acceptable deliverable pack, and the specialist
shops charge human rates for a job whose marginal cost is now cents.

### 7. Price signal
$400–$1,600 per feature per language, human. Target: $49–$149 per title.

### 8. Confidence: **6/10**

---

## C-04 · Hudl-Assist arbitrage: the sports whose film is still tagged by hand

**One sentence:** Hudl sells film breakdown for $250–$1,700 per team per season and, by its own admission,
does it with human analysts tagging every play — for every sport except volleyball.

### 1. The artifact
Upload game film → get the tagged play index and stat report a coach currently pays Hudl Assist for:
every play with situation (down/distance/score/personnel/formation), outcome, and a clickable playlist per
player and per tag. Wedge: the sports Hudl has **not** automated (wrestling, lacrosse, water polo, field
hockey, rugby, and the football scout-game product).

### 2. Evidence — **T1, from the incumbent's own pages**
- **Prices, verbatim** (https://www.hudl.com/pricing/assist/football, fetched 2026-08-27):
  Standard Priority — **"Your Games $250 per team, per season"**, **"Your Games & Scout Games $750 per team,
  per season"**; Express — **"$400"** / **"$1,200"**; Standard Assist+ — **"$450"** / **"$1,250"**;
  Express Assist+ — **"$650"** / **"$1,700"**.
- **The humans, verbatim** (https://www.hudl.com/products/assist/faq, fetched 2026-08-27):
  **"For most sports, the core of Hudl Assist relies on a team of trained analysts who manually tag every
  play, event, and statistic"**; **"we're staffed 24/7 to keep pace."**
- **The exception proves the direction**: volleyball is **"Assist powered by Balltime AI"** using computer
  vision — so Hudl is repricing sport-by-sport, slowly, and has left the rest on human labour.
- Club pricing for other sports (via search, secondary): basketball **$900 / $1,300 / $1,500 per team per
  season** (as of January 2026); club soccer **$700 / $1,100**.
  https://www.hudl.com/pricing/club/assist/soccer

### 3. The clock
Long-video understanding at usable cost is a 2025-2026 capability. Hudl's own volleyball switch to Balltime
is the dated proof that the capability crossed the line — and that the other sports are un-repriced human
labour sitting in plain sight on a public pricing page.

### 4. First ten users
**Not named — I could not enumerate ten coaches within budget.** The channel is high-school and club coaching
communities (sport-specific coaching forums, coaching X/Twitter, athletic-director listservs). Note that
Hudl owns the film-exchange network, which is a genuine moat on *film access*, not on tagging.

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **MARGINAL/FAIL** — the buyer is a school or club with a budget cycle and an incumbent contract. This is the gate that most likely kills it. |
| **G2 observable demand** | **PASS, strongest of any candidate** — a public price list plus a vendor admission that humans do the work, 24/7. |
| **G3 buildable by us** | **MARGINAL** — the pipeline is heavy (tracking, event detection, per-sport rules) and Hudl controls film distribution. Skilled work, not access — but a lot of skilled work. |
| **G4 self-verifiable in 14 days** | **PASS** — public game film on YouTube exists in volume for every one of these sports; tag it and score against published box scores. No stranger required. |
| **G5 the clock** | **PASS** — dated: Hudl's own volleyball/Balltime switch. |

### 6. What already exists
Hudl Assist (human, priced above), Balltime (volleyball, inside Hudl), SportsVisio, Veo, Pixellot, Trace.
Adequate for basketball/soccer/volleyball; **not** shipped for the long tail.

### 7. Price signal
$250–$1,700 per team per season, currently paid, for humans watching video.

### 8. Confidence: **5/10** — best evidence on the sheet, worst distribution.

---

## C-05 · Agent-driven VPAT / Accessibility Conformance Report for SaaS vendors

**One sentence:** A SaaS founder who has just been asked for a VPAT by a government or university buyer gets
one produced by an agent that actually drives their product, instead of paying a consultancy $2,000–$15,000.

### 1. The artifact
A completed VPAT 2.5 / ACR (WCAG, Section 508, EN 301 549 or INT edition) with, per success criterion, the
evidence: the screen, the interaction path the agent took, the automated check result, and the remarks text.
Plus a prioritised remediation list.

### 2. Evidence — **T1**
- **Published prices for the human version**, https://accessible.org/pricing/ (fetched 2026-08-27):
  VPAT **WCAG edition "$350"**, **"Section 508: $550"**, **"EN 301 549: $650"**, **"INT: $950"** —
  *on top of* an audit at **"$100–$250 per page or screen, $25-$100 for light pages/screens"**;
  technical support **"$195/hour"** (2-hour minimum); user testing **"$550 per session"**.
- Consultancy fees for a full engagement: **"$5,000-$15,000"** traditionally; **"$2,000 to $5,000"** and
  **"$1,000–$3,000"** at the lower end depending on complexity (adacompliancepros, corpowid, 2026).
- The purchase is forced by a buyer: a VPAT is needed **"when selling to buyers who require accessibility
  documentation… demonstrates WCAG conformance to procurement agents."**

### 3. The clock
Computer-use / agentic browsing became reliable enough in 2025 to *operate* a logged-in SaaS product —
navigate, fill forms, trigger modals, tab through focus order — which is precisely what an accessibility
audit requires and what static scanners (axe, Lighthouse) cannot do. Before that, the manual-testing half of
a VPAT was irreducibly human. The DOJ Title II deadlines (**April 26, 2027** / **April 26, 2028**,
https://www.ada.gov/resources/2024-03-08-web-rule/) mean every vendor selling to a US state/local entity will
be asked for one before those dates.

### 4. First ten users
**Named channel, unnamed individuals.** The trigger event is public and searchable: a SaaS company that
appears on a state/university RFP or vendor list has been asked for an ACR. Founder communities (Indie
Hackers, r/SaaS) are the self-serve channel. I could not name ten.

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **MARGINAL** — buyer is a founder with a credit card and an urgent procurement blocker (good), but finding them at the trigger moment is unproven (bad). |
| **G2 observable demand** | **PASS** — four published VPAT edition prices, plus $1,000–$15,000 consultancy range. |
| **G3 buildable by us** | **PASS** — the bottleneck is agent engineering, not access. Liability: an ACR is a representation to a government buyer. We would be producing a document the customer signs, not signing it ourselves. That must be structured carefully. |
| **G4 self-verifiable in 14 days** | **PASS** — run the agent against products with *published* ACRs and score our findings against theirs. No cooperation needed. |
| **G5 the clock** | **PASS** — computer-use agents 2025; Title II deadlines 2027/2028. |

### 6. What already exists
AllAccessible — **"Generate Professional VPAT Reports In Minutes, Not Months"**
(https://www.allaccessible.org/vpat) — plus Accessible.org, DigitalA11Y, Skynet, ADA Compliance Pros as human
shops. The gap: existing "instant VPAT" tools are questionnaire wrappers around automated scans; none of them
*drives the product*. That is the only part that was impossible before 2025.

### 7. Price signal
$1,850–$15,000 all-in today; the VPAT document alone $350–$950.

### 8. Confidence: **5/10**

---

## C-06 · The academic monograph index

**One sentence:** Academic authors are contractually required to supply and personally pay for their book's
index, at $1,250–$1,562 for a 250-page book, for a job that is now a whole-corpus context problem.

### 1. The artifact
A Chicago-style back-of-book index against final page proofs: consolidated headings and subheadings,
cross-references, and — the part that actually matters — **verified page locators** tied to exact character
offsets in the proof PDF, in an editable form the author can hand the press.

### 2. Evidence — **T1**
- **The author pays, personally.** Multiple university presses: *"Unless otherwise agreed in a contract, it
  is the author's responsibility to index the book"*; if a professional does it, *"the author is usually
  responsible for paying for this."* (OUP, Cornell, UCL Press, Michigan author guidelines; Manuscript Works
  and dissertationtobook.com — businesses that exist specifically to coach academics through these costs.)
  https://global.oup.com/academic/authors/author-guidelines/index/ ·
  https://www.cornellpress.cornell.edu/author-guidelines/ · https://manuscriptworks.com/blog/costs
- **The price.** EFA 2026 guideline rates: **$5.00–$6.25 per 250-word page**, i.e.
  **$1,250–$1,562.50 for a 250-page book**; academic books **"$3.00-$6.00 per indexable page"**;
  *"anywhere from $1k–$2k give or take"* for a scholarly monograph.
  the-efa.org's own rate page is bot-blocked from here — figures are as quoted by
  https://www.mwediting.com/how-much-do-book-indexing-services-cost/ and https://indexbusters.com/book-indexing-rates/. **Verify first-hand before building.**
- **The trade body has publicly dug in — the classic overhang tell.** ASI statement, **updated March 25,
  2026**: **"AI tools based on large language models (LLMs), such as ChatGPT and Claude, do not produce
  viable book indexes, either in whole or in part"** … **"We recommend AI-generated indexes not be used in
  books."** https://asindexing.org/ai-news/statement-on-ai-and-book-indexing/

### 3. The clock
1M-token context windows across the current model generation mean a whole 120k-word monograph fits in one
pass — which is what a coherent index requires and what chunked 2023-2024 pipelines could never do. Batch
pricing (50% off) makes the many-pass approach cheap.

### 4. First ten users
Academic authors at page-proof stage. Named adjacent businesses that already sell to exactly this person and
could channel: **Manuscript Works** (manuscriptworks.com) and **dissertationtobook.com**. Individuals not
named.

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **PASS** — individual pays out of pocket, self-serve, at a known moment (page proofs), with two named coaching businesses serving the same person. |
| **G2 observable demand** | **PASS** — $1,250–$1,562 paid by individuals; three commercial AI entrants already selling. |
| **G3 buildable by us** | **PASS** — LLM for concept selection + deterministic offset→locator mapping. The locator half is engineering, not modelling, which is where the entrants are weakest. |
| **G4 self-verifiable in 14 days** | **PASS** — take 20 published monographs with human indexes, regenerate from the text, score topic overlap and locator precision against the printed index. |
| **G5 the clock** | **PASS** — 1M context; ASI's dated defensive statement (2026-03-25). |

### 6. What already exists — **and this is why confidence is low**
- **Indexia** (https://www.indexia.tech/): **"We charge $0.0015 per token… indexing a 60,000-word manuscript
  would cost about $90."** Testimonials from **Philip Alston (NYU Law)** and **Stephen G. Brooks
  (Dartmouth)**; claims authors from Rice/Stanford/Dartmouth/Emory/Northwestern/CMU/Melbourne and users at
  Oxford, Cambridge, Princeton, Harvard and Chicago presses; **StartX** accelerator.
- **IndexerLabs** (https://indexerlabs.com/ai-book-index-generator): **"Subject book indexing starts at $99
  per book, with $199 and $299 tiers available at checkout"**; trained a purpose-built model,
  **"IndexLM-1.0 was trained on more than 1,000 real-world back-of-book indexes"**, **"tested across 20,000
  locator claims"**, reporting **57%** human-topic overlap vs Claude 29% / Gemini 18% / GPT 15%.
- **IndexAI** on Leanpub (one-click index for Leanpub books).

**Honest read:** the overhang is real and the price gap is 13×, but **"nobody productised it" is false**.
Two funded/serious entrants are already at $90–$299 with academic references. Submitting this as a candidate
requires an argument for why we beat IndexLM-1.0, and I do not have one.

### 7. Price signal
$1,250–$1,562 human → $90–$299 machine, already in market.

### 8. Confidence: **4/10** — included for completeness and for the ledger, not because I would spend a month on it.

---

## C-07 · Wholesale per-page document remediation engine (the price-overhang play)

**One sentence:** Ten named vendors already use AI to remediate documents for accessibility and still charge
$4.00–$11.50 per page; the engine underneath could be sold at $0.10.

### 1. The artifact
An API: PDF/DOCX/PPTX in, a tagged, reading-order-correct, alt-texted, table-structured, PDF/UA-conformant
file out, with a per-file conformance report. Priced per page, self-serve, no minimum.

### 2. Evidence — **T1**
- **Live per-page prices, fetched 2026-08-27** from https://accessible.org/pricing/ :
  **"PDFs start at $7.50/page"**, **"Word Documents start at $7.00/page"**, **"PowerPoints starts at
  $7.00/page"**.
- **The rest of the market, same range:** Documenta11y **"Starting at $4 per page"**; Allyant **"$5–$8 per
  page for standard PDFs"**; Softek **"$5–$30 per page"**; Accessible.org **"$7.50–$11.50 per page"**;
  market range **"$5–$25 per page depending on document complexity"**.
  https://venngage.com/blog/pdf-accessibility-cost/
- **They already have the AI.** Continual Engine's vendor round-up (published **2025-09-24**, updated
  **2026-08-21**) classifies 7 of 10 providers as AI-automated or "AI + Human Expert Review"
  (Continual Engine, Equidox, GrackleDocs, CrawfordTech, Documenta11y, PDFix, Allyant), and only three as
  human-only (TestPros, Be Accessible, Accessible.org).
  https://www.continualengine.com/blog/top-pdf-remediation-service-providers/
- **The forcing function, with dates:** DOJ Title II final rule published **April 24, 2024**, standard
  **"WCAG 2.1, Level AA"**, compliance **April 26, 2027** (population ≥50,000) and **April 26, 2028**
  (<50,000 or special district). https://www.ada.gov/resources/2024-03-08-web-rule/

### 3. The clock
Mistral OCR, **2025-03-06**, **~$1 per 1,000 pages**; OCR 3, Dec 2025, **"$2 per 1,000 pages"** with a 50%
batch discount. Structure/reading-order/table detection at $0.001–0.002/page against a $4–$11.50/page price.
This is the single largest verified unit-economics inversion I found on this surface: **~3,000–10,000×**.

### 4. First ten users
**FAIL — I cannot name them.** The end buyers are ~90,000 US state/local entities and their higher-ed
equivalents, all of which buy through procurement. The alternative (wholesaling to the ten vendors above) is
ten enterprise sales conversations.

### 5. Gate check
| Gate | Verdict |
|---|---|
| **G1 distribution** | **FAIL** — every path is a sales motion: government procurement, or B2B wholesale to incumbents who already have their own engine. |
| **G2 observable demand** | **PASS, emphatically** — four vendors' published per-page prices and a federal deadline. |
| **G3 buildable by us** | **PASS** — pure document engineering. |
| **G4 self-verifiable in 14 days** | **PASS** — PAC 2024 / veraPDF give a deterministic PDF/UA pass-fail; run 500 real government PDFs through and measure. |
| **G5 the clock** | **PASS** — dated to 2025-03-06 and the 2027/2028 deadlines. |

### 6-8.
**Closest competitor:** ten of them, seven already AI-powered, with government relationships.
**Price signal:** $4.00–$11.50/page. **Confidence: 3/10.**
**Recorded here because the price gap is the largest on the sheet and because the finding — "they adopted the
model and kept the price" — is the most useful generalisation this scout produced.** It is a Gate-1 kill for
*us*, not a bad market.

---

# CHECKED AND KILLED

Recording these so the ledger does not pay for them twice.

| Candidate | Kill | Evidence |
|---|---|---|
| **Medical-record chronology for PI firms** | **G2/G5 — already repriced, twice.** Offshore humans are at $25/hr (500-page chronology = **10 hours = $250**, https://www.medicolegalrequestllc.com/pricing/) and there are ≥5 AI entrants (Tavrn, RapidCare, Ares Legal, ProPlaintiff, LezDo). Per-page rates already **$0.90–$2.50**. No arbitrage left. | T1 |
| **Certified translation for USCIS** | **G1.** The arbitrage is real and enormous — RushTranslate **"$24.95 per page"**, Translayte **"$24.99 per page"**, market **$25–$40/page**, machine cost <$0.01 — but the entire channel is paid search and SEO, which our profile explicitly cannot buy at scale. Also already contested by AI entrants (certtranslate.com et al.). | T1, killed on distribution |
| **Audio description (WCAG SC 1.2.5)** | **G5 — the incumbents repriced during the window.** Human AD was **"$15 to $75 per minute"** (3Play, 2022-06-03) and 3Play's live pricing page now says the rate depends on **"what blend of AI and expert human review you require"**; Verbit sells "AI audio description" for **"large content libraries"** alongside human. The overhang closed in 2025-2026. | T1 |
| **Legal citation / hallucination checking** | **G2/G5 — crowded.** The clock is superb (Charlotin's AI Hallucination Cases database at **1,871 records as of August 11, 2026**; penalties up to **$15,000 per attorney** and a single matter at **~$109,700**) but at least six vendors are already selling into it (GC AI, HAQQ, Vaquill, Clearbrief, PlatinumIDS, Voibe). | T1/T2 |
| **Lease / title / document abstraction** | **G1.** Demand is visible — ZipRecruiter Aug 2026: Remote Abstractor **$19–$62/hr**, Title Abstractor **$30–$63/hr**, Lease Abstractor average **$82,454/yr**, ~87 employers hiring remote abstractors on Indeed — but every buyer is an enterprise with a procurement process. | T2, killed on distribution |
| **Pay-transparency job-posting sweeps** | **G1/G2.** 18 states + DC as of 2026, penalties **$1,000–$3,000 per posting** (NY), up to **$25,000** (MA) and **$250,000** (NYC unremedied), with MA and NJ actively auditing in 2026. But no observable money moving on the audit itself, and the only channel is cold outbound. | T2/T3 |
| **Systematic-review data extraction** | **G2/G5.** Standard practice is still dual human extraction and reviews cost ~$140k, but Covidence ($339/yr single review), DistillerSR, Elicit and a stack of 2025-2026 papers on AI-as-second-reviewer already occupy it. | T2/T3 |

## Sub-surfaces that came back genuinely dry (or unverifiable within budget)

- **Real-time voice.** The price collapse is real, dated and large (Oct-2024 $100/$200 per 1M audio tokens →
  Aug-2025 GA **"$32 / $64"**, ≈**$0.05/conversation-minute**). I could **not** attach an observable-demand
  buyer to it before the search budget ran out. Every candidate I generated (provider-directory verification,
  benefit verification, employment verification, apartment comp-shopping, CATI market research) is a B2B
  sales motion, and I could not price the human version from a primary source. **Recommend a dedicated pass
  next cycle** — this is the largest un-mined price collapse on the sheet.
- **On-device / offline models for privacy-sensitive work.** No T1 or T2 found. Every candidate I generated
  (ITAR/CUI defence, tax-preparer document handling under IRS Pub 4557, small-firm privileged review, K-12
  FERPA) either fails on procurement or is already served by cloud vendors offering BAAs/DPAs, which removes
  the reason to go local. **Reporting this as dry rather than padding it.**
- **"Demo went viral, nobody productised it."** In its literal form this is dry. Every 2025-2026 capability I
  probed — long context, computer use, cheap OCR, video understanding, handwriting — already has at least one
  commercial entrant. The exploitable version is C-01's shape: not "nobody built the product", but
  **"nobody built the *exhaustive* version, because exhaustiveness was the thing that was impossible."**

---

## RECOMMENDATION TO THE CYCLE

If one candidate goes forward from this surface: **C-01 (exhaustive register indexes)**. It is the only one
where the artifact literally could not exist in 2024, the demand is priced by ~7 named sellers and a 48-entry
professional directory, the queue is visibly rationed, the buyer pays personally, the distribution is
marketplace search rather than a sales call, and the 14-day test needs no stranger's cooperation.

The most useful *finding*, separate from any candidate, is the one in the headline: on this surface, the
incumbents largely **did** adopt the capability — and kept the human price. Where we can reach the payer
directly (C-01, C-02, C-03), that gap is a business. Where we cannot (C-07), it is just a fact.
