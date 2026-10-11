# Exact metric classification of the two-private-side octagon family

**Status:** adversarially reviewed and exactly certified;
[fresh independent hostile review](../reviews/regular-pentagon-private-octagon-geometry-review.md) is valid. This is a restricted
classification, not a solution of the unrestricted main problem.

## Statement and exact two octagons

Let P be the regular unit pentagon and Q satisfy the hypotheses of
[the private-octagon periodicity theorem](regular-pentagon-private-octagon-periodicity.md):
Q is a genuine convex octagon with two nonadjacent108-degree corners,
six144-degree corners, exactly six unit sides, and two distinct positive
nonunit sides. Then {P,Q} tiles the plane **if and only if** Q is congruent
to the octagon Q3 defined below. Every admitted tiling has a nonzero period
by that periodicity theorem. Q3 also has the explicit doubly periodic
six-tile witness below. All isometries and unrestricted original contacts
remain permitted.

Identify the plane with C. Let z be the root of

    z^4-z^3+z^2-z+1=0,
    4/5<Re(z)<9/10,  1/2<Im(z)<3/5.

These conditions select z=exp(i*pi/5) uniquely. Put

    phi=(1+sqrt(5))/2,  s=sin(pi/5)>0.

Equivalently Re(z)=phi/2 and s=Im(z), so all coordinates are exactly
algebraic. P has successive unit side vectors1,z^2,z^4,z^6,z^8, starting
at0. For d in {2,3}, set

    k_j=j+1[j>=d],                    j=0,...,7,
    v_0=0,  v_(j+1)=v_j+l_j*z^k_j.

For Q2 use d=2, l_0=sqrt(5), l_2=(5-sqrt(5))/2, and all other l_j=1.
For Q3 use d=3, l_0=2, l_3=phi, and all other l_j=1. In both cases
v_8=v_0, and the vertex lists(v_0,...,v_7) define genuine convex octagons.
The angles at0 and d are108 degrees and all other angles144 degrees.

Positive closed side chains with these cyclic directions are strictly
convex: for any fixed side, perpendicular vertex heights first increase
through the subsequent open semicircle of directions and then decrease
to0 at closure. All nonincident vertices have positive height. The exact
producer additionally checks every strict supporting-side inequality.

## Complete closure classification

In any admitted tiling, reviewed all-obtuse forcing gives full native-side
contacts and only alpha,alpha,beta stars. Each private side must match the
same unique native side of another Q. Nonadjacent alpha corners exclude
alpha/alpha sides; a beta/beta side would match beta/beta and violate the
star language. Thus each private side is alpha/beta with reversed endpoint
correspondence. Both private sides cannot meet the same alpha corner:
their two neighbors would then both contribute beta there. Consequently
exactly one private side is incident to each alpha corner.

Normalize the smaller alpha separation to d in {2,3,4}; reflection and
rotation permit this. Set alpha corners0,d and start side0 in direction1.
The private side indices are i in {7,0}, j in {d-1,d}: exactly12 cases.
All other sides are unit, so closure is the two-real-equation system

    (l_i-1)*z^k_i+(l_j-1)*z^k_j = z^d+z^9.             (1)

The right side comes from the two omitted directions of the ten-root orbit.
Its exact solutions are:

| d | Private sides | Private lengths or obstruction |
| --- | --- | --- |
|2|7,1|(5-sqrt(5))/2, sqrt(5)|
|2|7,2|parallel directions; inconsistent closure|
|2|0,1|phi, phi|
|2|0,2|sqrt(5), (5-sqrt(5))/2|
|3|7,2|phi,2|
|3|7,3|0,0|
|3|0,2|(5-sqrt(5))/2, (5-sqrt(5))/2|
|3|0,3|2,phi|
|4|7,3|parallel directions; private lengths equal|
|4|7,4|1,1|
|4|0,3|1,1|
|4|0,4|parallel directions; private lengths equal|

Each nonparallel row follows by the unique2-by-2 real solve in(1).
In parallel d=4 rows the right side is0 and the private directions are
opposite, forcing equal lengths. The parallel d=2 row has its right side
not parallel to its private directions. Only four rows meet positivity,
nonunitness, and distinctness. Reflection of corner indices k->d-k sends
outgoing sides0,d to incoming sides d-1,7 and interchanges their lengths.
Thus every possibly tileable Q is congruent to Q2 or Q3. No free metric
parameter remains in this specified family.

## Why Q2 is untileable: the complete third-neighbor domain

Suppose {P,Q2} tiles. The reviewed
[octagon chain-limit theorem](obtuse-pentagon-octagon-chain-limit.md)
supplies an admitted good tiling where every Q has P on all six unit sides,
and every P has exactly three Q neighbors and two nonadjacent P neighbors.
This invocation is necessary here: those statements need not hold in every
original tiling, although its private chains still have parallel axes.

Use the reference Q2 above, private midpoints a,b on sides0,2, and
H_b(v)=2b-v. The required P across Q2 side1 has vertices

    p_0=v_2,
    p_k=v_2-(v_2-v_1)*sum_(r=0)^(k-1) z^(2r), k=1,...,4.

