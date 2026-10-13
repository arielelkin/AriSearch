# Track A edge diamonds and one kink repair: independent hostile review

Date: 2026-10-13. Reviewer did not develop the surgery or repair. Domain: one
required H/P1 seam at J=1/2+(4/5)w and its one prescribed epsilon=1/1000 kink.
No centroid tuning, congruence census or enlarged source atlas was performed.
The unrestricted problem is unchanged and B5+1 remains paused.

## Exact claims and assumptions

Import the independently reviewed existence and convexity of the H/P1/P2
source at this J, with full-edge contacts and the required K-type H-J' star.
Pairing P1/P2 c partners gives the nonconvex H/D precursor. The changed surgery
returns to the original source edges and pairs the two centroid fan triangles
at each edge into Q_e. Claims audited: a globally compatible infinite finite-
prototile polygonal covering; new third-face incidence at formerly degree-two
H-J'; the <=4-corner obstruction; one exact convex local diamond and periodic
omission escape; and the repaired full-plane covering with a nonconvex losing
face. Exact coordinates and isometries are in the
[construction record](../searches/construction-cycle-a-edge-diamonds.md).

## Analytic infinite-covering and incidence audit

The arithmetic vertex mean of each strictly convex source polygon is interior:
for any supporting edge line, every source vertex lies on its closed interior
side and at least one lies strictly inside, so their positive average does too.
Fans from this interior point partition the polygon. Every original source
edge belongs to exactly two source polygons, so pairing their assigned fan
triangles covers the entire plane with disjoint interiors. The two triangles
are on opposite sides of a full edge and have interior apexes, hence their
union is a simple quadrilateral support (possibly with a flat or reflex
boundary vertex), bounded by two source diameters. Neighboring choices cannot
conflict because every fan triangle is assigned to exactly one edge pair.
The construction uses only a bounded radius and no unproved source atlas
beyond imported full-edge existence. Finite native side choices, source shape
choices and endpoint assignments give finitely many support classes. This
proves finite-prototile polygonal covering, NOT two convex shape classes.

At the forced H-J' K-star, the source H/P1/P2 faces give three edges, hence three
resulting diamond faces separated by the centroid spokes. The original H/D
macro had just two faces there. Diamonds across H/P source edges contain a
positive-area piece from each side of the old H/D boundary. These are actual
changed incidences and boundary-crossing faces; the old incidence-preserving
obstruction does not automatically apply. The new obstruction does: every
diamond has at most four genuine corners. If all final shapes were convex
and exactly two classes, their periodic monohedral tilings would defeat the
aimed aperiodicity immediately, irrespective of any decoder.

## Independently checked exact local evidence

[Independent checker](check_construction_cycle_a_independent.py), with no
construction-author imports, embeds Q(w) in the real algebraic plane using
w=exp(i*pi/5) and checks Euclidean determinants exactly. Its
[retained result](construction-cycle-a-independent-check.json) gives field
coefficient vectors for the vertices and kink. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_construction_cycle_a_independent.py

Default execution is read-only; --output may target disposable evidence.
The independent audit confirms g(z)=(J'/K)z has unit multiplier, matches K to
J' and 0 to 0, and puts the H and P1 centroids on opposite sides of that seam.
Q=(0,g(c_P1),J',c_H) has all four strictly positive native turns. Gluing Q to
its half-turn about the midpoint of side0 gives a convex centrally symmetric
six-corner carrier of twice Q's area; the independently computed convex hull
has exactly that area. Thus the local example itself has a periodic omission
tiling by the elementary central-hexagon opposite-side construction.

The author's stronger general quadrilateral formula was checked separately:
for Q=(A,B,C,D), Q*=A+B-Q, t1=C-A, t2=D-B, the four edges of Q have exactly
reversed counterparts in Q* shifted by 0,t1,t1+t2,t2. The determinant is
2*area(Q)>0. Consequently the distributional derivative of the periodic
multiplicity function is zero: every directed edge measure cancels. The
function is constant almost everywhere and its mean is one by covolume.
Local finiteness and closed tiles imply boundary coverage. Hence these copies
form a full-plane tiling with both nonzero independent periods. This does not
rely on a rendered patch or a bounded periodic-witness search.

## One repair: defect found and independently rechecked

A preliminary coordinate paragraph used U=c_H,V=J' with the right normal,
while Q's positive boundary runs J' to c_H. The reviewer identified that the
stated direction removed area from Q instead of enlarging it. The author
corrected the orientation before final evidence: U=J',V=c_H, then
M=(U+V)/2-(1/1000)(w-conjugate(w))(V-U). This is the SAME intended outward
kink mechanism and its one allowed repair, not another surgery or enlarged
parameter search. The corrected proposal was independently recomputed.

M lies strictly inside the adjacent H fan triangle (J',1,c_H). The enlarged
Q=(0,g(c_P1),J',M,c_H) has five strictly positive turns. The losing local
fan boundary (J',1,c_H,M) has a strictly negative turn at M. Exact area
conservation holds. Although a complete losing diamond contains a second
source fan triangle, that triangle is away from M, so the negative turn
persists in the complete face. The point M lies on an interface with only
two incident faces. Their angles sum 2pi; if both are convex, both are pi.
Thus ANY admissible nonzero kink creating a convex corner on one side creates
a reflex corner on the other. This uniform obstruction is analytic; global
compatibility evidence is for the one fixed epsilon, not a claimed full
parameter classification.

Applying the cap at each source H-J' is globally compatible: it lies in that
H's side1 fan, there is only one cap per H, and distinct source H interiors
are disjoint. H side0 and side1 at the K-star meet P1 and P2, respectively,
so affected diamonds cannot receive a competing request from another H.
Transporting the cap by the source placing isometry also handles reflected
source copies. The plane is still covered without gaps or overlaps; its
losing faces are nonconvex. No extra two-shape or convex-covering claim survives.

## Universal forcing attack and final verdict

The forward source rule is not an intrinsic inverse on arbitrary final
tilings. Original source full-edge restrictions cannot be transferred to
unmarked final tilings, and no exclusion of final partial contacts is proved.
Reflection allowance cannot eliminate the explicit half-turn omission escape.
The escape has two independent periods, so already defeats single-direction
period exclusion. Any proposed uniform decoder would therefore contradict
an admitted periodic omission tiling if applied to a convex two-class output.

VALID: exact changed-incidence finite-prototile infinite polygonal covering;
<=4-corner obstruction to an aperiodic convex two-class output; exact local
convex crossed diamond and periodic omission; fixed repaired polygonal
covering and local/global nonconvexity obstruction.
INVALID: this surgery or its one kink repair as an aperiodic pair of convex
polygons. UNRESOLVED (not pursued after the gate failed): the global diamond
convexity census, congruence-class count and intrinsic recognition. These are
not needed to certify this proposal's failure. No global impossibility or
novelty claim is made.

Next obligation: propose a different exact branching network with at least five
genuine corners on every complete face, and establish globally compatible
infinite covering before metric/congruence searches. A new vertex created
only on a two-face interface cannot meet that obligation while preserving
convexity on both sides. Arbitrary final tilings still require a canonical
translation-equivariant decoder, with reflections, partial contacts and
omission explicitly addressed.
