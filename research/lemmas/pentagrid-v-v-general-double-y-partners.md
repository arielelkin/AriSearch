# Every V-angle pentagon has a periodic V partner

**Status:** adversarially reviewed VALID in the [fresh independent review](../reviews/pentagrid-v-v-general-partner-review.md).
This generalizes the [mirror double-Y family](pentagrid-v-v-double-y-periodic.md)
to arbitrary asymmetric V metrics. It proves partner existence and an exact
four-parameter periodic continuum. It does not classify arbitrary V/V pairs,
prove that every tiling of these pairs is periodic, or resolve the original
two-unmarked-convex-polygon problem.

The [second fresh independent hostile review](../reviews/pentagrid-v-v-general-partner-fresh-review.md) also returns VALID for all parameter domains, reflections, dissection and plane coverage. Its quantifier audit confirms selected-partner existence and the explicit sufficient compatibility family only.

## The theorem and full positive cone

Put z=exp(pi*i/5) and phi=(1+sqrt(5))/2. Fix real parameters satisfying

    x>0, k>0, y>0,
    x+k/phi < f < phi*(x+k),
    y < x+f/phi.                                      (1)

Define

    r=phi*(x+f)-y,     e=f+phi*(x-y),
    l=phi*(x+k)-f,     m=phi*(f-x)-k.                  (2)

Let A and B have, respectively, native side lengths

    A: (x,r,y,e,f),       B: (k,f,l,m,x),

and the angle-after-side word (2,2,4,3,4)*pi/5. Then these are genuine
strictly convex polygons in two distinct congruence classes and admit a
periodic plane tiling with two copies of each per lattice fundamental cell.
All isometries and contacts are unrestricted. The construction itself uses
half-turns and translations and includes partial native-side contacts.

The cone (1) is exactly the positivity cone for the displayed dissection
with the chosen side roles. It is not a necessary condition for arbitrary
V/V tilability. The family has four free real parameters before overall
scaling.

**Universal partner consequence.** Given any genuine convex V-word pentagon
B with native lengths (b,d,c,h,j), the closure identities are

    d=phi*(b+j)-c,       h=phi*(d-j)-b.                (3)

For every 0<y<j+d/phi, it has a periodic V partner

    A_y=(j, phi*(j+d)-y, y, d+phi*(j-y), d).           (4)

The polygons A_y are pairwise noncongruent, and every A_y is noncongruent
to B. In particular y=j gives the mirror partner

    A_j=(j, phi*d+j/phi, j, d, d).                    (5)

Reflecting the native order of B gives the analogous mirror partner
(h,phi*d+h/phi,h,d,d). When h=j these partners coincide.
Thus arbitrary asymmetric V metrics, rather than only the previously
studied mirror subcone, have explicitly admitted periodic partners.

## Closure, positivity and strict convexity

The identities

    z^2=phi*z-1,    z^3=phi*(z-1),    z^4=z-phi

reduce the A edge closure

    x*z^4-r*z^2+y+e*z+f*z^3=0

to the two real relations for r,e in (2). The B closure

    -k-f*z^3+l*z+m*z^2+x*z^4=0

gives exactly the other two relations in (2). The real vectors 1,z are
linearly independent. Therefore these two real equations are also necessary
for any positive native walks in the prescribed directions. Equations (3)
are the B form with k=b,f=d,l=c,m=h,x=j.

The inequalities l>0 and m>0 are exactly the two f inequalities in (1).
The inequality e>0 is exactly y<x+f/phi. On that domain,

    r=(x/phi)+f+(x+f/phi-y)>f>0.

All remaining lengths are assumed positive. Conversely positivity of all
native sides forces every inequality in (1). This establishes the claimed
full cone, without assuming positivity of an auxiliary old parameter c.
For any B, equations (3) and c,h>0 give precisely these f inequalities;
then any y in the stated interval gives (4).

