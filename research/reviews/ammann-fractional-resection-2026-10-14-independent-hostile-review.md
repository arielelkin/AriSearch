# Independent hostile review: Ammann fractional edge-fan transfer

Date: 2026-10-14. **Verdict: VALID for the stated global fan partition,
strict convexity and immediate periodic omission obstruction.** The rule
produces boundary-word categories, not a proved two-congruence-class
aperiodic pair. No new source/contact-class census is warranted by this
result.

Reviewed [the construction note](../searches/ammann-fractional-resection-2026-10-14.md),
[producer](../searches/ammann-fractional-resection-2026-10-14.py) and
[frozen certificate](../certificates/ammann-fractional-resection-2026-10-14.json).
The [independent checker](ammann-fractional-resection-2026-10-14-independent.py)
imports no producer. It reconstructs true complex rhomb centers in
CyclotomicField(10), checks128 strict global supporting determinants
over16 geometries, verifies32 quarter-area identities and instantiates
the two stated native marked contacts exactly. This differs from the
producer's Q(phi) representation and local-turn check.

## Source assumption and plane existence

The selected point J=1/2+(4/5)ζ is exactly the listed J0 in the
[reviewed Ammann theorem](../lemmas/ammann-forcing-aperiodicity.md),
not an unspecified numerical generic point. Its Lemma2 and independent
local review certify strict convexity, distinct a,b,r,c lengths and a
rank3 valuation certificate for (G2), hence (G1)+(G2′) and J∈G*.
The repaired theorem's status includes independent re-review of the
genericity, marked reconstruction and infinite-existence arguments.

Lemma7 gives a legal marked thin/thick rhomb tiling of the entire plane.
Lemma5's converse decorates it into a genuine Ammann three-shape tiling
at J0; its canonical reconstruction gives the marked rhomb partition
used here. Thus the new surgery starts from an established infinite
source, not from finite patches assumed to extend. The later fan surgery
actually needs only the marked rhomb tiling; its geometry is independent
of J0's interior resection.

The native mark table is exactly Lemma5's: thin AB and CB are X, AD and
CD are Y; thick EF and EH are X, FG and HG are Y. Each rhomb has two
edges of each category. Both incident rhombs read the same type and
arrow on a shared whole edge. Full edge-to-edge incidence is an
established source property.

## Global conservation and coverage

The diagonal intersection of a parallelogram divides it into four
equal-area center-to-edge triangles. Their interiors are disjoint and
their union is the rhomb. Each such triangle is assigned to its unique
base edge, and each plane rhomb edge has exactly two incident rhombs.
Gluing the two assigned triangles therefore partitions the entire
plane. Even near original rhomb vertices or diagonal intersections,
there is neither an omitted sector nor duplicated positive-area sector:
these are the existing boundaries of the complete fan partition.

This proves actual global coverage and compatibility for the constructed
partition. It does not assert that every unmarked output tiling is such
a partition. Counting edge categories divides the two incidences at
each edge: n_X=h+T+O(R) and n_Y=h+T+O(R). Because all centers and assigned
edges are at uniformly bounded displacement from their rhomb anchors,
the window error is O(R). Summing exact fan areas gives the original
rhomb area, with the same bounded boundary error in a window. There is
no equal-whole-triad hypothesis; the construction genuinely transfers
fractional rhomb sectors.

## Convexity, degeneracies and exact contact fixtures

Normalize the common edge to0→1. A thin/thick unit rhomb has center
(x,±h), with x=(1±cosθ)/2, h=sinθ/2 and θ∈{π/5,2π/5}. Thus0<x<1 and h>0
for every choice. A right/left center pair makes the simple boundary
word (0,o_right,1,o_left). The right and left triangles lie on opposite
halfplanes, so no self-crossing is possible. Every turn is strictly
positive by the four formulas in the note. The independent checker also
tests all nonadjacent vertices strictly against every support, avoiding
any reliance on local-turn positivity alone.

