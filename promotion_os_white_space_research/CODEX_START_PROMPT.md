# Codex kickoff prompt

You are the research director for this repository.

Read `AGENTS.md`, `research/COMPANIES.md`, `research/CAPABILITY_MATRIX.md`,
`research/WHITE_SPACE_SCORING.md`, and every file in `managers/` before beginning.

This is a research project, not an implementation project.

Your assignment:

1. Delegate one research subagent per company listed in `research/COMPANIES.md`.
2. Have each agent complete the standardized company report using
   `research/templates/company_report.md`.
3. Research agents must use current web research and prioritize official product
   pages, official docs, API docs, security/compliance pages, pricing, and case studies.
4. Run agents in parallel where practical. If the subagent concurrency limit is reached,
   queue the remaining companies in additional waves.
5. After the company agents return, send each category's reports to its assigned
   category manager for review and normalization.
6. Managers must reject unsupported statements and request/research corrections
   rather than filling gaps by assumption.
7. Have the chief synthesis manager merge the verified results into one master
   capability matrix and identify at least five possible white-space theses.
8. Assign the red-team manager to attack every thesis and search for competitors,
   substitutes, internal-build alternatives, legal-service substitutes, and switching
   barriers that invalidate it.
9. Only after red-team review, have the final decision manager rank surviving
   opportunities and issue a GO / PIVOT / KILL recommendation.
10. Do not begin coding a product.

The objective is not to validate Promotion OS.
The objective is to discover whether there is a sufficiently large enterprise
white space worth spending substantial development time on.

A KILL recommendation is a successful result if the evidence supports it.

When finished, ensure these files exist:

- `outputs/company_reports/*.md`
- `outputs/category_summaries/*.md`
- `outputs/final/master_capability_matrix.csv`
- `outputs/final/candidate_white_spaces.md`
- `outputs/final/red_team_report.md`
- `outputs/final/final_decision.md`
- `outputs/final/executive_summary.md`

At the end, report only:
- completion status
- reports generated
- top 3 surviving gaps (if any)
- final GO / PIVOT / KILL verdict
- links/paths to final artifacts
