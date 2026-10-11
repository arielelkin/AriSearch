# A periodic continuum inside the golden pentagrid avenue

**Status:** adversarially reviewed; the [fresh hostile review](../reviews/pentagrid-u-w-periodic-continuum-review.md) is VALID for the entire real parameter domain.
The [independent verifier](../reviews/verify_pentagrid_u_w_periodic_continuum.py) checks formal seams, ordered links, area identities and the irrational fixture. This is a family of periodic escapes,
not a classification of every pentagrid pair or a solution of the main problem.

## Exact family

Let z=exp(pi*i/5), phi=z+z^(-1)=(1+sqrt(5))/2. Algebraically z is the unique
root of z^4-z^3+z^2-z+1 with positive imaginary part and real part in
(4/5,81/100). For real parameters

    b>0, 0<c<phi*b,
    A=phi^2*b+phi*c, H=phi^2*b-phi*c,

define counterclockwise polygons

    U=[0,A,b*(z+z^3)+c*z^2,c*z^2+b*z^3,b*z^3],
    W=[0,b,b*(1+z^2),b*(1+z^2)+H*z^4,
                     b*(1+z^2)+H*z^4+c*z^6].

U has consecutive lengths(A,A,b,c,b) and angles after those sides
(1,3,4,4,3)*pi/5. W has lengths(b,b,H,c,H), and every angle is3pi/5.
Thus their angle words are different and they represent exactly two distinct
congruence classes. For every displayed parameter choice, the pair has a
whole-plane tiling with two independent translation periods. Parameters
need not lie in Q(sqrt(5)). Exact algebraic parameter choices give exact
algebraic tiles under the original problem's defining-data requirement.

The special case b=c=1 is the previously certified
[U/regular-W periodic pair](../counterexamples/pentagrid-golden-metric-periodic-pair.md).
Here W need not be regular: its metric changes with c/b.

## Closure and genuine convexity for the whole parameter domain

U's five directed side vectors are

    A, A*z^4, b*z^6, c*z^7, b*z^8.

These close by the defining identities of z and phi. The W directions are
1,z^2,z^4,z^6,z^8. Closure follows, for example, from

    z^4+z^8=phi^(-1)*z^6, 1+z^2=-phi*z^6,
    H/phi+c=phi*b.

Every listed side length is strictly positive. Both direction lists turn
strictly counterclockwise through a total2pi, with each turn less thanpi.
For any chosen side, successive vertex heights above its supporting line
increase as subsequent edge directions traverse the positive sine
semicircle, then decrease as they traverse the negative semicircle, returning
to zero exactly at closure. Every nonincident vertex has strictly positive
height: at least one strict positive increment and one strict negative
increment are present, and monotonicity on the two arcs excludes any earlier
return to zero. Thus these are genuine globally convex pentagons. The U
convexity is also a subfamily of the previously independently checked
[positive area family](../searches/pentagrid-golden-metric-area-compatible.md).
No assumption of a generic parameter or distinct W lengths is made.

## Explicit periodic motifs and complete seam identities

Use zero-based vertices of U and W. Put

    u=U2=b*(z+z^3)+c*z^2,
    v=b*(4-z+2z^2-5z^3)-c*z^2.

The four counterclockwise motifs, in the indicated local vertex order, are

    F0=U,
    F1=[A-Uj:j=0,...,4],
    F2=[z*Wj+U3:j=0,...,4],
    F3=[z^6*(W_(j+3 mod5)-W3)+U4:j=0,...,4].

F1 is a half-turn of U; F2 and F3 are rotations and translations of W.
The index shift in F3 is essential: its local side0 is native W side3.
Take all Fi+n*u+m*v for integers n,m.

The following ten rows use every motif side once. A row(i,a,j,d,n,m)
states the exact reversed-endpoint equations

    Fi[a]=Fj[d+1]+n*u+m*v,
    Fi[a+1]=Fj[d]+n*u+m*v,

with side/vertex indices modulo5:

| i,a | j,d | n,m |
| --- | --- | --- |
| 0,0 | 1,0 | 0,0 |
| 0,1 | 1,1 | 1,0 |
| 0,2 | 2,0 | 0,0 |
| 0,3 | 3,0 | 0,0 |
| 0,4 | 2,1 | -1,0 |
| 1,2 | 3,2 | 0,1 |
| 1,3 | 2,3 | 0,1 |
| 1,4 | 3,3 | 1,1 |
| 2,2 | 3,4 | 1,0 |
| 2,4 | 3,1 | 0,0 |

All equations are identities linear in b,c. The certificate verifies both
coefficient vectors exactly, so the argument covers all parameters and is
not a collection of sample checks.

## Circular links and area identities

