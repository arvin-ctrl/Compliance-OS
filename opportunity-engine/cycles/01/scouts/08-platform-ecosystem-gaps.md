# SCOUT 08 — PLATFORM ECOSYSTEM GAPS

**Surface:** App marketplaces (install counts + reviews as public demand data; the marketplace itself as cold-start distribution).
**Date of research:** 2026-08-27. All numbers pulled live on this date.
**Verdict on the surface: NOT DRY.** Eight candidates below, six of them carrying T1 or T2 evidence.

---

## 0. HOW THIS SURFACE WAS WORKED (method + what is actually verifiable)

Two data routes turned out to be open and machine-readable. Both are primary sources, not analyst material.

1. **`marketplace.atlassian.com/rest/2/addons?text=<query>`** — public, unauthenticated JSON. Returns
   `totalInstalls`, `averageRating`, `reviewCount` per app. This is a **live census of a paid B2B app
   market**, not a survey. Every Atlassian install/rating number in this document came from it on 2026-08-27.
2. **`jira.atlassian.com/rest/api/2/search?jql=...`** — Atlassian's own public issue tracker, unauthenticated
   JSON, with **vote counts** on feature requests and an explicit resolution/status field. This gives
   *demand with a number on it* plus, where status is `Not Being Considered` or resolution is `Won't Fix`,
   **the platform's written refusal to build it** — i.e. explicit permission.

The combination is unusually strong: for a given job you can read (a) how many customers asked the vendor for
it, (b) the vendor's refusal, and (c) exactly how many people are already paying a third party for a
substitute and how well that substitute is rated. That is the whole gate-2 question answered from primary
data in one pass.

**Routes that did NOT work, stated plainly so the next cycle does not repeat them:**
- Atlassian Marketplace *HTML* search (`/search?query=`) ignores the query server-side and returns the same
  default popular list. Only the REST API respects the query. I lost several calls to this.
- Shopify App Store `/search?q=` and `/categories/<slug>/all` are client-rendered → empty or 404.
  Working routes: `apps.shopify.com/categories/<slug>` and `apps.shopify.com/<app-slug>/reviews`
  (the latter accepts `?ratings[]=1` to isolate 1-star reviews — this is how the complaint quotes below
  were obtained).
- Chrome Web Store category pages render ratings but **not** user counts or review counts.
- monday.com marketplace is fully client-rendered; I could not obtain install or review counts. **monday.com
  is therefore listed below on economics only, with no demand evidence, and I am not submitting a
  monday.com candidate.**

**Caveat on Atlassian ratings.** An Atlassian Community post surfaced in search indicates the Marketplace is
mid-transition from a 1–4 star scale to a 1–5 star scale. I could not verify this at a primary source. It
means an `averageRating` near 3.3 may be less damning than it looks in isolation. **I have therefore leaned
on *relative* ratings within a category and on *quoted review text*, not on absolute star values.** Treat
every absolute star number below as directional; treat the quoted complaints and the install counts as hard.

---

## 1. PLATFORM ECONOMICS AND PLATFORM RISK (gate-3 screen, run FIRST)

The brief asks for revenue share and platform risk per platform. This screen eliminated four platforms
before any idea was generated, which is the correct order.

| Platform | Take rate | Who bills the customer | Verdict |
|---|---|---|---|
| **Atlassian (Forge)** | **0% up to $1M lifetime Forge revenue**, then 16% (from 1 Jan 2026), 17% (from 1 Jul 2026) | **Atlassian** | **BEST** |
| **Shopify** | 0% on first $1M **lifetime**, then 15% | **Shopify** | **GOOD** |
| **monday.com** | 0% until $200k lifetime, then 15% | **monday.com** (mandatory since Jul 2024) | **GOOD** (no demand data obtainable) |
| **GoHighLevel** | 15% | Platform | OK |
| Atlassian (Connect, legacy) | 20% (1 Jan 2026) → **25%** (1 Jul 2026) | Atlassian | Build Forge, never Connect |
| **HubSpot** | 0% — but **ISVs bill customers directly** | You | Fails the "platform solves payments+trust" test |
| **Chrome Web Store** | n/a — **Google shut down Web Store Payments (wound down 2020–2021)** | You | Distribution only, never billing |
| **Xero** | **App Store billing being retired 2 Mar 2026**; payouts cease end of Jun 2026; developers moved to API tiers **$0–$895/month** | You, from Jun 2026 | **DISQUALIFIED** |

### Sourced detail

- **Atlassian, 0% to $1M.** `atlassian.com/blog/development/updates-to-marketplace-revenue-share-2026`,
  post dated **5 May 2025**: *"0% revenue share for eligible Forge earnings"* up to *"$1 million in lifetime
  Forge revenue"*, effective **1 Jan 2026**; 16% above it from 1 Jan 2026, 17% from 1 Jul 2026. Connect goes
  to **20% on 1 Jan 2026 and 25% on 1 Jul 2026** — a deliberate squeeze to force Connect→Forge migration.
- **Shopify.** Developers keep 100% of the first **$1,000,000 USD**, 15% above. **Platform risk, dated:**
  Shopify **rolled this back from *annual* to *lifetime*** with Partner Program Agreement changes effective
  **16 June 2025**. That is a documented unilateral worsening of developer economics. Assume it can happen
  again.
