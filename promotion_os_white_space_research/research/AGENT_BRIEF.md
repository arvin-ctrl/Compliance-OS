# Company Research Agent — Operating Brief

This brief applies to every company research agent. Read it fully before researching.

## Project context

This repository is a market research project testing whether a defensible enterprise
software white space exists at the intersection of promotion/sweepstakes
administration, incentive decisioning, regulatory action authorization,
jurisdiction-aware policy management, compliance evidence/auditability,
identity/geolocation/risk signals, and policy-as-code infrastructure.

The working hypothesis being tested (called "Promotion OS") is a product that would:

- encode jurisdiction-specific regulatory rules as executable, versioned policy (J01)
- provide a legal-to-production deployment workflow with counsel as an approver (J02, J03)
- run impact analysis before policy rollout (J04)
- authorize regulated actions across products in real time (allow/deny/review + reasons) (J05)
- normalize identity/geo/fraud signals across vendors (J06)
- produce evidence-grade decision reconstruction and historical "why was this allowed?" replay (J07, J08)
- offer reusable jurisdiction/domain policy packs (J09)
- act as a regulatory policy lifecycle control plane (J10)

Your job is NOT to validate this hypothesis. Your job is to understand your assigned
company accurately, including capabilities that argue AGAINST the hypothesis.

## Required reading (all in this directory tree)

1. `AGENTS.md` — research quality rules and evidence standards
2. `research/CAPABILITY_MATRIX.md` — the 100 capability squares (A01–J10) you must score
3. `research/templates/company_report.md` — the report template you must complete
4. `agents/<your assignment file>` — your company assignment
5. `research/COMPANIES.md` — your company's row and category

## Research method

- Use WebSearch and WebFetch (load them via ToolSearch if not already loaded).
- Prioritize, in order: official product pages → official docs / API docs →
  security/compliance/trust/legal pages → case studies → pricing → implementation
  guides → credible industry analysis → reviews/forums (only for market perception
  or pain evidence).
- Read actual API documentation and developer docs where they exist. Do not score
  capabilities from feature-name matching on marketing pages.
- If WebFetch fails on a URL (proxy/TLS/404), retry once, then try an alternate
  page or a search-snippet corroborated source; note reduced confidence.
- Today's date for `access_date` fields: **2026-08-18**.

## Deliverables (both required)

### 1. Company report
`outputs/company_reports/<NN>_<company>.md` — exact filename from your assignment file.

Complete ALL 17 sections of `research/templates/company_report.md`. Fill header
fields: Researcher = "Research Agent <NN> (<Company>)", Date = 2026-08-18,
Category and Manager from `research/COMPANIES.md`.

Section 12 (capability matrix scores) MUST contain a machine-readable fenced code
block covering every one of the 100 squares, one line per square:

```csv
square,score,claim_ids
A01,3,VOTIGO-002;VOTIGO-007
A02,?,
...
J10,0,VOTIGO-031
```

- `score` ∈ {0,1,2,3,4,?}
- `claim_ids` = semicolon-separated IDs from your evidence ledger supporting the
  score (empty allowed only for `?` scores and for well-reasoned 0/1 scores where
  you explain the reasoning in notes below the block).
- NEVER score 0 merely because the website does not mention the feature. Use `?`
  when unresolved. A 0 requires positive evidence of absence (e.g. docs enumerate
  the full feature set, an FAQ denies it, the architecture precludes it) or an
  explicit reasoned inference labeled as inference.
- Scores 3–4 require official-doc or equivalently strong evidence, not marketing copy.

### 2. Evidence ledger
`outputs/evidence/<NN>_<company>.jsonl` — one JSON object per line using the schema
in `research/templates/evidence_record.json`:
`claim_id`, `company`, `capability_square` (or "" for general claims), `claim`,
`source_url`, `page_title`, `source_type`
(official-doc | official-marketing | case-study | third-party | user-report),
`access_date`, `confidence` (HIGH | MEDIUM | LOW), `notes`.

Claim IDs: `<COMPANY>-001` upward (e.g. `VOTIGO-001`). Aim for 20+ records; every
important claim in your report should trace to one. Also render the same ledger as
the Section 16 table in your report.

## Additional requirements

- Identify at least 2 adjacent competitors/substitutes (Section 15) with one line
  each on why they matter.
- Section 13 ("white-space implications") must answer all 6 questions concretely
  against the J01–J10 hypothesis above.
- Section 17 verdict: DIRECT THREAT / MAJOR OVERLAP / COMPLEMENT / SUBSTITUTE /
  LOW RELEVANCE, with ≤150-word justification.
- Distinguish clearly between documented behavior, marketing claims, and your own
  inference. Label inference as inference.
- Do not declare or score white spaces. That happens downstream.

## Return value (your final message)

Return a compact status summary only (the files are the deliverable):
- report path + evidence path written
- verdict (Section 17 choice)
- 3–5 most important findings (one line each)
- adjacent competitors discovered
- number of evidence records
- any squares left `?` that materially matter and why
