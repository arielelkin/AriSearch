# Hostile review: common-five adjacent-repeat native microstates

Date: 2026-10-15. **Verdict: VALID** for the complete 360-word necessary microstate gate and its component-escape conclusions. The [limited adjacent/separation-two theorem](../lemmas/hexagon-common-five-adjacent-separation-two-periodicity-2026-10-15.md) follows. This does not close the two-adjacent or adjacent/opposite classes by itself.

## Independent reconstruction and completeness

I reviewed the [root reconnaissance producer](../searches/hexagon-five-adjacent-microstate-recon-2026-10-15.py) without assuming its native-state completeness. My [standalone checker](hexagon-five-adjacent-microstate-independent-2026-10-15.py) imports no author modules. It instead enumerates all ordered triples of directed native sectors: each sector specifies one actual corner index, its two native side slots in one of both left/right orders, both far native endpoints, and both ray colors. Repeated occurrences of the same corner are allowed. Consecutive ray colors must match cyclically.

Every actual trivalent vertex has such an ordered reading. Reflections change native left/right order and are included independently on every sector. Quotienting a completed state's corner triple and its three seam records by sorting only forgets information; it does not omit actual states. For three corners every ordering differs by cyclic rotation or reversal, including repeated corners. Thus the author's sorted-corner plus all-arm-flips enumeration covers the same state data. This is not true in arbitrary vertex valence without further analysis, but the source here is everywhere trivalent.

For each of the three seams, its native side-slot pair and both near/far corner MULTISETS are retained simultaneously. Repeated side colors and loop corners are not collapsed to color pairs. A physical full side has the same native slot pair at both ends, with the computed other native corners. Hence actual states survive inductively when a state is deleted only for lacking a compatible far-end key. In particular the stronger equality-slot key is necessary and does not remove a legitimate repeated-arm realization. Losing cyclic orientation when storing keys may leave false positives, which is harmless for this necessary gate.

The reconstruction exactly agrees with the author's complete initial and fixed atlases for every one of the 360 raw words. It retains an independent [complete certificate](../certificates/hexagon-five-adjacent-microstate-gate-2026-10-15.json). Each B separation has 120 words, with no quotient. Counts (no corner cover, component escape, both doubled pairs joined) are:

| B repeat separation | No cover | Component escape | Residual |
|---|---:|---:|---:|
| 1 | 88 | 24 | 8 |
| 2 | 96 | 24 | 0 |
| 3 | 92 | 24 | 4 |

The upper seam graph uses every native slot pair in every surviving state. The actual graph is a subgraph and its component partition refines the upper partition. Different original numerical colors cannot become connected. If either doubled slot pair is disconnected, actual-component recoloring gives six formal colors on that shape and at least five on the other. The independently reviewed six/five source theorem then applies. No auxiliary matching rule is imposed on the final unmarked tiling.

For the limited adjacent/separation-two corollary both species must occur: the separation-two shape has no pure star, while the adjacent-repeat shape's only pure states have corner multisets (0,0,0), (0,1,1), or (0,5,5). In particular its other native corners cannot occur without the partner. Therefore a source covers all twelve corners. All 120 words either fail this necessary cover or have the valid component escape. Pure repeated-ray stars are retained throughout; no opposite-repeat monohedral argument is imported.

## Additional B2 branch independently checked

The root proposed a separate closure for A=(0,0,1,2,3,4), B=(0,0,2,4,1,3). The checker now verifies the exact finite inputs to that closure. This paragraph reviews that argument independently; the other residual representatives require their own witnesses or proofs.

The full fixed atlas has 14 corner-multiset stars and 16 native states. Exhausting all star subsets, restricting to their states, and applying full endpoint closure leaves exactly twelve corner-covering necessary supports. The actual support equals one of these: its actual states survive pruning after restriction to that actual star set. Sizes are two six-star, two seven-star, three twelve-star, four thirteen-star and one fourteen-star support.

For each of the eight supports of size at least twelve, the exact angle coefficient matrix, including both polygon total-angle rows, has rank twelve. The constant assignment of every angle equal to 2/3 pi satisfies every equation, so it is the unique solution. Both polygons would therefore be equiangular 120-degree hexagons. Fix either polygon's first edge direction independently. Consecutive edge directions then differ by 60 degrees. In the exact basis with doubled horizontal coordinate and vertical coordinate scaled by sqrt(3)/2, the two closure equations per shape have the following coefficient matrix on its five common length values (r,x,y,z,t):

```text
 3 -1 -2 -1  1
 1  1  0 -1 -1
 3 -1 -1  1 -2
 1 -1  1 -1  0
```

The checker derives these coefficients directly from the two words and the six exact direction vectors. Rank is four and the all-ones vector is in the kernel, so all five lengths must be equal. This contradicts the five-distinct-numerical-length premise. Global rotation or reflection of either polygon only changes the coordinate basis for its own two closure equations, not this conclusion.

Each six-star support consists entirely of AAB stars, or entirely of ABB stars with the roles swapped. The minority species has each native corner in exactly one star. The repeated-arm star could appear ambiguous at one endpoint, so I tested BOTH endpoints, retaining the exact native side-slot pair. For every one of the twelve native host sides there is exactly one opposite-species guest side and ordered endpoint identification. The six-star AAB support stated by root therefore satisfies full AB-neighbor uniqueness; its species-swapped counterpart does too.

