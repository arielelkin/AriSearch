# A periodic mirror-V/equiangular-W continuum

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/pentagrid-v-w-periodic-continuum-review.md) is VALID for every real b,c>0. The [independent verifier](../reviews/verify_pentagrid_v_w_periodic_continuum.py) checks all formal identities and the32-overlap irrational fixture by exact clipping. This is a periodic escape family, not a classification of every
V/W metric pair or a solution of the original aperiodicity problem.

## Exact two-parameter statement

Let z=exp(pi*i/5) and phi=(1+sqrt(5))/2=z+z^(-1). For any real
parameters b>0,c>0 put

    E=phi*(b+c),
    D=2*phi*b+phi^2*c = phi*E+b/phi,
    H=2*b+phi^2*c    = phi*E-b/phi.

Define V by cyclic native side lengths (b,D,b,E,E), with angles after
those sides (2,2,4,3,4)*pi/5. Define W by lengths (b,H,b,E,E), with
all five angles3*pi/5. The theorem is that V and W admit a whole-plane
tiling with two independent translation periods. No marking or matching
rule is added to either polygon. Every tile in this witness is an
orientation-preserving isometric copy; the original convention allowing
reflections and arbitrary partial contacts therefore also admits it.

Both shapes are genuine convex pentagons, and their angle multisets
make them noncongruent. In particular this gives periodic partners for
EVERY b>0,c>0 member of the mirror-V family previously used in the
area-compatible U/V mechanism. This claim does not apply to every
asymmetric V metric.

## Dimer and exact polygons

Construct an octagon Q with counterclockwise vertices

    q0=0,
    q1=b,
    q2=b+E*z,
    q3=b+E*(z+z^3),
    q4=D*z^2,
    q5=q4-b,
    q6=q4-q2,
    q7=q4-q3.

Its eight directed side vectors are

    b, E*z, E*z^3, b*z^4,
    b*z^5, E*z^6, E*z^8, b*z^9.

They close exactly; use1+z^4=z^2/phi and z+z^3=phi*z^2.
Q has vertex angles (4,4,3,4,4,4,3,4)*pi/5. It is centrally
symmetric under p -> q4-p. The diagonal [q0,q4] has length D;
its two halves are congruent pentagons. Give the first half the native
V vertex order

    V=[q3,q4,q0,q1,q2].                                 (1)

This has side lengths(b,D,b,E,E) and angles after its sides
(2,2,4,3,4)*pi/5. Its half-turn q4-V is the other half. Thus this is
precisely a mirror-V dimer across the72-to72 D side; no implication
from mere dimer convexity to plane extension is assumed.

Define the reference equiangular W vertices by

    w0=0,
    w1=b,
    w2=b+H*z^2,
    w3=phi*E*z^2,
    w4=phi*E*z^2+E*z^6.                                (2)

The sides are b,H*z^2,b*z^4,E*z^6,E*z^8. Closure follows from
b*(1+z^4)=b*z^2/phi and z^6+z^8=-phi*z^2. Every listed length is
positive. All successive exterior turns of V, W and Q lie strictly
between0 andpi, with total2pi. The closed direction-ordered chains are
genuine convex polygons: relative to any side, subsequent signed height
increments first have one positive sine arc, then one negative sine arc.
They return to0 only at closure, and positivity of the edge lengths
makes every nonincident vertex's height strictly positive. This checks
global support, not only local turning. The supplied fixture producer
also checks every strict support inequality directly.

## Four native motifs and ten complete seams

Put

    u=2*b+E*z-D*z^2,
    v=2*phi*E*z^2.

The four motifs, all counterclockwise and in their native reference
vertex orders, are

    F0=V,
    F1=q4-V,
    F2=b-W,
    F3=q5+W.                                           (3)

For all integer n,m take the copies Fi+n*u+m*v. A seam row
(i,a,j,d,n,m) means exact reversed endpoint equalities

    Fi[a]=Fj[d+1]+n*u+m*v,
    Fi[a+1]=Fj[d]+n*u+m*v,

with native indices modulo5. Every motif side occurs exactly once:

| i,a | j,d | n,m |
| --- | --- | --- |
| 0,1 | 1,1 | 0,0 |
| 0,2 | 2,0 | 0,0 |
| 0,3 | 1,3 | 1,0 |
| 0,4 | 3,4 | 1,0 |
| 0,0 | 2,2 | 0,1 |
| 1,2 | 3,0 | 0,0 |
| 1,4 | 2,4 | -1,0 |
| 1,0 | 3,2 | 0,-1 |
| 2,1 | 3,1 | 0,-1 |
| 2,3 | 3,3 | 1,-1 |

