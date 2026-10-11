# Fresh hostile review of the residual Robinson-rhomb assembly

**Reviewer:** pending_reviews, 2026-10-10. The reviewer did not develop the
root-owned residual producer or certificate. The independent audit imports
no producer code and uses clipping geometry instead of separating axes.

**Verdict: valid** for the complete fixed finite source-cluster geometry
domain. All 28 U boundary words have geometric clusters; among 185 V words,
168 have clusters and 17 are impossible in the complete residual domain.
Every positive certificate was independently checked, and all 17 negatives
were independently replayed without failed-state memoization. These are
finite unit-rhomb/half-rhomb packings with the stated macro boundary, not
Penrose-arrow legality, whole-plane repartition or aperiodicity results.

## Claim, exact domain, and reviewed dependencies

The [producer](../searches/pentagrid-robinson-residual-rhombs.py) starts from
the complete 28 U and 185 V boundary-word domains surviving the
[reviewed exterior-completion geometry](pentagrid-robinson-boundary-geometry-review.md).
U has four forced interior boundary half-triangles and V has seven.
Each is completed to its unique full source unit rhomb, including its
outside half. The exact height/wedge vector q and diagonal counts d force
remaining source-rhomb counts r_ij=(q_ij-d_ij)/2, with totals six for U and
nine for V. These are determined by the macro area and actual source
pairing, not a guessed maximum patch size.

The search tests the fixed b=c=1 U,V polygons, the specified unit thin/fat
source scales, the fixed ten unit directions, and every retained ordered
boundary word. Rotations and reflections are included through the source
frame and the four source placements at an oriented native edge. No child
metric variation, arbitrary non-source triangle partition, arrow rule,
frequency condition or infinite extension is searched.

## Soundness and completeness of native-edge peeling

Subtracting the counterclockwise forced triangles from the subdivided
counterclockwise parent boundary gives the oriented native-edge chain of
the residual region. Every uncancelled edge is unit length. The dictionary
preserves exact native endpoints; it does not join collinear successive
edges. The residual lies to the left of each oriented exposed edge,
including boundaries of holes or different residual components.

For an exposed native edge a to b with b-a=z^k, any valid source-rhomb
cluster must have an entire rhomb side there. Its other adjacent unit
vector lies to the left and is exactly z^(k+d), with d=1,2,3,4. These four
choices include both thin angles 36/144 and both fat angles 72/108. There
is no fifth choice in the source direction frame. Thus the producer's
candidate list is complete and finite for that edge. Its translation is
anchored by the edge, so no finite absolute-position assumption is made.

Parent containment, interior disjointness and native full-edge compatibility
with all fixed completed boundary rhombs and already placed residual rhombs
are necessary. The additional original unit-boundary native-vertex filter
is necessary in a source tiling as well. Rejecting an orientation whose
remaining count is zero is exact. Subtracting an accepted rhomb updates the
native residual chain and reduces the remaining count by one. Every actual
cluster has a branch that places its rhomb adjacent to the chosen edge;
choosing the edge with the fewest candidates, or stopping the edge scan
when one candidate is found, cannot remove this branch. A zero-candidate
edge proves that current state impossible.

The recursion ends after exactly six or nine residual placements. Contained
pieces with disjoint interiors and the exact total area cannot leave an
open macro gap; the closed boundary chain must also vanish in a complete
cluster. Conversely a returned certificate is checked directly as a packing
and coverage witness. Each valid cluster supplies a full branch regardless
of the chosen exposed-edge order. Holes and disconnected residual regions
do not undermine this argument.

The failed-state memo key includes the exact native boundary chain and
remaining orientation counts. For two admissible partial fillings with the
same chain, the winding function of the chain gives the same uncovered open
region. Therefore they occupy the same region. Any future piece interior
disjointness depends on that region, not its internal decomposition. A future
positive-angle contact can occur only on its boundary; all native boundary
edges and endpoints remain in the key. Internal native vertices have a
filled neighborhood and cannot admit another genuine tile sector. Thus
future full-edge compatibility also agrees. Fixed completed exterior rhombs
and original native unit vertices do not vary between states. This justifies
the memo key. Independently, the negative replay below uses no failed-state
memo at all, so the accepted negative results do not depend on this argument.

