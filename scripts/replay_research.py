"""Replay the full research registry on copied evidence, preserving original files."""
from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def evidence_hashes():
    paths = list((ROOT / "research").rglob("*"))
    paths += [ROOT / name for name in
              ("discovery-log.md", "research-problem.md", "research-protocol.md", "main_prompt.md")]
    return {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".lock"
    }


def main():
    if sys.flags.optimize:
        raise SystemExit("Assertions must be enabled; unset PYTHONOPTIMIZE.")
    if len(sys.argv) != 1:
        raise SystemExit("Research replay is all-or-nothing; no selection arguments are accepted.")
    before = evidence_hashes()
    with tempfile.TemporaryDirectory(prefix="arisearch-replay-") as directory:
        checkout = Path(directory)
        shutil.copytree(ROOT / "research", checkout / "research",
                        ignore=shutil.ignore_patterns("__pycache__", "*.lock"))
        for name in ("discovery-log.md", "research-problem.md", "research-protocol.md", "main_prompt.md"):
            shutil.copy2(ROOT / name, checkout / name)
        result = subprocess.run(
            [sys.executable, "research/searches/verify.py"], cwd=checkout,
        )
    if evidence_hashes() != before:
        raise SystemExit("Research files changed during verification; investigate concurrent writers.")
    if result.returncode:
        print(f"Research replay failed (exit {result.returncode}). "
              "Original research files are unchanged.", flush=True)
    else:
        print("Research replay passed. Original research files are unchanged.", flush=True)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
