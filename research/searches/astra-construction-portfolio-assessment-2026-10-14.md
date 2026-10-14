# Independent construction-portfolio assessment

**Later status:** the directed-offset gate recommended here was subsequently executed and [closed exactly](../lemmas/ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md). Every admissible two-class rule in that topology is the midpoint/common-height periodic component. This historical assessment does not authorize restarting that closed gate. The conditional two-parent proposal remains a separate undeveloped mechanism.

Date: 2026-10-14. Status: strategic assessment, not a construction or reviewed theorem.
Author: independent Astra assessment requested by the user. No construction search or additional agents were launched. No novelty claim is made.

## Recommendation

There is value in one further bounded construction gate now. There is not presently a defensible case for launching two or three full new construction searches in parallel. Allocate a second independent worker to attacking that gate's assumptions, or to specifying a genuinely different scheme before it earns computation. Parallelism should buy independent mechanisms or falsification, not simultaneous enlargement of unsupported patch domains.

The leading gate is **arrow-dependent lateral resection with jointly moving receiving quadrilaterals**. It starts from a certified infinite source and changes precisely the information-erasing assumption killed by the previous two-node rules. Its chance of producing a solution is unknown and probably substantially lower than its chance of yielding a useful finite obstruction. Its information value is nevertheless good: an exact small system can decide whether this topology can retain arrows while still having two shapes.

The fixed Y pair is an incompatible, useful retained object, but its unrestricted partial-contact existence is unknown. The whole-native-edge propagation obstruction closes every whole-edge plane construction for it, not only the 6P4Q quotient. I would not assign another construction search to those coordinates without an explicit partial-contact extension rule.

## 1. Launchable gate: directed triangle exchange on the two-node source

### Changed mechanism and exact scheme

Use the legal thin/thick unit-rhomb source and its exact directed X/Y edges from `../lemmas/ammann-forcing-aperiodicity.md`, Lemmas 5–7. Preserve the auxiliary vertex bipartition of the recent two-node construction. Each source rhomb has two opposite triangle edges and two opposite receiving edges.

For an arrow-directed edge with tail U, head V and unit left normal n, prescribe its donor apex by

    U + a_Z (V-U) + epsilon h_Z n,   Z in {X,Y},

where epsilon selects the side occupied by the donor rhomb, 0<a_Z<1 and h_Z>0. The four real parameters are a_X,a_Y,h_X,h_Y. Offsets are measured from the **arrow tail**, not the counterclockwise boundary start. This matters when the arrow and boundary orientations disagree. The actual donor side is selected by the bipartition rule, not by an imported orientation convention from the older three-shape Ammann surgery.

The two donor apices are the internal tree nodes p,q. Partition the rhomb using the same five tree edges Ap,Bp,pq,Cq,Dq after relabeling its triangle edges as AB and CD. Thus moving either apex changes both receiving quads. Attach to each receiving quad the prescribed triangle outside its receiving edge, using that edge's actual arrow and mark. Adjacent rhombs share the arrow and mark and choose opposite roles, so this is a globally compatible rule whenever the local partitions and output convexity checks pass. Global existence is inherited from the source by an actual piecewise partition; no patch-growth inference is involved.

There are four source/role cases (two rhomb types, two opposite-edge choices), and two output pentagons per case: eight indexed output polygons. Reflections must be admitted in every congruence comparison. Keeping all eight cases is a safe sufficient domain even if some orientations could later be identified.

### Exact invariant before solving

In coordinates A=(0,0), B=(1,0), C=(1+c,s), D=(c,s), write p=(u,h), q=(c+v,s-k). The receiving quad B,C,q,p has area

    s - s(u+v)/2 + c(h-k)/2 + h(v-1)/2 + k(u-1)/2.

Adding a unit-base triangle of altitude ell adds ell/2. This identity was expanded symbolically with SymPy during this assessment. It is an internal algebra check, not independently reviewed evidence. The previous altitude-only formula is recovered by u=v=1/2.

The new lateral terms show exactly why the old pair-mean argument cannot simply be reused: quadrilateral area changes with the arrow-dependent offsets. They do not establish that two classes exist. First impose at most two area values; then impose full congruence. Area alone is never sufficient.

Use cyclic ordered squared-distance matrices for pentagon congruence, including all five shifts and reversal. There are only 127 partitions of eight labeled outputs into exactly two nonempty unlabeled classes. Enumerate these class assignments as a finite symbolic disjunction, with any congruence correspondences handled exactly. Require the two representative polygons to be noncongruent. The assignment count is a bound on a local algebraic gate, not a bound on plane tilings.

### Bounded experiment and stop

1. Construct the eight outputs symbolically over the real cyclotomic coordinate field; derive area and distance equations.
2. Solve this one four-parameter semialgebraic system, with strict support inequalities for every output and strict interior/disjoint partition inequalities for the sectors. First use linear area reductions and polynomial elimination in Sage. Z3 nonlinear-real arithmetic is a secondary discovery tool after algebraic constants are encoded with isolating data.
3. Stop after this exact topology and four parameters. A solver timeout/UNKNOWN is a blocked gate, not permission to discretize more finely or grow source patches. Retain the equations, eliminated branches, exact witnesses, and unresolved residual components separately.
4. Any surviving exact two-class solution immediately faces periodic omission and wrong-arrow assembly attacks. Try the two homogeneous rhomb lattices with all allowed arrow/role assignments in a fixed 2-by-2 carrier, and direct single-species periodic identities. A successful witness kills the candidate. Failure of this deliberately small attack proves nothing.
5. Before any larger enumeration, demand an intrinsic geometric rule for recovering the exchanged chord and its X/Y direction from every placed pentagon, plus a reason arbitrary contacts enforce compatible reconstructed rhombs. Stop as BLOCKED if these are merely assumed. The old three-shape atlas does not apply to the new shapes.