Its side0 matches Q2 side1. Its side4 matches H_b(Q2) side3 exactly,
as verified by the retained endpoint equalities. These are consecutive
Q-neighbor sides4,0. The third Q neighbor must occupy side2: choosing
side1 or3 instead would leave adjacent P-neighbor positions. At either
endpoint of side2, its other neighbor is P, so this new Q side must have
two beta corners. Q2's beta/beta unit sides are precisely3,4,5,6.

Write E=p_3-p_2=1 and e_j=v_(j+1)-v_j. For each such Q side j there
are exactly two placements across P side2:

    preserving: G_j(v)=r*v+t,
                r=-E/e_j, t=p_3-r*v_j;
    reversing:  G_j(v)=r*conjugate(v)+t,
                r=E/conjugate(e_j), t=p_2-r*conjugate(v_j).

The two possibilities cover all rotations and reflected endpoint maps.
The chosen supporting half-plane fixes the outside placement for each
endpoint bijection, so there is no third isometry or unenumerated position.

The private-chain theorem forces the new Q axis to be parallel to the old
one. For Q2 that axis has direction z. Since e_j=z^(j+1), the preserving
map rotates it by z^(4-j) and is parallel only at j=4. The reversing map
sends z to z^j and is parallel only at j=6. Thus exactly two of the eight
maps survive: preserving4 and reversing6. Both remain genuine candidate
placements even if Q had an internal symmetry; repeated parametrizations
could only duplicate candidates, not add any.

For each surviving G, the exact intersection

    H_b(Q2) intersect (G(Q2)+u),    u=2(b-a),

has positive area s=sin(pi/5). The producer retains the full algebraic
intersection polygons and their positive areas in the certificate. The
translated new copy G(Q2)+u is mandatory because every private Q chain
has this period, with either sign giving the same tile set. Therefore
both possible third neighbors overlap another required Q tile. No good
plane tiling exists; the reviewed limit theorem then excludes the original
assumed tiling. Reflection excludes the congruent incoming-side row as well.

## A direct six-motif plane witness for Q3

For a counterclockwise polygon V and unit side j, define S(V,j) to be the
unique regular pentagon across that side, in the opposite supporting
half-plane. Its vertices are

    q_0=V_(j+1),
    q_k=V_(j+1)-(V_(j+1)-V_j)*sum_(r=0)^(k-1) z^(2r), k=1,...,4.

For Q=Q3 put a=(v_0+v_1)/2, b=(v_3+v_4)/2 and H_b(v)=2b-v.
The two period vectors are

    u=2(b-a)=((1+3phi)/2, s*(2+3phi)),
    w=(phi+2, -2phi*s).

The six finite motifs are exactly

    Q, H_b(Q), S(Q,1), S(Q,2), S(H_b(Q),5), S(H_b(Q),6). (2)

Their translates by Z*u+Z*w tile the plane. All four pentagon copies are
regular unit P, and the two octagons are congruent Q3, so no extra tile
class or matching rule is present. Their exact coordinates and lattice
are retained independently in the certificate's whole_plane_witness.

Here is the finite-to-infinite verification. Express every motif vertex
in lattice coordinates via the inverse matrix with columns u,w. Any
intersecting translated pair must have each integer shift coordinate in
the exact interval obtained by subtracting their projection bounds.
Checking every integer pair in those intervals, excluding identical copies,
leaves36 ordered comparisons. Each has zero intersection area by exact
convex clipping. Every omitted shift has disjoint projections. Thus all
translated motif interiors are disjoint, without a period or shift cutoff.

The exact area identities are

    area(P)=s*(3phi+1)/2,
    area(Q3)=s*(9phi+8)/2,
    abs(cross(u,w))=5s*(3phi+2)=4area(P)+2area(Q3)>0.

Hence the disjoint motifs occupy full area in a lattice fundamental cell.
Their periodic union is closed and locally finite. An uncovered point
would have an uncovered open neighborhood of positive area, contradicting
that cell-area identity. This proves whole-plane coverage. In particular
u,w are independent and both are translational symmetries. No band-gluing
or unproved finite-patch extension is used.

## Certificate, replay, review, and scope

[Producer](../searches/regular_pentagon_private_octagon_geometry.py),
[certificate](../certificates/regular-pentagon-private-octagon-geometry.json),
and [complete search record](../searches/regular-pentagon-private-octagon-geometry.md).

```text
conda run --no-capture-output -n arisearch python3 research/searches/regular_pentagon_private_octagon_geometry.py
```

All finite arithmetic decisions are exact. Coordinates and overlap polygons
are represented by minimal polynomials and rational isolating intervals,
with each nonrational interval checked to contain one real root. The
classification's finite computation and its first whole-plane certificate
are awaiting an independently structured hostile check. No novelty claim
is made. Equal private lengths, irregular equiangular P, adjacent alpha
corners, and other angle or length signatures remain outside this theorem.
