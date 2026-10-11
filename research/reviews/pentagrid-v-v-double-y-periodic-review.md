# Independent hostile review of the mirror-V double-Y continuum

**Verdict: VALID for the complete stated real parameter domain.** No geometric
repair was needed. The proof and formal sign checks in fact extend to every
a>0,k>0; the restriction0<k<a/phi only preserves positivity of the old
auxiliary mirror-V parameter for B. This extension is not a classification
of arbitrary V/V metrics and is not a solution of the main problem.

The reviewer did not develop the [original construction](../lemmas/pentagrid-v-v-double-y-periodic.md).
The [independent verifier](verify_pentagrid_v_v_double_y_independent.py)
imports no author code and reconstructs both shapes from native edge walks,
then derives the macro corners from exposed child vertices. It compares
complete formal coordinate vectors with the author's certificate and uses
exact polygon clipping instead of the author's separating-axis method.

## Assumptions, cone and native geometry

Every native A and B side is strictly positive for a,k>0. In the original
parameter domain0<k<a/phi, both auxiliary pairs defining mirror-V are
positive, as claimed. Their physical side positivity does not require this
extra inequality. Exact normalized support polynomials were independently
reconstructed for all edges against all nonincident vertices of A,B,C.
All54 are nonzero and have nonnegative coefficients in a,k over Q(phi).
Thus the entire positive cone has global strict convexity; no numerical
orientation or local-turn-only inference is used.

The native after-side angle word is(2,2,4,3,4)*pi/5 and the native vertex
word is(4,2,2,4,3)*pi/5. The half-turn copies preserve these indices. The
unique72-to72 edge has length r=2phi*a+k in A and e=phi*a+k/phi in B;
r-e>0, so the shapes are distinct even with unrestricted isometries.

The individual monohedral exclusion is correctly confined to the separately
reviewed Rao-filter dependency. Neither that dependency nor its completeness
is needed for this periodic tiling. The new all-a,k-positive extension can
include individually tileable B at k=a, so the original individual exclusion
must retain its original domain or an explicit k!=a qualification.

## Dissection and actual macro lattice

All120 child-vertex macro half-plane polynomials have nonnegative
coefficients. All six whole-child separation lines have the claimed signs
for every positive a,k. These establish global containment and pairwise
interior disjointness, rather than only seam consistency. All five whole
internal seams have reversed endpoints, and the six outer chains account
for each of20 native sides exactly once. Independent native shoelace
calculation confirms the corrected area formulas and total macro area.
The finite closed union argument then proves exact coverage of C.

The three macro edge pairings have exact reversed endpoints under shifts
-v,u-v,u. Their actual ordered corner links are(0,4,2) and(1,5,3), each
summing to360 degrees with zero lattice-shift holonomy. The resulting
connected oriented compact quotient has Euler characteristic0. Strict
convexity puts opposite seam neighborhoods on opposite sides, and the
actual ordered links give one full disk at each vertex. Thus its map to
the ordinary lattice torus is a local Euclidean isometry everywhere.
Compactness gives a finite covering; the exact area(C)=cross(u,v)>0
forces degree1. This justifies the actual infinite lattice tiling, including
absence of any global overlap or uncovered region.

The partial boundary division distances are exactly a and r, and r>a.
The author's description correctly avoids forcing D-to-D dimers throughout
the plane. The child partial contacts lie on shared macro boundaries and
are admitted by the original unrestricted contact convention.

## Independent coordinate and overlap certificate

For a=1,k=phi^-2 the checker independently reconstructs all four children,
the macro, the periods and the positive areas in QQbar/AA. Every saved real
and imaginary coordinate is decoded from its rational defining polynomial
and rational isolating interval. Each interval isolates one real root, and
all reconstructed values match the author's certificate.

The inverse lattice coordinate map supplies complete vertex-extremum boxes
for every convex motif. Any intersection of motif i with motif j+(n,m)
requires the integer translation to lie in the exact two-coordinate box
obtained by subtracting their extrema. Recomputing these boxes gives44
nontrivial ordered comparisons. Exact Sutherland-Hodgman clipping gives
intersection area0 for every comparison. The complete domain matches the
author list. This finite domain validates the fixed infinite fixture;
it is not a bounded search for a period and does not establish arbitrary
V/V periodicity.

The verifier completed successfully with SageMath10.9 and Python3.12.13:

    conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_v_v_double_y_independent.py

The retained [review certificate](../certificates/pentagrid-v-v-double-y-review.json)
contains formal tests, seams, links and all44 clipping comparisons. Normal
invocation prints without writing; explicit --output is required to save.
During checker development one unused guessed endpoint assertion was removed
before the first run. This did not change any source claim or geometric
formula. No author defect remains.

## Broader mechanism and remaining uncertainty

The fresh review exposed that mirror symmetry is not required for the
five-seam double-Y combinatorics. The reviewer developed a separate
[four-parameter general theorem](../lemmas/pentagrid-v-v-general-double-y-partners.md)
with asymmetric V children and an elementary boundary-winding coverage
proof. That new theorem is not promoted by this review of the old theorem;
it requires a fresh reviewer who did not develop its algebra or proof.

The original continuum and fixture are certified. The entire unrestricted
problem remains unresolved. This review neither claims novelty nor asserts
that every pairing of V shapes has a periodic tiling.
