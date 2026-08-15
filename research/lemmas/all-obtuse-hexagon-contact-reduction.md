# All-obtuse hexagon contact reduction

**Status:** Candidate under repair after hostile review.

## Statement

Let `P` be a finite set of strictly convex hexagons such that every interior
angle of every member of `P` lies strictly between `pi/2` and `pi`. In every
tiling of the Euclidean plane by isometric copies of members of `P`, with
reflections and unrestricted contacts allowed:

1. no tile vertex lies in the relative interior of another tile side;
2. every side is paired along its full length with one full side of a
   neighboring tile;
3. exactly three tile vertices meet at every tiling vertex; and
4. the resulting abstract cell complex is the standard `{6,3}` honeycomb.

No matching rules, edge-to-edge convention, orientation restriction, or
chirality convention is assumed.

## Definitions and hypotheses

A tiling is a covering of the plane by closed polygonal tiles with pairwise
disjoint interiors. It is locally finite here. Indeed, the finite protoset
has a positive minimum inradius `r` and a finite maximum diameter `D`. If a
tile meets a compact set `K`, its incenter lies in the bounded closed
`D`-neighborhood of `K`. The tiles' open inballs of radius at least `r` are
pairwise disjoint, and only finitely many such balls can be packed into that
bounded neighborhood.

The *abstract cell complex* has one face for each tile and uses the actual
side and vertex incidences established below.

## Proof

Suppose first that a vertex `x` of one tile lies in the relative interior of
a side of another tile. The latter tile occupies one of the two local
half-planes bounded by the supporting line of its side. Tiles on the other
side must fill an angle of exactly `pi` at `x`.

One strictly convex tile corner has angle less than `pi`, so it cannot fill
that half-plane alone. Two or more permitted corners have total angle greater
than `pi`, because each is greater than `pi/2`. An edge-interior sector has
angle `pi` and leaves no room for a corner. Hence no tile corner can occur in
the relative interior of another tile side.

If the neighboring tile along a side changed at an interior point of that
side, the change point would be a vertex of one of the neighbors lying in the
relative interior of the original side. This has just been excluded.
Therefore one neighboring side runs along the entire original side. Its
endpoints cannot extend beyond either endpoint of the original side, since
that would put the original endpoint in the relative interior of the
neighboring side. The two sides consequently coincide in full.

At a tiling vertex only polygon corners now occur. One corner cannot fill
`2*pi`. Two corners have total strictly less than `2*pi`. Four or more have
total strictly greater than `2*pi`. Thus exactly three corners meet at every
vertex. The tiling is an edge-to-edge trivalent hexangulation of the plane.

Replace each physical hexagonal face by a unit regular hexagon and glue full
sides according to the established incidences. Three sectors of angle
`2*pi/3` meet at every vertex, so the resulting polyhedral metric is locally
Euclidean, including at vertices. Its topological realization is the plane,
and hence is simply connected.

The regularized metric is complete. Triangulate every unit regular hexagon by
joining its center to its vertices. This is a locally finite complex of
congruent equilateral triangles with uniformly bounded vertex degree. Choose
`epsilon>0` smaller than one quarter of the altitude of such a triangle. The
closed `epsilon`-neighborhood of any triangle is contained in the union of
the triangles meeting that triangle at a vertex: outside that finite closed
star, every route from the triangle must cross the interior strip between two
nonincident sides, whose width is at least the triangle altitude. Each closed
star contains a uniformly bounded finite number of triangles and is compact.

Now let `(x_n)` be a Cauchy sequence. Choose `N` such that
`d(x_n,x_N)<epsilon` for all `n>=N`, and choose a triangle containing `x_N`.
The tail lies in that triangle's finite closed star, hence has a convergent
subsequence. Since the full sequence is Cauchy, it converges to the same
limit. Thus the regularized path metric is complete.

A complete simply connected flat surface has a developing map to the
Euclidean plane that is a global isometry: the developing map is a local
isometry, completeness makes it a covering onto the plane, and the plane is
simply connected. Therefore the regularized complex is the standard regular
hexagonal `{6,3}` honeycomb. This proves all four claims.

## Dependencies

Only elementary planar angle sums and the standard developing-map theorem for
complete simply connected flat surfaces are used.

## Scope and non-consequences

- The lemma applies only when **every** prototile is a hexagon and every angle
  is strictly between `pi/2` and `pi`.
- It reduces unrestricted contacts to a honeycomb cell structure. It does not
  force edge labels, tile types, orientations, or aperiodicity.
- It does not resolve the two-prototile objective. Either hexagon may still
  admit a periodic monohedral tiling, and a two-type honeycomb system may have
  periodic symbolic configurations.
- The strict inequalities are essential to the short angle-counting proof.

## Adversarial-review status

The first hostile review found an invalid completeness inference in the
original extraction; see
`research/reviews/all-obtuse-contact-review-2026-08-15.md`. The proof above
contains a replacement uniform-star argument and awaits the required fresh
review of that repair.

## Supporting computation

None. The result is purely deductive.
