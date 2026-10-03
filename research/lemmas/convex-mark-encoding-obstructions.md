# Local obstructions to encoding matching rules with convex polygons

**Status:** Proved.  These are local obstructions, not an impossibility
theorem for nonlocal geometric encodings.

## Carrier-preserving obstruction

Suppose an encoding replaces a decorated convex carrier \(C\) by an unmarked
convex polygon whose occupied support is required to remain exactly \(C\).
Then the polygon is \(C\) itself; there is no boundary freedom with which to
encode the decoration.

More locally, if two convex encoded tiles fill neighbourhoods on opposite
sides of a source carrier edge, their common interface lies in a supporting
line.  Interior-disjoint convex sets on the two sides are separated by that
line, and local gap-free coverage makes their interface the full carrier
segment.  Convex jigsaw modulation therefore cannot encode colours or arrows
while preserving a square/rhomb grid.

For Wang squares this leaves an unmarked square; for Penrose carriers it
leaves the two unmarked rhombs.  Each resulting quadrilateral has a periodic
monohedral tiling, so monohedral escape kills the proposed target pair.

## Reflected edge self-match

### Lemma

For every edge \(e\) of a convex polygon \(P\), the union of \(P\) with its
mirror image across the line containing \(e\) is a legal two-tile patch whose
tiles share all of \(e\).

### Proof

Convexity places \(P\) in one closed half-plane bounded by the supporting
line of \(e\).  Its reflected copy lies in the opposite closed half-plane.
Their interiors are disjoint and their intersection contains exactly the
shared edge (apart from a degenerate symmetry which still gives no interior
crossing). \(\square\)

Hence a one-source-edge/one-polygon-edge encoding cannot locally simulate a
source edge-state for which reflected self-contact is forbidden.  Equal edge
lengths cannot repair this obstruction.  Endpoint angles may prevent the
patch from extending to a plane tiling, so the lemma refutes only a claimed
**local** matching equivalence; a nonlocal vertex-corona mechanism remains
logically possible.

## Reflection closure obligation

Because target tiles may be reflected, every encoded state automatically
comes with its mirror state.  A source matching system used in a proof must
remain strongly aperiodic after those mirror states are adjoined, or the
geometric proof must globally forbid their extension.  Directed-arrow or
fixed-handedness arguments do not transfer without this audit.

Together these facts require a successful convex encoding to alter the
global carrier geometry and prove nonlocal forcing, recognizability, and
resistance to partial-edge contacts.  They do not rule out such a mechanism.
