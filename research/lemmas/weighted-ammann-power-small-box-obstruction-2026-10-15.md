# Three persistent power-cell classes in the fixed Ammann mean-site family

Status: independently hostile-reviewed VALID, including the finite-cell radius repair
and the every-source hierarchy bridge; [fresh review](../reviews/weighted-ammann-power-hostile-2026-10-15.md). This is a finite obstruction to the specified construction family, not a result about the unrestricted two-polygon problem.

Let w=exp(iπ/5), and take the reviewed Ammann source with J=1/2+(4/5)w. Put one site at the arithmetic mean of the genuine vertices of each source polygon H6,P1,P2. Give these types weights 0,a,b respectively. Define rho as the minimum distance from a prototype mean to any of its supporting side lines, R as the maximum distance from a prototype mean to any of its vertices, C=sqrt(R²+rho²), and L=C+sqrt(C²+rho²).

**Finite witness.** For every |a|,|b|≤rho²/2, the source-cell contexts described below give power cells with respectively seven, six, and five genuine corners. Consequently this power partition has at least three congruence classes throughout the entire closed weight box. No parameter stratum survives the first gate. This statement applies to EVERY legal Ammann source at the specified J, by the exact supertile embedding and the reviewed arbitrary-depth Robinson composition argument below. No minimality theorem or finite-patch claim of exhaustive corona coverage is assumed.

## Exact source occurrence and geometry

The producer uses the existing exact Robinson sun seed and five subdivisions, pairs mirror triangles into rhombs, scales by phi^5 to unit edge, and applies the reviewed Ammann decoration with options (B,B). The source reconstruction is a dependency of the existing [Ammann forcing theorem](../lemmas/ammann-forcing-aperiodicity.md), implemented in [the reconstruction](../searches/ammann-two-class-reconstruct.py). An additional exact [source embedding checker](../searches/weighted-ammann-power-source-embedding-2026-10-15.py) removes any assumption that the centered sun patches form a nested sequence. It selects all source rhombs with a vertex within distance5 of any witness mean (137 rhombs), and matches every selected decorated reference frame into the ninth subdivision of the SINGLE Robinson triangle rec.sun()[0]. The match is the translation

    delta=34+8w+26w²−13w³,

with no rotation or reflection. Thus these are interior patches of an actual Robinson supertile. To prove occurrence in EVERY legal source, apply Lemma6 of the reviewed Ammann forcing theorem ten times. Choose any tenth-level Robinson parent half. The explicit substitution rule for either parent type contains a red child (red gives one red and one blue; blue gives one red and two blue). Consequently the original unit tiling contains the nine-level deflation of a red half. Up to isometry this is exactly the single supertile used in the retained embedding, so all137 decorated rhomb frames and all three witness contexts occur in that source. Root independently checked this use of arbitrary-depth composition and both substitution rules; the fresh reviewer also checked the exact child counts. No centered-sun nesting or repetitivity assertion is needed. The checker proves each unit rhomb has diameter less than2; every rhomb meeting a radius3 witness disk has a vertex within5 and is selected. The main gate proves L+2R<3 and each witness is more than3 from the original patch boundary. Therefore the embedded patch supplies every required source tile and competitor. The retained exact source-embedding certificate lists all137 typed reference frames and the translation. No centered seed extendability or complete corona census is assumed.

Decoration edges plus the rhomb patch boundary are traced into faces. The checker verifies exact total positive face area equal to the rhomb area and exactly one negatively oriented outer face. Every complete internal face is strictly convex and exactly congruent, allowing reflection, to one of the three reviewed prototypes. There are 650 such faces. Sites are their genuine arithmetic vertex means.

Indices are deterministic face-trace indices in the producer, zero-based. The JSON certificate additionally stores all source polygons, all sites with types, the boundary segments, and the witness coordinates in the exact basis 1,w,w²,w³.

| Source face | Source type | Power-cell corners | Squared distance to patch boundary (approximate) |
|---|---|---|---|
|43|P1|7|31.1996054233|
|44|H6|6|24.3379758348|
|45|P2|5|25.1854681568|

Approximate constants, for orientation only, are rho²=0.0466681472606, R²=0.493755685157, and L=1.50135452420. All proof comparisons use exact algebraic real numbers, not these decimals.

## Completeness of the finite neighbor set

