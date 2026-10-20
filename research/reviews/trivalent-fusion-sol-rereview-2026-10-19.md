# Independent hostile rereview: trivalent convex-cluster obstruction

**Date:** 2026-10-19  
**Reviewer:** fresh independent Sol review agent; did not develop the claim or its repairs.  
**Artifacts:** [convex-cluster-fusion.md](../lemmas/convex-cluster-fusion.md), specifically “Trivalent-vertex obstruction” and “No finite convex multitile cluster in a trivalent tiling”; prior record [trivalent-fusion-review.md](trivalent-fusion-review.md).  
**Verdict:** **VALID** within the precise scope below.

## Exact claim and assumptions

In a locally finite, edge-to-edge tiling of the entire Euclidean plane by nondegenerate compact convex polygons, with no redundant straight corners and exactly three incident tile sectors at every vertex, every nonempty finite collection of tiles whose union is convex consists of one tile. No assumption of congruence, finitely many prototiles, bounded global tile diameter, periodicity, or regular dual lattice is required. The empty collection is excluded by “patch”; otherwise the empty union is a trivial wording exception.

Here edge-to-edge has its usual face-to-face meaning: two distinct tiles intersect in an entire common edge, a common vertex, or the empty set. Every polygon has positive area, finitely many sides, and genuine corner angles strictly below pi. Tiles are closed and interiors are disjoint. The plane is covered. These are the standard polygonal tiling conventions under which the artifact is stated.

## Independent proof audit

At a vertex incident to precisely three tiles, a collection containing precisely two occupies an angular sector of size 2pi minus the third tile angle, hence strictly greater than pi. Local finiteness permits a disk small enough that no other tile of the finite collection contributes near that vertex; the omitted sector is genuinely missing. A convex union cannot have this reflex boundary sector. Thus inclusion of two incident tiles forces inclusion of the third.

A finite convex union containing multiple tiles must have a shared edge between two included tiles. To justify this without assuming the patch is already connected by edges, choose interior points of two different included tiles. They lie in the open convex interior of the union. A polygonal path inside that interior can be perturbed to avoid the finitely many patch vertices and to cross tile edges transversely. At each crossing the tile on the other side is included, so some pair of included tiles shares an edge.

The artifact propagates this pair across triangular dual faces. Its propagation is valid. An equivalent direct check avoids any dependence on a geometric choice of dual embedding: let A and B be the initial included neighbors. At an endpoint of their shared edge, the other edge of A has an exterior neighboring tile C. Trivalence and the face-to-face property mean that A, B, C are the three incident tiles. Consequently C is included. Continuing around the finite boundary cycle of A forces every edge neighbor of A. Every such neighbor now has an included edge neighbor itself, so the same argument applies to it.

The tile edge-adjacency graph of the entire plane tiling is connected. For any two tile interior points, take a bounded polygonal path in general position avoiding vertices. Local finiteness gives only finitely many intersecting tiles and vertices in its compact neighborhood, so the perturbation and finite crossing sequence are legitimate. The preceding forcing therefore includes every tile in the tiling. There are infinitely many tiles: a finite union of compact polygons cannot cover the plane. This contradicts the finiteness of the collection.

This establishes the theorem, rather than merely reporting absence of a counterexample. The direct propagation argument is a verification of the existing proof, not a change to the theorem.

## Counterexample attempts and boundary checks

- **T-junctions / apparent degree three:** A rectangular grid with a removed seam or a subdivided side can permit convex fusion at apparent degree-three nodes. It violates the face-to-face condition or the prohibition on redundant straight corners. A side-interior sector has angle pi, precisely the equality case excluded from the local strict inequality.
- **Convex two-hexagon or larger honeycomb patches:** Every selected adjacency forces its third tiles at both endpoints. Growing a finite patch cannot terminate with a convex boundary. No hexagon-specific argument is used.
- **Isolated vertex contacts and disconnected tile collections:** A nonempty convex union of positive-area polygons has connected interior. The generic interior path argument forces an included edge adjacency; vertex contacts alone cannot evade it.
- **Holes:** Convexity rules out any open bounded complementary region. At an omitted incident sector, no remote included tile can fill the local gap because of local finiteness and disjoint tile interiors. A hole cannot disguise the local reflex sector.
- **Boundary pinches or multiple boundary components:** A full-dimensional compact convex polygonal union has a simple polygonal boundary. Pinches and inner boundary components are incompatible with convexity; the proof does not assume them away before using convexity.
- **Nonuniform tile sizes and possible accumulation:** No uniform inradius or diameter bound is needed. Local finiteness suffices for both generic paths and local sectors. Accumulating tilings without local finiteness are outside the claim.
- **Dual topology:** Every common primal edge has two distinct endpoints and separates two distinct tiles; each endpoint supplies a triangular dual face. A dual can be drawn within the primal tiles, and local finiteness makes compact generic paths cross finitely many edges. The direct argument above independently confirms the connectivity/propagation conclusion even without this construction.
- **Higher valence:** Four squares forming a larger square exhibit finite convex fusion in an everywhere-four-valent grid. This does not contradict the theorem and confirms that everywhere-trivalent is substantive.

## Defects, repairs, and remaining uncertainty

No mathematical defect found in the repaired local lemma or global theorem. No repairs made and no theorem artifact edited. The usual nonempty-patch and nondegenerate-polygon conventions are recorded explicitly above; they do not require a new geometric hypothesis. The adjective “connected” in the theorem is harmless and already follows for plane edge-adjacency from the stated tiling conventions.

This review clears the independent rereview gate for these two trivalent statements only. It does not review the opening conditional aperiodic fusion theorem, the decorated periodic-lift lemma, frequency tests, any particular source tiling, or a claim that a non-edge-to-edge construction can be converted to an edge-to-edge one. The theorem excludes finite convex macrotiles formed from two or more tiles in the stated source class; it makes no exclusion for T-junctions, higher-valence sources, nonconvex tiles, infinite clusters, or other recomposition operations.
