# 15 — The DIY Substitute Stack: What Contractors Actually Do Today

**Target:** The "do nothing / do it in Excel" competitor — the human process and the tool stack that
already occupies the seat any commercial-event / notice / claim product would need to take.
**Analyst framing:** This file treats *the status quo* as the vendor being scored. The BRIEF's 26-dimension
capability matrix is applied to the incumbent DIY stack (Excel + Outlook + Procore + a person), because
that is the thing the founder is actually displacing.
**Date of research:** 19 August 2026. All Reddit sources are dated; job postings were live on 19 Aug 2026.

---

## RESEARCH METHOD & LIMITATIONS (read this first)

- **Reddit was reachable only via the Arctic-Shift archive API** (`arctic-shift.photon-reddit.com`),
  because reddit.com, all Redlib mirrors, PullPush, and Google/Bing/DDG were blocked or challenge-walled
  from this session's rotating datacenter IPs. Every Reddit quote below carries a live `reddit.com`
  permalink recovered from that archive and is verifiable.
- **LinkedIn's guest job API was reachable**, so job postings are primary-source with URLs and, where the
  employer published one, real salary bands.
- **CFMA's paywalled Benchmarker was partially recovered** through two publicly-linked sample files on
  cfma.org (a peer-comparison Excel and the full FY2024 all-companies Excel). These are the single most
  valuable numbers in this report.
- **A serious data-quality caveat on Reddit:** r/ConstructionManagers in 2025–2026 is heavily polluted by
  AI-written vendor marketing accounts. I have labelled every quote `[PRACTITIONER]` or `[VENDOR/SUSPECT]`.
  Only `[PRACTITIONER]` quotes should be used as evidence of demand. **This pollution is itself a finding**
  — see §9.
- **Not established:** a defensible industry-wide dollar figure for change-order write-offs. See §11.

---

## 1. SNAPSHOT: WHAT THE INCUMBENT IS

The competitor is not a product. It is a **staffed manual process** with three layers:

| Layer | What it is | Who pays for it |
|---|---|---|
| **People** | Project engineer → project manager → contract administrator → project executive; plus claims consultants bought by the hour when it goes wrong | Charged to job cost (field) or G&A (office) |
| **General tools** | Excel/Google Sheets, Outlook, Word, PDF, Bluebeam, SharePoint/Dropbox/Google Drive, Teams, phone camera, text messages | Already bought (Microsoft 365) — marginal cost ≈ $0 |
| **Construction tools** | Procore, Autodesk Build/ACC, Sage/Viewpoint/Foundation/CMiC/Spectrum, Primavera P6, Fieldwire, Buildertrend | 0.26%–0.40% of revenue (CFMA, below) |

**Market share of the incumbent:** overwhelming. Procore — the category leader — had **17,850 total
customers worldwide as of 31 Dec 2025**, growing only **4% in 2024 and 4% in 2025**
([Procore FY2025 10-K, filed 2026-02-24](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm)).
For reference, that is the whole installed base of the dominant construction PM platform, against a US
construction industry of hundreds of thousands of firms. The default is still spreadsheets and email.

---

## 2. THE ROLE MAP — WHO ACTUALLY DOES THIS WORK

### 2.1 The core finding

**Change-order and entitlement work is already someone's named job — but only above roughly $100M of
revenue, and only in heavy civil, industrial/EPC, federal, and owner-side organisations.** Below that,
it is a fragment of a project engineer's or project manager's week, and there is no budget line for it.

### 2.2 Evidence from live job postings (all captured 19 Aug 2026)

**Dedicated change-order headcount exists and is titled as such:**

