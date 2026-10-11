# Equal private octagon sides: symmetry kills the matching branch

**Status:** adversarially reviewed symmetry theorem and exact unit-metric
closure classification; see the [VALID fresh review](../reviews/private-octagon-equal-private-symmetric-review.md). The universal equiangular-P
rigidity dependency is separately [adversarially reviewed](private-octagon-adjacent-corner-rigidity.md).
This file addresses an equal-private-side mechanism and does not classify
all equal-private octagons or resolve the unrestricted research target.

## Exact theorem

Let P be any genuine convex equiangular108 pentagon. Let Q be a genuine
convex octagon with two nonadjacent108 corners and six144 corners. Suppose:

* a length L absent from P occurs on exactly two native sides e0,e1 of Q;
* an actual Euclidean symmetry S of Q exchanges those two sides.

Then every admitted plane tiling by{P,Q} has a nonzero translation period.
The other six Q lengths are unrestricted. Equal private lengths need not
produce distinct geometric neighbor choices when their two native roles
are related by a genuine shape symmetry.

By all-obtuse forcing, all contacts are full sides and every native star
is108+108+144. Each L side matches another L side of Q. It cannot be144/144:
neither possible mate has two108 endpoints, because Q has no108/108 side.
Every matching would therefore produce a144/144 endpoint on at least one
end. Thus both private sides are108/144, and their endpoint correspondence
exchanges angle types. Exactly one private side is incident to each108
corner, since two at the same108 corner would contribute two144 neighbors.

Consider the mate of a reference Q across e_i. It is GQ and its matching
native side may be either e_i or e_(1-i). If it is the second, replace its
native labeling by composing G with S or S^-1, so that the same polygon
GQ is represented using native side e_i. This does not alter the physical
placement or endpoint corner types. The unique allowed endpoint-exchanging
isometry across one fixed108/144 side is its midpoint half-turn: the other
endpoint-exchanging isometry is reflection in the perpendicular bisector,
which preserves the supporting interior half-plane and overlaps. Therefore
the geometric mate is always precisely H_(a_i)Q, independent of native
labeling. Here a_i is the midpoint of e_i.

The private midpoint-chord argument in the reviewed direct theorem now
applies without change: both private contacts are actual midpoint half-turns,
so every Q chain is a straight double-infinite chain with period2(a1-a0).
All Q axes are disjoint full lines, hence parallel, and their equal-length
period vectors synchronize to one nonzero u. All Q copies belong to these
chains. The entire Q set is invariant under both u and -u.

Every equiangular108 P has adjacent-corner rigidity, even with repeated
lengths. Every P has at least3 Q side neighbors, hence a PQQ corner with
prescribed whole adjacent P sides. Translation by u sends its Q pair to
actual Q copies; the third tile cannot be Q because pulling it back by -u
would overlap the original P. The actual P completion is unique and equals
P+u. The same with -u gives the inverse. Thus the whole original tiling
has period u, proving the theorem. No good-limit saturation is used.

## Complete equal-private closure family for regular unit P

Suppose additionally P is regular unit and the other six Q lengths are1,
with L>0,L!=1. Normalize Q's108 corners to0,d, where d in{2,3,4}. Rotate
side0 to direction1. Its native direction exponents are

    k_j=j+1[j>=d],   j=0,...,7,

in units pi/5. The two private sides must lie at i in{7,0} and
j in{d-1,d}, one incident to each108 corner. Thus exactly12 cases occur.
Writing z=exp(pi*i/5), native closure is

    (L-1)*(z^k_i+z^k_j)=z^d+z^9.                      (1)

The complete positive nonunit solutions are:

| Alpha gap | Private slots | Equal length | Actual symmetry |
| --- | --- | --- | --- |
| 2 | 0,1 | phi | reflection vertex index v -> 2-v |
| 3 | 0,2 | (5-sqrt5)/2 | reflection vertex index v -> 3-v |
| 4 | 7,3 | arbitrary L>0,L!=1 | central half-turn v -> v+4 |
| 4 | 0,4 | arbitrary L>0,L!=1 | central half-turn v -> v+4 |