Every source tile contains the open rho-disk about its site; disjoint tile interiors imply distinct site separation at least 2rho. Since any two weights differ by at most rho², all sites stay strictly active. Every point lies within R of some site, so every global cell lies in the closed C-disk about its generating site.

For a competitor at distance d>L, throughout that disk the power difference in favor of the generating site is at least d²−2Cd−rho²>0. Such competitors are redundant there.

For each of the three witnesses, the checker verifies that its distance to EVERY rhomb boundary segment exceeds L+2R. The witness site is inside the patch. A missing complete source tile either lies outside the patch or meets its boundary; the whole tile has diameter at most 2R. Thus no missing source mean can lie within distance L of the witness. The finite competitor set contains precisely all reconstructed means at distance at most L.

To bridge the bounded global cell to the finite half-plane intersection, the checker also verifies that every candidate finite-cell vertex, at every weight-box corner, has squared norm at most C². These vertices depend affinely on (a,b); convexity of squared norm puts every such vertex, and hence the entire finite polygon, in the C-disk throughout the box. Therefore omitted competitors cannot cut it. The finite polygon equals the global power cell, not merely a superset of it.

## Closed-box corner persistence

Write y=x−c_i. The j-th competitor gives

    2(c_j−c_i)·y ≤ |c_j−c_i|² + weight(i) − weight(j).

Normals are constant and offsets affine in a,b. At weight zero, all feasible pair intersections are computed exactly and duplicate vertices removed. Their active-side incidence gives a cyclic order, and the checker verifies every zero-weight turn is strictly of the same sign. The respective distinct vertex counts are seven, six, five.

For each retained vertex pair, its line intersection is affine in (a,b). At all four corners of the CLOSED box the checker verifies every competitor inequality. Every such slack is affine, so nonnegativity holds everywhere in the box. It also checks that each consecutive edge is parallel to its zero-weight edge and has strictly positive projection onto that edge at all four box corners. This projection is affine, hence stays positive throughout the box. All corners remain genuine and have their original strict turn sign because the directions of consecutive edges are fixed.

The heptagon has a persistent four-site power vertex: three competitor lines (indices46,47,48) meet there. This is retained exactly. Non-strict competitor inequalities are intentional. In particular, a slack zero at the box center and nonnegative at all four box corners is identically zero. No generic trivalence assumption or deletion of boundary strata is used.

The pair of active competitor indices defining each cyclic vertex is retained in the certificate:

- Face43: (44,45),(44,47),(46,47),(48,51),(51,52),(50,52),(45,50).
- Face44: (43,45),(43,47),(47,66),(64,66),(49,64),(45,49).
- Face45: (43,44),(43,50),(50,54),(49,54),(44,49).

The finite intersection is bounded at weight zero. Its recession cone depends only on the fixed normals, so it is bounded for every weight. The feasible affine vertices with the same nonzero edge cycle therefore describe that entire intersection. This proves the stated corner counts for every parameter, including all one- and zero-dimensional strata. Three different corner counts imply three different Euclidean congruence classes, allowing reflections.

## Replay and scope

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/weighted-ammann-power-gate-2026-10-15.py

The admissibility bridge replays separately:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/weighted-ammann-power-source-embedding-2026-10-15.py

To regenerate the retained exact geometry, append to the main checker:

    --output research/certificates/weighted-ammann-power-gate-2026-10-15.json

The script uses exact Sage AA comparisons; decimal prints are diagnostics. The existing reconstruction uses numerical angular ordering when tracing its planar graph, followed by exact geometry and area checks; this dependency is explicit. The new half-plane and corner-persistence gate has no floating predicate. It enumerates neither larger quotient tilings nor all possible source coronas. The specified small weight box is excluded; changing sites, source metrics, or expanding the box is outside this result. The unrestricted main problem remains unresolved.

The [independent checker](../reviews/weighted-ammann-power-independent-2026-10-15.py)
rebuilds exact angular face order, clips all cells independently, checks the
complete source embedding and the hierarchy child counts. The geometry and
embedding records are [retained](../certificates/weighted-ammann-power-gate-2026-10-15.json)
[separately](../certificates/weighted-ammann-power-source-embedding-2026-10-15.json).
All checks passed. The proof applies only to the stated fixed source metric,
fixed vertex-mean sites and closed weight box.