The sixteen rows are the full4×4 center-choice domain, including a
superset of marked-legal contacts. They exhaust the geometric choices
used by the universal convexity claim; no marked contact catalogue was
silently claimed. All outputs have four genuine native corners. No flat
corner, nonconvex branch, or higher-side face survives this rule.

The thin/thin X example is correctly instantiated. The left copy's AB
arrow is0→1. Mapping the right copy's native C→B arrow to0→1 uses rotation
−ζ⁻¹ and translation−(−ζ⁻¹)(1+ζ), placing its center at(1+ζ⁻¹)/2 below
the edge. The left center is(1+ζ)/2.

The thick/thick Y example is also correct. Normalize the left F→G
arrow by p↦ζ⁻²(p−1); its center is(1−ζ⁻²)/2 above the edge. The right
H→G arrow uses p↦p−ζ² and its center is(1−ζ²)/2 below. These are precisely
the two frozen boundary words and the two mark types in the source
table. Their use as examples does not imply that every legal global
source contains either particular contact.

## Direct independent justification of periodic omission

Every convex quadrilateral has a periodic monohedral tiling. Here is
the elementary argument checked independently for this review. Name
its successive corner anglesα0,…,α3. Their sum is2π, so one of the
adjacent pairsα0+α1 andα2+α3 is at mostπ. Choose the corresponding edge.
Half-turn a second copy about that edge's midpoint. The two copies
have disjoint interiors on opposite halfplanes and form a convex
centrally symmetric hexagon; if the angle sum isπ the two flat boundary
vertices are removed, leaving a parallelogram.

A convex centrally symmetric hexagon tiles by translations pairing
its three opposite equal parallel edge pairs. More explicitly, with
successive hexagon verticesV0,…,V5 and centerO, use the rank2 lattice
generated by V3−V1 and V5−V3. The third neighbor vector is their sum,
V4−V2. Each paired edge is shared by exactly two translated hexagons;
the three angle types at each vertex sum to2π since opposite angles
are equal. The elementary parallelogram case uses its two edge vectors.
This gives a periodic tiling by the hexagon, and placing its two original
quadrilateral copies in every lattice cell gives a periodic monohedral
quadrilateral tiling. For a quadrilateral A,B,C,D joined across AB,
the two lattice generators are A−C and B−D, which are independent
diagonal vectors. Their covolume is twice the quadrilateral area,
matching the two-copy cell.

The research problem permits omission of either species. Therefore any
retained output congruence class already supplies a permitted periodic
tiling, regardless of whether the X/Y categories collapse to two
classes. This is a complete obstruction to this proposed rule as an
aperiodic protoset. It does not deny existence of the constructed fan
cover or constrain other fractional surgeries with different boundaries.

## Defects, repairs and limits

One wording defect was found: the source initially called the cited
side-count/omission argument “reviewed,” whereas its repository artifact
explicitly said the elementary quadrilateral portion had no separate
hostile review. The author was notified and corrected that attribution.
The direct argument above independently supplies the needed elementary
omission proof, so no mathematical gap remains in the fan-rule exclusion.

No defect was found in generic-source applicability, boundary coverage,
quarter-area conservation, the sixteen-row domain, handedness, exact
reference placements or the decoder-scope disclaimer. The constructed
quadrilaterals' remembered bases and parent sectors are auxiliary data;
they have not been recovered intrinsically from arbitrary unmarked
output tilings. The periodic omission counterexample prevents an
equivariant all-tilings decoder into only the reviewed aperiodic source.
No claim about arbitrary other convex pairs, source decoder existence,
two-shape collapse or universal novelty follows.

Replay from the repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-fractional-resection-2026-10-14.py --check research/certificates/ammann-fractional-resection-2026-10-14.json
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-fractional-resection-2026-10-14-independent.py
```

Both commands passed. The new checker uses exact cyclotomic equality
and real-algebraic signs; no float tolerance, solver, random seed,
bounded-failure inference or larger contact enumeration is involved.
