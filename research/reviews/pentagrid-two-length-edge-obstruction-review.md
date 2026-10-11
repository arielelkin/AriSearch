# Fresh review of the two-length U/V edge obstruction

**Verdict: valid for edge-to-edge tilings only.** Reviewed 2026-10-10 by an
agent who did not develop the metric fixture, its obstruction, or its
seventeen-star certificate. The unrestricted tilability of this pair
remains unresolved.

The reviewed claim is
[the two-length edge obstruction](../lemmas/pentagrid-golden-metric-two-length-edge-obstruction.md):
U has after-side angles (1,3,4,4,3) in pi/5 units and side lengths
(L,L,S,S,S); V has after-side angles (2,2,4,3,4) and side lengths
(L,L,L,S,S), with L=phi^3 and S=1. No plane tiling by this fixed pair is
edge-to-edge, allowing reflections and either shape to be omitted.

## Independent exact check

The new checker
[verify_pentagrid_two_length_edge_obstruction.py](verify_pentagrid_two_length_edge_obstruction.py)
imports none of the author's producer. It reconstructs native corner
classes from adjacent cyclic side labels rather than trusting the labels
in the certificate. It enumerates all angle-count vectors with total10
by recursive residual budgets rather than a rectangular Cartesian product.
For each vector it checks an actual closed walk through the numerical
side-length symbols, using every corner once, rather than the author's
parity-and-connectivity test. Reflections permit a corner's two side
labels to be traversed in either direction.

The independently obtained complete list agrees with all seventeen
retained full-star vectors. The checker also verifies exact polygon
closure modulo Phi_10 using integer polynomial arithmetic, and recovers
the after-side angles from the directed edge turns. The distinct positive
lengths follow from the supplied embedding: phi=2Re(z)>8/5>1, hence
phi^3>1. The polygons' strict convexity is also consistent with the
reviewed metric data: their positive edge vectors are in cyclic direction
order with successive turns in (0,pi), total2pi, and close exactly.

Actual execution completed successfully:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_pentagrid_two_length_edge_obstruction.py
```

It passed exact closures, corner classes, all seventeen full length cycles,
the opposite-edge contradiction, V-only exclusion, and the separate
enumeration of all nine half-angle signatures.

## Full-star and endpoint attacks

At a full edge-to-edge vertex each incident ray is a whole shared side,
so consecutive corner sectors must agree on its numerical length L or S.
An LL or SS corner preserves that ray symbol; an LS corner changes it.
A circular sequence must change symbol an even number of times and must
use a single connected length cycle. The author's necessary condition
is therefore correct and reflection-invariant. It is not asserted to be
sufficient for extending a vertex into a geometric tiling.

After placing a U144_SS corner, the remaining angle budget is6. If a
switch occurs, at least two switches are necessary, and their minimum
total angle is6, attained by two U108_LS corners. A V144_LS switch already
uses4, so a second switch would exceed the budget. If no switch occurs,
all remaining sectors must stay on the S symbol; the only way to fill6
is two V108_SS corners. Thus the two 108 sectors must both be U or both
be V. A mixed U108/V108 pair changes the symbol once and cannot close.

U side3 is a unit side whose two endpoint angles are144. In an
edge-to-edge tiling it is matched to one whole side of another tile. At
each endpoint the two possible full stars require that neighbor's seam
corner to be108. Therefore that same neighboring side joins two108
corners. U has two nonadjacent108 corners; V has only one108 corner.
Neither has such a side. This excludes every U occurrence, independently
of orientation, reflection, frequency, or any global counting argument.

With only V present, a full star containing its108 corner must have angles
3+3+4 or3+3+2+2 in pi/5 units. The former changes L/S once; the latter
contains both LL and SS loops without a switch and so is disconnected.
Neither is a numerical length cycle. A V tile has a native108 corner,
so a V-only edge-to-edge tiling is impossible. This handles the omission
cases. The additional window count inequality in the author's lemma is
also true on all seventeen stars but is unnecessary for the proof.

## Why partial contacts really evade the argument

The checker enumerates all nine typed native half-star count vectors of
angle sum5. In particular U36_LL+U144_SS and V72_LL+V108_SS have totalpi.
They can be realized as actual finite three-tile patches covering a small
neighborhood of the proposed vertex, not just as numerical sums:

Place the two chosen corner sectors consecutively in the upper half-plane.
Their angle sum ispi. Each convex tile is contained in the wedge formed
by its two supporting sides at that corner, so the two complete tiles
have disjoint interiors. Their common ray contains one side of length L
and one of length S. Since L>S, their contact ends at a native corner of
the shorter side inside the longer side. Place a third copy with the
midpoint of one supporting side at the original vertex, with its interior
in the lower half-plane. It is disjoint from the first two. A sufficiently
small disk is covered because the first two tiles supply the two corner
sectors and the third supplies the straight sector.

This exact convex-sector construction is available for either of the
listed half stars. It proves a legal local T-junction patch; it does not
prove extension to the plane. At these contacts the adjacent ray lengths
are unequal whole native side lengths, so the circular whole-side length
test cannot be applied. Other partial full contacts can similarly break
whole-side bookkeeping.

The author correctly preserves this distinction: any unrestricted tiling
of the pair must use partial contacts, but no unrestricted impossibility
or aperiodicity is claimed. A proof about extension and all partial
contacts is still required before this fixture can become a solution.

No defect or repair was necessary. The result is a specific geometric
restriction on one exact pair and leaves a concrete partial-contact
construction problem; it does not close the user-proposed avenue.
