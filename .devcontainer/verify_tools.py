"""Fail fast when the development container and research protocol diverge."""

from __future__ import annotations

import shutil

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