The two gap4 rows are congruent by reflection. Thus there are two fixed
metric types and one positive one-parameter type, up to congruence.
Every displayed positive closed walk is strictly convex by its increasing
edge directions. Its angle and length words are invariant under the
indicated index involution, which therefore is an actual geometric
reflection or half-turn of the polygon. That symmetry exchanges the two
private sides. The theorem consequently excludes strong aperiodicity for
this entire regular-P equal-private subfamily.

This conclusion does not assert that any particular row tiles the plane.
It says that any admitted tiling of any row is periodic, while all omitted
rows are excluded by exact closure/positivity or by the private-length
hypothesis L!=1. In particular, gap4 L=1 is a genuine closed octagon; it
is excluded because its length is not private from regular unit P. The distinction matters:
a periodic-escape theorem can kill a candidate without providing a new
plane-existence proof for its individual metrics.

The [exact producer](../searches/private-octagon-equal-private-unit-closure.py)
performs the12 cyclotomic closure solves and retains every row in
[the certificate](../certificates/private-octagon-equal-private-unit-closure.json).
Normal replay is nondestructive:

    conda run --no-capture-output -n arisearch python research/searches/private-octagon-equal-private-unit-closure.py

There is no solver, seed, symmetry pruning, period cutoff or timeout. The
producer completes with SageMath10.9/Python3.12.13. Saving requires explicit
--output. Its finite domain is exactly the12 closure cases; tiling existence
is not searched. The retained fresh review separately validates the symmetry-mate
argument and independently checks equation(1), omitted cases and actual
coordinate involutions, including the full free-L positive range.

## Nonsymmetric equal-private sides: exact local holonomy boundary

The equality L alone does not identify a physical mate. For arbitrary Q
with exactly two L sides, write sidei from p_i to q_i with e_i=q_i-p_i,
|e_i|=L. Let delta_i=+1 when it starts108 and ends144, and -1 when it starts
144 and ends108. Both sides are108/144 in any tiling by the first argument.
Across native sidei, a Q mate using native sidej has one precise allowed
isometry, including reflections:

* If delta_i=delta_j, the mate is orientation preserving,

      G_ij(t)=-(e_i/e_j)*t+q_i+(e_i/e_j)*p_j.

  It sends p_j to q_i and q_j to p_i, rotates by
  pi+arg(e_i)-arg(e_j), and has opposite supporting interior.
* If delta_i=-delta_j, the mate is orientation reversing,

      G_ij(t)=(e_i/conjugate(e_j))*conjugate(t)
                +p_i-(e_i/conjugate(e_j))*conjugate(p_j).

  It sends p_j to p_i and q_j to q_i, exchanges the angle types,
  and again has opposite supporting interior.

For i=j the first formula is the midpoint half-turn. For i!=j, it may be a
nontrivial rotation, translation, reflection or glide reflection. The two
formulas exhaust endpoint assignments because the108/144 angle types and
supporting half-plane force which endpoints correspond.

A private chain exiting sidei and entering the mate's sidej must next exit
its other side1-j; its holonomy is the actual product of these G maps.
In the homogeneous all-cross-slot pattern its copies are G_01^n(Q).
An orientation-preserving G_01 has angle an integer multiple of pi/5:
nonzero angle gives finite order dividing10, while zero angle gives a
translation. An orientation-reversing G_01 squares to a translation; if its
square is identity, an all-cross pattern would make two tiles share both
private sides and cannot occur. Thus allowable all-cross reflection patterns
are glide chains with a nonzero two-step period. Mixed native choices need
not reduce to a single repeated map.

These are exact local alternatives, not a plane-existence assertion for
such chains. Without the actual Q symmetry in the theorem, G_ij(Q) can
be a different geometric neighbor from H_(a_i)(Q). Then private chords can
turn or zigzag, so the earlier straight-axis/common-period proof does not
apply. No broad impossibility follows from this limitation. A nonsymmetric
equal-private family remains an active boundary requiring a concrete
assembly or a new invariant.
