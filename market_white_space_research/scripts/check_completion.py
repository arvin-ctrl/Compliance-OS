from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]

signals = sorted((root / "outputs" / "signals").glob("*.md"))
dossiers = sorted((root / "outputs" / "dossiers").glob("*.md"))
reviews = [
    "manager_1_promotion_memo.md",
    "manager_2_validation_memo.md",
]
finals = [
    "red_team_report.md",
    "opportunity_ranking.md",
    "top_picks.md",
    "executive_summary.md",
]

missing_reviews = [x for x in reviews if not (root / "outputs" / "manager_reviews" / x).exists()]
missing_finals = [x for x in finals if not (root / "outputs" / "final" / x).exists()]

print(f"Scout signal files: {len(signals)}/12 expected")
print(f"Dossiers: {len(dossiers)} (target: one per promoted hypothesis)")
print(f"Manager reviews: {len(reviews) - len(missing_reviews)}/{len(reviews)}")
for x in missing_reviews:
    print(" - missing", x)
print(f"Final artifacts: {len(finals) - len(missing_finals)}/{len(finals)}")
for x in missing_finals:
    print(" - missing", x)

ok = len(signals) >= 12 and not missing_reviews and not missing_finals
sys.exit(0 if ok else 1)
