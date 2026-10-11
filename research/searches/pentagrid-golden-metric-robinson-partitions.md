# Unit Robinson repartition: exact geometric patches, rejected source compiler

**Status:** exact geometric verification complete; the selected source compiler
is falsified. The finite boundary test passes, so it does not exclude other
source clusters. The [fresh hostile review](../reviews/pentagrid-robinson-partitions-review.md) is VALID for this scoped rejection; the [independent geometry and boundary checker](../reviews/verify_pentagrid_robinson_partitions_independent.py) passed.

This tests a different construction mechanism from homothetic pentagon
substitution. It supplies concrete triangle geometry, then checks the source
legality that a global Penrose recomposition would require. It establishes
neither a plane tiling by U/V nor shape-only forcing.

## Exact shapes and source assumptions

Let z=exp(pi*i/5), phi=z+z^(-1), and work in Q(z), with
z^4-z^3+z^2-z+1=0. Use the b=c=1 instance of
[the area-compatible family](pentagrid-golden-metric-area-compatible.md):

    U = [0, phi^3, z+z^2+z^3, z^2+z^3, z^3],
    V = [0, 1, 1+(1+3phi)z^3, 2phi^2 z^3, 2phi z^4].

The unit thin triangle has reference vertices [0,1,z], angles
(36,72,72) degrees, lengths (1,1,phi^(-1)), and area sin(36)/2.
The unit fat triangle [0,1,z^3] has angles (108,36,36) degrees,
lengths (1,1,phi), and area phi*sin(36)/2. These are respectively
the halves of a unit thin rhomb cut along its short diagonal and a unit fat
rhomb cut along its long diagonal. Only these exact unit scales are tested.

The hypothesized source is an actual edge-to-edge unit Penrose rhomb tiling,
with each rhomb cut as specified. Its triangles necessarily meet whole edge
to whole edge: rhomb outer edges have length1 and its diagonals are internal.
The checks below use this necessary geometric property. They do not assert
that any unmarked triangle patch satisfying it has legal Penrose arrows.

## Concrete geometric partitions

[The exact producer](pentagrid-golden-metric-robinson-partitions.py) gives
U=7 thin+9 fat unit triangles and V=9 thin+16 fat unit triangles. The
[certificate](../certificates/pentagrid-golden-metric-robinson-partitions.json)
lists every vertex and the exact rotation, translation and optional reflection
from its reference triangle. For every triangle it checks all five parent
supporting halfplanes. It checks all120 U and300 V triangle pairs by exact
separating axes and checks the exact sums of triangle areas against the
parent area. Finite closed containment, interior disjointness and area equality
prove coverage: any omitted parent interior point would have an omitted open
neighborhood of positive area.

U consists of the phi^3 thin triangle [0,phi^3,phi^2 z^2] and a quadrilateral.
The triangle is subdivided three times by the geometric templates

    phi*thin [0,phi,phi*z]
       = fat [0,1,phi*z] + thin [1,phi,phi*z],
    phi*fat [0,phi,phi*z^3]
       = fat [phi,phi-1,z^2] + thin [0,phi-1,z^2]
         + fat [0,z^2,phi*z^3].

The quadrilateral is cut at P=z^2 into

    fat  [U2,U3,P], thin [U3,U4,P], thin [U4,U0,P].

V consists of the 2phi fat cap [V4,0,V3] and the remaining trapezoid.
Split the cap medially into four phi fat triangles and apply the second
template once to each. This contributes4 thin+8 fat triangles. In the
trapezoid place the four unit fat rhombs

    R_j = [j*z^3, 1+j*z^3, 1+(j+1)*z^3, (j+1)*z^3], j=0,...,3,

and cut each along its long diagonal. With T=4z^3 and s=phi-1, let
A_i=T+i*s*z^3 (i=0,1,2) and B_i=T+1+i*s*z^3 (i=0,1,2,3).
The remaining strip is the five unit thin triangles

    [A0,B0,B1], [A0,A1,B1], [A1,B1,B2],
    [A1,A2,B2], [A2,B2,B3].

The trapezoid therefore contributes5 thin+8 fat triangles.
[The diagnostic SVG](pentagrid-golden-metric-robinson-partitions.svg) uses
floating coordinates for rendering only; none of the geometric assertions do.

The content matrix, with thin/fat rows and U/V columns, is
C=[[7,9],[9,16]], of determinant31. It commutes with
M=[[1,1],[1,2]], and C*(1,phi)=(7+9phi)*(1,phi). Thus a hypothetical
repartition of a source with thin:fat frequency1:phi would have U:V
frequency1:phi. This is only an arithmetic compatibility check: the source
cluster geometry, global repartition and recovery from unmarked shapes would
still need proofs.

## Minimal source-legality failure

Both retained partitions fail the necessary edge-to-edge property. The exact
contact certificate finds4 partial positive contacts in U and15 in V.
These are valid geometric partitions with T-junctions, not actual patches of
the hypothesized unit rhomb halves. Assigning Penrose arrows cannot repair
their geometry.

