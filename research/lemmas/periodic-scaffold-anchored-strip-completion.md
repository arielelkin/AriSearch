# Periodic completion of uniformly bounded anchored strips

Date:2026-10-13. Status: conditional lemma, independently hostile-reviewed VALID; [review](../reviews/periodic-scaffold-anchored-strip-hostile-review.md). This is a periodic-completion mechanism, not an unrestricted tile theorem.

## Precise hypotheses

Fix a nonzero vector v, finite compact genuine convex polygon sets S and T, and a locally finite interior-disjoint scaffold Q of isometric S copies invariant under v. Assume a plane completion by isometric T copies exists, and each completion tile has a whole native side in common with a whole native side of some scaffold tile. Suppose the open complement of the closed scaffold support has a v-equivariant decomposition into connected components of these two kinds:

1. Components individually invariant under v and each contained in a strip of width W parallel to v, with the same fixed W for all such components.
2. Components whose v-translates are pairwise distinct; each admits a finite T-tile completion. Different translates of any such component have disjoint interiors.

Every completion tile interior belongs to a single open complement component. This follows automatically because it is connected and interior-disjoint from the scaffold. The stated kinds of component cover the entire complement; no assumption that arbitrary periodic scaffolds have this component classification is made.

Then there is a completion invariant under Mv for some positive integer M. The integer M has a finite bound depending only on the finite prototiles, |v| and W, not on the particular strips or their number. The original completion need not be periodic.

## Finite anchored placements in a strip

Put D=maximal diameter among S and T, and a=minimum area of an S tile. Choose axes along v and perpendicular to it. For an invariant strip component C, restrict attention to placements fully compatible with the scaffold and whose interiors lie in C. A whole-side matching fixes a T placement by choosing one of finitely many S sides, one T side of equal length, and one of two endpoint identifications on the unoccupied side. Thus each S tile gives at most2s_S s_T |T| placements, with s_S,s_T the maximal respective native side counts. Symmetries or duplicate placements only reduce this number.

Assign each possible T placement to an integer slab by flooring the longitudinal coordinate of its centroid divided by |v|. A candidate anchored in slab0must meet an S tile lying in a rectangle of bounded width W+4D and longitudinal length |v|+4D, up to translating the rectangle with C. Each such S tile lies entirely in a further D enlargement. Since scaffold tile interiors are disjoint and each has area at least a, their number is uniformly bounded by the area of that enlargement divided by a. Hence the number N of candidate placements assigned to any one slab is bounded by an integer constant N0 independent of C. Because C and Q are v-invariant, translation by v bijects the candidates of slab n and n+1.

Local finiteness also makes every union of scaffold supports closed. Different side matches producing the same placement can be deduplicated. No finite orientation assumption is imported; whole-side anchoring derives finitely many placements in each slab even if scaffold orientations vary from strip to strip.

## Finite-state completion on one invariant strip

Encode a candidate selection in slab n by a subset of its N labeled placements. The alphabet has at most2^N0symbols. Take an integer K>=1 large enough, depending only on D/|v|, that every candidate tile meeting slab n has its reference point in slabs n-K,...,n+K. Interior-disjointness and coverage of C in slab n are predicates of this finite selection window. Both concern finitely many polygons intersecting a bounded rectangle, and are invariant under translating the window by v. Coverage includes component boundary points only insofar as they belong to the closures of the selected T tiles; interior coverage is the essential predicate, with closure handled globally below. These local predicates define a one-dimensional shift of finite type.

The actual completion supplies a bi-infinite legal sequence, so the finite directed graph whose states are allowable length2Kwords has a directed cycle. Repeating that cycle gives a legal periodic selection. Its period is at most the number of graph states, at most

    B=(2^N0)^(2K).

The periodic selection has interior-disjoint polygons and covers C. Candidate tiles respect the scaffold and lie in C apart from boundaries, so this is a valid replacement completion on C.

## Common period and moving component orbits

For each invariant component choose one cycle completion, of period p_C<=B. Let M=lcm(1,...,B). Every such completion is invariant under Mv, even if there are infinitely many strips and their candidate alphabets differ.

For each orbit of moving components choose one representative, retain any finite completion there, and translate it by nv to every component in that orbit. The hypotheses make these components distinct with disjoint interiors, so choices do not conflict. This part is invariant under v, hence under Mv. Choices may be made component by component; no unique decoder is needed.

The scaffold and replacement completions cover the entire plane: all complement interiors are covered, and finite positive-area bounded prototiles give local finiteness of the replacement family by the same area-packing estimate. Its support union is therefore closed. Since scaffold together with all complement interiors is dense in the plane, closure covers every boundary point as well. Distinct components have disjoint interiors, so cross-component overlaps cannot occur. This proves the claimed nonzero period.

## Dependencies and exact remaining application gates

Only finite side matching, area packing, one-dimensional finite-state cycle extraction and local finiteness are used. The theorem does not assert that every singly periodic polygon tiling can be made doubly periodic. It derives one periodic completion of an explicitly periodic scaffold with the stated component geometry and anchoring.

For the one-right pentagon/equiangular octagon route, native reduction supplies whole P-Q anchoring. Two distinct private Q side lengths may give half-turn QQchains and a common scaffold period. Those facts, disjoint proper chain paths, a uniform strip width and the component-orbit classification must be proved separately before using this lemma. An arbitrary periodic scaffold can have components outside these hypotheses. No conclusion about arbitrary two convex polygons follows.
