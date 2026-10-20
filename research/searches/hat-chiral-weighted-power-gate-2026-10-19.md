# Hat chirality-weighted power cells: exact small-parameter gate

2026-10-19. Exact finite-witness obstruction with [independent Sol hostile review PASS](../reviews/hat-chiral-weighted-power-sol-hostile-2026-10-19.md). This is a changed weighted mechanism, not a replay of the unweighted moving-site disk. It excludes only the fixed site and declared compact weight interval below, not the entire weighted family or the main problem.

## Exact definition and genuine source

Use the native full-size Hat, actual substitution frames and published genuine infinite hierarchy already documented and independently reviewed in `hat-voronoi-existence-gate-2026-10-19.md`. The producer reconstructs the level-3 H, its 1156 Hats and 9248 disjoint primitive kites, and all exposed actual-support boundary edges. Targets are the same certified occurrences 509, 519, 516. Each center has its closed radius-10 disk inside the finite actual support. The primary theorem dependency and source snapshots remain those of the earlier report, not a new claim that finite patches alone extend.

Fix the intrinsic reference point p=(5/8,5sqrt(3)/8). If t is the retained half-size frame, the actual full-size site is s=2t(p), including its translation; the actual full-size orthogonal linear part is twice that of t. Set chi=1 for negative determinant, 0 for positive determinant, and weight w=lambda chi. Declare lambda in [-1/4,1/4]. A relative cell coordinate z satisfies

    2(s_j-s_i) dot z <= |s_j-s_i|² + lambda(chi_i-chi_j).

The certificate retains exact target frames and endpoint relative vertices over Q(sqrt(3)). The source generator deterministically defines every neighbor frame.

The producer enumerates every ordered vertex-pair image of a fixed edge and both determinant signs, then checks equality of the full vertex set. Only the identity preserves the reference Hat. Every isometry of a polygon maps vertices to vertices, so this is exhaustive. Consequently an unmarked Hat occurrence has a unique reference frame and an unambiguous transported site and handedness. Reflected copies transport p by their actual reflected frame, rather than resetting its coordinates. Handedness is relative to a fixed orientation of the source plane. Globally reflecting the source swaps the two handednesses; for unequal weights this changes the construction (equivalently replacing lambda by -lambda and adding the irrelevant common weight lambda). This is permitted for producing one existence tiling. It is not an imposed chirality condition on a final polygon tiling.

## Weighted plane tiling and rigorous finite domain

The fixed site lies at boundary distance 5/8, so distinct source sites are separated by at least a=5/4. Every point lies at distance at most R0=sqrt(301)/4 from some source site. Both facts follow from the exact Hat boundary and vertex-distance checks replayed here, with actual reflected frames.

For any i and any j, at z=0 the j halfplane slack is at least a²-1/4=21/16>0. A uniform open disk of radius less than (a²-1/4)/(2a)=21/40 around each site belongs to its cell: (d²-1/4)/(2d) is increasing for d>0. Thus no source site loses its cell on the declared interval.

At a point x in the power cell of i, choose a source site k within R0. Power minimality gives |x-s_i|² <= R0²+w_i-w_k <= 301/16+1/4=305/16. Write C=sqrt(305)/4. Bounded weights, site separation and density imply a minimum power value is attained everywhere; the closed cells cover the plane with pairwise disjoint interiors. Every cell is a compact convex polygon with nonempty interior. Finitely many sites can affect any cell.

For d=|s_j-s_i|>=10 and |z|<=C, its slack is at least d²-2dC-1/4>0. The last inequality follows from (100-1/4)²>400 C² and monotonicity for d>=10. Thus only sites with d<10 can affect a cell. Actual radius-10 containment excludes all omitted infinite-source Hats, whose interior sites cannot lie in this finite support. The finite neighbor lists have sizes 21,23,22. The finite local polygons are separately checked to have every vertex squared radius <20; the same exclusion works for that larger radius because (100-1/4)²>400*20. Thus finite halfplane intersections equal the actual source power cells without circular reliance on the global C bound.

## Complete transition partition on the declared interval

Keep the original cyclic neighbor lists:

* 509: 507,510,516,480,523 (five sides).
* 519: 518,516,508,511,513,517 (six sides).
* 516: 509,510,508,519,518,520,480 (seven sides).

The two-line intersection determinant is constant and nonzero. Every vertex is affine in lambda. Every nonincident halfplane slack and every oriented edge length is affine in lambda. The producer checks strict positivity at both endpoints; therefore it holds throughout the entire closed interval. The squared vertex norm is convex in lambda, so its maximum is bounded by the endpoint maxima. These checks rule out all combinatorial transitions, vertex collisions, redundant listed edges and unlisted active constraints. The exact partition is one closed interval [-1/4,1/4], with side counts (5,6,7). All three witnessed cells have at least five sides, but these three cannot have at most two congruence classes, even allowing reflections. No parameter survives this declared gate.

This is a small-parameter obstruction only. It gives no global palette census or decoder. The output geometry is unmarked; chirality and weights are construction data, not additional rules for admitted output tilings. Even a future global two-shape census would still require proof that every tiling by those unmarked shapes is aperiodic.

## Assessment of the next actual events

The producer also computes every exact root of an incumbent affine slack or edge-length predicate. The closest positive root is 226/69 and closest negative root is -249/68. Exact ordering uses Q(sqrt(3)) signs, not numerical root sorting. Radius-10 exclusion remains available up to absolute weight 249/68 since (100-M)²>400(301/16+M). This identifies accessible local events; it does not enlarge the main gate. The elementary proof that every source site retains its cell only covers |lambda|<25/16, so extending the whole construction through these events requires a stronger source nonemptiness argument or an explicit treatment of disappearing sites.

Exact finite halfplane clipping samples immediately below, at and above each event are retained in the certificate. They are actual cells for those three occurrences: all sample vertices lie strictly inside squared radius 365/16, and (100-4)²>400(365/16), with sample weights of magnitude <4. These samples do not assert that every other source site remains nonempty, or that no further nearby event exists. At lambda=226/69-1/100, 226/69, 226/69+1/100 the side counts (509,519,516) are respectively (5,6,7), (5,6,6), (5,7,6): the positive event permutes six and seven away from the event itself. At lambda=-249/68-1/100, -249/68, -249/68+1/100 they are (5,5,8), (5,5,7), (5,6,7), respectively. At each exact event, the equal-sided pair has unequal exact areas (also retained), so those two parameter values still have at least three congruence classes. The negative-side sample (5,5,8) alone does not exclude a two-class palette.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hat-chiral-weighted-power-gate-2026-10-19.py

Certificate: `research/certificates/hat-chiral-weighted-power-gate-2026-10-19.json`. The script uses rational arithmetic in Q(sqrt(3)); no solver, random seed or numerical decision supplies the proof. No novelty claim is made. The independent hostile review passed. A future extension should address the explicitly identified cell-survival obligation and genuine transition cells, rather than automatically enlarging the weight interval.
