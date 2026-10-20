# Independent hostile review: minimal regular P5 / Q8 carrier

**Verdict: PASS**, for the all-parameter AABBAABB periodic escape and the complete normalized 2P+1Q finite domain. **NARROW**, for AAABBABB: absence only at this inventory in a rank-two translational quotient. No general plane nonexistence, aperiodicity, larger-quotient exclusion, or singly periodic exclusion follows.

## Material reviewed and exact claims

Read AGENTS.md, research-problem.md, research-protocol.md, the Q8 first-gate report, AA-capacity hostile review, saturated-P-star report and hostile review, and the minimal-carrier producer report, Sage script and JSON. Dependencies supply the unrestricted-contact reduction to whole-edge PPQ and PQQ stars and the prior metric-family classification. This review independently audits the new finite carrier domain and reconstructs its first positive witness; it does not rerun the entire earlier word classification or claim a classification of arbitrary octagons.

The claims checked are: exactly 4320 labeled pairings for each surviving word; counts 48 endpoint-compatible for each, zero correct-star maps for AAABBABB, four for AABBAABB; and a degree-one Euclidean torus carrier for every h>0 in the latter metric family. The isolated AAABBABB QQ length is checked independently by solving complex closure. All decisions are algebraic, with the distinguished embedding w=exp(2 pi i/20).

## Completeness attacks

No public Q side has BB endpoints in either specified word: the only BB sides are the two QQ sides. A P with zero PP sides would have all five PQ sides BB-facing; one PP side forces a BB-facing side among the remaining four. Consecutive PP sides violate the PPQ/PQQ stars. Consequently each P has two nonconsecutive PP sides, with cyclic corner roles AAAAB after normalizing the PP pair to {0,2}. All five nonconsecutive unordered pairs are rotation equivalent. Reflecting a regular P introduces no new shape or placement species, since every reflected regular pentagon is also a direct isometric copy. Its normalized side-role pattern remains covered.

For a rank-two translation quotient, corner counting forces p=2q. A compact polygon has no nonzero translation stabilizer, so faces survive as whole copies under the quotient and the smallest possible positive inventory is exactly (2,1). No argument reduces a larger quotient to this inventory. Pure-species cases are forbidden by the exhaustive star list, rather than silently omitted.

Four PP darts have exactly three perfect matchings, including same-face pairs. Six PQ darts may pair to six public Q darts in all 720 bijections. The two QQ darts have one pairing, necessarily a self-face pairing because there is one Q. Both Q reflection parities are included, with conjugation plus reversed indexing maintaining counterclockwise orientation. Thus 2*3*720=4320 labeled cases per word, without any extra symmetry quotient. A translation torus is orientable and each edge gluing reverses the boundary direction. Endpoint reversal is therefore required. Reflected Q edges correctly use source index -(i+1), while its corners use -i. No chirality restriction is imposed on the tiling problem.

The independent checker uses union-find endpoint identifications instead of the producer's vertex-permutation traversal. It independently enumerates all matchings/bijections, reproduces counts (4320,48,0) and (4320,48,4), and compares the complete four surviving pairing encodings with JSON. Endpoint compatibility is only a label check, not geometric compatibility. An additional analytic obstruction independently proves the isolated negative: native QQ edges 3 and 6 have directions w^7 and w^15. Their ratio is w^8, not -1. They therefore cannot self-pair by translation; reflection preserves failure of antiparallelism. This applies to any translational quotient with exactly one Q, regardless of pentagon pairings. It says nothing about multiple Q faces or a cylinder quotient.

## Exact geometry and parameter boundaries

The independent checker reconstructs AAABBABB by solving closure for its two equal private lengths and obtains exactly -w^7+w^5-w^3+2w, positive and real. It verifies all strict supporting inequalities. For AABBAABB it independently constructs the edge walk with private lengths h and public lengths 1 and verifies closure identically. All nonincident vertices are strictly in the appropriate edge supporting half-plane for every h>0: the exact cross-product polynomial has nonnegative real coefficients and is nonzero. This verifies strict convexity without sampling. The parameter boundary h=0 is excluded because its private edges collapse; no claim includes that boundary. Arbitrarily large positive h is covered algebraically.

The first witness is rebuilt from native coordinates as P, 1-P, 1+w^4-w^4 Q(h). The checker verifies both endpoint equations for all nine advertised pairings with the advertised integral lattice shifts. This simultaneously verifies edge reversal, equal lengths, and zero rotational holonomy for this witness. The basis L1=w^6+w^4+w^2 and L2=(w^7-w^5+w^3-w)h+2w^6-1 has determinant exactly the sum of the three developed face areas. Each face area has a positive constant coefficient and nonnegative remaining coefficients; the determinant does too. In particular it is strictly positive throughout h>0. No numerical approximation, bounded translate check, or overlap assumption is used to establish global coverage.

The checker reproduces six distinct vertex classes, checks that each has a single three-corner link cycle, and checks every angle sum is exactly 360 degrees. Face adjacency is connected by the displayed pairings; all faces have positive orientation and interiors. Thus gluing yields a compact connected oriented surface without boundary, with Euler characteristic 3-9+6=0. The local map to the lattice torus is an isometry in faces and along edges. At vertices the oriented gluing places successive positive sectors around the same point; the single link and total angle 2 pi imply winding one and a local homeomorphism. Merely checking total angle without the single-link condition would have been insufficient; both are verified here.

The continuous local homeomorphism has open image and, by compactness, closed image, hence is onto the connected target torus and is a finite covering. Its degree is the positive total face area divided by the positive target covolume. The exact identity makes that degree one. Lifting gives the whole Euclidean plane tiled with disjoint interiors by the two shapes and the stated rank-two periods. This resolves possible distant overlaps and holes rigorously. No assumption about a finite translate cutoff enters.

## Independent verifier, defects and scope

Companion checker: `research/reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.sage`. It imports no producer code, never executes the producer search, and uses its JSON only to compare final finite counts and pairing encodings. The first positive geometry, lattice and area identities are independently reconstructed; the checker does not claim independent geometric verification of all four equivalent certificates.

Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-octagon-minimal-carrier-hostile-sol-2026-10-19.sage
```

Completed replay: exit 0 under SageMath 10.9, printing PASS for the independent finite domains and all-parameter carrier checks.

No substantive defect was found and no producer repair was required. The negative claim remains deliberately finite. The positive carrier excludes every member of this specific AABBAABB metric family from being an aperiodic partner of the regular pentagon. The AAABBABB metric remains unresolved beyond this inventory. This is partial progress toward the unrestricted problem, with no novelty claim. No Git or discovery-log edits were made.
