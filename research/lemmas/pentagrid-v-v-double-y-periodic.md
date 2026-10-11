# Two individually untileable mirror-V pentagons in a periodic double-Y family

**Status:** adversarially reviewed; [independent hostile review](../reviews/pentagrid-v-v-double-y-periodic-review.md) valid. Exact continuum and fixture certified. This is a periodic escape family for two V words, not a
classification of all V/V pairs or a solution of the original research
problem. Partial contacts across the macro boundary are essential to the
displayed construction.

## Exact shapes and parameter domain

Let z=exp(pi*i/5), phi=(1+sqrt(5))/2=z+z^(-1). Take

    a>0, 0<k<a/phi.

Write

    r=2phi*a+k, e=phi*a+k/phi,
    y=e+k=phi*(a+k), t=r+a=phi^3*a+k.

Let A have native side lengths(a,r,a,e,e), and B have lengths(k,e,k,a,a),
each with the angle-after-side word(2,2,4,3,4)*pi/5. Equivalently, in the
previously used mirror-V(b,c) parameterization,

    A=V(a,k/phi^2), B=V(k,a/phi-k).

Both parameter pairs are strictly positive. The key cross-type metric
relations are

    D_B=E_A=e, E_B=b_A=a.

The72-to72 side of A has length r>e, the72-to72 side of B has length e,
so the two shapes are noncongruent. The exact side/angle definitions alone
specify the polygons up to unrestricted isometry. Exact coordinates and
convexity are given below.

The [reviewed unrestricted monohedral filter](pentagrid-pentagon-monohedral-filter.md)
says a V-word pentagon with this side convention is monohedral only when
side2=side4 or side3=side0. For a mirror V both equations say b=E. Here
e>phi*a>a and a>phi*k>k, so neither A nor B tiles by itself. This imported
classification is used only for this individual-untileability observation;
the periodic existence proof does not depend on it.

An immediate whole-family corollary is useful. For every b,c>0, the pair

    {V(b,c), V(phi*(b+c),b/phi^2)}                     (2)

has such a periodic tiling, and neither member tiles alone. To obtain(2),
choose a=phi*(b+c),k=b; the retained domain k<a/phi is exactly b<b+c.
Thus this construction supplies a same-angle-word periodic partner for
every member of the original positive-parameter mirror-V family. It does
not assert that every two mirror-V metrics tile together.

## Convex centrally symmetric macro and the four exact children

Define the counterclockwise central hexagon C by

    h0=0, h1=a, h2=a+y*z,
    h3=a+y*z+t*z^2, h4=y*z+t*z^2, h5=t*z^2.

Its side vectors are a,y*z,t*z^2,-a,-y*z,-t*z^2. They are positive,
close exactly, and have strictly increasing edge directions with exterior
turns(108,36,36,108,36,36) degrees cyclically. Its native angles are
(72,144,144,72,144,144) degrees. Thus C is a genuine convex hexagon,
centrally symmetric about h3/2.

The four boundary seam endpoints and two interior seam vertices are

    X=r*z^2, Y=a+e*z,
    J=X-a*z^4, J'=h3-J,
    X'=h3-X=h2+a*z^2, Y'=h3-Y.

Take these four counterclockwise polygons in their native reference orders:

    F0=A0=[J,X,h0,h1,Y],
    F1=A1=h3-A0,
    F2=B0=[J',J,Y,h2,X'],
    F3=B1=h3-B0.                                       (1)

The five directed sides of A0 are

    a*z^4, r*z^7, a, e*z, e*z^3;

those of B0 are

    k*z^5, e*z^8, k*z, a*z^2, a*z^4.

For these identities use z+z^3=phi*z^2,1+z^4=z^2/phi,
and phi^2=phi+1. They also give J'-J=k. Consequently both polygons have
the claimed native length word and positive exterior turns. Their native
vertex angles are(144,72,72,144,108) degrees. The half-turn copies in(1)
preserve these native indices and plane orientation. No matching rule,
label restriction, or additional congruence class has been introduced.

