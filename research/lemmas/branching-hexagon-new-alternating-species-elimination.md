# Alternating-species elimination by trivalent corner budgets

**Status:** proved and independently hostile-reviewed VALID on 2026-10-10 for both branches; see [the fresh review](../reviews/branching-hexagon-new-alternating-species-elimination-review.md). No novelty claim. This is a new length-word obstruction, not the unrestricted two-convex-tile theorem.

## Exact theorem

Let A and B be two fixed genuine strictly convex hexagons. Let p,q,r be pairwise distinct positive lengths. Assume:

* A has alternating native side lengths p,q,p,q,p,q. Its angles are arbitrary; no threefold symmetry is required.
* B has precisely two p sides, three q sides, and one r side. Its r side has a p side at one endpoint and a q side at the other, and no two p sides are adjacent.

Equivalently, after choosing a native direction and a starting r side, the admissible B words are (r,p,q,q,p,q) and (r,p,q,p,q,q), together with their reversals and cyclic rotations. Its native corner-pair multiplicities are one rp, one rq, three pq, and one qq.

**Private-r theorem.** If A,B satisfy the hypotheses above and admit any plane tiling under the unrestricted problem conventions, B admits a monohedral plane tiling. Consequently the pair admits a periodic tiling and cannot be aperiodic.

**Binary-length theorem.** Let instead B have only p and q side lengths, while A remains any genuine strictly convex alternating p/q hexagon with p!=q. Let h be the number of native B corners whose two incident side lengths agree. If h=0, the pair admits no tiling. If h=2, any plane tiling implies a monohedral tiling by B and hence a periodic escape. Equivalently h=2 means exactly four cyclic transitions between p and q in B's six-side word. The h=4 or h=6 cases are outside this binary statement.

Reflections, partial contacts, omission of a tile type, and arbitrary fixed angles are allowed in the original tiling problem in both statements.

The key new conclusion is elimination of A in a genuine admitted limit. It does not assert that A is absent from every original tiling. It does not infer integer frequencies, surjectivity of an infinite map, or global extension of a finite patch.

## Dependencies

1. The independently reviewed [hexagon defect-free limit theorem](hexagon-limit-and-periodicity.md) supplies an admitted edge-to-edge trivalent tiling from any unrestricted tiling of the two hexagons; either type may vanish.
2. The independently reviewed compactness argument in [uniform occurrence](two-type-uniform-density.md) applies to unrestricted tilings by fixed convex polygons, including reflections and continuous orientation sets. We use it only to turn growing B-only disks into a B-only plane tiling.
3. The imported unrestricted monohedral convex-hexagon classification and periodic constructions are recorded in [hexagon limits and periodicity](hexagon-limit-and-periodicity.md): Zhu, Wang, Yan, *Hexagonal Tiling of the Plane*, arXiv:2508.01404v2, Main Theorem. Every monohedral convex hexagon tiler admits a periodic tiling. No new classification or priority claim is made here.

The finite incidence argument below is proved directly and does not require a species-frequency existence theorem.

## Private-r branch: forced r seam and exhaustive length-star types

Take an admitted edge-to-edge trivalent limit tiling. Its side lengths are the distinct lengths p,q,r. A has only pq corners. B has the corner pairs rp,rq,pq,pq,pq,qq; neither tile has pp.

Every r side must match the unique native r side of another B. Of the two placements matching a fixed whole side across its line, the reflected same-slot placement preserves its endpoints and gives two rp corners at the p endpoint. Their remaining p rays must meet, so the third sector would need a pp corner. This is absent. The r mate is therefore the half-turn about the seam midpoint, exchanging its endpoints.

At each r seam endpoint the two B sectors have pairs rp and rq. The third sector has pair pq, and may belong to A or B. Thus every r vertex contains precisely one rp corner, one rq corner, and one pq corner. No second r ray can occur there because no corner has rr. Every B contributes its two r-adjacent corners to these vertices.

A vertex with no r ray has only pq and qq sectors. The number of p incidences among the sectors must be even: every p ray borders two sectors. There are three sectors and no pp corner, so the number of pq sectors is zero or two. The complete list of non-r length stars is therefore

    (pq,pq,qq), or (qq,qq,qq).

This uses no angle equation or chirality assumption.

## Uniform finite-window count

Choose each tile center to be its vertex average. Let N_A(R,x),N_B(R,x) count these centers in Q_R(x)=x+[-R,R]^2. Let J(R,x) count r vertices in that square; let X(R,x) and Y(R,x) count non-r vertices of the two displayed star types, respectively.

All incidence discrepancies in the following equations are bounded by C R for a common constant C depending only on the two fixed shapes, uniformly in square center x and R>=1. To justify this, let D bound tile diameters and a>0 be their minimum area. A tile whose center and a counted corner lie on different sides of the square boundary intersects its width-D boundary strip, and the whole tile lies in the width-2D strip. This strip has area O(R); disjoint tile interiors and minimum area bound such tiles by O(R). Each contributes at most six native corners. Every counted vertex discrepancy is incident to one of these tiles, so it obeys the same bound. This proof applies when a type is omitted as well.

