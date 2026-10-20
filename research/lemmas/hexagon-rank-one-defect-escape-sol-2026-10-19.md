# A single period survives hexagon defect removal

Date: 2026-10-19. Status: independently hostile-reviewed valid; see [review](../reviews/hexagon-rank-one-defect-escape-hostile-sol-2026-10-19.md).
No novelty claim. This is a structural result, not a resolution of the two-polygon problem.

## Statement and dependencies

Let F consist of two fixed genuine convex hexagons, with nonempty interiors.
If an unrestricted plane F-tiling has a nonzero translation period T, then
F admits an edge-to-edge, everywhere-trivalent plane tiling with period T.
Consequently F admits a doubly periodic edge-to-edge, everywhere-trivalent
tiling. A species may disappear. Reflections are allowed.

The first conclusion uses the uniform defect bound and sector-disk separation
argument in [hexagon limits](hexagon-limit-and-periodicity.md), based on the
reviewed [global side-count proof](side-count-and-monohedral-obstructions.md).
The second uses the independently reviewed [single-period escape](edge-to-edge-single-period-double-period-escape-2026-10-19.md).
All sides below are genuine native sides, so every corner angle is strictly
between zero and pi. Let D bound the tile diameters.

## 1. A geometric defect set and its uniform bound

Planarize all tile boundaries at native vertices and contact endpoints.
Let B be the union of these two sets of geometric points:

* a native vertex lying in the relative interior of another tile's native side;
* a planarized vertex whose graph degree is at least four.

The tiling is locally finite, with a uniform bound on tiles meeting a bounded
window: tile interiors are disjoint, tile areas have a positive minimum, and
a tile meeting a window lies within its D-neighborhood. Thus B is locally
finite, though a uniform separation for B is neither assumed nor needed.
Translation T preserves B.

There is a constant C such that, for every R>=1,

    #(B intersect Q_R) <= C(R+1),       Q_R=[-R,R]^2.             (1)

Here is the precise passage from the imported patch bound to (1). Use the
selected square patch for Q_(R+D+1). Every tile touching a point of Q_R is
selected, since its interior meets the larger open square. Thus every such
point has its complete star in the interior of the selected union. Every
first-kind defect contributes at least one subdivision to delta=I-6N; each
distinct point contributes a distinct native-side subdivision. Every
second-kind defect contributes at least one to D_v=sum(deg(v)-3).
Even when a point is of both kinds, counting the union is bounded by the
sum. Therefore #(B intersect Q_R)<=delta+D_v for the enlarged patch.
The identity and boundary estimates of the imported hexagon lemma give
(1), with a constant depending only on F. Padding is essential: no boundary
vertex is charged as an interior valence defect.

Every defect-free open neighborhood in this tiling is edge-to-edge and
trivalent away from its boundary. Indeed an endpoint of a proper partial
side contact is a native corner in another side's relative interior. The
absence of such points makes each contact a common complete native side or
a common native vertex. All remaining vertices have degree at least three,
by strict convexity; absence of second-kind defects makes the degree three.
There are then exactly three native corner sectors.

## 2. Only finitely many defect orbits

Set ell=|T|, e=T/ell, and choose a unit vector n perpendicular to e.
Take any m distinct T-orbits in B. Choose representatives b_1,...,b_m
so that 0<=b_j dot e<ell. Their transverse coordinates have a finite maximum
absolute value H; H can depend on this chosen finite collection.
For R>=max(H,ell,1), all points

    b_j + kT,    |k| <= floor(R/ell),    1<=j<=m,

have e-coordinate of absolute value at most 2R and n-coordinate of absolute
value at most R. Their Euclidean norm is less than 3R, so all lie in the
original-coordinate square Q_(3R). Points counted for different j are
distinct, since their orbits are distinct. By (1),

    m(2 floor(R/ell)+1) <= C(3R+1).

