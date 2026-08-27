"""Build the master capability matrix from company reports + manager overrides.

Reads the machine-readable score block in Section 12 of each company report,
applies the score-normalization blocks from the four category manager summaries,
and writes:
  outputs/final/master_capability_matrix.csv        (companies x 100 squares, normalized)
  outputs/final/master_capability_matrix_long.csv   (traceability: company,square,
                                                     agent_score,final_score,claim_ids,
                                                     override_reason)
"""
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "outputs" / "company_reports"
SUMMARIES = ROOT / "outputs" / "category_summaries"
FINAL = ROOT / "outputs" / "final"

COMPANIES = [
    ("01_votigo", "Votigo"),
    ("02_sweeppea", "Sweeppea"),
    ("03_rtm", "Realtime Media"),
    ("04_shortstack", "ShortStack"),
    ("05_viralsweep", "ViralSweep"),
    ("06_talonone", "Talon.One"),
    ("07_voucherify", "Voucherify"),
    ("08_openloyalty", "Open Loyalty"),
    ("09_geocomply", "GeoComply"),
    ("10_persona", "Persona"),
    ("11_socure", "Socure"),
    ("12_opa", "OPA"),
    ("13_aws_cedar", "AWS Verified Permissions / Cedar"),
    ("14_cerbos", "Cerbos"),
    ("15_permitio", "Permit.io"),
]

# Normalize the many ways managers may spell company names.
ALIASES = {
    "votigo": "Votigo",
    "sweeppea": "Sweeppea",
    "rtm": "Realtime Media",
    "realtimemedia": "Realtime Media",
    "realtimemediartm": "Realtime Media",
    "shortstack": "ShortStack",
    "viralsweep": "ViralSweep",
    "talonone": "Talon.One",
    "talon1": "Talon.One",
    "voucherify": "Voucherify",
    "openloyalty": "Open Loyalty",
    "geocomply": "GeoComply",
    "persona": "Persona",
    "socure": "Socure",
    "opa": "OPA",
    "openpolicyagent": "OPA",
    "openpolicyagentopa": "OPA",
    "awscedar": "AWS Verified Permissions / Cedar",
    "awsverifiedpermissions": "AWS Verified Permissions / Cedar",
    "awsverifiedpermissionscedar": "AWS Verified Permissions / Cedar",
    "cedar": "AWS Verified Permissions / Cedar",
    "avp": "AWS Verified Permissions / Cedar",
    "cerbos": "Cerbos",
    "permitio": "Permit.io",
    "permit": "Permit.io",
}

SQUARES = [f"{block}{i:02d}" for block in "ABCDEFGHIJ" for i in range(1, 11)]
SQUARE_RE = re.compile(r"^([A-J]\d{2}),\s*([0-4?]),?\s*(.*)$")


def canon_company(raw: str) -> str | None:
    key = re.sub(r"[^a-z0-9]", "", raw.lower())
    return ALIASES.get(key)


def parse_report_scores(path: Path) -> dict[str, tuple[str, str]]:
    """Return {square: (score, claim_ids)} from a report's fenced score block."""
    scores: dict[str, tuple[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = SQUARE_RE.match(line.strip())
        if m:
            sq, score, claims = m.group(1), m.group(2), m.group(3).strip().strip(",")
            if sq in scores and scores[sq][0] != score:
                print(f"  WARN {path.name}: duplicate {sq} ({scores[sq][0]} vs {score}); keeping first")
                continue
            scores.setdefault(sq, (score, claims))
    return scores


def parse_overrides(path: Path) -> list[tuple[str, str, str, str, str]]:
    """Return [(company, square, agent_score, normalized_score, reason)] from a summary."""
    out = []
    text = path.read_text(encoding="utf-8")
    for block in re.findall(r"```(?:csv)?\n(.*?)```", text, re.DOTALL):
        if "normalized_score" not in block:
            continue
        reader = csv.reader(io.StringIO(block))
        for row in reader:
            if len(row) < 4 or row[0].strip().lower() == "company":
                continue
            raw_co, sq = row[0].strip(), row[1].strip().upper()
            company = canon_company(raw_co)
            if company is None:
                print(f"  WARN {path.name}: unknown company '{raw_co}' in override row {row}")
                continue
            if sq not in SQUARES:
                print(f"  WARN {path.name}: unknown square '{sq}' in override row {row}")
                continue
            reason = row[4].strip() if len(row) > 4 else ""
            out.append((company, sq, row[2].strip(), row[3].strip(), reason))
    return out


def main() -> int:
    matrix: dict[str, dict[str, tuple[str, str]]] = {}
    problems = 0

    for slug, name in COMPANIES:
        path = REPORTS / f"{slug}.md"
        scores = parse_report_scores(path)
        missing = [s for s in SQUARES if s not in scores]
        if missing:
            print(f"  ERROR {slug}: missing squares {missing}")
            problems += 1
        matrix[name] = scores
        print(f"  {name}: {len(scores)}/100 squares parsed")

    overrides: list[tuple[str, str, str, str, str]] = []
    for summary in sorted(SUMMARIES.glob("manager_*.md")):
        found = parse_overrides(summary)
        print(f"  {summary.name}: {len(found)} overrides")
        overrides.extend(found)

    override_map: dict[tuple[str, str], tuple[str, str]] = {}
    for company, sq, agent_score, new_score, reason in overrides:
        cur = matrix.get(company, {}).get(sq, ("?", ""))[0]
        if cur != agent_score:
            print(f"  NOTE {company} {sq}: manager cites agent_score={agent_score}, report has {cur} (applying override to {new_score})")
        override_map[(company, sq)] = (new_score, reason)

    FINAL.mkdir(parents=True, exist_ok=True)

    with open(FINAL / "master_capability_matrix.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["company"] + SQUARES)
        for slug, name in COMPANIES:
            row = [name]
            for sq in SQUARES:
                score = matrix[name].get(sq, ("?", ""))[0]
                score = override_map.get((name, sq), (score, ""))[0]
                row.append(score)
            w.writerow(row)

    with open(FINAL / "master_capability_matrix_long.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["company", "square", "agent_score", "final_score", "claim_ids", "override_reason"])
        for slug, name in COMPANIES:
            for sq in SQUARES:
                agent_score, claims = matrix[name].get(sq, ("?", ""))
                final_score, reason = override_map.get((name, sq), (agent_score, ""))
                w.writerow([name, sq, agent_score, final_score, claims, reason])

    applied = len(override_map)
    print(f"\nWrote master_capability_matrix.csv (15 x 100) and long-format traceability file.")
    print(f"Overrides applied: {applied}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
