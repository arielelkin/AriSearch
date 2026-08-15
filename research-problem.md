# Two convex tiles that force aperiodicity

## Objective

Find two unmarked convex polygons whose geometry alone permits tilings of the
Euclidean plane, but permits no tiling with a nonzero translational symmetry.
The result must be an explicit construction with a complete proof, plausibly
new within a documented literature-search boundary.

## Definitions

Let `P = {A, B}` consist of exactly two distinct congruence classes of compact
convex polygons with nonempty interiors and exact coordinates.

A `P`-tiling is a covering of the Euclidean plane by isometric copies of `A`
and `B` with pairwise disjoint interiors. Translations, rotations, and
reflections are permitted. Contacts are unrestricted and need not be
edge-to-edge. Tiles carry no colors, markings, orientations, adjacency rules,
or other placement restrictions. A tiling need not use both prototile types.

The pair `P` is **aperiodic** when:

1. at least one `P`-tiling exists; and
2. every `P`-tiling has no nonzero translational symmetry.

The quantifier is over every tiling admitted by the two shapes, not merely a
favored substitution, hierarchy, generator, or local-isomorphism class.

## Acceptance criteria

A successful result must include:

1. **Exact tiles.** Give finite exact definitions of `A` and `B`; algebraic
   coordinates must include defining data sufficient for exact verification.
2. **Existence.** Prove that the shapes tile the entire plane. Arbitrarily
   large finite patches are insufficient.
3. **Shape-only forcing.** Prove that every admitted tiling is nonperiodic,
   including tilings using reflections, partial-edge contacts, unintended
   assemblies, or only one prototile type.
4. **Exact computation.** State the finite domain of each proof-relevant
   search, retain replayable commands and certificates, and provide a small
   independent verifier where practical. Bounded failure to find a periodic
   tiling is not an aperiodicity proof.
5. **Novelty boundary.** Search current primary literature, record the queries
   and closest constructions examined, and state novelty only relative to
   that documented boundary.
6. **Reproducible report.** Produce a self-contained mathematical report and
   preserve all stable lemmas, counterexamples, searches, certificates, and
   hostile reviews under `research/` as specified by `research-protocol.md`.

Symbolic matching rules, substitutions, recompositions, SAT/SMT searches, and
known aperiodic tiles may be used as intermediate tools. They count only if
the final two convex unmarked shapes enforce the claimed structure without
supplementary rules.

## Non-results

The following do not resolve the problem:

* a marked pair or an imposed edge-to-edge, orientation, or chirality rule;
* one nonperiodic tiling when another admitted tiling may be periodic;
* a finite patch, numerical coincidence, or visually persuasive rendering;
* a candidate with an unproved extension, recognizability, or forcing lemma;
* a bounded search with no periodic witness;
* a known construction, literature survey, or research framework; or
* a weaker theorem obtained by silently changing the definitions above.

Conduct the search and preserve partial progress according to
`research-protocol.md`. Do not present partial progress as a solution.
