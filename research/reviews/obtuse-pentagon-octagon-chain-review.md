# Fresh hostile review: nonadjacent-alpha octagon chain limit

Reviewer: `primary_literature`, 2026-10-09. The reviewer did not develop or
modify the proof. Reviewed
[the chain-limit lemma](../lemmas/obtuse-pentagon-octagon-chain-limit.md),
[all-obtuse forcing](../lemmas/obtuse-edge-forcing.md), and the fixed-sector
separation step, independently of the author's conclusions. No computation
is required for this claim.

## Exact claim and hypotheses

P is a fixed genuine convex equiangular pentagon with every angle108 degrees.
Q is a fixed genuine convex octagon with two108-degree and six144-degree
corners, with the two108-degree corners nonadjacent. If these two polygons
admit any plane tiling, allowing reflections and arbitrary contacts, they
admit a potentially different translated-limit plane tiling in which every
P has two nonadjacent P full-side neighbors and three Q neighbors, and every
Q has two Q full-side neighbors and six P neighbors. Each Q-to-Q side has
opposite alpha/beta endpoint correspondence; the resulting same-type graphs
are simple2-regular and have only finite cycles or double-infinite paths.

The claim does not classify side lengths, bound cycle lengths, force
deterministic placements, or give any translational period. It expressly
allows sparse bad contacts in the original tiling. Nonadjacent alpha corners
are essential to its particular nonnegative Q deficit.

## Nonnegative deficits and uniform boundary counts

All native angles are strictly between90 and180 degrees, so the reviewed
all-obtuse argument excludes vertex-to-side contacts and forces complete
native-side matches and three sectors at every vertex. The only allowed
three-sector sum is108+108+144=360 degrees. Three108 sectors sum324;
one108 and two144 sum396; three144 sum432. Thus every star has exactly
two alpha and one beta sector.

At a P corner, two P side neighbors would create a forbidden all-alpha
star. P-neighbor slots therefore form an independent set in a five-cycle,
with size at most2. P has at least3 Q sides, so d_P=#Q sides-3>=0.
At each alpha-Q corner at least one neighboring sector is beta and hence
belongs to Q. A Q side cannot touch both alpha corners because they are
nonadjacent. Consequently Q has at least2 Q sides, at most6 P sides, and
d_Q=6-#P sides>=0. These arguments apply pointwise to the original tiling,
not just in the selected limit.

Here is an independent justification of the uniform O(R) errors. Choose a
fixed interior center for each reference tile, transported with its placement,
and let D bound tile diameters. Any tile whose corners, center, or full-side
neighbor cross a window boundary lies in a strip of bounded width depending
only on D. This strip has area O(R), uniformly in the translated square's
center. Disjoint tile interiors and positive minimum area bound its tile
count by O(R). A tile has at most8 corners and8 full-side neighbors, so
both corner and side-incidence errors are uniformly O(R). Complete-side
neighbor multiplicity is bounded, including reflected or differently
oriented copies. The same area bounds give N_P+N_Q=Theta(R^2).

Counting alpha and beta corners, with boundary stars discarded, yields

    5N_P+2N_Q=12N_Q+O(R), hence N_P=2N_Q+O(R).

Counting P/Q side incidences from the two sides gives

    3N_P+sum_P d_P=6N_Q-sum_Q d_Q+O(R).

Substitution gives sum_P d_P+sum_Q d_Q=O(R). Because all terms are
nonnegative integers, the number of tiles with positive deficit is bounded
by the same uniform O(R). There is no cancellation of two signed deficits,
and this count is uniform in translation. It does not imply that an
original tiling has no bad tile.

## Disk avoidance and the actual plane limit

Suppose every radius-L disk contained a bad-tile center. Then every point
of a square of side2R would lie in a radius-L disk about a bad center in its
L-enlargement. There are O(R+L) such centers. The union of their radius-L
disks has area at most C(R+L)L^2, which is less than4R^2 when R is large
enough compared with L^2. This contradiction gives arbitrarily large disks
without bad centers in one actual tiling. The proof does not assume that
locally legal patches can independently be extended.

After translating these disks to the origin, local finiteness gives a
uniform tile-count bound in any fixed window: all tiles meeting it lie
inside its D-enlargement and have a fixed positive minimum area. Their
orthogonal maps lie in compact O(2), and translations are bounded on that
window. A diagonal subsequence therefore has limiting whole placements.
Full-area overlaps would persist on a small open ball, contradicting the
approximants. The locally finite closed union of limiting tiles cannot
leave an open gap, since all the approximating tiles meeting a surrounding
compact window have been extracted. Coverage and interior-disjointness
give an admitted plane tiling by the same undeformed prototiles.

