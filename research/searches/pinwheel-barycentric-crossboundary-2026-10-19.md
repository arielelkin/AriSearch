# Pinwheel midpoint/corner-star retiling: common-center family rejected

Status: exact restricted exclusion; [independent Sol hostile review](../reviews/pinwheel-barycentric-center-family-hostile-sol-2026-10-19.md) valid within its finite-patch scope. No target solution or two-tile candidate. This is a cross-boundary retiling, not whole-triangle fusion or a Voronoi construction.

## Explicit construction and scope

Start with T=((0,0),(2,0),(0,1)). The large similar triangle B=((0,0),(5,0),(4,2)) has five congruent 1:2 right-triangle children

1. ((0,0),(2,0),(2,1));
2. ((2,0),(4,0),(4,1));
3. ((4,0),(5,0),(4,2));
4. ((2,1),(4,1),(4,2));
5. ((2,0),(4,1),(2,1)).

Map B to T by N(x,y)=(2-(2x+y)/5,(x-2y)/5). At each further step transport these normalized children by the unique similarity sending T's right vertex, long-leg endpoint, short-leg endpoint to those of each parent. Three subdivisions give 125 exact rational triangles. Their containment, pairwise interior disjointness, and total area1 are checked exactly. No literature theorem or infinite source existence is needed for the local rejection: the family is rejected on this explicit finite pinwheel substitution patch.

Planarize every T junction using all triangle vertices. On every resulting edge segment use its midpoint. Each triangle has the same center rule

C=O+p(L-O)+q(S-O), p>0, q>0, p+q<1,

where O is its right-angle vertex, L the long-leg endpoint, S the short-leg endpoint. For each planarized source vertex v, assemble all corner regions bounded by v, its two incident segment midpoints, and C in each incident face. These regions partition each source triangle and join across its boundaries. The new cell boundary alternates edge-segment midpoints and triangle centers. All81 fully interior vertex cells of the fixed depth3 patch are audited; boundary cells are excluded. The seam rule is the midpoint throughout. Other seam rules, center rules depending on environment, or changed sources are outside.

The rule crosses source boundaries and automatically produces a plane cover if applied to an appropriate entire locally finite triangulation. This observation does not imply convexity, a two-class output, source decoding, or aperiodicity.

## Decisive family obstruction

Write F=-4p²+3p-q²+q/2 and G=-4p²+p-q²+q/2. Four positively oriented consecutive boundary turns in three exact interior source stars are F/125, G/125, -G/125, -F/125. Their source vertices and raw boundary turn indices are respectively

- (1/25,2/25), indices0 and2;
- (1/25,22/25), index6;
- (1/5,1/5), index4.

Convexity requires every turn nonnegative. The first/opposite pair forces F=0, the second/opposite pair G=0. Since F-G=2p, these imply p=0, contradicting an interior center. Thus **no common interior affine center rule with segment midpoints yields all-convex dual cells even on this fixed depth3 patch**. This also excludes any infinite source containing this patch with this local rule. It is not an impossibility theorem for arbitrary two convex polygons or arbitrary pinwheel surgeries.

A single QF_NRA solve of all465 nonidentically-zero turn inequalities returned UNSAT (Z3 4.16.0,30s cap). The retained core has six inequalities; four suffice for the displayed elementary proof. The independent family fixture checker verifies the four determinant identities without invoking Z3. The family certificate retains the symbolic predecessor/current/successor triples. Solver UNSAT is corroboration; the algebraic contradiction carries the exclusion.

## Two fixed-center gates and minimal witness

Centroids p=q=1/3:81 interior cells,50 convex,31 nonconvex; the convex cells have3 congruence classes. Exact side-free full squared-distance matrices, minimized over cyclic shifts and reversal, classify congruence.

A minimal centroid failure at v=(1/25,2/25) is a three-triangle T-star. Scaling by150 gives source triangles

((0,0),(12,24),(0,30)),
((18,36),(6,12),(18,6)),
((6,12),(0,0),(30,0)).

Their squared side lengths are180,720,900. The reduced dual polygon is

(3,6),(12,4),(12,9),(14,18),(4,18),

whose exact turns are110,45,-10,90,120. Thus it is a concave pentagon. The independent minimal checker verifies this fixture.

The minimal-star obstruction alone does not exclude varying centers. In the same scaled T-star the six turns are

-90(8p²-6p+2q²-q), 45(4p+2q-1),
-90(8p²-2p+2q²-q), 45(4p+2q-1), 0,180q.

At p=q=1/5 the reduced local cell is convex. The one authorized repair gate at that parameter on the SAME patch gives81 cells,40 convex,41 nonconvex; the convex subset has2 classes. No patch growth or grid scan was done. The common-center contradiction above shows that further parameter tuning in this family cannot repair all cells.

## Replay and retained evidence

Run each command with the repository wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pinwheel-barycentric-crossboundary-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pinwheel-barycentric-crossboundary-2026-10-19.py --center fifth
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/check-pinwheel-barycentric-crossboundary-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pinwheel-barycentric-center-family-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/check-pinwheel-barycentric-center-family-2026-10-19.py

Producer uses standard-library exact Fractions; parameter gate uses SymPy and Z3; the independent family checker uses SymPy only. All files share this report's prefix except the family files. Certificates are adjacent JSON files. Domain is fixed, deterministic, no seed, no orientation quotient in enumeration. Congruence permits reflections. Each run finished; no timeout or incomplete domain. No current-literature novelty claim is made for this simple rule or restricted obstruction. No discovery-log or git edits were made by this worker.

Route closed for the specified common-center/midpoint rule. Reopening requires an explicit changed seam or environment-sensitive center mechanism that evades the opposing turn identities; increasing patch depth or repeating the same parameter solve cannot do so.
