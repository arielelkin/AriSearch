# Hostile review: trivalent-vertex fusion obstruction

**Re-review status:** this record includes repairs or extensions made during
review. A separate independent review of the resulting version is not
established by the retained record and remains pending under
[protocol Section 8.2](../../research-protocol.md#82-review-artifacts).

**Artifact reviewed:** [convex-cluster-fusion.md](../lemmas/convex-cluster-fusion.md).

**Date:** 2026-10-02
**Reviewed claim:** A convex cluster in an edge-to-edge convex polygon tiling
cannot contain exactly two of the three tiles incident at a 3-valent vertex.
**Verdict:** **Valid with the stated nondegeneracy convention.**

## Checks and repairs

* “Strictly convex polygon” is potentially misleading for a polygonal set.
  The lemma instead assumes the polygon representation has no redundant
  collinear vertices, hence every genuine corner angle is less than \(\pi\).
* Local finiteness is explicit.  It is automatic for a tiling by a finite set
  of compact polygonal prototiles with positive areas and bounded diameters.
* Valence means the number of incident tile sectors.  The argument is not a
  graph-degree assertion at an artificially subdivided straight point.
* At a trivalent vertex any selected pair of sectors is cyclically adjacent.
  Their aperture is \(2\pi-\gamma>\pi\), where \(\gamma\) is the omitted
  tile's genuine convex angle.
* The omitted sector makes the vertex a boundary point of the cluster.
  A convex set's tangent cone there cannot be the resulting reflex cone.
* If redundant \(\pi\)-angle vertices were permitted and counted in the
  valence, equality could occur.  Removing redundant vertices avoids this
  false edge case.

## Scope

The local lemma forbids a two-tile convex fusion across any edge with a trivalent
endpoint.  For larger clusters it supplies the label rule “all equal or all
distinct” at a trivalent vertex.  It does not prove that this closure rule
propagates through the whole tiling and does not exclude larger convex
clusters by itself. The stronger reviewed propagation result follows below.

## General propagation upgrade

The former multihex conclusion did not actually use six-sidedness or the
regular triangular lattice.  In any connected edge-to-edge tiling whose
primal vertices are all trivalent, the planar dual has a triangular face for
each primal vertex.  Starting from one selected dual edge, the local
all-or-none rule selects the two incident triangles; crossing each boundary
edge inductively selects every face in the connected dual triangulation.
The reviewed theorem has therefore been strengthened to exclude every finite
convex multitile cluster in every such convex tiling.  The connectivity step
can be seen by a general-position planar path crossing successive dual edges;
it does not assume periodicity or combinatorial regularity.