There is a short obstruction that rejects the selected V compiler independently
of how its four medial cap triangles are further refined. The cap base runs
from0 to2phi^2 z^3, and the medial split makes

    M = phi^2 z^3

a genuine corner of cap pieces. Refining those pieces into finitely many
nondegenerate triangles must preserve M as a native triangle vertex. The unit
rhomb R_2 has the whole unit outer edge [2z^3,3z^3]. Since

    2 < phi^2 < 3,

M lies strictly inside that edge. Moreover any subdivision of that unit rhomb
into the specified unit triangle scales leaves this outer edge whole. Indeed
the only positive sum of 1,phi,phi^(-1) equaling1 is the single term1,
as seen by comparing coefficients of1 andphi. Thus a triangle vertex at M
meets the interior of another whole triangle edge. This is forbidden in an
edge-to-edge source patch. The certificate retains M, the exact fraction
phi^2-2 along this edge, actual cap triangle indices, and the row triangle
carrying that edge.

This excludes the medial-cap/four-rhomb-row compiler. It does not exclude all
unit triangle partitions of V. In particular the phi fat triangle also admits
the different geometric fan

    fat [0,phi,z], thin [0,z,z^2], fat [0,z^2,phi*z^3],

whose long-side subdivisions differ from the chosen template. No uniqueness
claim about phi fat partitions is used. Crossing the chosen macro interfaces,
changing their geometry, or constructing another globally legal source atlas
would require a new mechanism.

## Complete finite necessary boundary test

The next check asks whether **any** edge-to-edge unit triangle patch inside
U or V is already impossible from its outer boundary alone. Use length symbols
u=1, l=phi, s=phi^(-1)=phi-1. A side of length a+b*phi must be a positive
ordered word with edge counts

    n_s=0,...,b, n_l=b-n_s, n_u=a+n_s.

The supporting-line argument makes these whole native source edges: a child
triangle inside a convex pentagon cannot extend an edge past a genuine
pentagon corner. At each boundary vertex, native triangle sectors give an
open walk in the length graph

    thin36: u--u, weight1; thin72: u--s, weight2;
    fat108: u--u, weight3; fat36: u--l, weight1,

where weights are in units pi/5. Both walk directions are allowed. The total
weight is5 at a side subdivision and the native parent angle at a parent
corner. These are necessary local matching conditions, with no placement or
marking sufficiency assertion.

[The independent boundary producer](pentagrid-golden-metric-robinson-boundary.py)
enumerates all ordered edge words and all finite open native-corner walks of
weight at most5. It uses only exact integer coefficients in the basis1,phi.
The [boundary certificate](../certificates/pentagrid-golden-metric-robinson-boundary.json)
retains the complete fan-count table and explicit witnesses:

| Shape | Ordered words per successive side | All boundary choices | Passing choices |
| --- | --- | --- | --- |
| U | 25,25,1,1,1 | 625 | 299 |
| V | 1,129,1,13,13 | 21801 | 18576 |

Every pair of terminal edge symbols admits a flat weight5 fan. Concrete
passing boundary words are

    U: (u,l,l), (u,l,l), (u), (u), (u),
    V: (u), (u,l,l,l), (u), (l,l), (l,l).

The retained fans demand respectively (thin36,thin72,fat108,fat36)
=(4,0,7,10) and(3,0,7,16), within the available native corner counts
(7,14,9,18) and(9,18,16,32). This necessary test therefore excludes neither
shape. It supplies local boundary data, not an actual triangle arrangement,
marked source cluster, or extension to the plane.

A further necessary disk count does not close the gap. An ETE triangulated
disk with F triangles, B boundary edges and I interior vertices satisfies
F=2I+B-2. The areas force exactly F=16 for U and F=25 for V, so U needs
B even and V needs B odd. The first local witnesses above fail that parity;
they are not asserted to extend. The same complete enumeration leaves150 U
words and9288 V words after requiring both fans and disk parity. Retained
parity-compatible witnesses are

    U: (u,l,l), (u,u,l,s), (u), (u), (u), with B=10 and required I=4;
    V: (u), (u,l,l,l), (u), (l,l), (u,l,s), with B=11 and required I=8.

Their selected fan corner demands are(5,2,7,10) and(3,2,6,20), within the
same available counts. This remains necessary combinatorial boundary data;
interior assembly and source arrows have not been recovered.

## Replays and current stopping point

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-golden-metric-robinson-partitions.py
    conda run --no-capture-output -n arisearch python research/searches/pentagrid-golden-metric-robinson-boundary.py

Ordinary invocation prints JSON without modifying artifacts. Files are written
only with explicit --output or --svg-output. No larger triangle packing search
follows this rejected source compiler. Reopening requires a concrete legal
unit-rhomb source cluster or a changed assembly mechanism that resolves the
mandatory-interface vertex, together with a global repartition argument.
