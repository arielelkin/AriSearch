# Independent hostile review: all 180 five/four words

Date: 2026-10-19. Verdict: **PASS / valid at the explicitly restricted theorem scope**, importing the named reviewed dependencies. No producer file was edited.

## Claim and boundary

Reviewed `research/lemmas/hexagon-five-four-all-words-periodicity-synthesis-sol-2026-10-19.md`: actual strictly convex closed hexagons with A=(0,1,2,0,3,4), B any distinct permutation of (0,0,1,1,2,3), five distinct positive physical lengths; plane tilability implies existence of a doubly periodic tiling of the unchanged pair. This is not an impossibility theorem for arbitrary pairs and is not periodicity of every admitted tiling. Read the governing problem and protocol first.

## Attacks and findings

1. **Orbit coverage:** independently replayed the retained integer comparison. Its assertions reconstruct all distinct multiset permutations, seven literal dihedral orbits, orbit disjointness, sizes twelve, complete union of 84 full-cover rows, and the remaining 96 rows. It fixes A and all numerical labels. It does not quotient by color permutations or species exchange. Output: `CHECK PASS: 180 = 96 + 7*12; literal disjoint orbits and all star/corona counts`. This audit imports the separately reviewed original atlas enumeration rather than independently rebuilding every atlas here.

2. **The 96-word branch:** an actual mixed trivalent ETE source necessarily exhibits every native corner of both species. Each actual star survives every pruning iterate by the actual far endpoint of each incident seam. Hence failure of full cover forbids this mixed source, not the original unrestricted tiling. The synthesis takes the monohedral limit branch first, so neither loss of a species nor partial initial contacts is omitted.

3. **Reflections and relabeling:** a rotation of the native starting index is harmless; a reversed word can be normalized by reflecting the physical prototype. Reflections already belong to the admitted isometry group. Applying the representative theorem to that normalized polygon transfers all angle indices at once, avoiding an incorrect unchanged corner-index equation. Absolute orientation is never assumed finite.

4. **Actual support versus angle closure:** the set C(alpha) consists of every atlas triple whose equation actually holds, not merely observed triples. Translating all twelve angles by 2/3 makes both polygon totals and star rows homogeneous. Any row-span consequence holds at alpha, so C(alpha) is closed. Additional accidental equalities cause a larger closed mask already in the census. Lifting all compatible signed stars and pruning only enlarges the actual support; induction retains every actual remote endpoint witness. The actual A dimer supplies a formal corona even if external neighbors repeat. Thus the full-cover/corona rejection cannot remove the current source. No genericity, realizability of arbitrary angle assignments, or equality between actual and compatible supports is needed.

5. **Partition and deterministic branch:** the reviewed census gives 306 pure escapes, 300 further cover failures, thirteen deterministic cases, and nine branching cases. Priority of pure escape is explicit. In a deterministic case, restricting an upper table cannot create alternatives, and every used side retains its actual neighbor. For fixed physical polygons, native neighbor index and handedness determine a complete relative isometry. The imported intrinsic determinism theorem therefore applies to the connected full-side graph; it does not require finitely many absolute rotations.

6. **Last-word carriers:** replayed both producer and independent checker. Producer: `CHECK PASS`, `EXHAUSTED 113400 candidates 6`, and precisely the nine displayed positive witness lists. Independent checker: `INDEPENDENT PASS: 113400 domains; 8 partitions; 6 tori; 432 exact augmented/separator tests`. The witnesses are positive constructions, not failure-of-search exclusions. Equal-color sides of the actual unchanged polygons glue with oriented boundary reversal; circular vertex links and augmented angle identities give a nonsingular compact flat torus. Its complete simply connected universal cover is Euclidean plane, providing coverage and disjoint interiors. The orientation-preserving freely acting deck group consists of translations and compactness forces rank two. Vector closure is already supplied by the actual polygon hypotheses.

7. **External classification provenance:** checked the primary v2 source at https://arxiv.org/html/2508.01404v2 (28 April 2026). Its Main Theorem classifies congruent-hexagon plane tilings with at least three tiles at every vertex; the text explicitly includes convex hexagons and non-edge-to-edge contacts. Reinhardt families and their periodic constructions are the imported dependency, not a new proof in this synthesis. The source also discusses flipping corner labels. The synthesis does not silently assume an edge-to-edge monohedral classification.

## Defects, repairs, uncertainty

No mathematical defect found in this synthesis. No repair proposed or performed. Historical pending or blocked passages in individual dependency artifacts are explicitly overridden only by their named later reviews/constructions, not silently used as current obligations. The global defect-free-limit theorem, first-six-orbit results, full atlas, resonance census, strip construction and monohedral classification remain imported dependencies at their recorded review scope; this integration review is not a fresh independent proof of all those results. No novelty claim is established.

The remaining whole-synthesis review gate can be marked passed for this restricted family. The original two-convex-polygon problem remains unresolved.

## Replay

All commands were executed with the mandated environment wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_all_words_orbits_sol.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-last-word-four-face-residual-gate-sol-2026-10-19.py --check
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-last-word-four-face-independent-check-sol-2026-10-19.py
