# Three-sector fractional surgery: a positive topology and its exact area gate

Date: 2026-10-15. Status: internally proved restricted topology bounds and
exact local fixture; later review/superseding status is stated below. This is construction
progress and a scoped obstruction, not an aperiodic pair or main solution.

**Later status:** the precursor was read in the [independent cap-gate audit](../reviews/thick-cap-split-congruence-hostile-2026-10-15.md),
and its finite fixture has an independent exact checker. More importantly,
the entire receiving-H component with mark-local donor triangles is now
[excluded even with arbitrary cuts/splits](../lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md).
No positive construction or further congruence task is pending here.
The original internally proved topology bounds are retained as author results,
not promoted beyond the scope of those reviews.

## The changed hypothesis, specified before coordinates

The old split-edge template gave exactly two final sectors at the marked
source-edge point M, with a common bent interface t-M-R. Their turns were
C and -C. Replace that common interface by THREE rays M-t, M-p, M-q,
where t is the external donor apex and p,q are the adjacent internal donor
nodes of the receiving rhomb. For receiving edge U-V in its boundary order,
partition its internal quad (U,V,q,p) into triangles (U,M,p), (M,V,q),
and (M,q,p). Divide the external donor triangle (U,V,t) into (U,M,t)
and (M,V,t). The five fractional source sectors assemble to THREE outputs:

    L=(U,t,M,p), R=(M,t,V,q), C=(M,q,p).

Their angles at M total 2pi, with three genuine sectors, and no two-sector
complementary-turn constraint remains. All fractional pieces are assigned
once. Each source rhomb has two receivers and hence owns four quads and
two triangles. An output is owned by the rhomb containing its receiving
sector, even though its donor fraction crosses a source boundary.

At each donor apex p, the resulting graph has six incident rays, to:
its donor-edge endpoints U,V; its own donor-edge split point M_d; the two
neighboring receiving-edge split points; and the opposite donor node q.
Replace EVERY such degree-six vertex by its convex hexagonal truncation
cap. Cut each ray at a common small distance epsilon from p and join these
six cut points cyclically. This is a complete incidence specification:
there is one new cap at each donor node, and existing incident outputs
retain their corner-cut remainders. Each original quad contains two donor
nodes and becomes a hexagon; each central triangle contains two donor
nodes and becomes a pentagon; each cap is a hexagon. Thus the final counts
per source rhomb are SIX hexagons and TWO pentagons. Every output has at
least five genuine corners. The three sectors at every M are retained.

This is a different graph from both the closed directed-offset pentagon
scheme and the failed two-output split-edge scheme.

## Vertex-density obstruction before truncation

More generally, retain the original source vertices, two internal donor
nodes per rhomb, and one split point per source edge, with no additional
final graph vertices. Suppose exactly three bounded outputs are owned by
each receiver, two receivers per source rhomb. In a large disk containing
N source rhombs, the source rhomb graph has N+O(sqrt(N)) vertices and
2N+O(sqrt(N)) edges; bounded geometry gives the boundary estimate.
Consequently final V<=5N+O(sqrt(N)), F=6N+O(sqrt(N)). Planar Euler gives
E=V+F+O(sqrt(N)), so the total number of face boundary corners is at most
2E<=22N+O(sqrt(N)). It cannot be at least 30N, as required for all outputs
to have five corners. In fact all outputs cannot even have four corners.
At fixed output density six, at least FOUR additional genuine final
vertices per source rhomb are necessary for all outputs to have five
corners. Inserting a bend on a two-face boundary does not supply such a
vertex in a convex tiling: it is straight or gives one face a reflex angle.

The untruncated explicit topology saturates the bound: four quads plus two
triangles have 22 corner incidences. Truncating the two degree-six vertices
adds ten vertices, twelve edges, and two faces per source rhomb. The new
counts V=15,E=23,F=8 give 46 incidences, exactly 6*6+2*5.

## Positive exact geometric fixture

Use the unit thin and thick Ammann source rhombs, with their native arrows
and opposite donor choices as in the cited prior split-edge artifact.
Set each mark position to its edge midpoint and every donor apex height
to h=1/100 into its donor rhomb. Receiving external apexes are at height h
outward. Set epsilon=1/100000 for all donor-node cuts.

