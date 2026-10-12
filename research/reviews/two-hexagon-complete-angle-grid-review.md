# Independent hostile review of the complete angle grid

**Verdict: VALID**, 2026-10-12, root reviewer independent of the proof author.

The reviewer checked every step of the uniform argument: centering at120,
primitive normalization only of triple-repeat rows, projection off the two
species rows, and Hadamard bounds on every restricted-column minor. Full-row
projection remains a valid row operation after restriction; no orthogonality
of restricted rows is needed. Primitive mixed2+1 rows attain squared projected
norm25/6; pure triple-repeat rows become unit rows. Cramer replacement-column
vectors span the rational kernel with every coordinate bounded by the same
minor bound. Saturation of the integer lattice is unnecessary.

Fixing one nonzero basis coefficient to1 preserves a proper affine equation
for every excluded triple. The balanced interval has H+1 integers, while at
most H last-variable roots are forbidden at each greedy step. This proves
uniform exact avoidance, including kernel dimension1. Rank10 is separately
the all120 point with all364 triples. H<=364-k follows from choosing k
independent triple rows already in T.

The reviewer independently recomputed all ten determinant bounds using
integer inequalities D^2*6^k<=36*25^k<(D+1)^2*6^k, then every deviation
bound and sufficient grid. The maximum is323632, strictly below60*5394.
The example's12 numerators satisfy both species sums and all364 exact triple
membership tests. No floating-point decisions or SAT/LP verdicts were used.

Consequently every exact closed angle type has a representative on denominator
5394, while the SFT side relation may be preserved formally. This asserts
completeness of the angle-type relaxation, not geometric realization of that
representative or finite-model sufficiency for plane tiling. UNKNOWN query
results remain inconclusive. The constants are sufficient bounds, not optimal.

[Proof](../lemmas/two-hexagon-complete-angle-grid.md),
[certificate](../certificates/two-hexagon-complete-angle-grid.json),
[constructive checker](verify_two_hexagon_complete_angle_grid.py).
