# All-obtuse pentagon–higher-polygon pairs with internally distinct lengths

**Status:** adversarially reviewed; [fresh whole-claim hostile review](../reviews/distinct-length-obtuse-pentagon-higher-review.md) valid. Restricted-family impossibility theorem; the original problem remains unresolved.

## Theorem

Let P be a genuine compact convex pentagon and Q a genuine compact convex n-gon, n>=7. Suppose every interior angle of both polygons is strictly between pi/2 and pi, and the side lengths within each polygon are pairwise distinct. If the pair tiles the plane by unrestricted isometries and contacts, then n=7 and the pair admits a doubly periodic tiling. Thus no pair in this restricted family is aperiodic. For n>=8 no tiling exists.

The metric hypotheses are per-polygon: P and Q may share numerical side lengths. No angle rationality, equilateral sides, orientation restriction, or edge-to-edge rule is imposed on the original tiling. Only [the all-obtuse forcing theorem](obtuse-edge-forcing.md) is imported; no monohedral polygon classification is used.

## 1. The finite side-cycle domain

The all-obtuse theorem forces every admitted tiling to be edge-to-edge and trivalent. Assign each distinct numerical side length a symbol. The symbols around P form a simple C5 and those around Q a simple Cn. Their union is the length graph. At a trivalent tiling vertex the three rays have distinct symbols, because any repeated pair would be adjacent equal-length sides within one polygon. Thus the three incident corners give a triangle in the length graph. Neither type can supply all three corners: neither simple cycle contains a triangle. Both types occur (monohedral tilings cannot have such vertices), and all actual corner occurrences of both types must occur in angle-legal triangles.

If a symbol is private to one cycle, its two neighbours in that cycle must be shared symbols, and the shortcut between them must be an edge of the other cycle. Private symbols are therefore isolated. Let k be the number of common symbols. Then k<=5, 5-k<=floor(5/2), and n-k<=floor(n/2). Hence k>=max(3,ceil(n/2)), and n<=10. This is an analytic bound for arbitrary n, not a computational cutoff.

Normalize P's side cycle to (0,1,2,3,4). Enumerate all choices of its k common symbols; all cyclic orders of these symbols around Q; and all placements of its n-k isolated private symbols. Private labels are renamed in order of first occurrence, and Q's cyclic rotation and reversal are quotiented. The exact finite domains and triangle-covered survivors are:

| n | k | domain | survivors |
|---|---|---|---|
|7|4|60|5|
|7|5|120|10|
|8|4|15|0|
|8|5|120|5|
|9|5|60|0|
|10|5|12|1|

Up to the dihedral relabelings of the P cycle the survivors have exactly these representatives:

| n,k | Q side word | graph triangles |
|---|---|---|
|7,4|(0,2,5,3,6,4,7)|012,235,346,047|
|7,5|(0,1,4,5,3,6,2)|012,014,236,345|
|7,5|(0,2,4,5,3,1,6)|012,016,024,123,234,345|
|8,5|(0,2,5,1,3,6,4,7)|012,123,125,346,047|
|10,5|(0,5,1,6,2,7,3,8,4,9)|015,126,237,348,049|

A string xyz denotes an unordered graph triangle. An edge xy denotes a corner, rather than adjacency between tile types. If xy is an edge in both cycles, its P-corner a_xy and Q-corner b_xy remain distinct.

The [complete search](../searches/distinct_pentagon_higher_length_graph.py), [certificate](../certificates/distinct_pentagon_higher_length_graph.json), and [independent verifier](../reviews/verify_distinct_pentagon_higher.py) retain and check the domain. The verifier additionally visits all normalized common/private interleavings, including adjacent private symbols, and checks they produce no omitted triangle-covered survivor. It checks corner-typed star supports, angle-sum linear consequences, and actual torus endpoint maps.

## 2. Excluding the higher cases

There are no graph survivors for n=9 or for (n,k)=(8,4).

In the n=8 survivor all corners have unique type assignments. Every one of its five triangles is forced by a corner occurring in no other triangle: a_01 forces 012; a_23 forces 123; b_25 forces 125; a_34 forces 346; a_04 forces 047. Sum their five legal angle equations. All thirteen actual corners occur once, except a_12 which occurs three times. Therefore

    10pi = (3pi + 6pi) + 2 a_12,

