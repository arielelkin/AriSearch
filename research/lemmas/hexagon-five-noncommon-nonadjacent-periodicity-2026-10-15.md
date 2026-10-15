# Five-length hexagons with nonadjacent repeats and unequal length palettes

Date:2026-10-15. Status: independently hostile-reviewed VALID with exact finite certificates; [fresh review](../reviews/hexagon-five-noncommon-hostile-2026-10-15.md). This is a restricted periodic-escape theorem, not unrestricted impossibility.

## Theorem

Let A and B be genuine convex hexagons, each having exactly five distinct NUMERICAL side lengths, so one length is doubled in each shape. Suppose each doubled pair is nonadjacent (cyclic separation2 or3), and the sets of five numerical lengths used by A and B are different. If the shapes tile the Euclidean plane with arbitrary isometries, reflections and partial-edge contacts permitted, then the same shapes admit a doubly periodic tiling.

Different symbols throughout this statement denote different numerical lengths. This artifact does NOT claim the stronger formal-color version with collisions between symbol values. Its private-repeat branch invokes a theorem whose hypotheses require six distinct numerical lengths.

Together with the reviewed common-five-palette separation2/2,2/3,3/3 results, this closes all exactly-five-length pairs with nonadjacent repeated slots, regardless of the size of their shared palette. The common-palette results remain separate dependencies, not part of the new finite domain below. Adjacent repeats and fewer than five numerical lengths in a member remain outside.

## 1. Defect-free source and pure-star escapes

Use the reviewed [defect-free limit theorem](hexagon-limit-and-periodicity.md) to obtain a full-side everywhere-trivalent source tiling. A native corner i is between side slots i and i+1, modulo6. The two possible normalized A words are

    A2=(0,1,0,2,3,4), A3=(0,1,2,0,3,4).

All adjacent side colors differ. At a trivalent vertex the three ray lengths are pairwise distinct, so its three native corner pairs are the edges of a triangle on three length symbols. In particular a native corner cannot occur twice in the same star.

For separation2 the single-shape corner graph has a doubled edge and a four-cycle, but no triangle. Thus no pure star exists. For separation3 it has exactly two triangles, on native corners{0,1,2} and{3,4,5}. If either occurs, its three actual angles sum2pi and the other triple also sums2pi, since the hexagon angle sum is4pi. The explicit two-face monohedral flat torus in [the opposite-repeat theorem](hexagon-both-opposite-repeat-periodicity-2026-10-15.md) supplies a periodic escape using just this shape. Concretely, in each of two oriented copies pair side0 to side3 within that face, and pair each other side to the same side of the other face. This gives four circular triple links, two of each angle triple.

Hence assume no actual star is pure. Both species then occur, including in cases where the original unrestricted tiling may have omitted one. Every one of the twelve native corners occurs in a mixed star. Removing all pure stars from the necessary atlas is therefore justified in this branch.

## 2. Complete unequal-palette finite domain

Normalize A as A2 or A3. Let k in{0,1,2,3,4} be the number of B lengths shared with A. Choose its shared subset from{0,1,2,3,4}; name its5-k private lengths5,6,...,9-k. Independent naming of these private lengths loses no numerical family. For each palette take all120 permutations(p,q,r,s,t), and use either

    B2=(p,q,p,r,s,t), B3=(p,q,r,p,s,t).

Choosing the repeated side as position0, then reading the boundary in either direction, puts every nonadjacent-repeat B into this domain. No quotient is used in its initial enumeration. For each of four separation pairs there are

    120*sum_(k=0)^4 binomial(5,k)=3720

raw words, hence14880 total. The initial corners have distinct adjacent colors in every case.

For each word pair form all triples of distinct native corners whose unordered incident-color pairs are exactly a color triangle. Delete pure triples. For every ray of every remaining star, identify the actual side slots at that ray and the OTHER native endpoint of each side. If their far-end corner pair belongs to no remaining star, delete the original star. Repeat to a fixed point. Every actually occurring star survives inductively, because its physical full side has an actual far endpoint. This is a necessary test, not an assertion that every surviving support extends to a plane tiling.