In an AAB source, each A corner has exactly one incident AB edge, so A's B-neighbor sides alternate. An A frame plus that parity uniquely determines its three B placements. A B frame uniquely determines all six adjacent A frames and their parity from the incoming side. The AB adjacency graph is connected: any AA edge in a full adjacency path can be bypassed by two AB edges through the B at one endpoint. Hence any indexed map between B occurrences propagates to a symmetry of the entire framed tiling. There are finitely many tile orbits, discreteness follows from compact tiles, and the previously reviewed planar group argument supplies a rank-two translation subgroup. This is a positive intrinsic-periodicity argument; a negative four-face search is not used. Indeed all-AAB incidence forces the A:B frequency ratio 2:1, so a 2A2B quotient was not suited to this branch.

Each seven-star support is one of the preceding mixed supports plus one pure star of the MAJORITY species at its native corner 0. This pure star cannot actually occur. For an A tile in the AAB case let b_i indicate whether side i meets B. At its other five native corners, b_i+b_(i+1)=1, i=1,...,5 modulo six. These five equations force b_0+b_1=1 as well. An AAA occurrence at corner 0 would require b_0=b_1=0, a contradiction. The ABB case with a pure BBB star is identical after swapping species. Actual-support equality is essential here: adding the pure star to a formal possible atlas does not imply it actually occurs.

These twelve branches therefore close this specific B2 representative. The checker verifies the exhaustive support classification, both-endpoint uniqueness, and the two exact rank calculations. The parity contradiction and flat framed-symmetry consequences are human arguments recorded above.

## Three indexed corona propagation certificates

The root subsequently retained [three exact tile-corona certificates](../certificates/hexagon-adjacent-corona-states-2026-10-15.json), produced by [the narrow native-state program](../searches/hexagon-adjacent-corona-states-2026-10-15.py). I independently rebuilt them with [a second no-author-import checker](hexagon-adjacent-corona-independent-2026-10-15.py). **Verdict: VALID** for each specified support's periodicity implication.

My reconstruction fixes each host sector's native arm order, enumerates both orders of its other two corner occurrences, and independently flips their arms. It reconstructs every possible neighbor native side and endpoint at each of six host corners. A tile state retains a guest native side and both ordered guest endpoint corners on each host side. Requiring the two host endpoint records to belong to that same entire guest side is necessary for every actual tile. The reciprocal-state pruning is necessary because the actual guest has a state with the inverse ordered endpoint map. Additional geometrically impossible states may remain, which only enlarges the upper state domain; uniqueness across that domain remains a valid implication for actual states.

The independent checker exactly matches all corner-port options, initial and fixed tile states, and every retained guest-state index. The first B3 support has two A states and one B state. Only A native side 2 has two guest-state choices, and both choices are across another A's native side 2. The second B3 support has one A and two B states; only B native side 5 has two choices, both across another B's native side 5. The B4 support has two A and one B state, with every side's guest state unique.

For B4, connected full-side adjacency immediately gives connected deterministic propagation. For the first B3 support discard A-side-2/A-side-2 edges. Each discarded edge has an endpoint whose native corner triple is (2,2,6). The third tile is B; it meets both A copies along their other side at corner 2, namely A native side 3. Both of these AB transitions have unique guest states in the retained upper atlas. Replacing the discarded edge by these two retained edges preserves connectivity. For the second B3 support discard B-side-5/B-side-5 edges. At its corner-4 endpoint the star is (0,10,10); the third tile A meets both B copies through B native side 4, again certain transitions. The same bypass argument applies. Every other transition has exactly one compatible guest state, and the only uncertain edges are same-native-slot pairings, so all retained edges are certain in both directions.

An indexed occurrence together with its finite tile-corona state determines each retained neighbor's complete relative isometry AND its state. Ordered endpoint images plus the opposite interior half-plane fix the full plane isometry. A map between two occurrences of the same type and state therefore propagates through the connected retained-edge graph, sending the entire framed tiling to itself. Finitely many states give finitely many tile orbits; local finiteness gives a discrete symmetry group. The reviewed elementary plane-group argument yields two independent translations. This verifies the needed geometric propagation, rather than treating a finite list of symbolic states alone as sufficient for periodicity.

Replay completed with exit status zero:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-adjacent-corona-independent-2026-10-15.py
```

```text
PASS: independent corner ports, all three complete coronas, reciprocal choices, two uncertain-edge bypasses, third fully deterministic corona
```

These three support implications do not by themselves establish complete coverage of the other residual word classes; that requires the remaining source-support classification and positive torus identities. A forthcoming complete common-five adjacent-repeat lemma must retain and review those obligations separately.

## Replay and scope

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-adjacent-microstate-independent-2026-10-15.py
```

Exit status zero. Output:

```text
PASS: B2: 12 exact supports, eight all-120-angle contradictions, two pure-star parity contradictions, two deterministic AB-parity supports
PASS: all 360 ordered-sector native microstate gates; counts (88,24,8), (96,24,0), (92,24,4)
```

The new checker default is a VERIFIER: it regenerates the complete gate and compares the retained certificate. Its explicit --output PATH option regenerates that certificate; default stdout is a concise verification report, not a certificate-producer JSON stream. Register it as a verifier if desired.

The existing defect-free limit, six/five formal-color source theorem, and planar framed-symmetry theorem are separately reviewed dependencies. This review does not replace those reviews or prove every other residual class. No general impossibility, aperiodic pair, or novelty claim is made.
