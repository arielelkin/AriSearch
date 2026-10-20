# Hostile review: radial eight-child angle gate

Date: 2026-10-20. Verdict: **the two stated exact angle systems are UNSAT**, independently reproduced. This is a necessary angle obstruction for the specified `7P+H` second-parent topology and the all-positive three-P radial first parent. It supplies neither a global two-convex-polygon impossibility theorem nor a tiling construction.

## Reconstruction

I used the [reviewed topology map](../searches/eight-child-radial-topology-2026-10-20.md), not the search script's stored vertex words. Its directed neighbor rotations are

```
0: (outside, 1, 6, 7, 5)    1: (outside, 2, 6, 0)
2: (outside, 3, 6, 1)       3: (outside, 4, 7, 6, 2)
4: (outside, 5, 7, 3)       5: (outside, 0, 7, 4)
6: (0, 1, 2, 3, 7)          7: (0, 6, 3, 4, 5)
```

For each child, a corner is the wedge between successive neighbors. The interior wedges produce eight distinct triples of child labels, each incident to three children. The six outside wedges produce six rim seam vertices, each incident to two. Placing the five parent corners into outer arcs according to the two topology orbits gives exactly the primal words recorded in [the original JSON](../searches/astra-eight-child-angle-gate-2026-10-20.json), up to a common cyclic relabeling of rim seams and each inner child's cyclic start. In particular, the exclusive-H orbit places two *consecutive* parent corners on H's three-side outer arc; no angle is silently assigned to an extra child.

The independent [replay script](eight-child-angle-hostile-2026-10-20.py) assigns a real variable to every child-corner slot. For each child it asserts a disjunction over all cyclic rotations and reversals of its native angle word. It uses `P=(120,alpha,beta,240-beta,180-alpha)` and `H=(beta,240-beta)^3`, with `0<alpha<180` and `60<beta<180`. It then asserts eight triple sums of 360 degrees, six pair sums of 180 degrees, and a disjunction over all ten cyclic rotations/reversals of the parent P angle word. This formulation has no phase-indexed `If` expression and derives the incidence slots directly from the graph.

Both orbits return `unsat` with exact Z3 rational linear arithmetic. A stronger control removes all five parent-corner equalities and still returns `unsat` for both orbits. As positive controls, keeping *only* the interior equations or *only* the rim seam equations returns `sat` for both orbits; the conflict arises from their combination. The independent run completed in about five seconds. The original script was replayed separately and returned `unsat` for both orbits in 124 seconds, before its individual 120-second solver timeouts.

Replay:

```
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/eight-child-angle-hostile-2026-10-20.py
```

This reproduces the finite UNSAT claim with a materially different solver encoding. It is solver evidence, not a standalone formal UNSAT certificate; its scope depends on the separately reviewed topology map and the stated first-parent angle family. No metric, dissection existence, unique composition, or unrestricted aperiodicity inference follows.

## First-parent template audit and mixed parity

The separate [independent Y replay](eight-child-y-template-hostile-2026-10-20.py) checks the 100 normalized center/orientation choices: first P centered at native vertex 0 with positive orientation, then two choices of native center among five and sign among two. It uses strict real inequalities and Z3 feasibility directly, not Sage polyhedra or rank comparisons. It reproduces the [original Y census](../searches/astra-heterotypic-y-gate-2026-10-20.py) exactly: 6 inconsistent equation systems, 78 with no strict convex-angle solution, 12 with a forced adjacent supplementary P-angle pair, and 4 same-center systems. The latter are one all-positive and three mixed-sign templates.

The mixed-sign statement also has a short direct derivation. Let the three center signs be `(+,s1,s2)` and call the two P angles adjacent to its 120-degree center `p1,p4`. Every distal seam equation is `p[-s_i]+p[s_{i+1}]=180` (cyclic indices). If any sign differs, the three equations include both `2p1=180` and `2p4=180`, so `p1=p4=90`. The remaining P word is `(120,90,beta,240-beta,90)`, with `60<beta<180`. Each H corner is either `beta` or `240-beta`, irrespective of their cyclic order.

The reviewed topology forces H onto the parent boundary, and each end of its one boundary arc is a simple H/P seam node. At such a node, an H corner and a P corner sum to 180. Comparing the two H corner types with the five P corner types in the open beta interval leaves only `beta=90` or `beta=150`. At `beta=90`, P has adjacent 90-degree corners at positions 1,2; at `beta=150`, at positions 3,4. The implication from an adjacent supplementary pair to a **periodic P-only tiling** is the existing [half-turn hexagon lemma](../lemmas/pentagrid-pentagon-angular-reduction.md#the-adjacent-supplementary-escape), not a new output of the finite census. These two mixed-sign branches therefore fail the required omission test even if a second-parent dissection existed.

Together, the independent Y census, the elementary mixed-sign complement check, and the two eight-child UNSAT checks close this **specific** three-P first-parent and `7P+H` second-parent similarity scheme, conditional on the separately reviewed topological incidence theorem. The conclusion does not cover other first-parent inventories, other substitution matrices, or tilings without such a substitution.
