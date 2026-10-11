# A nonsymmetric octagon with two equal private sides in a periodic pentagon pair

**Status:** adversarially reviewed VALID in the [fresh independent coordinate-and-clipping audit](../reviews/octagon-q3-equal-private-periodic-review.md); exact whole-plane periodic witness. This is an explicit periodic escape in the previously untreated
nonsymmetric equal-private octagon branch, not an aperiodic pair or an
unrestricted impossibility theorem. No literature priority is claimed.

## Exact two shapes

Let z=exp(pi*i/5), phi=z+z^-1=(1+sqrt5)/2 and a=2phi-2. Define a
counterclockwise equiangular108 pentagon P by native lengths

    (a,phi,1,phi,a)

and successive edge directions1,z^2,z^4,z^6,z^8, starting at0. This closes
because1=phi*a-phi/phi. Its positive sorted edge walk is strictly convex.
Its native length word has the reflection symmetry discussed in the
[reviewed universal equiangular-P lemma](../lemmas/private-octagon-adjacent-corner-rigidity.md).

Define Q's native vertices q0,...,q7 by q0=0 and positive successive edge
lengths and direction exponents

    lengths=(phi^2,a,phi,phi^2,1,a,phi,phi),
    exponents=(0,1,2,4,5,6,7,8).

Its exact walk closes. Its native corner angles are
(108,144,144,108,144,144,144,144) degrees. Positive closure in those sorted
directions proves strict convexity; the producer independently checks all
supporting-line inequalities. P and Q are distinct by their side counts.
All coordinates lie in Q(z), with defining polynomial
z^4-z^3+z^2-z+1 and embedding Im(z)>0,4/5<Re(z)<81/100.

The length L=phi^2 is absent from P and occurs on exactly Q sides0,3.
Both private sides start at108 and end at144. Q has no nonidentity symmetry:
any rotational symmetry of its eight-vertex cycle preserving{0,3} is the
identity. The only possible reflection preserving that set is the vertex
involution v->3-v, which sends side0 to side2. Those lengths are phi^2
and phi, so it is not a symmetry. Thus equal private slots do not become
geometrically identical via an actual Q relabeling symmetry.

## Six exact motifs

For (s,epsilon) in{(0,+1),(1,-1)}, let T_(s,epsilon) be the positive
counterclockwise pentagon starting at0 with successive edge vectors

    p_((s+epsilon*j) mod5)*z^(2j),  j=0,...,4,
    p=(a,phi,1,phi,a).

Both walks close and are isometric copies of P. Put H=q3+q4. The six motifs
are

    F0=Q,
    F1=H-Q,
    F2=q2-z*T_(0,+1),
    F3=q3-z^2*T_(1,-1),
    F4=H-q6+z^6*T_(0,+1),
    F5=H-q7+z^7*T_(1,-1).

All six lists are counterclockwise and strictly convex. Choose periods

    u=-3phi+(7phi-1)*z = H-q1,
    w=3phi+4-2phi^2*z.

Their determinant is nonzero:

    cross(u,w)/sin(pi/5)=-(34phi+11).

## Complete exact torus and whole plane

Each row pairs sideh of facei with sideg of facej translated by n*u+m*w,
with reversed endpoints. Native indices are modulo8 for Q and5 for P.

| i,h | j,g | n,m |
| --- | --- | --- |
| 0,0 | 1,0 | -1,0 |
| 0,1 | 2,0 | 0,0 |
| 0,2 | 3,0 | 0,0 |
| 0,3 | 1,3 | 0,0 |
| 0,4 | 4,2 | 0,-1 |
| 0,5 | 3,2 | 0,-1 |
| 0,6 | 2,3 | 0,-1 |
| 0,7 | 5,3 | -1,-1 |
| 1,1 | 5,2 | 0,-1 |
| 1,2 | 4,3 | 0,-1 |
| 1,4 | 3,4 | 0,0 |
| 1,5 | 4,0 | 0,0 |
| 1,6 | 5,0 | 0,0 |
| 1,7 | 2,1 | 1,0 |
| 2,2 | 5,4 | -1,0 |
| 2,4 | 3,1 | 0,0 |
| 3,3 | 4,1 | 0,0 |
| 4,4 | 5,1 | 0,0 |

