# Equivariant one-block obstruction for the Walton hexagon

**Status:** proved, conditional only on the explicitly stated compiler model;
the finite claims have replayable exact certificates.

**Review coverage:** the underlying finite searches have
[vertex](../reviews/walton-vertex-rank-review.md) and
[state-assignment/relabeling](../reviews/walton-state-assignment-review.md)
reviews. The group-theoretic upgrade below has no separate whole-claim
hostile-review record.

## Theorem

Consider a compiler from the Walton--Whittaker decorated regular hexagon to
two labelled convex hexagons (A,B) with these properties:

1. it is **one-block and equivariant**: the geometric prototile and placement
   assigned to a source tile depend only on that tile's decorated state, and
   commute with every Euclidean isometry;
2. it takes each of the two global-charge source orbits to a geometric-
   prototile placement orbit (the two images may be the same type);
3. every source-legal full-edge contact is geometrically possible and every
   source-legal trivalent vertex has angle sum $2\pi$; and
4. all side contacts used by those vertices are full-edge contacts, so their
   paired sides have equal length.

If both target types occur, then $A$ and $B$ are congruent regular hexagons.
If only one occurs, that target is regular.  In either case this compiler
cannot yield an aperiodic pair.

## Proof

The uncharged spatial symmetry group of a regular hexagon is $D_6$.  Each
global charge choice of the asymmetric Walton decoration is one free
$D_6$-orbit, and the placements of each labelled geometric hexagon are also
one $D_6$-orbit after a reference slot is fixed.  An equivariant map between
two free transitive $D_6$-sets is determined by the image of one state and is
bijective onto its orbit.  Fixing the reference for the first image, the
relative image for the second therefore
has six shifts and two chiralities.  The two source charge orbits may also be
interchanged.  Thus, up to a common relabelling, the compiler is one of
$6\cdot2\cdot2=24$ relative choices.

[research/searches/walton_relative_relabeling_rank.py](../searches/walton_relative_relabeling_rank.py) enumerates precisely
these choices.  For each it independently considers all 24 geometric corner
flags (two types, six corners, two placement chiralities), all $24^2$
ordered contacts, and all $24^3$ ordered trivalent triples.  The R1
near-endpoint bit and R2 charged-orientation rule are evaluated before a
triple is retained.  The result for every relative choice is:

* 240 compatible ordered flag contacts;
* 1,056 source-legal ordered vertex triples;
* rational rank 12 in the twelve deviations of the corner angles from
  $2\pi/3$, after adjoining the two hexagon angle-sum equations; and
* one side-length equivalence class containing all twelve side slots.

If the charge orbits map to distinct types, the rank statement forces every
angle of both hexagons to be $2\pi/3$.  The contact equalities force every
side of both hexagons to have a common length.  An equiangular equilateral
hexagon is regular, so $A$ and $B$ are congruent.  If both charge orbits
instead map to the same type, identify the corresponding two sets of
geometric variables; the already-full-rank system still forces that sole
image hexagon to be regular.  In either case a regular image hexagon has a
lattice-periodic monohedral tiling.  Since a tiling by the pair may omit the
other prototile, aperiodicity fails.  This proves the theorem.

The exact output is retained as
[research/certificates/walton_relative_relabeling_rank_certificate.json](../certificates/walton_relative_relabeling_rank_certificate.json).

## Why this does not solve the research problem

The theorem does not cover a compiler depending on a tile's neighbourhood or
hierarchical address, a non-bijective factor with additional recognition, a
strict extendible sublanguage that intentionally discards some source-legal
contacts, or a different aperiodic source system.  Those are genuine logical
possibilities, not technicalities.  The result does show that merely changing
the relative rotation, reflection, or charge convention of the obvious
one-tile Walton transcription cannot work.
