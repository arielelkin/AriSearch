# All native cyclic orders of the balanced two-triangle pair root

Date: 2026-10-12. Status: [independently reviewed VALID within the complete unique-B-pair family](../reviews/two-hexagon-odd-pair-graph-orders-review.md).
This record covers its600 two-triangle native orders, not arbitrary hexagon angle types.

## Domain and symmetry

The abstract pair graph is two disjoint triangles on the six A corner
labels. Fix the actual native order of A to 0,1,2,3,4,5. Its group
partition is then an unordered partition into two three-element sets.
There are binomial(6,3)/2=10 choices; choose the group containing 0 first.
Each group contributes its three unordered pairs. These are the six
distinct B corner labels. The native B order is an arbitrary cyclic order
of those pairs, up to rotation and reversal: 6!/(6*2)=60 choices. Choose
the first pair at position 0 and require the second pair's ordinal to be
less than the last pair's ordinal. This gives exactly **600 rooted orders**.

Every actual native-order assignment of this abstract root is represented:
first label A corners by their actual cyclic positions, then identify the
two pair-graph components; the only remaining choice is the B cyclic order.
Unmarked polygons admit reflection, so reversing B is a sound equivalence.
The 600 objects are not claimed inequivalent under further dihedral changes
of A, component automorphisms, or exchanging the physical species.

Every order has the previously proved six-triple exact closure, rank five,
and positive corner balance. Relabeling preserves those algebraic facts.
Native cyclic order changes spatial legality and is the finite variable
classified here.

## Exact local-state computation

Every triple contains exactly one B corner. A B cell consequently has six
A neighbours. For each of its twelve placements, the producer enumerates
every legal ring of six native A placements using all six central vertex
constraints. A local state records the B placement and its **full A ring**.

Two B states separated by Delta_k=D_k+D_(k+1) must agree on their two
shared A cells. The six Delta directions form the coarser triangular lattice:
Delta_(k+1)-Delta_k=Delta_(k+2). Necessary pruning consists of:

1. Remove a state without a surviving successor in any of the six directions.
2. Remove a state for which, in some adjacent direction pair k,k+1, no
   two successors also satisfy their mutual direction-k+2 compatibility.
3. Repeat each stage until its recorded finite deletions stop.

No actual infinite field can lose a state under either rule. This does not
assert that every surviving state extends globally.

Result: **581 rooted orders have empty pruned cores**. Nineteen remain.
Of these, fifteen have maximum successor degree one in every direction;
their full-state cores have twelve or twenty-four states. Four branching
cores are rooted IDs **0,209,349,549**, with respective sizes 48,48,120,48.

## Side equalities are retained

For a full B ring, each of its six B/A edges and six surrounding A/A
edges forces a native side equality. Take their equivalence closure E_ring
on the twelve sides. Every metric tiling containing that ring has an
actual side equivalence e coarser than E_ring.

For every distinct E_ring in each branching core, a periodic labelled torus
was found whose required side identifications are contained in E_ring.
The four branching cores require respectively 4,4,7,4 such local metric
closures: **19 exact torus escapes**. Therefore, whenever a metric SFT
for one of those orders is nonempty, any occurring B ring supplies a torus
legal for its same actual e. The conclusion is not obtained merely from
an angle-only torus with all lengths declared equal.

The metric producer also tested the older twenty-seven edge-consistent
cores before the stronger triangle pruning. Its retained file contains
45 local metric closures including these 19 sufficient escapes; negative
index-at-most-eight controls on the other closures are **not** global
emptiness claims. No tori failed verification. Index three or six is
sufficient for the retained escapes. A finite torus must have cell count
divisible by three because each vertex contains one B corner, so these
are the only possible indices at most eight.

The fifteen functional cores are intended for the root's separate theorem:
a one-direction functional relation on full B-ring states forces a common
nonzero translational period of any bi-infinite state field. Subject to
that independently reviewed theorem and the reviewed faithful hexagon SFT
reduction, the 581 empty cases, fifteen functional cases and four metric
escape cases exclude this entire 600-order family for every side equivalence.
This record does not independently promote the root's general theorem or
claim a solution of the unrestricted two-convex-polygon problem.

## Certificates and independent checker

Producers:

* `research/searches/two-hexagon-balanced-root-cyclic-orders.py`
* `research/searches/two-hexagon-balanced-root-ring-metrics.py`

Certificates:

* `research/certificates/two-hexagon-balanced-root-cyclic-orders.json`
* `research/certificates/two-hexagon-balanced-root-ring-metrics.json`

The standalone pure-Python checker
`research/reviews/check_two_hexagon_balanced_root_cyclic_orders.py` imports
neither producers nor SFT/solver modules. It reconstructs all rings by
orienting the six A pairs (at most 64 choices per B placement). At a shared
A neighbour, the two prescribed corners must be native adjacent corners;
their difference determines its orientation and hence its full placement.
This independently enumerates exactly the producer's ring sets.

It verifies the 600-order domain, every compatibility pair, every recorded
edge/triangle pruning round, all surviving core degrees, all forced metric
closures and each of the 19 branching escape tori directly by native
corner and side incidences. Its result was:

    PASS: 600 native orders; 581 empty, 15 functional cores,
          4 branching cores covered by 19 exact metric torus escapes.

The torus producer uses OR-Tools CP-SAT, one worker, seed zero, a three-second
timeout per query. SAT witnesses are checked exactly; failed or unknown
bounded searches do not enter the positive coverage argument. Ring pruning
and the independent checker use only finite integer operations.

Nondestructive replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/check_two_hexagon_balanced_root_cyclic_orders.py

Regeneration commands write their explicit certificate paths:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/two-hexagon-balanced-root-cyclic-orders.py research/certificates/two-hexagon-balanced-root-cyclic-orders.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/two-hexagon-balanced-root-ring-metrics.py research/certificates/two-hexagon-balanced-root-cyclic-orders.json NEW_METRIC_OUTPUT.json

The last regenerated file now needs only nineteen final cores; the retained
earlier metric file preserves its additional bounded control queries.