- **monday.com.** `developer.monday.com/apps/changelog/announcing-the-revshare-program`: *"Once an app
  reaches the milestone of $200,000 in lifetime accumulated revenue, the revenue sharing model is
  activated"*, then *"85% ... to the developer and 15% ... collected by monday.com"*. Launched **1 Sep 2024**.
  Built-in monetisation **mandatory for all new marketplace apps from July 2024**.
- **Xero — the cautionary tale, and the reason this screen runs first.** Xero is retiring App Store billing
  from **2 March 2026**, requires partners to move customers to their own billing by **30 June 2026**, and
  replaces revenue share with **five API tiers charging $0 to $895/month**. A developer who built on Xero in
  2024 lost platform billing *and* acquired a five-figure annual API bill. **Do not build on Xero.**
- **Chrome Web Store.** Google shut its own payments system down (deprecated 2020, off by 2021). Billing,
  subscriptions, refunds, tax and reconciliation are all yours. Fails the brief's preferred criterion.

### Platform absorption risk (does the platform eat successful apps?)

- **Atlassian: YES, demonstrably.** Atlassian acquired Code Barrel (Automation for Jira) and made automation
  native; Portfolio for Jira became native Advanced Roadmaps. **Mitigation that actually works:** pick jobs
  Atlassian has *put in writing* it will not do (`Not Being Considered` / `Won't Fix`). Candidates 2, 3, 7
  and 8 below are all built on written refusals. This is the single most important design rule on this
  surface.
- **Shopify: YES, and it cuts both ways.** Shopify acquired **Codisto** and rebranded it **Marketplace
  Connect** (candidate 5 — and it has since rotted, see the reviews). Conversely Shopify **withdrew its own
  Order Printer app** — `apps.shopify.com/order-printer` now returns *"This app is not currently available on
  the Shopify App Store"* — and the third-party replacements (Order Printer Pro, Vify) both sit at **4.9**.
  Shopify both eats categories and abandons them.
- **Live warning, unverified:** search surfaced claims that **Shopify will not allow new custom apps after
  2026**. I could not confirm this at a Shopify primary source and my search budget was exhausted.
  **Flagged `UNVERIFIED` — verify before committing to Shopify.**

### Does a marketplace actually deliver cold-start distribution?

The postmortem's strongest counter-example is Document Crunch: **187 installs against 17,850 Procore
customers** after four years. That is the right thing to be afraid of. The Atlassian census contradicts it
for *this* marketplace — small vendors reach real install bases:

- codefortynine, **Deep Clone for Jira — 12,100 installs**
- SaaSJet, **Time in Status — 5,400 installs**
- HeroCoders, **Clockwork Lite — 7,046 installs**; Clockwork Pro — 4,646
- Cappsule, **Timesheet Tracking for Jira — 13,368 installs**
- Big Fig Tree, **Default Values for 'Create Issue' — 2,504 installs**

These are small teams, several of them effectively one- or two-person shops, on five-figure install counts.
**This is the strongest single argument for the whole surface** and the reason I rate Atlassian above
everything else available to this operator.

---

## 2. CANDIDATES

Ordered by my confidence. I have killed two of my own along the way (§3).

---

### CANDIDATE 1 — Scheduled Entra ID / Intune → Jira Service Management Assets sync
**Confidence: 8/10.** My strongest. Narrow, dated, written-refusal-backed, tiny build.

**1. One sentence.** JSM Assets can only import your Microsoft directory by someone clicking a button;
this keeps your CMDB continuously and correctly in sync on a schedule, including devices from Intune.

**2. The artifact.** A Forge app that runs scheduled recurring imports from Microsoft Entra ID and Intune
into JSM Assets object schemas, correctly maps enabled/disabled account state, and emails an admin a
per-run reconciliation diff (objects created / updated / gone stale).

**3. Evidence — T1 + T2.**
- **The platform's written refusal (T2, hard vote count).** `JSDCLOUD-10502` *"Azure Integration for JSM
  Assets"* — **476 votes**, status **"Not Being Considered"**, created **2021-10-20**, last updated
  **2026-08-26** (i.e. still being commented on the day before this research).
- **The incumbent is a free, unsupported first-party beta (T2).** `JSM Assets - Microsoft Entra ID (Azure AD)
  Beta Integration`, vendor **Atlassian Labs**, app id 1232506 — **1,469 installs, 3.0/5, 16 reviews,
  "Free app", support status "Unsupported"**.
- **The complaint pattern is one single missing feature, quoted verbatim with dates:**
  - **Tim Johnson, 25 Aug 2026** (two days before this research): *"Needs scheduled/recurring imports,
    expanded support to other objects like devices (especially Intune)"* — and explicitly points readers to
    paid alternatives.
  - **Marina Jambrošić, 20 Jan 2026:** *"It's missing scheduling imports. Disabled users are often syncing
    as enabled"* — and expresses disappointment at the lack of progress.
  - **Ramesh Saravanan, 6 Jun 2025:** *"It's been disappointing so far, as it's simply not working as
    expected. I'm not sure why the tool was released in this state."*