Count the r-adjacent native corners. Every B has two and every r vertex has two, so

    2 J = 2 N_B + O(R), hence J = N_B + O(R).          (1)

Count pq corners. A has six and B has three; each r vertex consumes one, each X vertex consumes two, and each Y vertex consumes zero:

    J + 2 X = 6 N_A + 3 N_B + O(R).                  (2)

Count qq corners. B has one and A has none; X consumes one and Y consumes three:

    X + 3 Y = N_B + O(R).                            (3)

Eliminating J and X from (1)--(3) yields

    6 N_A + 6 Y = O(R).                              (4)

Here O(R) denotes an error with absolute value at most a uniform constant times R, so nonnegativity gives

    N_A(R,x) <= C' R                                 (5)

for a fixed C'. This is a genuine boundary bound, not merely a subsequential zero frequency. In particular all translations obey it. Tiles intersecting a square have centers within its D-enlargement, so the same linear estimate holds for the number of A tiles meeting any radius-R disk or side-2R square.

The impossible A-only trivalent limit is already covered by this estimate: coverage by A alone would give a quadratic number of A tiles, contradicting (5). Directly, a three-sector all-pq vertex would require an odd three-ray cycle alternating distinct p and q. A B-only limit is permitted and immediately gives the theorem's first conclusion.

## From sparse A tiles to a B-only admitted plane tiling

For completeness, fix an integer n and choose R much larger than (n+D)^2. Only O(R) A tiles meet Q_R(0), by (5). Their centers lie in Q_(R+D)(0). Within an inner square of side proportional to R, the union of disks of radius n+D about those centers has area O((n+D)^2 R), strictly less than the inner square's area for sufficiently large R. Choose a point z outside this union and at distance at least n+D from the boundary of Q_R(0).

No A tile meets B(z,n). An A tile intersecting this disk would meet Q_R(0), and its center would lie within n+D of z, contrary to the choice of z. Hence B(z,n) is covered exclusively by B tiles.

Translate z to the origin and let n tend to infinity. The reviewed fixed-polygon compactness proof gives an admitted plane-tiling subsequential limit. In that proof every occurrence is represented by its type, an interior anchor, and an orthogonal matrix; the anchor separation and bounded tile diameters uniformly bound occurrences on compact sets. Diagonal placement limits retain coverage and interior disjointness, and the growing A-free disks ensure no limit occurrence is of type A. Thus the resulting plane tiling is monohedral by B.

By the recorded unrestricted monohedral hexagon classification and periodic constructions, B consequently admits a periodic monohedral tiling. This tiling is admitted by the original pair, which allows omission of A. The asserted periodic escape follows.

## Binary-length branch: at least one homogeneous corner per star

Call a pp or qq corner homogeneous. A has none, and B has h. In an admitted trivalent edge-to-edge limit, each vertex has three rays, each of length p or q. If all three sectors were pq, consecutive rays would alternate p and q around an odd cycle, impossible. Every vertex therefore consumes at least one homogeneous B corner.

Let V(R,x) count geometric vertices in Q_R(x), and use the same tile center convention and uniform boundary-incidence estimate as above. Each tile has six native corners and each vertex has three sectors, so

    3 V = 6(N_A+N_B)+O(R).

The total number of available homogeneous corners in that square is h N_B+O(R), hence

    V <= h N_B+O(R).

Combining these equations gives the direct finite-window inequality

    2 N_A+(2-h) N_B <= O(R),                          (6)

uniformly in square center and R>=1.

If h=0, (6) bounds the total tile count by O(R). Plane coverage contradicts this: if M bounds tile area and D tile diameter, Q_(R-D)(x) is covered by tiles centered in Q_R(x), so N_A+N_B>=4(R-D)^2/M. Thus no trivalent limit and consequently no original unrestricted tiling exists. This includes omission of either type.

If h=2, (6) gives N_A=O(R). The growing A-free disk and compactness argument already written above yields a B-only admitted plane tiling, and the recorded monohedral classification supplies a periodic escape. A B-only initial limit is allowed and yields the conclusion immediately. An A-only initial limit contradicts the same bound.

The number of cyclic p/q transitions is even. Since B has six sides, h is one of 0,2,4,6, including constant-length words in h=6. Thus the hypothesis is an exhaustive finite side-word condition, not an angle genericity assumption. No oriented or marked edge rule is imposed.

## Scope and restart boundary

The private-r branch eliminates both stated three-length B words for every exact convex metric. The binary branch eliminates every B p/q word having four or six cyclic transitions. Both allow repeated angles, arbitrary A angles, reflected copies, and partial contacts in the original tiling. No computational component is used.

The corner count depends on B having exactly one qq corner, three pq corners, and one of each r-adjacent mixed corner, while A has only pq corners. Changing these multiplicities, allowing pp corners, identifying p with q or r, or replacing the two-hexagon defect-free-limit hypothesis requires a different argument. In particular this does not classify B=(r,p,q,q,q,q), which has three qq corners and is covered by a separate more geometric result only for threefold A. The binary branch leaves B words with exactly two transitions (one p run and one q run), and constant-length B words, unclassified by its corner budget. The unrestricted original target remains unresolved.
