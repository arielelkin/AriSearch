# Fresh hostile review: distinct-length pentagon/private-octagon periodic escape

**Verdict: VALID for the stated periodic-escape theorem.** The reviewer did
not develop or repair the [root proof](../lemmas/private-octagon-distinct-pentagon-periodic-escape.md).
No computation is needed. One non-consequence sentence should be corrected:
additional Q sides with lengths absent from P are covered by the theorem's
explicitly unrestricted other-six-side hypothesis. They force untileability
once the two Q slots of every good Q are already consumed by x,y; they are
not an excluded family. This is a scope wording issue and does not affect
the theorem or proof.

## Exact claim and hypotheses

P is genuine convex equiangular108, with five distinct native side lengths.
Q is genuine convex with two nonadjacent108 and six144 corners. It has two
specified distinct positive lengths x,y, each occurring on exactly one Q
side and absent from P. The claim is that any admitted plane tiling implies
existence of an admitted tiling with a nonzero translation period. It does
not assert periodicity of the original tiling. Rotations, reflections,
contacts and omission conventions are those of the unrestricted problem.

## Limit and private neighbor maps

The independently reviewed all-obtuse forcing and octagon chain limit have
exactly the needed hypotheses. The limit is a genuine tiling by undeformed
P,Q with full side contacts, every Q has exactly two Q neighbors and every
P exactly one PQQ corner. It is legitimate to prove a periodic tiling in
this potentially different limit: one periodic admitted tiling refutes the
strong-aperiodicity quantifier. The source proof does not assume that sparse
original defects vanish pointwise.

Each unique private x/y side has a Q mate at the identical native slot.
No Q alpha-alpha side exists. A beta-beta side would create a forbidden
pair of beta sectors at a star. Hence the private sides are alpha-beta,
and the endpoint pairing exchanges the corner types. Exactly two plane
isometries exchange the two fixed endpoints: a half-turn about their
midpoint and reflection in their perpendicular bisector. The reflection
preserves the supporting interior half-plane and produces local interior
overlap along the side. The half-turn is the unique allowed mate, including
when the current placement is reflected.

## All Q copies, axes and common period

The two private midpoints are distinct points on different genuine sides.
Their open chord lies inside Q: any boundary chord between two relative
side interiors would require a common supporting face, incompatible with
two distinct genuine polygon sides. Midpoint half-turns concatenate those
chords on one line, each advancing the same nonzero displacement. The
private graph has degree2 at every Q, not only at a selected subset. It
cannot close because the resulting chord line advances monotonically,
and its two-step tile map is translation by a nonzero vector.

At least one open chord at an axis intersection would put a different
closed tile inside an existing tile interior, causing positive-area overlap.
If two chord endpoints coincide, a full-side midpoint has precisely its
two side mates in a small neighborhood; these belong to the same private
chain. Thus distinct axes are disjoint entire lines and consequently
parallel. All their two-step periods have the same fixed length because
all Q placements are isometries of one shape. Their period vectors are
therefore u or -u for one nonzero u. Each chain is invariant under both
signs, so the entire set of Q occurrences is invariant under both signs.
There is no unexamined finite chain or Q component.

## Pentagon wedge uniqueness and propagation

The two Q copies at a PQQ corner prescribe the residual108 wedge and two
whole adjacent P side segments. Their distinct numerical lengths identify
two unique native sides of P. They meet at exactly one native vertex, so
its image must be the prescribed corner. Unequal lengths fix which native
side maps to which segment. The common vertex and the two other endpoints
then determine at most one Euclidean isometry. A reflection cannot create
another placement: it would have to fix the same three noncollinear
points after composition with the first placement, hence is the identity.
This checks endpoint reversal and reflection explicitly.

Translation by u sends every original good-limit Q pair to an actual Q
pair in the same limit. Every endpoint of a Q-Q seam in that limit has
star PQQ, so the third tile is P. The prescribed two segments are translated
exactly, and wedge uniqueness makes the actual P equal to P+u. All P tiles
have such a corner, and applying the same argument to -u gives a bijection
of the P set. Together with Q invariance this proves the claimed period.
No finite-state or rank-two assertion is required.

## Defects, repairs and remaining uncertainty

No counterexample, omitted orientation, native-index ambiguity or limit
quantifier error was found. No geometric repair is required. The other-six-
length scope wording identified above is the sole requested clarification.
The original unrestricted two-polygon problem remains open; repeated private
lengths, only one unique private length and different angular signatures
have not been covered by this audit. No novelty claim is reviewed.

The reviewer separately noticed that the good-limit step is avoidable and
proposed a direct every-original-tiling strengthening plus an exact
adjacent-corner-rigidity classification in
[the proposed addendum](../lemmas/private-octagon-adjacent-corner-rigidity.md).
That new work was developed by this reviewer and is **not** adversarially
approved by this review. It requires an independent reviewer who did not
develop it. The present verdict concerns only the root's weaker theorem.
