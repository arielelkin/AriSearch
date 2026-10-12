# Hostile review: balanced minimal covering rank-five root

Date: 2026-10-12. Verdict: **VALID for the exact closed type and stated native-order SFT**. No ring, edge-neighbour, closure or balance defect found.

The [lemma](../lemmas/two-hexagon-balanced-minimal-covering-root.md) supplies a positive balanced, angle-feasible rank-five covering root with no proper covering ancestor. Its angle-only SFT is nevertheless empty for the specified native cyclic orders and for every side equivalence. This disproves coverage by extending only covering low-rank ancestors even after adding positive corner balance. It neither constructs an aperiodic polygon pair nor classifies non-dihedral reorderings or other higher-rank types.

[The independent checker](check_two_hexagon_balanced_rank_five_ring.py) imports no producer, author verifier, SFT code, CP-SAT or Sage. It reads the retained certificate and independently checks rank, all 364 rational affine closure memberships, the six positive weights, generic rational angles and all 41 generating subsets of at most three triples using Python rational arithmetic. Rank modulo polygon sums is five, exact closure has six triples, and the generic point has exactly those six angle stars. The stronger no-proper-covering-ancestor argument is immediate: each B corner occurs in precisely one closed triple, so every covering closed subset must contain all six. The lemma's direct closure proof by B-corner multiplicity and the two disjoint odd pair-cycles is correct.

The ring audit was rebuilt from the two canonical global triangle orientations, rather than accepting the author's six-slot corner formulas. For each star around a central cell it searches translated canonical triangles and reconstructs the three cell/corner incidences. These recover central slot k and neighbour slots k+2,k+4 for all six directions, including the four stars whose canonical anchor is an adjacent cell. This rules out the main possible rotated/reflected-neighbour convention error.

Using those independently derived incidence maps, exhaustive twelve-state recursive assignment gives exactly one A-neighbour ring for each of the twelve B placements. Every stored binary relation and unique ring agrees. Adjacent A neighbours at D_k,D_(k+1) share exactly two canonical triangle vertices: their third cells are 0 and D_k+D_(k+1). The opposite third cell must be B because each allowed triple has exactly one B corner. Coordinate subtraction independently derives its shared ring positions k+4 and k+3, in that order. Consequently the author's matching conditions are correct, with no omitted reflection or shifted side index.

There are exactly four compatible ordered B-placement pairs in each direction. The permitted first placements for directions zero and one are respectively

    {(0,+1),(3,+1),(0,-1),(3,-1)}
    {(2,+1),(5,+1),(1,-1),(4,-1)}.

These sets are disjoint. Every B cell needs both opposite B successors, so no B cell can occur. Every complete vertex requires a B corner, so there is no infinite angle-only SFT configuration. Side equalities cannot restore a missing configuration. This proof uses finite label enumeration and coordinate identities only; the [retained controls](two-hexagon-balanced-rank-five-ring-check.json) carry the source certificate digest.

The reported radius-one SAT, radius-two INFEASIBLE and 56 small-torus INFEASIBLE queries remain bounded controls. This review did not rerun them and does not need their solver verdicts. The independent ring obstruction proves the infinite SFT empty without a CP-SAT infeasibility certificate. No conclusion about alternative native boundary orders or simultaneous polygon/length realization is imported.

The independent checker is nondestructive by default. `--output PATH` optionally writes controls, so registered replay can use a temporary path. The author's original verifier also runs solver controls and writes its retained certificate; it should not be used as a nondestructive registered checker.

```bash
MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_two_hexagon_balanced_rank_five_ring.py
```
