# Independent shape-first assessment, 2026-10-20 15:19 UTC

Post-assessment audit: the [seven-child hostile review](../reviews/seven-child-mixed-hostile-2026-10-20.md), [eight-child topology review](../reviews/eight-child-radial-topology-hostile-2026-10-20.md), and [independent angle/Y-template reconstruction](../reviews/eight-child-angle-hostile-2026-10-20.md) validate the stated restricted obstructions. The full two-convex objective remains unresolved.

**Unresolved.** The run produced no pair with plane existence and unrestricted aperiodicity. It exposed an important missed preflight theorem, supplied a new seven-child obstruction, and tested the first genuinely admissible eight-child topology. Both eight-child radial angle systems returned exact-solver UNSAT. The new topological proof and solver transcription require independent hostile review; no solver UNSAT is presented as a certificate of the unrestricted problem.

## 1. Deduplication changes the starting point

Read the problem/protocol, discovery log, shape-first deduplication audit, 14:49 assessment, both radial metric reports, and corrected three-child hostile review. The prior `lambda P=2P+H` and `lambda P=4P+H` experiments were already impossible by the reviewed general convex-pentagon dissection theorem, independently of their metrics:

* `research/lemmas/pentagon-higher-partner-positive-conjugate-bound.md` proves every nontrivial convex pentagon partition into children with at least five sides has at least six children.
* `research/lemmas/six-child-topology-universal-wheel.md` proves an exactly-six-child partition has only pentagonal children.

Thus three-, five-, and six-child mixed P/H parents fail before scalar length searches. The new arithmetic gates are valid scoped information but were unnecessary to close those inventories. This is a routing correction, not a defect in their final corrected length calculations.

## 2. Seven children also cannot include a higher-sided child

The full internally checked proof is retained in `astra-seven-child-mixed-obstruction-2026-10-20.md`. It extends the old incomplete seven-child investigation. It allows partial contacts and interior children that touch the parent boundary at isolated points.

In brief, augment the planar child adjacency graph with an exterior vertex O. Join consecutive distinct O-neighbors by narrow paths parallel to their spokes; this supplies a connected graph on boundary children without assuming they actually touch one another. If r>=3 children are interior and b=7-r are boundary children, interior minimum degree five and planarity of the interior induced graph give at least 2r+6 interior-incident edges. Add b exterior spokes and b-1 boundary connections to obtain at least19 edges on8 vertices, contradicting the planar bound18. Two interior children yield a K3,3; zero is excluded by the existing forest/cycle lemma. Hence exactly one child is interior and six touch the parent boundary.

The exact defect identity then forces all seven children to be pentagons: a cyclic boundary containing six different child labels has at least six transitions, whereas any higher-sided child lowers the defect budget below the required seven. The new conclusion is a mixed-parent minimum of **eight children**, pending independent hostile review of the augmentation proof.

For eight children the full boundary-neighbor cycle gives a stronger count when b>=3. With r>=3 this gives22 edges on9 vertices, exceeding21. When b=2 the weaker bound gives equality21 but O has degree2, impossible in a maximal planar graph. Thus the eight-child mixed parent has exactly two interior children. Root assigned the complete incidence audit to `eight_child_topology`, whose files are `eight-child-radial-topology-2026-10-20.py` and its report.

## 3. Complete three-P first-parent angle preflight

The replay `astra-heterotypic-y-gate-2026-10-20.py` checks100 normalized native-center/handedness templates with exact rational linear algebra and rational polyhedra. Fix the first P center to native vertex0 and its orientation positive; choose the other two centers among five vertices and their two orientation signs independently. The equations are the pentagon angle sum540, central sum360, and three distal seam sums180. All native angles must lie strictly between0 and180.

The exact census is:

| Outcome | Templates |
| --- | ---: |
| Inconsistent linear equations | 6 |
| No strict angle solution | 78 |
| Forced adjacent supplementary P angles | 12 |
| All three copies use the same native center | 4 |

The12 omission branches have explicit adjacent-angle equalities, so the elementary half-turn periodic pentagon construction kills them; Rao classification completeness is unnecessary. The four remaining templates are the all-positive orientation and three mixed-parity words. This is a necessary angle gate; it asserts no metric realization for a surviving template.

This Y domain is exhaustive for a convex hexagon partition into three genuine convex pentagons. There can be no seam cycle, since an interior pentagon would require five neighbors. The forest and angle identities force one component, one trivalent interior node, three boundary nodes, no parent-corner split, and no flat child incidence. Every child then contains two parent corners. Consequently the normalization above omits no alternative three-child topology.

For the all-positive same-center template,

    P angles = (120, alpha, beta, 240-beta, 180-alpha),
    H angles = (beta, 240-beta) repeated three times,
    0<alpha<180, 60<beta<180.