The independent checker reconstructs both algebraic rhomb angles and both
donor parities. It checks all supporting-line inequalities for the 24 local
precursor pieces (three outputs times two receivers times four cases), all
source-local precursor area balances, all corner-cut separation inequalities,
and the six cyclic rays at each of the eight donor nodes. Every consecutive
ray gap is strictly smaller than pi. Equal-radius cut points are cyclic,
so their hexagonal cap is strictly convex and contains the original node.
Cutting each corner by a chord preserves strict convexity; the checked
edge-length bounds keep adjacent cuts disjoint. Thus this is a valid
plane partition when applied to the known infinite source. No two-class
or universal shape-forcing conclusion follows.

The fixture avoids unnecessary giant algebraic composita: strict convexity
of each precursor and the cap-ray gaps are checked exactly, and geometric
corner clipping proves convexity of the final pieces. The first experiment
that directly constructed every nested-radical cut coordinate was manually
interrupted during exact algebraic-field comparison; it supplied no proof
result. The retained checker uses only smaller exact computations and the
stated clipping argument.

## Receiving-class identities: a broad area obstruction

There is an immediate gate for TWO final congruence classes. Pentagons and
hexagons are not congruent, so all pentagons must have one area P and all
hexagons the other area H. It is necessary to account for transfers across
source boundaries rather than summing whole outputs inside one source.

For edge mark Z, let T_Z be the donor triangle area and D_Z the area of
the two cap sectors adjacent to the rays p-U,p-M,p-V. Exactly these two
sectors belonged to the outputs owned by the neighboring receiving rhomb;
the other four cap sectors belonged to the donor rhomb's outputs. Thus the
net transferred area after truncation is tau_Z=T_Z-D_Z. It depends only
on the physical donor-edge rule when apex offsets/heights and cut distances
on these three rays depend only on mark Z and actual source arrow.
It is independent of the receiving rhomb's other donor nodes.

Assign each cap to the rhomb containing its donor apex. Sum its two caps
and six truncated receiving outputs. By dissection, the sum equals

    source area + sum(received tau_Z) - sum(donated tau_Z).

Every one of the four source-type/role cases has one X and one Y donor,
and one X and one Y receiver. The transfers cancel, even with different
X/Y offsets, heights, and cut radii, provided all sectors remain valid and
the external cap slice is mark-local as just stated. Therefore two classes
would require simultaneously

    6H+2P=sin(pi/5),
    6H+2P=sin(2pi/5),

which is impossible. This excludes the entire admissible mark-local
truncation topology, not merely the small-cut fixture. No metric congruence
search is warranted within this scope.

The concrete fixture also fails two classes by the simpler size test:
a cap is contained in a radius-epsilon square of area 4epsilon^2, whereas
each derived large hexagon has area at least its original quad area minus
epsilon^2. The checker verifies strict separation of these bounds.

## Exact remaining escape

A new construction must change either the thin/thick final count vectors
or the mark-local transfer balance. Context-dependent cap slices can break
the latter: D must depend on the donor rhomb species or neighboring source
context, so opposite incoming/outgoing transfer sums need not cancel in
each source type. Such a rule must still reconstruct only two unmarked
convex classes and enforce its context geometrically. No such coordinates,
two-class construction, or decoder are established here. Alternatively,
source-species-dependent incidence counts must yield linearly independent
vectors (number of pentagons, number of hexagons); keeping the same (2,6)
vector cannot defeat this area gate when transfers remain mark-local.

Replay, exact finite domain and geometry checks:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/three-sector-fractional-independent-check-2026-10-15.py

Dependencies: the previously reviewed marked infinite Ammann source; the
rhomb coordinates and arrow incidence in
`ammann-split-edge-two-recipient-gate-2026-10-14.md`; elementary polygon
dissection, planar Euler counting, and convex corner clipping. The new
combinatorial and area arguments are written above and do not import the
closed directed-offset algebra classification. Novelty is not claimed.
