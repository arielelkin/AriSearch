# Hostile review: two-parent P5/Q7 saturated cap design

Date: 2026-10-19. Verdict: **PASS / valid restricted obstruction**.
Independent reviewer; producer files were not edited. Replay regenerates the adjacent JSON deterministically.

## Exact claim reviewed

Reviewed `research/searches/two-parent-p5-q7-cap-design-2026-10-19.{md,py,json}` against `research-problem.md`, `research-protocol.md`, and `research/lemmas/six-child-topology-substitution-consequences.md`. The claims are rejection of two explicit incidence maps and exclusion of simple triangulated dual disks with respectively four or three boundary vertices and five interior vertices, each interior vertex requiring degree at least five. No exclusion of all maps for M=[[7,5],[2,3]] follows.

## Assumptions and arithmetic

For the P column, sum(6-ni)=7-2=5 and 6-p=1, leaving defect budget 4. For Q, the corresponding quantities are 5-3=2 and -1, leaving budget 3. The allocations (B,J,D,H)=(4,0,0,0),(3,0,0,0) therefore agree with the exact defect identity. The characteristic polynomial is mu^2-10mu+11; mu=5+sqrt(14) and the area ratio (mu-7)/2 are correct.

The single connected outer arc per boundary child, absence of repeated labels, simple dual, trivalence, and H=0 are hypotheses of the chosen mechanism. They are not consequences of the matrix or defect budgets. In particular, no conclusion here rules out multiple outer arcs, other defect allocations, or other dual topology. The text states this restriction explicitly, so there is no hidden quantifier promotion.

## Explicit disk verification and replay

Ran:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-parent-p5-q7-cap-design-2026-10-19.py

Replay exited successfully. Independently reconstructed dual edges and vertex links from the retained JSON. Every internal edge has two incident triangles, every boundary-cycle edge has one, every interior link is a connected cycle, and every boundary link is a connected path. Euler V-E+T=1 holds: P gives (9,20,12), Q gives (8,18,11). This verifies combinatorial disks rather than relying solely on incidence totals.

Their primal seam graphs have respectively I=12,11 and E=20,18, agreeing with E=I+F-1. Boundary words contain each parent corner once, in order, with 4 and 3 active seam nodes. Counting one native segment per word interval gives total child-side counts 49 and 46, as required by the intended inventories, but their distributions fail. Independently checked native counts agree with the reported tuples. The vertex e has three sides in both; no H=0 role assignment supplies five genuine pentagon corners. Global angle totals 31pi and 30pi do not cure that failure.

## Attack on the stronger obstruction

In a simple triangulated disk E=3V-b-3. Thus E=20 for P and 18 for Q. With five interior vertices, sum of interior degrees is 2eII+eIB=eII+E-eBB and is at least 25; eBB>=b. Consequently Q requires eII>=10, exceeding the planar simple five-vertex bound 9. This argument does not assume a particular annulus or placement of the heptagons.

For P, eII>=9 forces eII=9 and eBB=4, with equality throughout the degree bound. A planar simple graph on five vertices and nine edges is maximal planar (abstractly K5 minus an edge). In its inherited disk embedding the unbounded face is triangular. Its other two vertices lie inside that triangle. Every boundary vertex of the whole disk is outside the triangle; an edge from either trapped vertex to a boundary vertex would cross the triangle. Each trapped vertex therefore has total degree at most four, contradicting degree at least five. Changing which children are heptagons only increases required degrees. No exceptional embedding evades this separation argument.

## Defects, repairs, and remaining uncertainty

No mathematical defect requiring repair was found. The replay checks fixed examples and arithmetic; the universal cap exclusion rests on the preceding planar proof, not an exhaustive enumeration. The producer script does not independently certify geometric realizability, and none is claimed. The unresolved construction obligation remains finding another admissible incidence mechanism and satisfying angles, lengths, coordinates, extension, and shape-only forcing. This review establishes no claim about arbitrary convex dissections, all maps for the matrix, periodicity, or the main two-tile problem.
