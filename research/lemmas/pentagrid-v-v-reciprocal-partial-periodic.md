# Reciprocal mirror-V pentagons: a full positive cone of partial-contact periodic tilings

**Status:** adversarially reviewed VALID throughout a,k>0, with exact
certificates and independent formal/coordinate checks; see the
[fresh hostile review](../reviews/pentagrid-v-v-reciprocal-partial-periodic-review.md).
This theorem concerns the reciprocal family below, not arbitrary independent
mirror metrics or arbitrary V/V pairs.
It gives a periodic escape and does not resolve the unrestricted two-polygon
research target.

## Theorem and exact shapes

Let phi=(1+sqrt(5))/2 and z=exp(pi*i/5), with z in the upper half-plane.
Equivalently z is the selected root of z^4-z^3+z^2-z+1=0, and phi=z+z^-1.
For every a,k>0, the mirror-V pentagons with native side lengths

    A=(a, r, a, k, k),       r=phi*k+a/phi,
    B=(k, f, k, a, a),       f=phi*a+k/phi,

and native after-side angle word (2,2,4,3,4)*pi/5 admit a rank-two periodic
plane tiling using two copies of each shape per lattice cell. When a!=k,
these are exactly two distinct congruence classes. All contacts in the
construction are actual contacts of unmarked polygons. The displayed construction has partial native-side contacts in every
parameter case. It uses the unequal D sides through their interval
decompositions rather than requiring whole-side matches. This does not assert
that every other tiling of the same pair must have partial contacts.
Thus no pair in this whole reciprocal positive family is strongly aperiodic.
The theorem asserts existence of a periodic tiling, not that every tiling of
these shapes is periodic.

Hereafter indices are modulo5, and a native side h joins vertex h to h+1.
The native vertex-angle word is (4,2,2,4,3)*pi/5. Define

    J=r*z^2-a*z^4,   H=2J+k,
    A0=[J, r*z^2, 0, a, a+k*z],
    B0=[J+k, J, J-f*z^3, J-f*z^3+k*z,
        J-f*z^3+k*z+a*z^2],
    A1=H-A0,        B1=H-B0.

A1 and B1 mean pointwise half-turn images; their native indices remain those
of A0 and B0. These four finite exact polygons are the motif.
Their edge direction exponents, in units pi/5, are respectively

    A0: (4,7,0,1,3),   A1: (9,2,5,6,8),
    B0: (5,8,1,2,4),   B1: (0,3,6,7,9).

Multiplying these directions by the prescribed positive native lengths gives
exactly the consecutive edge vectors in the displayed coordinates. The
cyclic directions increase by exterior turns all strictly between0 and pi.
The exact producer additionally proves every nonincident native vertex lies
strictly on the interior side of every supporting edge: every normalized
support determinant has positive nonzero coefficients in a,k. Consequently
all four displayed walks are genuine strictly convex pentagons throughout
a,k>0, rather than merely closed walks or sample convex polygons.

Any congruence preserves the unique side joining the two72-degree corners,
so congruent A and B would require r=f. But r-f=k-a. Hence a!=k makes them
distinct. The construction also remains valid at a=k, where the two classes
coincide; that point is simply excluded from the original two-class statement.

## Exact lattice and six full native-side seams

Set

    U=B0[3]=J-f*z^3+k*z,
    V=H-a,
    T=U-V=A0[4]+B0[2]-H.

Also H-U=(r+a)*z^2. The lattice is Lambda=Z*U+Z*V.
All motif copies translated by every lattice vector will be included.
A notation such as B1+T below denotes its actual translated physical polygon.
The following six seams identify entire native sides with reversed directed
endpoints:

| First occurrence | Second occurrence |
| --- | --- |
| A0 side0 | B1 side4 |
| A1 side0 | B0 side4 |
| B0 side0 | B1 side0 |
| A0 side2 | (A1-V) side2 |
| A0 side3 | (B1+T) side2 |
| A1 side3 | (B0-T) side2 |

Every side occurrence in this table is used once. These account for12 of the
20 native-side occurrences. The remaining8 occur on two families of lines.
Their partial contacts are explicit next; no unproved gluing condition is
hidden in the choice of lattice.

## First contact line: two interval decompositions of [0,r+a]

On the line q*z^2, the remaining four occurrences are:

