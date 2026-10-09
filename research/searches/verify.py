#!/usr/bin/env python3
"""Nondestructively replay retained certificates and independent verifiers.

Run with the arisearch Conda environment. Outputs are captured in memory and
compared as parsed JSON; retained certificates are never overwritten.
This verifies the recorded finite computations, not global mathematical proofs.
"""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SEARCHES = ROOT / "research/searches"
CERTIFICATE_DIR = ROOT / "research/certificates"
CERTIFICATES = (
    ("walton_vertex_rank.py", "walton_vertex_rank_certificate.json"),
    ("walton_relative_relabeling_rank.py", "walton_relative_relabeling_rank_certificate.json"),
    ("walton_state_assignment_rank.py", "walton_state_assignment_rank_certificate.json"),
    ("nonresonant_5_6_scaffold.py", "nonresonant_5_6_scaffold_certificate.json"),
    ("joint_5_6_local_verify.py", "joint_5_6_local_certificate.json"),
)
VERIFIERS = (
    ROOT / "research/reviews/verify_walton_vertex_rank.py",
    ROOT / "research/reviews/verify_walton_relative_relabeling.py",
    ROOT / "research/reviews/verify_joint_5_6_two_ended.py",
)


def run(script):
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                            capture_output=True, text=True, check=False)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"{script.name} exited {result.returncode}: {detail}")
    return result.stdout


def main():
    if sys.flags.optimize:
        print("FAIL: assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.",
              file=sys.stderr)
        return 1
    failures = []
    for script, certificate in CERTIFICATES:
        try:
            expected = json.loads((CERTIFICATE_DIR / certificate).read_text())
            actual = json.loads(run(SEARCHES / script))
            if actual != expected:
                raise ValueError(f"generated JSON differs from {certificate}")
            print(f"PASS certificate replay: {script}", flush=True)
        except (OSError, ValueError, RuntimeError) as error:
            failures.append(str(error))
            print(f"FAIL: {error}", file=sys.stderr, flush=True)
    for script in VERIFIERS:
        # The endpoint obstruction relies on the distinct-length closure check.
        if script.name == "verify_joint_5_6_two_ended.py" and failures:
            print("SKIP endpoint verifier: resolve certificate failures first.", flush=True)
            continue
        try:
            output = run(script)
            if script.name == "verify_joint_5_6_two_ended.py":
                data = json.loads(output)
                if data["verdict"] != "no plane tiling":
                    raise ValueError("endpoint verifier did not certify no plane tiling")
            print(f"PASS independent verifier: {script.name}", flush=True)
        except (OSError, ValueError, KeyError, RuntimeError) as error:
            failures.append(str(error))
            print(f"FAIL: {error}", file=sys.stderr, flush=True)
    if failures:
        print(f"Verification failed ({len(failures)} failures).", file=sys.stderr)
        return 1
    print("All 5 certificate replays and 3 independent verifiers passed; no certificates written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