Glue abstract polygon faces along the listed equal full sides, reversing
endpoints. The side involution induces the corner permutation
(i,a)->(j,d+1). It has six circular orbits. Two have angle multiset
(1,3,3,3) and four have(4,3,3), in pi/5 units, so every orbit sums to2pi.
The certificate retains the actual ordered orbits, not only corner unions.
Face adjacency is connected; the quotient is a compact connected oriented
surface, and6vertices-10edges+4faces=0. Each point of an edge has exactly
two incident half-disks, and every vertex has a single circular link.
Hence it is a genuine surface with no singular vertex or boundary.

Normalize signed crosses and areas by sin(pi/5)>0. Direct exact quadratic
coefficient identities give

    area(U)/sin(pi/5)=phi^3*b^2+2phi^2*b*c+(phi^2/2)*c^2,
    area(W)/sin(pi/5)=phi^3*b^2-(phi^2/2)*c^2,
    cross(u,v)/sin(pi/5)=-4phi^2*b*(phi*b+c)<0.

In particular u,v are independent for every parameter in the domain, and

    2area(U)+2area(W)=abs(cross(u,v)).                       (1)

The three coefficient evaluations (b,c)=(1,0),(0,1),(1,1) in the producer
verify the complete quadratic identities. Those degenerate coefficient
probes are not asserted to be geometric tiles; positivity is proved on the
stated open parameter domain separately.

## Why the motifs cover the entire plane

Let Lambda=Z*u+Z*v. Independence makes this a discrete rank-two lattice.
Map each abstract face to the ordinary flat torus R^2/Lambda using its
explicit motif Fi. Seam equations make this map continuous and well-defined.
It is an orientation-preserving local isometry on face interiors. Across
an edge the reversed directed endpoints put the two incident convex faces
on opposite supporting half-planes, so the map remains locally one-to-one.
At a vertex its single circular link maps successive positive corner sectors
in order. Their total angle is exactly2pi, so it again maps a neighborhood
one-to-one onto a Euclidean disk. Thus the map is a local homeomorphism
everywhere and preserves area locally.

For completeness, compactness turns this into a finite covering. Its image
is open by local homeomorphism, closed by compactness, nonempty, and therefore
all of the connected target torus. A fiber is discrete and compact, hence
finite. Choose disjoint local neighborhoods around its finitely many points;
the complement is compact and its image avoids the chosen target point.
Shrinking the target neighborhood removes that complement and makes the
local neighborhoods evenly cover it. The number d of preimages is therefore
a positive integer constant on the connected torus. Local area preservation
gives source area=d times target area. By(1), d=1.

Consequently the quotient faces have disjoint interiors and cover the torus
exactly. Lifting their explicit polygons to the plane gives exactly all
listed motifs and their Lambda translates, with disjoint interiors and full
coverage. This proves the whole parameter family, without a bounded patch
search, an overlap check at finitely many parameter samples, or a presumed
extension of a local patch. Nonzero u and v are translation periods.

## Exact irrational-parameter fixture

Take b=1,c=sqrt(2), the positive root of c^2-2=0 in(7/5,3/2).
Since sqrt(2)<phi, H>0 and the theorem applies. Also sqrt(2) does not belong
to Q(sqrt(5)): writing sqrt(2)=r+s*sqrt(5), r,s rational, and squaring forces
rs=0; neither r^2=2 nor s^2=2/5 is a rational square. Thus this is a periodic
pair inside the pentagrid angle language with a parameter ratio outside the
golden field. Its area ratio is

    area(U)/area(W)=1+2phi+2phi*sqrt(2),

which is outside Q(sqrt(5)) and in particular irrational. Both shapes fail
monohedral tilability: U under the explicitly imported, reviewed Rao
classification, W directly because neither a full nor a half native star
can be made solely from108-degree corners. Those monohedral facts are not
needed for the periodic construction.

The [producer](../searches/pentagrid-u-w-periodic-continuum.py) and
[certificate](../certificates/pentagrid-u-w-periodic-continuum.json) retain
all formal coefficients, seams, circular links, and exact algebraic fixture
coordinates with root-isolation data. For the fixture a separate exact
separating-axis check derives the complete integer translation domain from
all lattice-coordinate bounding boxes, checks every possible overlap, and
verifies motif-area equality. This is redundant evidence for the fixture;
the whole-family proof uses the degree-one map above.

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-u-w-periodic-continuum.py

## Scope and novelty

These two shapes permit a periodic tiling under the original unrestricted
isometry/contact convention, which excludes strong aperiodicity. This does
not assert that every tiling is periodic, does not exclude arbitrary U/W
metric pairs, and says nothing about the remaining U/U,U/V,V/V,V/W families.
The parameter range c<phi*b is a positivity condition on this particular W;
its failure does not exclude some other partner or assembly. No novelty
claim is made. A fresh review must check the local-map argument and complete
formal domain, rather than infer family validity solely from the irrational
fixture's direct overlap checker.
