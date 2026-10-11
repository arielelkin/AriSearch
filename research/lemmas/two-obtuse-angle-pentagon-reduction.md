# Two obtuse angle values in a pentagon-containing pair

**Status:** adversarially reviewed; [fresh review](../reviews/two-obtuse-angle-pentagon-review.md) valid. This is a restricted-family necessary condition, not a solution of the original problem.

## Definitions and claim

Angles are genuine interior angles. Let P be a convex pentagon and Q a convex n-gon, n >= 5. Suppose every angle of both polygons belongs to {alpha,beta}, where pi/2 < alpha < beta < pi. Reflections, all rotations, and partial-edge contacts are permitted initially.

If a plane tiling by {P,Q} contains a P-tile, then the angle data have one of the following forms. Multiplicities, rather than cyclic order, are recorded.

| alpha/pi | beta/pi | corners of P | possible n | number of alpha corners of Q |
|---|---|---|---|---|
| 3/5 | 7/10 | five alpha | 5,6 | 20-3n |
| 4/7 | 5/7 | four alpha, one beta | 5,6,7 | 14-2n |
| 3/5 | 4/5 | five alpha | 5,6,7,8,9,10 | 10-n |

The other n minus that many Q-corners are beta. The n=9 and n=10 cases in the last row admit no plane tiling. The n=9 exclusion is the subsequent independently reviewed [neighbour-count obstruction](obtuse-pentagon-nonagon-neighbour-obstruction.md). The n=5 cases admit no plane tiling. The n=6 cases cannot be aperiodic, by the defect-free hexagon limit and imported unrestricted monohedral hexagon theorem cited below.

Consequently an aperiodic pair within this two-angle, all-obtuse family must have one of exactly these angle signatures:

* P: five 3pi/5 corners; Q: an n-gon, n in {7,8}, with 10-n corners of 3pi/5 and 2n-10 corners of 4pi/5;
* P: four 4pi/7 corners and one 5pi/7 corner; Q: a heptagon with seven 5pi/7 corners.

No assertion is made that any of these signatures closes with positive side lengths, admits a tiling, or forces nonperiodicity.

## Proof of the angle table

The all-obtuse forcing theorem [obtuse-edge-forcing.md](obtuse-edge-forcing.md) gives edge-to-edge contacts and exactly three corners at each vertex. Thus a vertex contains p alpha corners and 3-p beta corners, for some p in {0,1,2,3}, and

    p alpha + (3-p) beta = 2pi.                       (1)

Two different values of p cannot satisfy (1), because subtraction would imply alpha=beta. Every vertex therefore has the same p. If p=0 or p=3, every present tile has all its angles equal to 2pi/3. Such a tile has exactly six sides by its angle sum, so it cannot be P. Since a P-tile occurs, p is 1 or 2, and both angle values occur in the tiling.

Put x=alpha/pi and y=beta/pi, and let k in {0,...,5} count the alpha corners of P. The pentagon angle sum and (1) give

    k x + (5-k)y = 3,
    p x + (3-p)y = 2.                                (2)

For p=1, eliminate y to obtain

    (3k-5)x = 2k-4,  y=1-x/2.

The strict inequalities 1/2 < x < y < 1 select exactly k=4, x=4/7, y=5/7 and k=5, x=3/5, y=7/10. The six k-values give respectively x=4/5,1,0,1/2,4/7,3/5; the first four fail the strict inequalities.

For p=2, elimination gives

    (3k-10)x = 2k-7,  y=2-2x.

The six k-values give x=7/10,5/7,3/4,1,1/2,3/5. Only k=5 satisfies the strict inequalities, yielding x=3/5,y=4/5.

If l is the number of alpha corners of Q, its angle sum is

    l x + (n-l)y = n-2.                              (3)

Substitution of the three surviving values yields respectively l=20-3n, l=14-2n, and l=10-n. Requiring 0 <= l <= n and n>=5 yields exactly the displayed n-ranges. This step is an elementary inequality for arbitrary n, not an extrapolation from a bounded search.

## Odd-face obstruction in the n=10 case

Here P is equiangular with angle 3pi/5 and Q equiangular with angle 4pi/5. Every tiling vertex must contain two P-tiles and one Q-tile. At a vertex of any P-tile, its two full-edge neighbours therefore have different types: one P and one Q. Along its five successive edges the neighbour types must alternate. Alternation around an odd cycle is impossible. Convexity ensures each full edge has one neighbour, and the all-obtuse theorem already excluded subdivisions. Hence no such tiling exists. This argument uses neither equality of side lengths nor a chosen orientation.

## Subsequent nonagon exclusion

The angle equations alone retain n=9, but the separately reviewed [pentagon–nonagon obstruction](obtuse-pentagon-nonagon-neighbour-obstruction.md) excludes it for arbitrary side lengths. Every P has at least three Q side neighbours, every Q at most eight P side neighbours, and corner counts force N_P=3N_Q+O(R). Double counting gives9N_Q<=8N_Q+O(R), contradicting quadratic tile growth. The retained angle-table certificate continues to record the raw angle-compatible row n=9; it does not claim that row is tileable.

## Other exclusions and imported scope

For n=5 the all-obtuse forcing theorem gives an edge-to-edge trivalent tiling by pentagons. The square-window side-count identity would give N=O(R), contradicting N=Omega(R^2). This is the established all-obtuse (5,5) exclusion.

For n=6 the same boundary identity gives only O(R) pentagons in any translated square of radius R. The sparse-type compactness lemma in [hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md) therefore produces a monohedral Q-tiling. That file states the external theorem used to turn it into a periodic Q-tiling: Zhu, Wang, Yan, *Hexagonal Tiling of the Plane*, arXiv:2508.01404v2, Main Theorem, including reflections and unrestricted contacts. The new angle table does not independently prove that classification. The pair then admits a periodic tiling using Q alone.

If a tiling of the original pair contains no P, it is a monohedral Q-tiling. For n>6 this contradicts the global side-count theorem; for n=6 it gives the same periodic escape. For n=5 an all-obtuse monohedral pentagon tiling is impossible. Thus this omission does not add an aperiodic case.

## Dependencies, computation, and non-consequences

The elementary angle classification and odd-face obstruction depend only on the all-obtuse forcing theorem and convexity. The reduction from the table to the three putative aperiodic signatures additionally uses the established square-window bound, sparse-type compactness, and the explicitly imported monohedral hexagon classification.

[Two-angle enumeration](../searches/two_obtuse_angle_pentagon.py) emits an exact rational certificate for the twelve pairs (p,k) in {1,2} x {0,...,5}, plus the finite face rows n in {5,...,10}. The displayed symbolic inequalities prove the upper bound, so the finite n-domain is not assumed to cover arbitrary polygons without justification. [The certificate](../certificates/two_obtuse_angle_pentagon.json) and [independent verifier](../reviews/verify_two_obtuse_angle_pentagon.py) are retained. Replay instructions are in [the search record](../searches/two-obtuse-angle-pentagon.md).

Angle signatures omit cyclic order, metric closure, side-length equality, and both-endpoint compatibility. They are necessary conditions only. In particular, the four surviving signatures are not exact tile candidates.
