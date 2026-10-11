# Fresh hostile review of symmetric equal private octagon sides

**Verdict: VALID for the exact conditional periodicity theorem and complete
12-case positive nonunit closure classification.**
Reviewer: `/root/penrose_extension_gate`, 2026-10-10. The reviewer authored neither
[the source lemma](../lemmas/private-octagon-equal-private-symmetric-periodicity.md)
nor [the producer](../searches/private-octagon-equal-private-unit-closure.py).
The earlier universal pentagon-rigidity dependency was already independently
reviewed. This review does not prove that any particular classified octagon
tiles and does not classify nonsymmetric equal-private octagons.

## Native branches really identify one physical neighbor

All-obtuse forcing removes T contacts and gives full native-side matches.
The only angle star is 108+108+144. A private 144/144 side would require a
mate with two 108 endpoints, absent because Q's 108 corners are nonadjacent.
Thus both private sides are 108/144. They cannot both meet the same 108 corner:
the two mates would each contribute 144 there, exceeding 360. Each 108 corner
therefore has exactly one of the private sides.

Let a placed mate be GQ with matching native side j different from the source
slot i. An actual symmetry S exchanging the two sides sends side i to side j
and preserves native corner angles. Replacing G by G composed with S (or its
inverse) changes the parametrization, not the physical polygon, because SQ=Q.
The resulting same-slot map must exchange the segment endpoints: the corner
angles on its two sides must be complementary 108/144 at each endpoint. There
are precisely two such Euclidean isometries of one fixed segment. The half-turn
puts the native interior in the opposite half-plane. Reflection in its
perpendicular bisector puts the interior on the original supporting side and
would overlap on an open neighborhood. Hence the mate's physical polygon is
exactly the midpoint half-turn of Q, independent of its native label. This
argument covers orientation-reversing symmetries as well as central symmetry;
it does not confuse equality of lengths with equality of placed polygons.

The native side labels may branch but the geometric neighbor does not. No
condition on the other six lengths, including their mutual equalities or
coincidences with P lengths, is used. The private value must still occur exactly
twice on Q and be absent from P, as expressly hypothesized.

## Synchronization and every original tiling

Both private contacts are actual midpoint half-turns. Their two midpoints are
distinct in a genuine strictly convex polygon. Chord segments lie in the tile
interior except at their endpoints, and matching half-turns extend the chain
along one line with nonzero two-step period 2(a1-a0). A bounded polygon cannot
be invariant under a nonzero translation, so no two-edge chain closes. The
chain extends in both directions in a plane tiling.

Two chain lines cannot cross: if they meet in a Q interior they share its
unique chain, and if they meet at a private side midpoint the two incident Q
tiles already cover a neighborhood there, again forcing the same chain.
Otherwise distinct chain interiors would overlap. Coincident lines likewise
force a shared Q and hence the same chain. Distinct chain axes are therefore
parallel. Every Q lies on a chain, and each chain's period magnitude is the
same fixed value 2|a1-a0|. Choosing either direction gives one common nonzero
u preserving the full Q set in both directions. Extra shared Q-Q contacts do
not change these private chains.

On the pentagon's five-cycle no two P side neighbors are consecutive, because
three 108 sectors do not form the required star. Every P therefore has at least
three Q side neighbors and a PQQ corner. Translate that corner's two actual Q
neighbors by u. A third Q in the translated residual sector would pull back by
-u to a present Q overlapping the original P near the corner. Thus the third
tile is P. The separately proved universal adjacent-corner rigidity identifies
it with P+u, including all repeated-length pentagons and reflected placements.
The inverse direction gives invariance rather than only inclusion. The theorem
therefore concerns every original admitted tiling, not a selected good limit.

## Complete unit closure cases, singular values and actual symmetries

The new [independent checker](verify_private_octagon_equal_private_unit_independent.py)
imports no producer. It reconstructs the direction exponents by accumulating
exterior turns from the two 108 corners, then derives the base closure sum and
solves each of the 12 cases. It compares every retained coefficient vector and
classification with the certificate. The outcomes are two positive fixed
nonunit solutions, two free-L rows, four nonreal solutions, one inconsistent
zero-coefficient equation, one L=0 solution and two unit-only solutions.

The accepted fixed lengths are phi and 3-phi=(5-sqrt(5))/2. For these it explicitly
checks the reflected vertex maps v->2-v and v->3-v using the actual complex
isometries, not only invariance of the angle and length words. For the two free
gap-4 rows it checks the actual central map v->v+4. Each symmetry exchanges the
private edges as physical segments. It also checks the physical-mate identity
H_i S^{-1}(Q)=H_i(Q), and verifies the reflected equivalence of the two free rows
as an identity in L. Supporting-side determinants are positive for the fixed
solutions; for the free family every such polynomial has nonnegative exact
coefficients and at least one positive coefficient. This proves global strict
convexity for every L>0, not just a sampled instance.

The unit distinction must be retained: gap-4 L=1 is a genuine closed octagon
but has no length private from regular unit P, so it lies outside the theorem.
It is not geometrically excluded by closure or positivity. The two unit-only
rows and that point on each free row are excluded by the explicit L!=1/private
hypothesis. The L=0 row is nongenuine. No limit theorem is asserted at these
boundaries. The author clarified the omitted-row sentence after this review:
L=1 is explicitly excluded by the private-length hypothesis. The formal domain
and certificate already had that correct restriction. No clarification remains
outstanding.

## Nonsymmetric local boundary and replay

The source's two local G_ij formulas correctly give the forced complementary
angle endpoint assignments: equal native start types require an orientation-
preserving endpoint swap, while opposite types require an orientation-reversing
endpoint preservation. The linear coefficients have unit modulus. A nontrivial
rational-angle affine rotation has finite order; a glide squares to a translation.
If the latter square is identity, two successive chain placements share both
private sides, impossible for distinct convex tiles with disjoint interiors.
These observations are local alternatives, not global existence or a common-
period proof for mixed nonsymmetric native choices. The source explicitly
retains that unresolved boundary.

Successful replay:

```text
conda run --no-capture-output -n arisearch python research/searches/private-octagon-equal-private-unit-closure.py
conda run --no-capture-output -n arisearch python research/reviews/verify_private_octagon_equal_private_unit_independent.py
```

PASS: all 12 closure cases, four admitted rows, four actual symmetry maps,
positive supporting sides over the full free-L range, physical-mate invariance
and free-family reflected equivalence. No solver, random seed, search bound,
producer import or plane-existence inference is involved. No new octagon
research mechanism was launched by this audit.