Fix this finite collection and let R tend to infinity. It follows that
2m/ell<=3C. Since the same upper bound holds for every finite collection of
orbits, the entire orbit set is finite. This avoids interchanging an
infinite orbit count with an asymptotic estimate; no uniform bound on H
was used.

Each orbit has a constant n-coordinate. Hence there is H_0<infinity such
that all defects satisfy |x dot n|<=H_0. If B is empty take H_0=0.
In particular, both half-planes outside this strip are defect-free. This
is stronger than merely having arbitrarily wide defect-free collars.

## 3. A translated limit keeps the period

Let a_j tend to positive infinity and translate the entire original tiling
by -a_j n. Its defect strip now has transverse coordinate near -a_j.
Every fixed bounded window and its fixed D-neighborhood are eventually
inside a defect-free half-plane. Each translated tiling still has the exact
period T, because translations commute.

Finite fixed polygon tilings are sequentially compact in the local placement
topology: uniform local tile-count bounds, compactness of orthogonal parts,
and bounded translation parts for tiles meeting a fixed window give a
diagonal convergent subsequence. One can use each tile's centroid as anchor
and a finite type label; limits preserve interior-disjointness and coverage.
For coverage, for each point choose a covering tile in every approximant;
a convergent subsequence of its bounded placements covers that point in
the limit. An interior overlap would persist in the approximants.

The limit retains T. For any limit tile P, choose approximating tiles P_j.
Their translates P_j+T are tiles of the same approximants and converge to
P+T, so P+T is a limit tile. The same argument with -T gives equality of
the translated tile families. This is preservation of the specified period,
not an inference from defect-free limits without controlled translations.

The limit is edge-to-edge and trivalent. For completeness, the uniform
separation used to close this condition is as follows. Choose r>0 below
every distance from any prototile vertex to any other vertex or any
nonincident side. At a defect-free vertex v, all incident tiles coincide
inside B(v,r) with their corner sectors, and those sectors cover that disk.
Another native vertex in that disk can lie neither in a sector interior
(disjoint interiors), nor on a sector boundary ray (whole-side matching
and the choice of r). Thus native vertices in a defect-free patch away
from its boundary are separated by r. In the translated sequence every
fixed window eventually has this bound. Native vertices cannot coalesce;
a trivalent corner star persists under placement convergence. Its sectors
already cover a small disk, so no additional tile or native vertex can
enter the limiting star. Side-interior contacts likewise cannot arise:
a native corner near such a putative contact would, in the approximants,
be an edge-to-edge corner with a complete separated star. Thus all limit
contacts remain whole native sides or common native vertices, and every
vertex has exactly three corner sectors.

This proves the first conclusion.

## 4. Double-period escape and trivalence

Apply the reviewed single-period escape lemma to the limiting tiling and T.
It gives a doubly periodic edge-to-edge F-tiling. Its cut-and-repeat proof
makes every new local neighborhood a translate of an original neighborhood,
so trivalence is retained. Alternatively, take a sufficiently large
sublattice of its period lattice so every tile embeds in the quotient torus.
Then 2E=6N and V-E+N=0 give V=2N and 2E=3V. Every degree is at least three,
so all degrees are exactly three.

## Scope and stop condition

For pairs of genuine convex hexagons, existence of any translationally
periodic unrestricted tiling is equivalent to existence of a doubly periodic
edge-to-edge trivalent tiling. The converse is immediate. Thus an unbounded
obstruction to all such tori would also exclude rank-one periodic tilings
for this side-count class, without any forced-edge-to-edge assumption.

There is no bound here on period lengths or quotient size, no passage from
a bounded torus search to an unbounded obstruction, no proof that an
arbitrary tileable pair has a period, and no proof that both species persist.
The argument uses the all-hexagon defect identity; it is not asserted for
arbitrary finite polygon sets with average side count merely at most six.
There is no computation or finite certificate to replay. The artifact is
an analytic proof, with the dependencies and pending review stated above.
