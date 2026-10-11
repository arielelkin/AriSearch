# Canonical four-pentagon clusters for a one-shared-arm exceptional pair

**Status:** freshly independently hostile-reviewed **VALID** as a conditional
geometric reduction; see [review](../reviews/partial-contact-cairo-single-shared-fourfold-clusters-review.md). It proves an equivalence of tiling problems for an exact
pair, not existence or absence of either tiling, and no aperiodicity claim.

## Exact pair and event inventory

Let w=sqrt3 and r=4/5,t=6/5. Use the internally distinct Cairo pentagons

    P=(1,r,(3w-r)/2,(wr-1)/2,2),
    Q=((wt-1)/2,(3w-t)/2,t,1,2).

Their sole cross arm equality is Pa=Qd=1. Their equal-perpendicular
right-corner events have total bank sums

    2Pa=2Qd=Pb+Qc=2,
    2Pb,2Pc,2Pd,2Qa,2Qb,2Qc.

The six latter values are mutually distinct and all differ from2. Thus
only the event class of total2 contains different native bank lengths.
The reviewed two-T switch theorem permits unequal opposing arms only
within the bank set{1,r,t}; all other arm rays are whole native matches.
Both e sides have length2, so they cannot host a T with any other event.
The exact arithmetic is independently replayable in the
[single-shared checker](../searches/partial-contact-cairo-single-shared-exception.py).

## Forced clusters in any hypothetical unrestricted tiling

The native Pc and Pd arms are globally private, cannot face an e-hosted
fragment, and cannot participate in an unequal arm switch. Every one is
therefore a whole native seam with the same slot of another P. Angle types
90 and120 differ, so its physical mate preserves the native endpoints and
is the reflection across the seam line. The same holds for the globally
private Qa and Qb arms.

At a P corner3 between c and d, the two90 sectors across either seam cannot
form a T: their banks d,d or c,c would have a singleton event total2d or2c.
An e host is excluded by e=2; an arm host would force another switch with
the same total but a different bank length, absent from that singleton
class. Hence this corner is a four90 star. Reflection across the two
perpendicular native c and d seam lines generates precisely four P copies,
all sharing this corner. Their interiors occupy its four quadrants.
Similarly each Q corner1 between its private a and b sides is the center
of precisely four reflected Q copies.

Every P belongs to its unique cluster centered at its own native corner3;
all four constituent copies have that same corner. Every Q belongs to the
analogous unique corner1 cluster. These clusters partition the original
tiles and have pairwise disjoint interiors. Their union therefore covers
the plane in any hypothetical original tiling. No assumptions about the
other contacts, orientations or species frequencies were used.

## Exact cluster shape

Choose perpendicular axes at angles60 and150 degrees for a P cluster,
with its common right-angle corner as origin. A constituent P occupies one
quadrant. After reflecting to the first quadrant, its vertices are

    (0,0), (d_r,0), (d_r+1,w),
    (d_r+1/2,3w/2), (0,c_r),

where

    d_r=(wr-1)/2,  c_r=(3w-r)/2.

Reflect this pentagon in both coordinate axes to obtain the whole cluster
S(r). It is a genuine nonconvex12-gon with four convex90 corners, four
convex120 corners and four reflex240 corners. Its native external edge
lengths are four copies each of1,2,r. Its area is4area(P).

Rotate a Q cluster by60 degrees. The same axis calculation gives exactly
S(t), with

    d_t=(wt-1)/2=Qa,  c_t=(3w-t)/2=Qb.

Its external edge lengths are four copies each of1,2,t, and its area is
4area(Q). This is a geometric identity, not merely an equality of angle
words or areas. The Q/P rotation comparison is only a reference choice;
actual clusters retain every isometry allowed by the original problem.

## Tiling equivalence and periods

Any original P,Q tiling gives, by the forced canonical partition, a tiling
by the unmarked nonconvex shapes S(r),S(t). Conversely any unrestricted
tiling by S(r),S(t) can be subdivided into their displayed four constituent
P or Q copies. The resulting tiling is admitted by the original convex pair:
no extra boundary matching requirement is imposed because arbitrary
contacts are allowed. Thus existence of the two tiling problems is
equivalent.

Any translational period of a macrotiling preserves this fixed reflected
subdivision: the axes and four quadrant faces are intrinsic to each
cluster, and its reflection symmetries permute them. In particular the four
convex90 corners form a non-square rectangle at(plus/minus wr/2,plus/minus
3w/2), whose center and axis directions determine the four quadrant pieces.
The same holds with t for the other shape. It therefore gives a
period of the original tiling. Conversely a period of the original tiling
preserves species (P,Q are noncongruent), private native corners and their
canonical clusters, and hence preserves the macrotiling. The exact pair
therefore also preserves the presence or absence of a nonzero translation
in each corresponding tiling. This does not establish that either tiling
problem is nonempty or aperiodic.

## Scope

The reduction is retained at the exact r=4/5 fixture. The same geometric
formula holds symbolically for1/w<r<2-1/w, but the forced-cluster proof must
recheck its private arm and singleton event assertions when r changes.
Further exact equalities can occur on exceptional values and are not
silently included in the theorem. This is a new finite geometric
reformulation of an open exceptional-metric contact mechanism, not a
bounded failure-to-find claim or a replacement for global extension.
