# Candidate obstruction for parameter-swapped symmetric U pentagons

**Status:** superseded as a proof candidate by the broader
[finite mirror-U native-measure obstruction](pentagrid-u-word-native-measure-and-maximal-ray.md),
which was internally proved with the same additive-weight limit argument
and is awaiting its own fresh review. This narrower record preserves the
concrete parameter-swapped constructive attempt and its cheap falsification.
It was developed after the independent Robinson review. It is not separately
promoted as independently reviewed.

## Exact proposed pair and broader hypotheses

Let z=exp(pi*i/5), phi=(1+sqrt(5))/2. For b,c>0 define U(b,c) by
successive side directions (1,z^4,z^6,z^7,z^8) and side lengths

    (a,a,b,c,b),    a=phi^2*b+phi*c.

The already reviewed metric family proves exact closure and strict convexity.
The native angle word after the sides is (1,3,4,4,3) in pi/5 units.
Its 36-degree corner is between the two a sides; each a side ends at a
108-degree corner. Each 144-degree corner is between a b side ending at
108 and the c side ending at the other144 corner. The shape is intrinsically
mirror symmetric, so the distinct proposed shapes are U(b,c) and U(c,b),
not a shape and its reflected congruent copy. The concrete proposed pair
uses b=1,c=sqrt(2).

The candidate theorem is slightly broader: a finite collection of such U
shapes cannot tile the plane if every native b or c side in the collection
is strictly shorter than every native a side. It allows all isometries,
arbitrary partial contacts, and omission of any types.

For the parameter-swapped pair this inequality holds for every b,c>0:
each of phi^2*b+phi*c and phi^2*c+phi*b exceeds max(b,c). The theorem
would therefore reject the whole swapped family, including b=c.

## Native-corner weight and a zero-weight plane limit

Assign native corner weights2,1,-2 to angles36,108,144 degrees,
respectively. Every U tile has total weight2+2-4=0. At a tiling vertex
with a genuine native corner, there can be at most one straight-through
tile: two pi sectors leave no positive angle. Thus native corners sum
either to2pi or to pi when a straight-through tile is present. Let
(n1,n3,n4) count the three native angles. These satisfy

    n1+3*n3+4*n4 = 10 or5.

Direct exhaustive integer enumeration gives nonnegative native weight

    h=2*n1+n3-2*n4.

The zero-weight possibilities are exactly

* full334: two108 and one144;
* full1144: two36 and two144;
* half14: one36 and one144 plus a straight sector.

All other possibilities have weight at least5. This finite enumeration
is of local angles only, not of a geometric patch or period domain.
For a hand check, put s=10 or5 and substitute
n1=s-3*n3-4*n4. Then h=2s-5*n3-10*n4. For s=10, n4 is0,1,2
with n3 at most3,2,0; for s=5, n4 is0 or1 with n3 at most1 or0.
The stated nonnegative values and zero cases follow immediately.

In a translated centroid window, the native corner weight sum differs from
the sum over stars inside the window by O(R), uniformly in translation.
Only tiles in a fixed-width boundary strip contribute this discrepancy;
fixed positive minimum area and bounded diameter bound their count by O(R).
Consequently the sum of nonnegative star weights is O(R), and the number
of positive-weight vertices is uniformly O(R). Mark a tile bad when one
of its native corners is at a positive-weight vertex. There are at most
ten native corner incidences per vertex, so bad centroids also have O(R)
counts. Every positive-weight vertex has at least one such marked tile.

For any fixed radius H, there is a disk containing no bad centroid:
otherwise radius-H disks about O(R+H) bad centroids would cover a square
of area4R^2, contrary to their O((R+H)H^2) total area for sufficiently
large R. Translate growing bad-free disks to the origin. Fixed compact
positive-area shapes, bounded positions, and compact O(2) permit a
diagonal limit of all tile placements in each bounded enlargement.
Disjoint interiors and coverage persist, by the usual open-overlap and
closed-covering-tile arguments. The result is an admitted plane tiling.