Construct the graph on the twelve native side slots with an edge for every seam type in the fixed atlas. The actual seam graph is a subgraph. If the two repeated slots of either shape are disconnected in this upper graph, they are disconnected in the actual graph. Recolor actual connected components: that shape has six distinct formal colors, while the other has at least five. The reviewed [six/five formal-color escape theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md) gives a doubly periodic unmarked tiling. Recoloring is a proof device for the existing source, not a restriction on final admissible tilings.

## 3. Exact census and six remaining native word classes

The [integer producer](../searches/hexagon-five-noncommon-gate-2026-10-15.py) and [certificate](../certificates/hexagon-five-noncommon-gate-2026-10-15.json) give these counts. Entries are(no corner cover, six-color escape, residual).

| A/B separations | k=0 | k=1 | k=2 | k=3 | k=4 |
|---|---|---|---|---|---|
|2/2|(120,0,0)|(600,0,0)|(1200,0,0)|(1198,0,2)|(566,28,6)|
|2/3|(120,0,0)|(600,0,0)|(1200,0,0)|(1200,0,0)|(560,40,0)|
|3/2|(120,0,0)|(600,0,0)|(1200,0,0)|(1200,0,0)|(560,40,0)|
|3/3|(120,0,0)|(600,0,0)|(1200,0,0)|(1168,32,0)|(512,76,12)|

There are exactly20 residual raw words. All have explicit global color bijections and independent dihedral native readings taking them into the following six classes. The certificate retains each map pointwise on both side words; no change of physical length equality is made.

|A|Canonical B|Raw words|Fixed stars|Closed covering supports|
|---|---|---:|---:|---:|
|A2|(0,3,0,5,1,6)|2|8|3|
|A2|(0,3,0,2,1,5)|4|10|7|
|A2|(5,3,5,2,1,4)|2|8|9|
|A3|(5,1,2,5,3,4)|4|4|1|
|A3|(5,1,2,5,4,3)|4|4|1|
|A3|(5,1,3,5,2,4)|4|4|1|

A native side reading i -> shift+direction*i induces corner reading i -> shift+i for direction+1 and i -> shift-i-1 for direction-1. Thus the retained side-word equivalences also transfer native angle/star data correctly; reflections are explicitly included.

For every representative exhaust all subsets of its fixed atlas. Retain exactly those covering all twelve corners and internally satisfying all three far-end demands for every included star. The ACTUALLY OCCURRING star set equals one of these supports. This is stronger than asserting it contains a minimal support. The six representatives have22 supports in total; counted over all20 raw words there are64. No geometric realization of an arbitrary support is assumed.

## 4. Three classes have intrinsic geometric determinism

For the first two A3 representatives the only support is

    {(0,2,7),(1,6,8),(3,5,10),(4,9,11)}.

For the third it is

    {(0,3,7),(1,6,9),(2,5,10),(4,8,11)}.

Each partitions all twelve corners. A host endpoint therefore has one unique star. Its chosen side color selects one unique guest corner and guest side, because the ray colors at that star are distinct. In the actual source the choice at the other endpoint must agree with that guest. The ordered endpoints of its full side, with its interior on the opposite half-plane, fix the complete relative plane isometry. All native sides consequently have deterministic indexed neighbors.

Any map between two occurrences with the same finite intrinsic frame propagates through the connected full-side adjacency graph. It preserves the whole tiling. This gives a discrete cocompact plane-isometry group; the reviewed intrinsic-state argument yields a rank-two translation subgroup. This is the same four-star frame mechanism used in [the common-palette opposite-repeat proof](hexagon-both-opposite-repeat-periodicity-2026-10-15.md), with its neighbor-uniqueness hypotheses verified here. Physical symmetries and reflected copies do not create additional unrecorded endpoint choices.