| Title | Employer | Location | Published pay | URL |
|---|---|---|---|---|
| **Change Order Engineer** | Tutor Perini | Los Angeles, CA | **$85,000–$120,000** | [link](https://www.linkedin.com/jobs/view/4446696515) |
| **Change Order Engineer (TE3)** | Washington State DOT | Seattle, WA | (state scale) | [link](https://www.linkedin.com/jobs/view/4448078841) |
| **Change Management Analyst** | Michels Corp (MICON Group) | Milwaukee, WI | — | [link](https://www.linkedin.com/jobs/view/4450643118) |
| **Change Management Coordinator** | Zachry Group | Lake Charles, LA | — | [link](https://www.linkedin.com/jobs/view/4393261146) |
| **Onsite Cost Coordinator** (owns CO process end-to-end) | Diamond Technical Services | Glendale, KY | — | [link](https://www.linkedin.com/jobs/view/4440835281) |

**Contract administration / commercial management:**

| Title | Employer | Published pay | URL |
|---|---|---|---|
| Construction Contract Administrator | AEONRG (SDVOSB federal GC) | **$60,000–$75,000** | [link](https://www.linkedin.com/jobs/view/4414614543) |
| Federal Contract Administrator | Jacobs | **$105,800–$185,100** | [link](https://www.linkedin.com/jobs/view/4388117953) |
| Contracts Manager, Industrial | McGough | **$120,000–$155,000** | [link](https://www.linkedin.com/jobs/view/4419916185) |
| Construction Contract Lead | Microsoft (owner side) | **$116,900–$203,600** | [link](https://www.linkedin.com/jobs/view/4453112542) |
| Senior Construction Contract Administrator (EPCM, 15+ yrs) | BBA Consultants | — | [link](https://www.linkedin.com/jobs/view/4423551959) |
| Mining Construction Contract Manager | WSP | — | [link](https://www.linkedin.com/jobs/view/4448808351) |
| Contracts Administrator | Louisiana Bridge Builders (I-10 Calcasieu JV) | — | [link](https://www.linkedin.com/jobs/view/4448200253) |
| Contract Administrator (T&M tickets + CO log) | commercial coatings subcontractor, San Diego | — | [link](https://www.linkedin.com/jobs/view/4451926370) |

**Cost / claims / risk:**

| Title | Employer | Published pay | URL |
|---|---|---|---|
| Construction Claims Manager | AECOM | **$140,000–$182,272** | [link](https://www.linkedin.com/jobs/view/4346086350) |
| Cost Manager, Mission Critical | Ryan Companies | **$115,000–$165,000** (Chicago) / **$130,000–$170,000** (South Bend) | [link](https://www.linkedin.com/jobs/view/4407097520) |
| Risk Manager – Mining Construction | Turner & Townsend | **$140,000–$160,000** | [link](https://www.linkedin.com/jobs/view/4426999907) |
| Construction Risk Manager | Jacobs | **$120,000–$200,000** | [link](https://www.linkedin.com/jobs/view/4338590085) |
| Senior Manager – Construction Dispute Resolution | SOCOTEC Advisory | — | [link](https://www.linkedin.com/jobs/view/4122684984) |
| Chief Estimator | Shawmut Design and Construction | **$250,000–$310,000** | [link](https://www.linkedin.com/jobs/view/4388559018) |
| Project Executive | Arena Family of Companies | **$200,000–$260,000** | [link](https://www.linkedin.com/jobs/view/4449676418) |
| Project Engineer | Ames Construction | **$80,000–$120,000** | [link](https://www.linkedin.com/jobs/view/4411531587) |
| Engineer II | Granite Construction | **$79,972–$119,958** | [link](https://www.linkedin.com/jobs/view/4413575760) |

LinkedIn's own result header for "Construction Contract Administrator, United States" reads
**"1,000+ Construction Contract Administrator jobs in United States"**
([search URL](https://www.linkedin.com/jobs/search?keywords=Construction%20Contract%20Administrator&location=United%20States), 19 Aug 2026).

### 2.3 Verbatim job-spec language — these people ARE the product

> "Coordinate with other project team members to **identify customer related actions or inactions, which
> may result in constructive contract changes**. **Recommend and implement actions to document and request
> the additional compensation or time due from the client.** … Review project correspondence to ensure the
> firm's rights are protected…"
> — Jacobs, *Federal Contract Administrator*, $105,800–$185,100.
> https://www.linkedin.com/jobs/view/4388117953

> "**Collect and organize project data: schedules, cost reports, daily reports, RFIs, submittals, meeting
> minutes, time sheets, logs, etc.** Perform initial document reviews to **identify relevant issues,
> including delays, disruptions, or other impacts**. … Assist in preparing exhibits, graphics, and
> supporting documentation for claims and change order requests. Assist with **drafting sections of change
> orders and claims narratives**."
> — Michels Corp, *Change Management Analyst*. https://www.linkedin.com/jobs/view/4450643118
> *(This is, line for line, the hypothesised product pipeline — currently performed by an analyst.)*

> "**Monitor contractual obligations, deliverables, milestones, notices, and deadlines.** Manage contract
> correspondence, records, claims, variations, and supporting documentation."
> — WSP, *Mining Construction Contract Manager*. https://www.linkedin.com/jobs/view/4448808351

> "Lead administration of change orders and variations, **maintaining clear entitlement positions**. …
> A commercially astute, disciplined operator who **protects entitlement** while supporting delivery."
> — Microsoft, *Construction Contract Lead*, $116,900–$203,600. https://www.linkedin.com/jobs/view/4453112542

> "…**prove entitlement for back charges** or develop Client or Engineering change orders as allowed…
> **Ability to identify scope transfer, quantity growth and extra work and determine who caused change.**"
> — Zachry Group, *Change Management Coordinator*. https://www.linkedin.com/jobs/view/4393261146

### 2.4 Role map by company size (synthesised — the size thresholds are `UNVERIFIED` inference from the posting evidence, not a surveyed fact)

| Revenue band | Who owns notice/CO/entitlement | Dedicated headcount? |
|---|---|---|
| **< $25M sub / GC** | Owner-operator or the one PM. Often the same person estimating and billing. | No. Reddit: *"I recently started working as the unofficial PM… I am currently helping to manage Change Orders and T&Ms without dedicated software."* |
| **$25M–$100M** | Project managers, with a shared office admin / contract administrator doing logs and billing. | Rarely; sometimes one CA at ~$60–75K (AEONRG band) |
| **$100M–$500M** | Project executives set policy; PMs execute; a contract administrator or two; chief estimator prices COs. | Usually one contract admin function; claims bought in |
| **$500M–$1B+** | Contracts Manager / Commercial Manager ($120–155K), Risk Manager ($120–200K), sometimes an in-house Claims Manager ($140–182K); General Counsel for disputes. | Yes, a small commercial team |
| **Heavy civil / EPC / mega-project JVs** | Named Change Order Engineers, Change Management Analysts, dedicated Contracts Administrators on-site. | Yes — this is where the money already is |

**Implication for the founder:** the buyer with an existing budget line is the **$100M+ heavy-civil,
industrial/EPC, or federal contractor**, and the **owner/developer** (Microsoft's posting proves owners
staff this too). Below ~$100M there is no line item and no owner of the problem — the product would have
to sell against a person's unpaid overtime.

---

## 3. THE ACTUAL TOOLS — HOW THIS IS LITERALLY DONE

### 3.1 The canonical change-order stack, described by a practitioner

> **[PRACTITIONER]** "I am currently helping to manage Change Orders and T&Ms **without dedicated software**
> for this. I take the information and put into a **google sheet**, to keep it editable, I then **save the
> google sheet as a PDF** (the pdf contains the details of the project, the details of the work, the cost,
> etc). I then **attach the report of the work completed, I.e pictures and description of the work, to the
> pdf**. I then **sign it using BlueBeam** and save. At this point I **send it to the GC for approval**. If
> approved I take the approved or signed doc and **add it as an additional page to the existing pdf**.
> This is very time consuming and tedious. I don't have dedicated software for this. **I know ProCore
> exists but that is out of the budget.**"
> — u/ZealousidealAd9379, r/ConstructionManagers, 6 Feb 2025 (score 9, 18 comments)
> https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/

### 3.2 The Excel change-order log, described in full by the person who built it

> **[PRACTITIONER]** "I use an **excel workbook that I have developed over the years**. **Sheet 1 is a COR
> Log** that tracks everything submitted along with **costs, approval status, and relevant dates**. **Sheet 2
> is a breakdown by cost codes** in the rows and COR numbers in the columns that gets fed by **my individual
> CORs that are Sheets 3-100** and have a nice letterhead for easy transmittal to the client. I send each
> individual COR to a **.pdf printer** before sending to the client and make DAMN sure the cost code sheet is
> not included. I also **send the COR log as an attachment with my pay app every month** so there is no
> miscommunication with my client as to what I am claiming as a COR. **This is the bare minimum. Do you not
> already have something similar in place?**"
> — u/Sad-Tea-3446, r/ConstructionManagers, 7 Feb 2025 (score 6)
> https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/mbelqp0/

That last sentence — *"This is the bare minimum"* — is the single most important line in this report for
pricing and positioning. The DIY stack is not perceived as a deficiency. It is perceived as competence.

### 3.3 Folder-per-issue: the manual evidence graph

> **[PRACTITIONER]** "Every change order **make an issue folder for it on your computer with an issue
> number**. Save correspondence about the CO in the issue folder. When submitting the bill put the issue
> number on the letter. **Log it all in excel**."
> — u/the_t_nastiest, 7 Feb 2025. https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/mbeifrb/

> **[PRACTITIONER]** "Ex. SCO-###-description of work. … Have a **folder for change orders submitted, being
> worked on and approved**."
> — u/Crowned_J, 7 Feb 2025. https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/mbejmzs/

### 3.4 The multi-log reality

> **[PRACTITIONER]** "Along with the change order log, **you also need the PCO log** too. I would add the
> **ROJ and long lead items log** to your list. **And a purchasing log** if you still have unbought scopes
> of work on your project."
> — u/Unusual_Week162, 4 Jul 2026. https://www.reddit.com/r/ConstructionManagers/comments/1unjqv7/new_project_engineer_at_fastpaced_ti_gc_thrown/ovlklru/

### 3.5 How notices are tracked — literally: **they are not**

There is no notice register in the DIY stack. Notice compliance is an artefact of whether somebody
happened to send an email. The tracking mechanisms observed across all sources are:

1. **A same-day confirming email** (most common, and the only thing that reliably works)
2. **A confirming RFI** referencing the verbal direction
3. **A daily log entry** in Procore or on paper
4. **A T&M ticket signed by the field**
5. **Nothing** — until it becomes a dispute

> **[PRACTITIONER]** "RFI like: *'confirming verbal owner direction to XYZ change per discussion from
> yesterday's on site meeting. Please confirm and provide updated detail. Pricing to follow.'* It's so easy
> idk why it has to be difficult."
> — u/LeaningSaguaro, 8 Aug 2026 (score 13). https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2dtifd/

> **[PRACTITIONER]** "It's 2026. **Nothing is verbal.** Pull your iPhone out and email it to me. Hell, hit
> that little voice to text button on it when you tell me and you don't even have to type it. **If you won't
> do that, you have not intent to pay for the changes**" [sic]
> — u/Bull_Pin, 7 Aug 2026 (score 8). https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2d7kmv/

> **[PRACTITIONER, GC side]** "Whenever I give verbal direction to a trade, I always say *'send me an email
> so I can confirm'*. Usually I'll beat them to it but it is nice when a trade is on top of their crap and
> sends me a recap of a convo so I can just reply with *'yes, please proceed.'*"
> — u/joefromjerze, 7 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2csgri/

**No source anywhere in this research described a calendar reminder, a deadline tracker, or a notice
register.** The closest anyone came was a general log discipline:

> **[VENDOR/SUSPECT — plausible but likely a marketing account]** "**Email is the worst possible tool for
> tracking critical drawing changes** because important stuff gets buried in the same inbox as lunch orders
> and CC chains. The guys who don't miss these things have an actual process, **every submittal response,
> RFI response, ASI, and bulletin gets logged into a tracking sheet or platform the moment it lands**, with
> a column for 'field notified'…"
> — u/811spotter, 20 May 2026. https://www.reddit.com/r/ConstructionManagers/comments/1ti3c73/just_got_promoted_but_every_mistake_makes_me_feel/omx1wbq/

### 3.6 Cross-project roll-up fails

> **[VENDOR — Planyard co-founder, disclosed]** "**Most people end up with a workbook per project with tabs
> for each of those. The problem is once you hit 3-4 active projects, those workbooks start living in
> different states and nobody trusts the roll-up numbers anymore.**"
> — u/Top_Drummer_3801, 18 May 2026. https://www.reddit.com/r/ConstructionManagers/comments/1tfhnx0/owner_rep_project_control_templates/omh42ww/
> *(Vendor-affiliated, but the failure mode is corroborated by the practitioner accounts above.)*

### 3.7 The mid-size reality: "we tried 5 tools and still run on texts and spreadsheets"

> **[PRACTITIONER]** "We're a **mid-sized construction company**—residential and light commercial—and it
> feels like **no matter what tool we try, we're still bouncing between spreadsheets, texts, and emails**
> to keep things moving. Biggest challenges right now: Tasks falling through the cracks; Field and office
> not on the same page; No consistent way to track progress or flag issues early; **Reporting is a mess
> unless someone manually builds it.**"
> — u/PhaseCool9084, r/ConstructionManagers, 27 Mar 2025 (score 18, 32 comments)
> https://www.reddit.com/r/ConstructionManagers/comments/1jldzkc/we_tried_5_tools_still_managing_projects_in_texts/

And the top-voted reply in that thread — by the OP himself — is the adoption thesis in one line:

> **[PRACTITIONER]** "So the title should be **'We Tried 5 People… Turns Out the Problem Was Us, Not the
> Software.'**"
> — u/PhaseCool9084, 27 Mar 2025 (score 25). https://www.reddit.com/r/ConstructionManagers/comments/1jldzkc/we_tried_5_tools_still_managing_projects_in_texts/mk2tfpe/

> **[PRACTITIONER]** "I told my team that we'd reposit our information across various software, but we'd
> **stick to good old email, phone calls, and Teams for communication. Within the company drive is where we
> store the information internally** until we are ready to distribute."
> — u/unknowndatabase (Federal Division QC lead at a large GC), 27 Mar 2025 (score 6).
> https://www.reddit.com/r/ConstructionManagers/comments/1jldzkc/we_tried_5_tools_still_managing_projects_in_texts/mk3iz5k/

### 3.8 Corroborating survey data on spreadsheet dependence (`FLAG: 2017 — best available; series discontinued`)

JBKnowledge *2017 ConTech Report* (the classic ConTech IT-budget source). **The series appears to be dead:
jbknowledge.com is now an insurance-technology consultancy with no construction report page**
(https://jbknowledge.com/, retrieved 19 Aug 2026). Latest recoverable full edition:
https://civil808.com/sites/default/files/2017-jbknowledge-contech-report.pdf

- **Workflows dependent on spreadsheets:** Estimating **71%**, Accounting **58.7%**, **Project Management 46.1%**,
  Bid Management 43.3%, Takeoff 33.3%, Project Scheduling 29.8%, Tracking Data/Performance Metrics 29%,
  Field Data Collection 18.9%. *"These dependencies remained consistent no matter the size of the company."* (p.34)
- **How data moves when apps don't integrate:** **Manually 48.7%**, **Spreadsheets 42.6%**, CSV 32.9%,
  Custom-built integration 25.2%, Email 15.9%, *"We don't transfer data"* 13.8%. (p.38)
- **30% of respondents reported that NONE of their applications integrate.** (p.38)
- **The largest single group of respondents used only 2 software solutions**, down from 6+ in 2012. (p.37)
- Survey verbatim: *"**We LOVE manual data entry.** Our Estimating to Operations project turnover files look
  like someone put a copy of Tolstoy's 'War & Peace' on a copy machine and hit 500 copies. Then it's up to
  the PM to 'digitize'."* (p.39)
- Top mobile apps 2017: **1. Procore 2. Bluebeam 3. PlanGrid**; the named app cloud also includes Excel,
  Outlook, OneNote, Office 365, Box, Dropbox, Egnyte, Google Drive, Smartsheet, Viewpoint, CMiC, HCSS, hh2. (pp.31–32)

---

## 4. THE ACTUAL FAILURE MODES — VERBATIM

### 4.1 The core failure, stated by a practitioner-facing thread with 43 comments

> "Every job I've worked, it goes the same way: **GC or owner's rep tells the super something changes in
> the field. Work happens. Nobody writes it down. Weeks later someone's trying to reconstruct who said what
> and whether the notice deadline even got hit, usually because it's now a dispute.** I've seen crews
> **lose money they were owed, not because the work wasn't done, but because nobody could prove the
> timeline.** Curious what you all actually do in practice, not the textbook contract answer. **Text and
> hope? Daily log? Some app? Nothing until it's already a fire?**"
> — u/32_ikigai, r/ConstructionManagers, 7 Aug 2026, *"How do you track verbal field directives before they
> blow up into disputes?"* — **43 comments, post score 0**
> https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/
> `[VENDOR/SUSPECT — this OP was publicly accused in-thread of being an AI-assisted founder doing customer
> discovery; see §9. The framing is nonetheless corroborated by the practitioner replies below.]`

### 4.2 Practitioners on why it happens anyway

> **[PRACTITIONER]** "**Why would you perform change work without some sort of proof of approval?** It
> doesn't matter the deadline, if design changes so does the deadline."
> — u/G_Sizzle97, 11 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p33w1uw/

> **[PRACTITIONER]** "We primarily do heavy civil work with municipalities, DOTs, and some private sites…
> **Most of the time we come across this issue with the private side because they do design build and every
> week something changes.** For those we started being upfront with the RPR that **if we don't have
> something in writing we will submit daily T&M sheets or we just won't do it** until we have something in
> writing. **I don't know that the issue will ever be resolved** but I have been fortunate to have very
> experienced supers that know how to handle these situations."
> — u/G_Sizzle97, 11 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p34cgwg/

> **[PRACTITIONER]** "We never- and I really truly do mean **never**- install work without an executed change
> order or field work directive which formally directs us to proceed while we price. … **Do clients
> sometimes get pissy about it? Yes. But my experience has been that I never have to have the argument more
> than twice.** … Respectfully, if you're doing it any other way you're making bad decisions."
> — u/WelpSeaYaLater, 8 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2fqt8y/

> **[PRACTITIONER — $100M+ contractor experience]** "I've seen the **graveyards of a few dozen $100m+ revenue
> companies** having controls in place to prevent changes without funding approval but still having a
> lessons-learned type discovery item undermining the argument… **Cash flow is everything in this business,
> and even if you think you're entitled, you've now introduced ambiguity that is now a dispute which becomes
> a ticket time bomb**, especially depending on insurance coverage."
> — u/ConstructTech, 12 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p35s2e7/

### 4.3 Where the hours actually vanish (ranking, from practitioners)

Thread: *"What part of the change order process actually consumes the most time?"* — 20 comments.
https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/

> **[PRACTITIONER]** "For us, it's **almost never identifying the extra work**—that usually happens pretty
> quickly. **The real time sink is documenting everything well enough that nobody can dispute it later.
> Photos, marked-up drawings, field notes, labor hours, material tickets, emails... by the time you've
> gathered it all, half the battle is already over.** Then comes the waiting. **A change order can sit in
> someone's inbox for days or weeks while everyone keeps working.** If you don't have a solid paper trail,
> you're in a tough spot when it's time to get paid."
> — u/TheTradeThinker, 9 Jul 2026. https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/owiblz4/

> **[PRACTITIONER]** "Our change order process is **about 30 steps for one change order** starting with an
> issue in the field, leading to an RFI, answer, cost proposal, **a bunch of clicks and Docusign's along the
> way**, and concluding with a signed owner change order and issuance of a commitment to the sub. Reviewing
> the Owner's comments, having the subcontractor revise the CO to address the comments, and resubmit takes
> the longest for me."
> — u/Abydosprime, 17 Jul 2026. https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/oxzvjqq/

> **[PRACTITIONER]** "For me, it's definitely **the approvals**. Everyone seems to have different priorities,
> and **chasing down signatures feels like a full-time job** sometimes. By the time you finally get the green
> light, **you've lost a week or more just waiting around**."
> — u/stealthagents, 18 Jul 2026. https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/oy7aszp/

> **[VENDOR/SUSPECT]** "**Documenting and substantiating is where the hours vanish, and it drags because most
> of it gets reconstructed after the fact from memory and a pile of texts.**"
> — u/811spotter, 8 Jul 2026. https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/owdaxom/

### 4.4 Document control as the named cause of lost change orders

> **[PRACTITIONER]** "you need to be **meticulous with document control**. That's key to being an assistant PM.
> Whether in a Dropbox folder or in procore, that's key to running a project effectively. **There's nothing
> worse than bad document control as that's where change orders get lost**, and close out paperwork gets to
> be a nightmare at the end of a project."
> — u/QuantityAlert6330, 14 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vo84wb/how_do_i_prove_i_am_ready_to_be_a_pm/p3qryix/

### 4.5 Subcontractor-side failure modes (older but structurally unchanged) `FLAG: 2008`

Mike Holt's Forum, *"General Contractor not signing change orders"* (Apr 2008), still the most candid
long-form practitioner discussion I could reach outside Reddit:
https://forums.mikeholt.com/threads/general-contractor-not-signing-change-orders.47657/

> "**Read your contract, any changes done without expressed written approval of the GC will be done at your
> own expense.** Why do you think they don't want to sign the CO? **Be careful who signs it too, I have been
> stiffed more than once because the guy who gladly signed all my changes was not authorized to approve
> changes** even though he said emphatically that he was. **An old trick GCs like to use on big jobs is to
> move in new supervision and a PM at the tail end of a job. These new guys, the closers, will have no
> recollection of anything said by the previous guys and will not pay any changes signed by the unauthorized
> people.**" — u/ITO, 15 Apr 2008

> "the GC also instructed his superintendents to add the following words under their signature, **'My
> signature above only verifies that the work was performed.'** This was used to prevent delays in the job
> BUT more importantly **to give him a way out of paying for the C/O's**. I learned later… that the GC argued
> at the final meeting that his superintendents were not authorized to approve C/O's." — u/sparky 134, 14 Apr 2008

> "There was no dispute on change orders during the work and **was told to just get the job done. We were
> also told not to delay job for signatures or they would bring someone else in to do the work.** Then when
> the job was done I had to actually go down and meet with them about the change orders because they
> disputed some of them. **We ended up dropping some small ones to actually get final payment.**"
> — u/ajlehman, 15 Apr 2008 (electrical scope, $1.2M) — **this is a documented write-off**

> "**The biggest problem I found was, as long as the power panels were not up and working, everyone was your
> friend but once the power was on, everyone forgot your name. Never wait to bill for a change order… If you
> wait until the end of the project you will most likely never see your money.**" — u/BAHTAH, 15 Apr 2008

> "**We have some customers that we handle 5 and 6 figure changes verbally. Others we won't spend an extra
> $100 without them signing first.**" — u/petersonra, 15 Apr 2008
> *(The relationship objection, stated plainly, 18 years ago.)*

### 4.6 The legal failure mode, with real cases

**Smith Currie & Oles, *"Strict Compliance with Mandatory Notice Provisions Required in Washington State"*,
11 Mar 2024** — https://www.smithcurrie.com/publications/common-sense-contract-law/strict-compliance-with-mandatory-notice-provisions-required-in-washington-state/

> "The City issued **16 change orders**… However, Carey did not agree with most of the adjustments and
> attempted to **protest nine of the change orders**. … *'A change order that is not protested as provided in
> this [s]ection shall be full payment and final settlement of all claims for [c]ontract time and for all
> costs of any kind, including costs of delays… By not protesting as this [s]ection provides, the
> [c]ontractor also **waives any additional entitlement**.'*"
> The contract also required the written protest to be supplemented **within 14 days** with cost breakdown
> and schedule analysis.

**Smith Currie, *"Don't Be Litigious; Give Notice"*, 19 Jun 2025** —
https://www.smithcurrie.com/publications/common-sense-contract-law/dont-be-litigious-give-notice/
cites *NOVA Contracting, Inc. v. City of Olympia* (WA Supreme Court): contractor **waived its claim for
extra-work compensation for failure to give immediate notice — "even though the owner had actual notice of
the change"**; and *Cascade Civil Construction v. Jackson Dean Construction* (WA Ct. App.): subcontractor
denied damages **"despite the general contractor causing the issue and having actual notice of the issue in
writing."** Also *Commonwealth v. AMEC Civil* (Va.): *"actual notice is not sufficient."*

**Smith Currie, *"A Guide to Obtaining Payment for Changed Work Not Expressly Authorized"*, 30 Jul 2018** —
https://www.smithcurrie.com/publications/common-sense-contract-law/guide-obtaining-payment-changed-work-not-expressly-authorized/

> "the architect… **tells the contractor to do the work and states that payment will be taken care of at the
> end of the job**. The contractor bills the owner for the changed work at the end of the job. **The owner
> refuses to pay** on the grounds that the architect did not have authority… **The bad news: the contractor
> will probably need to hire a lawyer** to make these arguments."

---

## 5. WRITE-OFF BEHAVIOUR — WHAT I COULD AND COULD NOT ESTABLISH

### 5.1 What is established

**Write-offs happen and are normalised.** Three independent classes of evidence:

1. **Direct practitioner admission of dropping COs to get final payment:** *"We ended up dropping some small
   ones to actually get final payment."* (Mike Holt forum, 2008, $1.2M electrical scope.)
   https://forums.mikeholt.com/threads/general-contractor-not-signing-change-orders.47657/
2. **Structural admission of the small-CO write-off** in the founder-authored problem inventory that a
   practitioner community did *not* dispute on substance: *"When do you charge? $90 CO on a $40k job feels
   petty. But $100 here, $250 there = thousands lost. **Eat small stuff for goodwill, but where's the line?**"*
   — u/Better_Couple2346, 17 Oct 2025. `[VENDOR — founder post, treat as hypothesis not evidence]`
   https://www.reddit.com/r/ConstructionManagers/comments/1o99ydm/whats_your_dream_change_order_solution/
3. **Legal literature treats waiver-by-missed-notice as routine**, and the remedy is described as hiring a
   lawyer (§4.6) — i.e. the economically rational action for small and mid-size amounts is to write off.

**A single, concrete, sourced write-off anecdote** (vendor blog, so treat as illustrative not statistical):

> "During a highways project, their site manager agreed to a variation with the client's representative… a
> straightforward scope change that would add roughly two weeks to the programme and **cost approximately
> £30,000**… The conversation happened on site. Both parties nodded in agreement. The work proceeded
> immediately. **But none of it was recorded**… Three months later… the client's PM had been replaced. The
> new PM… simply replied: **'Where's the evidence this was instructed? I see no record of agreement to
> additional cost.'** Without contemporaneous documentation… **the contractor absorbed the entire £30,000
> loss.**"
> — Gather (vendor blog), 22 Jan 2026. `[VENDOR]`
> https://www.gatherinsights.com/blog/contemporaneous-records-construction-claims

### 5.2 What is NOT established

**I could not find any credible, published, industry-wide quantification of change-order write-offs.**
Attempts made and failed: CFMA article search (no results reachable), Construction Executive site search
(broken), Levelset payment reports (404 — the report series appears retired post-Procore acquisition),
Rabbet Construction Payments Report (404), Arcadis Global Construction Disputes Report (latest publicly
reachable edition is **2022**), HKA CRUX (Cloudflare-blocked), National Law Review search (broken).

**Do not build an ROI model on a write-off percentage. There isn't a defensible one in public.**
See §11 for what would settle it.

### 5.3 The one number that *is* defensible for sizing

**CFMA 2025 Benchmarker, FY2024, n=1,558: Underbillings to Equity = 8.1%**, and **Days in Accounts
Receivable = 55.2**, with **Months in Backlog = 9.1**.
Source: https://cfma.org/files/o-files/view-file/ce6fe0cc-2dfe-420a-999b-a2ad030acd9a
Underbillings (costs and earnings in excess of billings) is the closest audited proxy in the standard
contractor balance sheet for "work performed that has not yet been converted into a billable claim." It is
a *proxy*, not a write-off measure — but it is the number a CFO already looks at, and it is the right hook
for a CFO-level sales conversation.

---

## 6. THE "WE JUST HAVE A GOOD RELATIONSHIP WITH THE OWNER" OBJECTION

**This objection is real, is stated verbatim by practitioners, and is endorsed by lawyers as the *cause* of
the problem.** It is the single largest adoption risk identified in this research.

### 6.1 Practitioners stating it

> **[PRACTITIONER]** "Yeah. **If you have a good relationship with the owner, then verbal approval can be
> more than enough to start the work on the change in the field**, but yes, eventually it will have to get
> wrapped into a change order."
> — u/LeaningSaguaro, 9 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2n3ob2/

> **[PRACTITIONER]** "We work for a number of different contractors and **the key for each is understanding
> how they want COs handled**… **Some, especially those we've worked for a while, will allow us to just bill
> them for the changes - knowing that we'll be fair - and they pay no problem.** The last category are the
> worst: those that say they require signed COs or else they won't pay, but are not willing to sign the COs
> even if the work has already been performed."
> — u/rlane00, Mike Holt Forum, 14 Apr 2008 `FLAG: 2008`
> https://forums.mikeholt.com/threads/general-contractor-not-signing-change-orders.47657/

> **[PRACTITIONER]** "**We have some customers that we handle 5 and 6 figure changes verbally. Others we
> won't spend an extra $100 without them signing first.**" — u/petersonra, 15 Apr 2008, same thread.

### 6.2 The legal profession names relationship-preservation as the root cause — and says the fear is misplaced

> "**Fearing that the relationship will sour, contractors often elect not to follow the formal notice
> requirements in the contract and try to work around the problem or talk through the issue with the owner.
> Unresolved issues often snowball into costly litigation at the end of the project – contravening the
> reason the contractor elected not to follow the formal notice requirements in the first place.**"
> …
> "**It is understandable that contractors do not want to undermine the relationships that they worked hard
> to build and thus do not want to deliver bad news to their customers. But it is important to understand
> that bad news does not age well.**"
> — John T. Crowley, Smith Currie & Oles, *"Don't Be Litigious; Give Notice"*, **19 June 2025**
> https://www.smithcurrie.com/publications/common-sense-contract-law/dont-be-litigious-give-notice/

### 6.3 The counter-evidence: formalising does NOT damage relationships when framed as policy

Multiple practitioners describe formal notice as *de-escalating*, provided it is framed as company policy
rather than as an accusation:

> **[PRACTITIONER]** "Just say **it's against company policy to proceed on verbal approvals otherwise you
> will be written up**. They will understand or they will get upset their plan for free work did not work."
> — u/YungPupper8, 9 Jul 2024. https://www.reddit.com/r/ConstructionManagers/comments/1dz8noz/my_client_is_pushing_me_to_complete_the_change/lcdzwie/

> **[PRACTITIONER]** "If it's a client that doesn't have a lot of experience **approach it from the
> perspective of coaching to avoid an adversarial situation. Explain to them that the change order protects
> both sides.** You know you have an approved change order, they know they have cost certainty, you both
> avoid having to negotiate at the end… **Explain it as a win-win.**"
> — u/Training_Pick4249, 9 Jul 2024. https://www.reddit.com/r/ConstructionManagers/comments/1dz8noz/my_client_is_pushing_me_to_complete_the_change/lcdz8cp/

> **[PRACTITIONER]** "**Defer to your 'partner' 'boss' 'lawyer'.** Instill with your client that you wouldn't
> be doing your job properly if you didn't properly document the change. **'Someone' insists that it must be
> done by the books for the benefit of all.**"
> — u/dzbuilder, 9 Jul 2024. https://www.reddit.com/r/ConstructionManagers/comments/1dz8noz/my_client_is_pushing_me_to_complete_the_change/lcfk31o/

> **[PRACTITIONER]** "If owners bitch about it, some form of the argument **'why do you think I'm only
> required to follow the contract terms that you like and not all of them'** shuts that down very quickly."
> — u/WelpSeaYaLater, 8 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2fqt8y/

**Product implication:** software that *sends* notices on the contractor's behalf will be resisted. Software
that *drafts a confirming email for a human to send*, and gives the PM a policy to hide behind, will not.
The whole thread on verbal directives converges on one artefact: **the same-day confirming email**. That is
the wedge, not the formal notice letter.

### 6.4 The counter-argument that formalising *is* the relationship

> **[PRACTITIONER, GC side]** "It also helps if **you actually follow through on extras regardless of whether
> it's in writing**. 99% of field and office people on a job site act like they're busy 125% of the time but
> in reality **a quick confirmation email takes no time to write or respond**."
> — u/jcbcubed, 8 Aug 2026. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2e9259/

---

## 7. CFMA / INDUSTRY BENCHMARKS — THE ROI DENOMINATOR

**Primary source:** CFMA's **2025 Construction Financial Benchmarker**, fiscal-year **2024** data,
**n = 1,639 submitted / 1,558 in final analysis**, distributed to ~10,000 firms via CFMA + CICPAC.
Executive Summary PDF: https://cfma.org/files/o-files/view-file/ce6fe0cc-2dfe-420a-999b-a2ad030acd9a
Full FY2024 all-companies data workbook (publicly linked sample):
https://cfma.org/files/o-files/download-file/5aff6a42-7a29-491c-bb4a-fde57e74487b
Peer-comparison sample report (segment columns): https://cfma.org/files/o-files/download-file/071f851d-c3b1-43f0-b920-b87e19d85ad6
Prior year (FY2023, n=1,290): https://cfma.org/articles/cfma-s-2-24-construction-financial-benchmarker-executive-summary

### 7.1 Net margin by contractor type — the ROI math is completely different per segment

| Segment | Net income before taxes, FY2024 | FY2023 |
|---|---|---|
| **All companies** (n=1,558) | **6.7%** | 6.3% |
| **Industrial & Nonresidential** (commercial GC/CM — *the classic "GC"*) | **4.4%** | 4.1% |
| **Heavy Construction** (highway/civil) | **8.3%** | 7.2% |
| **Specialty Trade** (subcontractors) | **7.7%** | — |
| NAICS 238210 Electrical Contractors (n=139) | **7.7%** | — |
| **Best in Class (top quartile, all)** | **12.0%** | 11.9% |
| Industrial & Nonresidential — Best in Class | **7.9%** | — |
| Heavy Construction — Best in Class | **15.1%** | — |

**Industrial & Nonresidential net margin by revenue band (FY2024):**
<$10M **3.3%** | $10–24.9M **5.9%** | $25–49.9M **4.7%** | $50–99.9M **3.9%** | $100–299.9M **4.2%** | $300M+ **3.4%**

**Heavy Construction net margin by revenue band (FY2024):**
<$10M **5.8%** | $10–24.9M **8.1%** | $25–49.9M **8.6%** | $50–99.9M **9.8%** | $100–199.9M **8.7%** | >$200M **7.1%**

> **This is the single most important framing fact in the report.** A $200M commercial GC at **4.2% net**
> earns ~$8.4M of pre-tax profit. Recovering **$1M** of otherwise-written-off change orders is a **12%
> increase in company profit**. The same $1M for a specialty trade at 7.7% is a smaller relative win, but
> the sub has far less overhead capacity to fund software. **The GC has the better ROI story; the sub has
> the sharper pain.**

### 7.2 Overhead / G&A structure (FY2024, all companies, % of total revenue)

| Line | % of revenue |
|---|---|
| Gross Profit | **17.77%** |
| **Total SG&A** | **11.33%** |
| — Base Payroll / Payroll Related | 5.41% |
| — Other Expenses | 4.30% |
| — Administrative Bonuses | 0.59% |
| — Professional Fees | 0.50% |
| — Sales & Marketing | 0.28% |
| — **Technology Costs** | **0.26%** |
| Income from Operations | 6.43% |
| **Net Income before Income Taxes** | **6.70%** |

Segment SG&A: **Industrial & Nonresidential 7.3%** of revenue (base payroll 3.6%);
**Specialty Trade 14.8%**; Electrical contractors 13.8%; Specialty Trade $100–300M 11.9%.

### 7.3 Productivity and liquidity context (FY2024)

- Revenue per FTE **$514,587** (first time above $500K in the series); gross profit per FTE **$83,554**
- Industrial & Nonresidential revenue per FTE **$1.24M**; gross profit per FTE **$101,300**
- Current ratio 1.7 · Days of cash 27 · **Days in A/R 55.2** · Days in A/P 32.8 · **Months in backlog 9.1**
- **Underbillings to Equity 8.1%** · Backlog to Equity 4.6 · Debt to Equity 1.3
- Revenue growth 7.3% (down from 10.4%); ROA 12.5%; ROE 32.7%
- Respondent mix: ~4% Residential, **32% Industrial & Nonresidential, 21% Heavy, 42% Specialty Trades**
- FY2023 sample by role: **Subcontractors 45.5%**, General/prime 37.7%, CM (self-perform <20%) 15.1%

---

## 8. SOFTWARE BUDGET REALITY

### 8.1 The hard number (best available anywhere, and it is very recent)

**CFMA 2025 Benchmarker, FY2024: "Technology Costs" is a discrete SG&A line item.**

| Cohort | Technology Costs as % of total revenue | n |
|---|---|---|
| **All companies** | **0.26% – 0.30%** * | 1,558 |
| Company Type: **Specialty Trade** | **0.40%** | 510 |
| Specialty Trade, $100–300M revenue | **0.40%** | 63 |
| NAICS 238210 Electrical Contractors | **0.40%** | 139 |

\* The all-companies workbook computes **0.264%**; the peer-report sample rounds the industry column to **0.30%**.
Sources: https://cfma.org/files/o-files/download-file/5aff6a42-7a29-491c-bb4a-fde57e74487b and
https://cfma.org/files/o-files/download-file/071f851d-c3b1-43f0-b920-b87e19d85ad6

**In dollars, from the same workbook:** average respondent revenue **$139.4M**, **Technology Costs $368K**,
Total SG&A $10.1M, NIBT $7.27M.

*Caveat:* this SG&A line almost certainly **excludes** internal IT payroll (which sits in Base Payroll),
capitalised software, and any technology billed direct to jobs. Treat 0.26–0.40% as the **discretionary
software-and-IT-services purse**, not total cost of technology ownership.

### 8.2 Corroboration `FLAG: 2017`

JBKnowledge 2017 ConTech Report (finance/accounting respondents only), *"What percentage of your company's
annual sales volume was spent on IT?"*: **<1% — 46.4%**, **1% — 21.8%**, **2% — 10%**, 3% — 3.6%,
4% — 1.1%, 5% — 2%, 6% — 1%, ≥7% — 1.8%, don't know — 12.8%.
Report note: *"**Among companies with less than $100 million in annual sales volume, only one respondent
reported allocating over 2% of that sales volume to IT.**"*
Also: **58.8% of contractors recover *none* of their IT expenditure from project owners**; 45.2% do not bill
IT to projects at all. https://civil808.com/sites/default/files/2017-jbknowledge-contech-report.pdf (pp.15–17)

### 8.3 What this implies for a $500–$5,000/month price point

Applying the CFMA 0.26%–0.40% band as the **total technology purse**:

| Contractor revenue | Total annual tech purse @0.26% | @0.40% | Monthly |
|---|---|---|---|
| **$50M** | **$130,000** | $200,000 | $10.8K – $16.7K/mo |
| **$200M** | **$520,000** | $800,000 | $43K – $67K/mo |
| **$1B** | **$2.6M** | $4.0M | $217K – $333K/mo |

Now subtract what is already committed. Anecdotal but consistent Procore pricing signals:

> **[PRACTITIONER, ex-construction-CRM PM]** "**mid-size GCs are either paying $20–40K a year for Procore and
> using a fraction of it, or running their bids and sub networks out of spreadsheets and group texts.**"
> — u/cal3091, 14 Jun 2026. https://www.reddit.com/r/ConstructionManagers/comments/1505c34/is_procore_as_dynamic_as_people_say_it_is/orn3tzp/

> **[VENDOR — Planyard, disclosed]** *"'Does not look like a product that should cost $50k a year' is the
> most accurate one-liner description of Procore I've ever seen."*
> — u/Top_Drummer_3801, 21 May 2026. https://www.reddit.com/r/ConstructionManagers/comments/1dznl14/best_software_to_help_with_construction_management/on2jsb5/

Procore itself publishes **no numbers** on its pricing page (https://www.procore.com/pricing) — it is a
custom-quote motion priced on annual construction volume.

**Conclusion on price point:**

- **$500/month ($6K/yr)** is comfortably inside the discretionary purse at **$50M+** revenue. This is a
  credit-card / departmental purchase. It is *below* the threshold at which most contractors run a
  procurement process. **This is the right V1 price.**
- **$5,000/month ($60K/yr)** is **46% of a $50M contractor's entire technology budget** — impossible.
  At **$200M** it is 7.5–11.5% of the purse — a board-visible line item requiring a CFO business case and
  displacing something. At **$1B** it is 1.5–2.3% — easily affordable, but that buyer runs an enterprise
  procurement, security review, and MSA negotiation, which the BRIEF's solo-founder constraint penalises.
- **The zone of least friction is roughly $500–$1,500/month for a $50–250M contractor**, sold to a single
  project executive or contracts manager, ideally on a per-project rather than per-seat basis (per-project
  pricing maps to how contractors already think and can be job-costed rather than hitting G&A — note that
  **58.8% currently recover no IT from owners**, so a job-costable product is a genuinely differentiated
  commercial design).

### 8.4 The category-leader's growth is the loudest signal about the DIY competitor

Procore FY2025 10-K (https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm):

- **Total customers: 16,367 (2023) → 17,088 (2024) → 17,850 (2025). Growth: 4%, 4%.**
- Revenue $1.0B → $1.2B → $1.3B (21%, 15% growth) — i.e. **essentially all growth is from selling more to
  existing customers, not from converting new contractors off spreadsheets.**
- Customers >$100K ARR: 2,008 → 2,333 → **2,710** (16%, 16% growth), representing **60% → 63% → 66% of total ARR**.
- Customers >$1M ARR: 62 → 86 → **115**, representing 14% → 17% → **20% of total ARR**.
- Derived: **average revenue per customer ≈ $73K**; the ~15% of customers above $100K ARR carry two-thirds of
  revenue; the remaining ~15,140 customers average roughly **$29K/yr**.
- Procore is **discontinuing total customer count disclosure from 2026**, stating: *"we do not believe our
  total customer count is an accurate representation of our business performance."*

**Read:** after 20 years and $1.3B of revenue, the dominant platform adds new logos at 4%/year. The DIY
substitute stack is not losing.

---

## 9. THESIS-THREATENING FINDING: THE COMMUNITY IS ACTIVELY HOSTILE TO THIS EXACT PRODUCT

Four separate 2025–2026 threads in which someone probed precisely this problem space on r/ConstructionManagers
were met with hostility, and in three cases the hostile comment outscored the post:

> **"What are you selling? Another shitty GPT wrapper or poorly created web app you created on Claude Code
> or Codex? Go away. Reported."**
> — u/PianistMore4166, 15 Aug 2026, **score 7** (post score 0), replying to *"Money Leak on change orders!"*
> https://www.reddit.com/r/ConstructionManagers/comments/1vp4kzv/money_leak_on_change_orders/p3ulirs/

> **"If only there was a tool that helps contractors stop losing money to late paperwork on change orders,
> that wasn't not just a pitch! 🙄"**
> — u/Martyinco, 15 Aug 2026, **score 6**, same thread.
> https://www.reddit.com/r/ConstructionManagers/comments/1vp4kzv/money_leak_on_change_orders/p3ulaq4/

> **"Your responses are AI generated. It's not the quality of your writing, it's the tells. Your entire goal
> is to extract value out of these people to create some software. Fuck you."**
> — u/Nacho_Libre479, 8 Aug 2026, on the verbal-directives thread.
> https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2hal07/

> **"But no, whatever software you're developing will not help this problem. The disconnect between those
> who spec the project and those who implement the specs will always be there."**
> — u/Meatloaf0220, 8 Jul 2026, **score 6**.
> https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/owb8a8k/

And the most economically important objection of all:

> **"This is like GC 101 and no one needs more software for anything. CONTRACTING is in the name. All our
> subs are well trained that if they don't have approval from the office for changes, they own it. Usually
> only takes once or twice for them to realize we are serious."**
> — u/sally_sparr0w, 9 Aug 2026.
> https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2p40of/

And on AI specifically in this workflow:

> **"estimating and change orders still need someone who knows the job because the liability when it's
> wrong is too high."**
> — u/Upset-Animal1376, 29 Jul 2026.
> https://www.reddit.com/r/ConstructionManagers/comments/1upnizh/where_is_ai_actually_useful_in_construction/p0k8blg/

> "Nah man this guy is gonna create your change orders in 30 seconds and send them to the client based on a
> photo only. What could go wrong. **Think of all the spare time you'll have because it'll definitely work
> correctly and will definitely take ownership when it makes a mistake.**"
> — u/jd35, 17 Oct 2025. https://www.reddit.com/r/ConstructionManagers/comments/1o99ydm/whats_your_dream_change_order_solution/nk1llle/

**Note the meta-finding:** the practitioner channel a solo founder would naturally use for discovery is
saturated with AI-written vendor astroturf, and the community has developed antibodies. **Reddit is not a
viable acquisition or discovery channel for this product.** Discovery must happen through CFMA chapters,
AGC/ABC contract-risk committees, and direct relationships with contracts managers.

**Counterweight — AI *is* being adopted, just not for entitlement decisions:**

> **[PRACTITIONER, score 16]** "We got **API access to our project management softwares**… **Claude can pull
> data from all of them. I don't trust it to write anything yet.** … I use Claude every day and it **scrapes
> my emails from the past 24 hours and my active jobs' folders and updates my to-do list** which lives in
> Obsidian… I do not use AI to develop estimates or write my emails. **I use it as a tool to speed up work
> and help keep my day organized.**"
> — u/healthycord, 8 Jul 2026. https://www.reddit.com/r/ConstructionManagers/comments/1uqtt61/how_much_has_ai_actually_changed_your_day_to_day/owc58ei/

That is the accepted shape: **read-only, assistive, human-in-the-loop, no outbound action.** Any product
that *sends* a notice will be rejected. A product that *detects and drafts* will not.

---

## 10. CAPABILITY MATRIX — SCORING THE DIY SUBSTITUTE STACK (0–3)

Scoring "how well does Excel + Outlook + Procore + a human already do this?"
**A high score = the incumbent already covers it = bad news for a startup. A low score = white space,
but only counts if §5/§9 show someone will pay.**

| # | Dimension | Score | Justification + URL |
|---|---|---|---|
| 1 | contract_ingestion | **2** | Contracts are reliably received and filed (SharePoint/Egnyte/Procore/company drive) and read by a human; at big firms abstracted into a "contract summary" and a contract database. Not retrievable at the clause level. https://www.linkedin.com/jobs/view/4388117953 |
| 2 | clause_extraction | **2** | Real at scale: Jacobs CAs "develop contract summaries and input contract information into the firm's Contract Database." Absent below ~$100M. https://www.linkedin.com/jobs/view/4388117953 |
| 3 | notice_detection | **1** | No mechanism. Notice compliance is incidental to whether a confirming email got sent. "whether the notice deadline even got hit" is described as unknowable after the fact. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/ |
| 4 | deadline_tracking | **1** | Zero evidence of any notice-deadline tracker in any source. WSP posts a *human* whose job is "Monitor contractual obligations, deliverables, milestones, notices, and deadlines." https://www.linkedin.com/jobs/view/4448808351 |
| 5 | rfi_event_ingestion | **3** | RFI logs are universal and disciplined; RFIs are actively used as the notice instrument. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2dtifd/ |
| 6 | email_ingestion | **2** | Email IS the system of record — Outlook folders, "email owner confirming exactly what was said." But unstructured and unlinked; "important stuff gets buried in the same inbox as lunch orders." https://www.reddit.com/r/ConstructionManagers/comments/1ti3c73/just_got_promoted_but_every_mistake_makes_me_feel/omx1wbq/ |
| 7 | daily_report_ingestion | **3** | Daily reports are produced on essentially every commercial job; supers review sub dailies nightly. https://www.reddit.com/r/ConstructionManagers/comments/1vostkw/turner_boston_family/p3v7gl0/ |
| 8 | schedule_integration | **2** | P6/MS Project are standard at $100M+; but schedule signals are not connected to commercial events — "the math is there, nobody runs it." https://www.reddit.com/r/ConstructionManagers/comments/1u24mqo/what_projectcontrol_signal_do_teams_usually_spot/or8t33v/ |
| 9 | change_order_workflow | **3** | Extremely well covered. COR/PCO logs in Excel, Procore CO modules, DocuSign, 30-step processes. Nobody is missing a change-order workflow. https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/mbelqp0/ |
| 10 | claim_identification | **1** | Reactive and end-of-job. Claims are identified when payment is refused, not when the event occurs. https://www.smithcurrie.com/publications/common-sense-contract-law/guide-obtaining-payment-changed-work-not-expressly-authorized/ |
| 11 | delay_detection | **1** | Slippage "lives in daily logs, informal WhatsApp messages, and toolbox talks — but there's no mechanism to convert 'we're behind' into a commercial signal." https://www.reddit.com/r/ConstructionManagers/comments/1u24mqo/what_projectcontrol_signal_do_teams_usually_spot/or8t33v/ |
| 12 | responsibility_attribution | **2** | Explicitly a staffed human skill at industrial contractors: "identify scope transfer, quantity growth and extra work and **determine who caused change**." https://www.linkedin.com/jobs/view/4393261146 |
| 13 | contemporaneous_evidence_graph | **1** | The only structure is folder-per-issue plus a CO number written on the invoice. No linkage between photo, email, log entry, notice and cost. https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/mbeifrb/ |
| 14 | evidence_completeness | **0** | **Nothing checks whether a claim's evidence is complete before it is submitted.** This is the clearest white space found. Corroborated by the "thousands of photos, hundreds of emails… no coherent narrative" failure pattern. https://www.gatherinsights.com/blog/contemporaneous-records-construction-claims |
| 15 | recoverable_dollar_estimation | **2** | Estimators price COs competently; chief estimators are paid $250–310K. What is missing is estimation of *unclaimed* exposure. https://www.linkedin.com/jobs/view/4388559018 |
| 16 | claim_package_generation | **2** | Done well — by consultants (SOCOTEC, AECOM) and dedicated analysts, at consulting rates. https://www.linkedin.com/jobs/view/4122684984 |
| 17 | notice_drafting | **2** | Humans draft confirming emails and RFIs fluently; templates circulate informally. Quality is inconsistent and depends on the individual PM. https://www.reddit.com/r/ConstructionManagers/comments/1dz8noz/my_client_is_pushing_me_to_complete_the_change/lcdzwie/ |
| 18 | schedule_impact_analysis | **2** | TIA/as-planned-vs-as-built is a mature consulting service; in-house only at large civil contractors. https://www.linkedin.com/jobs/view/4122684984 |
| 19 | procore_integration | **2** | Procore is present at ~17,850 firms globally and is the default at mid/large GCs — but subs describe it as overkill and out of budget. https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm |
| 20 | autodesk_integration | **2** | ACC/Autodesk Build is the explicit cost-driven alternative to Procore. "I would have selected Procore 100% if it was in the budget." https://www.reddit.com/r/ConstructionManagers/comments/1ij9g2g/change_order_management/mbh67t4/ |
| 21 | outlook_gmail_integration | **2** | Perfect human integration (email is the tool), zero automation. The gap is machine access to the mailbox, not the mailbox. |
| 22 | mobile_workflow | **3** | Universal: phone camera, voice-to-text, texts, tablet daily logs. "Pull your iPhone out and email it to me." https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p2d7kmv/ |
| 23 | audit_trail | **2** | Email timestamps + Bluebeam-signed PDFs + dated logs are accepted evidence; but a log entry "can be waved away as something you typed up afterwards." https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/p3fbz1t/ |
| 24 | portfolio_risk | **1** | Fails at 3–4 concurrent projects: workbooks diverge and "nobody trusts the roll-up numbers anymore." https://www.reddit.com/r/ConstructionManagers/comments/1tfhnx0/owner_rep_project_control_templates/omh42ww/ |
| 25 | performance_pricing_compatibility | **2** | The market already understands contingent claims economics (claims consultants, dispute-resolution practices), so success-fee pricing is culturally legible. |
| 26 | consultant_replacement_potential | **1** | The DIY stack does not replace consultants — firms hire SOCOTEC/AECOM/Michels analysts precisely because it can't. That is the opportunity, and also the incumbent to beat. https://www.linkedin.com/jobs/view/4346086350 |

`SCORES| 2,2,1,1,3,2,3,2,3,1,1,2,1,0,2,2,2,2,2,2,2,3,2,1,2,1`

---

## 11. ANSWERS TO THE FOUR KEY QUESTIONS

### Q1 — Which missed-revenue problem happens MOST FREQUENTLY in practice, per practitioners (not vendors)?

Ranked from practitioner testimony, most→least frequent:

1. **Work performed on verbal direction with no same-day written confirmation.** Named as the pattern by
   the OP and confirmed by every substantive reply on the 43-comment thread; independently the subject of a
   78-comment 2024 thread; independently the subject of the entire 2008 Mike Holt thread. It is the
   universal failure. https://www.reddit.com/r/ConstructionManagers/comments/1vicb7d/how_do_you_track_verbal_field_directives_before/
2. **Substantiation/documentation debt** — the evidence exists but is scattered and gets reconstructed after
   the fact. *"The real time sink is documenting everything well enough that nobody can dispute it later."*
   https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/owiblz4/
3. **Approval latency** — COs sitting in inboxes for weeks while work continues at risk; *"chasing down
   signatures feels like a full-time job."*
   https://www.reddit.com/r/ConstructionManagers/comments/1uqwkjg/what_part_of_the_change_order_process_actually/oy7aszp/
4. **Small-CO write-off for goodwill** — the "$90 CO on a $40k job" problem. Frequent but individually tiny.
5. **Signature-authority failure** — the person who signed wasn't authorised; "the closers" arrive at the end
   of the job. Less frequent but high severity.
   https://forums.mikeholt.com/threads/general-contractor-not-signing-change-orders.47657/
6. **Formal notice-deadline waiver.** This is the *lawyers'* headline problem and the one that produces
   reported cases (NOVA v. Olympia, Cascade Civil, C.A. Carey). **But it is NOT what practitioners talk
   about.** Across every Reddit thread reached, practitioners discussed *approval* and *proof*, almost never
   *notice periods*. **Notice-deadline compliance is a lawyer's frame, not a PM's frame.**

**Product consequence:** a "notice deadline tracker" is selling the lawyer's problem to the PM's budget.
The frequently-felt problem is *"a change happened and nothing got written down today."*

### Q2 — Is the pain acute enough that someone is already spending money or hours on it?

**Yes — money, but only above roughly $100M revenue and only in specific verticals; hours everywhere else.**

Evidence of *money already being spent*:
- Tutor Perini employs **Change Order Engineers at $85–120K**. https://www.linkedin.com/jobs/view/4446696515
- WSDOT employs **Change Order Engineers** for the SR 520 program. https://www.linkedin.com/jobs/view/4448078841
- Michels employs **Change Management Analysts** whose job description is this product's pipeline. https://www.linkedin.com/jobs/view/4450643118
- AECOM pays **$140,000–$182,272** for a Construction Claims Manager. https://www.linkedin.com/jobs/view/4346086350
- Microsoft (owner side) pays **$116,900–$203,600** for a Contract Lead to "protect entitlement." https://www.linkedin.com/jobs/view/4453112542
- SOCOTEC runs a whole Dispute Resolution practice on this. https://www.linkedin.com/jobs/view/4122684984
- LinkedIn shows **1,000+ open Construction Contract Administrator roles in the US**.

Evidence of *silent absorption* below that line:
- The sub PM building his own Google-Sheet→PDF→Bluebeam pipeline because *"ProCore… is out of the budget."*
- The Excel-workbook COR log described as *"the bare minimum."*
- Dropping change orders to secure final payment (Mike Holt 2008).

**Net: the pain is loud but the budget is concentrated.** For the top of the market the product competes
against a salaried human (attractive: $85–180K/yr is a huge budget umbrella). For the bottom it competes
against unpaid evenings (brutal: willingness to pay approaches zero, as the Procore-is-out-of-budget quotes
show).

### Q3 — Realistic annual software budget for $50M / $200M / $1B contractors, and what it implies

Using CFMA FY2024 **Technology Costs 0.26%–0.40% of revenue** (n=1,558):

| Revenue | Total annual technology purse | Typical committed spend (Procore/ERP/estimating, anecdotal) | Realistic **incremental** budget for a new point tool |
|---|---|---|---|
| **$50M** | **$130K–$200K** | ~$20–40K Procore-class + accounting ERP | **$5K–$15K/yr** — i.e. **$400–$1,250/month** |
| **$200M** | **$520K–$800K** | $50K+ platform, ERP, P6, Bluebeam, estimating | **$25K–$75K/yr** — i.e. **$2,000–$6,000/month** |
| **$1B** | **$2.6M–$4.0M** | Enterprise ERP + platform + full IT dept | **$100K–$300K/yr**, but requires procurement, security review, MSA |

**Implication for a $500–$5,000/month price point:**
- **$500/mo is right for the $50M–$150M band** and is the only price a solo founder can sell without a
  procurement cycle. It sits under most signature thresholds.
- **$5,000/mo requires the $200M+ buyer** and a defended business case; it is a 4–7 month sales cycle,
  a security questionnaire, and an MSA — which the BRIEF's solo-founder constraint penalises heavily.
- **Best structural fit: per-project pricing (~$300–$1,000/project/month) rather than per-seat.** It maps to
  how contractors budget, it can be **job-costed rather than charged to G&A**, and it therefore escapes the
  0.26%-of-revenue technology cage entirely. Note that **58.8% of contractors today recover nothing from
  owners for IT** — a job-costable, owner-recoverable product design is genuine commercial differentiation,
  not just a pricing tactic.
- **Do not price on a share of recovered value in V1.** The market understands contingency (claims
  consultants work that way), so it is legible — but it requires attribution proof the product cannot
  produce until it has a history, and it invites the "you're just a GPT wrapper taking a cut" reaction
  documented in §9.

### Q4 — Would formal notice automation be culturally rejected?

**Yes, if it sends. No, if it drafts.**

Rejected:
- **Automated outbound notice.** The relationship objection is real and stated verbatim (§6.1), and the
  legal profession confirms contractors deliberately suppress formal notice to protect relationships (§6.2).
  An AI that fires a contractual notice at an owner without a human decision would be, in the words of the
  community, *"a ticket time bomb."*
- **Anything that looks like an AI making a commercial judgement.** *"estimating and change orders still
  need someone who knows the job because the liability when it's wrong is too high."*
- **Anything that arrives through Reddit-style community marketing** (§9).

Not rejected:
- **The same-day confirming email.** This is already the accepted, culturally-native artefact. Every
  practitioner in the biggest thread converged on it independently. Automating its *drafting* — "here is the
  confirming email for what your super was told this morning, review and send" — is assistive, human-in-the-
  loop, and matches the accepted shape of AI use already reported (§9, u/healthycord).
- **Policy-as-shield framing.** Practitioners already deflect relationship friction onto policy: *"it's
  against company policy to proceed on verbal approvals,"* *"defer to your 'partner' 'boss' 'lawyer'."* A
  product positioned as *the company's standard process* rather than *a distrust mechanism* inherits an
  existing, socially-accepted script.
- **Evidence-completeness checking before a human submits.** Score 0 on the matrix — nothing does this today,
  it is invisible to the owner, and it carries no relationship cost at all.

**Sharpest formulation:** the culturally survivable product is **an entitlement-and-evidence assistant that
never talks to the owner.** The moment it addresses the owner, it stops being software and starts being an
accusation.

---

## 12. WEAKNESSES AND GAPS IN THE INCUMBENT — DELIBERATE OR UNATTENDED?

| Gap | Deliberate (strategy) or Unattended (opportunity)? |
|---|---|
| **No notice-deadline register anywhere** | **Deliberate-adjacent.** Contractors *choose* not to formalise notice to protect relationships (§6.2). A tracker that surfaces deadlines forces a decision they are avoiding. This gap is defended by culture, not by a competitor. Hard opportunity. |
| **No evidence-completeness check (score 0)** | **Unattended.** Nobody is against it, nobody has built it, and it costs no relationship capital. **Best white space found.** |
| **No commercial-event detection from daily reports/email** | **Unattended, but low perceived value** — practitioners say identifying extra work is the easy part. Sell it as *evidence capture at the moment of the event*, not as detection. |
| **Portfolio roll-up fails at 3–4 projects** | **Unattended.** Felt by project executives and CFOs, not by PMs. This is the executive-buyer hook. |
| **Claim package generation only via consultants** | **Deliberate on the consultants' part** (it is their revenue). Attacking it means competing with AECOM/SOCOTEC on credibility, which a solo founder cannot do in V1. |
| **Procore not affordable for subs** | **Deliberate** — Procore prices on construction volume and is explicit that SMB is a small share of ARR and that it is de-emphasising the metric. **The sub market is being actively abandoned by the leader.** |
| **58.8% recover no IT cost from owners** | **Unattended commercial design gap** — an opportunity to make the product job-costable and owner-recoverable. |

---

## 13. HARDEST FACTS (5 strongest numeric findings)

1. **Commercial GCs (CFMA "Industrial & Nonresidential") ran a 4.4% net income before taxes in FY2024** and
   4.1% in FY2023 — versus 6.7% for all contractors, 8.3% for heavy civil and 7.7% for specialty trades.
   By size, commercial GCs at $100–300M revenue made **4.2%** and above $300M just **3.4%**. n=1,558.
   https://cfma.org/files/o-files/view-file/ce6fe0cc-2dfe-420a-999b-a2ad030acd9a
2. **"Technology Costs" is 0.26% of revenue for the average contractor (0.40% for specialty trades)** —
   $368K on $139.4M of revenue, inside a total SG&A of 11.33%. FY2024, n=1,558.
   https://cfma.org/files/o-files/download-file/5aff6a42-7a29-491c-bb4a-fde57e74487b
3. **Procore's total customer count grew 4% in 2024 and 4% in 2025 (16,367 → 17,088 → 17,850)** while revenue
   grew 21% and 15% — all growth from existing accounts. It is discontinuing total-customer disclosure in
   2026. The DIY stack is not being displaced.
   https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm
4. **Dedicated change-order headcount is real and priced: Tutor Perini "Change Order Engineer" $85,000–$120,000;
   AECOM "Construction Claims Manager" $140,000–$182,272; Microsoft "Construction Contract Lead"
   $116,900–$203,600; and LinkedIn lists 1,000+ open US Construction Contract Administrator roles.**
   https://www.linkedin.com/jobs/view/4446696515 · https://www.linkedin.com/jobs/view/4346086350 · https://www.linkedin.com/jobs/view/4453112542
5. **71% of contractors' estimating and 46.1% of project management workflows ran on spreadsheets; 48.7% moved
   data between systems manually and 30% said none of their applications integrate** — JBKnowledge 2017
   ConTech Report, the last full edition of the series (JBKnowledge has since exited construction tech).
   https://civil808.com/sites/default/files/2017-jbknowledge-contech-report.pdf `FLAG: 2017`

---

## 14. UNKNOWNS — AND WHAT WOULD SETTLE THEM

| Unknown | What would settle it |
|---|---|
| **Dollar magnitude of change-order write-offs.** No credible public number exists. | CFMA's full Benchmarker subscription (the questionnaire captures claims/disputes data not in the free summary); or a direct survey of 30–50 contract administrators; or a surety/insurer data set. `UNVERIFIED` — do not model ROI on any published write-off percentage. |
| **What share of contractors have any notice register at all.** | A single-question survey through a CFMA chapter or AGC contract-risk committee. My finding of "essentially none" rests on absence of evidence across ~15 threads and ~30 job postings, which is suggestive, not conclusive. |
| **Actual Procore contract values by contractor size.** Procore publishes nothing; my $20–50K/yr band is Reddit anecdote. | Vendr/Spendflo benchmark data (both blocked in this session), or 3–5 contractor reference calls. |
| **Where exactly the "dedicated contracts headcount" threshold sits by revenue.** | Cross-tab of job-posting employer revenue against role existence, or CFMA staffing benchmarks. My $100M threshold is inference from posting patterns, labelled `UNVERIFIED`. |
| **Whether the hostility observed on Reddit generalises to the real buyer.** The people who mocked the idea are PMs and supers, not project executives or CFOs — who were absent from every thread. | Direct conversations with 10 project executives / contracts managers at $100M–$1B contractors. **This is the single highest-value next research action.** |
| **Latest Arcadis / HKA CRUX dispute-cause data (both unreachable).** Arcadis' latest publicly reachable edition is 2022; HKA CRUX is Cloudflare-blocked. | Direct download of the 2025/2026 Arcadis Global Construction Disputes Report and HKA CRUX Insight from an unblocked network. These would give authoritative "% of claims failing on records/notice." |
| **CFMA Specialty Trade and Industrial segment SG&A/technology detail beyond the free sample columns.** | A CFMA Benchmarker subscription (cfma.org/benchmarker). |

---

## 15. STARTUP POSTURE VS THE INCUMBENT

The DIY stack cannot be a partner or a channel — it is the thing being replaced. The correct framing:

- **Do not fight the Excel change-order log.** It is competently built, emotionally owned, and described as
  "the bare minimum." Read from it; do not replace it.
- **Do not fight Procore.** It is present at the buyer with money and absent at the buyer without money.
  Sit beside it.
- **Fight the gap the humans admit to:** the interval between "a change happened in the field this morning"
  and "somebody wrote it down in a form that survives a dispute." Every practitioner source in this report
  independently identified that interval as where the money leaks, and none of them has a tool for it.
- **The product that survives contact with this culture is:** ingest email + daily reports + photos →
  detect that a commercial event occurred → assemble the evidence → **draft the confirming email and flag the
  entitlement and the deadline to a human** → score evidence completeness → roll up exposure for the project
  executive. **It must never send anything to an owner by itself.**

