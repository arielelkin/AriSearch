# Independent coordinates for the reciprocal partial-contact V/V construction

**Computational verdict: PASS.** Root reconstructed the motifs from exact
native lengths and direction words, without importing author code, in
[the checker](verify_reciprocal_v_partial_periodic_independent.py).
Root suggested the periodic boundary-jump coverage argument to the author;
therefore this coordinate audit is not counted as the fresh independent
whole-proof review. The [separate non-author review](pentagrid-v-v-reciprocal-partial-periodic-review.md) is now complete and VALID for the full cone.

Formal polynomial arithmetic over Q(zeta10)[a,k] proves native closure and

    det(U,V)/sin36=phi^2*(a^2+4*a*k+k^2)=sum motif areas/sin36.

The coefficient expression is strictly positive for every a,k>0. Six new
exact coordinate fixtures check supporting half-planes, each exact native
angle cosine, determinant/area equality and every possible ordered motif
intersection with an integer lattice translate. The exact finite domain
comes from inverse-lattice vertex extrema, independently of the author's
contact table or fixture boxes. Exact convex clipping gives zero area for
all292 intersections, including self-translates.

| Ratio k/a | Stratum | Complete comparisons |
| --- | --- | ---: |
| phi^-4 | lower open |34|
| phi^-3 | lower coalescence |40|
|3/2| middle open |44|
| phi^3 | upper coalescence |68|
| phi^4 | upper open |62|
|1| congruent interior |44|

The ratio1 case intentionally checks geometry where the two prototile
classes coincide; it is outside the noncongruent-pair conclusion. Boundary
cases are exact algebraic values, not close floating approximations.

    conda run --no-capture-output -n arisearch python research/reviews/verify_reciprocal_v_partial_periodic_independent.py

Replay passed on2026-10-10 in Python3.12.13/SageMath10.9, with no solver,
seed, timeout or artifacts written. The checker reuses only root's exact
AA coordinate/cross/clipping utilities from the independently reviewed Q3
checker; it imports no candidate producer. Those explicit dependencies
are retained in the focused checkpoint.

These finite checks do not establish the full-cone plane theorem by
extrapolation. Its general proof requires the two exact oriented interval
coverings, all parameter strata and the periodic multiplicity argument.
The source includes that proof; its full positive domain, distinctness,
reflections and arbitrary-pair quantifier boundaries have now passed the
separate independent whole-proof review. That reviewer also extended this
checker with full-cone support/angle identities, every full seam and directed
interval occurrence, all five segment-sign cases, individual areas and the
monohedral gate differences.
