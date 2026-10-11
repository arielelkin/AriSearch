# Fresh review of the private-octagon common-period theorem

Reviewer: root,2026-10-10. The reviewing agent suggested an initial band
mechanism, but did not develop the author's decisive straight-chord and
regular-neighbor proof. The final proof is audited independently below.
**Verdict: valid** under the exact metric and angle hypotheses in
[the theorem](../lemmas/regular-pentagon-private-octagon-periodicity.md).

The strengthened statement says **every admitted original tiling** has a
nonzero period. Root freshly reread the direct version after the author
rewrote it; this review covers that version, including extra unit QQ contacts.
It does not prove a rank-two lattice. A single nonzero period suffices to
refute aperiodicity under the authoritative problem definition.

Only all-obtuse ETE/trivalent forcing is imported. The only native star is
(alpha,alpha,beta), so two beta sectors cannot meet. A private nonunit side
must match its own unique index in Q. An alpha/alpha side is excluded by
nonadjacency; beta/beta would create two beta sectors. An alpha/beta side
must match with opposite endpoints. Defining graph edges **only** at the
private contacts gives degree2 even if unit sides have extra QQ neighbors.
Convexity prevents two distinct sides being shared with the same neighbor.
The proof therefore needs neither averaged saturation nor the chain limit.

Every P corner must have a Q side neighbor because a PPP star is impossible.
At most two P sides can have P neighbors, hence each P has at least three Q
side neighbors pointwise. This conclusion covers the original tiling.

The half-turn argument is complete even for reflected tiles. In the frame
of a Q copy, a neighbor matching the same native side and swapping its
distinct-angle endpoints is either the midpoint half-turn or reflection
in the perpendicular bisector. The latter puts both polygon interiors on
the same supporting side and causes overlap near the shared segment's
midpoint. Hence only the half-turn is admissible. Allowing reflections
does not add a missed neighbor choice.

The two native private midpoints a,b are distinct. Their chord interior
lies in the strictly convex polygon interior. Composing the two forced
half-turns gives translation2(b-a). The author's induction displays every
member of a degree-two chain, with chords consecutively filling a complete
straight line. These copies cannot close into a finite cycle because a
compact polygon is not invariant under a nonzero translation.

The axes of distinct chains cannot cross or coincide. A chord interior
is inside its Q; the interior of another tile is dense up to its boundary,
so no point of any other tile can lie there. At a chord endpoint both
incident Q tiles fill a disk on the two sides of a whole private segment;
no third chain can reach it. Every chain axis is an entire affine line,
so disjointness forces all axes parallel. All two-step vector lengths are
the same2|b-a| because every initial frame is orthogonal, even under a
reflection. Parallelism therefore gives exactly a common vector u or-u,
not arbitrary multiples or an irrational scale mismatch. Both signs
preserve each chain, so the entire Q tile set is u-invariant.

Finally, a regular unit pentagon is geometrically unique across a given
unit side in a prescribed half-plane. This uses actual regularity, not
equiangularity alone. Every P has a Q side neighbor. The neighbor across
the translated Q side cannot be Q: Q-set invariance under-u would translate
that Q neighbor back to an existing Q on the original P side, causing an
overlap. Hence it is P, and uniqueness identifies it with P+u. Applying
the argument to-u proves equality of P tile sets, rather than an injection.
This extra neighbor-type argument is essential in the strengthened version,
where unit QQ contacts are allowed, and it is correct. The full original
plane tiling has a nonzero translational symmetry.

Attacks checked: private edges lying in inadmissible positions; same-length
ambiguity; reflection alternatives; coincident private midpoints; a finite
Q cycle; chord boundary degeneracy; intersections at seam midpoints;
different chain spacings or chiral frames; an omitted prototile; a period
of the Q set that fails to preserve P; and replacing a required rank-one
conclusion by an unproved rank-two construction. The hypotheses and proof
exclude all of these within the statement. No substantive defect or repair
was needed. No computation, numerical bound, or current literature theorem
beyond reviewed all-obtuse forcing is used.

Remaining families include equal private lengths, irregular equiangular P,
other side alphabets and adjacent-alpha Q. This restricted theorem neither
excludes them nor resolves the general two-convex-polygon target.


The initial limit-based version was also valid but weaker. The author
supplied the direct strengthening; root did not develop that proof. The
fresh re-review checked the changed dependency, private-contact graph and
neighbor-type propagation explicitly. **Verdict: valid for the strengthened
every-tiling statement.**
