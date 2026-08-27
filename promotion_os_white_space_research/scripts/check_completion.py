from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
expected = [
    "01_votigo.md","02_sweeppea.md","03_rtm.md","04_shortstack.md","05_viralsweep.md",
    "06_talonone.md","07_voucherify.md","08_openloyalty.md","09_geocomply.md",
    "10_persona.md","11_socure.md","12_opa.md","13_aws_cedar.md","14_cerbos.md",
    "15_permitio.md"
]
reports = root/"outputs"/"company_reports"
missing = [x for x in expected if not (reports/x).exists()]

finals = [
    "master_capability_matrix.csv",
    "candidate_white_spaces.md",
    "red_team_report.md",
    "final_decision.md",
    "executive_summary.md",
]
final_dir = root/"outputs"/"final"
missing_final = [x for x in finals if not (final_dir/x).exists()]

print(f"Company reports complete: {len(expected)-len(missing)}/{len(expected)}")
if missing:
    print("Missing company reports:")
    for x in missing: print(" -", x)

print(f"Final artifacts complete: {len(finals)-len(missing_final)}/{len(finals)}")
if missing_final:
    print("Missing final artifacts:")
    for x in missing_final: print(" -", x)

sys.exit(1 if missing or missing_final else 0)
