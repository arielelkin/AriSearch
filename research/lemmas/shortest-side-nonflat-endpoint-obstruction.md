# A shortest side with non-flat endpoints must match a whole equal-length side

Date: 2026-10-12. Status: [fresh hostile review VALID](../reviews/shortest-side-nonflat-endpoint-review.md).

Let a finite collection of fixed genuine compact convex polygon prototiles
have nonempty interiors, all isometries admitted and arbitrary partial side
contacts permitted. Call a native corner flat-eligible if its angle occurs
in any multiset of native corner angles whose total is pi, allowing repetitions.
For an admitted tiling this is a necessary condition for that native corner
to lie in the relative interior of another tile's side: the other tile
contributes pi and the remaining native sectors must sum to pi.

Suppose native side e of A has minimum length among ALL native sides of all
prototiles, and neither endpoint corner of e is flat-eligible. Then every A
tile in any admitted tiling must have a whole-side match along e with a native
side of exactly the same length. Thus if all such endpoint correspondences
are forbidden, no A copy can occur in any admitted tiling. For a two-species
pair, if B also cannot tile alone, the pair is untileable.

## Local proof including arbitrary partial contacts

Local finiteness follows from fixed positive inscribed disks and bounded
tile diameters. Across the relative interior of e, neighboring tiles supply
finitely many positive contact intervals covering e. Each interval lies
on one native side f of a neighbor: convexity prevents a genuine polygon
from having several distinct collinear sides on the same supporting line.

If f extended beyond either endpoint of e, that A endpoint would lie in
the relative interior of f, making its corner flat-eligible, a contradiction.
Consequently every f with positive overlap is contained entirely in e.
But |f|>=|e| by minimality, so containment forces |f|=|e| and f=e as
geometric segments. Thus the neighbor supplies a whole-side match. There
cannot be another positive interval except the same matched tile; the two
convex interiors occupy opposite half-planes along the common side.
All equal-length native partner types and both endpoint orders must be
checked before concluding no A is admitted. QED.

Two flat pi sectors cannot accompany a native positive corner, so the
flat-eligibility test above misses no possible endpoint-on-side vertex.
The result assumes neither edge-to-edge tiling nor a frequency limit;
it proves the particular side is forced edge-to-edge locally.

## Exact current construction application

The current words are A=(65,140.5,147.5,75,112) and
B=(40,144.5,136,47,172.5) degrees. Their only native angle multiset
summing to180 is(A65,A75,B40). The endpoints of A1 are140.5 and147.5,
so neither is flat-eligible. On the exact local-module samples A1=1/10
is strictly shorter than every other native side of A or B. Its only
equal-length partner is another A1. A reflected match fails at the
140.5/140.5 endpoint: its remaining79-degree sector cannot be filled
(minimum native angle40 and no native79). A half-turn match has endpoint
sum288, leaving72, again smaller than two minimum native angles and
unequal to any one native angle. Thus no A copy can occur.

Pure B full stars consist only of nine40-degree corners; its native144.5
corner cannot occur in any pure full or flat star. Hence B cannot tile
alone. The two-species sample is untileable even though an exact four-tile
partial-contact module is geometrically valid. This local argument is
stronger than the separately reviewed hosted-contact capacity argument on
those samples, but it does not replace that general resource theorem.

Relaxing the shortest-side inequalities or adding another equal-length
partner with compatible endpoint stars changes an actual hypothesis.
The broader parametric family is not excluded by this lemma unless its
metric falls in the stated minimum-side locus.
