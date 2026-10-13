# Independent hostile review: resumed source compiler

Date: 2026-10-13. Verdict: **VALID** on the specified compiler domain.
Reviewer did not develop the construction or its exclusion.

Reviewed [source artifact](../searches/resumed-source-compiler.md) and
[exact witness check](../searches/resumed-source-fan-check.py).

## Claims and assumptions checked

The finite domain is the eight three-letter words over{C,O}, with every
triangle glued consecutively around its distinguished apex along unit
radial sides. Since each triangle is isosceles, reflections do not create a
new radial-angle or length case. These are literal consecutive fans, not
all clusters of golden triangles. Summed apex angles are108,180,252,324;
only108 is strictly convex. At180 the apex is redundant, giving four
genuine outer corners; at252 and324 it is reflex. No marked Penrose rule,
source-star occurrence, or global source tiling is used in this exclusion.

The CCC coordinates have all unit radii and three bases phi-1. Their
positive oriented cross products establish strict convexity, and the
claimed angle word follows from the consecutive36-degree ray gaps.
The half-turn mate about(1/2,0) lies below the seam, while P lies above;
there is no interior overlap. Supplementary endpoint corners flatten the
seam endpoints. The six remaining corners form the given genuine strictly
convex centrally symmetric hexagon. The centrally symmetric convex
hexagon translation-tiling theorem applies; the provided exact opposite
edge translations and determinant/area equality also agree with its
standard parallelohexagon lattice. Thus the omission-allowed original
problem admits a periodic P-only tiling whenever P is in the target pair.

The literal-source inheritance theorem has the correct quantifiers:
EVERY source representative must have one finite dissection into target
copies for its periodic source tiling to transfer. The motif is finite and
all its transported subdivisions repeat by the period lattice. Boundary
subdivision mismatches are permitted by unrestricted contacts, reflections
are permitted in transported motif isometries, and target omission is
permitted. The rhomb corollary needs a dissection of only one rhomb because
that single rhomb has its own parallelogram periodic tiling. Existence of a
marked nonperiodic source does not invalidate the plain periodic rhomb
witness. Cross-boundary recompositions and incomplete target fragments at
parent boundaries lie outside the theorem.

## Replay and attempted defects

Executed exactly:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed-source-fan-check.py

Exit0, with PASS for strict pentagon, half-turn hexagon, edge-pair lattice
and exact area equality. Computation uses exact real algebraic arithmetic,
not tolerances. The check is a single witness; no enumeration-completeness
claim is attached. The eight-word exhaustion is analytic in the artifact.

Attacks on the diagonal triangle conventions, reflected fan cases,
suppressed180-degree apex, hexagon orientation, period-rank assertion,
source dissection quantifiers, and mixed subdivision endpoints found no
unresolved defect. No repair made. No claim about arbitrary two-convex-tile
pairs or the existence of a Penrose compiler outside this domain is endorsed.