### Independent hostile review

A fresh reviewer should reconstruct source arrows and all eight coordinate outputs independently; check both far endpoints of every glued base; test midpoint/complement offsets and reflection-induced arrow reversals; distinguish necessary congruence equations from sufficient partition inequalities; and actively seek a periodic carrier. Any proposed universal decoder needs separate review of T contacts, opposite handedness, alternate chords and omission. The reviewer must not simply rerun the producer.

**Ranking:** best infinite-existence prospect because existence is source-backed; recognition prospect still poor/unknown. Worth one bounded launch, not an open-ended search campaign. This is one mechanism, not several parallel variants.

## 2. Conditional alternative: two nonconvex polygonal parents with pentagon defects

This is genuinely different from fractional source exchange, but it is **not launchable as a coordinate search yet**. It is included to specify what a second independent construction proposal would have to supply.

A concrete algebraic target is two simple nonconvex parents H,K assembled respectively from 2P+Q and P+2Q, with P,Q convex pentagons. Seek similarity factor phi and rules

    phi H = 2H + K,
    phi K = H + K,

where the right sides mean exact dissections, including specified orientations and seam placement. The count matrix has Perron eigenvalue phi^2. Area consistency forces area(H)/area(K)=phi and

    area(P)/area(Q) = (2phi-1)/(2-phi) = 3phi+1.

This supplies an immediate exact invariant and prevents an unconstrained parent hunt. It is a proposed NEW parent system, not a request to reuse the rational Y coordinates. Genuine nonconvex boundary turns and pentagonal atoms change the closed intact-convex-parent and all-hexagon hypotheses.

The missing prerequisite is a fully specified planar incidence template for BOTH base parent dissections and BOTH substitution dissections, including native far-endpoint correlations. A matrix, an area ratio and a suggestive picture do not provide one. I cannot currently supply that template, so this track should receive at most a bounded analytic design task, not a CP-SAT placement census.

If a template is supplied, the first experiment is an exact support/closure/area solve for that template only. Reject immediately if it reduces to a closed palette, forces quadrilateral atoms, has contradictory far endpoints, or fails convexity. Both parent substitution rules, exact disjoint coverage and an expanding inradius/compactness construction must be certified before claiming an infinite tiling. A subsequent universal geometric grouping into H,K remains a separate, difficult obligation. Unique grouping in a chosen generated tiling is insufficient.

Independent review should first attack the template's topology and all reflection/partial-contact alternatives, then the substitution's boundary closure and plane-extension argument. Stop if no explicit template emerges in one design cycle; do not replace it with a larger number of atoms or arbitrary patch search.

**Ranking:** lower existence confidence than track 1; potentially direct hierarchical recognition if a forced seam gadget can actually be designed, but no such gadget is presently provided. Preserve as an incompatible conditional idea. Do not call it an active promising construction.

## 3. Do not launch another strip or two-hexagon patch track now

A tempting third approach is a quasiperiodic word of independently reusable rows, or irrational horizontal phase accumulation. The reviewed repeatable-strip theorem already defeats finite complete periodic interface states. More fundamentally, a construction in which all rows retain one common horizontal period already has a forbidden nonzero translation, regardless of whether their transverse sequence is Fibonacci or otherwise nonperiodic.

A viable replacement must specify nonperiodic row interiors or unbounded interacting transverse context and then force it from the two convex atoms. Naming Fibonacci order or continuous phase does not supply that mechanism. Likewise, the all-hexagon polygonal-parent perimeter theorem prevents a finite simple-polygon similarity hierarchy on two hexagon atoms. Neither obstruction classifies arbitrary two-hexagon tilings. They do make a third generic strip/substitution search low value without an explicit changed boundary mechanism.

**Ranking:** no launch. Keep the incompatible general two-hexagon possibility open, without resuming its census or pretending the restricted theorems settle it.

## Tools and allocation

Sage exact algebraic geometry is the principal tool for track 1; symbolic area/distance elimination precedes nonlinear feasibility. Z3 can return candidate witnesses or exact finite UNSAT results only for the encoded system; arbitrary plane tilings are outside that model. CP-SAT becomes useful only after a proved finite list of native placements or a specified incidence template exists. It is not the right first tool for unknown continuous edge offsets. Existing primary-source reconstruction and the exact marked-rhomb proof suffice for the first gate; a fresh broad literature survey would not resolve its algebraic bottleneck. Any eventual novelty claim still needs the project's primary-source search boundary.

Suggested bounded allocation: one constructor for track 1, one independently briefed adversary, and optionally one analytic designer for track 2's missing template. Do not present that allocation as three new construction mechanisms. Stop each task at its stated gate. No new enumeration, log/registry mutation, or additional delegation was performed for this assessment.

## Evidence read and scope

Read `AGENTS.md`, `research-problem.md`, `research-protocol.md`, the current restart log and mechanism registry, and these central artifacts:

- `ammann-bipartite-tree-pentagons-2026-10-14.md`
- `ammann-mark-altitude-gate-2026-10-14.md`
- `pentagon-y-interface-2026-10-14.md`
- `../lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md`
- `../lemmas/two-hexagon-repeatable-strip-cycle-2026-10-14.md`
- `../lemmas/nonconvex-parent-hexagon-perimeter-bound.md`
- `../lemmas/ammann-forcing-aperiodicity.md`

The target remains unresolved. This portfolio judgment establishes neither a new candidate pair nor a new exclusion theorem. It is deliberately conservative about whether more parallel constructions are currently worth launching.
