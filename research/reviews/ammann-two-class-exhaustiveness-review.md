# Hostile audit of the recorded Ammann two-class collapse

Date: 2026-10-12. Independent reviewer, not the producer of the searches.

## Claims and scope

The review distinguishes two claims that the existing search record combines:

1. For the explicit two-real-parameter polygons H6, P1 and P2 in
   `research/lemmas/ammann-two-class-reconstruction.md`, no convex two-class
   specialization can be aperiodic. Parameters with an actual triangle or
   quadrilateral are discarded by their periodic monohedral tilings.
2. The generalized 98-by-98 marked-rhomb graph search exhausts its declared
   strictly-interior, at-most-two-point decoration domain and has no further
   convex two-class specialization with at least five actual corners per
   shape.

Neither claim concerns all pairs of convex polygons. No points on source
edges, extra points, neighbour-dependent decorations or changed substrates
were searched or authorized by this audit.

## Independent exact check of claim 1

Verifier: `research/reviews/verify_ammann_two_class_distance_audit.py`.
Retained output: `research/reviews/ammann-two-class-distance-audit.json`.

The verifier reconstructs the coordinates directly. It does not import the
producer or use its proportional-edge equations, gcd roots, or certificate.
For each correspondence it equates every pairwise squared distance:

    |P_i-P_j|^2 = |Q_(k+d i)-Q_(k+d j)|^2,
    0 <= i < j < 5, k in {0,...,4}, d in {+1,-1}.

It checks P1 against P2 and, separately, H6 with each one of its six
vertices removed against each pentagon. In the latter cases the original
deleted corner's straightness equation is imposed before solving. This is
13 polygon pairs and 130 complete polynomial systems over Q(zeta_10)[s,t].
All 130 ideals are empty or zero-dimensional; every real root is computed
exactly. Global convexity is checked by putting every vertex on the left
of every oriented boundary edge, requiring nonzero edges and positive area.
This is stronger than checking only successive nonnegative turns and does
not silently admit a multiply-wound star polygon.

**Observed exact result:** exactly one correspondence has all three
polygons globally convex: P1/P2 at

    s = t = (5+sqrt(5))/10.

The check imposes fewer admissibility inequalities than the original
piece-based filter. Consequently it excludes omitted piece-admissibility
cases as well: every admissible parameter lies in the checked convex superset.
The surviving point is strictly convex and has already passed the separate
independent root/central-symmetry check in
`verify_ammann_two_class_collapse_point_root.sage`.

### Why the case list suffices for candidate exclusion

For a nonempty compact convex polygon, deleting boundary subdivisions at
straight angles gives its intrinsic corner count. An isometry preserves
this count. If P1 or P2 loses a corner, its count is at most four and it
tiles periodically by itself. If H6 loses at least two corners, the same
escape applies. Otherwise both pentagons have five corners and H6 has six
or five. With six H6 corners, a reduction from three to at most two classes
requires P1 congruent to P2. With five H6 corners, at least one of the three
pairwise congruences must hold. The P1/P2 case plus all six possible H6
deletions therefore covers every remaining candidate, including mirrors.
At the sole surviving point H6 is centrally symmetric; a centrally
symmetric convex hexagon tiles by translations. The protoset admits this
monohedral periodic escape because using both shapes is not required.

**Verdict for claim 1: VALID**, as a restricted candidate exclusion.
Trust remaining: Sage's exact algebraic arithmetic and Singular ideal/root
computations; this is not a formal proof-assistant certificate.

## Defect in the stronger boundary classification wording

The statement "the set has at most two congruence classes only at the
circumcentre point in the closed admissible region" also purports to
classify strata with intrinsic corner count at most four. Neither the
producer nor the independent 130-system check solves those strata.
Their periodic escape establishes failure as aperiodic candidates, not
absence of other congruence collapses. No counterexample on those strata
was asserted or found here. The proof of that stronger literal uniqueness
statement is **UNRESOLVED**. A precise supported formulation is:

> Apart from strata containing a triangle or quadrilateral prototile,
> the circumcentre point is the only convex two-class specialization of
> the reconstructed two-parameter Ammann polygons; it too admits a
> periodic monohedral tiling.

This wording repair does not weaken the candidate exclusion used above.

## Generalized search: checked stored points and algorithmic audit

Verifier: `research/reviews/verify_ammann_generalized_recorded_points.py`.
Output: `research/reviews/ammann-generalized-recorded-point-audit.json`.