Partial contacts can make distinct vertices merge in this limit, so no
uniform vertex separation is claimed. Instead native weights are additive
under merging. Fix a native vertex v of the limit. In a sufficiently small
ball about v there are no other limiting native vertices: only uniformly
finitely many tiles meet its bounded enlargement, and each has five native
vertices. Choose the ball boundary away from those finite corner positions.
Extract all these tile placements, so the corresponding native corners in
the approximating tilings are exactly the ones converging to v. For large
indices every original star inside this ball is zero-weight, since its
native incident tile centroids lie in the growing bad-free disk. The
sum of their weights is zero. Equivalently, the sum of native corner
weights inside the ball is zero. After convergence this is precisely the
native weight at v, even if multiple stars have merged and straight sectors
have changed. Thus every limiting star has weight zero. This step is the
specific fresh-review obligation; it avoids imposing full-edge forcing
or a finite orientation alphabet on these acute-corner pentagons.

## The exact two-step local obstruction

Choose any U tile in that zero-weight plane and its36-degree corner v.
In a full1144 star, every36 sector has at least one adjacent144 sector;
in a half14 star it has exactly one adjacent144 sector. These exhaust the
zero-weight stars containing36. Hence one of the tile's a sides shares a
positive initial segment from v with a native side of a144-corner neighbor.
That neighboring side has length b or c, and is shorter than a by the
global metric inequality. It therefore ends strictly inside the a side.

If it is the neighbor's b side, its other endpoint has angle108. A
native108 corner in the interior of the original side is impossible in a
zero-weight tiling: the original tile supplies a pi sector and the remaining
72 degrees must be two36 corners. This is the positive-weight half311 star.

Therefore the initial neighbor must use its c side. Its far endpoint w has
angle144 and lies strictly inside the original a side. The star at w is
then half14, forcing a new36-degree U corner. Its side along the forward
ray of the original a side is another a side, of length a'. Its other a
side lies along the other side of the same144-corner neighbor. That side
is a b side: at the opposite end of the neighbor's c base, the adjacent
side has length b and ends at108. By the global metric inequality b<a'.
Thus this b side ends strictly inside the new tile's a side, producing
the forbidden half311 star. There is no need to iterate a length recurrence.

Alternatively, comparing the forward a' side to the remainder of the
original a side forces a'=a-c_neighbor, since a mismatch puts one of
their108 endpoints inside the other's side and also creates half311.
This gives a strict-length descent, but the b-side obstruction already
contradicts the zero-weight tiling after two adjacent native contacts.

No zero-weight plane tiling exists; the preceding limit implication then
excludes an arbitrary original admitted tiling.

This local argument uses actual full polygons and finite positive edge
segments. Reflection changes neither the endpoint types nor the forward
length comparison. The third tile's forward a side follows from the half14
sector geometry, not an assumed global edge-to-edge rule.

## Constructive attempt and scope

The attempted seed was a long-edge zipper. A long upper U(1,sqrt(2)) edge
was paired partially with an opposite U(sqrt(2),1) long edge; a144-corner
tile fills the36-degree apex gap. Since

    a(sqrt(2),1)-a(1,sqrt(2))=sqrt(2)-1,

an initial horizontal placement can align its short segments of lengths1
and sqrt(2). Following the other long edge invokes the descent above and
forces a108 T-junction of positive native weight. This rejects the hoped-for
zero-defect zipper mechanism rather than treating an unexplored macro gap
as an aperiodicity claim. The analytic candidate would reject all assemblies
of this swapped pair if its zero-weight limit step passes review.

No bounded period search or larger packing search was run. This theorem
does not concern the different-angle U/V or U/W families. It also does not
exclude arbitrary asymmetric U-word metrics, a finite metric collection
whose short and long lengths interleave, or other angle words. No primary
literature priority claim is made.
