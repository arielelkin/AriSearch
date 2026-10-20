# Independent hostile review: regular pentagon / 144–126 octagon

Reviewed artifacts: `research/searches/regular-pentagon-octagon-144-126-first-gate-2026-10-19.{md,sage,json}`. Reviewer independently read the problem and protocol §§8,11,19. No plane existence, periodicity, aperiodicity, or novelty claim is reviewed as proved here.

## Claims and reconstruction

The unrestricted contact reduction is valid. In a locally finite tiling by these fixed compact positive-area tiles, a noncorner point on a side contributes a straight sector. The remaining half-plane cannot be filled by one allowed corner (108°,126°,144°), or by two or more corners since their sum is at least 216°. Thus T junctions and partial-edge endpoint contacts are excluded. A genuine corner cannot sit inside another side. Exactly three corners meet: two are insufficient and four exceed 360°. Solving 6p+7b+8a=20 with p+b+a=3 gives only (p,b,a)=(2,0,1),(1,2,0). This also excludes single-prototile tilings.

At A both Q sides face regular unit P edges. At B one side faces P and the other Q. Therefore the QQ edges are precisely a matching covering all four B corners; there are two BB edges and six unit edges. This is a consequence of geometry, including reflections. There is no hidden edge-to-edge premise.

Enumerating all 70 labeled 4A4B words and all two-edge subsets before quotient independently gives precisely the canonical word/matching pairs AABBAABB/(2,6), AAABBABB/(3,6), AAAABBBB/(4,6). Reversal and rotation preserve the contact constraints. AABBABBA lies in the AAABBABB orbit. No surviving word has an additional inequivalent matching missed by canonicalizing the word first.

With d0=1 and turn at vertex i equal to 36° or 54°, the closing turn at vertex zero is automatic because the total exterior turn is 360°. The two unknown lengths satisfy a real two-dimensional linear equation. The nonsingular determinants give x=y=z+conjugate(z)=2cos(18°)>0, agreeing exactly with the retained cyclotomic expression. Every nonincident vertex lies strictly inside each directed edge half-plane. The checker uses QQbar algebraic real/imaginary coordinates independently of the search's cyclotomic cross-product function.

For AABBAABB, the unknown directions are opposite and the fixed-edge sum vanishes, so closure is exactly x=y=t with t>0; there is no isolated solution hidden in this singular case. Positive edge lengths, closure, and a direction sequence whose positive turns sum to 360° give the convex boundary. Equivalently the t=0 boundary contracts the two QQ edges to a convex hexagon and positive t adds a segment. This proves strict convexity for t>0, but does not audit forced neighborhoods throughout that continuum. Nothing in the isolated-candidate computation eliminates this family.

For each isolated metric, the six P placements outside Q's six unit edges are unique regular pentagons. Four pairs at A must share unit PP sides; their exact two common vertices and unit separation are checked. Distinct forced P copies have disjoint interiors. The independent checker additionally includes Q versus each P in its pair audit.

Each isolated Q has two target and two source QQ edges. Two orientation parities give eight joins per metric, sixteen total. Reflecting the entire assembly gives no new isometry class; if counted as sixteen placements per metric, those additional placements are global reflections of these eight. The direct isometry reverses edge endpoints; the indirect isometry preserves endpoints while conjugating. Both put the moving Q on the exterior side. All lengths equal, so every such seam is metric-compatible. No assumption fixes a chirality. Exact duplicates must be merged as one physical tile, not called overlaps; all other tile pairs must have disjoint interiors.

## Adversarial checks and scope

Attacks considered: a side-interior contact bypassing angle sums; unmatched B corners; cyclic-word reversal errors; omitted matchings; closing-turn indexing; singular positive families; an incorrect cyclotomic embedding; pentagons placed inside Q; missing reflected seams; counting identical forced P copies as collisions; overlooked partial-side coincidences; and extrapolating finite neighborhoods to a plane tiling. The independent checker audits proper overlap by exact separating axes and then separately checks vertices on open edges, common edge endpoints, and coincident full polygons. It evaluates the complete stated isolated domain, with no random seed, timeout, or numerical decision.

The source certificate itself records collision lists but not a complete incidence inventory. This is a record-detail limitation, not evidence that bounded local legality implies extension. The companion checker supplies additional exact contact checks. No repair to the source mathematics was required.

Degree two Q adjacency follows only in a hypothetical plane tiling; a pair of convex tiles cannot occupy opposite sides of two distinct Q edges without violating the supporting-half-plane condition. It permits cycles or bi-infinite paths, and proves neither a preferred strand geometry nor a plane extension. Larger bounded searches cannot discharge those obligations by themselves.

## Replay and verdict

SageMath 10.9, deterministic exact arithmetic. Source replay completed successfully:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-144-126-first-gate-2026-10-19.sage
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-octagon-144-126-hostile-sol-check-2026-10-19.sage
```

Independent checker completion and final verdict are recorded below.

Independent checker completed successfully (exit 0). There are 20 labeled word/matching pairs before dihedral reduction. For each isolated metric, its seven-tile base has 21 unordered tile pairs: 10 full-edge contacts and 11 disjoint pairs. In every QQ join there are exactly two pairs of identical P copies; these represent shared physical pentagons. For AAAABBBB, the 49 cross-patch pairs comprise 2 identical, 7 edge contacts, and 40 disjoint pairs. For AAABBABB they comprise 2 identical, 9 edge contacts, and 38 disjoint pairs. These counts hold for every source/target choice and both parities. No distinct-tile interior overlap, vertex on an open edge, or partial-edge coincidence occurs. The additional AAABBABB edge contacts are allowed coincidences, not an omitted collision.

**Final verdict: valid**, restricted to the exact local gate and stated metric classification. The continuum's complete immediate-neighbor audit remains unproved and is correctly excluded from the source's local audit claim. Plane tilability, periodic extension, and universal absence of translations are **unresolved**. This review supplies no novelty determination and no answer to the unrestricted main problem.
