# Independent shape-first assessment, 2026-10-20 14:19 UTC

**Unresolved.** The fixed all-obtuse P5/Q8 metrics are untileable. The Q9 hub's reported 64 surviving owner patches are invalidated by its collision implementation: cyclotomic elements were ordered before real embedding, and an off-grid quarter-turn was truncated. A corrected two-vertex obstruction is under independent review. Treat the original survival and downstream carrier discussion as withdrawn pending that review. The mixed-midpoint B construction fails its specified forcing gate because whole-host alternatives complete. None warrants additional fixed-metric patch growth.

Read: problem/protocol, discovery-log opening, dedup audit, 13:49 assessment, Q9 hub and mixed-midpoint reports; the root supplied the corrected Q9 status. No discovery-log edit or subagents. This is repository triage, not a literature novelty claim.

## Changed mechanism: a forced complementary corner at an unequal seam endpoint

Use u(d)=exp(pi*i*d/180), with every direction below a multiple of10 degrees, hence in Q(zeta_36). Define p,q uniquely by

    p*u(0) + q*u(150) = -u(50) - (3/2)*u(200) - (1/2)*u(280).

Set L=p+q. Define c,e uniquely by

    c*u(180) + e*u(280) = -L*u(0)-u(50)-u(100)-(1/2)*u(230).

Integrate these directed edge lists from zero:

* P directions (0,50,150,200,280), lengths (p,1,q,3/2,1/2), native angles (100,130,80,130,100).
* H directions (0,50,100,180,230,280), lengths (L,1,1,c,1/2,e), native angles (100,130,130,100,130,130).

Exact real-algebraic checks give

    p=1.094562266451497..., q=0.478779296751258...,
    L=1.573341563202755..., c=1.962272519917858...,
    e=1.388930956715103....

Both close, have positive side lengths, and are strictly convex. Numerical values identify the exact definitions; they are not used for decisions. The replay script asserts all relevant numerical lengths distinct except the named repeats.

**Omission gates already passed.** P has no hit among the fifteen imported Rao pentagon types, including every cyclic shift and reflection and exact side equalities. P-only nontilability is conditional on that imported classification. H-only nontilability has a direct elementary proof: all H corners exceed90, so a hypothetical H tiling is edge-to-edge and trivalent; the only angular triple is100+130+130. H's corner0 has incident lengths(e,L), while its130-degree corners have unordered pairs(L,1),(1,1),(c,1/2),(1/2,e). There is no length-compatible two-corner path from e to L in this list. Thus corner0 cannot be completed. This argument concerns H alone; mixed tilings admit partial contacts.

**Precisely prescribed first geometry gate.** Split H side0 of length L with P side0 of length p and P side2 of length q. At the split, P corner0=100 and P corner2=80 fill180. Their outgoing sides P4=1/2 and P1=1 lie on the same ray. At the endpoint E of the shorter side, P corner4=100 lies against the interior of the longer side. The remaining80-degree sector has exactly one possible native corner: P corner2. Unlike the closed equal-length seam, this construction has a named forced species/index at a nonzero offset.

Enumerate both orders, all actual exterior reflection choices, and all ways of putting P2 into that80-degree gap. Check host, two guests, and this forced continuation simultaneously with real-algebraic separating axes. Then complete both host endpoints simultaneously: one has gap130 (H100+P130), the other100 (H130+P130). Include partial contacts along the outgoing rays; their full native side lengths need not equal. Record where each new ray ends, including collisions with existing tiles. Do not infer a completed vertex merely from angular sums. This gate is a finite prescribed configuration, not permission to enlarge a patch indefinitely.

Compare every H/H full-host attachment on the same length-L edge, including both reflections, and all corner/partial-contact completions there. If such alternatives remain locally interchangeable with no changed successor state, stop the fixed metric. Stop also on any exact overlap or impossible compulsory continuation. Only an observed deterministic or finitely branching offset transport with a separately specified infinite extension could justify a second gate. The present pair has no proved plane tiling, forced split, recurrence, or hierarchy.

For these shapes the complete native angular partitions are: flat180=80+100; full360=100+130+130 or80+80+100+100. Hence every T junction contains the unique P80 corner and a100 corner, while a four-corner junction uses exactly two P80 corners. This gives an explicit contact-network state space for any surviving offset rule. It does not by itself force those junctions to occur or rule out periodic networks.

## Failed precursor and deduplication

An initially derived P=(80,120,100,120,120) with equal outgoing unit sides and H equiangular120 was killed before geometry work: the P metric has Rao type2, reflection sign -1 and offset4. Its exact equations and failed omission test are retained in the same script. The final unequal-seam proposal above also initially had equal P1=P3=1, which gave a different type2 omission; setting P3=3/2 removes all classification hits. These observations explain why closure and a good-looking split cannot replace the omission gate.

The replacement differs from the earlier asymmetric P5/P5 words (80,110,100,120,130)/(60,100,120,130,130), the mixed B words (72,96,120,132,120)/(60,84,144,108,144), the rational half-side fixtures, and the former P5/Q6 full-edge120 bridge. It has a non-equiangular hexagon partner, same-species complementary100/80 guests, and a forced80 corner at the first unequal-seam endpoint. It shares the broad partial-contact idea with earlier work; changing the metric alone would not establish a new mechanism. The specific new falsifiable feature is the restricted three-angle contact network and its compulsory80 successor. Repository text checks and the dedup audit found no identical angle/metric pair. No literature search or novelty assertion has been made.

## Replay and numerical discipline

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/astra-shape-first-assessment-2026-10-20-1419.py

The script checks exact closure, positive real embeddings, strict turns, pentagon omission classification, H corner0 obstruction, and angular partitions. It does not execute the proposed attachment gate. It also retains the killed precursor as a positive classification control. Require exact divisibility before interpreting direction exponents, and convert all signed cross products to AA before min/max or comparison. These are essential corrections exposed by the Q9 audit, not optional precision improvements.
