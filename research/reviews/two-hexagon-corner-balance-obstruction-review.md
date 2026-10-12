# Independent review of corner-balance obstruction

**Verdict: valid within the stated SFT reduction.** Reviewed by the root agent,
which did not develop the result, on 2026-10-12.

The claim is that infeasibility of positive two-species corner balance excludes
aperiodicity of any actual convex-hexagon pair with the given allowed triples.
A rational potential with nonnegative sum on every allowed triple and negative
sum over each species proves the entire SFT empty for every side equivalence.

The reviewer checked the translation-average invariant-measure argument. There
are two star orbits per honeycomb cell; stationarity counts each of the six
native corners once per cell even when placement symbols include reflections.
Thus the species probabilities multiply all six corresponding native corner
coordinates equally. A zero species probability gives a monohedral point by
a countable union over lattice sites. No assertion about the original tiling's
species densities or translational symmetry is used. Actual polygons are
needed for the imported monohedral escape and geometric reduction.

Independently, Sage rational matrices and their right kernels checked the
five generating triples in the retained example. The rank modulo polygon
sums is five, and its closure consists of exactly the six stored triples,
covering all twelve corners. The first potential has species sums (-1,0)
and no pure-B star is allowed, giving emptiness. The stronger potential
(0,0,0,-2,-1,2,0,0,0,0,-1,0) has species sums (-1,-1) and nonnegative
sum on all six triples, proving emptiness directly.

Minimal covering was checked combinatorially: native corners 0,1,2,3,4 each
occur in exactly one respective generating triple. Any covering subset must
contain all five independent generators and has the same closure. This is
an explicit rank-five covering root with no proper covering ancestor. It
substantiates the existing warning against continuing enumeration from only
covering low-rank parents.

The stronger potential's nonnegative region contains 195 of the 364 triples.
Every subset of that region has empty SFT; adding a negative-potential triple
can restore balance, so obstructed parents cannot be pruned from enumeration.
This is a sound analytic empty-supertype certificate, not a census of all
rank-four-through-ten types or a construction.

Dependencies: [lemma](../lemmas/two-hexagon-corner-balance-obstruction.md),
[exact example](../certificates/two-hexagon-corner-balance-obstruction-example.json),
[verifier](verify_two_hexagon_corner_balance.py). Remaining trust for the
rank computation: exact Sage/SymPy rational linear algebra. The potential
inequalities themselves require only integer arithmetic.

The reviewer separately checked the explicit finite-patch argument. A
hex-radius-R ball has N=1+3R(R+1) tiles and 6R^2 complete star triangles,
leaving 18R+6 corner incidences. Each tile contributes -1, each complete
star contributes at least zero, and each leftover incidence contributes at
least -2. Thus N<=2(18R+6), contradicted at R=12 (469>444). This justifies
an analytic radius-12 empty record, without invariant measures or solver
infeasibility trust. Counts were independently enumerated at R=1,2,3,12.
