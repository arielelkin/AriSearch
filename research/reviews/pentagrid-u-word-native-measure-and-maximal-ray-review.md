# Fresh hostile review of the U native measure and maximum-ray obstruction

**Reviewer:** pending_reviews. This reviewer did not develop the U route,
its metric identities, or the measure/maximal-ray proof.

**Verdict: valid** for the native-measure limit theorem, conditional
maximum-ray exclusion, finite mirror-U untileability theorem, and the
subsequently added finite-U edge-to-edge untileability corollary. One
omitted case in the description of the asymmetric gap was reported and
has been repaired by the author. The reviewer read that repaired text and
the added edge-to-edge proof. No mathematical proof repair was required.
General asymmetric U tilability with partial contacts remains unresolved.

## Exact claims and hypotheses inspected

The [lemma](../lemmas/pentagrid-u-word-native-measure-and-maximal-ray.md)
concerns an arbitrary fixed, nonempty finite collection F of genuine convex
pentagons with cyclic angle word (36,108,144,144,108) degrees, up to cyclic
shift and reversal. All side lengths are positive; each polygon has positive
area. Tiles use arbitrary translations, rotations and reflections, and a
tiling may omit reference types. There is no common scale, algebraicity,
finite orientation, full-edge, or uniform vertex-separation assumption in
the main theorem.

The reviewed statements are:

1. Any admitted tiling by F has an admitted translated placement limit in
   which every native-corner atom has weight zero. Its full native stars are
   exactly 334 and 1144, and its partial-contact stars are exactly 14 plus
   one straight sector, with angles in units of pi/5.
2. In such a zero-star tiling, an acute-incident side of globally maximum
   length cannot directly border a native 144 sector at its acute endpoint.
3. If every reference polygon has equal acute-incident lengths A=B, no
   admitted tiling by F exists, including unrestricted partial contacts.
4. Every finite U collection, including asymmetric metrics, admits no
   edge-to-edge tiling. This fourth statement was added during the review
   and was separately inspected after the initial three statements.

Finiteness is used materially: it gives a fixed positive minimum area,
bounded diameter, compact placement limits, and an attained length maximum
on the subset of types occurring in the limit. No extension to infinite
collections or variable scales within one reference type is certified.

## Metric identities and the full/half-star enumeration

With the stated labeling, the directed edges are
A, B*z^4, b*z^6, c*z^7, d*z^8, where z=exp(pi*i/5). The independent real
components of closure give

    A=phi*b+phi*c+d,  B=b+phi*c+phi*d.

The reviewer checked the directions against the external turns and checked
substitution using the golden-ratio relations. Every b,c,d is strictly
shorter than both A and B, since all lengths are positive. Multiplication
by phi gives

    phi*A-B=phi*b+c,  phi*B-A=c+phi*d,

so A<phi*B and B<phi*A are strict. A reflected copy reverses the labeling
and exchanges the relevant choices; both long-side formulas and both ratio
bounds are present. No metric restriction beyond genuine positive lengths
has entered.

At a native corner, finitely many incident tile sectors cover the disk.
A tile containing that point in the relative interior of a side contributes
one straight sector. Two such straight sectors leave no positive angular
space for the distinguished native corner, so there are either zero or one.
The native angle budgets are consequently 10 and 5 in units of pi/5.

For full stars, n1+3*n3+4*n4=10 and
h=2*n1+n3-2*n4=5*(4-n3-2*n4). The cases n4=0,1,2 give n3<=3,2,0,
respectively, and hence h>=0. Equality occurs only at
(n1,n3,n4)=(0,2,1) or (2,0,2). For half stars the budget is 5 and
h=5*(2-n3-2*n4); the cases n4=0,1 give n3<=1,0, with equality only at
(1,0,1). This exhausts the three advertised zero stars. All other atoms
have weight at least 5. The angle budgets also bound native valence by 10;
no infinite star or subdivided-side case is suppressed.

Each tile contributes two weights 1, one weight 2, and two weights -2,
with total zero. Although individual native contributions can be negative,
all coincident contributions must first be added at their common point.
The resulting measure is nonnegative by the exhaustive star calculation.
This aggregation is essential and is explicitly present in the proof.

## Window defects and continuity under merging vertices

For a fixed collection, every tile meeting a bounded region lies in its
fixed diameter enlargement. Pairwise disjoint interiors and a positive
minimum tile area bound its number of tiles. The same packing bound applies
to any fixed-width strip around a square boundary and gives O(R) tiles,
uniformly over translated squares.

Comparing the corner sum within a square with the sum from tiles whose
centroids lie in it therefore changes only O(R) tile contributions. The
latter sum is zero tile by tile; each tile has bounded total absolute corner
weight. Thus mu(W_R)=O(R). Because mu is nonnegative and every positive
atom weighs at least 5, the number of positive atoms is O(R) as well. No
density limit or positive density of a particular type is assumed.

For each fixed H, if every radius-H disk contained a positive atom, the
radius-H disks about relevant atoms would cover a large square. Only
O(R+H) atoms in its H-enlargement could contribute, so their total disk
area is O((R+H)*H^2), smaller than the square area for large R. Growing
bad-free disks therefore exist. This is a nonnegative defect argument,
not a pointwise inference from a vanishing mean.

