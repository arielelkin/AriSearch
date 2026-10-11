# Exact comparison of local angle coverage with frequency balance

Question: for two hexagon angle multisets, can every corner be angle-eligible
while nonnegative whole-tile frequency balance fails?

Domain: every sorted six-element multiset from
{100,110,120,130,140,150,160,170} degrees with sum720:46 multisets. Every
unordered pair with repetition is tested:1081 pairs. Sorting discards cyclic
order only for this angle-only test; no claim about geometric equivalence
of polygons is made. Available stars are all three-element multisets on
combined-present angles summing360. There are seven in the full angle domain.
No higher-valent stars or partial contacts can occur for genuine convex
polygons with these strictly obtuse corners; the proof separately establishes
this fact. Angles170 fail local coverage in the full domain.

Encoding: multiplicities of each numerical angle. Variables fA,fB>=0 with
fA+fB=1; one x_t>=0 per available star. For each angle v impose

    sum_t mult_t(v) x_t = mult_A(v) fA + mult_B(v) fB.

The normalization is permissible for this homogeneous necessary count system;
it is not an area normalization for the concrete polygons. A type can vanish.
No tileability, polygon closure, endpoint matching, lattice, placement, scale
or chirality assumption is encoded by this angle-only system.

Z3 exact linear rational arithmetic decides the systems. For each feasible
system retain an exact rational primal solution. For each infeasible system
find a rational functional nonnegative on all star vectors and at most-1
on both tile vectors; retain it as an independently checkable Farkas
certificate. Every decision has a finite rational certificate, so no trust
in the solver is needed to check the classification. No random seed,
search timeout, symmetry reduction beyond unordered angle multisets,
floating arithmetic or period bound is used.

Complete run2026-10-10:1081 pairs,692 angle-covered,681 frequency-feasible,
11 frequency-infeasible. The concrete counterexample is realized as two
circumscribed algebraic convex hexagons in Q(zeta36), with exact support
tests and angle checks. Its infinite untileability follows from the
separate weighted boundary proof, not extrapolation from the search.

Software: Python3.12.13, Sage10.9, Z3 4.16.0. Run from repository root:

    conda run --no-capture-output -n arisearch python research/searches/angle-frequency-cover-counterexample.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_angle_frequency_cover_independent.py

Normal runs do not write. The retained file was saved explicitly with:

    conda run --no-capture-output -n arisearch python research/searches/angle-frequency-cover-counterexample.py --output research/certificates/angle-frequency-cover-counterexample.json

The independent verifier uses rational arithmetic for every classification
certificate and exact cyclotomic/real-algebraic arithmetic for both polygons;
it does not import the producer or use Z3. Producer replay need not reproduce
a solver's choice among many equivalent primal/dual witnesses; verification
checks the actual retained witnesses rather than comparing their text.

Scope: exact finite angle-only classification and concrete unrestricted
untileability family, not a complete two-hexagon classification or resolution.
The underlying frequency-balance method is elementary and no novelty is claimed.