The documented first constructor attempt failed before a boundary was
searched because cached coefficient tuples were passed to the field
constructor in the wrong form. The corrected producer uses list conversion.
That execution failure is not a search result. The retained certificate
reports the whole domain complete under its 120-second limit, with no
timeout. No failure or interruption is reported as UNSAT.

## Independent validation of every positive witness

The [independent checker](verify_pentagrid_robinson_residual_independent.py)
imports only the reviewer's independently written height and clipping
checkers. It first reruns the full prerequisite word/geometry audit and
compares the residual record set with the complete surviving domain.
It reconstructs every forced half and full boundary parent from the word.
The residual rhombs are decoded directly from their exact field coefficients.

For all 28 U and 168 V positive records it verifies:

* each residual polygon is a genuine counterclockwise unit rhomb, with
  opposite edge pairs and directions in the source frame;
* its actual ten unit-axis-pair counts equal the independently derived
  (q-d)/2 vector, with exactly six or nine residual rhombs;
* every residual rhomb is contained in the convex parent by exact clipping;
* every pair among residual rhombs and completed boundary rhombs has zero
  interior intersection area and no native vertex inside the other's side;
* forced halves and residual rhombs have exact total parent area and are
  contained and interior-disjoint, proving exact closed macro coverage.

Containment plus disjointness plus area equality implies coverage: any
omitted parent interior point would have an omitted open neighborhood of
positive area. Boundary coverage follows from closedness of the finite union.
The exact source-thin/fat triangle counts therefore agree with the parent
area and height/wedge identity. These tests include every outside boundary
mate, not just the macro's selected halves.

The checker additionally integrates the unit-edge lift on the entire finite
completed packing, including the exterior halves, and reports no height
inconsistency among any of the positive records. The first U and V witnesses
are independently rechecked explicitly. This finite graph consistency does
not prove extension to a whole-plane source or Penrose arrow matching.

## Independent replay of every negative boundary

For the 17 reported V failures, the checker rebuilds the native residual
boundary and all four candidate rhombs per exposed edge. It uses its own
clipped-area containment and overlap predicates, dot-product side-interior
predicate, reversed candidate order, and no failed-state memo. Its bound is
still the exact required remaining-rhomb count.

All 17 fail already at the initial residual state: each has an exposed
native unit edge with no admissible rhomb after parent, completed-boundary,
unit-vertex and orientation-count restrictions. Each negative replay visits
one node. Hence the full negative conclusion is supported by direct complete
four-choice rejection at an exposed edge, without a deeper bounded-search
extrapolation or dependence on the author's memoized backtracking.

| Parent | Complete boundary domain | All positive certificates verified | All negative boundaries independently replayed | Negative replay nodes |
| --- | ---: | ---: | ---: | ---: |
| U | 28 | 28 | 0 | 0 |
| V | 185 | 168 | 17 | 17 |

No positive certificate has a finite whole-patch height inconsistency.
The complete record sets, SAT counts and first witnesses match the retained
[certificate](../certificates/pentagrid-robinson-residual-rhombs.json).

## Attacks, repairs, uncertainty, and replay

Attacks included missing reflected rhomb placements, assuming a connected
residual, replacing whole native edges by merged line segments, pruning
by a guessed area bound, candidate positions not anchored to the boundary,
ignoring exterior halves, caching states with different internal fillings,
losing native subdivision vertices, a zero-area contact violating full-edge
legality, physical closure mistaken for exact height closure, and treating
finite source geometry as infinite Penrose extraction. The explicit source
domain, complete four-choice argument, exact native chains, independent
clipping certificates and memo-free negative replay address these attacks.
No substantive defect or mathematical repair was required. No uncertainty
remains in this finite geometric claim.

Penrose arrows, source-atlas compatibility, a global extraction/repartition
and forcing by unmarked U/V convex polygons remain unproved. The pre-existing
selected compiler with T-junctions remains rejected; the new witnesses are
other geometric source-cluster candidates. No priority claim or aperiodic
pair is established by this audit.

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_residual_independent.py
```

The command completes using exact rational/cyclotomic arithmetic. It uses
no producer import, numerical tolerance, solver, random seed, increased
bound or timeout to assert a negative result.
