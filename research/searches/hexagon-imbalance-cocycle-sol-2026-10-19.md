# Equiangular hexagon imbalance: exact cocycle gate and its stopping certificate

Date: 2026-10-19. Status: internally checked, pending independent hostile review. The minimal local imbalance gate is **feasible with two noncentral species**, so it does not force centrality or rational return. A generic subfamily of the witness is provably untileable by an additional endpoint obstruction. One specified nongeneric fixture has an exact feasible one-corona witness. No plane tiling, periodic escape, or aperiodic pair is established for that fixture.

Read: `research-problem.md`, protocol §§5,19, latest `discovery-log.md`, `two-equiangular-hexagons-sol-2026-10-19.md`, and `../reviews/two-equiangular-hexagons-hostile-sol-2026-10-19.md`. The reviewed full-edge trivalence, abstract honeycomb and global three unoriented directions are dependencies. No new literature search or novelty claim. Root owns log/Git integration; this task edits neither.

## Complete native states and signed imbalance

Put u_k=(cos(kπ/3),sin(kπ/3)), with indices modulo six. For one native CCW length vector s, closure is equivalent to

    s0−s3 = s2−s5 = −(s1−s4) = δ.

All strictly positive closing vectors give strictly convex equiangular hexagons: their edges turn positively by 60° in cyclic direction order. Central symmetry is equivalent to δ=0. An arbitrary placed copy, after fixing the global six directed headings, has length in heading k

    l_(X,r,ε)(k) = s_X[(r+εk) mod 6],
    r∈{0,1,2,3,4,5}, ε∈{−1,+1}.

These twelve states include every native-side phase and reflection parity; symmetric shapes may give repeated geometric states. Reversing native cyclic traversal under reflection supplies ε=−1. For this convention the signed directional imbalance is

    l(k)−l(k+3) = (−1)^(r+k) δ_X.

There is no extra ε factor: (−1)^(εk)=(−1)^k. A different convention for the first reversed native edge could absorb a sign into r; neglecting that convention would invent a reflection-invariant positive charge. Native δ is not an intrinsic signed charge without a phase choice.

## Exact translation cocycle and minimal face equations

For each placed state f, let q_f,0=0 and q_f,k=Σ_(i<k) l_f(i)u_i. If cell f crosses side k to cell g, the native heading on g is k+3. Full-side gluing requires

    l_f(k)=l_g(k+3),
    D_fg := t_g−t_f = q_f,k − q_g,k+4.

The second endpoint equation follows from the first. Reversal gives D_gf=−D_fg. Every closed dual walk C has exact metric holonomy

    H(C)=Σ_(f→g in C) D_fg = 0.

There is no rotational holonomy left after all states are written in the same global frame. Coordinates lie in the real span of the two triangular basis vectors; the equations are linear in all native lengths.

The minimal bounded dual faces are triangles, one per primal trivalent vertex. Label one triangle f0,f1,f2 counterclockwise. At its common primal vertex the three polygon corner indices are j,j+2,j+4, in the appropriate cyclic order. Translate each tile by −q_f,its_corner. The two incident edge rays then coincide exactly when their lengths match, and all three translations telescope. Consequently the triangle holonomy equations impose **no additional scalar imbalance equation beyond its three edge matches**. This argument includes all phases and both reflection parities.

More generally, every finite closed dual walk in a simply connected dual disk is a sum of its elementary triangle boundaries; the translation holonomy is the sum of their holonomies. This is exact integrability of a prescribed consistent state field, not existence of such a state field on the infinite honeycomb, injectivity/properness of its development, or a repeatable complete strip. It cannot turn the abstract honeycomb into a periodic geometric embedding.

## Parametric exact two-noncentral triangle

Let h>0, a>0, c=h+a and 0<|b|<c. Define

    A=(c,h,c,h,c,h),       δ_A=a,
    B=(c,c,c+b,c−b,c+b,c), δ_B=b.

Both shapes are strict and noncentral, and are distinct since B has adjacent equal c sides whereas A does not. All states are as above. Use the three states B_(r=0,ε=+1), A_(0,+1), A_(1,+1), with common corner indices respectively 0,2,4. Thus their sectors have boundary ray pairs (u0,u2), (u2,u4), (u4,u0). The common ray lengths are respectively c,h,c. Their interiors lie in these three disjoint 120° sectors, so they form an actual nonoverlapping three-tile vertex patch, not merely incidence counts.

The oriented dual cycle is

    B --side5--> A0 --side1--> A1 --side3--> B.

The corresponding receiving sides are 2,4,0. The exact translations t=−q_corner satisfy each seam equation and H=0 identically in h,a,b. The signed imbalance sum for these states is b+a−a=b, which need not vanish. One may choose b/a irrational. Therefore this minimal face-cycle gate forces neither δ_X=0 nor rational imbalance ratio. This is a **local** stopping certificate only; as the next argument shows, generic members of this same locally feasible family do not tile the plane.

`hexagon-imbalance-cocycle-sol-2026-10-19.py` verifies the complete 24 native states of the two species symbolically, all three endpoint equations, and triangle holonomy identically. Its fixture h=a=b=1 is

    A=(2,1,2,1,2,1), B=(2,2,3,1,3,2).

## Additional exact endpoint obstruction for generic parameters

