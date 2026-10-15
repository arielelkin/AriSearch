# Unequal five-length palettes with an adjacent repeat

Date: 2026-10-15. **Status: independently hostile-reviewed VALID, with exact retained certificates.** Restricted numerical periodic escape only.

## Theorem

Let A,B be genuine convex hexagons, each having exactly five distinct numerical side lengths, with different five-value palettes. Suppose at least one shape's doubled length occupies adjacent sides. If these shapes admit a plane tiling with arbitrary isometries, reflections and partial contacts permitted, then the same unmarked shapes admit a doubly periodic tiling.

This theorem does not assume the two doubled numerical values are equal. It does not assert a formal-color extension allowing differently named numerical values to coincide. It does not solve the unrestricted two-convex-polygon problem.

The [independent whole-claim review](../reviews/hexagon-five-unequal-adjacent-hostile-2026-10-15.md) validates the theorem, its finite-to-global steps, and the corollary below. The [standalone independent verifier](../reviews/hexagon-five-unequal-adjacent-independent-2026-10-15.py) reconstructs the complete domain without importing author code.

## Corollary: each hexagon has at least five numerical lengths

If EACH of two genuine convex hexagons has at least five distinct numerical side lengths, unrestricted plane tileability implies a doubly periodic tiling by the same unmarked shapes. If either has six lengths, apply the reviewed [six/five general theorem](hexagon-six-five-general-periodic-escape-2026-10-15.md). Otherwise both have five. Equal palettes are covered by the [complete common-five theorems](hexagon-common-five-adjacent-periodicity-2026-10-15.md), including their cited nonadjacent cases. For unequal palettes, either both repeats are nonadjacent, covered by the [noncommon nonadjacent theorem](hexagon-five-noncommon-nonadjacent-periodicity-2026-10-15.md), or this theorem applies. These cases exhaust the corollary.

Combined with the separately reviewed [six-distinct arbitrary-partner theorem](hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md), a hypothetical aperiodic hexagon pair therefore has no six-distinct member and has at least one member with at most four distinct numerical side lengths. Pentagon-containing pairs remain outside these results.

## Source, single-species escapes, and complete word domain

Use the reviewed [hexagon defect-free limit theorem](hexagon-limit-and-periodicity.md) to obtain an indexed full-side everywhere-trivalent plane source. Choose the adjacent-repeat shape as A and normalize

    A=(0,0,1,2,3,4).

Corner i is between native side i and i+1. Adjacent-repeat A cannot supply a pure-species source: its only possible pure stars use corner multisets (0,0,0), (0,1,1), (0,5,5), so native corners 2,3,4 could not appear. The same argument applies if B's repeat is adjacent. If B's repeat has separation two, its distinct-adjacent-length corner graph is triangle-free and it has no pure star. If B's repeat is opposite and a pure B star occurs, its angles at native corners {0,1,2} or {3,4,5} sum to two pi; the other triple follows from the four-pi total. The reviewed [opposite-repeat two-face torus](hexagon-both-opposite-repeat-periodicity-2026-10-15.md) gives an immediate monohedral periodic escape. In particular this handles every source omitting A. Outside that escape both species occur and all twelve native corners occur.

Let k in {0,1,2,3,4} be the number of shared length values. Choose their subset from A's five symbols and name the remaining B-private values 5,6,...,9-k. Take all 120 permutations (p,q,r,s,t) of this palette, and insert a second p at native position bp=1,2,3. These three forms cover every adjacent, separation-two and opposite B repeat after rotation and choosing a boundary reading. No quotient is taken in the initial gate. There are 31 palettes, 120 assignments and three separations, totaling 11,160 raw words. Different symbols denote different positive numerical lengths throughout.

## Native directed-sector gate

