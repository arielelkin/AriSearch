# Nonnegative corner potentials admit a zero-star translated limit

Date: 2026-10-13. Author: sol. Status: independently adversarially reviewed VALID;
[fresh terra review](../reviews/terra-nonnegative-corner-potential-review.md). This is a geometric transfer lemma, not a periodicity theorem.

## Statement and definitions

Let P be a finite set of fixed compact convex polygons with positive area.
Use genuine native polygon vertices, removing redundant collinear boundary
vertices. Suppose T is an admitted edge-to-edge tiling of the entire Euclidean
plane by isometric copies of P: contacts along edges are whole native sides,
and every incident tile contributes a genuine native corner at every vertex.
Reflections and arbitrary rotations are allowed. No finite-local-complexity,
periodicity, frequency, or ergodicity assumption is made.

Choose a native indexing on each polygon. An indexed occurrence records an
isometry from that indexed polygon; indexings resolving polygon symmetries
are retained. Give each native corner a fixed real weight. Assume:

1. The sum of native corner weights on every complete polygon is zero.
2. Every indexed corner star occurring in T has nonnegative total weight.

A star is the multiset of indexed native corner slots incident at a vertex;
its score is the sum of their weights. Then positive-score stars of T have a
uniform O(R) count in every translated square of side2R, for R>=1.
Moreover there is an admitted edge-to-edge plane tiling T0 by P, obtained as
a limit of translations of indexed T, in which every star has score zero.
A prototile species may disappear in T0. Trivalence, if present in T, persists.
More generally any finite allowed indexed star language containing all stars
of T persists in T0. Forgetting indexings gives an ordinary unmarked tiling.

It suffices in assumption2 to specify a finite allowed native-star language
and prove all its stars nonnegative. No restriction beyond those satisfied
by the actual field is added to the unmarked problem. If the positive-star
set is empty, T itself is a witness and the extraction is unnecessary.

## Uniform geometric bounds

Let D bound all polygon diameters and let a>0 be their minimum area. A tile
meeting a bounded set K is contained in its closed D-neighbourhood. Interior
disjointness therefore bounds the number of such tiles by the area of that
neighbourhood divided by a. In particular, for any fixed width h, O(R) tiles
meet a width-h strip around the boundary of any translated square Q_R.
The constant is uniform in square position. Let m bound the native corner
count per tile, and M bound the absolute value of corner weights.

Let alpha>0 be the minimum native interior angle. Every star has at most
floor(2pi/alpha) sectors. Thus only finitely many indexed star multisets can
occur. If any has positive score, their positive scores have a minimum eta>0.
Weights need not be rational or algebraic: this step uses a finite set of
fixed real numbers and strict positivity.

There is also a uniform vertex-separation constant r>0 for every
edge-to-edge field of P. Choose r smaller than every distance from each
native vertex to any other native vertex and to any nonincident native side
of its polygon, over all polygons. All these distances are positive for
fixed genuine convex polygons. Within radius r of a tiling vertex v, its
incident polygons are exactly their corner sectors and together cover the
disk. Another native vertex cannot lie inside a sector, by disjoint interiors,
nor on an incident ray, by whole-side matching and the chosen native distance
bounds. Hence distinct tiling vertices are separated by at least r.

## Boundary identity gives linear positive-star counts

Choose the centroid of every indexed tile as its centre, and select tiles
whose centres lie in Q_R. These are finitely many tiles. Their total corner
weight is exactly zero by assumption1. Partition their corners by geometric
vertex. Vertices with all incident tiles selected contribute their complete
nonnegative star score. Vertices with only some incident tiles selected have
absolute partial score at most mM times the number of selected incident tiles.

Every selected tile participating in such an incomplete star lies within
fixed distance2D of the boundary of Q_R: it has its centre inside, whereas
some tile sharing that vertex has its centre outside and both centres lie
within D of the vertex. The preceding strip-area bound gives O(R) such tiles
and corners, uniformly in the square's centre. Therefore

    0 = sum_complete_star_scores + boundary_partial_weight,
    0 <= sum_complete_star_scores <= C R.

