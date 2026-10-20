# Ammann three-to-two direct construction probe: no new compatible topology

Date: 2026-10-19. Status: **stopped before a new geometric experiment**. This is a negative design checkpoint, not a new obstruction theorem, construction, literature survey, or reviewed result.

## Assigned gate and exact source

The gate was one complete globally compatible cross-source repartition into exactly two strictly convex congruence classes, each with at least five genuine corners, or an exact obstruction for a materially new specified repartition. No such new repartition was specified in this probe. Accordingly no parameter search, patch growth, or congruence census was run.

Use the generic source domain G* in [the reviewed forcing lemma](../lemmas/ammann-forcing-aperiodicity.md). With w=exp(i*pi/5), J=s+t*w, its source words are H=(0,J',1,J,w,J''), P1=(0,J',1,L,K), P2=(K,L,1+w^2,J2,w^2), where J'=1+w^4(J-1), J''=w+w^6(J-w), K=w^2+w^6(J-1), L=1+w^7(J-1-w), J2=1+w+w^2-J. These are the actual reviewed unmarked polygons; no properties of other Ammann tile systems are imported. The source coordinate setting and its documented relation to Healey were read directly in the forcing artifact. No new external primary-source verification or novelty claim was made.

## Concrete design decision and duplicate boundary

The most immediate geometry is to pair P1/P2 across c=KL, fill the two reflex notches of D=P1 union P2 by taking caps from neighboring H, and attempt to compensate H elsewhere. That retains the H/D face identities unless a third final face is introduced at the vanished notch apex. The [reviewed H/D incidence obstruction](../lemmas/ammann-hd-incidence-preserving-convexification-obstruction.md) already kills every such incidence-preserving rule: some H has both J' and J'' as two-face vertices, forcing both flat and leaving at most four genuine corners. Moving cap endpoints without declaring a new branching incidence does not change this hypothesis. This is a duplicate, not a new no-go result.

Introducing a third recipient at each troublesome apex is the necessary concrete change for that proposal. It requires specifying the third recipient's entire boundary, the exact cap taken from each incident source face, and an assignment that uses every transferred region exactly once. Neither a cyclic boundary word nor an assignment was obtained here. Declaring that an H can receive a remote compensating cap leaves a missing global partition rule: it does not tell which source sector supplies that cap, whether another occurrence claims it, or whether all output copies have one of two fixed shapes. Those missing data occur before recognizability and cannot be supplied by source aperiodicity.

Other immediate alternatives were checked against existing artifacts rather than rerun: whole-source fusion must use balanced P1/P2 content in each of its two supports by [uniform resection](../lemmas/ammann-supported-pair-uniform-resection-obstruction.md); retained-boundary cuts face the [area module](../lemmas/ammann-source-by-source-two-area-module-obstruction.md); center-fan edge transfer yields quadrilaterals in the [fractional gate](ammann-fractional-resection-2026-10-14.md); splitting that edge into two bent-interface recipients is already excluded by the [opposite-turn identity](ammann-split-edge-two-recipient-gate-2026-10-14.md). The [two-node pentagon partition](ammann-bipartite-tree-pentagons-2026-10-14.md) is globally compatible and two-class but has explicit homogeneous periodic omission. None is a changed topology for this assignment.

## Omission, mixed periodic escape, and recognizability

There is no candidate pair from this probe, so neither an omission clearance nor a mixed periodic escape test can honestly be reported as passed or executed. In particular, a pair that merely avoids the known monohedral pentagon lists has not thereby passed omission. The old two-node pair has an exact omission escape; the quadrilateral and H/D incidence routes have small-face omission escapes. Those existing failures already terminate their specific rules, before a mixed audit.

For any actual next pair the mandatory first gates remain: exact complete partition, two congruence classes, at least five genuine corners each, individual periodic-omission tests, and a concrete mixed periodic carrier attempt. Even passing those gates would leave a universal decoder or a different unrestricted forcing proof. A remembered source hierarchy is construction data and supplies no decoder for every unmarked target tiling.

## Precise stop and reopening condition

Stop this probe under protocol section 5 because no explicit new exchange topology arose. The missing object is a finite list of new output boundary words and source-sector ownership rules, valid at every source incidence, that introduces a third final face at the obstructed H/D two-face vertices while producing only two fixed strict convex shapes. No theorem excluding that object is asserted. A materially new branching incidence rule would reopen the gate; shifting coordinates, increasing a patch radius, or repeating the closed cap/split-edge families would not.

The overall research objective remains unresolved and active under section 19. This agent was instructed not to edit discovery-log.md or Git; the parent should record this bounded stop in its checkpoint. No independent hostile review is required to treat this as a no-new-result checkpoint, and it must not be promoted to a stable mathematical lemma.