The [standalone producer](../searches/hexagon-five-unequal-adjacent-recon-2026-10-15.py) uses the ordered-sector algorithm previously independently validated in the [common-five native review](../reviews/hexagon-five-adjacent-microstate-hostile-2026-10-15.md), now over arbitrary union colors. No hardcoded five-color ray enumeration remains. Each sector retains one actual corner index, both incident native side slots in either left/right order, and their actual other native endpoints. Enumerate all ordered triples, with repeated corner occurrences and independently reflected arm orders allowed; require consecutive ray colors to agree.

Each surviving vertex state records all three seams simultaneously: the pair of native SIDE slots, the near-end corner multiset, and the far-end corner multiset. Prune a state if any seam has no state at its other endpoint with the SAME native slot pair and required far-end multiset. Iterate. Every actual state survives inductively; no sufficiency for plane extension is asserted.

Connect native side slots across all seams in the fixed atlas. The actual seam graph is a subgraph, so its actual component partition refines this upper graph partition. If either doubled native pair is disconnected in the upper graph, that species has six actual component-colors. Its partner retains at least five since unequal numerical lengths cannot be connected. The reviewed [six/five formal-color source theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md) supplies a doubly periodic unmarked escape. Auxiliary source colors are not imposed as final matching rules.

The compact [residual certificate](../certificates/hexagon-five-unequal-adjacent-recon-2026-10-15.json) retains every hard word, explicit equivalence maps and representative state atlases. No archive of all negative-word atlases is made; the complete 11,160-word domain is deterministic and regenerable.

| B repeat separation | No twelve-corner cover | Six-color escape | Residual |
|---|---:|---:|---:|
| 1 | 3668 | 40 | 12 |
| 2 | 3656 | 64 | 0 |
| 3 | 3672 | 48 | 0 |

All residual words share four values and have adjacent repeats on both shapes. Explicit global color bijections and independent native dihedral readings take them to three ordered representatives, four raw words each:

    B1=(0,0,1,3,5,4),
    B2=(2,2,1,3,0,5),
    B3=(2,2,4,0,3,5).

B2 and B3 are exchanged by swapping species; the certificate retains explicit swap maps as well. There are two unordered pair classes. The proof below keeps all three ordered representatives to avoid an implicit species-swap step.

## Exactly five actual source-support cases

For each representative exhaust every subset S of its six-star fixed atlas. Restrict the vertex states to stars in S, rerun simultaneous endpoint pruning, and require all twelve corners covered and EVERY selected star still represented. The actual occurring-star set EQUALS one of these supports: its actual states survive this restricted pruning. A minimal-support containment statement would be insufficient.

The [support and witness producer](../searches/hexagon-five-unequal-adjacent-supports-2026-10-15.py) and [certificate](../certificates/hexagon-five-unequal-adjacent-supports-2026-10-15.json) retain three B1 supports and one each for B2,B3, total five. Their complete fixed states, corner occurrence counts and vertex species counts are retained. This is an authoring computation, separately reconstructed by the independent verifier linked above.

For B1 the two four-star supports are

    P={(0,5,11),(1,6,7),(2,3,8),(4,9,10)},
    Q={(0,1,7),(2,3,8),(4,9,10),(5,6,11)}.

Each partitions the twelve actual corners. The third support is exactly P union Q.

For B2 and B3 the sole supports are respectively

    T={(0,10,10),(1,8,9),(2,6,7),(3,7,8),(4,5,9),(6,11,11)},
    V={(0,1,1),(0,5,8),(2,2,6),(3,4,7),(3,10,11),(4,5,9)}.

No metric realization of a mere formal support is assumed; these are necessary alternatives for the given actual source.

## B1: three positive four-face torus implications

A justified fixed positive-witness domain uses two A and two B faces. Fix one boundary orientation, allow all eight relative orientation signs, and enumerate within-color perfect matchings of all 24 side occurrences. Color group sizes are 8,4,4,4,2,2, giving exactly

    8*105*3^3=22,680

