# Independent hostile review: saturated AAABBABB pentagon star

## Claim and assumptions

Reviewed the saturated-P `.md`, `.sage`, and `.json`, the problem, protocol §§8,11,19, first P5/Q8 gate and hostile review, and AA-capacity lemma and hostile review. The claim is a complete finite local gate for the isolated AAABBABB metric, not existence of a plane tiling. Reflections and initially unrestricted contacts are permitted.

## Independent reconstruction and attacks

The prior angle argument excludes vertices in open sides and gives only PPQ at A and PQQ at B. Thus each physical side has a whole neighbor. PP sides of a pentagon form a matching of C5. With no PP sides all five PQ sides have BB endpoints. With one PP side, the four other sides have roles AB,BB,BB,BA in cyclic order. Q has no public BB side: its six public sides are 0,1,2,4,5,7. Both cases are impossible. Hence every P has two nonconsecutive PP sides. This is pointwise and does not assume asymptotic equality implies saturation.

Every two-element matching of C5 is dihedrally equivalent to {0,2}. The three remaining sides then have roles AA,AB,BA at indices 1,3,4. The unique regular pentagon outside each PP side is forced. For Q, an ordered source edge and parity uniquely determine an isometry; the exterior placement is direct with reversed endpoints or indirect with preserved endpoints. AA admits two source edges with both parities. Each mixed role admits four source edges with exactly one parity each. This exhausts 4 cubed = 64 labeled branches. No residual reflection quotient is taken. Distinct encodings need not represent inequivalent global assemblies, which is harmless.

The source overlap predicate is orientation invariant after multiplying by the signed polygon orientation. For convex polygons with nonempty interiors, a separating supporting line parallel to some edge exists whenever interiors do not overlap; the source tests all edges of both polygons. Zero contact is correctly allowed. Its separate open-side vertex test excludes T junctions and unequal partial collinear edge overlaps. Coincident whole tiles are merged rather than counted as overlaps; none actually occurs here. With disjoint interiors, two common vertices of distinct convex tiles determine their common boundary segment. The independent checker strengthens this by checking they are consecutive vertices in both polygons and by checking the edge length.

At root vertices 0..4 the external pairs are respectively (PP0,Q4), (PP0,Q1), (PP2,Q1), (PP2,Q3), (Q3,Q4). Exactly three corners meet in each star. The last common edge must have length 2cos(18°); the other four must be unit edges. This establishes the required five stars, without imposing completeness at other boundary vertices of this finite patch.

## Independent exact verifier

The companion `regular-pentagon-octagon-saturated-p-star-hostile-sol-check-2026-10-19.sage` never imports the source search. It reconstructs the octagon by solving closure over QQbar, using the previously retained independent first-gate geometry helpers. It derives endpoint roles from the PP matching, enumerates source edges and both parities independently, constructs the forced pentagons by a clockwise edge walk, and checks all 15 unordered tile pairs in every branch. Its separating-axis test compares projection intervals and needs no polygon orientation sign. It checks open-side vertices, common-edge adjacency, all five incidences, and exact neighbor-edge lengths. It compares its full branch-key set with the retained JSON and requires 64 distinct encodings and 64 survivors. Pair checks are cached only by complete exact coordinate tuples.

Replay (SageMath 10.9; exact algebraic arithmetic; deterministic, no solver, seed, or search cutoff):

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-octagon-saturated-p-star-hostile-sol-check-2026-10-19.sage
```

## Defects, uncertainty, and verdict

No mathematical defect or repair to the source was required. Omitted reflections, reversed endpoint roles, false saturation from density, coincident neighbors, orientation-sensitive intersection tests, forbidden partial contacts, and an unlicensed local-to-global inference were explicitly attacked.

Completion and exact verdict are recorded below. This gate supplies no plane extension, infinite carrier, periodic witness, aperiodicity theorem, or novelty result. The source's decision to stop this particular route is consistent with the absence of a new global mechanism; it does not terminate the overall research obligation in protocol §19. No Git or discovery-log edits were made.

**Final verdict: valid**, for the stated finite necessary local gate. Independent verifier completed with exit 0: all 64 branches pass, with exactly ten full-edge contacts and five disjoint pairs among the fifteen unordered tile pairs in every branch. No full-tile coincidence occurs. The JSON domain matches the independent enumeration exactly. Plane tilability and periodicity remain unresolved.
