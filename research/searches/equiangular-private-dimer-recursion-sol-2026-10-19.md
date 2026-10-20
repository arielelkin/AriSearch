# Private-edge dimers: one exact equiangular hierarchy design cycle

2026-10-19. **STOP: forced first grouping, no exact recursive boundary rule.** Internally checked; independent hostile review pending. The specified shapes are valid noncentral convex hexagons and cannot tile monohedrally. In any mixed tiling their private sides force same-species dimers, with two physical seam identifications each. No infinite legal honeycomb assignment, periodic escape, hierarchy, or aperiodic forcing theorem has been obtained. This is an unresolved seed and a stopped mechanism, not a construction meeting the problem.

## Correct exact shapes and the discarded invalid preliminary word

The initial message proposing A=(5,2,3,4,4,3) was wrong: its three opposite differences are (1,0,2), so that word cannot close at 120° angles. Root caught this before the dimer gate. It is discarded and never used as a polygon below. The replay explicitly rejects it.

The **corrected** exact words are

    A=(5,3,3,4,4,2),  B=(1,3,3,2,2,4).

More generally, for m>2d>0 take

    A=(m+2d,m,m,m+d,m+d,m−d),
    B=(m−2d,m,m,m−d,m−d,m+d).

Every length is strictly positive. The closure differences s0−s3=s2−s5=s4−s1 are respectively +d for A and −d for B. Thus both close and neither is central. Their five numerical labels m−2d,m−d,m,m+d,m+2d are pairwise distinct. Each member has four distinct labels with multiplicities (2,2,1,1), and they cannot be congruent because their side-length multisets differ. The fixture is m=3,d=1. It is also useful that B_i=2m−A_i componentwise; this is an exact arithmetic identity, not a geometric placement rule.

Let u_k=(cos(kπ/3),sin(kπ/3)); define q0=0 and q_(k+1)=q_k+s_k u_k. This gives exact coordinates over Q(sqrt3) for the fixture. Ordered edge headings and positive closure imply strict convexity. One direct check: for each edge, cross products of its direction with the vectors to the nonadjacent vertices at cyclic offsets2,3,4,5 are positive multiples of s_(i+1), s_(i+1)+s_(i+2), the same sum, and s_(i−1), respectively, using closure for the latter two. Thus every nonincident vertex lies strictly inside its support half-plane.

The valid A is the reversal of root's alternative correction (5,2,4,4,3,3); these are the same congruence class under permitted reflections. All actual computations below use only the two displayed corrected raw words.

## Specified attempted mechanism

The intended invariant was **recursive private-edge pairing**: a length appearing exactly once in a species and absent from the other forces a perfect matching of tiles of that species; regard each pair as a supertile and repeat with an intrinsically distinguishable supertile boundary word. An infinite uniquely recognizable sequence of such groupings might supply a hierarchy, but only if a second grouping and all later boundary recursions are actually proved.

Use the reviewed full-edge trivalence and honeycomb development results as dependencies: `../lemmas/equiangular-hexagon-honeycomb-development-2026-10-19.md` and its hostile review, together with the structural review `../reviews/two-equiangular-hexagons-hostile-sol-2026-10-19.md`. An actual infinite legal honeycomb assignment of these states would develop to a plane tiling. These results produce no such assignment and do not impose a hierarchy.

All phases and reflections are allowed. In global heading k the side length is s[(r+εk) mod6], for r=0,…,5 and ε=−1,+1. Both shapes have twelve distinct such states: the unique private side fixes its native slot, and its two neighboring lengths differ, excluding a reflection fixing that slot. No orientation, chirality, or species-use condition is imposed externally.

In the fixture, A length5 occurs once and is absent from B; B length1 occurs once and is absent from A. Therefore any actual tiling pairs each A across its5 edge to a unique A, and each B across its1 edge to a unique B. The disjoint same-species pairs cover all tiles. This is a genuine intrinsic first grouping, conditional on a tiling existing.

## Exact dimer boundary words and both physical seam pairings

Fix either polygon with private side0 along [(0,0),(p,0)] and interior above it. There are exactly two possible mates using that unique native side and lying below the common segment:

    half-turn: q -> (p,0)−q,
    reflection: (x,y) -> (x,−y).

Both whole dimers have disjoint component interiors because their components lie in opposite closed half-planes of the shared supporting line. They are distinct physical placements. Let W=(s1,s2,s3,s4,s5). Traversing the outer boundary with both component interiors on the left gives W W for the half-turn mate and W reverse(W) for the reflected mate. At the two common-edge endpoints the union has angle240°; its eight other vertices have angle120°. The ten listed boundary sides are actual sides, and no straight angle is silently suppressed.

For A, U=(3,3,4,4,2); for B, V=(3,3,2,2,4). The exact cyclic ten-edge words, with a separator indicating the second component chain, are:

| dimer | half-turn boundary | reflected boundary |
|---|---|---|
|AA|3 3 4 4 2 / 3 3 4 4 2|3 3 4 4 2 / 2 4 4 3 3|
|BB|3 3 2 2 4 / 3 3 2 2 4|3 3 2 2 4 / 4 2 2 3 3|

