# Every cyclic order of the balanced two-triangle pair root is excluded

Date: 2026-10-12. **Computer-assisted theorem.** The 600-order data have
passed a fresh independent audit; the general ring reduction and functional
period theorem have separately passed two independent hostile reviews. The theorem
depends on those results in precisely the roles stated below.

## Statement

Let A and B be genuine convex hexagons, permitting every Euclidean isometry
and unrestricted contacts. Label their native corners cyclically. Suppose
their exact set of triples whose angles sum to 360 degrees is obtained as
follows: partition A's six corners into two sets of three; assign each of
the six pairs within those sets to one distinct B corner; the allowed
triples consist exactly of that A pair and its assigned B corner.

Then {A,B} is not aperiodic: it either does not tile the plane or admits
a tiling with a nonzero translational symmetry. This holds for **every**
cyclic corner order of both polygons and every actual side-equality pattern.
The assertion concerns this exact six-triple type, not any descendant with
additional triples or every positive corner-balanced pair.

## Domain coverage

Label A by its actual cyclic positions 0,...,5. There are ten unordered
partitions of these positions into two triples. For each partition, the
six assigned A pairs are distinct. Their order around B is a cyclic order
of six distinct entries modulo rotation and reflection, giving sixty
orders. These ten times sixty **600 rooted representatives** contain every
case in the statement. Further dihedral changes of A may duplicate cases;
duplicates do not omit any native order.

The exact triple rank, closure and positive balance are unchanged by these
reorderings; see [the minimal covering root](two-hexagon-balanced-minimal-covering-root.md).
These algebraic properties alone do not prove the spatial conclusion.

## Proof

Use the reviewed [faithful global SFT encoding](two-hexagon-global-sft-encoding.md)
and its unrestricted defect-free-limit and periodic-development corollaries.
If the actual polygon pair tiles, those results give a legal configuration
of X(T,e) for its exact triple set and actual native side equivalence e.

Every triple contains exactly one B. The
[one-B ring reduction](two-hexagon-one-b-ring-spatial-reduction.md) therefore
places B cells on one index-three coset and represents the configuration by
full B-centred ring states on its triangular lattice. A state records the
B placement and all six neighbouring A placements; it does not forget
chirality, native rotations or neighbouring corner assignments.

For each of the 600 types enumerate all angle-legal full states, initially
ignoring side lengths. Apply the exact neighbour and elementary-triangle
deletions of the ring reduction. Every actual metric configuration uses
only states surviving this angle-only pruning. The retained computation
has the following exhaustive outcomes:

* **581 types:** the surviving state set is empty. Hence X(T,e) is empty
  for every e, contrary to the configuration supplied by plane tilability.
* **15 types:** in at least one direction every surviving full state has
  at most one successor; in fact all six directions are functional here.
  Restricting to the actual metric e cannot introduce extra successors.
  The ring reduction's functional-direction theorem gives a common nonzero
  placement period for any actual bi-infinite configuration. Periodic
  development gives an admitted periodic polygon tiling.
* **4 types:** the angle-state relations branch. For any actually occurring
  ring q, the actual e contains the twelve native side equalities of q,
  denoted E(q), and thus their equivalence closure. The retained library
  has a torus for every distinct E(q) in these four cores. Each torus uses
  only T triples and side matches belonging to the closure of E(q).
  Therefore it is legal for the same actual e. Periodic development again
  gives an admitted periodic polygon tiling.

The branching cases are rooted IDs 0,209,349,549, with respectively
4,4,7,4 forced metric closures. Their **19 torus witnesses** supply the
entire metric library required by the last case. No bounded negative
torus search or angle-only torus with all sides declared equal is used
as a substitute for this metric coverage.

Consequently plane tilability implies an admitted periodic escape in
every case. The pair is not aperiodic. QED.

## Finite certificate and independent verification

The [search record](../searches/two-hexagon-balanced-root-cyclic-orders.md)
states every finite domain, symmetry, state definition, pruning rule,
metric constraint and replay command. Its certificates are
`research/certificates/two-hexagon-balanced-root-cyclic-orders.json` and
`research/certificates/two-hexagon-balanced-root-ring-metrics.json`.

The standalone
[pure-Python checker](../reviews/check_two_hexagon_balanced_root_cyclic_orders.py)
reconstructs every full ring from independently derived canonical triangle
incidences and native placement constraints. It verifies domain coverage, all
compatibility pairs, every pruning round, all successor degrees, the local
side-equivalence closures and all19 metric tori directly from native labels.
It imports no Sage, CP-SAT, SFT or producer module.

The root's fresh auditor independently checked the 600-order records,
including3408 original states,182 deletion rounds,581 empty cores,
15 functional cores,4 branching cores and19 escape tori. These finite
checks and the general mathematical ring/period proof are distinct
acceptance gates; the final status of that general proof remains its own
review record.

Nondestructive replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/check_two_hexagon_balanced_root_cyclic_orders.py

## Scope and non-consequences

The theorem includes all side equivalences, rotations, reflections and
the original unrestricted-contact convention through the reviewed global
reduction. It proves existence of a periodic escape whenever the pair tiles;
it does not claim every original tiling, with possible defects, is periodic.
No geometric realisability of abstract witnesses is assumed: development
is applied only to the actual polygons and their actual T,e.

Higher-rank descendants, other A-pair graphs, angle types with pure stars
or one-A/two-B stars, and pentagon-containing pairs are outside this theorem.
The unrestricted two-convex-polygon problem remains open in this repository.
