# Fixed asymmetric pentagon/regular-dodecagon periodic witness

**Completion:** all exact constraints and the complete overlap domain passed.
The certificate is retained. The [fresh independent checker](../reviews/verify_regular_dodecagon_independent.py)
has passed, and the [full hostile review](../reviews/all-obtuse-pentagon-regular-dodecagon-review.md)
is valid.

## Mathematical question and finite domain

Does the seven-motif construction in the
[classification lemma](../lemmas/all-obtuse-pentagon-regular-dodecagon-classification.md)
form a whole-plane periodic tiling for the fixed exact parameters

    ell=2,   sin(p)=1/8,   cos(p)=sqrt(63)/8,   0<p<pi/12?

The domain is one fixed algebraic witness. It is not a parameter search or
bounded periodic search. There are seven fixed polygons: one regular unit
Q12 and six isometric copies of the same asymmetric P. For all 7*7 ordered
motif pairs, exact lattice-coordinate bounding boxes determine the complete
integer translation range that can intersect. The bounds are
ceil(min_i-max_j) and floor(max_i-min_j) on each coordinate. Only the
identical copy (i=j,shift=0) is omitted. The resulting 62 nontrivial ordered
comparisons exhaust every possible intersection; any excluded shift has
disjoint one-dimensional projections.

## Object encoding and constraints

The producer uses Sage AA/QQbar exact algebraic arithmetic. Put
z=QQbar.zeta(24), omega=z^8, rho=sqrt(63)/8-i/8, ell=2. The five P vertices
are

    0, ell, ell+z^5*rho, ell*omega-z^15*rho, ell*omega.

The Q center is q0=ell+rho/(2sin(pi/12)); its twelve vertices are centered
there with radius1/(2sin(pi/12)), starting at P_vertex2 and advancing by
30 degrees. The remaining P motifs are omega^j P and
(1+omega)q0-omega^j P, j=0,1,2. Periods are
(omega-1)q0 and (omega^2-1)q0. These are unrestricted permitted
isometries, with no markings or additional contact rules.

The exact constraints are strict positive side-support inequalities for
all seven polygons, unit sides and150-degree native angles for Q, P side
lengths (2,1,t,1,2) with t>0, one120-degree P angle, four P angles strictly
between90 and120 degrees, unequal complementary angle pairs, a positive
period determinant, zero intersection area in all 62 complete comparisons,
and total motif area equal to the lattice covolume. It also checks the
explicit P area identity used in the analytic construction.

No symmetry quotient, solver, random seed, floating-point branch, timeout,
or resource cutoff is used. Algebraic values are retained as exact rational
strings or as minimal polynomials with rational isolating intervals. A RIF
approximation is used only to propose exact binary rational interval
endpoints; exact AA root counting subsequently confirms that each interval
contains precisely one root. The decision procedures for convexity,
angles, intersections, bounds, and equality are exact.

The producer clips convex polygons exactly. Together with the area equality,
this proves the specific infinite family covers the plane: it has disjoint
interiors, its periodic union is locally finite and closed, and a missing
point would give an open disk of missing positive fundamental-domain area.
The continuous-family lemma has a separate abstract local-gluing/degree-one
proof; its entire parameter range is not inferred from this fixed fixture.

## Artifacts and replay

Producer: [obtuse_pentagon_regular_dodecagon_witness.py](obtuse_pentagon_regular_dodecagon_witness.py).
Certificate: [obtuse-pentagon-regular-dodecagon-witness.json](../certificates/obtuse-pentagon-regular-dodecagon-witness.json).

The run used Python 3.12.13 and SageMath 10.9 in the arisearch Conda
environment. No other package is required beyond the standard library.
Run without Python optimization, because assertions are proof relevant.

```text
conda run --no-capture-output -n arisearch python research/searches/obtuse_pentagon_regular_dodecagon_witness.py
```

Its stdout is the exact JSON certificate. The recorded completion was
normal, with seven strictly convex motifs, unequal small P angle pairs,
62 exhaustive comparisons passing, and area equal to the positive lattice
determinant. The fresh checker reconstructs this fixture and its complete domain
independently, using separating axes rather than the producer clipping code.
It also checks the universal symbolic side, corner-cycle, and area claims.

## Scope and restart

This is a retained positive periodic escape for one asymmetric exact member
of the classification family. It disproves a claim that only the symmetric
four-105-degree pentagon can tile with a regular unit dodecagon. It neither
shows strong aperiodicity nor tests other candidate n>=13 families. The
whole-plane construction has no bounded extension obligation. Both this fixture and the analytic parameter/flat-torus construction
proof have passed fresh independent audit. Replay the independent checker:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_regular_dodecagon_independent.py
```
 The [narrow primary-source audit](../literature/regular-dodecagon-pentagon-source-audit.md)
found a close 2025 construction whose exact metric match is unresolved.
No novelty is claimed.
