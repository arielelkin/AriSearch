# A forced-mate overlap kills the one-shared-arm Cairo fixture

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/partial-contact-cairo-single-shared-notch-obstruction-review.md). This is an unrestricted untileability result for the
specific r=4/5 pair. It does not classify the full symbolic family or prove
any original target-wide impossibility.

## Pair and reviewed geometric reduction

Let w=sqrt3,r=4/5,t=6/5 and

    P=(1,r,(3w-r)/2,(wr-1)/2,2),
    Q=((wt-1)/2,(3w-t)/2,t,1,2).

Use the independently reviewed
[canonical fourfold cluster reduction](partial-contact-cairo-single-shared-fourfold-clusters.md).
Any hypothetical original tiling partitions into macrotiles S(r),S(t),
where S(z) is the four axis reflections of the convex quadrant pentagon

    (0,0),(d_z,0),(d_z+1,w),(d_z+1/2,3w/2),(0,c_z),
    d_z=(wz-1)/2, c_z=(3w-z)/2.

Every macro has precisely four convex120 corners E=(plus/minus(d_z+1),
plus/minus w), four convex90 corners R=(plus/minus wz/2,plus/minus3w/2),
and four reflex240 axis corners. Both species must occur in any original
tiling, since each is internally four-distinct and cannot tile alone by
the reviewed private-arm theorem. In fact the proof below only needs one
S(r) occurrence; an S(t)-only tiling would give a Q-only original tiling and
is already excluded.

## Exhaustive filler placements at one right-axis notch

Fix one S(r) centered at the origin. At its right-axis notch

    A=(d_r,0),

the macrotile interior occupies240 degrees, leaving the rightward120
sector between directions300 and60. Any incident macrotile sector has
angle90,120,180 or240 (the180 value is a side-interior contact). Therefore
the missing120 can only be one macro convex120 corner, not several sectors
or a straight-side fragment. This sector must be an E corner of S(z), with
z=r or t.

Matching its two boundary rays to the notch directions exhausts its physical
placements. The choices that interchange its unit and double edge are the
two reflected possibilities. The intrinsic two axis reflections of S(z)
identify its other native E corners. Thus the only possibilities are S(z)
with the same axis directions and centers

    B_center=(H_z, plus/minus w),
    H_z=d_r+d_z+1.                                   (1)

The upper choice has its lower-left E at A, with its length2 edge along the
host's upper length2 edge and its length1 edge along the first half of the
host's lower length2 edge. The lower choice is exactly reflection in the
horizontal axis. This derivation allows every original orientation sign
and species, rather than presupposing a common macro orientation.

For reference all four actual whole-macro placements in(1) have interiors
disjoint from the host. Thus the contradiction below arises at a forced
continuation, not a fabricated one-ended angle mismatch.

## The unit breakpoint forces a reflected entire cluster

Consider the upper choice. Its length1 edge ends at its native90 corner

    X=(d_r+1/2,-w/2)=(wr/2,-w/2),                     (2)

strictly inside the host's length2 e side. The host contributes a straight
180 sector, the filler contributes90, and the remaining tile must contribute
90. At X the perpendicular seam is the whole private native bank of
length z: Pb=r if z=r, or Qc=t if z=t. Those globally private side lengths
can only match their own native slots; their90/120 endpoints force the
physical mate to be reflection in their common seam line. The line from X
to the filler cluster's lower axis notch has direction30 degrees.

By the canonical cluster theorem the mate tile belongs to the whole
reflected cluster C obtained by reflecting the filler B in this line. Put

    F30=((1/2,w/2),(w/2,-1/2)),
    C={X+F30*(y-X): y in B}.                          (3)

The cluster center in(3) differs from B_center, so this is a different
canonical cluster. It must have interior disjoint from B. The lower choice
is the horizontal reflection of this entire configuration and has the
corresponding Fminus30 reflection.

The original perpendicular seam is forced even though other bank contacts
in this family may be partial. The argument uses a T's two native90 sectors
and their full90-to120 perpendicular arms, not an assertion that the bank
length z must always whole-match in every other situation.

## Exact strict interior overlap, both possible filler species

Index the four quadrant pieces by their reflection signs in the order
(-,-),(-,+),(+,-),(+,+). For the upper choice, piece2 of B and piece2 of
its reflected C have a common strict interior point:

    z=r:  W=(24w/25+3/10, -2w/5+14/25),
    z=t:  W=(31w/25+3/10, -2w/5+21/25).              (4)

Each of the five oriented edge determinants for either polygon has the
same strict sign at W. The reflected lower choices have the horizontally
reflected witnesses. Thus all four placements in(1) force overlap of two
actual original pentagon interiors in different canonical clusters. This
contradicts the tiling definition.

Every possible filler for the one notch has been excluded. Therefore the
exact pair P,Q admits no unrestricted plane tiling.

## Replay, review and scope

[Exact checker](../searches/partial-contact-cairo-single-shared-notch-obstruction.py)
uses Q(sqrt3) only. It reconstructs all four whole macro placements, checks
all64 constituent convex-pair comparisons for initial host/filler interior
disjointness by the separating-axis theorem, reconstructs both forced
reflection matrices and distinct centers, and checks all40 strict oriented
edge determinants for the witnesses in(4) and their lower reflections.
No solver, finite extension search, numerical angle test or failed deadline
is used. The output is a finite geometric certificate of a proved forced
local contradiction.

This proof has not been extended to every parameter in1/w<r<2-1/w. The
cluster reduction's privacy and singleton event hypotheses and the strict
overlap inequalities must be rechecked before any such extension. There
is no existence claim for the pair or its macrotiling. The original global
two-convex-polygon task remains unresolved.
