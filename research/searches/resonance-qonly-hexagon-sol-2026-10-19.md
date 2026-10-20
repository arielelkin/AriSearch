# The Q-only equiangular hexagon survivor

Date: 2026-10-19. Status: closed, conditional on the stated primary classification theorem.

## Result

Let Q be a fixed strictly convex hexagon with every interior angle 120 degrees. If congruent copies of Q tile the plane, allowing reflections and unrestricted partial side contacts, then Q is centrally symmetric and admits a tiling by translations alone. Consequently the BBBBBB survivor cannot force the absence of a nonzero translational symmetry. This does **not** say that every equiangular hexagon tiles.

## Primary classification and applicability

Source: Ze Zhu, Erxiao Wang, and Min Yan, *Hexagonal Tiling of the Plane*, arXiv:2508.01404v2 (revised 28 April 2026), [Main Theorem and definitions H1–H3](https://arxiv.org/html/2508.01404v2#S1).

The Main Theorem classifies congruent straight-sided hexagon tilings when every vertex meets at least three tiles. Section 2 explicitly allows non-edge-to-edge tilings. Its three families, up to cyclic relabeling or reversal, are:

- H1: angles 0+1+2 and 3+4+5 each total 360 degrees; side lengths s2=s5.
- H2: angles 0+1+3 and 2+4+5 each total 360 degrees; s1=s3 and s2=s5.
- H3: angles 0,2,4 are 120 degrees; s0=s1, s2=s3, s4=s5.

Here side i connects vertices i and i+1 modulo six. Strict convexity ensures the three-tile hypothesis. The classification uses congruence without an orientation restriction; its local enumeration includes flipped corner labels. Thus reflected copies and partial contacts are covered.

## Specialization to equal angles (direct calculation)

Identify the plane with the complex numbers, choose the first side direction as 1, and put z=exp(i*pi/3). The directed sides of Q are s_j z^j, with s_j>0. Closure gives

    (s0-s3) + (s1-s4) z + (s2-s5) z^2 = 0.

Since z^2=z-1 and 1,z are linearly independent over the reals,

    s0-s3 = s2-s5 = -(s1-s4).

Therefore equality of any one opposite pair implies equality of all three opposite pairs. Both H1 and H2 provide such an equality. Opposite directions already differ by 180 degrees, so these equalities imply central symmetry.

In H3 write (s0,...,s5)=(a,a,b,b,c,c). The displayed closure relations become

    a-b = b-c = c-a.

Their sum is zero, hence each is zero. Thus H3 is regular, in particular centrally symmetric. Cyclic relabeling and reversal do not affect either argument.

## Translational construction and its global validity

Center Q at the origin, with cyclic vertices v0,...,v5, so v_(i+3)=-v_i. Define

    t0=v0+v1,   t1=v1+v2,   t2=v2+v3=t1-t0.

Across the side [v_i,v_(i+1)], the translated copy Q+(v_i+v_(i+1)) shares exactly the corresponding opposite side. Strict convexity puts its interior on the other side of the shared line. The vectors t0,t1 are independent: their directions are the directions from the center to the midpoints of two adjacent sides, which cannot be collinear for a strictly convex central hexagon.

Here is a way to verify globally that this continuation tiles, rather than merely displaying a local patch. Start with the abstract cell complex of the ordinary regular hexagonal honeycomb. Replace every face by a copy of Q with the same cyclic side labels. Identify each side with the opposite-labeled side of its neighbor by the translation just described. The combinatorial honeycomb permits these labels consistently: its three edge directions correspond to the three opposite side pairs. Along an edge the quotient metric is Euclidean. At every vertex exactly three 120-degree corners meet, so it is Euclidean there too. The resulting surface is simply connected, since its underlying cell complex is the ordinary honeycomb plane.

It is complete: all faces are copies of the same compact nondegenerate polygon, and the honeycomb has bounded incidence; equivalently, its piecewise Euclidean metric is uniformly comparable to that of a regular honeycomb, using a fixed triangulation of the faces. The development of this simply connected complete flat surface is a global isometry onto the Euclidean plane. For completeness, straight segments from a base point lift for their full length by completeness and local Euclidean charts; this makes development a covering of the plane, and simple connectedness of the target makes the covering one-to-one. Thus the developed faces cover once, with disjoint interiors.

Every edge gluing has identity linear part, so all developed faces have Q's original orientation and are translates. Their displacement vectors are exactly the lattice

    L = Z t0 + Z t1,

because t2=t1-t0 and the honeycomb is connected. Hence {Q+l : l in L} is the desired tiling, invariant under the nonzero translations t0 and t1.

## Scope

The existing star-list exclusion of mixed P/Q tilings is taken as an input here. This note settles only the remaining Q-only branch. It relies on the cited primary classification, revised in 2026, rather than assuming completeness of Reinhardt's original 1918 proof; the cited authors explicitly identify gaps in the older classification proofs. No assertion about all equiangular hexagons being tileable is used.
