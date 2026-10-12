"""Check locked research dependencies, command provenance, and solver smoke tests."""

from __future__ import annotations

import shutil
import hashlib
import re
from email.parser import Parser
import importlib.metadata
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlparse


def canonical_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def verify_distributions(prefix: Path, installed: dict, packages: list) -> list[str]:
    """Compare all visible Python distributions with locked package ownership.

    Conda names are not necessarily Python distribution names. Use the metadata
    files owned by the already-checked Conda records, validating their recorded
    hashes before trusting their names and versions.
    """
    errors = []
    expected = {}
    for record in installed.values():
        paths = {entry["_path"]: entry
                 for entry in record.get("paths_data", {}).get("paths", [])}
        for filename in record["files"]:
            if not (filename.endswith(".dist-info/METADATA")
                    or filename.endswith(".egg-info/PKG-INFO")):
                continue
            path = prefix / filename
            # Bundled vendor metadata is not an installed top-level distribution.
            if path.parent.parent.name != "site-packages":
                continue
            if not path.is_file():
                errors.append(f"Missing Conda distribution metadata: {filename}")
                continue
            data = path.read_bytes()
            # Noarch records keep site-packages-relative paths before relocation.
            noarch_path = "site-packages/" + filename.split("/site-packages/", 1)[1]
            entry = paths.get(filename, paths.get(noarch_path, {}))
            digest = entry.get("sha256_in_prefix") or entry.get("sha256")
            if not digest:
                errors.append(f"No recorded hash for Conda distribution metadata: {filename}")
            elif hashlib.sha256(data).hexdigest() != digest:
                errors.append(f"Conda distribution metadata overwritten: {filename}")
            metadata = Parser().parsestr(data.decode("utf-8"))
            name, version = metadata["Name"], metadata["Version"]
            if not name or not version:
                errors.append(f"Invalid Conda distribution metadata: {filename}")
                continue
            expected[canonical_name(name)] = version
    for package in packages:
        if package["manager"] == "pip":
            expected[canonical_name(package["name"])] = str(package["version"])

    seen = set()
    for distribution in importlib.metadata.distributions():
        name = canonical_name(distribution.metadata.get("Name", ""))
        if name in seen:
            errors.append(f"Duplicate Python distribution: {name}")
        seen.add(name)
        if name not in expected:
            errors.append(f"Unexpected Python distribution: {name}")
        elif distribution.version != expected[name]:
            errors.append(f"Python distribution {name}: expected {expected[name]}, "
                          f"got {distribution.version}")
        if not Path(distribution.locate_file("")).resolve().is_relative_to(prefix):
            errors.append(f"Python distribution outside the research environment: {name}")
    for name in sorted(expected.keys() - seen):
        errors.append(f"Missing Python distribution: {name}")
    return errors


def main() -> None:
    import yaml

    if sys.flags.optimize:
        raise SystemExit("Assertions must be enabled; unset PYTHONOPTIMIZE.")

    if len(sys.argv) != 1:
        raise SystemExit("Environment verification accepts no selection arguments.")

    prefix = Path(sys.prefix).resolve()
    lock_path = Path(__file__).resolve().parents[1] / "environment/conda-lock.yml"
    lock = yaml.safe_load(lock_path.read_text())
    installed = {record["name"]: record for path in (prefix / "conda-meta").glob("*.json")
                 for record in [json.loads(path.read_text())]}
    expected_conda = {package["name"] for package in lock["package"] if package["manager"] == "conda"}
    errors = []
    if set(installed) != expected_conda:
        errors.append(f"Conda package set differs: missing={sorted(expected_conda - set(installed))}, "
                      f"extra={sorted(set(installed) - expected_conda)}")
    for package in lock["package"]:
        name, version = package["name"], str(package["version"])
        if package["manager"] == "pip":
            try:
                actual = importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError:
                actual = "missing"
            if actual != version:
                errors.append(f"{name}: expected {version}, got {actual}")
        elif name in installed:
            filename = unquote(Path(urlparse(package["url"]).path).name)
            build = filename.removesuffix(".tar.bz2").removesuffix(".conda")[len(f"{name}-{version}-"):]
            record = installed[name]
            if (str(record["version"]), record["build"]) != (version, build):
                errors.append(f"{name}: expected {version}/{build}, got {record['version']}/{record['build']}")
    errors.extend(verify_distributions(prefix, installed, lock["package"]))
    if errors:
        raise SystemExit("Research environment differs from the lock:\n" + "\n".join(errors))

    import hypothesis
    import matplotlib
    import numpy
    import ortools
    import pytest
    import z3
    from ortools.sat.python import cp_model
    from sage.all import QQ
    from sage.env import SAGE_VERSION

    required_commands = (
        "sage",
        "z3",
        "geng",
        "dreadnaut",
        "dot",
        "jq",
        "pdfinfo",
        "pdftotext",
        "rg",
        "rsvg-convert",
    )
    missing = [command for command in required_commands if shutil.which(command) is None]

    if missing:
        raise SystemExit(f"Missing required commands: {', '.join(missing)}")

    outside = [command for command in required_commands
               if not Path(shutil.which(command)).resolve().is_relative_to(prefix)]
    if outside:
        raise SystemExit(f"Commands must come from the research environment: {', '.join(outside)}")

    assert QQ(1) / 3 + QQ(2) / 3 == 1

    z3_value = z3.Int("smoke_z3_value")
    z3_solver = z3.Solver()
    z3_solver.add(z3_value == 1)
    assert z3_solver.check() == z3.sat

    cp_model_instance = cp_model.CpModel()
    cp_value = cp_model_instance.new_int_var(0, 1, "smoke_cp_value")
    cp_model_instance.add(cp_value == 1)
    assert cp_model.CpSolver().solve(cp_model_instance) == cp_model.OPTIMAL

    print(f"SageMath {SAGE_VERSION}")
    print(f"Z3 {z3.get_version_string()}")
    print(f"OR-Tools {ortools.__version__}")
    print(f"pytest {pytest.__version__}")
    print(f"Hypothesis {hypothesis.__version__}")
    print(f"NumPy {numpy.__version__}")
    print(f"Matplotlib {matplotlib.__version__}")
    print("Nauty/Traces, Graphviz, jq, Poppler, ripgrep, and librsvg commands found")
    print("All locked Conda builds and Python distributions match; research commands use the Conda prefix")


if __name__ == "__main__":
    main()