- **Money is already moving for the better version (T1).** Paid third parties in the same slot, all rated
  far above Atlassian's free one: **Pio, "Azure AD (Microsoft Entra ID) Importer for JSM Assets" — 599
  installs, 4.77/5, 16 reviews**; **Deviniti, "Entra ID (Azure AD) Attributes Sync for Jira" — 911 installs,
  4.52/5, 21 reviews**; **Onward, "OnLink Import for Assets, Entra ID, Intune, Okta, Iru, Jamf" — 201
  installs, 5.0/5, 18 reviews**; **Sykora IT, "Azure Sync for Jira Assets" — 128 installs, 4.82/5**.
  ~1,840 paid installs across four vendors for a job the platform gives away badly.

**4. The clock.** Atlassian shipped the free Labs beta and then left it: **476 votes moved to "Not Being
Considered"**, and the newest review (**25 Aug 2026**) still asks for the same missing feature first raised
in the **6 Jun 2025** review. Fifteen months, no scheduling. Combined with **Forge 0% revenue share from
1 Jan 2026**, the window is open now.

**5. First ten users — named, public, reachable without a warm intro.**
- The three named reviewers above (**Tim Johnson**, **Marina Jambrošić**, **Ramesh Saravanan**) are public
  commenters on app id 1232506 who have each stated the exact missing feature.
- The **476 voters and the commenters on `jira.atlassian.com/browse/JSDCLOUD-10502`** are public and named
  on the ticket, still active as of 2026-08-26.
- Posting the app as an answer *on that ticket* and on the corresponding Atlassian Community thread is a
  legitimate, on-platform, non-spam distribution move — the ticket exists to collect exactly this.

**6. Gate check.**
- G1 distribution — **PASS.** Named public reviewers + 476 named voters on a live ticket + marketplace search.
- G2 observable demand — **PASS.** ~1,840 paid installs across four vendors; 1,469 on the free broken one.
- G3 buildable — **PASS.** Microsoft Graph API (documented, public) → JSM Assets REST. Forge scheduled
  triggers are a first-class primitive. No proprietary data, no credential.
- G4 self-verifiable in 14 days — **PASS.** Free Atlassian Cloud dev instance + free Entra tenant; prove a
  scheduled import with correct enabled/disabled mapping alone, no stranger required.
- G5 clock — **PASS.** "Not Being Considered" + 0% Forge revenue share from 1 Jan 2026.

**7. What already exists.** Pio (599 installs, 4.77) is the real competitor and is *good*. **This is the
honest weakness of this candidate.** The wedge is Intune **device** objects (Tim Johnson, 25 Aug 2026, asks
for this specifically and no incumbent name suggests device coverage except OnLink at 201 installs) and the
disabled-user correctness bug. This is a *share-taking* play in a proven category, not virgin ground.

**8. Price signal.** Incumbents are paid per-user Marketplace apps; I did **not** capture Pio's or Deviniti's
price points (Marketplace pricing tabs did not render for me). **`UNVERIFIED` — get these before building.**

**9. Confidence: 8/10.**

---

### CANDIDATE 2 — Markdown ⇄ Jira/Confluence round-trip, built for AI-generated text
**Confidence: 8/10.** Biggest vote count of anything I found that still has no good app.

**1. One sentence.** Paste markdown from an AI assistant into Jira or Confluence and have it arrive as
correctly formatted content — and get clean markdown back out.

**2. The artifact.** A Forge app adding a "Markdown" mode to the Jira work-item description and the
Confluence editor: paste/import markdown → native ADF; export any page or issue back to faithful markdown;
handles code fences, tables, nested lists, task lists, and Mermaid.

**3. Evidence — T2, very heavy, plus a whole category of failing incumbents.**
- **`JRACLOUD-72631` "Provide users with a plain text markdown editor" — 1,749 votes, 508 watchers,
  status "Future Consideration", created 2019-07-30.**
- **Atlassian's own PM, on the ticket, January 2025 — Kieran Gray:** *"This work is not currently roadmapped,
  so I cannot provide a timeframe right now as to a resolution date however I will provide an update in the
  coming months should there be a change."* That is a soft refusal in writing, 19 months old.
- **Every single incumbent in this category is rated poorly.** This is the tell — it is not that nobody has
  tried, it is that everybody has tried and failed:

| App | Vendor | Rating | Reviews | Installs |
|---|---|---|---|---|
| Markdown Rich Text Editor for Jira (LaTeX, Mermaid UML) | Fulstech | **2.68** | 14 | 300 |
| Markdown Editor for Confluence | Narva Software Labs | **3.13** | 6 | 1,469 |
| Render Markdown | StreamlineSoft | **3.46** | 26 | 3,887 |
| Markdown for Confluence | Appfire | **3.52** | 16 | 2,305 |
| Markdown Extensions for Confluence | Appfire | **3.52** | 22 | 764 |
| Alt Text — Markdown and Source Editor | Hugemassive | 3.75 | 3 | 62 |
| Markdown Importer for Confluence Cloud | Yamuno Software | 4.06 | 4 | 941 |
| Markdown Exporter for Confluence | Narva Software | 4.20 | 22 | 2,265 |
| Just Add+ (Embed Markdown, Diagrams, Code) | Modus Create | 4.25 | 50 | **8,352** |

- **~20,300 combined installs** across a category where **the best-rated meaningful app is 4.25 and two
  Appfire apps sit at 3.52**. Appfire is the largest consolidator in the ecosystem and it cannot get this
  above 3.52.

