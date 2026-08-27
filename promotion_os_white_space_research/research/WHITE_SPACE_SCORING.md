# White-Space Scoring Framework

A candidate opportunity is scored 0–5 on each dimension.

## 1. Unmet pain — weight 15%
How severe is the current problem?

## 2. Enterprise economic value — 15%
Potential labor savings, risk reduction, revenue enablement, or loss prevention.

## 3. Competitive gap — 15%
How poorly do existing vendors and substitutes cover it?

## 4. Willingness to pay — 10%
Is there a real budget and identifiable buyer?

## 5. Switching / add-on rationale — 10%
Why adopt this instead of extending the incumbent stack?

## 6. Technical feasibility — 5%
Can an initial product be delivered without impossible dependencies?

## 7. Data / policy defensibility — 10%
Can the company accumulate proprietary operational value?

## 8. Expansion potential — 10%
Can the wedge expand into a broader platform?

## 9. Regulatory durability — 5%
Does the business remain useful as laws/products change?

## 10. Distribution feasibility — 5%
Can customers realistically be reached and sold?

### Weighted score

Score each dimension 0–5, multiply by weight, and normalize to 100.

## Hard gates

A candidate cannot be labeled "GO" if any apply:

- Competitive gap <= 2/5
- Willingness to pay <= 2/5
- Switching/add-on rationale <= 2/5
- No identifiable enterprise buyer
- Value depends primarily on giving unreviewed legal advice
- A generic rules engine + ordinary counsel + simple configuration covers the need cheaply
- The moat is primarily UI, prompt engineering, or branding

## Enterprise displacement test

For every surviving concept write:

> Current stack = [incumbent products + internal process]
>
> New product = [candidate]
>
> Customer changes because = [quantified or strongly evidenced reason]

If this sentence is not compelling, reject the concept.

## Ranking labels

90–100: Exceptional white space
80–89: Strong
70–79: Investigate further
60–69: Weak / likely feature
Below 60: Reject

A GO recommendation normally requires >=80 plus passing every hard gate.