The local placement compactness step also checks. Tile count in every
bounded enlargement is uniformly finite, centroid coordinates remain
bounded there, the reference label set is finite, and orientation matrices
lie in compact O(2), including reflection. A diagonal extraction on
boundaries avoiding limiting centroids accounts for every limiting tile.
Every point is covered by a convergent covering tile within bounded
centroid distance. An interior overlap between limiting polygons, including
two copies collapsing onto the same polygon, would persist before the
limit and is impossible. The resulting locally finite covering is admitted.

For a compactly supported continuous test function, only uniformly finitely
many tile placements in a fixed centroid enlargement can contribute native
corners. Their corner coordinates converge and their reference weights
remain fixed. This proves vague convergence of the signed native measures
by an actual finite sum, even when different vertices or T-junctions merge.
The approximating sum is zero once its support lies in the growing good
disk, so the limit measure is zero. Coincident limiting corners add their
weights; the proof does not require an old combinatorial star to persist.
Reapplying the unrestricted full/half-star classification to the admitted
limit is legitimate. A native 108 in another side interior would require
the positive half star 108+36+36 and is therefore forbidden.

## Conditional maximum ray and finite mirror theorem

The maximum is taken after restricting to types actually used in the
zero-star limit; it is attained by a present tile. Every used short side
is strictly below it. Suppose the selected maximum acute side M has a
native 144 neighbor R along that ray. If its R side is b or d, the other
endpoint has angle 108 and lies strictly inside the maximum side, already
excluded. The R side must be c.

At c's other endpoint, the maximum-side tile supplies a straight sector
and R supplies 144. The zero-star list forces a third tile S supplying 36.
Its forward acute side and the remaining part of the maximum side both
end at native 108; unequal lengths would put the shorter endpoint inside
the longer side. The same argument applies to the other acute side of S
and the b/d side of R. Thus their lengths are exactly M-c and r, where
r is b or d. The strict ratio bound for S gives M<c+phi*r.

If r=b, the R long side A exceeds c+phi*b; if r=d, its long side B exceeds
c+phi*d. Either contradicts M's global maximum. The local sector geometry
uses the whole actual overlapping segment; it does not assume that an
initial partial contact is a full-edge match.

Every zero star containing a native 36 gives that corner a native 144
neighbor along at least one of its two rays. In full 1144 this holds for
both cyclic arrangements, and in half 14 it holds on the ray away from
the straight sector. If A=B=M, either ray is maximum, so a permitted ray
always exists. This validates the finite mirror-U corollary at arbitrary
relative scales and under reflection. A stronger cross-type inequality
between all short sides and all long sides is unnecessary.

## Added edge-to-edge corollary

The reviewer independently checked persistence of full-side neighbors.
For a limiting tile and one native side, every approximating placement has
a whole native side of a neighbor equal to it. That neighbor's centroid
lies within a uniform bounded enlargement. Passing to a further subsequence
fixes its reference type, native side index, and endpoint correspondence.
The neighbor is among the extracted placements, and full endpoint equality
passes to the limit. It cannot collapse onto the original tile because
interior overlap would persist. At an interior point of their common side,
the two genuine convex polygons occupy the two opposite local half-disks.
A third native positive-angle sector there would overlap one of them.
Hence additional partial contacts cannot appear on the full matched side,
and the admitted limit is edge-to-edge.

For a globally maximal long side M and the other acute long side L of its
tile, a zero-star acute ray has a 144 neighbor and length x in {M,L}.
Full-side matching gives a neighbor short side x, equal to b,c, or d.
Its corresponding A or B is strictly greater than phi*x. If x=M this
already violates maximality. If x=L, the tile's own ratio gives M<phi*L,
and the neighbor long side again exceeds M. This checks all b/c/d and
reflected choices and proves the edge-to-edge obstruction for every finite
U collection. The proof does not promote this conclusion to unrestricted
asymmetric partial-contact tilings.

## Defect found, author repair, and remaining scope

The first version said that a maximum ray failing to meet 144 could meet
only the other 36 in a full 1144 star. The half 14 star also allows it to
border a straight 180 sector while the shorter acute ray meets 144. The
reviewer reported that omitted case; the author repaired the description
to list both possibilities, and the reviewer reread the repaired text.
This was a scope-description defect, not a defect in the explicitly
conditional maximum-ray claim or the mirror theorem. No claim excluding
all straight-carrier subcases is used or certified here.

Attacks included arbitrary relative scales, omission of the type attaining
the original reference maximum, reflected native labels, multiple straight
sectors, merging partial vertices, signed-weight cancellation, coincident
limit tiles, boundary atoms, changing full-side neighbors, and replacement
of a maximum ray by a shorter ray. None invalidates the four stated
claims. There is no remaining uncertainty in those claims after the
wording repair. General asymmetric U tilability with partial contacts
remains a separate theorem-strength obligation; no bounded patch search,
monohedral classification, or external theorem establishes it in this
artifact. No literature-priority claim was audited or is made. The original
unrestricted two-convex-polygon target remains unresolved.

This is an analytic review. No floating-point decision, solver result,
finite computational bound, or new computer checker is needed for its
verdict.
