# Penrose two-weight center rule: complementary tail gate

Date: 2026-10-19. Status: exact producer checks and [independent Sol hostile review](../reviews/penrose-weighted-center-tail-gate-hostile-sol-2026-10-19.md) passed. The fixed weighted rule remains unclassified on an exact negative-parameter gap.

## 1. Source and scope

Use precisely the reviewed 430-rhomb genuine infinite substitution source and collar construction in [the unweighted gate](penrose-center-voronoi-quadrilateral-2026-10-19.md), its [hostile review](../reviews/penrose-center-voronoi-sol-review-2026-10-19.md), and [the weighted first gate](penrose-weighted-center-first-gate-sol-2026-10-19.md) with its [review](../reviews/penrose-weighted-center-first-gate-hostile-sol-2026-10-19.md). The source dependency is the standard Robinson/Penrose base-pairing property already disclosed there. The producer reconstructs the 890 triangles, exact T1 subset T5 nesting, opposite-apex same-color pairs, unit rhomb sides and outer unmatched bases. No patch enlargement occurs.

Thin weight is zero; thick weight is delta, and power is squared distance minus weight. Set phi=(1+sqrt(5))/2. All coordinates are exact in Q(phi), using z=x+i sin(36 degrees)y and metric x²+((3-phi)/4)y². The implementation computes in the equivalent cyclotomic representation and verifies all exported real pairs exactly.

## 2. Two fixed same-type quadrilaterals

The search orders centers of each type by exact squared distance to the origin, breaking ties by index, and stops at the first strict quadrilateral. The first thick candidate is index 25; the first thin candidate is index 26. Both succeed. There are no subsequent scans. Each cell is clipped against every retained center of its own type starting from a large parallelogram; every final side is independently checked to lie on a genuine same-type bisector, so no initial bounding side survives. All cyclic turns are positive and all vertices satisfy every same-type inequality. Thus each is the entire finite same-type Voronoi cell, rather than merely an inscribed feasible polygon.

| Type / index | Four cyclic supports | Maximum squared vertex radius R² | Squared boundary clearance M |
|---|---|---|---|
| thick / 25 | 24,70,328,413 | 11(1+phi)/36 | 93/4+149phi/4 |
| thin / 26 | 29,72,116,374 | 1/2+3phi/4 | 41/2+129phi/4 |

Exact cyclic vertices, centers, limiting pairs and finite search record are retained in the matching JSON. Positivity of turns establishes four positive-length sides, including the parameter endpoints below, because the same-type polygons are fixed.

## 3. Exact opposite-type thresholds and weight sign

For a fixed polygon point v relative to center c and another center q, write d=q-c. Its power inequality is

    2 d dot v <= |d|² + weight(c)-weight(q).

For a thick selected center and thin q, the weight difference is +delta; for a thin selected center and thick q it is -delta. The maximum of 2 d dot v-|d|² over all polygon vertices and all retained opposite-type centers is respectively

    thick: 1/4+phi/3,
    thin: 21/44+9phi/22.

These are exact maxima of finitely many affine functions of v, with all maximizers retained. Consequently the thick polygon is unchanged for delta >= 1/4+phi/3, and the thin polygon is unchanged for delta <= -21/44-9phi/22. The endpoints are included: opposite-type constraints touch vertices only and do not remove any existing polygon side. Because the polygons already equal their same-type halfplane intersections, feasibility against all opposite-type inequalities proves equality with the full cell.

## 4. Uniform infinite-tail completeness

Let U be the union of the same 430 complete source rhombs. The exact minimum distance squared M from c to all exposed perimeter segments is recorded above. Since c is interior to its retained rhomb, B(c,sqrt(M)) lies in U. Every omitted genuine source center is interior to an omitted rhomb and hence has D=|q-c|>=sqrt(M). Each certificate checks M>4R² exactly. Thus for every point v in the fixed convex polygon,

    D²-2 d dot v >= D(D-2|v|) >= D(D-2R) > 0.

This proves completeness of each same-type polygon against all omitted same-type centers. On the thick positive half-line, omitted thin constraints add delta>=0 to this strictly positive geometric slack. On the thin negative half-line, omitted thick constraints add -delta>=0. These signs make the proof uniform for unbounded parameters; no bound on |delta| is used. All retained opposite-type constraints were checked exactly at the worst threshold. Hence both claimed half-lines certify actual complete infinite-source cells.

## 5. Coverage and stop

The independently reviewed central certificate covers [-1/4,1/4+phi/3). The new thick half-line begins at its excluded upper endpoint and includes that endpoint, so together they cover [-1/4,infinity). The new thin half-line covers (-infinity,-21/44-9phi/22]. The exact remaining open gap is

    (-21/44-9phi/22, -1/4).

This gap has length 5/22+9phi/22>0. Neither endpoint is a remaining gap: both have complete strict quadrilateral witnesses. No assertion of absence of other witnesses in the gap follows. Per the bounded gate instruction, no further site scan or patch enlargement was performed.

Every certified strict convex quadrilateral tiles periodically by itself. Therefore any proposed two-shape protoset containing every output class of this fixed weighted rule fails unrestricted aperiodicity for all covered parameters. This excludes neither the parameters in the stated gap nor arbitrary weighted rules, context-dependent duals, or arbitrary dual constructions. No all-real exclusion or solution of the main research problem is claimed.

Replay from repository root:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-weighted-center-tail-gate-sol-2026-10-19.py --check

There is no randomness, floating geometry, solver, timeout or congruence census. Exact AA comparisons select the specified real embedding. Only the two first candidates were examined, all same-type constraints and all opposite-type vertex inequalities were checked, and all exposed source boundary segments were used for the tail certificate. No git or log files were edited.
