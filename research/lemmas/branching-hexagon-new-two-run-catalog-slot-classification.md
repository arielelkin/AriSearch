# Exact native-slot classification of the distinct-length two-run catalog

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/branching-hexagon-new-two-run-catalog-slot-review.md). This is a specified finite catalog and three specific parameter
curves, not a classification of arbitrary two-run hexagons or a main-target
resolution. The15 equal-length cases remain outside this theorem.

## Fixed finite domain

Let z=exp(i*pi/12), q=1. A has native side lengths(p,q,p,q,p,q) and
side directions(0,75,120,195,240,315). Enumerate all81 ordered tuples
(beta1,beta2,beta4,beta5) in{90,120,150}^4 with no symmetry reduction.
These describe B's homogeneous p,p and q,q corner angles. For a tuple
(a,b,c,d), put

    P=(1,z^((180-a)/15),z^((360-a-b)/15)),
    Q=(1,z^((180-c)/15),z^((360-c-d)/15)),
    p=sqrt(|sumQ|^2/|sumP|^2)>0,
    R=-p*sumP/sumQ.

B's six directed edges are pP followed by RQ. Closure is exact and R
is unit. Strict support is checked for every side against every nonincident
vertex. All66 reconstructed p!=q shapes are strictly convex. The15 p=q
cases are recorded as excluded equal-length cases, not as periodic escapes.
They are not analyzed by the distinct binary-edge model.

## Exact result

**Theorem. The66 distinct-length pairs split into54 untileable pairs and12 pairs with explicit periodic tilings.** The original angle-only gate had52 feasible
cases and14 rejects. Of its52 survivors,40 now carry exact strong seam
duals and12 carry actual periodic quotient witnesses. No case in the66
is unresolved, timed out, or classified from a bounded search failure.

The12 periodic tuples, grouped by an exact native similarity orbit, are

|Representative|All tuples in its orbit|Native p values|Quotient faces|
|---|---|---|---:|
|(120,120,90,150)|(120,120,90,150),(120,120,150,90),(90,150,120,120),(150,90,120,120)|cos15 or1/cos15|4|
|(90,90,90,150)|(90,90,90,150),(90,90,150,90),(90,150,90,90),(150,90,90,90)|2cos15 or1/(2cos15)|4|
|(150,150,90,150)|(150,150,90,150),(150,150,150,90),(90,150,150,150),(150,90,150,150)|1/sqrt2 orsqrt2|8|

The other54 distinct-length tuples are exactly those with UNSAT strong
native-slot data in the complete retained catalog. The two outcomes are
supported by different certificates: rational separating functionals for
the54, actual flat-torus quotients for the12.

## Complete native-slot star and seam model

Each shape has6 indexed native corner slots, giving12 typed corners.
For each slot retain both cyclic orientations, resolving its two incident
indexed side slots and which reference endpoint is at the star centre.
All length-legal oriented native three-corner stars are enumerated, allowing
repetition of a native slot from distinct tile occurrences. Their angles
sum360 exactly when the product of their three unit internal-angle complex
numbers is1. Strict angles lie in(0,180), so no other multiple of360 is
possible. Every permutation and every reflection is considered, modulo
cyclic rotation of the entire star only. Homogeneous ppp and qqq stars are
included when their native angles permit them.

For a shared native edge let its indexed slots be x,y and reference-end
flags px,py in{0,1}. Its key is the lexicographically ordered slot pair
and parity px xor py. Its sign is+1 at reference endpoint0 of the smaller
slot and-1 at endpoint1. At the other geometric endpoint both flags reverse,
so its signed potential cancels. If x=y and parity0, the flags agree and
the sign is unambiguous. If x=y and parity1, no occurrence is distinguished;
define the feature to be0 rather than choosing an arbitrary first tile.

Let C_t,S_t be the typed corner and signed seam counts of star t, and M_s
one copy of each native corner of species s. The complete necessary system
for a trivalent edge-to-edge tiling is

    sum_t C_t X_t = F_A M_A + F_B M_B,
    sum_t S_t X_t = 0,
    X_t>=0, F_A>=0, F_B>=0, F_A+F_B=1.