A's directed edge angles are (4,7,10,11,13)*pi/5 in increasing order, and
B's are (5,8,11,12,14)*pi/5. Each cyclic turn is strictly between0 andpi,
and the total turn is2pi. A closed positive edge walk with such strictly
increasing directions is strictly convex: from any edge, the successive
signed cross increments toward later vertices have a positive block,
possibly zero increments at an opposite direction, then a negative block.
The first is positive and the last negative. Closure makes their full sum
zero. Every intermediate partial sum is positive, either directly in the
positive block or as the negative of the remaining negative sum. Thus each
nonincident vertex lies strictly in the supporting left half-plane of every
edge. This proves global strict convexity and simplicity, rather than only
local turn signs. Both polygons have native corner angles
(144,72,72,144,108) degrees.

The native edge between the two72-degree corners is unique. Its length is
r in A and f in B, and r>f. Hence the shapes cannot be congruent under any
rotation or reflection. For distinct y, r changes strictly, so the partner
shapes in (4) are also pairwise noncongruent.

## Four exact polygons and their macro boundary

Define

    J=r*z^2-x*z^4,       J'=J+k,        H=J+J'=2J+k,
    beta=e+l=phi*(2x+k-y),
    gamma=m+r=2phi*f-k-y.

The native polygons in counterclockwise order are

    F0=A0=[J,r*z^2,0,y,y+e*z],
    F1=A1=H-A0,
    F2=B0=[J',J,y+e*z,y+beta*z,y+beta*z+m*z^2],
    F3=B1=H-B0.                                      (6)

The A and B closure relations imply exactly

    H=y+beta*z+gamma*z^2.

Both beta and gamma are positive sums of positive child sides. The macro
polygon is the centrally symmetric hexagon

    C=[0,y,y+beta*z,H,beta*z+gamma*z^2,gamma*z^2].      (7)

Its positive edge vectors are
(y,beta*z,gamma*z^2,-y,-beta*z,-gamma*z^2), with cyclic native angles
(72,144,144,72,144,144) degrees. The convexity argument above proves its
strict convexity. This definition provides exact coordinates in Q(z) over
whatever exact parameter field is used.

All five whole internal child-side pairings have reversed endpoints:

| Child side | Paired child side |
| --- | --- |
| F0 side0 | F3 side4 |
| F0 side4 | F2 side1 |
| F1 side0 | F2 side4 |
| F1 side4 | F3 side1 |
| F2 side0 | F3 side0 |

The remaining ten directed sides form the entire macro boundary:

| Macro side | Ordered child sides |
| --- | --- |
| 0 | (0,2) |
| 1 | (0,3),(2,2) |
| 2 | (2,3),(1,1) |
| 3 | (1,2) |
| 4 | (1,3),(3,2) |
| 5 | (3,3),(0,1) |

All20 native sides occur exactly once, in either an internal paired seam
or one exterior chain. Substitution in (6) checks each endpoint identity.
These facts hold as polynomial identities throughout the four-dimensional
cone; no embedding or containment assumption is used to derive them.

## Exact dissection by boundary winding

Let p avoid all finite child and macro boundaries. The reversed internal
seams cancel as oriented chains. The exterior chains concatenate to the
counterclockwise boundary of C. Therefore winding-number additivity gives

    sum_i winding(boundary(Fi),p)=winding(boundary(C),p).

For a counterclockwise strictly convex polygon its winding is1 inside and0
outside. Consequently

    sum_i 1_{p in interior(Fi)} = 1_{p in interior(C)}. (8)

This proves containment, interior disjointness and complete coverage at
once. Any overlap of two child interiors is open and would contain a point
avoiding the finitely many boundaries, contradicting (8). A child with an
interior point outside C would give the same contradiction there. Since a
convex polygon is the closure of its interior, every child is contained in
C. If an interior point of C were missing from the finite closed union of
the children, an open ball avoiding that union would contain a point off
all boundaries; this would contradict (8). Taking closure gives coverage
of all C. The boundary cancellation plus convexity thus proves the exact
dissection; equal total areas alone is not the argument.

The inner seam junctions J,J' have actual angles144+72+144=360 degrees.
The four boundary seam endpoints have angles72+108=180 degrees. These local
checks agree with the global winding proof but are not being used as a
substitute for global coverage.

## Infinite periodic plane and partial contacts

Put

    u=y+beta*z,         v=beta*z+gamma*z^2.

Their determinant is positive:

    cross(u,v)/sin(pi/5)=y*beta+phi*y*gamma+beta*gamma>0. (9)

The exact macro edge identifications are

| Side | Opposite side | Translation applied to opposite side |
| --- | --- | --- |
| 0 | 3 | -v |
| 1 | 4 | u-v |
| 2 | 5 | u |

Their ordered corner links are (0,4,2) and(1,5,3), each with angles
72+144+144=360 and accumulated integer lattice shift(0,0). The connected
oriented macro gluing is a compact flat surface, and its displayed map to
R^2/(Zu+Zv) is a local Euclidean isometry, including at both actual vertex
links. It is a finite covering: the image is nonempty, open and closed in
the connected torus; compactness and discrete fibers give evenly covered
neighborhoods. Direct shoelace computation gives

    area(C)=cross(u,v),

so the covering degree is1. Therefore the translates C+n*u+t*v tile the
whole plane with disjoint interiors. Retaining the exact four-child
dissection in each translate proves that

    {Fi+n*u+t*v : i=0,1,2,3; n,t integers}

is an admitted periodic two-class tiling. The finite macro identity extends
to the infinite plane by this exact covering proof, rather than an appeal
to finite patches or bounded search.

On macro side2 the native division lies at distance m from its initial
vertex, whereas on the neighboring macro side5 translated by u it lies
at distance r. They are generally different. Macro sides are still paired
in full and their interiors lie on opposite sides, so the resulting partial
contacts introduce no overlap. In particular the mirror-partner choice
(5) has r=phi*f+x/phi and m=phi*f-phi*x-k, hence
r-m=(2phi-1)*x+k>0. Thus this simplest universal partner family necessarily
evades saturation into full D-to-D octagon dimers.

## Exact computation, review, and scope

The [producer](../searches/pentagrid-v-v-general-double-y.py) checks native
walks, all reversed endpoints, all macro chains, the exact20-side accounting,
formal periods, determinant and shoelace equality as polynomial identities
in Q(z)[x,k,y,f]. It constructs the specific asymmetric fixture

    x=1,k=1,y=1/2,f=2,
    A=(1,3phi-1/2,1/2,2+phi/2,2),
    B=(1,2,2phi-2,phi-1,1).

The producer ran to completion with SageMath10.9 and Python3.12.13,
without solver, seed, symmetry reduction or timeout. The only finite domain
is the complete translation comparison set for this one fixed fixture;
all four formal parameters are checked symbolically. Its56 exact convex
clipping comparisons are derived from inverse-lattice coordinate
boxes for every ordered pair of the four motifs. It checks every integer
translation that can meet those boxes. This is a direct validation of a
fixed infinite periodic construction, not a bounded search for any period.
The [retained certificate](../certificates/pentagrid-v-v-general-double-y.json)
contains formal coordinate vectors and the complete fixture comparisons.
Normal invocation is nondestructive:

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-v-v-general-double-y.py

Saving a certificate requires explicit --output. The certificate and producer were independently checked through fresh native
walks, oriented edge cancellation and all56 separating-axis comparisons in
[the reviewer verifier](../reviews/verify_pentagrid_v_v_general_partner_independent.py).
The fresh review checks the full cone, winding argument, native angle
conventions, macro covering degree and universal-partner quantifiers.

This is an elementary constructive theorem, with no claimed literature
priority. It uses no monohedral classification. If the separately reviewed
Rao filter is imported, the mirror partner (5) is individually untileable:
its two repeated lengths are j and d, and d>j+b/phi>j. The proof of periodic
pair existence is independent of that observation. Partner existence for
every V does not exclude aperiodicity when that same V is paired with some
other unrelated shape. Arbitrary V/V metrics still require separate work.
