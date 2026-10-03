# Hostile review: angle-nonresonance edge forcing

**Artifact reviewed:** [angle-nonresonance-edge-forcing.md](../lemmas/angle-nonresonance-edge-forcing.md).

**Date:** 2026-10-02
**Verdict:** valid after adding isolated point contacts to the proof.

At a genuine vertex in the relative interior of another tile's side, the
straight-through tile occupies one local half-disk.  The other half-disk must
be a finite union of genuine corner sectors whose angles sum to $\pi$.
Local finiteness is available from the finite positive-area protoset.  A
second straight-through tile cannot occupy the opposite half-disk because
the assumed genuine vertex itself has a positive sector.  This covers both
positive-length T-junctions and an isolated vertex-to-side touch.

Once every vertex-to-side incidence is excluded, a positive-length boundary
overlap cannot be a proper subsegment of either native side: the endpoint of
the shorter overlap would be a forbidden vertex-to-side incidence.  Convex
polygon boundaries cannot cross transversely in a tiling with disjoint
interiors.  Remaining point contacts are vertex-to-vertex, so the usual
edge-to-edge definition is satisfied.

The no-sum condition allows repetitions and must be checked exactly.  It is
only sufficient, not necessary: some resonant angle multiset might never be
geometrically realizable at a T-junction.  The claimed finite bound follows
from positivity of the smallest angle.  The theorem makes no claim about
which $2\pi$ vertex sums extend to global tilings.

Combined with the curvature identity, this theorem gives a useful exact
$(5,6)$ target.  Edge-to-edge forcing sets subdivision defect to zero, so
$2D=N_5+O(R)$.  If all exceptional vertices have valence four, each
contributes one to $D$ and their asymptotic count is half the pentagon count.
This is an accounting necessity only, not a local-to-global existence proof.
