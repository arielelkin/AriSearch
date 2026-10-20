# Independent hostile review: six-boundary obstruction and seven-boundary pivot

Date: 2026-10-19. Verdict: **VALID with strictly combinatorial scope; convex metric realization UNRESOLVED**.

## Claim and inputs

Reviewed `research/searches/six-boundary-substitution-2026-10-19.{md,py,json}`, the research problem, protocol sections 8, 11, 19, the five-interior native cap lemma, and the two-parent junction design. No coordinate realization, substitution existence, plane extension, recognizability, forcing, or aperiodicity claim is certified. No source, certificate, discovery-log, or git edits were made.

## Six-boundary obstruction

The general finite convex dissection identity is correctly applied: seven pentagons and three heptagons in a heptagon give B+2J+2D+H=5. Six distinct positive-length single outer arcs force at least six distinct active transitions, hence B+J>=6, contradicting that identity. Parent-corner transitions cost two rather than one, so allowing them cannot evade the proof. Higher seam degrees and flat incidences also have nonnegative costs. The restriction to six distinct single-arc boundary children is explicit; the scalar bound does not establish impossibility for every smaller boundary allocation. The displayed angle deficit is the same count obstruction, correctly not presented as independent. The P companion ledger and original matrix arithmetic are correct.

## Pivot disks and primal reconstruction

The three inner fan triangles and eleven annulus triangles form an oriented triangulated disk with five interior vertices and six boundary vertices. Attaching (a1,a2,e0), and additionally (a5,a0,e1) for P, along boundary edges preserves disk topology. Shared oriented edges cancel; the stated boundary cycles are exact. Interior links are cycles and boundary links are paths. Thus this assertion follows constructively, not merely from Euler characteristic.

For Q the resulting disk has 12 vertices, 26 edges, 15 triangular faces and boundary length seven. For P these counts are 13, 28, 16 and eight. Every interior vertex has degree five. The stated boundary degree lists and corner allocations give native counts degree+1+c equal to five or seven, with species totals Q:9P+3Q and P:11P+2Q. The parent allocations sum to seven and five respectively.

The dual-to-primal reconstruction is sound as a cell complex: a face becomes a trivalent seam vertex, a dual edge becomes a seam joining its two face vertices or its face vertex and boundary endpoint, and each dual vertex becomes one disk child. The reverse oriented links give consistently oriented child words. I independently read the retained JSON and checked that every f node occurs three times, every t node twice, every u node once, every child word has distinct entries and its prescribed length, and each seam occurs with opposite direction in its two child words. This strengthens the source checker, which checks consecutive membership but does not explicitly assert opposite primal directions. All checks passed. Boundary words concatenate in the given outer order to a cycle with exactly the prescribed parent corners. There are no hidden extra native or flat corners in this abstract reconstruction.

## What P and Q labels mean

The labels correctly designate combinatorial pentagonal and heptagonal faces: their native words have respectively five and seven vertices, all intended to be genuine corners. They do **not** establish that these faces admit simultaneous convex straight-edge embeddings, nor that all P faces are congruent and all Q faces congruent. Even a topological polygon with five or seven named vertices has no angles until metric data are assigned. Consequently “abstract incidence pair” is valid terminology only with this distinction. “Convex pentagon/heptagon child polygons even abstractly” cannot be read as a proof of convexity or realizability. The manuscript expressly retains those metric requirements as unresolved, so no claim needs invalidation on this ground.

## Inflation and necessary equations

For columns (11,2) and (9,3), the characteristic polynomial is mu^2-14mu+15. Its Perron root is 7+sqrt(34), and r=(mu-11)/2=(sqrt(34)-4)/2 is positive. The area relation uses the left area eigenvector (1,r), giving mu=11+2r and mu*r=9+3r. The common length inflation is sqrt(mu). These formulas are correct conditional on a geometric substitution; they supply no geometry.

Angle requirements are necessary: native angle sums 3pi and 5pi, strict bounds (0,pi), three-child sums 2pi, transition sums pi, and parent-corner equality. Cyclic phases and reversal cover all rotations/reflections of an unmarked polygon word. The total ledgers 66=45+14+7 and 69=48+16+5, and the corresponding angle totals, are correct. These linear requirements have not been solved, and their global sums alone are insufficient.

The vector conditions are necessary when R_v means the orthogonal linear part of the child isometry and x_v its translation. Seams here have no intermediate flat corners, so whole native edge matching is the appropriate condition. Opposite edge vectors and endpoint coincidence, closed strictly convex native vector words, ordered collinear boundary subdivisions, and scaled parent edge sums are all necessary. Nonoverlap and the common geometry linking angle data to vector data remain essential; independent angle and vector assignments would not suffice. The manuscript retains nonoverlap and simultaneous realization as an explicit gap. A reflected parent can be normalized by the common coordinate frame, so the reference to common parent rotation creates no necessary-condition error.

## Attacks, defects, and limits

Attacks checked: orientation reversal, an Euler-only false disk test, duplicate primal corners, wrong seam direction, missing parent corners, species versus valence confusion, use of a right area eigenvector, conflation of angle totals with feasibility, and inference of convexity from an abstract cellulation. None invalidates the restricted claims. No repair was made. No angle phase enumeration or metric solve was performed. The five-interior cap lemma imposes b>=6 in its stated class and is compatible with b=7 and b=8 here; it does not certify those cases geometrically.

Final verdict: the six-boundary 7P+3Q obstruction and the explicit pivot **topological/native-incidence** pair are valid. Whether that pair has any realization by two congruence classes of convex polygons remains unresolved. This review supplies no evidence of a geometric substitution or aperiodicity.