No ratio F_A/F_B is prescribed and species omission is allowed. For the12
feasible records an additional exact check finds both species positive;
their retained primal frequencies happen to have F_A=F_B=1/2. This is
a result of those records, not an inserted restriction.

The model is only necessary and may overinclude impossible assemblies.
For every UNSAT case the retained rational vectors W,Y satisfy

    W dot C_t + Y dot S_t >= 0 for every enumerated star t,
    W dot M_A <= -1, W dot M_B <= -1.

All inequalities are checked with exact Fraction arithmetic before the
record is retained. A rational primal is stored for every feasible case.
All81 ordered cases finish; no timeout or floating decision occurs.

## Infinite consequence of each strong dual

Suppose one rejected pair tiled the plane. The independently reviewed
[defect-free hexagon limit theorem](hexagon-limit-and-periodicity.md)
produces an admitted tiling by the same two shapes that is edge-to-edge
and everywhere trivalent. Either species may disappear; the strong dual
still gives negative charge on every occurrence of either shape.

Select native tiles whose interiors meet a square Q_R. There are N selected
tiles, with total W corner charge at most-N. At a complete selected star,
adding the signed Y seam potentials gives a nonnegative charge. The two
ends of every seam whose endpoint stars are both complete cancel exactly.
Incomplete selected stars are incident to boundary tiles. Fixed maximum
diameter, positive minimum area and disjoint tile interiors bound their
number by O(R), uniformly. Every tile has6 corners and6 sides and all
finite rational weights are bounded, so all incomplete corner charges
and uncanceled seam-end charges together are O(R).

Therefore the total selected W charge is at least-O(R), yielding N<=O(R).
But the selected tiles cover Q_R and have bounded maximum area, so
N>=4R^2/Amax. This contradiction excludes the trivalent tiling and hence,
via the reviewed defect-free limit, any original unrestricted tiling.
No translation invariance, existence of frequencies, positive density of
either species, or restriction on rotations/reflections is used.

## Positive certificates for all12

Three raw quotients supply the representative tilings:

* [first curve](branching-hexagon-new-two-run-periodic-escape.md):4faces;
* [second curve](branching-hexagon-new-two-run-sqrt2plus3-periodic-escape.md):4faces;
* [third curve](branching-hexagon-new-two-run-third-curve-periodic-escape.md):8faces.

Every quotient has all side occurrences paired once, equal exact matched
lengths, connected dual graph, and one circular link of angle360 at every
vertex. It is a compact orientable flat torus, whose complete universal
cover gives a periodic plane tiling. The third representative arises at
attempt278 of the pre-stated1024 two-copy seam lifts; exhaustion would
have supplied no untileability conclusion.

The [transfer certificate](../certificates/branching-hexagon-new-two-run-catalog-periodic-transfers.json)
contains all12 target tuples, exact native vertex shifts and cyclic/reflected
orientations, their common positive scale factors, raw target face boundaries,
side pairings and vertex classes. Each species is congruent to its source
with the same scale; independent rotations and native reflections are
allowed. All6 vertices of each native similarity are checked exactly,
rather than only side/angle multisets. A common rescale therefore transfers
the full plane tiling. Raw transferred side lengths and exact three-corner
angle products are also rechecked. Eight targets have4-face quotients and
four have8-face quotients. No frequency vector supplies the existence proof.

## Retained artifacts and replay

[Complete slot certificate](../certificates/branching-hexagon-new-two-run-catalog-slot-balance.json),
[slot producer](../searches/branching-hexagon-new-two-run-catalog-slot-periodic.py),
[exact transfer producer](../searches/branching-hexagon-new-two-run-catalog-periodic-transfers.py):

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-catalog-slot-periodic.py
    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-two-run-catalog-periodic-transfers.py

Normal replay is read-only. Explicit --output is required for retained
writes. The complete domain is all81 ordered tuples;15 equal-length cases
remain excluded rather than silently collapsed into another category.
The global rejection proof depends specifically on the reviewed defect-free
limit and each independently reconstructed exact strong dual. The positive
proof depends on actual geometry and flat quotients. Both outcomes have passed fresh independent review and raw no-producer certificate reconstruction.
