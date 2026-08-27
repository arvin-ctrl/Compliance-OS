# Project Instructions — Promotion OS White-Space Research

## Objective

Do NOT build Promotion OS.

Research the adjacent market rigorously and determine whether a white space exists that is large and valuable enough to justify an enterprise software company.

## Required delegation

Use subagents for independent company research.

- Assign one company to one research subagent.
- Organize company agents under the category managers defined in `managers/`.
- Category managers must review every report in their category.
- The chief synthesis manager may not begin final synthesis until category managers mark reports complete.
- The red-team manager must independently challenge every candidate white-space opportunity.
- The final decision must wait for the red-team output.

If concurrency limits prevent all company agents from running simultaneously, queue them in waves. Do not collapse multiple companies into one shallow scan merely to finish faster.

## Research quality

Prioritize evidence in this order:

1. official product website
2. official documentation / API docs
3. official security, compliance, trust, and legal pages
4. official case studies
5. official pricing
6. customer documentation / implementation guides
7. credible industry analysis
8. reviews, forums, and customer commentary only for market perception or pain evidence

Never treat marketing language as proof of a capability without locating product documentation, API documentation, an implementation guide, or a concrete workflow where possible.

For each important claim record:
- source URL
- page title
- date accessed
- exact capability supported
- confidence: HIGH / MEDIUM / LOW
- evidence type: official-doc / official-marketing / case-study / third-party / user-report

## White-space standard

A capability missing from competitors is NOT automatically an opportunity.

A candidate white space must pass all of these tests:

1. **Pain** — a meaningful enterprise problem exists.
2. **Frequency** — the problem occurs often enough to justify infrastructure.
3. **Economic consequence** — errors, delay, labor, risk, or lost revenue are material.
4. **Budget owner** — a specific buyer can pay for it.
5. **Platform fit** — software can solve the problem materially better than consulting or a spreadsheet.
6. **Existing-stack inadequacy** — current vendors or internal tooling do not solve it well.
7. **Switch / integration rationale** — a company has a credible reason to add or replace software.
8. **Defensibility** — the advantage is more than UI polish.
9. **Expansion** — the initial use case can expand into a larger product.
10. **Regulatory legitimacy** — do not assume legal conclusions. Identify where licensed counsel or authoritative interpretation is required.

## Anti-bias requirements

Actively search for evidence that invalidates the proposed product.

Do not:
- force the original Promotion OS thesis to survive
- call an integration inconvenience a market gap
- count generic AI features as a moat
- assume regulatory complexity alone creates willingness to pay
- infer that "not mentioned on website" means "not supported"
- claim "nobody does this" without a broad competitor and substitute search
- treat consulting/legal services as irrelevant substitutes

## Enterprise-switch standard

For each candidate opportunity, answer:

> Why would a $50M–$5B company integrate this product instead of continuing with its current vendor + internal engineering + outside counsel?

If the answer is weak, reject the opportunity.

## Required outputs

Use the templates under `research/templates/`.

All final outputs belong under `outputs/`.

Do not overwrite raw company reports during synthesis. Managers create separate summary files.

## Completion gate

The project is complete only when:

- all 15 company reports exist
- all claims in the capability matrix link back to evidence
- all category manager reviews exist
- at least 5 candidate gaps were considered
- red team challenged all candidate gaps
- surviving opportunities include an explicit switching thesis
- final verdict is GO, PIVOT, or KILL
