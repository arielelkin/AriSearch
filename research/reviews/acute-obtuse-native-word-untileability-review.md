# Fresh hostile review: fixed acute/obtuse pentagon words, all metrics

Date: 2026-10-12. Verdict: VALID, including arbitrary reflections and partial contacts.

This review independently checks the proof in
[the all-metric theorem](../lemmas/acute-obtuse-native-word-untileability.md).
The independent doubled-integer
[angle checker](check_acute_obtuse_angle_capacity.py) reconstructs ALL native
180 and360 multisets, pure-species tables, the formal corner ledger and
endpoint exclusions without importing the construction producer. It verifies
one flat type and all nine full types. Coordinate realizability of the older
module is not a premise of the all-metric theorem.

## Native continuation and forbidden AAA star

A seam ray from x=A147.5 toward alpha=A65 using A1 has far native corners
z/z or z/y. Neither far corner can lie on a flat vertex, because the sole
flat180 multiset is(alpha,beta,gamma). Different lengths therefore force
an impossible endpoint-on-side event. Equal lengths would force an equally
impossible full native completion at the far point. Both combined far angles
exceed180, so no unlisted flat incidence can rescue them. Consequently both
x copies at a proposed(alpha,x,x) star use A2 toward alpha. Their mutual
seam is A1/A1, which starts at the common x point and has equal length on
both copies, so its far endpoint has z/z. This is impossible independently
of metrics. The proof retains both native edge choices under reflection.

## Resource counts

After removing that star, every native x belongs to P=(x,gamma,w), and
every native B144.5 belongs to D=(z,beta,delta). Each is a single occurrence
per tile, not an assumed density. Every flat T uses one beta and one gamma.
Hence finite-window counts give b>=a+T-O(R), a>=b+T-O(R). These imply
T=O(R) and |a-b|=O(R). The only full stars with w are P and Q=(z,v,w),
so Q=O(R). Star lists with higher valence are included; in particular the
doubled flat six-corner star is not silently removed. It only contributes
additional nonnegative beta/gamma consumption to the inequalities.

## Whole and partial A1 contacts

Enumerating the ordered endpoint incidences from the complete full list
leaves exactly A2,B0,B3,B4 as possible whole A1 partners. Its endpoints
z,x cannot be flat vertices, so any non-whole contact necessarily has an
interior junction on A1: a larger covering side extending past an endpoint
would put that forbidden native endpoint on a flat sector. This explains the
whole-or-interior-junction dichotomy used in the final paragraph. A junction
has a flat host and native corners, hence is precisely T; two such A1 hosts
cannot select the same vertex because two pi sectors leave no native angle.

A2 forces the already forbidden(alpha,x,x). B3/B4 force Q through the
unique source A z corner. For B0, the third beta tile at the z endpoint
has just two incident choices. A0/A3 leaves A2/B1 at the third ray; its
nonflat far x/u corners have no full completion. A0/A2 forces A0<A2:
the reverse inequality puts x on a flat sector, equality forces the forbidden
AAA star. Strict inequality instead puts the SOURCE alpha corner on a T.
That event is possible locally and is correctly counted rather than
incorrectly called locally impossible for every metric. Its map to T is
injective because every T contains exactly one alpha.

Partial-A1 and whole-A1/B0 assignments can share a T, but the theorem allows
both charges separately, giving a<=2T+Q+O(R). B3/B4 charges share neither
with another source z nor with a flat vertex. Thus a,b=O(R), contradicting
quadratic area coverage.

## Boundaries and quantifiers

Fixed polygon diameters bound every association. Fixed positive inscribed
radii give uniform local finiteness and O(R) tile counts in fixed-width
annuli; each native vertex/contact has a bounded number of tiles. No FLC,
empirical frequency, invariant tiling measure, pure-species density assumption
or pentagon defect-free-limit theorem is required. Constants may depend on
the actual fixed metrics, which is harmless for the universal statement.
Reflections only permute the two incident native edges already enumerated.

The theorem is stronger than the particular maximum/minimum-edge and
matched-length sample exclusions. It is restricted to these exact native
cyclic angle words. It does not exclude other orderings or perturbed angles,
and establishes no global two-convex-polygon impossibility theorem.