| Occurrence | Undirected coordinate interval | Directed sense |
| --- | --- | --- |
| A0 side1 | [0,r] | negative |
| (B0-U) side3 | [0,a] | positive |
| (A1-U) side1 | [a,r+a] | positive |
| B1 side3 | [r,r+a] | negative |

Thus the negative occurrences partition [0,r+a] as [0,r] and [r,r+a],
while the positive occurrences partition the same interval as [0,a] and
[a,r+a]. Directed chain cancellation is exact for every positive r,a.
The actual contacting pieces, with their positive lengths, are:

* r<a: [0,r] pairs A0 with B0-U; [r,a] pairs B1 with B0-U;
  [a,r+a] pairs B1 with A1-U.
* r=a: [0,a] pairs A0 with B0-U; [a,2a] pairs B1 with A1-U.
  The middle zero interval is absent, not a degenerate tile edge.
* r>a: [0,a] pairs A0 with B0-U; [a,r] pairs A0 with A1-U;
  [r,r+a] pairs B1 with A1-U.

The side numbers are the ones in the table. Hence the middle contact may
join two A or two B tiles, and is a genuine partial D-side contact. The proof
does not insist on old full-D dimers or convex-octagon saturation.

## Second contact line: two interval decompositions of [-k-f,0]

On the line J+q*z^3, the other remaining four occurrences are:

| Occurrence | Undirected coordinate interval | Directed sense |
| --- | --- | --- |
| A0 side4 | [-k,0] | positive |
| B0 side1 | [-f,0] | negative |
| (A1+T) side4 | [-k-f,-f] | negative |
| (B1+T) side1 | [-k-f,-k] | positive |

Both orientations again cover the whole interval exactly once. The actual
pieces are:

* k<f: [-k,0] pairs A0 with B0; [-f,-k] pairs B1+T with B0;
  [-k-f,-f] pairs B1+T with A1+T.
* k=f: [-k,0] pairs A0 with B0; [-2k,-k] pairs B1+T with A1+T.
  Again the zero middle interval is absent.
* k>f: [-f,0] pairs A0 with B0; [-k,-f] pairs A0 with A1+T;
  [-k-f,-k] pairs B1+T with A1+T.

Together the six full seams and these two interval tables account exactly
once for every directed native boundary segment modulo Lambda.
All contacts are between physical polygons with opposite supporting
interior half-planes along the indicated segment. Inserted subdivision
points have straight sector angle pi; they are not new marked vertices or
new prototile edges.

## The full parameter cone and its five cases

Since

    r-a=phi*k-a/phi^2,    k-f=k/phi^2-phi*a,

there are exactly the following cases:

| k/a | First line | Second line | Positive parameterization |
| --- | --- | --- | --- |
| (0,phi^-3) | r<a | k<f | a=phi^3*s+t, k=s |
| phi^-3 | r=a | k<f | a=s, k=phi^-3*s |
| (phi^-3,phi^3) | r>a | k<f | a=s+t, k=phi^-3*s+phi^3*t |
| phi^3 | r>a | k=f | a=s, k=phi^3*s |
| (phi^3,infinity) | r>a | k>f | a=s, k=phi^3*s+t |

Here s,t>0 where used; each parameterization covers its entire stated case.
All interval lengths are strictly positive after their zero coalescence
pieces are omitted. The exact producer checks this symbolically by positive
coefficients in s,t, not by extending signs inferred from fixtures.

As an additional local audit, subdivide native boundaries only at the listed
contact endpoints, pair the reversed segments, and trace the vertex links.
In every open case there are4 faces,12 paired edges and8 vertices on the
abstract torus; at either boundary there are4 faces,11 edges and7 vertices.
Every link has total angle2pi and zero lattice holonomy. The open cases have
four native (2,4,4) links and four T links (2,3,5), in units pi/5. At either
boundary two T links coalesce into one (2,2,3,3) native link, leaving two
T links. This explicitly keeps72+108=180 contacts throughout the family.
No identification at a zero-length artificial segment is retained.

## Infinite coverage from boundary cancellation and positive area

Normalize oriented area and determinants by sin(pi/5). Direct exact identities
give

    area(A0)/sin(pi/5)=(a^2+2phi^2*a*k+phi*k^2)/2,
    area(B0)/sin(pi/5)=(k^2+2phi^2*a*k+phi*a^2)/2,
    det(U,V)/sin(pi/5)=phi^2*(a^2+4a*k+k^2)>0,
    2area(A0)+2area(B0)=det(U,V).

