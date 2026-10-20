# Pentagon / regular hexagon: a corner-expansion obstruction

Status: proved internally, awaiting independent hostile review. Narrow exact family obstruction, not the unrestricted two-convex-tile theorem. No novelty claim.

## Exact claim

Let P be any strictly convex pentagon whose angles are four copies of 100 degrees and one of 140 degrees. Let H be a regular hexagon of arbitrary positive side length. In every unrestricted plane tiling using isometric copies of P and H, no copy of P occurs. Consequently this palette always has the regular-hexagon periodic escape and cannot be aperiodic.

The point of this gate is that mixed local vertex stars DO exist: 100+120+140=360. Their required corner multiplicities nevertheless prevent any pentagon occurrence, even one of zero density.

## An exact P

Set z=exp(2 pi i/18), the root of x^6-x^3+1 with complex argument 20 degrees. Let n(k)=(Re(z^k),Im(z^k)), for k in (0,4,8,12,16). Define P by n(k) dot x <=1. Vertices are intersections of consecutive lines; for normals (a,b),(c,d) the intersection is ((d-b)/(ad-bc),(a-c)/(ad-bc)). Normal gaps 80,80,80,80,40 degrees make this a strictly convex pentagon of the specified angles. H may have vertices (cos(j pi/3),sin(j pi/3)), j=0,...,5. The exact checker for the related angle gate reconstructs and verifies P over the real algebraic field:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/pentagon-hexagon-100-140-angle-obstruction-2026-10-19.sage

## Complete proof, including partial-edge contacts

Tilings by finitely many compact shapes are locally finite: if a tile meets a compact set K it lies in its D-neighborhood, for D the maximal diameter. Each tile contains a disk of a common positive radius r; disjoint tile interiors give disjoint disk interiors in that bounded neighborhood. Only finitely many tiles therefore meet K.

At any tile vertex v, incident sectors sum to 360 degrees. Every genuine corner angle is at least 100 degrees, so at most three genuine corners meet. If v were in the relative interior of some tile edge, that tile would contribute a straight 180-degree sector; the other sectors would have to sum to 180 degrees. One genuine corner is strictly below 180, whereas two sum to at least 200, impossible. Thus no T vertex occurs.

The complete genuine-corner equation is 5a+6b+7c=18, where a,b,c count 100-,120-,140-degree corners. The only solutions are (a,b,c)=(0,3,0) and (1,1,1). Indeed one or two genuine corners sum to strictly less than 360 and four sum to more; with three corners, subtracting six times their count yields c=a, whence these two solutions. Thus every 100-degree corner of P meets exactly one 140-degree corner of another P, and one corner of H. Every 140-degree corner meets exactly one 100-degree corner of P.

Form a directed graph on P copies: each of a copy's four 100-degree corners gives an arrow to the P copy contributing the incident 140-degree corner. Each node has four distinct outgoing targets: a target P has just one 140-degree corner at one point, so cannot serve two different corners of the source. Each node has indegree exactly one because its unique 140-degree corner lies in a unique (100,120,140) star. Reflections do not affect these counts.

Suppose P occurs and start with its singleton node set S_0. Define S_(n+1) to be the outgoing targets of S_n. Since every node has four outgoing targets and no target has two incoming arrows, |S_n|=4^n. Choose one reference point in each P copy, for example its centroid. An arrow joins copies sharing a vertex, so their reference points have distance at most 2D, where D=diameter(P). Hence all 4^n copies in S_n have reference points within distance 2nD of the initial point, and their whole polygons lie in the disk of radius (2n+1)D. Disjoint interiors imply

    4^n area(P) <= pi (2n+1)^2 D^2.

The inequality fails for sufficiently large n, a contradiction. No P occurs. The only admitted tilings are regular-hexagon tilings, and the standard hexagonal lattice supplies a doubly periodic tiling.

## Scope and next changed gate

No edge-length matching restriction, edge-to-edge hypothesis, repetitivity, positive tile frequency, or bounded-period search is used. The graph contradiction excludes sparse pentagon defects as well as positive-density mixtures. The local star itself is realizable, so this is a global obstruction beyond the empty-star gate.

To evade this obstruction while retaining the 100/120/140 palette, the second polygon needs both 100- and 140-degree corners; such corners could transmit the required pairing through chains of unbounded length, destroying the bounded-distance branching graph on P copies. A hexagon's angle total forces equal numbers of 100 and 140 corners. This changed case has a genuine neutral transmission mechanism, and the present proof does not exclude it.

Dependencies: elementary geometry and exponential versus quadratic growth. Literature boundary: no primary literature consulted for this elementary derivation; no priority asserted. Supporting exact calculation: research/searches/pentagon-regular-hexagon-stars-2026-10-19.py.