**4. The clock.** Two things changed. (a) **Atlassian said in Jan 2025 it is not roadmapped** — after
1,749 votes. (b) The volume of machine-generated markdown exploded: every coding assistant, every LLM chat,
every agent emits markdown, and the destination for a lot of it is a Jira ticket or a Confluence page. The
2019 ticket was about developer keyboard preference; the 2026 job is *interoperability with machine output*,
which is a materially larger and newer job than any incumbent was designed for.

**5. First ten users.** The **1,749 voters and 508 watchers on `JRACLOUD-72631`** are public and named on the
ticket, and the ticket is the single best-targeted list of buyers for this product in existence. Also: the
reviewers leaving sub-4 reviews on the nine apps above are named on those listings.

**6. Gate check.**
- G1 — **PASS.** 1,749 named voters + 508 watchers on one public ticket; marketplace search intent is high.
- G2 — **PASS.** ~20,300 installs already paid/installed for inadequate versions; 1,749 votes.
- G3 — **PASS.** ADF ⇄ markdown conversion is pure, well-understood, testable software. Atlassian publishes
  the ADF schema. **This is exactly "the bottleneck is skilled work, not access."** It is also the kind of
  problem where an AI-agent-heavy operator has a real edge: the work is a very large volume of
  fixture-driven edge-case conversion tests, which is our strongest build mode.
- G4 — **PASS.** Build a conversion corpus of 300 real-world markdown documents and measure fidelity
  round-trip. Zero strangers involved. This is a genuinely excellent 14-day test.
- G5 — **PASS.** Jan 2025 "not roadmapped" + AI markdown volume + Forge 0%.

**7. What already exists.** Nine apps, listed above with numbers. **Why they are inadequate:** they split the
job — importers that do not export (Yamuno), exporters that do not import (Narva Exporter), renderers that
put markdown in a macro island rather than converting to native content (Render Markdown, Just Add+). The
1,749-vote request is for *native editing*, and the macro-island approach is why ratings cluster at 3.5.
**Risk to be honest about:** Atlassian could ship this natively; it is a core-editor feature and the ticket
is "Future Consideration", not "Not Being Considered". This is a weaker permission signal than candidate 1.

**8. Price signal.** Not captured. **`UNVERIFIED`.** Appfire and K15t sell comparable Confluence content
utilities as paid per-user apps (K15t's Scroll PDF Exporter: 8,926 installs, 4.72, 226 reviews) which
establishes that content-format utilities are a paid category on this marketplace — but I did not read the
dollar figures.

**9. Confidence: 8/10.**

---

### CANDIDATE 3 — Jira ↔ GitHub sync that actually syncs
**Confidence: 6/10.** Largest install base I found anywhere; hardest competitive field.

**1. One sentence.** A reliable replacement for Atlassian's free GitHub integration, which 136,788 teams have
installed and which repeatedly fails to sync.

**2. The artifact.** A Forge app that mirrors GitHub branches/PRs/commits onto Jira work items with an
explicit, inspectable sync state (last sync, what failed, retry), plus branch creation that honours a
configured naming convention.

**3. Evidence — T1 + T2, unusually strong on both.**
- **`GitHub for Atlassian`, vendor Atlassian, "Free app" — 136,788 installs, 3.34/5, 509 reviews.** That is
  the largest install count I encountered on this surface, attached to the lowest first-party rating.
- **Quoted complaints, dated:**
  - **Tam Pham, 10 Apr 2026:** *"Please improve Github integration. The create branch doesn't apply the
    saved branch format. The list of branches is limited."*
  - **tiktakaz, 10 Apr 2026:** *"Extremely frustrated with this app. I've tried every possible
    troubleshooting step... no data is synced... this is a deep-rooted issue... It feels like a lottery
    rather than a professional tool."*
- **Money is moving for the better version (T1).** **GitKraken, "Git Integration for Jira (GitHub, GitLab &
  Azure DevOps)" — 8,696 installs, 4.41/5, 343 reviews**, paid. 8,696 teams pay to escape a free app.