There is an exact universal support check as well as the direction proof.
For each side of A0,B0,C and each nonincident vertex, expand the signed
support cross divided by sin36 as a polynomial in a,k over Q(phi).
Every one of these54 polynomials is nonzero with nonnegative coefficients.
It is therefore strictly positive for a,k>0. This proves global strict
convexity, rather than only local turning signs. The exact producer
reconstructs these54 expressions from(1), without a numerical decision.

## Finite dissection: complete seams, containment, and area

Each row below matches the whole native side (i,s) with side (j,q), with
endpoints reversed. Native side indices are modulo5.

| i,s | j,q |
| --- | --- |
| 0,0 | 3,4 |
| 0,4 | 2,1 |
| 1,0 | 2,4 |
| 1,4 | 3,1 |
| 2,0 | 3,0 |

The central B-to-B seam is[J,J']; the other four form two Y junctions
at its ends. At J the native angles are A0:144,B0:72,B1:144;
at J' they are A1:144,B0:144,B1:72. Both are actual full244 stars.
At X,Y,X',Y', the inside boundary angles are respectively72+108 or
108+72, so the outside macro boundary is straight there.

Every unpaired child side occurs exactly once on these macro side chains:

| Macro side | Ordered child sides |
| --- | --- |
| h0 to h1 | (0,2) |
| h1 to h2 | (0,3),(2,2) |
| h2 to h3 | (2,3),(1,1) |
| h3 to h4 | (1,2) |
| h4 to h5 | (1,3),(3,2) |
| h5 to h0 | (3,3),(0,1) |

The five internal seams and ten outer side pieces account for all20 native
child sides. Exact endpoint substitution verifies every row and chain.

For containment, evaluate the six macro supporting half-planes at all20
child vertices. Each of these120 normalized cross polynomials has
nonnegative coefficients in a,k, allowing zeros on the boundary. Thus
every child lies inside C. For pairwise interior disjointness, convexity
makes any one separating supporting line sufficient. Suitable supporting
edges are

| Child pair | Separating directed edge |
| --- | --- |
| 0,1 | F0 side4 |
| 0,2 | F0 side4 |
| 0,3 | F0 side0 |
| 1,2 | F1 side0 |
| 1,3 | F1 side4 |
| 2,3 | F2 side0 |

Every first polygon lies on the left of that edge and every second polygon
on the right. This also follows by nonnegative coefficients of all the
corresponding negated support crosses; the producer verifies it formally.
These six universal separation tests concern the entire polygons, not
only their matched seam endpoints.

Exact normalized areas are

    area(A)/sin36=(3phi+2)a^2+2phi*a*k+(phi-1)k^2/2,
    area(B)/sin36=phi*a^2/2+phi^2*a*k+k^2/2,
    area(C)/sin36=(7phi+4)a^2+(6phi+2)a*k+phi*k^2.

They give2area(A)+2area(B)=area(C). The four children are closed subsets
of C with disjoint interiors, and their summed area is the entire macro
area. Any missing interior point would lie in an open positive-area gap,
since the finite union is closed; this contradicts the area equality.
Their closed union then contains the closure of the interior of C, hence
all of C. This proves the complete exact four-child dissection. Area alone
is not being used to infer containment or disjointness.

## Whole-plane hexagon lattice and partial child contacts

Put

    u=h2=a+y*z, v=h4=y*z+t*z^2.

The normalized determinant is

    cross(u,v)/sin36=a*y+phi*a*t+y*t
                      =(7phi+4)a^2+(6phi+2)a*k+phi*k^2>0.

Thus u,v span an ordinary lattice. The three macro seam pairings are

| Macro side s | Opposite side q | Translation applied to q |
| --- | --- | --- |
| 0 | 3 | -v |
| 1 | 4 | u-v |
| 2 | 5 | u |

Each gives exact reversed endpoint equalities. Tracing the side mate
followed by the within-face successor gives actual circular links
(0,4,2) and(1,5,3), each with angles72+144+144=360 degrees. Their accumulated
integer lattice shifts are(0,0). Gluing the
three pairs forms a compact connected oriented surface. Mapping it to
R^2/(Zu+Zv) through the displayed macro coordinates is a local Euclidean
isometry: convexity gives opposite half-disks at seams, and each actual
ordered vertex link gives one full disk. The compact local homeomorphism
is a finite covering of the torus. Since area(C)=cross(u,v), its covering
degree is1. Hence the translates C+n*u+m*v cover the whole plane with
disjoint interiors. This is the standard central-hexagon lattice proof,
with its seams, determinant, and degree explicitly exhibited here.

Retain the same four-child dissection in every macro translate. This gives
exactly the admitted periodic set

    {Fi+n*u+m*v: i=0,1,2,3; n,m integers}.

Macro edges match in full, but the children on opposite macro sides do
not generally do so. On side[h2,h3], the native child division is at
distance a from h2. The opposite side5 of the neighboring macro translated
by u has its division at X+u, distance r from h2. Because
r=2phi*a+k>a, the division points differ. The resulting partial contacts
are permitted under the original problem and force no overlap: each macro
is already tiled exactly, and its neighbors lie on the opposite side of
its boundary. A D-to-D full dimerization of every V is therefore not a
property of this witness. Coarsening all V tiles into convex octagons would
discard the actual partial-contact geometry.

## Exact positive fixture and replay

Take a=1,k=phi^(-2)=2-phi in(0,phi^(-1)). Then

    A=V(1,phi^(-4)),
      sides(1,phi+2,1,3phi-3,3phi-3);
    B=V(phi^(-2),phi^(-3)),
      sides(2-phi,3phi-3,2-phi,1,1).

All coordinates lie in Q(z). Both shapes pass the individual non-mono
gate stated above and are distinct. The exact fixture producer derives
the complete integer translation boxes for all16 ordered child pairs in
lattice coordinates. It tests every possible nontrivial overlap in those
boxes with exact separating axes: all44 comparisons have disjoint interiors.
It retains every comparison. This is
a direct validation of a fixed infinite periodic construction, not a
bounded search for a period or patch extension.

The [illustrative SVG](../figures/pentagrid-v-v-double-y-periodic.svg)
shows two adjacent macro translates, both child types, and the two different
division points on their shared macro side. Its plotted coordinates are
for illustration; the algebraic certificate is the exact geometric record.

The [exact producer](../searches/pentagrid-v-v-double-y-periodic.py) verifies
the full linear geometry, all polynomial support and containment signs,
universal pair separation, complete side chains, area and period identities,
and exact positive fixture. The
[retained certificate](../certificates/pentagrid-v-v-double-y-periodic.json)
stores coefficient vectors, seam data, root-isolated fixture coordinates,
and the complete overlap comparison list. Normal invocation is nondestructive:

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-v-v-double-y-periodic.py

Explicit `--output` is required to write a certificate. The initial internal
run caught an area-coefficient transcription mistake before retention:
the B coefficient of a^2 is phi/2, and the macro coefficient is7phi+4.
The corrected formulas above pass the independent native shoelace checks.
A separate Sage monomial-key comparison was normalized to ordinary tuples;
neither change altered geometry or the parameter domain.

## Scope and independent review

This is a changed constructive mechanism: four V tiles with a nonfull
native contact across a lattice-hexagon boundary, rather than a search for
a larger full-edge torus using earlier golden exponent fixtures. It proves
periodic existence for the displayed continuum and kills strong aperiodicity
for those pairs. It does not classify every V/V pair, imply all their tilings
are periodic, or claim literature priority. Its monohedral observation has
the separate reviewed Rao-filter dependency explicitly stated.

The [independent verifier](../reviews/verify_pentagrid_v_v_double_y_independent.py) reconstructs native walks and formal geometry without importing producer code, checks whole-family support/containment and separation, and independently derives the complete44-comparison lattice domain. Exact clipping confirms zero interior intersection for every comparison. Its [retained review certificate](../certificates/pentagrid-v-v-double-y-review.json) records the passing audit. The fresh review also found a [general asymmetric V/V partner mechanism](pentagrid-v-v-general-double-y-partners.md), whose full theorem now has [a fresh independent review](../reviews/pentagrid-v-v-general-partner-review.md) and [a second hostile review](../reviews/pentagrid-v-v-general-partner-fresh-review.md), both VALID.
