# Additive native-corner potentials survive unrestricted-contact limits

Date: 2026-10-13. Author: sol, independently checking the root proposal.
Status: complete analytic proof internally checked; fresh hostile review of
this extracted general statement pending. No novelty claim is made.

## Theorem

Let P be a finite set of fixed genuine convex polygons of positive area.
Assign a fixed real weight to each indexed native corner slot, such that
every complete prototile has total corner weight zero. Let T be any plane
tiling by indexed isometric copies of P, admitting reflections, rotations,
partial-edge contacts and arbitrary vertex valences. If polygon symmetries
exchange differently weighted slots, retain the chosen indexed isometry on
each occurrence as bookkeeping.

A tiling vertex is a position of at least one native tile corner. Its score
is the sum of the weights of ALL native corner occurrences at that position.
Tiles meeting it in the relative interior of a side contribute ZERO; their
flat sectors do not receive native-corner weights. Assume every actual
complete vertex of T has nonnegative score.

Then positive-score vertices have a uniform O(R) count in every translated
square of side2R, for R>=1. There exists an admitted plane tiling T0, obtained
as a limit of translations of indexed T, with score zero at every vertex.
Some species may disappear. No edge-to-edge, trivalence or finite indexed
star-language persistence is claimed for T0.

## Finite positive gap and boundary balance

Let D bound tile diameters, a>0 bound tile areas below, m bound native corner
counts above and M bound absolute corner weights. A tile meeting a compact
set K is contained in its D-neighbourhood; disjoint interiors bound their
number by the neighbourhood's area divided by a. Thus bounded windows have
uniformly finite tile and native-corner counts. Fixed-width strips around
translated square boundaries meet O(R) tiles, uniformly in square position.

Let alpha>0 be the minimum genuine native angle. At a tiling vertex, native
corner sectors have pairwise disjoint interiors and total angle at most2pi;
there are at most floor(2pi/alpha) native corner occurrences. There are only
finitely many possible indexed native-corner multisets, regardless of the
number or arrangement of flat host sectors. Their sums therefore have a
minimum strictly positive score eta, if any positive score occurs at all.
If none occurs, T itself is already the required T0.

Select all tiles with centroids in a translated Q_R. The sum of all their
native-corner weights is zero. At vertices where all incident tiles are
selected this is the full nonnegative vertex score. Incomplete vertices
contribute partial native-corner sums. All selected tiles touching an
incomplete vertex lie within fixed distance2D of the boundary: a selected
centre and an unselected incident centre are each within D of the vertex.
Their total absolute corner weight is O(R). Hence the sum of complete
nonnegative scores is O(R). Every positive complete vertex contributes at
least eta. Every vertex in Q_(R-D) has all its incident tile centroids in
Q_R. Enlarging the selection square by D proves the uniform O(R) bound on
positive-score vertices in arbitrary Q_R. Side hosts cause no uncounted
weight: they contribute zero at the vertex and their genuine corners are
counted at their own positions.

## Clean disks and indexed placement compactness

For each prescribed L, choose disjoint radius-(L+D) disks with centres on
a separated grid inside Q_R. Their number is Omega(R^2/(L+D)^2), whereas
only O(R) positive-score vertices occur in Q_R. Each such vertex spoils at
most one disk. For R sufficiently large a positive-score-free disk remains.
Translate its centre to the origin and let L tend to infinity. Each translated
tilings has zero score at every vertex in its growing clean disk.

The fixed-polygon placement space is sequentially compact on bounded
windows. Local tile counts are uniformly bounded as above; tile translation
parts are bounded and orthogonal parts lie in compact O(2). Retaining finite
native labels, a diagonal subsequence converges to indexed tile placements
on every bounded window. Distinct limiting tiles cannot become identical
or have overlapping interiors, because such an overlap persists under small
placement perturbations. Coverage persists: points are covered by tiles in
a uniformly finite enlarged window and a further finite subsequence retains
a covering tile. The limit T0 is thus a plane tiling by the original shapes.
This argument supplies no vertex-separation assumption.

## Additivity repairs vertex coalescence

Fix a vertex v of T0. Only finitely many limiting tiles meet a neighbourhood
of v and only finitely many native corner positions occur there. Choose
rho>0 so v is the only LIMIT native-corner position in the closed disk of
radius2rho. Work in a larger compact window containing all tiles that could
meet this disk. Under the convergent indexed placements, for sufficiently
late approximants the following two finite multisets are in bijection:

- all approximating native corner occurrences with position in B_rho(v);
- all limiting native corner occurrences with position exactly v.

Indeed a corner converging to v eventually enters that disk, and every other
limiting native corner stays outside it. Uniform local tile counts and the
diameter bound prevent an additional untracked tile from entering the disk.
Native labels, hence weights, are preserved. Each polygon's own distinct
native vertices remain distinct under its isometry; different tiles' corners
may coalesce, but their occurrences remain distinct and both are counted.
There are no duplicate limiting tile occurrences because positive interior
area would contradict disjointness.

Group the approximating native corners in B_rho(v) by their actual geometric
vertex position. Each group is an ENTIRE actual approximating vertex star:
all native corners at that position are included, and any side-interior host
has zero contribution. These finitely many vertices lie within the growing
clean disk for sufficiently late approximants, so each group's total score
is zero. Summing groups yields total native-corner weight zero in B_rho(v).
The multiset bijection makes this sum exactly the limiting score at v.
Therefore v has score zero. Since v was arbitrary, every vertex of T0 does.

This proof handles both splitting and coalescence: several distinct zero
stars may merge, but their additive native weights still sum to zero. It
would FAIL for a desired finite star LANGUAGE that is not closed under these
mergers, or for a host weight depending on whether an incidence is native
rather than flat. Neither stronger assertion is made here.

## Scope and related literature

This strengthens [the edge-to-edge zero-star lemma](nonnegative-corner-potential-zero-star-limit.md)
for the additive zero-SCORE conclusion only. It permits arbitrary original
partial contacts only when NONNEGATIVITY HAS ACTUALLY BEEN PROVED for every
complete native-corner star in that admitted field. Nonnegative scores for
an intended trivalent language alone do not meet the hypothesis. Host-flat
stars, additional valences and reflections must all be checked in an application.
Species disappearance is admitted; it may produce an omission escape but
a separate theorem must establish periodicity. A zero-score limit need not
retain the original contact combinatorics or a prescribed native-star list.

Related primary work: [Rao, arXiv1708.00274v1](https://arxiv.org/pdf/1708.00274),
Section2 Lemma2 and Proposition3, removes sparse vertex types and derives
corner-potential sign balance in monohedral pentagon tilings, including half
vertices. The present artifact supplies a direct finite-window multi-shape
additive cluster argument; no claim of novelty or independent priority is
made. The general theorem is analytic and uses no finite search or solver.
