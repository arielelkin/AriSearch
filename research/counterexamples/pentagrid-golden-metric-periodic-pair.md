# Two pentagons with golden side lengths still admit a periodic tiling

**Status:** exact counterexample, independently reviewed as valid in the
[fresh audit](../reviews/pentagrid-golden-periodic-review.md). This rejects one concrete instance of the pentagrid/golden metric avenue. It does not exclude arbitrary pairs in that avenue.

## Exact shapes and periods

Work in the complex plane. Let z be the unique root of

    z^4-z^3+z^2-z+1=0, Im(z)>0, 4/5<Re(z)<81/100.

Thus z=exp(pi*i/5). Set phi=z+z^(-1)=(1+sqrt(5))/2. Define the counterclockwise pentagons

    U = [0, phi^3, z+z^2+z^3, z^2+z^3, z^3],
    W = [0, 1, 1+z^2, z+z^3, z^3].

U has side lengths (phi^3,phi^3,1,1,1) and angles, recorded at the vertex after each side,

    (pi/5,3pi/5,4pi/5,4pi/5,3pi/5).

W is the regular unit pentagon, with all angles 3pi/5. Both are genuine convex pentagons. The exact closure and strict supporting-side inequalities are checked in [the metric search](../searches/pentagrid-golden-metric.py) and [its certificate](../certificates/pentagrid-golden-metric-closure.json). The two classes are distinct by their angles. In particular the example has only pentagrid angles and its distinct lengths have irrational ratio phi^3.

Put

    u = z+z^2+z^3,
    v = 4-z+z^2-5z^3,
    Lambda = Z*u+Z*v.

For every lattice vector t in Lambda take the four tiles

    U+t,
    -U+phi^3+t,
    z*W+z^2+z^3+t,
    z^2*W+z^3+t.                                  (1)

They tile the entire plane. Consequently this pair is not aperiodic, whether or not either shape tiles alone. The individual monohedral question for U is not inferred from the periodic mixed witness; an independently audited pentagon-classification argument is needed for that stronger observation. W alone is untileable directly: neither an integer number of 3pi/5 corners sums to pi nor to 2pi.

## Direct exact coverage proof

For complex a,b define C(a,b)=(conjugate(a)*b-a*conjugate(b))/(z-conjugate(z)). This is the oriented cross product divided by sin(pi/5). Thus C(u,v)=-(8+12phi)<0, proving that u and v are independent. The area of U divided by sin(pi/5) is (7+9phi)/2, and that of W is (1+3phi)/2. Hence the sum of the four tile areas in (1) is exactly the lattice cell area:

    2 area(U)+2 area(W) = (8+12phi)*sin(pi/5) = abs(cross(u,v)).

For each placed polygon compute the minimum and maximum of its two lattice coordinates

    a(p)=C(p,v)/C(u,v), b(p)=C(u,p)/C(u,v).

All extrema are exact real algebraic numbers. If placed polygons P_i and P_j+m*u+n*v meet, then

    ceil(min a(P_i)-max a(P_j)) <= m <= floor(max a(P_i)-min a(P_j)),
    ceil(min b(P_i)-max b(P_j)) <= n <= floor(max b(P_i)-min b(P_j)).

These complete bounds leave 38 ordered, nonidentity shift tests. [The placement checker](../searches/pentagrid-golden-metric-periodic.py) checks all of them using the separating-axis theorem: for each test it finds an edge of one polygon with every vertex of the other in its closed exterior half-plane. The exact field identities, period vectors, placements, and full list of tested shifts are retained in [the placement certificate](../certificates/pentagrid-golden-metric-periodic.json). Thus all interiors in (1) are pairwise disjoint. No approximate equality or fixed unproved shift cutoff is used.

Integrate the periodic coverage multiplicity over one fundamental parallelogram. Pairwise disjoint interiors give multiplicity at most one almost everywhere; the area identity gives integral equal to the cell area, so multiplicity is one almost everywhere. The union is closed because this finite collection of compact polygons and its lattice translates is locally finite. Any uncovered point would therefore have an uncovered open neighborhood of positive area, a contradiction. This proves full-plane coverage and two independent translational periods.

The first implementation compared a number-field expression directly with its AA image and rejected a true area identity. This coercion/comparison failure was repaired by comparing the two signed expressions in the same number field. No mathematical placement changed. The corrected checker passes all 38 tests.

## Independent combinatorial witness

The metric search first found this witness as a four-face flat torus. Label the two U faces 0,1 and the two W faces 2,3. Side j goes from vertex j to vertex j+1 modulo5. Glue each listed pair by reversing endpoints:

    (0,0)-(1,0), (0,1)-(1,1), (0,2)-(2,0), (0,3)-(3,0),
    (0,4)-(2,1), (1,2)-(3,2), (1,3)-(2,3), (1,4)-(3,3),
    (2,2)-(3,4), (2,4)-(3,1).

Every side is used once and only equal lengths are paired. All faces are unreflected, all boundaries oriented counterclockwise, and the side identifications reverse boundary directions. The six corner-link components are

    [(0,1),(1,0),(1,2),(3,3)],
    [(0,0),(0,2),(1,1),(2,1)],
    [(0,3),(2,0),(3,1)],
    [(0,4),(2,2),(3,0)],
    [(1,3),(2,4),(3,2)],
    [(1,4),(2,3),(3,4)].

The first two have angle signature (1,3,3,3); the other four have (4,3,3), in units pi/5. Every sum is 2pi. Each link is a circle, the face-adjacency graph is connected, and V-E+F=6-10+4=0. These checks independently explain the flat quotient behind (1). Unfolding along a spanning tree gives the four frames in (1); every remaining seam has identity rotational holonomy and translation 0, u, -u, v, or u+v. The direct separation-and-area argument above supplies full coverage without assuming that an arbitrary locally legal patch extends.

## Replay and scope

Run all commands in the repository environment:

    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric.py
    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-torus.py
    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-periodic.py

The finite search domain and incomplete-versus-complete statuses are recorded in [the metric search record](../searches/pentagrid-golden-metric-search.md). Bounded failure on the eleven other metric fixtures does not exclude a plane tiling or imply aperiodicity. This example specifically disproves the proposed inference that irrational golden lengths require nonperiodicity, even within convex pentagon pairs whose angles are multiples of pi/5. No novelty assertion is made.