Tiles meeting a fixed radius-M disk have centers at distance at most M+D
from the origin, so their approximating copies are good once L>M+D. This
margin is necessary: a disk containing no bad centers alone does not say
that every tile touching its boundary is good. The proof uses the margin
correctly.

## Full-side, vertex-star, and degree stability

The fixed-shape separation argument is sufficient. Take r below every
reference vertex's distance to every other native vertex and every
nonincident native side, across both fixed polygons. All those distances
are positive. A tile incident at a vertex v agrees with its whole corner
wedge inside B(v,r). The three wedges cover the disk. Any other native
vertex there would lie in a tile interior or on a shared native-side ray.
The first violates interior-disjointness; the second would subdivide a
complete native side, which all-obtuse forcing forbids. Distinct tiling
vertices are therefore uniformly separated, including vertices from
different tile occurrences.

This is stronger than a minimum side-length observation and excludes
coalescence of distinct stars in the limit. For each selected tile one
may freeze the finite types and native side slots of all its neighbors
on a subsequence. Its matching endpoint equalities survive placement
convergence; the full positive-length sides remain matched. Distinct
neighbors cannot collapse to one tile, because their full-area interiors
would then overlap in nearby approximants. All-obtuse forcing also applies
to the resulting actual limit tiling, giving uniqueness across each side
and three genuine sectors at its vertices. Each retained tile thus keeps
the same P/Q neighbor counts and has deficit0. Both types remain: a good
P has Q neighbors, and a good Q has P neighbors.

## Endpoint, corner, and chain claims

Every good Q has only two Q sides. Its two nonadjacent alpha corners each
need a distinct one, so exactly one Q side is incident to each alpha
corner, and the other side neighbor there is P. Every alpha-Q star is
P,Q,Q; its neighboring Q sector is beta.

A Q-to-Q side with two beta endpoints would require two alpha endpoints
on the other Q, since two beta sectors cannot occur at a star. That would
be an alpha-alpha side, excluded by nonadjacency. A side with two alpha
endpoints is excluded immediately. Hence both Q sides have one endpoint
of each angle type, and their endpoint pairing is opposite. All their
endpoint stars are P,Q,Q. The two Q sides of one tile cannot share a beta
corner: that would give a Q,Q,Q star. Such a star would contain two
alpha-Q sectors, each having two Q side neighbors, contrary to the preceding
one-Q-side property. They cannot share an alpha corner for the same reason.
The two sides have four distinct endpoints, so Q has exactly four P,Q,Q
and four P,P,Q corners.

The two P-neighbor side slots of each good P are nonadjacent. Their
complement of three Q slots has exactly one consecutive pair in the
five-cycle. The corner between that pair is P,Q,Q. The other four P corners
are P,P,Q. This independently agrees with the global incidence counts:
N_P=2N_Q, one P,Q,Q corner per P and four per Q give respectively
2N_Q P incidences and4N_Q Q incidences at that star kind.

Finally, two interior-disjoint convex whole tiles cannot share two distinct
native sides. Those segments do not lie on one line for genuine convex
polygons; their convex hull would have positive area inside the intersection
of the two tiles. Thus side-neighbor slots correspond to distinct neighbors,
the same-type graphs have no parallel edges, and no plane tile neighbors
itself. Their degree is exactly2. In a connected simple2-regular graph,
walking through the other edge at each vertex either returns to form a
finite cycle or continues indefinitely in both directions. Degree2 forbids
an attached branch or a one-ended endpoint. This proves exactly the
claimed component classification, with no hidden finiteness or periodicity
assumption.

## Defects, repairs, uncertainty, and verdict

No counterexample or proof defect was found under the stated hypotheses.
No proof repair was made by this reviewer. The potentially dangerous
steps—signed deficits, boundary uniformity, center-versus-tile margins,
vertex coalescence, and parallel adjacency edges—are all accounted for.
The proof does not establish existence for chosen length data, rule out
finite cycles, establish a finite geometric state set, or prove periodicity.
Its statements concern the translated-limit tiling; sparse exceptions in
an original tiling remain possible. No novelty claim is audited.

**Verdict: VALID necessary chain-limit reduction**, for nonadjacent-alpha
108/144 octagons exactly as stated.