Thus Lambda is a genuine rank-two lattice for the whole positive cone.
On its ordinary geometric torus define the multiplicity function

    N(x)=sum_(lambda in Lambda) sum_(C in {A0,A1,B0,B1}) 1_(int(C)+lambda)(x).

This is a locally finite, integer-valued periodic function. The exact
oriented native boundary chains cancel modulo Lambda by the preceding seam
and interval tables. Therefore the jump of N across every open boundary
atom is zero: every positively directed segment has the same multiplicity
of negatively directed segments. Subdivide at all segment endpoints and
intersections on the compact torus. Any two points outside this finite
boundary arrangement can be joined by a path crossing its segments
transversely and avoiding the finite exceptional vertices. N consequently
has the same value on all complementary cells. Equivalently its distribution
gradient is zero, so it is constant almost everywhere on the connected torus.

The average of N equals total motif area divided by covolume, which is1 by
the exact area identity. Hence N=1 off the boundary arrangement. An interior
overlap would contain an open set with N>=2 and is impossible. A hole in the
union of the closed translated tiles would be open: the family is locally
finite because the lattice has rank two and the motif is finite and bounded.
That hole would give N=0 on an open set, also impossible. Therefore the
closed tile copies cover the plane with disjoint interiors. Their set is
preserved by U and V. This proves the infinite periodic tiling directly,
without assuming that the abstract gluing embeds, inferring existence from
large patches, or extrapolating fixture checks to unsampled parameters.

## Replay, certificate and finite computational domain

The [producer](../searches/pentagrid-v-v-reciprocal-partial-periodic.py) retains
[the exact certificate](../certificates/pentagrid-v-v-reciprocal-partial-periodic.json).
Replay is nondestructive unless --output is explicitly supplied:

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-v-v-reciprocal-partial-periodic.py

The producer performs no tiling search. Its whole-cone computational domain
is exactly the five stated parameter cases, four formal native motifs,
every side subdivision and every resulting link. All operations use exact
Q(z)[a,k] coefficients and real-algebraic signs. It additionally reconstructs
five exact fixtures (a,k)=(10,1),(1,phi^-3),(1,2),(1,phi^3),(1,10), with no
floating tolerance. For each fixture it computes lattice-coordinate bounding
boxes of all four convex polygons and checks every possible translated
intersection within the resulting exhaustive integer ranges by exact convex
clipping. The counts are respectively38,40,56,68,74, totaling276 comparisons;
all intersection areas are zero. These fixture audits support the retained
certificate; the full positive-cone proof is the symbolic boundary and area
argument above. There is no solver, random seed, period cutoff, timeout,
larger-patch inference or hidden shared-side matching restriction.

The [separate root coordinate audit](../reviews/pentagrid-v-v-reciprocal-coordinate-audit.md) constructs six different exact fixtures, including both coalescence values and the congruent ratio1. Its no-author-import clipping checker passes all292 complete comparisons and verifies the formal area identity. Root suggested the boundary-jump argument, so this coordinate audit is not counted as the fresh independent whole-proof review. The [separate non-author hostile review](../reviews/pentagrid-v-v-reciprocal-partial-periodic-review.md) is now complete and VALID over the full positive cone, including both coalescence boundaries, reflections, congruence classes and coverage.

## Relation to the arbitrary mirror family

The earlier [general full-D double-Y partner theorem](pentagrid-v-v-general-double-y-partners.md)
selects special compatible partners. The present family instead exchanges
the mirror metric roles a and k and uses explicit partial contacts. It is
not a relabeling of that theorem's whole-side hypothesis: here A's D length
r equals B's E length a only on k/a=phi^-3, while B's D length f equals A's
E length k only on k/a=phi^3, and these boundaries cannot coincide.

For an arbitrary independently chosen pair
(b_i,b_i/phi+phi*f_i,b_i,f_i,f_i), the reciprocal condition need not hold.
The [reviewed imported Rao filter](pentagrid-pentagon-monohedral-filter.md) excludes a monohedral escape for either reciprocal member when a!=k: its two equalities both reduce to a=k. The construction itself does not depend on that classification. No extension or forcing invariant has been proved for the larger independently specified domain.
A proposed assertion that every such tileable pair has a finite periodic
quotient would merely restate its central global obligation. This theorem
therefore closes the specified reciprocal partial-contact family, while
leaving arbitrary independent mirror metrics outside its claim.
