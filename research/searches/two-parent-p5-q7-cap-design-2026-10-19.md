# One two-parent incidence design cycle: saturated dual caps

Date: 2026-10-19. Status: **Falsified design / blocked construction route**;
[independent Sol hostile review](../reviews/two-parent-p5-q7-cap-design-hostile-review-2026-10-19.md) PASS. No substitution, coordinates, plane tiling, or
aperiodicity is claimed. This is the single cycle requested by the 19:22
assessment Priority 2. No larger inventories or topology enumeration were run.

## Target and chosen incidence mechanism

Columns of M=[[7,5],[2,3]] specify a P5 parent containing 7P+2Q and
a Q7 parent containing 5P+3Q. The characteristic polynomial is
mu^2-10mu+11, so mu=5+sqrt(14), lambda=sqrt(mu), and
area(Q)/area(P)=(sqrt(14)-2)/2. The conjugate is positive.

Choose the saturated defect allocations P:(B,J,D,H)=(4,0,0,0),
Q:(3,0,0,0). These satisfy exactly B+2J+2D+H=4 and 3.
Each outer child has one connected positive boundary arc, with no repeated
child label on the boundary cycle. All internal seam vertices are trivalent,
and every incidence is native. The corresponding simple dual is a
triangulated disk with four (respectively three) boundary vertices and five
interior vertices. This is an explicit choice, not a claim these are the
only possible allocations or contact patterns.

The complete fixed maps, including every seam endpoint, intended species,
native-side counts, and ordered parent boundary words, are in the adjacent
JSON. They are combinatorial disk maps with the intended face *labels*, but
fail the native-side requirement: they are not P5/Q7 dissection maps.
The adjacent Python file deterministically constructs and checks just these
two maps. No solver or coordinate search is used.

## Exact encoding of the attempted maps

Five interior children are a,b,c,d,e, all intended P. Both caps have the
following five interior dual triangles (one primal internal vertex per
triangle): abe,bce,cae,bdc,dac. The outer face of this core is abd;
c and e are enclosed by it. Its edge graph is K5 minus de.

For P, the four outer children in cyclic order are u0=P,u1=Q,u2=Q,u3=P.
The annular dual triangles are abu1,bu2u1,bdu2,du3u2,du0u3,dau0,au1u0.
For Q the three outer children are all Q; its annular triangles are
abu1,bu2u1,bdu2,du0u2,dau0,au1u0.
These lists specify every internal primal vertex and its three incident
children. Each dual edge xy is the unique primal seam between x and y;
its endpoints are its two incident triangles. For a boundary dual edge
ui,u(i+1), its second endpoint is the parent-side seam node si. The JSON
lists these endpoints explicitly: 20 seams for P and 18 for Q.

Parent corners pi are ordered counterclockwise, and si are the active
boundary seam nodes. Each following word is an entire outer child arc;
concatenating them in the listed order gives the full parent boundary:

P:
- u0: s3,s0
- u1: s0,p0,p1,s1
- u2: s1,p2,p3,s2
- u3: s2,p4,s3

Q:
- u0: s2,p0,p1,p2,s0
- u1: s0,p3,p4,s1
- u2: s1,p5,p6,s2

Every consecutive pair is one complete child native edge in this attempted
H=0 design. Parent sides are the paths between consecutive pi, including
the intermediate si where present. Thus these words also specify the ordered
boundary length sums, before any child side-role assignment.

## Exact failure and stronger cap obstruction

In the P map the native side counts are
(a,b,c,d,e;u0,u1,u2,u3)=(6,6,4,6,3;5,7,7,5).
In the Q map they are (6,6,4,5,3;8,7,7).
In particular e is triangular in both maps, while its intended species is P5.
No suppressed or inserted straight incidence is available: H=0. Adding two
native corners along its three sides would introduce forbidden flat corners,
contrary to strict convexity, rather than repair this map.

The failure is stronger than these particular annuli. For *any* simple
triangulated dual cap with these boundary sizes and five interior children,
all five interior child vertices must have degree at least five. Write eII
for edges between interior vertices, eIB for cross edges, and eBB for
boundary-boundary edges. P has 20 dual edges and eBB>=4; Q has 18 and eBB>=3.
Thus

    25 <= 2eII+eIB = eII+(E-eBB).

For Q this gives eII>=10, whereas a simple planar graph on five vertices has
at most 9 edges. For P it gives eII>=9, forcing equality and a maximal planar
induced graph on the five interior vertices. Its outer face is a triangle;
at least two of its vertices lie strictly inside that triangle in the disk
embedding. They cannot join any boundary child without crossing the triangle.
Their entire degree is at most four (there are only four other interior
vertices), contradicting the required degree at least five. Hence neither
saturated cap can supply the target native polygons, under the stated cap
assumptions. This argument allows any assignment of the two heptagons:
putting them inside only strengthens the degree requirement.

## Angle and metric gate status

For valid maps the common angle variables would be P angles alpha_0..alpha_4
and Q angles beta_0..beta_6, with sums 3pi and 5pi and each in (0,pi).
Each interior triangle imposes the sum of its three assigned angles=2pi;
each si imposes two assigned angles summing to pi; each pi equates its
single child corner to the corresponding parent angle. Reflections reverse
cyclic role assignments and are permitted. The native-role assignment already
fails: e has three corner slots for five P roles, with no straight incidences.
Its geometric triangle angle sum pi cannot supply a strictly convex pentagon
with all five native roles and angle sum 3pi at these incidences. Thus the
simultaneous angle/native-incidence gate is empty. The global summed-angle
identities alone are satisfied (31pi for P,30pi for Q); they miss this local
failure and must not be mistaken for compatibility.

For completeness, the later boundary equations would read
lambda*l_X,j = sum(l_child,role) along each ordered pi-to-p(i+1) word,
with common lambda=sqrt(5+sqrt(14)) and all twelve native side lengths >0.
Internal seams would equate the corresponding child lengths. There is no
valid assignment of native roles on which to instantiate this system;
positive metric, nonlinear coordinates, omission screens, and intrinsic
recognition therefore have no surviving candidate to test. No claim about
metric infeasibility for other maps is made.

## Stop and restart condition

Stop this seed's one design cycle at the topology gate. The precise missing
step is a pair of native P5/Q7 disk maps outside this saturated, single-arc,
trivalent cap mechanism: they must use another allowed defect allocation or
another boundary contact structure, and still satisfy the tiny defect budgets.
No such new incidence mechanism is supplied here, so section 5 blocks further
coordinate solves, larger counts, and blind map enumeration. This is a
restricted obstruction, not an impossibility theorem for M or for convex pairs.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-parent-p5-q7-cap-design-2026-10-19.py

Dependencies: research/lemmas/six-child-topology-substitution-consequences.md
and its seam-count conventions; research/searches/progress-assessment-2026-10-19-1922.md.
