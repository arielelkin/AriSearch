"""Guarded fresh-output entry point for the fixed mixed discovery generators.

The default family is the angular-first finite pipeline. Historical generator
modules remain immutable replay dependencies; their direct default output
paths must not be used to start a new run.
"""
from __future__ import annotations

import argparse
import math
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def run_generation(output, *, family="angular-first", cpu_cap=540):
    if family not in ("mixed", "angular-first"):
        raise ValueError("unknown finite generator family")
    if not math.isfinite(cpu_cap) or cpu_cap <= 0:
        raise ValueError("CPU cap must be finite and positive")
    output = Path(output).absolute()
    if os.path.lexists(output):
        raise FileExistsError("Output already exists; choose a fresh directory: " + str(output))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir()  # Atomic refusal also covers another process creating it.
    if family == "mixed":
        command = [sys.executable, "-m", "research.discovery.mixed_angles"]
    else:
        command = [sys.executable, "-m", "research.discovery.angular_first", "--worker", "filtered"]
    command += ["--output", str(output), "--cpu-cap", str(cpu_cap)]
    completed = subprocess.run(command, cwd=ROOT, check=False)
    return completed.returncode, output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--family", choices=("mixed", "angular-first"), default="angular-first")
    parser.add_argument("--cpu-cap", type=float, default=540)
    args = parser.parse_args()
    try:
        code, output = run_generation(args.output, family=args.family, cpu_cap=args.cpu_cap)
    except (ValueError, FileExistsError) as error:
        parser.error(str(error))
    print("Run directory: " + str(output))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
