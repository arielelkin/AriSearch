# Root hostile review: complete fixed-B classification

Date2026-10-10. Reviewer root, independently of the branch author.
Verdict **VALID after the explicit omission-ledger clarification**.
The separate partial_contacts reviewer is independently rechecking that
clarification. [Reviewed proof](../lemmas/branching-hexagon-new-fixed-b-classification.md).

The exact theorem excludes aperiodicity for A threefold alternating(p,q)
with angles120±delta and B=(r,p,q,q,q,q), pairwise distinct r,p,q.
It proves periodic existence from arbitrary admitted contacts by an admitted
trivalent edge-to-edge limit, rather than silently imposing that rule on
the original tiling. The imported limit and prior monohedral/chain mechanisms
have their separate independent reviews.

Initially the new proof proceeded directly to B's r seam, without explicitly
excluding an A-only limit. Root requested the missing omission ledger.
The updated text correctly rules out three pq sectors around a3-ray vertex
by parity, and rules out B-only in the S!=360 case by the r-star angle sum.
This clarification uses the already reviewed local argument; it adds no
both-species requirement to the problem.

The numerical identity S=240+mu follows exactly from the hexagon total and
r-dimer kappa. If the required qq angle mu repeats twice, the other angle
is240-mu and every triple sum differs from360 by an odd nonzero multiple
of mu-120. If it repeats three times then mu=120 and the direct B torus
settles the pair. These cases exhaust the multiplicities except one.

In that case source B2 maps to unique qq target j injectively, because its
p-side A neighbor prevents two sources in one target star. The map moves
centers by bounded distance. Counting source owners in an inner disk proves
O(R) unused targets in an outer disk; the annular area argument is sound.
The union of fixed-radius disks around O(R) defects leaves large rooted
regions with no unused targets. Every A q side meets B, so rooting at B
requires only bounded displacement. This does not assume an injection on
an infinite set is surjective, or infer absence from zero density in the
original tiling.

The exact full-side neighbor choices of a rooted edge-to-edge tiling are
finite. Diagonal stabilization of finite adjacency balls gives a plane
tiling: each Euclidean disk meets uniformly boundedly many fixed-area,
bounded-diameter convex tiles, and transverse segments to dense target
points cross each tile at most once. Uniform graph balls cover those points,
then the locally finite closed union covers the disk. Disjointness and
full-edge trivalent stars stabilize exactly. The fixed root preserves B
and every finite target neighborhood is saturated in the limit.

The three native target cases were checked independently:

* j3: saturation prevents a BBB star at B3, forcing q2/q2 half-turn seams.
  Known A across q3 rules out q4/q4 by the length triples qq,qq,pq, even
  when qq angles resonate. All A neighbors remain physically fixed. The
  repaired disjoint straight-chain argument gives the common B period,
  which transports to all A copies.
* j5: saturation pairs every q2 with q4. A remaining BBB vertex uses only
  B3 and B4; each B3 has one q2 halfedge and each B4 one q4. They must
  occur in equal number, impossible with three sectors.
* j4: the only source mate is q3; the opposite endpoint gives B3 triples
  and beta3=120. Known q4/q5 A neighbors give beta5=120. The exact q-tag
  table forces successive q tags4,5 around every A to differ across each
  p edge. A has an odd3-cycle, giving the contradiction under reflection
  as well.

No new computational search or novelty claim is used. No unresolved gap
remains in this exact fixed-B theorem after the omission clarification.
Other B words or A geometries remain outside its scope.
