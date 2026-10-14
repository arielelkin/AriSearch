# Perimeter obstruction for polygonal parents made from hexagons

Date: 2026-10-14. Status: **independently hostile-reviewed VALID** for the
stated simple-polygon dissection and iteration domain; see the
[fresh review](../reviews/nonconvex-parent-hexagon-perimeter-bound-review.md).
This is a dissection obstruction, not a classification of plane tilings.

## Statement

Let M be a compact simple polygon with p genuine corners, possibly nonconvex.
Suppose M is the union of finitely many compact convex polygons with disjoint
interiors, each having at least six genuine sides. Let L be the largest native
side length among those children. Partial contacts and arbitrary isometries,
including reflections, are allowed. Then

    perimeter(M) <= (2p - 6) L.

Consequently, a fixed finite set of convex atomic polygons with at least six
sides cannot support arbitrarily large similar copies of any fixed simple
polygonal parent. In particular it cannot support an iterable expansive
similarity substitution with finitely many simple polygonal parent types,
each a finite patch of those fixed atoms. Nonconvex parents are included.

## Planar counting proof, including flat sectors at reflex corners

Planarize the dissection at every parent corner and every genuine child
corner. Suppress any other degree-two point. Write t for the number of
children, V_b for vertices in the relative interiors of parent sides, and
V_i for interior vertices. At a vertex v, let m(v) count incident child
sectors, INCLUDING a sector of angle pi when v is in the interior of a
child side. Set S = sum_v m(v). Let F_flat count all such flat child-sector
incidences, including those at reflex parent corners. The total number N
of native child corners satisfies

    N = S - F_flat.

The minimum sector counts are one at a parent corner, two at a V_b vertex,
and three at a V_i vertex. At a boundary point of angle pi a single flat
sector would not be a retained vertex. At an interior retained vertex two
sectors cannot cover 2pi unless both are flat, in which case there is no
genuine corner and that point was suppressed. Thus, with X >= 0 the total
excess over these minima,

    S = p + 2 V_b + 3 V_i + X.

The graph degree is m(v) + 1 on the boundary and m(v) in the interior.
Hence 2E = S + p + V_b. Euler's identity for this cell decomposition of a
disk, (p + V_b + V_i) - E + t = 1, gives

    2t = 2 + V_b + V_i + X,
    6t - N = 6 - p + V_b + 2X + F_flat.       (1)

Every child has at least six native corners, so N >= 6t. All extra terms
on the right are nonnegative, and therefore V_b <= p - 6.

The boundary is divided into p + V_b elementary segments. Each lies in a
single native child side, so has length at most L. Summing their lengths
proves perimeter(M) <= (p + V_b)L <= (2p - 6)L.

The sector convention is essential. A child can contribute a flat sector at
a reflex parent corner. Counting only native corners there and importing
the convex-parent identity unchanged would omit this case. Equation (1)
accounts for it explicitly.

## Iteration obstruction

For fixed atoms, L is fixed. For a fixed parent M, its number p of genuine
corners is invariant under similarity, but an expansion factor lambda > 1
gives perimeter(lambda^k M) = lambda^k perimeter(M), which is unbounded.
The perimeter inequality therefore prohibits atomic dissections for all k.
An iterable substitution of finitely many polygonal parents would provide
exactly those dissections, by composing the rules and then replacing the
smallest parents with their defining atomic patches. This is a contradiction.

More quantitatively, any one-generation candidate must satisfy

    lambda <= (2p - 6)L / perimeter(M).

One generation below that threshold may still exist; it cannot certify an
iterable hierarchy. No bound on the number of children was assumed.

## Scope and construction consequence

This covers simple polygonal supports, fixed finite atomic shapes, and an
expansive similarity hierarchy. It does not exclude arbitrary tilings by two
hexagons, nonpolygonal or infinitely varied parent boundaries, or other
hierarchy mechanisms. Holed or disconnected supports are not part of the
statement. The result is elementary and no novelty claim is made.

For the current finite polygonal-parent construction strategy, an atomic
pentagon is necessary once triangles and quadrilaterals have been rejected
by their known periodic omission tilings. This is a restriction on this
strategy, not a proof that every aperiodic pair must contain a pentagon.

The motivating finite two-hexagon construction census and applied adversary
checks are recorded separately. The earlier convex-parent Euler identity is
at [convex-substitution-dissection-euler.md](convex-substitution-dissection-euler.md);
the proof above supplies the extra flat-sector accounting required here.
