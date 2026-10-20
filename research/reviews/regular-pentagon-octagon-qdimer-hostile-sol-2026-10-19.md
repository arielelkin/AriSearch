# Hostile independent review: isolated AAABBABB two-Q carrier

Verdict: **PASS** for the exact periodic plane witness. **NARROW** for the finite-domain claim: exactly four P and two Q faces in an oriented full-edge translation quotient under the previously reviewed star and P-normalization reductions. The two retained maps encode the same geometric tiling; they are not two distinct physical examples. No claim about arbitrary convex octagons or the unrestricted research problem follows.

Read AGENTS.md, research-problem.md, research-protocol.md, the Q8 first gate, the minimal-carrier hostile review and the new qdimer script, JSON and completed report. This review independently reconstructs the new geometry and audits the enumeration logic. It does not rerun the older palette classification or supply a second full combinatorial enumeration.

## Independent exact geometry

The companion Sage checker imports no producer code. It constructs Q from the A/B exterior angle walk, then solves its two-real-variable closure equation for the private edge lengths. This independently gives equal positive private lengths. It constructs the six direct placements from explicit rotations and translations and the displayed two lattice vectors. Every nonincident vertex lies strictly to the left of every oriented edge of every representative polygon, proving simple strict convexity and positive orientation. The determinant is strictly positive and equals exactly the total signed face area (approximately 21.0947567836472); the decimal plays no role in any decision.

Rather than importing gluing pairs, the checker searches all representative edges for an opposite edge vector whose endpoint displacement has integral lattice coordinates. Every dart has exactly one mate. It checks mate involution, opposite shift, all endpoint equations, all twelve single three-corner vertex cycles, their APP/PBB labels and their exact 360 degree angle sums. Face adjacency is connected and 6−18+12=0. It then compares every advertised endpoint equation and shift in both JSON records against these independently constructed geometric polygons.

As a separate global attack, the checker transforms the polygons to exact real algebraic lattice coordinates. For each ordered face pair, the necessary intersection inequalities bound each integer shift between ceil(minimum first−maximum second) and floor(maximum first−minimum second). All 36 nonidentity candidates in these complete bounds are tested by exact Sage Polyhedron intersection; every intersection has dimension less than two. This includes same-face nonzero translates. Hence no distant or nearby interior overlap is omitted.

## Reflection parity and corrected QQ alternatives

The positively oriented reflected walk R_i=conjugate(Q_{−i}) has private indices 4 and 1, since edges transform with source index −i−1. Native private indices are 3 and 6. Independently subtracting the edge direction exponents gives the four QQ tests: direct straight (10,10), direct swapped (2,18), reflected targets (4,1) gives (14,10), reflected targets (1,4) gives (2,2). Exactly the first and last pass. Thus the reflected swapped matching must be retained. Omitting it would invalidate a claimed exhaustive orientation enumeration.

The exact symmetry z↦Q_2−w² conjugate(z) preserves the Q vertex set. In the two JSON records, Q1 has the identical geometric vertex set with a cyclic indexing shift of two, and all other representative polygons are identical. Both maps are physically valid because reversed indexing restores counterclockwise boundary orientation after reflection. They represent duplicate geometric data, which does not weaken the positive existence conclusion.

A one-face QQ self-pair would require its native private directions w^7 and w^15 to be antiparallel; their ratio is w^8, not −1. Reflection does not repair this. Therefore with two Q faces every private dart pairs across the faces and the two permutations just analyzed exhaust QQ possibilities.

## Topological coverage audit

Gluing the six oriented polygon disks along the verified orientation-reversing edge maps yields a compact connected oriented surface. Each vertex has one link circle made of three positive sectors with total angle 2pi. Endpoint identities modulo the rank-two lattice make the coordinate map to the flat torus continuous. In face interiors it is an isometry; across an edge the two positive orientations occupy opposite half neighborhoods. At vertices, the single link and positive 2pi angle sum imply winding one, hence a local isometry. Angle sums alone without the single-link check would not suffice.

A local homeomorphism from this compact surface has open and closed image in the connected target torus, hence is onto and is a finite covering. Its degree is the total positive face area divided by target covolume, exactly one. Therefore it is an isometric homeomorphism, and lifting gives a plane tiling with both lattice periods and disjoint interiors. This proves full coverage and excludes overlaps. Independently, the exact intersection check plus equal area also proves coverage: compact representatives and a discrete lattice give a closed locally finite union; an omitted point would give an omitted open set of positive torus area, contradicting equal area.

## Finite domain and limits

Under the reviewed normalization, each P has PP sides {0,2} and one PQ side each of AA, AB and BA type. Each Q has two public edges of each type. Numbering the four P faces by the four receiving Q AA darts removes only face relabeling. The remaining two bijections give 4!²=576 possibilities for each passing QQ case; checking the single rotation derived from each AA edge against its other two PQ edges is necessary for any translation quotient. The eight remaining PP darts have all 105 perfect matchings, including self-face matches. Vertex-link filtering is correctly applied after direction reversal. The producer counts are 1152 PQ choices, two PQ direction survivors, 210 PP matchings, four PP direction survivors and two star survivors. These counts are audited from source logic, not independently reenumerated. Their exhaustive finite scope does not include larger inventories or general cylinder quotients, and is unnecessary to certify the positive counterexample to aperiodicity.

No new scope obstacle was found to combining this witness with the previously reviewed AAAABBBB capacity exclusion and all-positive-parameter AABBAABB periodic carrier within the already classified regular-P5/four-A-four-B Q8 palette. That synthesis still depends on the exact hypotheses and completeness of those earlier reviewed reductions; this report does not enlarge them.

Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-octagon-qdimer-hostile-sol-2026-10-19.sage
```

Completed exit 0 under SageMath 10.9, printing PASS and 36 translate tests. All proof decisions use exact cyclotomic or ordered real algebraic arithmetic. No randomness, tolerance, solver timeout, Git edit or discovery-log edit. No substantive defect found in the completed producer report.
