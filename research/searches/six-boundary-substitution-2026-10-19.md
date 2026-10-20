# Six-boundary 7P+3Q substitution gate

Date: 2026-10-19. Status: **independently reviewed valid within its combinatorial scope**. The fixed seed is impossible already by its exact boundary defect budget. This does not exclude another inventory or fewer boundary children.

## Fixed bounded seed and common inflation

P and Q are genuine convex pentagon and heptagon. The Q parent has exactly seven P and three Q children, six distinct boundary children occupying six single connected outer arcs, and four strictly interior children. Allow arbitrary parent-corner seam endpoints, higher seam degrees, and flat incidences: these only strengthen the obstruction. Full-polygon similarity is intended, with no markings.

The arithmetically compatible P inventory chosen for this single cycle is 9P+2Q, giving M=[[9,7],[2,3]] with columns indexed P,Q. Its positive area eigenvalue is mu=6+sqrt(23), length inflation sqrt(mu), and area ratio r=area(Q)/area(P)=(sqrt(23)-3)/2>0. Exactly mu=9+2r and mu*r=7+3r. This arithmetic choice supplies no geometric map.

## Exact incidence and native corner budget

Use the conventions and general finite-dissection identity of the two-parent junction design: B is the number of active seam nodes in parent side interiors; J is the number at parent corners; D is total seam-degree excess above degree three internally and degree one at active boundary nodes; H counts flat child incidences. They are nonnegative integers. For F convex children with native side counts n_i in a p-gon,

    E=I+F-1,
    I+B+J+D=2F-2,
    sum_i(6-n_i)=6-p+B+2J+2D+H.

For the Q inventory F=10 and total native corners 7*5+3*7=56. Consequently

    7-3=6-7+B+2J+2D+H,
    B+2J+2D+H=5.

Each distinct positive-length boundary arc needs a transition to its next child. Six distinct single-arc children give six distinct transition points. Every transition is an active seam node, so B+J>=6. But

    5=B+2J+2D+H >= B+J >=6,

a contradiction. Extra active nodes and any nonsimple junction only increase the left budget cost. No simple dual or trivalence assumption is needed for this contradiction.

For comparison the proposed P inventory has F=11 and 9*5+2*7=59 native corners. It gives B+2J+2D+H=6. A six-boundary-child P allocation could pass this scalar gate only with B=6,J=D=H=0; it would have I=14,E=24 and five interior children. This is only an arithmetic admissibility statement, not a disk map.

## Angle and boundary word gate

At a side-interior transition the child angles sum to pi; at a seam-bearing parent corner they sum to that parent angle; at an ordinary internal trivalent node they sum to 2pi; at each untouched parent corner its child corner equals the parent angle. For Q, assuming exactly six simple active boundary nodes, D=H=0, gives B+J=6 and I=12. The native corner ledger would then require

    56 = 3I + 2(B+J) + (7-J) = 55-J,

which is impossible for J>=0. Equivalently the total child angle is 36pi while the node-angle total would be 2I*pi+B*pi+5pi=(35-J)pi. These are restatements of the same deficit, not additional independent obstructions.

A hypothetical boundary word would have six cyclic distinct child labels C0,...,C5 with transition endpoints t0,...,t5 and seven parent corner roles distributed among their arcs or transition points. The vector sum of directed child boundary subedges along each parent side must equal sqrt(mu) times that parent's directed native edge. Internal seam vectors must cancel in opposite directions, and each child angle/edge word must be a cyclic native P or Q word up to reflection. No such word can satisfy the corner count above, so no exact corner-role assignment, seam endpoint list, or pair of parent disk maps exists for this seed. Supplying invented words or a coordinate solve would skip the failed gate.

## Scope and stop under protocol section 5

The obstruction is the elementary general implication: in any convex p-gon dissection into native convex children, the number of distinct single-arc boundary children is at most sum_i(6-n_i)-(6-p). Here that maximum is five. This bound alone does not prohibit five boundary children; the separately reviewed five-interior native cap lemma excludes a narrower five-boundary all-native trivalent domain.

Stop this six-boundary seed. The exact remaining construction obligation is a compatible pair of full-polygon similarity disk maps after materially changing the Q inventory or boundary-contact/defect mechanism. Within the fixed 7P+3Q inventory, simply asking for six boundary children cannot supply that mechanism. No existence, recognizability, or unrestricted shape-only forcing theorem follows from the matrix arithmetic. The unrestricted two-convex-polygon problem remains unresolved.

Dependencies: research-problem.md; research-protocol.md sections 5,11,19; discovery-log.md current substitution entries; research/searches/two-parent-junction-design-2026-10-19.md; research/lemmas/five-interior-native-cap-boundary-obstruction-2026-10-19.md. No finite graph enumeration, numerical geometry, randomness, or solver was used. Adjacent script checks integer ledgers and the area polynomial exactly. No git or discovery-log edits.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/six-boundary-substitution-2026-10-19.py


## Single authorized pivot: complete abstract two-parent incidence candidate

After the six-boundary obstruction, root authorized exactly one changed seed: Q inventory 9P+3Q, seven distinct simple boundary children, five interior. The following maps pass all native corner and disk gates. Status: **independently reviewed combinatorial candidate, not geometric substitution**. No further count increase or coordinate solve was attempted. See the [Sol hostile review](../reviews/seven-boundary-substitution-incidence-hostile-sol-2026-10-19.md).