These exact words are also represented in the adjacent SVG. Rendering coordinates there use decimal sqrt3 only for illustration; the proof and replay use integer triangular-basis coordinates.

Every seam endpoint must be completed by a third 120° corner. With left/right native neighboring lengths s5,s1, the half-turn requires the mixed pair (s5,s1) at both endpoints, while the reflection requires (s5,s5) and (s1,s1). The full fixture table is:

| seam | required third-corner pairs | species possessing those corners |
|---|---|---|
|AA half-turn|(2,3),(2,3)|B,B|
|AA reflection|(2,2),(3,3)|B, either|
|BB half-turn|(3,4),(3,4)|A,A|
|BB reflection|(4,4),(3,3)|A, either|

This checks native incidence, not just numerical angle sums. The complete native corner lists are

    A: (2,5),(5,3),(3,3),(3,4),(4,4),(4,2),
    B: (4,1),(1,3),(3,3),(3,2),(2,2),(2,4).

Thus **both mate placements pass every individual endpoint corner test** in the mixed pair. For any chosen endpoint, the two dimer components occupy two disjoint120° corner cones and the third polygon is contained in the complementary120° cone, so that endpoint test has an actual nonoverlapping three-tile realization. This does not claim simultaneous completion of both endpoints, a corona, or an infinite extension for either seam option.

The same argument works throughout m>2d>0 after replacing fixture labels2,3,4 by x=m−d,y=m,z=m+d. It handles all phase/reflection states because corner pairs are unordered and the private side is unique.

## Monohedral and prior periodic-escape gates

Neither species tiles alone, without any external monohedral-classification citation. In an A-only tiling, its unique5 side must meet an A5 side. The half-turn needs a (2,3) corner, absent from A; the reflection needs a (2,2) corner, absent from A. Both possible relative placements fail. In a B-only tiling, the half-turn across1 needs a (3,4) corner, absent from B; the reflection needs a (4,4) corner, absent from B. Thus both omissions are impossible. This is a pointwise obstruction and includes every rotated/reflected mate and unrestricted contacts through the reviewed edge-forcing reduction.

The pair does **not** satisfy the hypotheses of the reviewed six-distinct/four-distinct theorem (`hexagon-six-four-double-pair-periodicity-2026-10-15.md`): neither member has six distinct lengths. It also does not satisfy the five-distinct/four-distinct synthesis (`hexagon-five-four-all-words-periodicity-synthesis-sol-2026-10-19.md`): neither member has five distinct lengths. Numerical labels and dihedral native changes cannot alter those multiplicities. The earlier binary theorem and three-length seed do not cover these four/four words.

I also tested exact membership in the whole reviewed four-parameter periodic cone `hexagon-adjacent-repeat-periodic-cone.md`, whose native patterns are

    X=(p,a,q,b,c,d), Y=(r,c,s,b,a,d),
    b=p+a−c, d=q+a−c, r=p+2(a−c), s=q+2(a−c).

The finite domain is the twelve dihedral states of each corrected word in both species orders, exactly288 ordered comparisons. None matches. This is an exact existing-family membership check, not a periodic-quotient search. It holds throughout the parametric family: represent each length m+kd by its integer coefficient k. Each cone formula has coefficient1 on m, so the comparisons reduce to the same integer offset words (2,0,0,1,1,−1) and (−2,0,0,−1,−1,1). No new theorem that arbitrary four/four pairs escape periodically is inferred.

Root independently authorized another agent's tiny periodic-carrier falsification. That separate record, `hexagon-corrected-private-periodic-small-sol-2026-10-19.{py,json}`, reports UNSAT over33 HNF quotients with at most six faces and all24 states. I did not run or independently review it in this design cycle. Its bounded absence of a carrier supplies neither plane untileability nor aperiodicity. No quotient enlargement follows here.

## Exact missing recursion and stop

Private lengths5 and1 disappear entirely from their dimer outer boundaries. Both supertile species have only common lengths2,3,4 on their boundaries, with two different possible seam geometries each. Therefore the **same unique-private-native-edge rule cannot simply be reapplied at the next scale**. A more elaborate boundary-word recognition theorem could conceivably distinguish composite boundary chains, but none was found. Passing both endpoint tests does not prove both choices globally extend, and their local ambiguity alone does not disprove a more subtle hierarchy.

The exact absent object is an explicit boundary substitution on these dimer states, with complete incidence maps, exact matching expanded boundary words, infinite extension, and a proof that every admitted assignment has the resulting recognizable successive grouping (or an independently proved periodic escape). No such substitution, return invariant, or global uniqueness proof exists in this cycle. No claim is made that the corrected seed survives every local or periodic gate.

Stop this one design cycle here under protocol§5. Do not enlarge patches or quotients. The seed's infinite mixed tileability and possible periodic escape remain unknown, as does the original unrestricted objective.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/equiangular-private-dimer-recursion-sol-2026-10-19.py

The standard-library script verifies raw exact vector closure (including rejection of the invalid preliminary A), all24 dihedral states, species distinction, the two boundary words per species, both endpoint pairings and monohedral exclusions, and all288 prior-cone comparisons. No solver, numerical grid, patch growth, or periodic search occurs. Files: this report, the adjacent `.py`, and the illustrative `.svg`. No discovery-log or Git edit.