It reconstructs all **38 retained real-point rows** in the stage-4 summary
from their defining polynomials. The printed approximations select a
unique exact real root within a rational radius 10^-10; no floating-point
value decides geometry. It rebuilds all recorded class vertex forms,
checks global supporting-line convexity, removes actual straight corners,
and counts classes by full squared-distance matrices under all cyclic
orders and both directions. Every stored class count and convexity verdict
agrees. The eight positive rows represent exactly two distinct parameter
points, one for (4,27) and one for (2,15). Each has a centrally symmetric
convex hexagon. Thus **all recorded candidates are independently killed**.

The following enumeration issues were also inspected:

* The mask domain contains every listed allowed edge. The skipped two
  crossing unsplit diagonals cannot be a straight-line plane embedding;
  their subdivided intersection is expressible by four spokes to P.
* For an actually embedded graph, corner-neighbour linear orders and
  interior-node cyclic orders cover its rotation system. The genus-zero,
  fixed-outer-face and simple-piece tests are necessary; unrealizable
  systems may be retained, giving a safe superset. P/Q exchange preserves
  the allowed parameter space.
* Generic class splitting causes extra necessary congruences rather than
  omitting a genuine two-class point. Exact identifications by a fixed
  root-of-unity rotation and translation are sound.
* Every convex polygon with at least five intrinsic corners supplies one
  of the enumerated deletion sets. Deleted adjacent straight vertices are
  still straight in the original list. Nonzero surviving edge norms
  justify saturation. Both chirality options are present.
* Fixing the smallest class in each partition block as representative is
  sound: at an actual common collapse point it is congruent to every
  member, with one fixed actual corner/deletion list. Sharing parameters
  and multiplying norm factors in the joint saturation are necessary.
  Every unlabeled partition into at most two blocks occurs in the mask
  enumeration.

These observations establish the logical coverage of the stated loops
**conditional on the correctness/completeness of the generated negative
cases and ideal computations**. They do not independently rerun those
loops.

### Remaining generalized exhaustiveness gates

1. The summary retains aggregate counts, not individual negative
   combinatorial components for the rejected 9,591 pairs. An independent
   checker has not rebuilt those witnesses in this audit. The recorded
   stage-3 list similarly retains nonempty options, not certificates for
   all discarded unit ideals. Checking the 38 stored points cannot prove
   that omitted options or omitted roots do not exist.
2. The producer decides the sign at an identically collinear corner by
   two floating-point samples. The sign is theoretically constant wherever
   the edge is nonzero, but it needs an exact computation, not sampling.
   See the exact replacement below. No erroneous sign was exhibited here.
3. Slit rejection assumes that every retained graph edge is an actual
   final tile boundary and that each open face must itself be a polygon
   interior. A slit is an obstruction under that convention. If the
   intended output is instead the closure of an open face after filling
   redundant internal slit segments, a slit alone need not make its
   closure nonconvex. The domain must make this convention explicit;
   silently using the broader closure interpretation is unsupported.
4. Finite patch interior faces are sufficient *negative* witnesses only
   for the intended marked Penrose language in which the witness patches
   occur. This does not certify arbitrary bare-rhomb tilings or global
   existence from finite class counts. The recorded exclusion uses the
   marked source, not those broader domains.

**Verdict for claim 2: UNRESOLVED as an independent exhaustiveness
certificate.** The retained metric points and their periodic escapes are
valid. No new viable mechanism or candidate was found. The prescribed
closed domain should remain closed to enlargement; the next work here is
verification of its existing cases, not a larger search.

## Exact replacement for the numeric collinearity sign

Let A and B be nonzero complex-affine edge forms in free complex parameters,
and suppose Im(conj(A) B) vanishes identically. On the open set A != 0,
B/A is holomorphic and real-valued, hence constant. Thus B = lambda A
for a real constant lambda. Choose a nonzero coefficient a_j of A and set
lambda=b_j/a_j in Q(zeta_10). Verify coefficientwise that B=lambda A
and lambda=conj(lambda); determine the sign in the chosen real algebraic
embedding. A positive lambda is identically straight; a negative lambda
is identically backward. A zero lambda means the second edge vanishes
identically. This argument also covers parameter-free A and B. It is
enough to replace the sampled sign test without any domain enlargement.
It has not been applied to all 9,604 pair executions in this audit.

## Replay and current artifact status

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_ammann_two_class_distance_audit.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_ammann_generalized_recorded_points.py

Both commands passed on 2026-10-12. MISE_AUTO_INSTALL=0 only prevents
installation of unrelated globally configured tools; the commands still
run in the repository's locked Conda research environment. No producer,
retained original certificate, discovery log or environment file was changed.