Choose P inventory 11P+2Q. The matrix is now [[11,9],[2,3]], area eigenvalue mu=7+sqrt(34), length inflation sqrt(mu), and r=(sqrt(34)-4)/2. Exactly mu=11+2r and mu*r=9+3r. Both parents have five interior P children, denoted i0,...,i4.

### Complete oriented disk maps

The common core has inner fan faces (i2,i1,i0),(i3,i2,i0),(i4,i3,i0), together with these eleven oriented annulus faces:

    (i0,i1,a0), (i1,a1,a0), (i1,a2,a1), (i1,i2,a2),
    (i2,a3,a2), (i2,i3,a3), (i3,a4,a3), (i3,i4,a4),
    (i4,a5,a4), (i4,a0,a5), (i4,i0,a0).

Q adds face (a1,a2,e0), with boundary order [a0,a1,e0,a2,a3,a4,a5]. P adds that face and (a5,a0,e1), with boundary order [a0,a1,e0,a2,a3,a4,a5,e1]. These are dual faces: each triple denotes one internal primal seam junction, not a triangular child tile.

For Q the boundary degrees in that order are [5,4,2,5,4,4,3]; Q species occur at a0,a2,a3 and the other nine children are P. Place respectively [1,0,2,1,2,0,1] native parent corners along those arcs. For P the degrees are [6,4,2,5,4,4,4,2]; Q species occur at a0,a2 and the other eleven children are P. Parent corner allocation is [0,0,2,1,0,0,0,2]. Every interior degree is five. For a boundary vertex v, native child count is degree(v)+1+c(v), giving exactly five or seven in every case.

The JSON certificate adjacent to this record gives **every ordered native child corner word and every internal seam endpoint pair**. Its conventions are exact: f_j is the seam junction corresponding to oriented dual face j; t_k is the parent-side seam endpoint between boundary children k and k+1; u_j is native parent corner j. At each boundary child the word is t_previous, its consecutive u corners, t_next, then its incident f corners along the reverse oriented link. Interior words are the reversed oriented link cycle, started from the lexicographically least neighbor. Every dual edge corresponds to one primal seam: its endpoints are the two incident f nodes, or its sole f node and the corresponding t node. No phase or shape role is silently assumed by these words.

The replay verifies opposite orientations on shared edges, exact outer boundary, connected path/cycle links, Euler characteristic one, prescribed species counts, native corner word lengths, each seam's consecutive incidence in both child words, and native parent corner counts. This is a deterministic construction and checker, not enumeration; no symmetry reduction, random seed, solver, timeout, or floating point. Python standard library only. No geometric realization is certified.

### Budgets and necessary equations

Q: F=12, B=7,J=D=H=0,I=15,E=26. Native corner sum 66=3*15+2*7+7. Native angle total 42pi=30pi+7pi+5pi. P: F=13,B=8,J=D=H=0,I=16,E=28. Native corner sum 69=3*16+2*8+5. Native angle total 43pi=32pi+8pi+3pi. Thus both defect and angle totals are exact, unlike the original six-boundary seed.

The following equations state the next necessary gate precisely. Let alpha_P=(p0,...,p4), alpha_Q=(q0,...,q6), with every entry strictly between zero and pi and sums 3pi,5pi. For each child v choose a cyclic phase s_v and orientation epsilon_v in {+1,-1}; the angle at its kth listed native corner is alpha_species(v)[s_v+epsilon_v*k modulo n_v]. At each f node the three incident child angles sum to 2pi; at each t node the two sum to pi; at each u_j its sole child angle equals alpha_parent[j]. These equations use exactly the certificate words, so they fully specify the finite angle-assignment question without pretending it has been solved.

For the metric gate let z_P,j and z_Q,j be the directed native edge vectors with zero polygon sums and strict convex turning, and let each child have an isometry R_v and translation x_v. Along each seam the directed edge vectors of its two owners must be negatives, with coincident endpoint coordinates. Along the parent boundary, each consecutive sequence of child boundary edges from u_j to u_(j+1) must sum to sqrt(mu)*z_parent,j (after a common parent rotation); all intermediate t nodes must lie strictly on that side in order. Parent corner equality and the t equations above supply the necessary local angle compatibility. This is a necessary boundary word and vector system; no solution is claimed.

### Exact remaining gap and stop

A complete **abstract incidence pair** now exists, and is retained for independent review. Its remaining obstruction or realization question is concrete: do there exist two convex native polygons P,Q, together with the finite phases/reflections, satisfying those simultaneous angle equations, seam edge matching, parent similarity, and nonoverlap? The disk checker does not establish any of these metric requirements. Without a concrete metric mechanism, this branch stops under section 5 after the requested first gate, with no unconstrained coordinate solve. Even successful realization would still require plane existence and unrestricted shape-only forcing; those are separate theorem-strength obligations. No conclusion about aperiodicity is drawn.

**Later exact gate:** the [complete phase/reflection angle solver](seven-boundary-substitution-angle-gate-sol-2026-10-19.md) returned UNSAT, independently reconstructed and reviewed [VALID](../reviews/seven-boundary-substitution-angle-gate-hostile-sol-2026-10-19.md). Thus this fixed incidence pair has no strictly convex realization with common native P and Q angles. The abstract map remains a valid combinatorial object, but is no longer a geometric candidate. The earlier open realization question is closed negatively for these exact words; no coordinate search is warranted.
