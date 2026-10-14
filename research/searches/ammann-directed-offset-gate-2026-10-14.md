# Directed source-arrow offset, two-node gate

Date: 2026-10-14. **Current status: closed for the aperiodic-pair objective.** The later [reviewed exact invariant theorem](../lemmas/ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md) excludes all four three-plus-one assignments. Combined with the two-plus-two result, every admissible two-class rule in this topology is the midpoint/common-height component with periodic omission. The historical UNKNOWN and unqueried corrected system below are preserved as provenance, not current unresolved obligations. No global two-convex-polygon solution is claimed. The original coordinate and branch reductions have a [fresh independent review](../reviews/ammann-directed-offset-hostile-review-2026-10-14.md); the new closure has its own [hostile review](../reviews/ammann-directed-offset-residual-hostile-review-2026-10-14.md).

## Exact scheme and source domain

Use the existing infinite legal marked Ammann rhomb source. For each unit rhomb in counterclockwise order (A=(0,0), B=(1,0), C=(1+c,s),D=(c,s)), use actual arrows:

| type | AB | BC | CD | DA |
|---|---|---|---|---|
| thin | X A→B | X C→B | Y C→D | Y A→D |
| thick | X A→B | Y B→C | Y D→C | X A→D |

Here ((c,s)=(\cos36°,\sin36°)) for thin and ((\cos72°,\sin72°)) for thick. A bipartite vertex coloring chooses either AB/CD or BC/DA as the opposite donor edges. For a donor edge with actual arrow tail (U), head (V), inward sign (\epsilon), and left unit normal (n), its node is

\[
U+a_Z(V-U)+\epsilon h_Zn,\quad Z\in\{X,Y\},\quad0<a_X,a_Y<1,\ h_X,h_Y>0.
\]

The receiving quad on each other edge receives the triangle from the neighboring rhomb, using the shared actual arrow and mark. Its boundary is the counterclockwise receiving edge start, the external incoming apex, the edge end, the next donor node, and the previous donor node. The source partition has the same five-edge tree topology as the earlier two-node construction. Shared source edges have opposite roles; therefore strict valid local sectors give a globally compatible plane partition on the known infinite source. This is an existence mechanism only, conditional on the strict local checks and the two-class gate.

There are eight indexed pentagons (two source types × two opposite donor-role choices × two receivers). A thin rhomb's reflection across diagonal BD preserves every arrow and mark, and exchanges its two role choices. A thick rhomb's reflection across AC does the same. Reflection also carries the inward apex rule to itself. Thus the two roles contribute the same unordered output pair in each type. The eight-indexed gate reduces exactly to four congruence representatives, (T_0,T_1,K_0,K_1), while retaining all seven unlabeled partitions of these four into two nonempty classes. This reduction does not assume that both roles occur on the source.

## Area invariant and eliminated branches

Put (\varphi=(1+\sqrt5)/2), (t=\sin36°), (c_T=\varphi/2), (c_K=(\varphi-1)/2), (s_T=t), (s_K=\varphi t). For each source type, its two output areas sum to the source area, because the two donor triangles comprise one X and one Y, as do the two received triangles. Their signed differences (first minus second) are

\[
D_T=(a_Y-a_X)s_T+a_Xh_Y-a_Yh_X+(c_T+1)(h_X-h_Y),
\]
\[
D_K=(1-a_X-a_Y)s_K+a_Xh_Y+a_Yh_X+c_K(h_X-h_Y)-h_X.
\]

The [reviewed two-plus-two obstruction](../lemmas/ammann-directed-offset-two-plus-two-obstruction-2026-10-14.md) closes all three such partitions. Both crosswise partitions contradict the unequal source-pair area totals. For the within-type grouping, equality of squared-edge sums forces a_X=1/2, and the two area equations plus donor interior force a_Y=1/2 and h_X=h_Y. This is exactly the earlier common isosceles interface with periodic monohedral omission. The complete proof, hypotheses and polynomial identities are extracted in that lemma.

