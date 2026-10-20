# Four congruent pentagons in a convex hexagon force periodic omission

Date: 2026-10-20. Status: finite exact theorem, [independently hostile-reviewed](../reviews/four-pentagon-hexagon-hostile-2026-10-20.md). No claim about arbitrary two-polygon tilings or novelty.

## Claim

If a genuine convex hexagon H is partitioned into four congruent genuine convex pentagons P, then P admits a periodic monohedral tiling. Consequently, a two-shape pair containing P cannot be aperiodic under the stated omission convention. This remains true when the first parent is a similarity image of H. Arbitrary contacts and reflected children are allowed.

The positive periodic constructions imported are the classical pentagon Types 1, 2, and 4 as source-audited in [the monohedral filter](../lemmas/pentagrid-pentagon-monohedral-filter.md). Completeness of the fifteen-family classification is NOT needed: every retained case satisfies a sufficient periodic construction. No negative monohedral inference is used.

## Complete topology reduction

Use the planarized internal seam graph, suppressing degree-two nodes that are no native corner. A seam cycle would enclose a child having no positive-length parent-boundary contact. That convex pentagon would require five distinct neighboring children, impossible with four children. The graph is therefore a forest.

Let I be the number of interior nodes, B the seam endpoints in relative interiors of parent edges, J the number of parent corners incident with a seam, k the number of forest components, and Hflat the inserted flat incidences on child boundaries. Disk Euler and the forest identity give B+J=F+k-1=3+k. Every interior seam node has degree at least three, hence I≤B+J−2k=3−k. Angle counting gives

    3F+Hflat = 2I+4+B,
    12+Hflat ≤ 2(3−k)+4+(3+k−J)=13−k−J.

Thus Hflat≤1−k−J. Since k≥1, equality requires k=1, J=Hflat=0, B=4, I=2. Equality in the degree inequality makes both interior nodes trivalent. The only such tree has two trivalent nodes U,V joined by one edge, with two boundary arms at each. No corner splitting, partial native-side contact, or alternative seam topology remains.

Name the boundary seam nodes a,b on the U end, c,d on the V end. The counterclockwise child loops are

    L = [U,a,C0,C1,b]
    T = [U,V,c,C2,a]
    R = [V,d,C3,C4,c]
    B = [V,U,b,C5,d].

The Ci are the six genuine parent corners. A child at either end has two parent corners; the upper and lower children each have one.

## Exact finite angle domain

Normalize the native U corner of L to index 0 and its handedness to positive. For each of T,R,B choose independently a native phase in 0..4 and sign ±1. This is exactly 10³=1,000 templates. Native corner i of face f is n(f,i)=phase(f)+sign(f)i modulo 5. Native side i has index phase+i for positive sign and phase−i−1 for negative sign.

Let alpha0..alpha4 be P's strict angles. Impose their sum 540 degrees, the U and V sums 360 degrees, and the four boundary seam sums 180 degrees:

    L0+T0+B1 = 360; R0+T1+B0 = 360;
    L1+T4 = 180; L4+B2 = 180;
    R4+T2 = 180; R1+B4 = 180.

The [angle enumerator](astra-four-pentagon-hexagon-tree-2026-10-20.py) uses exact rational matrices and rational polyhedra. Strict angle feasibility introduces delta≥0 with delta≤alpha_i≤180−delta and maximizes delta on the resulting compact polyhedron. Positive maximum is equivalent to strict feasibility. Complete counts are:

| Result | Templates |
| --- | ---: |
| Inconsistent equations | 668 |
| Consistent but no strict angles | 260 |
| Forces adjacent supplementary P angles | 50 |
| Remaining strict templates | 22 |

The 50 supplementary cases satisfy the positive Type 1 periodic construction. The [full JSON](astra-four-pentagon-hexagon-tree-2026-10-20.json) retains all 1,000 phases, signs and statuses, and the affine solution spaces for 22 survivors.

## Seam-length omission certificates