Since every positive complete star has score at least eta, their number is
at most C R/eta. A vertex in Q_(R-D) has all incident tile centres in Q_R.
Replacing R by R+D proves the asserted uniform O(R) bound for all positive
stars inside an arbitrary Q_R. No cancellation between negative complete
stars is allowed or needed.

## Avoid positive stars in arbitrarily large disks

For a prescribed L>=1, put a grid of candidate centres in Q_R separated by
more than2(L+D), with their radius-(L+D) disks contained in Q_R. For R large
compared to L+D there are at least c R^2/(L+D)^2 candidates. Their disks are
disjoint, so each positive star contaminates at most one candidate disk.
The entire Q_R has at most C'R positive stars. Choosing R sufficiently large
compared to (L+D)^2 leaves an uncontaminated disk of radius L+D.
Translate its centre to the origin. Taking L to infinity supplies translated
indexed plane tilings with no positive star in growing disks.

## Indexed compactness and persistence of whole-side stars

For finitely many fixed shapes, bounded diameter and positive minimum area
uniformly bound the number of tiles meeting every compact set. The translation
part of a tile meeting that set lies in a bounded set, and its orthogonal
part lies in compact O(2). Retain the finite prototile and symmetry-resolving
native labels as discrete data. Successive subsequences on larger windows
and a diagonal extraction therefore give convergent indexed tile placements
on every compact window. Coverage and interior-disjointness persist: an
uncovered open disk or overlap of interiors would persist for sufficiently
close approximating placements. The resulting placements form a plane tiling.

The uniform r separation prevents distinct native vertices from coalescing.
At each limit vertex, extract the incident indexed corner sectors on a small
star disk; their finite labels and whole-side partner incidences are constant
on a subsequence. Their limiting sectors already cover that disk. No extra
tile can enter its interior or subdivide an incident whole side without
violating that sector coverage and the whole-side contacts of the convergent
partners. Thus the limiting field remains edge-to-edge and has the same
indexed star at that vertex as sufficiently late approximants. A finite
allowed star language, and in particular trivalence, is consequently preserved.

If a limit vertex had positive score, its persistent indexed star would be
positive at approximating vertices in a fixed bounded disk. Those vertices
converge to the limit vertex, whereas the avoidance radius tends to infinity.
This contradicts the positive-star-free disks. Every limit star therefore
has score zero, proving the statement.

If a polygon symmetry exchanges differently weighted native corners, do not
assign new indexings after taking the limit: the indexed isometries themselves
must be carried through the compactness subsequence. The construction above
does exactly that. Once the zero-core assertion has been used, forgetting
labels retains an admitted unmarked tiling. No shape-only forcing rule is
created by this bookkeeping.

## Scope, dependencies, and applications

The proof uses the standard fixed-polygon placement compactness and the
uniform sector-disk separation argument already independently reviewed in
[the hexagon limit lemma](hexagon-limit-and-periodicity.md). They are written
out here for arbitrary finite genuine convex shapes and edge-to-edge fields.
It does not require a monohedral classification or computation.

The hypothesis is an ACTUAL edge-to-edge plane field. Assigning weights only
to a desired trivalent language does not justify their application to an
original unrestricted partial-contact tiling. Such a tiling must first supply
a suitable field through a separately proved reduction, as in
[the isolated ABB resonance application](two-hexagon-opposite-a-resonance-removal.md).
A zero-star limit establishes existence, not periodicity or universality of
the source field; the zero core still needs an independent obstruction or
periodic-extension theorem. The positive stars may survive sparsely in T.
No positive density or bounded gaps are concluded for any species.

There is no finite search or replay certificate associated with this analytic
lemma. The independent hostile review has completed with a VALID verdict.

## Prior-art boundary

[Rao2017, Section2 Lemma2 and Proposition3](https://arxiv.org/html/1708.00274v1)
already uses zero-density vertex removal and zero-tile corner-weight sign
balance for monohedral pentagon tilings, including partial contacts. The
present statement gives a direct multiple-type edge-to-edge finite-window
formulation. This is a reusable verified version of a known mechanism;
no novelty of the mechanism is claimed. See the
[targeted refresh](../literature/2026-10-13-opposite-angle-coverage-boundary.md).
