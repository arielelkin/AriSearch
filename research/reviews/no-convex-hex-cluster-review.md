# Hostile review: no finite convex multihex cluster

**Artifact reviewed:** [convex-cluster-fusion.md](../lemmas/convex-cluster-fusion.md).

**Date:** 2026-10-02
**Verdict:** **Valid with genuine-corner, edge-to-edge, trivalence, and local
finiteness hypotheses.**

The review checked that a convex union with more than one positive-area tile
must contain a full-edge adjacency; vertex-only contacts cannot connect its
open interior.  At each endpoint of such an adjacency, omitting the third
tile creates a reflex aperture because its genuine convex angle is less than
\(\pi\).  Thus the cluster's dual vertex set is closed under completing both
triangles incident to every included triangular-lattice edge.

The existing honeycomb combinatorics lemma identifies the dual with the
triangular lattice.  Closure of one edge under both triangle completions
grows every lattice ball and is infinite.  Therefore a finite convex patch
has one tile.

Weak polygons with redundant \(\pi\)-angle vertices, T-junctions,
higher-valence vertices, and merely point-connected “clusters” were
explicitly excluded.  The theorem is a cluster obstruction, not a statement
that all two-hexagon tilings are periodic.