The seam lengths at the central P corner must agree. Importantly, the other two outer arms need not agree: the generalized native side word is `(1,a,b,c,1)`, and the hexagon word is `(b,a+c)` repeated. The earlier radial family imposed the extra restriction a=c. The angle gate below includes unequal arms because it imposes no lengths.

For mixed parity the distal seam equations force alpha=90. The H angle word consists of three copies each of beta and240-beta, with changed cyclic order. If H touches the parent boundary at a simple seam endpoint, its angle must have a complementary P angle. The only strict possibilities are beta=90 or150. Either gives adjacent90-degree P corners and a periodic P-only tiling. Thus mixed parity does not rescue an omission-safe eight-child construction, where the topology forces H to be a boundary child.

## 4. The admissible eight-child topology and exact angle gate

The first permitted radial inventory is

    lambda H = 3P,
    lambda P = 7P+H,
    mu=lambda^2=(7+sqrt(61))/2.

It is materially different at the dissection level: two interior P children share a whole side; it is not a three- or five-child parent rejected by the old forest theorem. Label six outer children0..5 cyclically. The two inner children U,V contact respectively `{0,1,2,3}` and `{0,3,4,5}`, and contact each other. Outer children0,3 are opposite shared neighbors. There are two H orbits:

* H at shared0: it contains one parent corner, opposite shared P3 contains none, and outer P1,2,4,5 each contain one.
* H at exclusive1: it contains two parent corners, shared P0,3 contain none, and outer P2,4,5 each contain one.

Both have six boundary seam nodes, eight interior trivalent nodes, and no inserted flat native incidences. The exact primal cyclic words are retained in the JSON result.

`astra-eight-child-angle-gate-2026-10-20.py` assigns every child every native cyclic phase and reflection, and assigns every parent cyclic phase/reflection. It uses exact real alpha,beta in the open intervals above. It requires all eight interior angle sums360, all six boundary seam sums180, and the five cyclic parent-corner angles. No metric equality, side matching, or packing hypothesis is added.

**Both H placements returned UNSAT before their120-second limits.** Results and primal words are in `astra-eight-child-angle-gate-2026-10-20.json`. This is exact solver evidence for the stated finite disjunctive linear angle systems, pending independent reconstruction; it is not yet an independently checkable UNSAT certificate. It rejects the generalized all-positive radial first parent, including unequal arms. Combined with the100-template gate and mixed-parity omission argument, it appears to close every omission-safe P5/H6 similarity substitution with matrix `[[7,3],[1,0]]`, conditional on the eight-child topology proof and independent angle-model review.

A useful independent sanity condition is that every H/P boundary flat lies on one of six parameter lines:

    alpha=180-beta; beta=90; alpha=beta;
    alpha=beta-60; beta=150; alpha=240-beta.

The exclusive H orbit has both H angle types at its boundary endpoints, which reduces its angle parameters to six intersections of the two corresponding three-line families. These conditions are only checks, not the UNSAT proof.

## 5. Stopped alternate first-parent thought experiment

A mirror pair of pentagons with one90-degree seam endpoint and one acute seam endpoint can form a convex heptagon. This gives a genuinely different first-parent inventory `lambda Q7=2P`, but no second parent or forcing was supplied. Two small triangulation explorations tested only simple native boundary patterns for `7P+Q7` and `8P+Q7`: one parent corner per boundary child in the eight-child case, and five corners on six distinct boundary arcs in the nine-child case. They found no prescribed degree pattern among respectively50 and233 reached unlabelled triangulations. Scripts are `astra-eight-child-disk-gate-2026-10-20.py` and `astra-nine-child-disk-gate-2026-10-20.py`. These are exploratory finite negatives only, not complete exclusions of either inventory; no claim of exhaustive geometric search follows. Stop this thought experiment without a new incidence principle.

## Recommendation and remaining work

First independently reconstruct the two eight-child angle systems and audit the planar augmentation. If those checks pass, stop the full three-P/7P+H substitution mechanism, not merely the earlier equal-arm metric. Do not assign another metric search for it.

This assessment has not found a promising surviving materially distinct construction. The next design must supply a complete admissible parent topology with a shared-angle solution before metric fitting. Reusing a new area eigenvalue, increasing a radial inventory, or growing an unforced patch is not evidence of progress toward existence and unrestricted recognition. The global problem remains unresolved; no impossibility theorem for arbitrary convex pairs follows from any result here.

Replay, from repository root:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-heterotypic-y-gate-2026-10-20.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-eight-child-angle-gate-2026-10-20.py

No web literature novelty claim, discovery-log edit, commit, or push was made by this assessment agent.
