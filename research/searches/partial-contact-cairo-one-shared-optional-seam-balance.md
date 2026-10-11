# Optional native subdivision and two-ended seam calculation

Status: complete exact-certificate generation, independent model audit pending.

Question: do the sixteen reviewed sole-Pa=Qd relative-open Cairo families have
any necessary corner/seam balance after retaining all possible native whole/T
occurrences? The model is defined in
[the candidate scoped theorem](../lemmas/partial-contact-cairo-sole-adjacent-shared-arm-obstruction.md).

Finite domain: all16 retained dimension2 survivor strata, all102 exact open
native-arm-order chambers, all complete five-side optional partitions, both
reflected orientations of every merged native/refined corner state, all
cyclic three-/four-sector stars and all their two-ended seam features.
No physical rotation restrictions, geometric cutoff or plane patch boundary
are imposed. Every whole native side is an option. Residual pieces without a
120 endpoint ignore length, a safe additional relaxation whose necessity
must be checked in the fresh audit. Counts of variants per chamber range10–28;
corner states25–40; permitted cyclic stars49–161; seam types27–50.

Outcome: all102 models have independently evaluable rational dual proposals.
The producer checks every retained dual inequality by exact Fraction
arithmetic after numeric optimization. Numeric solver status alone is never
used to certify obstruction. Fresh independent checker and boundary/model
proof are pending; no untileability conclusion is promoted at this stage.

Software: Python3.12.13, Sage10.9,
SciPy1.18.0, NumPy2.5.2, Z34.16.0.
No randomness or imposed solver time limit. SciPy/HiGHS proposes coefficients;
Python Fraction verifies the resulting finite inequalities exactly.

Read-only full replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-one-shared-optional-seam-balance.py

A specified case may use --flat381 --chamber0 (with spaces between option and
value). Only --output explicitly writes a certificate. Retained certificate:
[all102 duals](../certificates/partial-contact-cairo-one-shared-optional-seam-balance.json).
The input is the independently reviewed complete event-flat certificate;
no data are retained only in a temporary directory. Result does not prove
existence of a tiling, classify other shared-arm orbits, or resolve the
original two-convex-tile problem.
