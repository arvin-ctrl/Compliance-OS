# SCOUT 07 — OPEN SOURCE WITH COMMERCIAL PULL

**Surface:** OSS projects whose users visibly want a hosted/managed/supported version; plus the
adjacent surface of developer-tool pain with public evidence.
**Date:** 2026-08-27 · **Candidates returned:** 8 live + 4 explicit kills

---

## THREE SURFACE-LEVEL FINDINGS THAT SHOULD SHAPE HOW YOU READ THIS

**1. The "hosted version?" issue with heavy reactions is largely a myth.**
I searched GitHub issue titles, sorted by reactions, for `"hosted version"`, `"cloud version"`,
`"managed service"`, `"SaaS version"`, `"hosted offering"`, `"commercial support"`, `"official hosted"`,
`"any plans for a hosted"`, `"would pay for a hosted"`. The top-reaction results are overwhelmingly
either (a) unrelated string matches, or (b) **the exact inverse** — users of a SaaS product begging for
a *self*-hosted version (sanity-io/sanity "Provide a (real) self hosted version" 27 reactions;
codesandbox "Team functionality or enterprise (self-hosted) offering?" 13 reactions;
keybase/client #24105 "Open source the server components of Keybase" 176 reactions). The one clean
willingness-to-pay quote I found in that direction is keybase/client #24105: *"I'd still happily pay a
small monthly fee for a hosted server"* — one comment, on a dead product.

**Implication:** on this surface, GitHub reaction counts are a *weak* demand instrument. The two
instruments that actually work are:
- **Multiple independent vendors publishing prices to host the same OSS project** (money already moving), and
- **A dated licence/abandonment shock** that strands businesses which are already capable of paying.

Every candidate below is anchored on one of those two, not on enthusiasm.

**2. The 24/7 problem kills most of this surface for our operator profile.**
"Managed hosting of X" means being on-call. The operator profile explicitly excludes 24/7 staffing.
This is the single most common reason the candidates below fail Gate 3, and it is why I have weighted
**asynchronous / batch / retryable** artifacts (a parsing API, an image build pipeline, a document
conversion endpoint) far above **critical-path** artifacts (an identity provider, a VPN control server,
an object store).

**3. "Developers won't pay" is confirmed — with one reliable exception.**
Where the buyer is a developer scratching an itch, no money moves. Where the buyer is a **business with
an externally-imposed reporting or retention obligation**, money moves fast and publicly. HN user
`miyuru` on the Bitnami thread (2025-08-28) states the mechanism exactly:

> "At my previous company, we used it because of the low CVE counts. **We needed to report the CVE count
> for every Docker image we used every month**, so most of the images were from Bitnami."

That is the shape of every candidate here that survives Gate 2. Filter on obligation, not enthusiasm.

---

# CANDIDATE 1 — Bitnami Refuge: maintained drop-in Helm charts + images for the orphaned Bitnami catalog

**One sentence:** Broadcom moved the free Bitnami container catalogue behind a $50k–$72k/year
subscription on 28 August 2025 and dumped every pinned version tag into an unmaintained
`bitnamilegacy` repo — thousands of companies' Helm `values.yaml` files now point at images that will
never receive another CVE patch, and someone has to keep building them.

### The artifact
A registry namespace (GHCR/Quay) publishing **version-pinned, digest-stable, CVE-patched rebuilds of
the top ~40 Bitnami images** (postgresql, redis, kafka, rabbitmq, mongodb, mysql, nginx, minio,
keycloak, etc.) built from the still-Apache-2.0 upstream Dockerfiles, **plus the matching Helm charts
kept API-compatible** so the customer's change is one line: `image.registry`. Delivered with a monthly
signed CVE-delta report per image (the artifact the compliance team actually needs) and an SBOM.
Subscription, self-serve, credit-card.

### Evidence — **T2 strong, with a T1 price anchor**
| What | Source | Date |
|---|---|---|
| The announcement issue | `github.com/bitnami/charts/issues/35164` — "Upcoming changes to the Bitnami catalog (effective August 28th, 2025)", opened by **wjimenez5271**, 16 Jul 2025. Content confirms: legacy images move to a separate unmaintained repo; only "latest"-tag hardened community images remain free; **"transition to a paid Bitnami Secure Images subscription model for production use."** | 2025-07-16 |
| HN #1 | ["Broadcom to discontinue free Bitnami Helm charts"](https://news.ycombinator.com/item?id=44608856) — **244 points, 135 comments**, submitter `mmoogle`. Links straight to the issue above. | 2025-07-18 |
| HN #2 | ["The Deletion of Docker.io/Bitnami"](https://news.ycombinator.com/item?id=45048419) — **348 points, 246 comments**, submitter `zdkaster` | 2025-08-28 |
| Ask HN | ["Bitnami ending free tier in August – what open alternative are you switching to?"](https://news.ycombinator.com/item?id=44873243), `urvader` | 2025-08-12 |
| Ask HN | ["What did you replace bitnami with?"](https://news.ycombinator.com/item?id=46076115), `kachapopopow` | 2025-11-28 |
| **Price of the worse version** | devoriales.com/post/402: *"Bitnami Premium costs **$50,000 annually** and provides unlimited access to 500+ applications, while **Bitnami Secure Images requires $72,000 yearly** for 280+ hardened applications"* — article sources these to "AWS Marketplace listings and Arrow Electronics distribution agreements". HN `gangstead` independently: *"Looks like it's **$5k/month, minimum 12 months** for 'secure' images"* citing an AWS Marketplace listing. | 2025 |
| Corroborating pain | HN `runamok`: *"My company is demoing Chainguard which is quite pricy for hardened images. Bitnami premium reportedly goes for $50k to $72k per year."* | 2025-08-28 |
| The literal request | HN `notimetorelax`: *"**Is anyone working on mirroring the images and keeping them updated?**"* | 2025-08-28 |

⚠️ **UNVERIFIED:** I could not load the AWS Marketplace listing page itself (it returned the marketplace
homepage). The $50k/$72k/$5k-per-month figures are **secondary** — a named article citing AWS
Marketplace, plus two independent HN commenters converging on the same range. Verify before relying on it.

### Licence
Broadcom's own announcement (quoted in-thread by HN user `Youden`): *"Helm charts and container images'
open-source code will continue to be maintained up-to-date and accessible on GitHub **under the Apache 2
license**."* → **Apache-2.0 source, rebuild-and-redistribute is permitted.** ⚠️ Confirm the current
LICENSE file in `bitnami/containers` and `bitnami/charts` directly before building anything. Note HN
`synchrone`'s warning: *"Their Dockerfiles include things like download pre built binaries from
$SECRET_BASEURL which is hosted by them"* — a rebuild may need to source upstream binaries independently.

### The clock
**16 Jul 2025** announcement → **28 Aug 2025** cutover. Legacy tags frozen, no further CVE patches.
Thirteen months of accumulating unpatched CVEs as of today. This is the freshest, hardest-dated clock
on this surface.

### First ten users — nameable
The Gate-1 channel is not cold outreach; it is four public threads where the affected people are already
assembled and self-identified:
- `bitnami/charts#35164` participants
- HN 44608856 (135 comments) and HN 45048419 (246 comments)
- The two Ask HN "what did you replace it with" threads (46076115, 44873243)
- Named handles already on record as affected and shopping: **`notimetorelax`** (asked the exact
  question), **`runamok`** (evaluating Chainguard, priced Bitnami Premium), **`miyuru`** (monthly CVE
  reporting obligation), **`tetha`** (runs mirrors + image observability across infra), **`elephantum`**
  (already prototyping "mirror and CI/CD on top of Github"), **`BSVogler`** (*"With Bitnami
  discontinuing their offer, we recently switched to other providers"*), **`mrweasel`**,
  **`supriyo-biswas`**, **`KronisLV`**, **`pveierland`**, **`TheCondor`** (*"Taking a bunch of projects
  and making containers and flexible helm charts for them is kind of an interesting model"*),
  **`kachapopopow`**, **`urvader`**, **`wink`**, **`0x6c6f6c`**.
- Plus a purely mechanical channel: `grep` public GitHub for `values.yaml` files still referencing
  `docker.io/bitnami` and open a PR. That is a build task, not a sales motion.

### Gate check
1. **Cold-start distribution — PASS.** Five public threads, ~400 comments, dozens of self-identified
   affected engineers, plus a mechanical GitHub-wide grep of stranded `values.yaml` files.
2. **Observable demand — PASS.** Broadcom charges $50k–$72k/yr for exactly this and people are paying or
   fleeing; Chainguard and Minimus are funded competitors in the same slot.
3. **Buildable by us — PASS on the build, RISK on trust.** Rebuilding Apache-2.0 Dockerfiles on a CI
   matrix with automated CVE scanning is precisely AI-throughput work. The bottleneck is not skill, it is
   **supply-chain trust**: we would be asking companies to run *our* binaries in production. That is the
   hardest thing an unknown vendor can sell. Mitigations: reproducible builds, public build logs,
   Sigstore signing, SBOM, source-only fallback.
4. **Self-verifiable in 14 days — PASS.** Build the top 10 images, publish free, instrument pulls.
   Pull counts within 14 days answer the demand question without anyone's cooperation.
5. **The clock — PASS.** 28 Aug 2025, named and dated.

### What already exists and why it's inadequate
- **Bitnami Secure Images** — the incumbent. Inadequate for the mid-market: $50k–$72k/yr and an
  enterprise procurement motion. This is the price umbrella.
- **Chainguard** — "quite pricy" per a named evaluator; enterprise sales.
- **Minimus** (launched 2025 by the Twistlock team; HN `morellonet`, 2025-08-28) — funded, near-zero-CVE
  images, same enterprise slot.
- **Docker Hardened Images went FREE in Dec 2025** ([HN 46302337, 360 pts, 98
  comments](https://news.ycombinator.com/item?id=46302337)). **This is the biggest threat to this
  candidate** and it is why the wedge must be the *Helm charts* and *version-pinned legacy tags*, not
  "hardened images" generically. HN `supriyo-biswas` (2025-08-28) puts it plainly: *"What probably
  carries more value is **the helm charts** that they provide which are also on their way out. The
  images themselves have official replacements."* Docker's free hardened images do not ship
  Bitnami-compatible Helm charts or Bitnami's historical version tags.
- **Flux Mirror plugin** (2026-07) — free chart/image mirroring tooling. Solves mirroring, not
  *maintenance*.

### Price signal
$50,000–$72,000/yr (Bitnami, secondary). Our slot: **$99–$499/month self-serve**, sized for the
company that will never sign a $50k PO but does have a monthly CVE report to file.

### Confidence: **7/10**
Best clock, best named cohort, real price umbrella. Marked down for the supply-chain-trust problem
and for Docker commoditising the adjacent "hardened images" pitch eight months ago.

---

# CANDIDATE 2 — Managed Keycloak

**One sentence:** Keycloak is the default open-source identity provider and is notoriously hard to run
correctly; at least three companies sell hosting for it with published prices.

### Evidence — **T1, the strongest money evidence on this surface**
| Vendor | Published price | Note |
|---|---|---|
| **Cloud-IAM** (cloud-iam.com/pricing) | Starter / Essential / Premium all **"Starting from €225/month"**; worked example **"€485/month for 500 users"** on Premium annual; Max = custom | *"Join over **5,000 users** who trust Cloud-IAM"*; customer logos shown: **Fare, Forto, Brittany Ferries, Vardot, Drupal, APS Group, Resilience, Powerflex, AgileTV** |
| **Phase Two** (phasetwo.io/pricing/hosting) | Starter **$149/mo** (15K MAU, 95% uptime target); Premium **$749/mo annual / $999/mo monthly** (100K MAU, 99.5% SLA); Enterprise **$2,499/mo annual / $2,999/mo monthly** (250K MAU, 99.95% SLA) | |
| **Skycloak** (skycloak.io/pricing) | Developer **$29/mo**, Launch **$149/mo**, Business **$599/mo**, Enterprise custom | flat infra pricing, unlimited users |

Adjacent developer-pain corpus (Stack Exchange API, sorted by votes):
`keycloak Invalid parameter: redirect_uri` **502,952 views** · `M1 docker preview and keycloak image's
platform...` **449,642 views** · `What are Keycloak's OAuth2 / OpenID Connect endpoints?` **374,149
views** · `Resources, scopes, permissions and policies in Keycloak` **180,752 views**.

**Licence:** Apache-2.0. Hosting commercially is unambiguously permitted.

### The clock
Weak. Managed Keycloak vendors have existed for years; this is a mature niche, not a new opening. The
only recent movement I can name is the general 2025–26 repricing of commercial IdPs (Auth0/Okta), which
is directional, not dated.

### Gate check
1. **Cold-start distribution — MARGINAL.** The audience is assembled (Keycloak Discourse, r/keycloak,
   a half-million-view SO corpus) but the only way in is answering questions and mentioning the product,
   i.e. content marketing. Under the brief's own rule, **that is a fail.**
2. **Observable demand — PASS, emphatically.** Three vendors, published prices from $29 to $2,999/month,
   one claiming 5,000 users and showing named enterprise logos.
3. **Buildable by us — FAIL.** A hosted IdP is the definition of critical-path infrastructure: when it
   is down, every customer's login is down. Phase Two sells a **99.95% uptime guarantee**. One operator
   cannot carry that pager, and buyers at this price point will demand SOC 2.
4. **Self-verifiable in 14 days — FAIL.** The riskiest assumption is "can a solo operator hold an
   identity SLA", which cannot be proven in 14 days.
5. **The clock — FAIL.** Nothing changed in 24 months that I can date.

### Verdict: **KILL on G3/G4/G5.**
Reported in full because it is the cleanest proof on this entire surface that businesses do pay real
money to have OSS run for them — which is the load-bearing assumption behind Candidates 1, 5 and 6.
Use it as evidence, not as a project.

### Confidence: 3/10 as a project · 9/10 as evidence for the thesis

---

# CANDIDATE 3 — Docling-as-a-Service (self-serve document parsing API)

**One sentence:** Docling is a 65.6k-star MIT document parser that businesses want behind an HTTP
endpoint, but running it well needs a GPU and non-trivial ops — and the two obvious commercial
alternatives charge $50–$500/month.

### The artifact
A metered HTTPS endpoint: POST a PDF/DOCX/PPTX/XLSX, get back structured Markdown/JSON with layout and
table structure. Async, batch, retryable — **no on-call catastrophe if it is down for an hour**, which
is exactly the property this surface needs.

### Evidence
| What | Detail |
|---|---|
| Repo | `github.com/docling-project/docling` — **65.6k stars**, **MIT**, 1,365 commits, **895 open issues**, housed in LF AI & Data, from IBM Research Zurich |
| Self-host friction (named, dated) | #1304 *"Docling is unusable on long PDFs with CUDA"* — **JamMaster1999**, 2025-04-06, 6 reactions, *"running Docling on L4 GPU from modal labs. Only uses 1.4GB of VRAM"* · #799 *"Could not load the custom kernel for multi-scale deformable attention"* — **jmvial**, 2025-01-24, 8 reactions, *"prevents it to run on GPU"* · #2536 — **mkesper**, 2025-10-28, 11 reactions · #1429 *"Performance decrease since version 2.26.0"* — **1greentangerine**, 2025-04-22 · #1235 *"How to Extract Values Using APIs"* — **shashank-indukuri**, 2025-03-24, 7 reactions, notes users are *"calling docling from the command line rather than through APIs"* · #2495 — **The-unknown-Shadowman**, 2025-10-19, 8 reactions |
| **T1 — LlamaParse** | llamaindex.ai/pricing: Free $0 (10K credits) · **Starter $50/month** (40K credits) · **Pro $500/month** (400K credits) · Enterprise custom. *"1,000 credits = $1.25"* |
| **T1 — Reducto** | reducto.ai/pricing: *"Free up to your first 15K credits"*, then **"$0.015 per credit after first 15K"**; *"Batch processing: 20% credit discount on parsing for non-urgent async jobs"* |
| Maintainer commercialisation | IBM ships a commercial managed/on-prem Docling offering and released a Docling OpenShift Operator with Red Hat in early 2026, targeting banks. ⚠️ **UNVERIFIED**: a secondary source quotes *"roughly $4/1K pages managed per IBM's announcement"* — I could not confirm this against an IBM page. |

### The clock
Docling reached 65.6k stars and joined LF AI & Data; IBM commercialised it with a Red Hat OpenShift
Operator in **early 2026**. Verify the exact date.

### First ten users
Named above from the issue tracker (JamMaster1999, jmvial, mkesper, 1greentangerine,
shashank-indukuri, The-unknown-Shadowman). Weaker than Candidate 1: these people are debugging
self-hosting, not asking to buy. Nobody in `docling` is asking for a hosted version in so many words.

### Gate check
1. **Distribution — MARGINAL.** 895 open issues is a large assembled audience with a demonstrable
   self-hosting failure rate, but they are individually debugging, not shopping.
2. **Observable demand — PASS.** LlamaParse and Reducto have published prices for the identical output.
3. **Buildable by us — PASS.** GPU inference behind a queue is well within scope; costs are the risk.
4. **Self-verifiable in 14 days — PASS.** Stand up the endpoint, price it under LlamaParse, measure
   signups from the issue-tracker cohort.
5. **The clock — MARGINAL.** IBM commercialising it is as much a threat as a signal.

### What already exists and why it's inadequate — **partly adequate, which is the problem**
LlamaParse, Reducto, Unstructured, Azure Document Intelligence and IBM's own offering all serve this.
The only defensible wedge is price-per-page against LlamaParse's $50 floor, and margin on a
commoditising GPU workload is thin. **This is a price war we would enter with no distribution advantage.**

### Confidence: **4/10**

---

# CANDIDATE 4 — The MinIO orphan: patched builds + migration off a dead object store

**One sentence:** MinIO — the default self-hosted S3 — stopped shipping free Docker images in Oct 2025,
declined to patch a CVE, entered maintenance mode in Dec 2025, and had its repository marked unmaintained
in Feb 2026, stranding an enormous installed base of businesses.

### Evidence — the best-documented abandonment arc I found
| Date | Event | HN |
|---|---|---|
| 2021-04-23 | Minio changes licence to **AGPL** | [172 pts, 141 comments](https://news.ycombinator.com/item?id=26919510) |
| 2025-05-30 | "MinIO Removes Web UI Features from Community Version, Pushes Users to Paid Plans" | [176 pts, 103 comments](https://news.ycombinator.com/item?id=44136108), `jordigh` |
| 2025-10-22 | **"MinIO stops distributing free Docker images"** | [**733 pts, 555 comments**](https://news.ycombinator.com/item?id=45665452), `LexSiga` |
| 2025-10-23 | "MinIO declines to release Docker builds resolving **CVE-2025-62506**" | [175 pts](https://news.ycombinator.com/item?id=45684035), `vngzs` |
| 2025-10-23 | "OpenMaxIO: Forked UI for MinIO Object Storage" | [185 pts, 40 comments](https://news.ycombinator.com/item?id=45684736), `nimbius` |
| 2025-12-03 | **"MinIO is now in maintenance-mode"** | [511 pts, 322 comments](https://news.ycombinator.com/item?id=46136023), `hajtom` |
| 2026-02-13 | **"MinIO repository is no longer maintained"** | [500 pts, 387 comments](https://news.ycombinator.com/item?id=47000041), `psvmcc` — links to commit `7aac2a2` |
| 2026-02-28 | "MinIO Is Dead, Long Live MinIO" | [224 pts, 92 comments](https://news.ycombinator.com/item?id=47200342), `zufallsheld` |

**Licence:** AGPL-3.0 — a fork and a hosted service are both permitted, but any modifications must be
published to users. Not a blocker; does constrain proprietary differentiation.

### Named affected users
`merpkz` (2026-02): *"I just bit the bullet last week and figured we are going to migrate our self hosted
minio servers to **ceph** instead... last minio server is currently mirroring its **~120TB** buckets to
new cluster"* · `PunchyHamster` (evaluating RustFS, flags its licence file as *"already prepared for
bait-and-switch"*) · `0x6c6f6c`: *"people who are **paying for support contracts** were also impacted by
this"* · plus ~1,500 comments across the eight threads.

### Why I am **not** advancing this
**Gate 2 fails.** Across ~1,500 comments I could not find a single person saying they would pay for a
maintained MinIO fork. What I found instead was people *migrating away* — to Ceph, Garage, SeaweedFS,
RustFS — and free forks (OpenMaxIO) already existing. The demand that exists is for **migration**, which
is one-off consulting work that `rclone`/`mc mirror` largely already does. The remaining hosted-storage
play is a commodity price war against Backblaze B2, Wasabi and Cloudflare R2.

### Gate check
1. Distribution — **PASS** (eight threads, ~1,500 comments, named handles).
2. Observable demand — **FAIL.** Enthusiasm and anger, no observed payment. **T4 by the brief's own ladder.**
3. Buildable — MARGINAL (maintaining an erasure-coded object store is deep systems work).
4. Self-verifiable — PASS.
5. Clock — **PASS, outstanding** (four dated events in 10 months).

### Verdict: **KILL on G2.** Perfect clock, no money. Textbook case of the brief's warning.
### Confidence: 3/10

---

# CANDIDATE 5 — Managed Mautic for marketing agencies

**One sentence:** Mautic is the open-source marketing-automation platform; its own foundation points
users at a partner charging **€247.50–€1,237/month** to run it, and agencies are the buyer.

### Evidence — **T1, published by the project itself**
From `mautic.org/start-using-mautic/managed-mautic/` — the official page, naming **Dropsolid** as
trials-and-hosting partner:
- **Mautic Essential: "From €247.50/mo"** (annual) or €275/mo (quarterly) — up to 50K emails/month, 50K contacts
- **Mautic Professional: "From €1237/mo"** — dedicated infrastructure, extendable to 3M contacts
- **Mautic Enterprise:** custom
- *"40% of all revenue will go straight to the community!"*

The page also points to a **hosting directory** of further providers among Mautic's partner network —
i.e. the project actively channels commercial hosting demand and there is more than one vendor.
Commodity floor: Elestio lists managed Mautic **from $16/month** (secondary source).

**Licence:** GPL-3.0 (Mautic core). Hosting is permitted.

### Why the buyer is a business, not a hobbyist
Mautic's users are agencies running campaigns for clients and SMBs escaping per-contact pricing at
HubSpot/Mailchimp. Marketing automation is **not critical path** — an hour of downtime delays a send;
it does not take a customer offline. That is the right risk profile for a solo operator.

### The clock — **WEAK, and this is the problem.**
I cannot name a dated change in the last 24 months. Managed Mautic has existed for years.

### Gate check
1. Distribution — **MARGINAL.** Mautic Slack/forums and the agency community are reachable, but there
   is no single hot thread to walk into; getting the first ten looks like partnership hustle.
2. Observable demand — **PASS.** €247.50–€1,237/month, published, on the project's own site.
3. Buildable — PASS. Mautic + SES + monitoring is squarely in scope.
4. Self-verifiable — PASS.
5. Clock — **FAIL.**

### What already exists
Dropsolid (official partner), a partner hosting directory, Elestio, Droptica, Kloudbean. The market
is served at both the $16 and the €250+ end. To win you would need an angle we do not have.

### Confidence: **4/10** — real money, no clock, no distribution edge.

---

# CANDIDATE 6 — Managed Paperless-ngx for EU statutory document retention

**One sentence:** Paperless-ngx is the standard open-source document archive; a cluster of German
providers already sell it as a managed service to SMBs whose retention obligations they are quietly
solving.

### Evidence — **T2 with T1 characteristics** (multiple independent paid vendors)
Independent commercial providers of managed Paperless-ngx found:
- **Elestio** — managed Paperless-ngx on dedicated VMs, **from $16/month** (secondary)
- **cloudshift.de** — own servers, no shared infra, monthly or annual billing
- **WZ-IT** (Germany) — managed hosting, 24/7 support, *"operating exclusively on German servers so
  documents never leave the EU"*, fixed monthly price
- **peaknetworks** — daily backups, 24/7 monitoring
- **paperless-home.com** — publishes a "Self-Host vs. Managed" comparison, i.e. sells against self-hosting

⚠️ **UNVERIFIED:** I did not load each vendor's price page individually; the $16 Elestio figure and the
existence of monthly billing at cloudshift/WZ-IT come from search-result summaries. **Verify prices
directly before advancing.**

**Licence:** GPL-3.0. Hosting permitted.

### The interesting wedge — the obligation, not the app
Every one of those vendors sells "we run the container." None of them, as far as I can see, sells the
thing that actually makes a German SMB pay: **GoBD-conformant, audit-proof (revisionssicher) archiving**
— immutable storage, retention locks, an exportable audit trail, and a written procedural documentation
(*Verfahrensdokumentation*). That is an obligation-driven purchase, which is the one buyer type this
surface has shown will actually pay.

### The clock — **NOT ESTABLISHED.** I could not date a regulatory or product change in the last 24
months. This needs a Scout on the compliance surface to check whether any GoBD/e-invoicing deadline
(e.g. German mandatory e-invoicing phase-ins) creates one. **Do not advance without it.**

### Gate check
1. Distribution — **FAIL as written.** The only channel I can name is SEO against incumbents who
   already rank. No named thread, no assembled cohort.
2. Observable demand — PASS (five vendors selling it).
3. Buildable — PASS on the app; ⚠️ the compliance claim may require attestation we cannot issue.
4. Self-verifiable — MARGINAL.
5. Clock — **FAIL / not established.**

### Confidence: **3/10** as scoped. Worth one hour of a compliance scout's time on the *obligation*,
not the hosting.

---

# CANDIDATE 7 — Document-conversion API on Gotenberg (the DOCX/HTML→PDF endpoint)

**One sentence:** Every developer eventually has to turn HTML or Office files into PDFs, does it badly,
and there is a live market of small hosted APIs charging $19–$249/month to make the problem go away.

### Evidence
| What | Detail |
|---|---|
| The OSS | `github.com/gotenberg/gotenberg` — **12.9k stars, MIT**, 24 open issues. One Docker container bundling headless Chromium, LibreOffice, QPDF, pdfcpu, PDFtk, ExifTool. Described as *"trusted in production by thousands of companies"*. |
| **Maintainer position = permission** | README: *"If Gotenberg powers your workflow or your business, consider becoming a sponsor."* No hosted version offered. Listed sponsors include **PDFBolt** and **FileToPDF.dev** — i.e. commercial PDF APIs are *already* building on it and funding it. |
| **T1 pricing** | **PDFBolt** (pdfbolt.com/pricing): Free 100 docs/mo · **Basic $19/month** (2,000 docs) · **Growth $79/month** (10,000 docs) · **Enterprise $249/month** (50,000 docs). **CloudConvert**: credit-based, *"conversions typically consume one credit per minute of conversion time"*, Office/iWork→PDF 2 credits, PDF→Office 4 credits. |
| **T2 developer pain (Stack Exchange API, view counts verbatim)** | "Generate pdf from HTML in div using Javascript" **1,569,344 views** · "How Can I add HTML And CSS Into PDF" **962,604 views** · "Convert HTML to PDF in .NET" **963,437 views** · "Command `libreoffice --headless --convert-to pdf` is not working" **204,559 views** · "Convert Word doc and docx format to PDF in .NET Core without Microsoft.Office.Interop" **165,234 views** · "avoid page break inside row of table" (wkhtmltopdf) **239,895 views** · "wkhtmltopdf: cannot connect to X server" **133,346 views** |
| Abandonment adjacency | `github.com/wkhtmltopdf/wkhtmltopdf` — **14.6k stars, LGPL-3.0**, *"This repository was archived by the owner on **Jan 2, 2023**. It is now read-only."* Its Qt-WebKit engine is frozen; distros are dropping it. |

### Gate check
1. Distribution — **MARGINAL.** Millions of SO views is intent, but SO answers are content marketing.
2. Observable demand — **PASS.** PDFBolt, DocRaptor, CloudConvert, Api2Pdf, Nutrient all charge for it.
3. Buildable — PASS, trivially. Gotenberg is MIT and containerised.
4. Self-verifiable — PASS.
5. **The clock — FAIL.** wkhtmltopdf was archived **43 months ago**. Nothing has changed in 24 months.
   The market is old, well-served and price-competitive at $19/month.

### Verdict: **KILL on G5 + commoditisation.** Genuine, permanent, monetised pain — with no opening.
Included because it is the cleanest example of the trap on the adjacent "developer-tool pain" surface:
huge public evidence of pain that is *already* efficiently served.

### Confidence: 3/10

---

# CANDIDATE 8 — Hosted listmonk with deliverability included

**One sentence:** listmonk is a 23.1k-star AGPL newsletter engine with **no hosted version at all**,
used by businesses specifically to escape per-contact pricing at Mailchimp/Brevo.

### Evidence
- `github.com/knadh/listmonk` — **23.1k stars, AGPL-3.0**, 91 open issues. README: *"listmonk is a
  standalone, **self-hosted**, newsletter and mailing list manager."* **No hosted, cloud or SaaS version
  is offered or mentioned.** That is explicit permission.
- Third parties already sell hosting: **Elestio from $11/month**; **Hostinger** listmonk hosting at
  **$11.99 / $14.99 / $28.99 / $49.99 per month** (2-year terms); **Kloudbean** flat monthly.
  ⚠️ Secondary sources — verify.
- Cost pain, dated: HN ["Built an email marketing platform after paying
  $230/month"](https://news.ycombinator.com/item?id=44637635) — 44 points, 35 comments, `rasadov`,
  2025-07-21.

**Licence note:** AGPL-3.0. Hosting it as a service is permitted, but **we must offer the corresponding
source to users**, including any modifications. Fine if we run stock upstream; it forecloses proprietary
feature differentiation.

### Why it probably dies at Gate 2
The whole reason people run listmonk is to *avoid paying per contact*. Selling hosting to the
cost-avoidance crowd is selling to the least willing buyer on the market — and existing vendors have
already competed the price to $11/month. The only version with margin is **"listmonk + warmed sending
IPs + deliverability management"**, which means we would own IP reputation for other people's email —
a spam-liability and abuse-handling burden that a solo operator should not take on.

### Gate check
1. Distribution — MARGINAL (listmonk GitHub, r/selfhosted; no hot thread).
2. Observable demand — **MARGINAL.** Vendors exist but at $11–$50/month; no evidence of a real
   business-scale buyer.
3. Buildable — PASS on the app, **FAIL on deliverability/abuse operations.**
4. Self-verifiable — PASS.
5. Clock — FAIL.

### Verdict: **KILL on G2/G3.**
### Confidence: 2/10

---

# EXPLICIT KILLS — checked and discarded, do not re-research

| Candidate | Licence | Why killed |
|---|---|---|
| **Hosted n8n** | **Sustainable Use License** (fair-code, not OSI) — permits internal business use only, not hosting-as-a-service. ⚠️ The canonical licence page 404'd when I fetched it; **confirm current terms** before ever revisiting. | **Licence-blocked.** Huge hosted demand exists; we are not permitted to serve it. |
| **Crawl4AI / Firecrawl-class scraping API** | Crawl4AI **Apache-2.0**, 79.5k stars, 38 open issues. Firecrawl is AGPL-3.0. | **The maintainer is already building it.** Crawl4AI's README advertises a **"Crawl4AI Cloud API… closed beta, Launching Soon"** with a Google-Form waitlist, plus a sponsorship programme *"$5 to $2,000 monthly"*. Competing against the maintainer's own cloud, in a market where Firecrawl charges $16/$83/$333/$599 per month and Browserbase charges $20/$99 + $0.10–$0.12 per browser-hour, both venture-funded, with no distribution edge. |
| **Hosted Headscale** | **BSD-3-Clause**, 43.2k stars, 83 open issues. | Maintainers explicitly narrow the scope — *"Headscale's goal is to provide self-hosters and hobbyists with an open-source server… suitable for a personal use, or a small open-source organisation"* and *"we do not support nor encourage the use of reverse proxies and container to run Headscale."* That is permission, but the artifact is a **critical-path VPN control server** (G3 fail on 24/7), the buyer motive is cost-avoidance against Tailscale (⚠️ reported 2026 seat pricing of $8/$18 per seat — UNVERIFIED), one maintainer is employed by Tailscale, and WZ-IT already offers managed Headscale. |
| **"Supported fork of an abandoned dependency" as a general model** | — | The model is real — **HeroDevs** sells "Never-Ending Support" for EOL AngularJS/.NET/Node etc. — but its distribution is **enterprise procurement**, which the operator profile excludes outright (G1 fail). Note also that a competitor already shipped the discovery tool: ["Show HN: Eolds, a scanner for EOL open source packages across 12M versions"](https://news.ycombinator.com/item?id=47234277), 2026-03-03. |

---

# SUMMARY TABLE

| # | Candidate | Licence | Evidence tier | G1 | G2 | G3 | G4 | G5 | Conf |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Bitnami-orphan charts + images** | Apache-2.0 ⚠️ | T2 + T1 anchor | ✅ | ✅ | ⚠️ trust | ✅ | ✅ | **7** |
| 2 | Managed Keycloak | Apache-2.0 | **T1** | ⚠️ | ✅ | ❌ | ❌ | ❌ | 3 |
| 3 | Docling-as-a-Service | MIT | T1 (competitors) | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | **4** |
| 4 | MinIO orphan | AGPL-3.0 | T4 on payment | ✅ | ❌ | ⚠️ | ✅ | ✅ | 3 |
| 5 | Managed Mautic | GPL-3.0 | **T1** | ⚠️ | ✅ | ✅ | ✅ | ❌ | **4** |
| 6 | Managed Paperless-ngx (EU) | GPL-3.0 | T2 ⚠️ | ❌ | ✅ | ⚠️ | ⚠️ | ❌ | 3 |
| 7 | Gotenberg doc-conversion API | MIT | T1 + T2 | ⚠️ | ✅ | ✅ | ✅ | ❌ | 3 |
| 8 | Hosted listmonk | AGPL-3.0 | T2 weak | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | 2 |

**Only Candidate 1 clears all five gates.** Candidates 3 and 5 are live but unexciting. The rest are
reported as evidence and as documented kills.

---

# METHOD AND ITS LIMITS

- **GitHub's REST/GraphQL API is unavailable in this environment** (the session proxy scopes it to the
  session's own repositories; `add_repo` refuses cross-owner adds). All GitHub facts here come from
  fetching rendered github.com pages, so **I could not read exact reaction counts or full commenter
  lists on `bitnami/charts#35164`** — the highest-value thread in this report. Someone with API access
  should pull `/repos/bitnami/charts/issues/35164/reactions` and the comment list; that is the single
  highest-value follow-up.
- Hacker News figures (points, comment counts, dates, usernames, story IDs) are from the HN Algolia API
  and are **exact**.
- Stack Overflow view counts are from the Stack Exchange API and are **exact**.
- Pricing quoted from vendor pricing pages is **verbatim**. Anything from a search-result summary or a
  third-party article is flagged **⚠️ UNVERIFIED**.
- The WebSearch budget for this session was exhausted partway through; later verification used direct
  fetches and the two open APIs only.