## 5. The old private-repeat class satisfies its numerical hypotheses exactly

The representative

    A2=(0,1,0,2,3,4), B=(5,3,5,2,1,4)

has six pairwise distinct numerical length values, by the original palette normalization. Both doubled lengths are private, with four shared singleton values. It is exactly [the independently reviewed private-repeat theorem](hexagon-five-length-private-repeat-periodicity.md), which gives a doubly periodic escape. No noninjective formal-color extension of that theorem is used or claimed.

## 6. Both genuinely new classes have four-face periodic witnesses

For the remaining two representatives take faces A0,A1,B0,B1. Fix the orientation of A0; allow all8 choices of the other three orientation signs. For each sign assignment enumerate all within-color perfect matchings of the24 sides, always reversing boundary endpoints in the oriented face cycles.

For B=(0,3,0,5,1,6), color-group sizes are8,4,4,2,2,2,2. This gives exactly

    8*105*3^2=7560

pairings. There are7488 connected gluings, four trivalent flat-torus combinatorial candidates, and two distinct native angle supports.

For B=(0,3,0,2,1,5), sizes are8,4,4,4,2,2. This gives exactly

    8*105*3^3=22680

pairings. There are22608 connected gluings, six trivalent torus candidates, and three distinct native angle supports. These are fixed positive-witness domains; their completeness as a search for all periodic tilings is neither asserted nor needed.

Each retained gluing pairs every full side exactly once with an equal-length side, is connected and orientable, and has eight circular three-corner links. It has V=8,E=12,F=4. When the eight actual angle sums equal2pi the quotient is a compact nonsingular flat torus. Its complete universal cover develops isometrically onto the Euclidean plane, yielding a tiling by the original entire polygons with two independent deck translations. No similarity, altered metric, or embedded source appearance of the torus patch is assumed.

The [four-face certificate](../certificates/hexagon-five-noncommon-fourface-2026-10-15.json) retains all five chosen angle-support representatives, their actual edge pairings and orientation signs, and a positive witness for EVERY one of the3+7 source supports. In units of pi, source rows are A's total4, B's total4, and one triple-sum2 for each source star. Every required target row is supplied as an exact Fraction linear combination of these augmented source rows. There are12+28=40 retained identities. Consequently all required torus angle sums hold for the actual given metrics. No numerical angle solve, polygon-closure solve, or bounded negative search enters this implication.

For clarity, the first new class has precisely the supports

    S0={(0,10,11),(1,8,9),(2,3,7),(4,5,6)},
    S1={(0,8,9),(1,10,11),(2,3,6),(4,5,7)},
    S0 union S1.

Both S0 and S1 are explicit positive four-face torus angle supports, so their union immediately inherits a witness. The second new class has support sizes4,4,4,6,8,8,10; every one is positively covered by its retained exact row identities.

Every branch of the complete unequal-palette domain has now supplied either a contradiction to existence of the assumed source or an admitted periodic escape. This proves the theorem. The complete finite computation and all proof bridges passed fresh independent review. QED.

## Replay and review obligations

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-noncommon-gate-2026-10-15.py --output research/certificates/hexagon-five-noncommon-gate-2026-10-15.json
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-noncommon-fourface-2026-10-15.py --output research/certificates/hexagon-five-noncommon-fourface-2026-10-15.json

Both commands completed. The [independent no-import verifier](../reviews/hexagon-five-noncommon-independent-2026-10-15.py)
regenerates the14880-word domain, native far-end pruning, actual seam-component criterion,20 word equivalences,22 representative supports, five positive torus gluings and40 augmented-row identities. The fresh whole-proof review also checked the pure-star omission branch and the precise numerical hypotheses of the inherited private-repeat theorem. Every check passed. An independent verifier need not exhaust the30240 possible four-face pairings: verifying the retained positive witnesses and every source-support implication suffices.

No main-problem resolution or novelty claim is made. The method does not classify adjacent repeats, four-length hexagons, or any pentagon-containing pair.