pairings. This is the ONLY torus search undertaken for this new theorem. It gives 22,608 connected gluings, four trivalent torus candidates and two different native angle-equation supports. No larger quotient is searched and no negative bounded result is used.

The certificate retains both actual positive gluings, their boundary orientation signs and every side pairing. Each uses every full side once with the same physical length, is connected and orientable under reverse boundary endpoint identifications, and has eight circular triple-corner vertex links. Thus V=8,E=12,F=4.

For EVERY one of P,Q,P union Q the certificate selects a witness and retains exact Fraction combinations of source rows yielding all target angle equations. Source rows are the two polygon angle totals four pi and each actual source star total two pi. All twelve augmented weighted-row identities, including constants, are retained. Therefore each selected quotient has actual cone angles two pi for the given polygon metrics. It is a compact nonsingular flat torus, whose complete universal cover develops isometrically onto the Euclidean plane. The lifted original whole polygons give the periodic unmarked escape with two independent deck translations. No corresponding source patch or new polygon-closure solve is required.

The two four-star supports separately have one necessary corona state per species and fully unique neighbors, but that additional observation is not needed: positive tori cover all three cases.

## B2 and B3: connected certain-transition corona graphs

At each host corner retain every compatible neighbor-side and native endpoint port option from the actual-star assignments. Choose one option at each of six corners, requiring the two endpoint records on each host side to name the SAME entire guest native side and its TWO distinct endpoints. This fixes the complete indexed relative neighbor isometry, since ordered endpoint images plus the opposite interior half-plane leave one Euclidean extension. All actual tile states survive. Prune any state lacking a reciprocal guest state across any side; all actual states again survive.

A transition is certain when the guest state is unique. If the actual graph using transitions certain in both directions is connected, a map between any two occurrences with the same indexed frame type and finite corona state propagates to a symmetry of the whole framed tiling. There are finitely many tile-state orbits, so its symmetry group is discrete and cocompact. The separately reviewed elementary planar argument then yields a rank-two translation subgroup. Merely having finitely many states would not suffice; the connectivity below is essential.

For exact B2 support T, the necessary corona atlas has one A state and two B states. Every side transition is certain except B native side 5 against B native side 5. Delete these uncertain BB edges. Each has an endpoint at B native corner 4, whose unique star is (0,10,10); its third tile is A. That A meets both B copies through their other incident B sides, namely native side 4, and both BA transitions are certain. Every deleted edge thus has a two-retained-edge bypass. Since full-side adjacency is connected, the certain-edge graph is connected.

For exact B3 support V, there are two A states and one B state. Only A native side 2 against A native side 2 has two guest-state choices. At its native corner-2 endpoint the star is (2,2,6); the third tile B supplies a two-AB-edge bypass through both A native side-3 incidences, again certain. Connectivity follows identically. In both cases the only uncertain edges are same-slot pairings, so every retained edge is certain in both directions. Indexed state propagation therefore gives a rank-two translation subgroup and an admitted doubly periodic tiling.

All five exact actual supports yield a positive periodic escape. Together with the complete finite source gate, this proves the theorem. QED.

## Replay, provenance and limits

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-unequal-adjacent-recon-2026-10-15.py
mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-unequal-adjacent-supports-2026-10-15.py
```

Default stdout is full deterministic JSON. Explicit --output PATH retains it. Both authoring producers completed with the counts above. The support producer imports the new native authoring routine and the previously reviewed generic four-face producer, setting its native A word to this adjacent-repeat word. That reuse is disclosed authoring code, not independent verification. Corona reconstruction uses this author's previously written anchored-host-sector algorithm; this new application was independently reconstructed and reviewed.

The numerical theorem addresses only exactly-five-length hexagon pairs with unequal palettes and at least one adjacent repeat. It does not address shapes with four or fewer numerical lengths or any pentagon-containing pair. The unrestricted main problem remains unresolved; no novelty or priority claim is made here.
