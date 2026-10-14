# Fresh hostile review: uniformly bounded anchored-strip completion

Date: 2026-10-13. Verdict: **valid as a conditional lemma**. Reviewer independent of author.

Reviewed `research/lemmas/periodic-scaffold-anchored-strip-completion.md`. No exact right-angle pair result is assumed. The component classification and uniform width are hypotheses, not inferred conclusions.

## Uniform candidate finiteness

A whole-side anchor determines a completion tile by native side indices and the two endpoint correspondences on the unoccupied side. This is finite even with arbitrary scaffold orientations. For an invariant width-Wcomponent, a completion placement with centroid/reference point in a length-|v|slab is contained in a bounded rectangle enlarged by tile diameters. Its anchor scaffold tile meets a further bounded enlargement. Disjoint positive-area scaffold tiles give a uniform finite bound on anchor count, and hence on candidate placements per slab. To avoid interpreting a reference point outside a polygon, take the centroid, which is available without changing the statement. Translation byvprovides coherent labels in every slab. Candidate duplicates and tile symmetries only reduce the alphabet.

## Coverage SFT and cycle extraction

All candidates are compatible with the scaffold and have their interiors in the component. Diameter bounds give a uniform finite window of slab labels controlling every tile intersecting the test slab. Both nonoverlap and coverage of the component portion are Boolean properties of finitely many selected candidates. The portion is bounded transversely and longitudinally; periodic scaffold geometry supplies the same predicate in every slab. No assumption of a finite global orientation alphabet or simply connected component is used.

A legal bi-infinite completion gives a bi-infinite path in a finite directed graph. Any infinite path in that graph repeats a vertex, giving a directed cycle; repeating the cycle satisfies every local window predicate, including coverage. With integerN0and a radiusKchosen at least1, the stated boundB=(2^N0)^(2K)bounds the graph's vertex count and a simple cycle length. These harmless choices are possible under the hypotheses. Thus infinitely many strips still admit periods dividing the single finite lcm(1,...,B).

## Component orbits and global closure

A moving component is not allowed a nontrivial stabilizer; its translates are assumed pairwise distinct. Its stipulated finite completion makes its region bounded, and translating one valid completion gives compatible orbit choices because the scaffold isvperiodic. This conclusion would fail without the no-stabilizer and finite-completion hypotheses, but they are explicit. Different component interiors are disjoint, so replacements cannot have cross-component interior overlap. The resulting finite-prototile packing is locally finite by area/diameter bounds and has closed support. Covering all open complement interiors plus retaining the closed scaffold covers all plane points, including limiting component boundaries.

## Scope attacks

An arbitrary periodic scaffold may have a wide component, a component with a proper multiple-of-vstabilizer, or an unbounded moving component; none is covered unless it satisfies the actual stated classification. The lemma expressly leaves that classification to the application. In particular the periodic Q-core theorem alone is insufficient to invoke this completion lemma. No substantive defect found within the exact hypotheses. No claim about all pairs, all periodic scaffolds or double periodicity follows.
