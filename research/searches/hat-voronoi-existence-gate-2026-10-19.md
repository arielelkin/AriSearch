# Prescribed-disk Hat Voronoi gate: uniform three-class obstruction

2026-10-19. **Exact finite-witness obstruction, independently Sol-reviewed.**
[Hostile review](../reviews/hat-voronoi-existence-sol-hostile-2026-10-19.md).
For every site in the prescribed closed disk, three cells in a genuine Hat
substitution tiling have respectively five, six, and seven sides. Hence this
entire unweighted disk family fails the exactly-two-congruence-class gate,
even allowing reversal. No claim is made about other site disks or weights.

## Normalization and source

Use the native full-size reference Hat `hat_outline` in
`source-decoration-hat-patch.py`. The eight native kites are the deterministic
output of `ref_kites()`; kite0 is
`[(0,0),(3/2,sqrt(3)/2),(1,sqrt(3)),(0,sqrt(3))]`.
Its vertex centroid is `p0=(5/8,5sqrt(3)/8)`. The retained patch generator
uses half-size Hats, so multiply every generated coordinate and affine frame
by two. This is a global similarity, preserving side counts and congruence
class counts. Reflected Hat occurrences use their actual reflected affine
frames throughout; no chirality restriction is imposed.

Primary source: Smith, Myers, Kaplan, Goodman-Strauss,
[An aperiodic monotile](https://arxiv.org/html/2303.10798v3), especially
Sections 2 and 5, supplies plane existence and the substitution hierarchy.
Creator implementation [hat.js](https://raw.githubusercontent.com/isohedral/hatviz/main/hat.js)
and [geometry.js](https://raw.githubusercontent.com/isohedral/hatviz/main/geometry.js)
were freshly inspected. Our retained exact code follows their outline,
child placement and child selection data. Primary theorem input is that
these genuine substitution supertile patches occur in the infinite Hat
source. This report does not infer source occurrence from area-mismatched
proxy outlines. Every parent type's selection contains an H child (counts
H/T/P/F parents: 3/1/2/2 H children), so every level-4 source supertile contains
a level-3 H. The three witnessed cells therefore occur in every infinite
source possessing this hierarchy; one such source already suffices to
exclude a two-class output for the proposed construction.

## Exact Delone bounds and plane existence

Project p0 onto each of the 13 closed boundary segments, clamping the
projection parameter to [0,1]. Their squared distances in native edge order
are
`[25/16,133/16,507/64,73/16,73/16,217/16,201/16,109/16,361/64,49/16,9/16,27/64,25/64]`.
Thus delta=dist(p0,boundary)=5/8 and rho=delta/4=5/32. Winding places p0
strictly inside the actual Hat; its disk of radius delta is interior.
For p in the closed rho disk, each site lies at boundary distance at least
`delta-rho=15/32`. The open radius-15/32 disks at sites are contained in
pairwise interior-disjoint Hats. Distinct sites are therefore separated by
at least `15/16`, including reflected occurrences.

The maximum squared distance from p0 to a Hat vertex is `301/16`, attained
at native vertex 6. Maximizing first over the p disk gives exactly
`R = sqrt(301)/4 + 5/32` for `max_{p,v}|p-v|`. Every point of a Hat lies in
the convex hull of its vertices, and the Euclidean norm is convex; hence
its distance to that Hat's site is at most R. The source site set is
uniformly separated and R-dense. Its closed Voronoi cells cover the plane
with disjoint interiors, contain a positive-radius disk, and lie in the
closed radius-R disk about their site. Each is consequently a compact
convex polygon, determined by finitely many sites at distance at most 2R.
A site farther than 2R cannot cut this disk, by the triangle inequality.
This proves plane existence of a finite-local-complexity convex palette;
it does not prove that the palette has two shapes.

## Complete local witnesses, without a global collar assumption

The level-3 H contains 1,156 actual Hats, hence 9,248 actual constituent
kites. The producer certifies that all kites are distinct primitive kites
on a single common hex-center lattice with basis
`(3,sqrt(3)),(0,2sqrt(3))`. Each is one of the six standard sectors at its
hex center. Thus interiors are disjoint. Exact edge cancellation includes
all external and hole boundaries; each edge has multiplicity at most two.
All distances below use these actual edges, never a proxy H outline.

Targets 509, 519 and 516 are zero-based recursive expansion indices. Their
p0 sites lie inside their own Hat, and their distances to every exposed
union-boundary segment are strictly greater than 10. Consequently the
entire closed radius-10 disk about each p0 site is covered by the actual
finite patch: a segment from an interior center to any uncovered point
would first cross an exposed union boundary. This argument also rules out
holes in the disk. The exact primitive-kite checks justify this boundary
argument without numerical area tolerances.

For each target retain every other patch p0 site strictly less than 10
away: respectively 21, 23, 22 sites. Any site's position moves by at most
rho as p ranges over the disk. Since
`2R+2rho = sqrt(301)/2+5/8 < 10`, every site at distance at most 2R for any
allowed p is in this local list. In an infinite source containing this
patch, every omitted Hat has its p0 site outside the covered radius-10
disk, since p0 lies in its interior and interiors of Hats cannot overlap.
Thus the local lists are complete. This is a local containment certificate,
not a fixed-depth claim about a complete global neighborhood inventory.

A positive two-class classification would require a proved global collar
closure. The direct attempted fixed geometric type-and-orientation closure
fails here: the retained H squared long/short side ratios at levels 0,1,2
are `16`, `784/25`, `4096/121`. The recurrence changes proxy geometry with
level. It cannot simply be treated as a fixed self-similar substitution.
No global collar certificate is claimed. The witnessed negative result
makes that broader classification unnecessary: three forced local cells
already exclude this disk, independently of any unenumerated cells.

## Exact parameter inequalities and certificate

Write `p=p0+(u,v)`, with `u^2+v^2 <= (5/32)^2`. For central affine site
`s_i(p)` and another site `s_j(p)`, put `d_j=s_j-s_i`. In coordinates
`z=x-s_i(p)`, the cell inequality is exactly
`2 d_j dot z <= d_j dot d_j`.
The d_j coordinates are affine polynomials over Q(sqrt(3)) in u,v.
For each proposed cyclic consecutive pair, solve the two bisector
equalities as equalities using the exact 2x2 determinant formula.

Rational interval arithmetic encloses sqrt(3) between adjacent rationals
of denominator 10^50, whose squared comparison is checked exactly.
Bisector intersections must have nonzero determinant; every nonincident
inequality must hold strictly; each edge's positive oriented length must
be proved; every vertex has squared radius less than 20, and `20<R^2`.
The last test proves the finite halfplane polygon is inside B(site,R),
so omitted sites cannot trim it. Distinct cyclic sides with positive
length and strict nonincident feasibility certify exactly the recorded
number of intrinsic sides, including absence of collinear adjacent sides.

The parameter square is bisected along its longer side, to maximum depth
18. A box is discarded only if its exact minimum distance to the origin
exceeds rho. Every retained box must pass interval checks. This is a finite
cover of the entire closed disk, including its boundary. SciPy proposes
cyclic edge lists at p0; every proof predicate uses rational arithmetic.
A wrong numerical proposal fails the exact checks.

The certified cyclic neighbor lists are:

| Target | Sides | Neighbor list |
|---|---:|---|
|509|5|507,510,516,480,523|
|519|6|518,516,508,511,513,517|
|516|7|509,510,508,519,518,520,480|

Polygons with different numbers of intrinsic sides cannot be congruent,
with either orientation. Hence at least three classes occur for every p
in the entire prescribed disk. The cycle stops at this uniform obstruction.
No two-tile candidate exists here, so periodic omissions and an intrinsic
site/Hat-frame inverse are not reached. No larger disk, weights, or deeper
patch default is introduced. This is a restricted-family negative result,
not a solution or impossibility theorem for the main problem.

## Replay and artifacts

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hat-voronoi-existence-gate-2026-10-19.py

Certificate:
`research/certificates/hat-voronoi-existence-gate-2026-10-19.json`.
Producer:
`research/searches/hat-voronoi-existence-gate-2026-10-19.py`.
The producer is also the exact interval verifier; an independent hostile
review is pending. No novelty claim is made. The precise restart condition
is a materially different site rule or a new theorem; repeating this disk
or increasing the patch size cannot evade the three side-count witnesses.