At that checkpoint four 3+1 assignments remained. They are now excluded by exact area, squared-edge and fourth-edge-moment invariants in the theorem linked above.

## Historical residual system and bounded computation

The replayable generator is `ammann-directed-offset-gate-2026-10-14.py`. Its `outputs()` gives all eight coordinate pentagons. `congruence_equations()` compares all ten squared distances under each of five cyclic shifts and reversal. The **current, unqueried** `z3gate()` encodes strict full support inequalities: for every oriented edge of every output pentagon and every source sector, every nonincident vertex lies strictly to its left. It also encodes strict donor-node support against all four source-rhomb edges, and pairwise sector interior-disjointness using the separating-axis theorem for convex polygons. Source sectors lie inside the convex rhomb because all their vertices do. Their oriented areas sum exactly to the rhomb area; hence pairwise interior-disjointness gives exact coverage. Adjacent source rhombs agree on arrows and marks and assign opposite roles, so the resulting pentagons partition the source plane. These conditions, together with (0<a_Z<1,h_Z>0), define strict admissibility independently of any numerical fixture. The algebraic constants satisfy

\[
\varphi^2=\varphi+1,\quad 8/5<\varphi<17/10,\quad
4t^2=3-\varphi,\quad58/100<t<59/100.
\]

It excludes the analytically closed midpoint/common-height component. The disjunction uses at most seven four-representative partitions, corresponding to at most 127 partitions of the eight indexed outputs. It does not discretize parameters or grow source patches. A model would still need independent exact verification of polygon coordinates, source partition, congruence, and periodic escape attacks.

The side-effect-free exact replay command is

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-directed-offset-gate-2026-10-14.py --check
```

It verifies the eight shoelace area identities and prints deterministic structural counts plus the SHA-256 of the ordered exact coordinate expressions. Its frozen output is `../certificates/ammann-directed-offset-gate-algebra-2026-10-14.json`: eight outputs, four role cases, 120 pentagon support inequalities, 88 sector support inequalities, 32 node-support inequalities, 24 pair-separation disjunctions, seven four-output class partitions, and ten dihedral correspondences per polygon pair. This is an algebra and formulation check, **not** a feasibility certificate.

Command used:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-directed-offset-gate-2026-10-14.py --z3 --cap 160
```

That command used the **historical system**, which included positive consecutive turns of each output pentagon and receiving quad, plus strict donor-node containment, but did not explicitly include full support of every sector and pairwise sector separation. The first branch, singleton (T_0) versus (T_1,K_0,K_1), returned `unknown` with reason `timeout` after 30.123 seconds. The driver had already started its second branch when interrupted at cumulative wall 49.702 seconds; that branch has no result. The historical run status record is frozen in `../certificates/ammann-directed-offset-gate-historical-run-2026-10-14.json`. The driver is now set to stop automatically at the first `unknown`, and the current corrected system has **not** been sent to a solver. It is possible that the historical turn-based conditions were equivalent to the explicit full-support conditions once all source geometry is considered, but that equivalence has not been established here and is not assumed. Thus the four 3+1 assignments remain an **exact unsolved semialgebraic residual**. There is no negative classification of the whole directed-offset scheme and no survivor. Total historical solver wall was below the predeclared 180-second cap. No homogeneous carrier, wrong-arrow, omission, or intrinsic decoder check is warranted without an exact surviving pair.

## Current scope and restart

The full four-parameter topology cannot yield an aperiodic pair: all admissible two-class realizations are the known midpoint/common-height periodic component. This is a local scheme classification, not an arbitrary two-polygon theorem. The historical UNKNOWN has been superseded by exact elimination, not by a longer timeout. Reopening requires a changed source partition or shared-triangle interface assumption; more offsets, parameter sampling or source depth within the same stated domain cannot help.
