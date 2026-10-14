# Fractional two-node Ammann resection: two pentagons, periodic omission

Date: 2026-10-14. Status: exact construction and obstruction, independently hostile-reviewed VALID; see the [fresh review](../reviews/ammann-bipartite-tree-pentagons-2026-10-14-hostile-review.md).
This cycle establishes a compatible infinite partition into two strict convex pentagons. It fails unrestricted recognition and aperiodicity immediately.

## Scheme and stopping condition, before enumeration

Start with the infinite legal marked thin/thick rhomb source established in [the forcing theorem](../lemmas/ammann-forcing-aperiodicity.md), Lemmas 5 and 7. Forget its arrows only for the surgery. Bipartitely color its vertices black/white. In each counterclockwise rhomb boundary, choose the two edges starting at black vertices as triangle edges; the other two edges are quadrilateral edges. Opposite edges have the same role. Across every source edge the roles are opposite, since its counterclockwise boundary directions are opposite and its endpoints have opposite colors.

Specify the repeatable interface first: every edge output consists of one quadrilateral sector and one **identical unit-base isosceles triangle** on the other side of its base. These sectors belong to different source rhombs. The two boundary words are the same five-vertex template, with the quad from a thin or thick source rhomb respectively. No source patch census is needed.

The bounded experiment checks the two source rhomb geometries exactly. Stop if either partition or output convexity fails, if more than two output shapes occur, or if either output shape has a periodic omission. The last condition holds, so no vertex/contact catalogue or larger patch search follows.

## Exact geometry

Write a rhomb as `A=0, B=1, C=1+c+i*s, D=c+i*s`, with `(c,s)=(cos(theta),sin(theta))`, `theta` equal to 36 or 72 degrees. Suppose AB and CD are its triangle edges. Fix the common physical triangle altitude

    h = sin(36 degrees)/10.

Put `p=1/2+i*h`, `q=1/2+c+i*(s-h)`. The two-node tree consists of Ap, Bp, pq, Cq, Dq. Its four sectors are

    (A,B,p), (B,C,q,p), (C,D,q), (D,A,p,q).

The first and third are congruent isosceles triangles of area h/2. The other two are congruent quadrilaterals of area `(s-h)/2`. The tree is embedded: p and q are strictly interior, pq runs inside the convex rhomb, and the four leaf segments are inside the four sectors. The checker verifies all sector turns positive and total area s. The alternate opposite-edge choice is obtained by a reflection interchanging the two unit edge directions, so it creates the same sector shapes up to allowed isometries.

For the quadrilateral `B,C,q,p`, attach the universal triangle with apex

    t=(B+C)/2 - i*h*(c+i*s).

Its new output boundary is `(B,t,C,q,p)`. The five positive consecutive turn determinants, starting at B, are

    s*(1/4+h^2), h, s*(1/4+h^2),
    s/2-h*(1+c), s/2-h*(1-c).

In particular **both far endpoints B and C** of the removed common base are checked, not merely the apex and new tree nodes. These formulas do not depend on the type or orientation of the neighboring triangle's source rhomb: its triangle is exactly the same geometric triangle. Thus they apply to every actual marked source contact without a contact enumeration. The bound `h < s/[2*(1+|c|)]` holds for both source angles, proving strict convexity and five unsuppressed sides. The output area is exactly s/2, so thin and thick outputs are distinct congruence classes.

## Global compatibility and choice of coloring

The rhomb vertex graph is connected and bipartite. Any finite simple edge cycle bounds finitely many quadrilateral faces, and counting their edge incidences makes its length even. Thus there are no odd cycles, giving a black/white coloring, unique up to swap. Local finiteness follows from the positive unit-rhomb inradii and bounded diameters. The planar edge graph is connected because its rhombs form an edge-to-edge plane covering.

Each source rhomb is exactly partitioned into the four stated sectors. Each shared edge has exactly one triangle and one quadrilateral sector, so gluing them partitions the full plane into output pentagons. This is a repeatable global extension rule on the known infinite source. Each quad produces one pentagon; a thin rhomb supplies two thin-class pentagons and a thick rhomb supplies two thick-class pentagons. Both species therefore occur on the reviewed source.

Swapping the coloring exchanges the opposite-edge roles in every rhomb. The thin/thick output shapes stay in the same two congruence classes, by the rhomb reflection mentioned above. A reflection of the source also reverses clockwise selection and hence exchanges these coloring conventions; the allowed congruence classes again stay the same. A chosen coloring is auxiliary construction data; no claim of an intrinsically chosen color is made.

## Immediate alternative assembly: periodic omission

For either angle theta, use the homogeneous periodic rhomb lattice with vertices `m+n*exp(i*theta)`, for integers m,n, and rhombs spanning the two unit lattice directions. Color a vertex by the parity of m+n, and apply exactly the same two-node surgery. Every source rhomb is now of the same type, so every output is a congruent copy of its one associated pentagon. The coloring and surgery are invariant under periods `2` and `2*exp(i*theta)`; the output is a periodic monohedral tiling. It omits the other pentagon species.

This alternative assembly is an explicit full-plane cover with independent periods, not a solver patch. It follows directly from the same compatibility proof. These carrier rhombs need not obey Ammann arrows, since the output polygons are unmarked. The scheme therefore fails even the strongest cheap omission test.

The constructed pentagon tiling can be decoded if its remembered triangle/quad sectors and source colors are supplied. A universal translation-equivariant intrinsic decoder into the legal aperiodic marked source cannot exist: applying such a decoder to either periodic monohedral assembly would produce a periodic legal marked source, contradicting the reviewed forcing theorem. Successful two-shape partition and unrestricted source recognition are consequently separate milestones here.

## Exact replay and changed assumption

The checker uses Q(phi), with coordinates `(x,y)` meaning `x+i*sin(36 degrees)*y`. It checks two rhomb partitions, both five-turn output formulas, distinct exact areas and explicit periodic carrier vectors. This is a two-row exact experiment and no source-contact census.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-bipartite-tree-pentagons-2026-10-14.py --check research/certificates/ammann-bipartite-tree-pentagons-2026-10-14.json

The assumption to change before restart is the **common triangle independent of mark and source type**. It makes each quad class complete in an arbitrary homogeneous rhomb carrier. Every altitude in the convex range above has the same escape; varying h or enumerating larger patches cannot repair it. A next explicit surgery must preserve some source-matching information in distinct/asymmetric triangle interfaces while still collapsing their receiving quad completions to two output classes. One bounded gate for such a restart is to assign different X/Y triangle apex offsets and compare the exact two completions at every receiving quad, then immediately test the homogeneous carrier. No such variant is claimed or enumerated in this cycle.