Assume b≠±a, in addition to the displayed strict domain. Then p=c+b and m=c−b are distinct and neither belongs to {c,h}. They occur only on B. At the B corner between sides2 and3 the incident lengths are p,m. Every tile meeting either incident ray must therefore be B, so the trivalent star there is BBB. For the star's three ray lengths, each pair that belongs to a corner must be an adjacent pair in B.

There is no adjacent (p,p) pair and no adjacent (m,m) pair in B. Since two of the rays already have lengths p,m, the third must give an allowed partner to both: neither p nor m works, and a different length cannot match the specified incident B-private ray without a B corner pairing it to that ray. More explicitly, allowed neighbors of p in the B cyclic word are {c,m}, and allowed neighbors of m are {p}; these sets have empty intersection. This excludes the star, even allowing a third ray of length c. This last check is essential: an unsupported assertion that all three rays must be private would be insufficient.

Thus **no B can occur**. If only A occurs, every corner is a mixed (c,h) pair, and the three ray lengths of a trivalent vertex would form a two-color triangle with every adjacent pair unequal. That is impossible. Hence the entire pair is **untileable** for b≠0,±a with |b|<c and h,a>0, despite the feasible AAB triangle.

At b=−a (which lies in the strict domain automatically because a<c), B has word (c,c,h,c+a,h,c). Its unique private length c+a is flanked by h at both ends. Across that private edge its B mate is also the same unique native side. At either endpoint the third corner would need two h sides, which neither A nor B has adjacently. Therefore this exceptional branch is untileable as well. This branch argument is analytic; the replay script checks only the stated triangle and fixed positive fixture, not this proof.

The only parameter branch of this displayed family not eliminated here is b=a. This is a reduction for this witness family, not a classification of two equiangular hexagons.

## Fixed one-corona gate at h=a=b=1

Parent explicitly authorized one immediate corona test after the minimal triangle, while forbidding patch growth. The complete finite domain is one fixed B=(2,2,3,1,3,2) at phase0, parity+1, and six neighbors in order across its sides0,…,5. Each neighbor ranges independently over both raw words A,B, all six r, and ε=−1,+1. Duplicate orientation states are deliberately retained. No external ring or periodic quotient is searched.

The integer triangular-basis vectors are u0=(1,0), u1=(0,1), u2=(−1,1), u3=(−1,0), u4=(0,−1), u5=(1,−1). Each state's q vertices are integral. Across central side k the neighbor shift is q_B,k−q_neighbor,k+4. Besides central edge equality, consecutive ring neighbors across sides k−1,k must obey

    l_(neighbor k−1)(k+1) = l_(neighbor k)(k+4).

The last/first condition is l_neighbor5(1)=l_neighbor0(4). Exact separating-axis tests reject every positive-area overlap between neighbor polygons; a strict collinearity test rejects any vertex in another polygon's side interior. Matching adjacent ring edges share the central corner automatically, so their endpoint equations follow. All seven polygons have disjoint interiors.

The candidate counts after the central seam are (12,12,4,8,4,12). Exactly **5,184 labeled coronas** pass all tests. This count includes duplicates from A's symmetries and is not a count up to congruence. The first retained neighbor states and shifts are:

| central side | type | r | ε | shift in (u0,u1) basis |
|---|---|---|---|---|
|0|A|1|−1|(2,−3)|
|1|A|0|−1|(3,−1)|
|2|B|3|−1|(2,2)|
|3|A|1|−1|(−2,5)|
|4|B|3|−1|(−3,2)|
|5|A|0|−1|(−2,−1)|

`hexagon-imbalance-cocycle-corona-sol-2026-10-19.py` is the exact replay; its adjacent `.json` preserves the witness and count. Full polygons are reconstructed from the raw words and twelve-state formula, so the table specifies every endpoint exactly. The gate includes every reflected state, not only the all-reflected first witness.

A-only tiling is impossible by the mixed c/h odd-cycle argument. B-only tiling is also impossible by an exact corner argument: at b=a, the three B lengths h,c,p=c+a are pairwise distinct because a>0 and c=h+a. The complete B corner list is (c,c),(c,p),(p,h),(h,p),(p,c),(c,c). Thus N_B(p)={c,h} and N_B(h)={p}, with empty intersection. A trivalent B-only star containing the mandatory (p,h) corner cannot choose its third ray length. This covers every phase/reflection since it uses the full undirected native corner list; there are no equality exceptions in h,a>0. Consequently neither one-species omission supplies an escape for this fixture. Neither the three-tile patch nor the seven-tile corona proves infinite extension, and the 5,184 count establishes no periodic return. No larger patch or torus search follows.

## Replay and stop

Run from repository root:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-imbalance-cocycle-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-imbalance-cocycle-corona-sol-2026-10-19.py

The first uses exact SymPy expressions; the second uses integers and a finite exhaustive search. No numerical grid, enlarged torus, or inference of period from honeycomb topology was used. Local cocycle feasibility falsifies the simple proposed invariant; endpoint compatibility independently excludes the generic local-witness family. The specified b=a fixture stops after its feasible immediate corona. A new exact global extension/return or periodic-carrier mechanism is required to continue it. The unrestricted objective and general two-noncentral-hexagon implication remain unresolved.