- **The rest of the field is also failing**, which shows the job is unserved rather than served:
  GitHub's own **`GitHub Copilot for Jira` — 2,477 installs, 2.52/5**; Move Work Forward **`GitHub Links for
  Jira` — 658 installs, 2.66/5**; Shim Technologies **`Create GitHub Branches from Jira` — 511 installs,
  2.94/5**; GitConnector **`GitHub connector for Jira` — 253 installs, 2.92/5**.

**4. The clock.** GitHub's own Copilot-for-Jira app launched recently and sits at **2.52/5 across 2,477
installs**, i.e. the AI-era entrant is worse than the incumbent. The branch-naming complaint (10 Apr 2026)
matters more now because agentic coding tools create branches programmatically at volume.

**5. First ten users.** Named reviewers **Tam Pham** and **tiktakaz** (10 Apr 2026) on the Atlassian listing;
the 509 reviewers of `GitHub for Atlassian` and the 20 reviewers of Shim's 2.94-rated branch app are public
and named. Sub-3-star reviewers on a free first-party app are a clean, self-identifying prospect list.

**6. Gate check.**
- G1 — **PASS.** Named reviewers; category search volume implied by 136,788 installs.
- G2 — **PASS, T1.** 8,696 paid installs at GitKraken is money already moving.
- G3 — **PASS with reservation.** GitHub API + Forge is straightforwardly buildable. The reservation is
  competitive, not technical: GitKraken is a funded company already doing it at 4.41.
- G4 — **PASS.** Reproduce the reported sync failure and branch-format bug on our own instance in days.
- G5 — **WEAK.** No dated platform change. The clock here is "the incumbent is broken", which is a condition,
  not an event. **This is the gate this candidate is weakest on.**

**7. What already exists.** GitKraken at 4.41/8,696 installs is a *competent* incumbent. **If the wedge is
"general Jira-GitHub integration", this should be killed** — GitKraken adequately serves it. It survives only
as the narrow wedge: **branch creation that respects a naming convention**, where the dedicated incumbent
(Shim, 511 installs) is rated **2.94** and Atlassian's own is broken per Tam Pham.

**8. Price signal.** GitKraken's Marketplace pricing page did not render dollar amounts for me.
**`UNVERIFIED`.** 8,696 paid installs is nonetheless a hard demand fact independent of the price point.

**9. Confidence: 6/10.**

---

### CANDIDATE 4 — Jira "default values for system fields"
**Confidence: 6/10.** The highest-voted Jira Cloud request in existence, 22 years unbuilt.

**1. One sentence.** Set default values for Jira's built-in fields so every new ticket arrives pre-filled
correctly instead of blank.

**2. The artifact.** A Forge app letting an admin define per-project, per-issue-type defaults for system
fields (priority, components, versions, assignee, labels, due date), applied on the create screen.

**3. Evidence — T2.**
- **`JRACLOUD-4812` "Default values of system fields" — 2,799 votes, status "Future Consideration", created
  2004-10-06.** This is the **single highest-voted open suggestion in the Jira Cloud project** of everything I
  queried. **Twenty-two years open.**
- **Related, also unbuilt:** `JRACLOUD-3523` *"Cannot change the default assignee"* — **198 votes,
  resolution "Won't Fix"**, created 2004-04-01.
- **The incumbent is mediocre and under-penetrated:** Big Fig Tree, `Default Values for 'Create Issue' screen
  — Issue Templates` — **2,504 installs, 4.09/5, 26 reviews**. **2,799 votes vs 2,504 installs** — roughly
  one install per voter, on a 4.09-rated app, meaning the request is *still* being voted on rather than
  considered solved.
- Adjacent well-rated apps show the category is paid and healthy: Appfire `Jira Misc Custom Fields (JMCF)` —
  3,299 installs, 4.80; Caelor `Fields` — 1,492 installs, 4.61; Seibert `Awesome Custom Fields` — 1,153
  installs, 4.95.

**4. The clock.** **WEAK — and I will not dress this up.** Nothing changed in 24 months about this job. The
only clock is **Forge 0% revenue share from 1 Jan 2026**, which changes the *economics of serving it*, not the
demand. A 2004 ticket with 2,799 votes is evidence of durable demand and of durable platform refusal, but it
is not a clock. **This candidate fails G5 on a strict reading.**

**5. First ten users.** The **2,799 voters on `JRACLOUD-4812`** are named and public — the largest such list
found on this surface. Plus the 26 reviewers of the Big Fig Tree app.

**6. Gate check.** G1 **PASS** · G2 **PASS** · G3 **PASS** (Forge UI modification on the create screen is a
supported module) · G4 **PASS** · **G5 FAIL** (no dated change; economics-only clock).

**7. What already exists.** Big Fig Tree at 4.09/2,504 installs. It is *adequate-ish*, which combined with the
G5 failure is why this is 6 and not higher. **Recommend WATCHLIST rather than build.**

**8. Price signal.** `UNVERIFIED`.

**9. Confidence: 6/10.**

---

### CANDIDATE 5 — Confluence page approval / controlled documents
**Confidence: 6/10.**

**1. One sentence.** Make a Confluence page a controlled document with a real review-and-approval trail that
an auditor will accept.

**2. The artifact.** A Forge app: approval workflow on a page (draft → review → approved), immutable approval
record with approver identity and timestamp, periodic re-review reminders, and an export of the approval
history as an audit evidence pack.

**3. Evidence — T2.**
- **`CONFCLOUD-4153` "Space/Page Approval Mechanism" — 94 votes, resolution "Won't Fix", created
  2005-09-29.** Written refusal, 21 years old.
- **The incumbents split cleanly into one good app and several bad ones, all from the same consolidator:**

| App | Vendor | Rating | Reviews | Installs |
|---|---|---|---|---|
| Comala Document Management | **Appfire** | 4.68 | 174 | **6,078** |
| Page Approval for Confluence | **Appfire** | **3.39** | 73 | **1,698** |
| Comala Document Approval | **Appfire** | **2.29** | 6 | 223 |
| Workflows for Confluence (Document Management & Approvals) | AppFox | 4.65 | 25 | 951 |
| Document Control for Confluence Cloud | Phase Locked Software | 4.46 | 7 | 220 |
| Breeze Document Management | B1NARY | 4.75 | 15 | 187 |
| AURA Workflow & Approval | Aura Apps (Seibert) | 5.0 | 31 | 257 |
| Herzum Approval | STAGIL by catworkx | 3.67 | 15 | 299 |

- **~9,900 combined installs** in a paid category. Appfire owns the #1 (6,078 installs, 4.68) *and* two of the
  three worst-rated (**3.39** across 73 reviews on 1,698 installs; **2.29** on 223). **1,698 installs sitting
  on a 3.39-rated app is the addressable pool.**

**4. The clock.** **WEAK/UNVERIFIED.** The plausible clock is EU regulatory pressure pushing more SMEs into
documented quality systems, but **I did not verify any dated regulatory trigger tied to Confluence document
control, and my search budget was exhausted.** Do not submit this on an assumed regulatory clock. The
verified clock is again only **Forge 0% from 1 Jan 2026**.

**5. First ten users.** The **73 reviewers of Appfire's 3.39-rated `Page Approval for Confluence`** and the
6 reviewers of the 2.29-rated `Comala Document Approval` are named and public. The 94 voters on
`CONFCLOUD-4153` are named.

**6. Gate check.** G1 **PASS** · G2 **PASS** (~9,900 paid installs) · G3 **PASS** · G4 **PASS** ·
**G5 WEAK** (economics-only).

**7. What already exists.** Comala Document Management (4.68, 6,078 installs) is genuinely good and is the
category king. **The honest read: the top of this category is adequately served.** The opportunity is only the
under-served tail on Appfire's two bad apps. That is a real but modest 1,900-install pool.

**8. Price signal.** `UNVERIFIED`.

**9. Confidence: 6/10.**

---

### CANDIDATE 6 — Jira / JSM issue merge
**Confidence: 6/10.**

**1. One sentence.** Merge duplicate tickets — comments, attachments, watchers and links all moved into one —
which Jira still cannot do natively.

**2. The artifact.** A Forge app: select two or more issues, merge with a preview of what moves, redirect the
losers, preserve full history, and auto-suggest duplicates in JSM queues.

**3. Evidence — T2, heavy votes, thin supply.**
- **`JSDCLOUD-4685` "Merge issue feature needed" — 1,236 votes, status "Future Consideration", created
  2017-01-23.**
- **`JRACLOUD-3592` "Merging of issues" — 494 votes, resolution "Won't Fix", created 2004-04-16.** Explicit
  written refusal on the Jira side.
- **Supply is strikingly thin against 1,730 combined votes:** codefortynine `Merge Agent for Jira (JSM Queue
  & Backlog Issue Merger)` — **766 installs, 4.29/5, 7 reviews**; Secretbakery.io `🔮 Duplicate AI > Find &
  Merge Duplicate Issues` — **100 installs, 4.11/5, 7 reviews**; La Forge `Merge Assistant` — **30 installs,
  5.0/5, 3 reviews**. **896 total installs against 1,730 votes.**
- **Proof the playbook works:** `JRACLOUD-37520` *"Add cloning as a bulk operation"* (**1,748 votes, "Under
  Consideration", created 2014**) went unbuilt and codefortynine's **Deep Clone for Jira** now has
  **12,100 installs at 4.5/5**. That is a declined-request → 12k-install paid app, by a small vendor, in the
  same marketplace. It is the single best precedent on this surface.

**4. The clock.** **WEAK.** No dated change. Duplicate-detection quality is now much better with embeddings
than it was in 2017, which is a real capability shift, but I have **no dated evidence** tying that to this
category. Economics clock only (Forge 0%).

**5. First ten users.** The **1,236 voters on `JSDCLOUD-4685`** (named, public, ticket still live) and the
494 on `JRACLOUD-3592`.

**6. Gate check.** G1 **PASS** · G2 **PASS** · G3 **PASS** (merge semantics are fiddly but entirely within
the Jira REST API) · G4 **PASS** · **G5 WEAK**.

**7. What already exists.** codefortynine's Merge Agent (766 installs, 4.29). codefortynine is a strong,
proven small vendor — the same shop that owns Deep Clone at 12,100 installs. **Competing directly with them
is not attractive.** The differentiated wedge is *automatic duplicate detection in JSM queues at intake*,
where the only entrant is Secretbakery at **100 installs**.

**8. Price signal.** `UNVERIFIED`.

**9. Confidence: 6/10.**

---

### CANDIDATE 7 — Shopify multichannel listing/inventory sync (eBay / Amazon / Walmart)
**Confidence: 5/10.** The most vivid complaint evidence I found; the worst gate-3 profile.

**1. One sentence.** A reliable replacement for Shopify's own Marketplace Connect, which merchants say
destroys their listings and has "hasn't worked in over 2 years".

**2. The artifact.** A Shopify app that syncs products, inventory and orders to eBay/Amazon/Walmart with a
visible per-listing sync ledger, safe-by-default publishing (never silently overwrite an existing listing),
and one-click rollback.

**3. Evidence — T2, with exceptional complaint quality.**
- **`Shopify Marketplace Connect`, developer Shopify — 4.3/5, 1,952 reviews.** Rating breakdown:
  **5★ 1,568 (80%) · 4★ 67 (3%) · 3★ 32 (2%) · 2★ 41 (2%) · 1★ 260 (13%)**. **260 one-star reviews** is the
  number that matters — a large, angry, self-identifying pool.
- **Pricing of the incumbent, verbatim:** *"Free to install; first 50 marketplace-synced orders per month
  free, then 1% fee per additional synced order (capped at $99/month)."*
- **Quoted 1-star reviews, all within the last four months, several within the last two weeks:**
  - **toycargeek (US), 23 Aug 2026:** *"Avoid this app at all costs! I have been using it since it was
    Codisto, and I never knew how bad"*
  - **Emma Jeans (US), 17 Aug 2026:** *"Never write reviews but this one is needed. Have gone back and forth
    with support regarding this"*
  - **KRE Prime (US), 13 Aug 2026:** *"If I could leave zero stars, I would. The problem is not just the
    support; it's the app itself."*
  - **Kappa Hobby (US), 11 Aug 2026:** *"This app is good when it work but all of sudden it cannot connect
    eBay. Customer support looked"*
  - **Limoges Boxes (US), 2 Aug 2026:** *"horrible. hasn't worked in over 2 years. When I ask questions they
    answer with another question"*
  - **Vanlife Outfitters (US), 19 May 2026:** *"Endless errors and syncing issues. Support just constantly
    tries to republish the listings to"*
  - **ECORTA (US), 29 May 2026:** *"Gefährlich, rechtlich bedenklich! Zerstörte meine Accounts und Layouts
    meine Angebote, ohne"* — *"Dangerous, legally questionable! Destroyed my accounts and layouts, my
    listings, without..."*
  - **MISTR (UK), 18 May 2026:** *"We reinstalled this app in April 2026 having previously used it in 2019.
    Upon reinstallation the"*

**4. The clock.** Shopify **acquired Codisto** and rebranded it **Marketplace Connect**; toycargeek's
23 Aug 2026 review explicitly traces the decline from the Codisto era. Limoges Boxes dates the breakage at
**"over 2 years"**. This is a documented case of a platform absorbing an app and letting it rot — the exact
platform-risk pattern, here creating an opening rather than closing one.

**5. First ten users — the best named list on this surface.** Eight merchants, each with a **store name and a
country**, each having publicly said in the last four months that this specific product fails them:
**toycargeek**, **Emma Jeans**, **KRE Prime**, **Kappa Hobby**, **Limoges Boxes**, **Vanlife Outfitters**,
**ECORTA**, **MISTR**. Shopify store names are resolvable to storefronts and public contact pages. There are
**260** one-star reviewers in total behind these eight.

**6. Gate check.**
- G1 — **PASS, strongest of any candidate.** 260 named, dated, angry merchants; Shopify bills the
  subscription so there is no payment-trust barrier.
- G2 — **PASS.** 1,952 reviews on the incumbent; merchants pay 1%-per-order today.
- G3 — **FAIL, and this is why confidence is 5.** eBay, Amazon Selling Partner and Walmart APIs each require
  separate developer approval, have distinct category taxonomies, listing-quality rules and rate limits, and
  Amazon SP-API onboarding is a gated review process. **This is access, not skilled work** — the fatal
  category per the brief. It is also a *reliability* product, where the whole value is uptime and correctness
  at scale; that is a poor fit for one operator with no on-call.
- G4 — **PARTIAL.** We could prove eBay sync alone in 14 days without a stranger; Amazon approval is a
  third-party dependency and would not clear in 14 days.
- G5 — **PASS.** Documented multi-year decline of a first-party incumbent, dated to Aug 2026.

**7. What already exists.** Shopify's own app, plus a large paid field I **was not able to enumerate** — the
`selling-on-other-platforms` category slug 404'd and my search budget was spent. **This is a real hole in the
research: I cannot tell you whether the paid alternatives are good.** Given several are long-established
(Codisto's former competitors), assume the category is contested until verified.

**8. Price signal.** Incumbent: free to install, **1% per synced order above 50/month, capped at $99/month**.
That establishes a ceiling of roughly **$99/month** per merchant for this job — a genuine, verbatim price
point, and a healthy one.

**9. Confidence: 5/10.** High demand, superb distribution, **but G3 access failure**. Recommend **kill unless**
scoped to eBay-only, where API access is self-serve.

---

### CANDIDATE 8 — Jira project-level export / restore
**Confidence: 4/10. I am submitting this as a KILL, with the evidence, so it is not re-researched.**

- **`JRACLOUD-34307` "Allow Single Project Export — offline backup that can be re-imported" — 1,030 votes,
  "Gathering Interest", created 2013-08-14.** Also `JRACLOUD-46206` *"Provide the ability for Cloud Admins to
  access application logs"* — **1,024 votes, "Gathering Interest", 2015-07-08**.
- **But the category is already well served by competent paid vendors:** Rewind `Backups for Jira` —
  **1,287 installs, 4.79/5, 73 reviews**; Rewind `Backups for Confluence` — 1,010 installs, 4.91/5; Revyz
  `Command Center for Jira` — 938 installs, **5.0/5**, 19 reviews; Xopero `GitProtect.io for Jira` —
  375 installs, 4.90/5; Twinit `Insight Assets Backup & Migration` — 534 installs, 4.92/5.
- The only badly-rated entrants are tiny: ProBackup for Jira (3.13, 199 installs), ProBackup for Confluence
  (2.19, 150 installs), ELFAPP `Backup Projects for Jira` (1.25, 28 installs).
- **Verdict: G2 fails on the "is the incumbent inadequate?" test.** Five vendors at 4.79–5.0. High votes plus
  a *well-served* category is not an opening. **Standing Law 1 applies: a missing native feature is not white
  space when the marketplace already serves it well.** Killed.

---

## 3. CANDIDATES I KILLED BEFORE SUBMITTING

Recorded so the next cycle does not spend calls on them.

1. **Jira status-field placement (`JRACLOUD-96247`).** Looked like the find of the day: **1,815 votes in
   under a year, status "Not Being Considered", created 2025-09-19** — the fastest-accumulating request I
   saw. **Killed on inspection:** Atlassian's Head of Product for Jira, **Dave Meyer, 10 Oct 2025**, wrote
   *"we've decided to revert the change to the status button location in the work item view"*, admitting
   *"we made significant misjudgments in how this change would affect our users"*, with the revert shipping
   **week of 13 Oct 2025**. The votes were a protest against a UI change that was then undone. **The pain no
   longer exists.** Lesson: a huge vote count on a *recent* ticket can be a protest artefact, not demand —
   always read the official comment before valuing the number.
2. **JSM outgoing email logs (`JSDCLOUD-4698`, 1,492 votes, "Gathering Interest", 2017-01-25).** Killed:
   Atlassian **has since shipped** a native Email logs page in JSM (project admin → Channels & self service →
   Email → View logs), and `Mail History` and `Email This Issue` (**5,643 installs, 4.38**) cover the residue.
   Demand real, gap closed.
3. **Shopify GPSR compliance.** The EU General Product Safety Regulation applied from **13 Dec 2024** — a
   perfect dated clock. **Killed on supply:** at least six apps already occupy it (SWEDev GPSR Compliance
   Hub, GC-GPSR Compliance, GPSR Kit, Alnage, EU GPSR Compliance Suite Pro, EU Compliance EUDR/GPSR/DPP), and
   the one I sampled (`GC ‑ GPSR Compliance`) is **5.0/5 across 6 reviews** with satisfied merchants
   (*"Simple and intuitive"* — Enjoy Pillows, Poland, 4 Feb 2025). Crowded and served.
4. **Shopify EAA accessibility.** Strong dated clock — the European Accessibility Act became enforceable
   **28 June 2025**, and the overlay category is legally discredited (**FTC fined accessiBe $1,000,000 in
   April 2025** for false advertising; **800+ businesses with overlays were sued in 2023–24**). **Not killed
   on merit — killed on evidence:** the `store-design-accessibility` category slug 404'd, I could not obtain
   a single install count or rating for any Shopify accessibility app, and my search budget was exhausted.
   **This is the most promising thing I could not verify.** Recommend it be re-scouted; genuine source-level
   theme remediation (not an overlay) against a hard-dated regulation is a good shape. Submitting it now
   would be a T3/T4 submission and the brief forbids that.

---

## 4. WHAT I WOULD TELL THE PRINCIPAL

**The surface is not dry, and one platform dominates it.**

**Atlassian Forge is the best cold-start software distribution channel available to this operator, and the
window has a date on it.** From **1 Jan 2026** the take rate is **0% to $1,000,000 of lifetime revenue**,
Atlassian bills the customer, the buyer is the user (no procurement), and — critically for the postmortem's
central worry — **the marketplace demonstrably delivers five-figure install counts to one- and two-person
vendors** (Deep Clone 12,100; Timesheet Tracking 13,368; Clockwork Lite 7,046). That is the opposite of the
Document Crunch/Procore result and it is the finding I would most want stress-tested.

**The repeatable method matters more than any single candidate.** Atlassian publishes, in machine-readable
form, both a vote count on every feature request and its own written refusal to build it, alongside a live
census of what customers already pay third parties for. **Cross-joining `jira.atlassian.com` votes against
`marketplace.atlassian.com` install counts and ratings is a repeatable opportunity generator**, and it
answers gates 1, 2 and 5 from primary data in a single pass. Both endpoints and their query syntax are
documented in §0. I would run this join systematically rather than treat the eight candidates below it as the
output.

**Rank order I would defend:** (1) Entra/Intune → JSM Assets scheduled sync — written refusal, three dated
complaints naming one missing feature, ~1,840 paid installs proving willingness to pay, two-week build.
(2) Markdown round-trip — 1,749 votes, "not roadmapped" in writing from Atlassian's PM in Jan 2025, and a
category where nine apps and ~20,300 installs cannot get above 4.25; it is also the candidate whose 14-day
test is cleanest and whose build style (large-volume fixture-driven conversion testing) best suits an
AI-agent-heavy operator.

**Three honest weaknesses in this report.** First, **I captured almost no incumbent price points** —
Marketplace pricing tabs did not render — so every "price signal" except Shopify's is `UNVERIFIED`, and that
is a gap worth ten minutes before anyone commits. Second, **candidates 4, 5, 6 and 8 have no real clock**;
their only dated change is the Forge revenue-share shift, which changes our economics, not the demand, and
under a strict G5 reading they should be watchlisted rather than built. Third, **the single most promising
regulation-clocked idea (Shopify EAA accessibility) is unsubmitted** because I ran out of search budget
before I could attach one install count to it — submitting it would have been a T3 submission, and that is
precisely the failure mode this engine exists to prevent.

**And one thing to carry forward regardless of what gets built:** the strongest recurring pattern on this
surface is **a free, unsupported, first-party app with a large install base and a poor rating**, sitting
above paid third parties that are rated far higher — Atlassian Labs' Entra beta (1,469 installs, 3.0,
"Unsupported") and `GitHub for Atlassian` (136,788 installs, 3.34, free) on one side, Shopify's Marketplace
Connect (1,952 reviews, 260 of them one-star) on the other. **A platform shipping something for free is not
the category closing; it is frequently the category opening**, because the free first-party version
establishes the job as legitimate, trains the market to expect it, and then stops being maintained.
