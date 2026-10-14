# One support-line deformation: a positive patch with a global incidence obstruction

Date:2026-10-13. Status: independently reviewed VALID for this exact pair; [hostile review](../reviews/contact-non-equiangular-one-deformation-hostile-review.md).
This is one genuinely non-equiangular octagon / pentagon pair, not a sweep.
The former equiangular-Q native reduction is NOT assumed for this palette.

## Exact shapes and positive patch

Write r=sqrt2,c=cos(pi/8),t=sin(pi/8),k=r-1. Begin with the side-one regular
CCW octagon at vertices(0,0),(1,0),(1+r/2,r/2),(1+r/2,1+r/2),
(1,1+r),(0,1+r),(-r/2,1+r/2),(-r/2,r/2).
Replace its bottom supporting line by y=k(x-1/3), retaining all other
supporting lines. Its first two vertices become

    Q0=(z,-z), z=k/[3(1+k)],
    Q1=(h,h-1), h=(1-k/3)/(1-k).

Keep the other six vertices. The resulting genuine convex Q has native
angles(112.5,157.5,135,135,135,135,135,135), and length word

    (H,u,1,1,1,1,1,v), u=1/3, v=(2+r)/3.

Let P have native word(x,u,v,y,w), x=1,

    y=1-(v-u)/(r*c), w=(u+v)/r-t*(1+y).

Integrate its native edge vectors(xc,-xt),(u/r,u/r),(-v/r,v/r),
(-yc,-yt),(0,-w). They sum0 and give native angles
(112.5,112.5,90,112.5,112.5). All lengths are positive; the five P lengths
are pairwise distinct. H is absent from all P lengths. No native P or Q
side has length2u or2v. These are exact real-algebraic identities and strict
comparisons checked by
research/searches/contact-non-equiangular-octagon-one-deformation.py.

A legal finite patch contains Q, its halfturn Q0+Q1-Q across sideH, and
one P at each endpoint of that seam. Each P90 fills the complementary
90-sector between Q112.5 and Q157.5; its u/v legs match the outgoing whole
Q edges. The producer constructs both endpoint-fixed Pplacements, checks
uniqueness, all pairwise exact convex-clipping intersection areas zero,
and the far native contact endpoints. Thus the newly admitted mixed-Q
angle bypass is geometrically real locally. It does not prove a plane.

## Complete native and flat star census

The available native angles are P90,P112.5,Q112.5,Q135,Q157.5. In units
22.5 degrees their values are4,5,5,6,7. The producer enumerates every
nonnegative count tuple with total16(full) or8(one180 host). Full stars are

    2Q112.5+Q135,
    P112.5+Q112.5+Q135,
    2P112.5+Q135,
    P90+2Q135,
    P90+Q112.5+Q157.5,
    P90+P112.5+Q157.5,
    4P90.

The only flat star is host180+2P90. In particular a native112.5,135 or157.5
corner can never lie inside another native side; their remainders67.5,45,
22.5 are below the smallest native angle90. Flat HOSTS can be P OR Q here,
which is why the old equiangular-Q contact theorem cannot be imported.

Nevertheless this fixture excludes flat hosts on Q by its own lengths.
At a twoP90 flat cap, the guest perpendicular sides are acute legs u/v.
If these perpendicular sides had unequal lengths, the shorter far endpoint
would be P112.5 inside the longer side, forbidden by the native star census.
Thus perpendicular legs are equal, so the remaining along-host legs are
also equal (both guests have the same unordered leg pair{u,v}). For a Q
host, the guests' far P112.5 endpoints cannot be interior to the host edge;
nor can either Q native endpoint lie interior to a guest side, since all Q
angles exceed90 and are forbidden in flat stars. Therefore the guest far
endpoints reach the two native Q endpoints, and Q's native host length is
2u or2v. No native Q side has either length. Hence Q cannot host a flat
cap. Since no native Q corner can lie in ANY other side interior either,
every positive-length contact involving Q is whole on BOTH participating
native sides. This is proved anew for this fixed palette and metric.

PP flat hosts are not excluded or classified here. In particular the new
full star P90+P112.5+Q157.5 prevents importing the former palette's blanket
no-acute-adjacent-P-host argument. The global proof below needs only whole
contacts involving Q, and includes every permitted PP partial contact.

## Exact global obstruction

Every Q length-one side has135 at both endpoints. If it matched Q, the mate
would also be one of the five length-one135/135 sides. At each endpoint the
star must be Q135+Q135+P90 by the complete census. Every length-one native
Q side has at least one incident neighboring length-one side of its OWN
polygon: slots2,...,6 form a run of five ones. At that endpoint the P90
has an acute leg along the neighboring Q side. Whole contact would require
its length to be1, but its acute lengths are u,v, neither1. Hence no Q
length-one side can match Q. Each matches the sole P side of length1,
namely native x. Each P has only one such side, so uniform window contact
counts imply

    5q<=p+O(R).

Every P112.5 native corner lies in a full star containing Q135 or Q157.5.
A Q135 occurrence supports at most two P112.5 corners; Q157.5 supports at
most one. With six Q135 corners and one Q157.5 per Q, uniform corner counts
give

    4p<=13q+O(R).

Combining gives q=O(R), then p=O(R). Fixed positive areas and bounded
diameters require p+q>=cR^2-O(R) by plane coverage, contradiction.
All counts use fixed-width boundary-strip O(R) errors and do not assume
individual positive species frequencies. P-only omission is independently
impossible because its112.5 cannot complete using90/112.5; Q-only omission
is impossible because Q157.5 requires a P90 in its only full stars.

Thus this exact non-equiangular pair is UNTILEABLE despite its positive
four-tile seam patch and genuinely new full corner stars. Nothing is claimed
for the support-line family at other pivots, other P metrics or every
non-equiangular partner. In particular the pivot1/2 has length-one=2u and
admits the Q-hosted90/90 local branch excluded here; that is not covered.
