# Regular P5 / 144–126 Q8: smallest full-edge torus

Status: internally proved exact periodic carrier for the entire AABBAABB metric family h>0; independent hostile review pending. Bounded absence for AAABBABB at exactly 2P+1Q. No unrestricted aperiodicity or untileability conclusion.

## Domain derived before enumeration

Dependencies read: research-problem.md, research-protocol.md, 20:22 Astra assessment and its stop warnings, Q8 first gate and hostile review, AA-capacity lemma/review, saturated-star artifact/review, and Q7 minimal-torus script/proof. This changes the blocked local-star mechanism to a single globally complete carrier gate. No star growth or larger quotient is performed.

The reviewed angle reduction forces full-edge stars PPQ at A=144 degrees and PQQ at B=126 degrees. Both surviving words have four A, four B, two AA edges, four mixed public edges, and two private BB edges. There is no public BB edge. A P with zero PP sides would face five public BB edges; one PP side would force a public BB edge among the other four. Consecutive PP sides are impossible. Thus every P has exactly two nonconsecutive PP sides. This pointwise saturation argument covers both words and reflections; asymptotic density equality alone would not suffice.

In a translational torus with p P faces and q Q faces, vertex counting is exact: 5p=2(4q)+(4q)/2=10q, hence p=2q. Both species must occur by the allowed stars. Thus the unique smallest possible inventory is p=2,q=1, with 18 darts, 9 edges, and 6 vertices. This is a smallest-inventory statement, not a reduction of arbitrary periodic tilings to this inventory.

Normalize each regular P independently by rotation so its PP sides are {0,2}; every nonconsecutive pair is rotation equivalent. Its corner types are AAAAB. Regular P reflection changes no shape, so it adds no species. Include Q in both isometry parities, using conjugation and reversed vertex indices to keep counterclockwise boundary orientation. Pair all four PP darts in all three perfect matchings, all six PQ darts with all six Q public darts in all 6! bijections, and pair the two QQ darts with each other (a self-face edge identification). This is 4320 labeled cases per word. There is no quotient by face swaps or residual symmetry. Edge reversals are mandatory in an oriented translation torus. Endpoint compatibility, complete vertex cycles, and exact edge geometry are then checked. Same-face PP identifications are included, even though geometry eventually rejects them.

All proof-relevant arithmetic is in K=Q(w), w=exp(2 pi i/20), or K[h]. The continuum word uses common QQ length h>0; its other six sides are 1, and opposite sides are parallel and equal. The isolated word uses common QQ length -w^7+w^5-w^3+2w. Directions start at 1 and turn by w^2 at A and w^3 at B. The script checks closure and supporting half-planes, including coefficientwise exact positivity for all h>0. No sampling or floating decision is used.

## Complete enumeration results

| Word | Raw cases | Endpoint compatible | Correct vertex stars | Translation holonomy | Area/lattice certificates |
|---|---:|---:|---:|---:|---:|
| AAABBABB | 4320 | 48 | 0 | 0 | 0 |
| AABBAABB | 4320 | 48 | 4 | 4 | 4 |

For AAABBABB, this is complete absence only in the specified 2P+1Q oriented full-edge translational torus domain. No conclusion about larger periodic quotients, plane tilability, or aperiodicity follows. Stop this word here.

## AABBAABB all-parameter carrier and coverage proof

Let P have vertices sum_{j<i} w^(4j), i=0,...,4. Let Q(h) have the native directions and lengths just defined, native corner word AABBAABB, and QQ edges 2,6. The first retained certificate uses representatives

    P, 1-P, 1+w^4-w^4 Q(h).

Their labels are P0,P1,Q. Dart numbers are P0 edges 0–4, P1 edges 5–9, Q edges 10–17. The complete pairing is

    (0,5),(2,7),(1,10),(3,13),(4,15),
    (6,14),(8,17),(9,11),(12,16).

In particular Q edges 2 and 6 self-pair. The six vertex cycles are

    (0,6,15),(1,11,5),(2,8,10),
    (3,14,7),(4,16,13),(9,12,17).

The first four have two P corners and one A corner; the last two have one P and two B corners. Each sums exactly to 360 degrees.

Use lattice basis

    L1=w^6+w^4+w^2,
    L2=(w^7-w^5+w^3-w)h+2w^6-1.

In the displayed edge-pair order the shift coefficients are

    (0,0),(1,0),(0,0),(0,1),(-1,1),
    (-1,1),(-1,0),(0,0),(-1,0).

The script verifies both endpoint equations for every pair as polynomial identities. The determinant equals the sum of the three positive face areas identically:

    det(L1,L2)=(-w^6+w^4+2)h
               -7w^7/2+2w^5-w^3/2+4w.

Its coefficients are real in the distinguished embedding and strictly positive; the retained script checks their algebraic signs. Hence this is a rank-two lattice for every h>0, including arbitrarily small or large h.

For completeness, form the abstract oriented surface by gluing the three polygonal closed disks along the nine paired edges with orientation reversing boundary maps. The face adjacency graph is connected (the explicit pairings connect both P faces and Q). Every dart belongs to one pair and every corner belongs to one of the six listed vertex cycles, so this is a compact connected surface without boundary; each vertex link is one circle. It has Euler characteristic 3-9+6=0 and is orientable, hence a torus.

The developed polygon coordinates modulo the displayed lattice define a continuous map from this abstract surface to the Euclidean lattice torus, because all edge endpoint differences have the stated integral lattice coordinates. It is an orientation preserving local isometry inside faces and across edges. At a vertex the incident convex sectors appear in the cyclic order prescribed by the boundary gluing; their positive angles sum exactly to 2 pi. Successive developments therefore cover a neighborhood exactly once and give a local isometry there too. Thus the map is a local homeomorphism everywhere. A local homeomorphism from a compact connected surface to a connected torus is a finite covering (its image is both open and closed). Its degree equals total developed face area divided by lattice covolume, which is exactly one. It is therefore a homeomorphism and an isometry locally. Lifting the three faces to the universal Euclidean cover produces a covering of the whole plane with pairwise disjoint interiors. This proves global existence and periodicity for every h>0, with no unproved translate bound or limiting argument. Reflections are permitted in the problem; the exhibited carrier itself uses direct copies only.

Consequently every AABBAABB member of this metric family has a periodic escape and cannot be an aperiodic pair with the regular pentagon. This says nothing about other Q angle words or other partner shapes.

## Replay and stopping state

Artifacts are the adjacent .sage script and .json certificate containing every surviving map, exact polygons, periods, edge shifts, and counts. Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-minimal-carrier-sol-2026-10-19.sage

The completed replay uses SageMath 10.9, deterministic exhaustive loops, no seed, no solver and no imposed timeout. An initial run completed mathematics but failed JSON serialization of Sage integers; the retained corrected script converts these integers and replays successfully. No conclusion depends on the failed serialization. A final self-audit adds exact parameter-wide supporting half-plane and area positivity checks. The gate terminates here; no larger q, local expansion, Git operation, discovery-log edit, or novelty claim is authorized by this artifact.
