# Changed eight-child parent: exact support-reflection scheme and angle-slice gate

Date: 2026-10-14. Analytic finite-mechanism gate independently reviewed VALID: [hostile review](../reviews/affine-two-convex-eight-child-support-reflection-hostile-review.md). No geometry search, substitution, second parent, or unrestricted impossibility theorem is claimed. No active process remains.

## Concrete proposed parent outline and placements

The parent is a convex P5 partitioned into seven congruent P children and one Q6. Two central P children share full native side0, and the second is the support-line reflection of the first. Write central vertices z0,...,z4 counterclockwise and reflected vertices zi'. The inner union boundary follows z1,z2,z3,z4,z0,z4',z3',z2'. Seam endpoints z0,z1 are reflex, and the other six vertices are convex. Six straight spokes run from those convex vertices to distinct relative-interior parent-side points.

The sector z4,z0,z4' is one outer P with no parent corner. The sector z2',z1,z2 is outer Q with one parent corner. Each of the four remaining sectors has one outer P and one parent corner. Thus the latter contact the full central sides2 and3 or their reflected copies. A nonreflex outer P contacting its native edgej has its unique parent corner at native index j+3 modulo5: the two neighboring edges are spokes and the remaining two parent-boundary edges meet at that corner. The resulting outer cyclic corner outline is four P parent corners, plus one Q parent corner inserted between the two side2-contact sectors. Its angle word must agree with the original pentagon up to cyclic shift and reversal, as required by similarity with reflections allowed. These placements and native corner equations are specified before any search.

For each source native edge whose length equals a host segment, consider both endpoint assignments and both determinant signs, retaining placements on the opposite side of the host support line. The orientation preserving choice reverses the endpoints; the orientation reversing choice preserves them, relative to each polygon's native counterclockwise edge order. When source and host use the same directed native edge these are the midpoint halfturn and support-line reflection. With a different matching native edge, the preserving mate can require a different rotation. The exclusion below allows every matching native index and either isometry. The reflex P placement is determined by its two consecutive central contact edges. No angles alone are being promoted to an actual Euclidean partition.

## A nonsupplementary angle slice that fails this scheme

Take P angles (120,120+ε,60,120-ε,120), with 0<ε<30 degrees. No adjacent pair is supplementary. Index lengths (x,u,w,v,y); corresponding edge directions can be chosen as 0,60-ε,180-ε,240,300 degrees. At z0 the exterior reflex-sector angle is 360-2*120=120. The outer P can use native corner0 or4, the only120 corners. Its two consecutive contact lengths both equal y. Thus corner0 forces x=y, while corner4 forces v=y. Both equal-angle mating cases must be considered.

Case A: x=y. Normalize x=y=1. Vertical/horizontal closure gives

    w=(sqrt3+u*sinε)/cos(30-ε),
    v=3+2u*cos(60-ε)-2w*cosε.

In particular w>sqrt3>1. If w!=v, a w-contact outer P can use only native side2 or side1 if u=w. Both yield parent angle120. The Q parent corner is then flanked by two parent120 corners, but no corner of the original angle word has two adjacent120 corners. If w=v, all four nonreflex sectors contact a side of this same length. Their possible matching native indices are1,2,3 (indices0 and4 have length1). Thus their parent corners belong only to {120,120+ε}; the original parent also has the two distinct angles60 and120-ε. A single Q parent corner cannot supply both. This excludes the w=v alias, including any further u equality.

Case B: v=y. Normalize v=y=1. Closure gives

    u=2cosε-(2x/sqrt3)sinε,
    w=(2x/sqrt3)sin(60-ε)+2cos(60-ε).

Positive u implies 0<x<sqrt3*cotε. The affine function w-x is positive at x=0, and at the upper endpoint equals sqrt3*(1-cosε)/sinε>0. It is therefore positive throughout the admissible interval. Also w>2cos(60-ε)>1. Hence w differs from x,v,y; only native sides1 or2 can match it. Their parent angles are again120, producing the same impossible Q-corner-neighbor requirement. Thus both reflex P mating cases fail for all admissible metrics in this positive-ε slice.

The initial ε=15, x=y=v=1 example has u=2sqrt(2/3) and w=(1+2/sqrt3)/cos15, but no candidate parent placement was promoted from it. The proof above treats the possible w=v and u=w aliases rather than relying on that numerical ray.

## Resume boundary

The independent review checked the fixed topology, the j+3 parent-corner convention, both reflex120 mating cases, both metric branches, and all relevant native-length aliases. Its [exact independent checker](../reviews/verify_eight_child_support_reflection_independent.py) checks the symbolic closure and strict inequalities over the entire parameter interval, plus finite cyclic/reversed parent-angle exclusions. Replay with `mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_eight_child_support_reflection_independent.py`. No numerical search or process restart is needed. Broader eight-child topologies and other angle words are untouched. The earlier scalar agent's unsaved angle-only sample is not enough to reconstruct a concrete second parent, and no script from that sample survives. Reopening needs a changed actual parent outline/placement rule outside this gate, rather than increasing a source or cluster bound. The root and other agents control independent Ammann cross-source triad work; no such source enumeration was duplicated here.