Each seam is a complete native side on both of its children. The five necessary native length equalities, in face-local CCW indices, are

    L.side0 = T.side4;
    L.side4 = B.side1;
    R.side4 = T.side1;
    R.side0 = B.side4;
    T.side0 = B.side0.

The [omission enumerator](astra-four-pentagon-hexagon-omission-2026-10-20.py) combines these homogeneous linear equations with each survivor's angle equations. Exact augmented-matrix rank tests prove that every remaining template implies a Type 2 or Type 4 construction, without choosing or sampling lengths or angles. Here vertex relabeling is old index off+sign*i; outgoing side relabeling is off+i for sign+ and off−i−1 for sign−. With that convention:

* Type 2: A+B+D=360 degrees and c=e.
* Type 4: A+B+D=360 degrees, E=90 degrees, d=e, b=c.

The table gives one sufficient witness per survivor. The normalized L phase/sign is 0/+ in every row.

| T,R,B phases | T,R,B signs | Type | relabel sign | relabel offset |
| --- | --- | ---: | ---: | ---: |
| 0,0,0 | +,+,+ | 2 | 1 | 2 |
| 0,0,3 | +,+,- | 2 | 1 | 0 |
| 0,3,0 | +,-,+ | 2 | 1 | 0 |
| 0,3,3 | +,-,- | 2 | 1 | 0 |
| 2,0,2 | +,+,+ | 4 | 1 | 2 |
| 2,0,2 | +,-,+ | 2 | 1 | 2 |
| 2,0,3 | +,+,- | 2 | 1 | 2 |
| 2,0,3 | +,-,- | 2 | 1 | 2 |
| 3,0,0 | -,+,+ | 2 | 1 | 0 |
| 3,0,2 | -,+,+ | 2 | 1 | 2 |
| 3,0,2 | -,-,+ | 2 | 1 | 2 |
| 3,0,3 | -,+,- | 2 | 1 | 2 |
| 3,0,3 | -,-,- | 2 | 1 | 2 |
| 3,0,4 | -,+,+ | 2 | 1 | 2 |
| 3,2,3 | -,-,- | 2 | 1 | 2 |
| 3,2,4 | -,-,+ | 2 | 1 | 2 |
| 3,3,0 | -,-,+ | 2 | 1 | 0 |
| 3,3,3 | -,-,- | 2 | 1 | 0 |
| 4,0,3 | +,+,- | 2 | 1 | 2 |
| 4,0,4 | +,+,+ | 2 | -1 | 3 |
| 4,2,3 | +,-,- | 2 | 1 | 2 |
| 4,2,4 | +,-,+ | 2 | 1 | 2 |

The [omission JSON](astra-four-pentagon-hexagon-omission-2026-10-20.json) records all sufficient family hits and the seam-length kernel. Its extra H Type 1 hits are diagnostic and are not needed by this proof.

Therefore every geometrically realized first parent has periodic P-only omission. It is unnecessary to solve closure, test overlap, fit a second parent, or select an inflation factor. The otherwise admissible second-parent inventory 7P+H with area eigenvalue (7+sqrt65)/2 must not be pursued for this first parent.

## Scope, replay, and review

The topology proof is unrestricted for four congruent pentagons in a genuine convex hexagon. The finite search includes all rotations and reflections through native phases/signs. It does not claim that every angle assignment geometrically realizes a dissection; the argument only needs that every realization passes these necessary conditions. Stronger geometric filtering could only delete cases.

Replay from the repository root:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-four-pentagon-hexagon-tree-2026-10-20.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-four-pentagon-hexagon-omission-2026-10-20.py

The [independent hostile review](../reviews/four-pentagon-hexagon-hostile-2026-10-20.md) reconstructed the face words, verified the forest reduction including possible boundary point contacts, reproduced the 1,000-case angle census, and checked the outgoing-side reflection shift in all 22 positive Type 2/4 implications. Its separate [checker](../reviews/verify_four_pentagon_hexagon.py) passed.
