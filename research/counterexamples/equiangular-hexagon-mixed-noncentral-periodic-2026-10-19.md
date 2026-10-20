# A noncentral equiangular hexagon in an exact periodic mixed tiling

This example refutes the inference that an equiangular 120° hexagon occurring in a mixed tiling must itself be centrally symmetric. It also supplies a periodic escape for its two-shape pair, so it is **not** an aperiodic-pair candidate.

Let `u_k=(cos(kπ/3),sin(kπ/3))` and take triangular-lattice sites `c_(i,j)=2i u_0+2j u_1`. Assign weight one when `i−j≡0 (mod 3)` and zero otherwise. The Euclidean power cell at site c is the set where `|x−c|²−w_c` is minimal over all sites. At a weight-one site its six nearest-site inequalities are `y·u_k≤5/4`, giving a regular hexagon B. At a weight-zero site they have alternating bounds `3/4,1`, giving a strictly convex equiangular hexagon A. The two zero-residue site environments give congruent rotations of A.

These nearest-site bounds are complete. Every candidate cell lies within radius `5/(2√3)` of its site. Every non-nearest lattice site has distance `D≥2√3`, and even under the worst weight difference its bisector is at distance at least `(D²−1)/(2D)≥11/(4√3)>5/(2√3)`. Hence no farther inequality cuts a cell. Power cells cover the plane and have disjoint interiors by the bounded-weight nearest-site rule.

The alternating side lengths of A are `5/(2√3),1/√3,5/(2√3),1/√3,5/(2√3),1/√3`; opposite sides differ, so A is not centrally symmetric. B is regular. The weight field has independent physical periods `(3,√3)` and `(6,0)`, so the pair has an explicit rank-two periodic tiling; B alone also tiles periodically.

The [full structural and geometric proof](../searches/two-equiangular-hexagons-sol-2026-10-19.md) and [independent Sol hostile review](../reviews/two-equiangular-hexagons-hostile-sol-2026-10-19.md) establish the scope. No conclusion follows for a pair in which both hexagons are noncentral.
