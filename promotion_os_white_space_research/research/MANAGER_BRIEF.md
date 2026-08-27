# Category Manager — Operating Brief

This brief applies to the four category managers (A–D). Read it fully before reviewing.

## Role

You are a quality-control manager, not a summarizer. Company research agents have
completed their reports. You must verify, challenge, normalize, and then synthesize
your category. Follow your manager rules file exactly.

## Required reading

1. `managers/<your manager file>` — your rules and required summary sections
2. `research/AGENT_BRIEF.md` — what the research agents were instructed to do
3. `research/CAPABILITY_MATRIX.md` — scoring definitions
4. Every company report in your category: `outputs/company_reports/<NN>_*.md`
5. Every evidence file in your category: `outputs/evidence/<NN>_*.jsonl`

## QC method

For every report in your category:

1. Check every score of 3 or 4 against its cited evidence records. If evidence is
   marketing-only, missing, or does not support the score, verify it yourself with
   targeted WebSearch/WebFetch (load via ToolSearch). If still unsupported,
   downgrade it in your normalization block.
2. Check 0 scores: were they justified by positive evidence/reasoning, or should
   they be `?` or higher? Spot-verify suspicious 0s.
3. Distinguish documented behavior from researcher inference; flag inference
   presented as fact.
4. Note contradictions between marketing and technical documentation and resolve
   them (docs win).
5. Identify capabilities that could plausibly be configured for the regulatory/
   authorization use case even if not marketed for it.
6. Assess: is "this vendor + internal engineering" a credible substitute for the
   proposed Promotion OS wedge (see J01–J10 in the capability matrix)?
7. Collect and deduplicate the adjacent competitors the agents discovered; add any
   material omitted competitor to your appendix.

Do NOT edit the raw company reports. All corrections go in your summary file.

## Deliverable

Write `outputs/category_summaries/<your file>`:

- Manager A → `manager_A_promotion_administration.md`
- Manager B → `manager_B_incentive_decisioning.md`
- Manager C → `manager_C_compliance_risk.md`
- Manager D → `manager_D_policy_infrastructure.md`

Required structure:

### 1. QC review per report
For each company: verification performed, challenged claims, and whether the report
is APPROVED or APPROVED WITH CORRECTIONS.

### 2. Score normalization block
A machine-readable fenced csv block listing ONLY squares you are changing:

```csv
company,square,agent_score,normalized_score,reason
Votigo,B03,3,1,"latency claim is marketing-only; no docs"
```

If no changes for a company, state so explicitly. Downstream synthesis will apply
agent scores + your overrides.

### 3. Category analysis (required by your manager file)
- strongest incumbent
- most dangerous substitute
- capabilities already commoditized
- capabilities partially covered
- apparent gaps
- gaps that are probably too small to monetize
- gaps worth passing to synthesis

### 4. Internal-build / stack-substitute assessment
Can enterprises in your category's buyer base cover the J01–J10 hypothesis with
your category's vendors + internal engineering + counsel? Be specific.

### 5. Adjacent competitor appendix
Deduplicated list with one-line relevance notes; mark any that materially change
the landscape.

### 6. Approval line
End with: `REPORTS APPROVED: <list of report filenames>` (required before chief
synthesis may begin).

## Return value (your final message)

Compact status only: summary file path, per-report approval status, number of score
overrides, top 3 category findings, gaps worth passing to synthesis.