The first row is the D-to-D V dimer seam. Each equality is linear in
b,c with exact coefficients in Q(z), so its complete formal verification
uses the two coefficient vectors (b,c)=(1,0),(0,1); these probes are
algebraic coefficient checks, not asserted positive metric examples.

The side involution and the successor within each face produce the
actual circular corner permutation. Its six links have four angle
multisets(3,3,4) and two(2,2,3,3), all summing to10*pi/5. The two latter
links correspond to the two endpoints of the V dimer seam. The ordered
links, and not merely corner union classes, are retained in the
certificate. Face adjacency is connected; thus the quotient is a compact
connected oriented surface with6vertices-10edges+4faces=0. Every edge
has two half-disks, every vertex has a single circle link, and the vertex
sectors occur in the direction order given by the reversed seam maps.

## Area and whole-plane coverage

Normalize signed areas and crosses by sin(pi/5)>0. Exact quadratic
identities give

    area(V)/sin(pi/5)
      =(3phi+2)*b^2+(4phi+2)*b*c+(phi+1/2)*c^2,
    area(W)/sin(pi/5)
      =(3phi+1)*b^2+(4phi+2)*b*c+(phi+1/2)*c^2,
    cross(u,v)/sin(pi/5)
      =2*phi*E*(2phi*b+E)
      =2*phi^3*(b+c)*(3b+c)>0.

Consequently u,v are independent and

    2area(V)+2area(W)=cross(u,v).                       (4)

The certificate checks all coefficients of these identities via the
three quadratic probes (1,0),(0,1),(1,1), and verifies that the two V
areas sum to the exact octagon area.

Let Lambda=Z*u+Z*v. Map the abstract polygon quotient to the ordinary
flat torus R^2/Lambda through motifs(3). The seam equations make the
map continuous. It is an orientation-preserving local Euclidean
isometry in face interiors, across edges (the reversed directed side
puts faces on opposite support half-planes), and at vertices. At a
vertex the single ordered circular link consists of positive corner
sectors with total2pi, so it maps one neighborhood to a Euclidean disk
without folding or overlap.

This local homeomorphism from a compact connected surface is a finite
cover of the target torus: the image is nonempty, open, and compact
hence closed; local injectivity and compactness give finite fibers and
an evenly covered neighborhood of each target point. Its covering
degree d is a positive integer and local area preservation makes source
area equal d times target area. Equation(4) gives d=1. Thus the four
quotient faces cover once and have disjoint interiors. Their Lambda
lifts are exactly the motifs(3) and all integer translations, proving
the stated full-plane periodic tiling.

This whole-family proof uses the formal seam, ordered-link, positivity,
and area identities. It does not extrapolate plane coverage from a
finite patch or finitely many parameter samples.

## Exact algebraic fixture and finite source search

Take b=1,c=sqrt(2), with c the positive root of t^2-2 in(7/5,3/2).
The producer independently computes every motif's lattice coordinates.
For each of the16 ordered motif pairs it derives the complete integer
translation bounding box that could yield overlap, and checks all
resulting32 nontrivial comparisons by exact separating axes. All have
disjoint interiors, and the summed exact areas equal the positive
covolume. Root-isolated algebraic coordinates and the entire comparison
list are retained. This fixture uses a parameter ratio outside Q(sqrt(5));
that is an additional exact example, not a hypothesis of the theorem.

The fixed pairing was first found by a prescribed dimer ansatz search:
one Q octagon and two congruent W faces, arbitrary full-edge pairings,
positive metric closure, and both relative W parities. The matching
search stopped at the first witness after6258 recursive pair branches
and151 complete angular matchings. It did NOT exhaust the full matching
domain and does not classify all V/W tori. Its separate retained record
is `research/certificates/pentagrid-v-w-dimer-torus.json`.

Family replay:

```text
conda run --no-capture-output -n arisearch python research/searches/pentagrid-v-w-periodic-continuum.py
```

Certificate:
`research/certificates/pentagrid-v-w-periodic-continuum.json`.

## Scope and review obligations

This kills strong aperiodicity for the displayed V/W metric continuum
because one admitted doubly periodic tiling exists. It says nothing about
universality or classification of other tilings, and does not rule out
other V/W metrics, U/V, or V/V as possible routes. No theorem about mono
omission is needed to obtain the periodic escape. No novelty claim is
made.

A fresh reviewer should independently verify the explicit native side
indices, complete formal seam identities, ordered vertex links, strict
convexity for the entire parameter domain, area coefficients, degree-one
coverage step, and the fixture's complete overlap domain. In particular
Q dimer convexity alone is not the global argument.