so a_12=pi/2, contradicting the strict obtuse hypothesis.

In the n=10 survivor each of its five triangles is forced and the triangles partition all fifteen actual corners. Their summed angle equations would give 10pi. But the polygon angle sums total 3pi+8pi=11pi. This contradiction excludes n=10.

## 3. Selecting a four-triangle ring for n=7

A four-triangle ring means four shared symbols forming a cycle R, with one edge of R subdivided by a P-private symbol and its other three edges subdivided by Q-private symbols. Each edge is direct in the other polygon. The four triangles partition the twelve actual corners. This is a formal label selection: a numerical side length shared by both original polygons may be renamed separately by type, selecting only particular legal contacts for the new periodic witness.

For k=4 the representative is already such a ring. Each actual corner belongs to only one triangle, so all four triangles are legal in the existing tiling.

For k=5 with Q=(0,1,4,5,3,6,2), the only duplicated corner edge is 01. Triangles 236 and 345 have unique assignments and are forced. Both 012 and 014 occur, respectively forced by a_12 and a_04. Each may use a_01 or b_01. Both actual corners occur somewhere. The two nonempty availability subsets therefore admit a matching choosing a_01 once and b_01 once. If 012 uses a_01, split numerical symbol 1 into a P-private and a Q-private label; if it uses b_01, split symbol 0. The resulting four selected triangles form the desired ring and are all legal.

For k=5 with Q=(0,2,4,5,3,1,6), the triangles 016 and 345 are forced by the private symbols. Triangle 024 is forced by a_04, and 123 by b_13. Split symbol 2 into type-specific private labels. The four forced triangles 016,024,123,345 become precisely a ring. Extra legal triangles in the original tiling are irrelevant to the selected witness.

## 4. Full-side flat torus and periodic plane tiling

Fix P's orientation and reflect Q if necessary so that its common symbols have reverse cyclic order around R. Give successive vertices x of R alternating bits h(x)=0,1,0,1. Take two counterclockwise copies P0,P1,Q0,Q1 of these oriented shapes, and pair whole equal sides with reversed boundary endpoint order:

* the P-private side between P0 and P1 in the same slot;
* every Q-private side between Q0 and Q1 in the same slot;
* for each common x, the x side of Pi with that of Q_(i xor h(x)), i=0,1.

There are twelve paired edges from twenty-four side occurrences. The quotient is connected and orientable. At a private symbol p inserted between common x,y, crossing the private seam identifies corner (p,x) of copy i with corner (p,y) of the other copy. The common seams lead to the same opposite-type face because h(x)!=h(y). Opposite common boundary order joins these two corners to its (x,y) corner. Each quotient vertex therefore has exactly the three corners of the appropriate ring triangle; its circular link has three sectors. Every ring triangle appears twice, yielding eight vertices. The Euler characteristic is 8-12+4=0, so the quotient is a torus.

All side identifications are metric isometries, and the selected four triangle equations make every cone angle 2pi. Thus the torus is a nonsingular compact flat Euclidean surface. Its complete simply connected universal cover develops isometrically to the Euclidean plane. The lifted whole polygons cover that plane with disjoint interiors. Deck transformations form a rank-two discrete orientation-preserving isometry group acting freely; a nontrivial rotation has a fixed point, so they are translations. The two generators are independent by discreteness and rank. The resulting tiling is doubly periodic, using two copies of each original shape in a torus quotient.

The independent verifier checks all endpoint identifications directly. This global metric construction proves extension; no finite-patch or angle-frequency feasibility is mistaken for existence.

## Scope, review, and restart

All n>=7 are covered under the two metric restrictions. The theorem leaves open all pentagon-containing pairs with a nonobtuse angle or repeated side length, and arbitrary two-hexagon pairs with repeated lengths. It supplies a periodic tiling from an assumed tiling; it does not supply a new aperiodic pair or prove unrestricted impossibility.

The angle and graph selection are newly recorded here; flat-torus development is classical. No priority claim is made. The fresh independent hostile audit validates this lemma; no primary source matching the exact mixed-pair statement is asserted or universal priority claimed. [The search record](../searches/distinct-pentagon-higher-length-graph.md) states commands, exact completion status, environment, and finite domains.
