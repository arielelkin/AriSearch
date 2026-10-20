# AAABBABB saturated pentagon: exact one-star gate

Status: complete finite necessary-local-condition computation, independently hostile-reviewed [VALID](../reviews/regular-pentagon-octagon-saturated-p-star-hostile-sol-2026-10-19.md); no plane extension claim.

The reviewed contact reduction gives only PPQ at A and PQQ at B. The public Q sides for AAABBABB are 0,1,2,4,5,7; their types are AA,AA,AB,BA,AB,BA. There is no public BB side. A pentagon with zero PP sides has five BB-facing sides, and one with one PP side has four consecutive PQ sides, including a BB-facing side. Both are impossible. Two PP sides cannot be consecutive. Hence every P necessarily has exactly two nonconsecutive PP sides. This is a pointwise argument, independent of density saturation.

Fix a counterclockwise unit pentagon P and PP sides {0,2}. Every matching of size two is carried here by a symmetry of the regular pentagon. Its other sides 1,3,4 have required endpoint types AA,AB,BA, respectively. The neighbors across sides 0,2 are unique regular pentagons.

For each PQ side, every permissible Q placement is determined by a public source edge and isometry parity. A direct placement reverses endpoint order; an indirect placement preserves it. Thus the AA side has four options (two source edges, both parities), and each AB/BA side has four options (four mixed source edges, the unique compatible parity). The finite domain is exactly 4^3=64 labeled branches. Q has no additional continuous placement freedom once a whole edge is identified. We do not quotient by the remaining root reflection, so this domain can contain globally reflected equivalents.

The Sage script constructs all six tiles: root P, its two forced PP neighbors, and the three Q neighbors. For every unordered tile pair it merges exact coincident polygons, tests interior intersection by exact convex supporting half-planes, and rejects any vertex lying on an open side of another tile. For each of the five root vertices it requires exactly three incident corners and exactly two common vertices between its two external neighbors. With disjoint convex interiors, these two common endpoints establish the required whole shared side. At the PQQ vertex this is the long QQ edge; at each PPQ vertex it is a unit PQ edge. All arithmetic is in Q(zeta_20); signs use its distinguished algebraic embedding through QQbar. No floating decision, random seed, solver or timeout is used.

The adjacent JSON retains all 64 branches, exact edge/parity encodings, rejection reasons, coincidences, pairwise common-vertex counts, and the five root-star incidences. The coordinates are uniquely reconstructible from these encodings and the short script's exact field definition. This is an independently verifiable finite certificate; an independent hostile verifier is requested separately.

Replay:

```sh
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-octagon-saturated-p-star-sol-2026-10-19.sage
```

Read dependencies: research-problem.md; research-protocol.md §§5,11,19; the P5/Q8 first gate and hostile review; reviewed AA-capacity lemma and hostile review; 19:52 Astra assessment. SageMath version is recorded in JSON. An initial completed run failed only while serializing Sage integers; the retained script converts them for JSON and is replayed below. No mathematical conclusion depends on the failed serialization run.

## Completed result and stopping boundary

Corrected replay completed with exit 0 in SageMath 10.9. All **64 of 64** branches survive. There are no coincident full tiles and no distinct-tile interior overlaps or forbidden partial contacts. All five root stars close with their required whole neighbor sides. An orientation issue identified during self-audit was corrected before this final replay: the supporting-half-plane test explicitly multiplies by each polygon's signed orientation, including reflected Q copies.

The complete branch list is the Cartesian product

- Q on P side 1: (source edge, reflected) in {(0,false),(0,true),(1,false),(1,true)};
- Q on P side 3: {(2,true),(4,false),(5,true),(7,false)};
- Q on P side 4: {(2,false),(4,true),(5,false),(7,true)}.

Every one of these triples survives. The root vertex incidences at vertices 0 through 4 are respectively (P,PP0,Q4), (P,PP0,Q1), (P,PP2,Q1), (P,PP2,Q3), (P,Q3,Q4). All are recorded branch by branch in JSON. These are forced local edge coincidences between distinct neighbors, not identifications of full polygons.

No exact obstruction arises in this prescribed saturated-star domain. Branching remains and this gate supplies no new global invariant. Under protocol §5, stop this route here: plane extension, a complete carrier, and periodicity properties remain unproved. No corona growth, strand extension, torus enumeration, literature/novelty claim, Git changes, or discovery-log changes were made.