Substitution checks all36 reversed endpoint equations. Every one of36
native sides occurs once, and the finite quotient is connected. The actual
corner permutation crosses a side mate and then advances to the next
corner on that face. Its12 cycles are retained in the certificate; every
cycle is one circular three-sector link with angles108+108+144=360 and
accumulated integer lattice shift(0,0). Its Euler characteristic is
12-18+6=0. Thus the reversed whole-side gluing is an oriented compact flat
torus and its displayed coordinates map it to R^2/(Zu+Zw) as a local
Euclidean isometry, including vertices and seams.

Direct shoelace identities give

    area(P)/sin(pi/5)=(7phi-1)/2,
    area(Q)/sin(pi/5)=(20phi+13)/2,
    4area(P)+2area(Q)=abs(cross(u,w)).

The compact local isometry is a finite covering of the connected ordinary
lattice torus. The exact area equality forces degree1. Therefore the six
motifs and all translates by n*u+m*w cover the entire plane with disjoint
interiors. This is an infinite periodic admitted tiling by exactly P,Q;
it is not inferred from a finite patch or a periodic-bound search.

The producer additionally derives the complete finite integer-translation
intersection domain from inverse-lattice vertex extrema for all36 ordered
motif pairs. Excluding identical copies leaves36 comparisons, and exact
separating axes show disjoint interiors for every comparison. All omitted
translations have disjoint coordinate projections. This directly checks
the fixed infinite geometry; an independent fresh reviewer should use
exact clipping instead of the author's axis method.

## Search, exact certificate and reproducibility

The metric search fixed the known Q3 six-face torus's18 seams, each face's
physical edge directions and the two Q faces' midpoint-half-turn relation.
It solved linear native closure and seam equations over Q(sqrt5), including
q0=q3 for the private equality, for5 P lengths,8 Q lengths and2 period
components. Its strict positive cone was tested exactly by homogeneous
rescaling to require all13 physical side lengths>=1, using Sage's field
polyhedron backend. The known regular-P placements leave cyclic/reflection
native assignments: normalize first P to(0,+), then give each other P one
of10(shift,sign) choices, a total1000-domain ansatz. It stopped at its first
exact nonregular witness, choice304, with assignments
[(0,+),(1,-),(0,+),(1,-)]. No exhaustive conclusion about the1000 choices
is claimed. No torus bound or cell size was increased.

Normal [producer](../searches/new-octagon-q3-metric-deformation.py) replay
reconstructs the explicit witness, all supporting signs, endpoints, actual
links, area identities and complete comparison boxes without rerunning the
search. The [certificate](../certificates/new-octagon-q3-metric-deformation.json)
contains the exact cyclotomic coordinate vectors, seams, links, areas,
periods and every comparison.

    conda run --no-capture-output -n arisearch python research/searches/new-octagon-q3-metric-deformation.py

Add --search to replay the deterministic fixed-quotient metric search to
its first witness. Saving requires explicit --output. The run completed
with SageMath10.9/Python3.12.13, no random seed or timeout. Certificate
coordinates use the specified field and embedding rather than floating
numerics. No search solver is trusted for the final geometry: the explicit
witness is checked directly.

## Scope

This gives a nonsymmetric equal-private Q that really tiles the plane with
one equiangular P, periodically. It refutes a shortcut that equal private
slots plus absence of Q symmetry by themselves prevent periodic tilings.
It does not prove that every admitted tiling of this pair is periodic,
force half-turn private mates in all its tilings, or classify arbitrary
nonsymmetric equal-private metrics. A cross-native private mate is locally
a36-degree rotation, a genuine different geometric neighbor; whether
all-cross or mixed private branches extend is not inferred from this
periodic witness. Further octagon searches are inactive under the current
portfolio constraint.
