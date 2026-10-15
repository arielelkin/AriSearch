# Fresh hostile review: adjacent-repeat six/five-length hexagons

Date: 2026-10-15. Verdict: **VALID** for the complete written theorem in
`research/lemmas/hexagon-six-five-adjacent-periodicity-2026-10-15.md`.
The reviewer is independent of the proof author and producer. The full
artifact, producer and retained certificate were read. No substantive
mathematical defect found and no author proof repair was required in this
review. Earlier producer revisions are not substituted for the final claim.

## Exact claim and dependencies

If A is a genuine convex hexagon with six distinct side lengths and B is a
genuine convex hexagon with five distinct side lengths whose repeated pair
is adjacent, then any unrestricted plane tilability of the pair implies
existence of a doubly periodic tiling with two A and two B faces in a flat-
torus quotient. Reflections and partial contacts are permitted initially.
The theorem and its union corollary with the reviewed separation-two,
opposite-repeat and six/six-distinct results are valid within their stated
hexagon hypotheses. This does not resolve the arbitrary two-convex-polygon
problem and does not establish novelty.

The reviewed defect-free limit theorem is an explicit imported dependency.
The new finite work is audited independently below. The compact flat-torus
metric argument is also audited, using the reviewed earlier construction.

## Repeated rays and actual-corner coverage

The author correctly does not reuse the distinct-ray claim. For B=(p,p,q,r,s,t),
its corner graph has a loop p-p and a five-cycle. Pure-B stars may indeed
have repeated rays; the blanket assertion that B has no stars would be
false. The author's q-r obstruction is valid: q has B-neighbors p,r and
r has B-neighbors q,s, with no common neighbor and no loops at q or r.
Thus this actual corner cannot occur in a B-only trivalent tiling. A-only
is excluded by its triangle-free simple six-cycle. Both types occur in the
defect-free limit, and all twelve actual corners must occur.

The private-A argument is valid as written. A-private u differs from p.
Of its distinct cycle neighbors v,w at least one v differs from p. The
corner u-v cannot use a repeated-ray star, whose edges besides the p-p loop
are all p-x. A distinct-ray triangle therefore requires shortcut v-w,
which cannot be an A edge and must be a B edge. Both neighbors are shared.
Three isolated private A lengths would force a three-distinct-length
triangle in B's five-cycle-plus-loop graph, impossible. No repeated-ray
case is omitted by choosing the u-v corner in this way.

## Independent stdlib reconstruction

The retained checker imports no producer code. It visits all 3780 words
B=(p,p,q,r,s,t), q<t, over every shared-label set and all private-label role
assignments, including k<4 rather than assuming the private-A proof. It
recovers exactly 42 surviving words for k=4 and 90 for k=5, in 4+8 dihedral
orbits, with no other survivors.

Its star atlas uses a different encoding from the producer: enumerate all
364 multisets of three actual corner indices, regard their native arm
pairs as three multigraph edges on numerical lengths, and require a
connected even-degree multigraph. Euler's circuit criterion is exactly
existence of a cyclic assignment of those three corner edges to three
rays. This includes loops, two equal rays, three equal rays, and repeated
actual corner indices representing distinct tile copies. It reconstructs
every producer atlas exactly.

For each potential triple the checker independently enumerates ALL orders
of its three corner occurrences and ALL choices of incoming/outgoing native
arms. Equal numerical arms are kept as distinct side slots. An assignment
is retained only when all three consecutive arm matches agree in length.
It then follows those exact slots to far endpoints. One single simultaneous
assignment yields the entire three-pair requirement; the checker never
chooses the three ray conditions independently. The resulting native-arm
assignment sets equal the certificate's sets exactly. This also verifies
the author's smaller sorted-order/eight-flip implementation: all cyclic
orders and arbitrary reflected corners produce the same unordered data.

Far pairs and target stars are compared as Counters, not sets. Thus a far
pair (c,c) requires two occurrences of c in its target star. Repeated copies
are not silently dropped. Constraints forget global tile-copy identity and
placement correlations, which enlarges the allowed finite supports and is
safe for this necessary-condition argument.

## Pruning and support quantifiers

For an actual occurring-star support S, every occurrence of a star gives
one simultaneous native-arm assignment, and all three far pairs belong to
actual stars in S. Thus at least one assignment for that star survives.
This is precisely existential-over-assignment followed by universal-over-
three-rays, not a stronger requirement for every possible assignment.
If S is inside a current atlas, none of its stars can be deleted at the
next monotone pruning step. Induction proves that actual S lies in the
final pruned atlas. Requiring actual S itself to be closed is valid even
if its other occurrences use different microstates.

The independent checker goes further than trusting this pruning lemma:
it exhausts every subset of each ORIGINAL atlas (up to 2^12 choices), not
only the pruned atlas. Every closed twelve-corner cover is found inside
the independently reconstructed pruned atlas. The exact support counts are

    1,1,1,0,3,0,0,3,1,0,1,0  (total 11).

It reconstructs the formal-ring sets independently by relabeling unmatched
B side occurrences and using its multigraph atlas encoding. Every retained
support contains one of these four-star rings. Independently of that ring
classification, the checker also enumerates actual equal-length side
perfect matchings of four faces A0,A1,B0,B1, with both B reference chiralities,
and finds a valid torus witness for EACH of the eleven supports.

## The unbounded geometric conclusion

All four selected ring stars occur in the initial defect-free tiling, so
their actual angle sums are 2pi. Splitting numerical side labels into formal
slot labels does not introduce any unequal-length matches or a new tile
restriction; it selects one permissible periodic witness.

The checked four-face pairings reverse boundary endpoints, use original
whole polygon faces, are connected and orientable, and have eight vertices,
twelve edges and four faces. Every vertex class contains three actual
corners from the support. Vertex links are circular: endpoint gluing
connects the same corner classes as the corner-link intervals. Euler
characteristic zero makes the quotient a torus. Its induced polygon metric
has no cone singularity because all eight angle sums are 2pi. Compactness
makes it complete; the simply connected complete flat cover develops
isometrically onto the Euclidean plane. Its lifted original faces therefore
tile the plane, and its rank-two deck group acts by translations. This
proves global existence; it is not an inference from bounded legal patches.

Reflections cause no omission in either finite encoding or the metric
argument. No assertion that the original unrestricted tiling itself is
periodic is needed. There is no deterministic-branch assumption in this
adjacent-repeat theorem.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-adjacent-independent-2026-10-15.py

Observed result: PASS. The verifier uses the standard library and helpers
from the earlier independent reviewer checker, which also reruns its
separation-two audit. No producer imports, solver, floating point,
randomness, geometric search depth or period bound is used. All finite
arithmetic is exact integer, set and multiset computation. The final
geometric implications are the written arguments above and the named
reviewed dependencies, not claims that the checker formalizes all geometry.

No unresolved defect remains in the scoped adjacent theorem or resulting
six-distinct/at-least-five-distinct hexagon periodic-escape corollary.
Fewer distinct lengths, two five-length hexagons, other side counts and
the main unrestricted two-convex-polygon objective remain outside scope.
