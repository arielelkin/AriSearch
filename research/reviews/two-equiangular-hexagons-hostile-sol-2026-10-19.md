# Independent hostile review: two equiangular hexagons

Date: 2026-10-19. Target: `research/searches/two-equiangular-hexagons-sol-2026-10-19.md`.

## Verdict

**PASS for the structural reduction and explicit mixed periodic example. General two-hexagon periodicity remains unresolved.** I found no counterexample to the claimed reductions or error in the exact construction. The monohedral classification citation was not independently audited here; it is unnecessary for the structural and constructive results reviewed below.

## Edge contacts and topology

The local-finiteness argument works for any fixed finite collection of compact positive-area polygon types: the inscribed disks can be chosen uniformly positive and their centers stay within a bounded distance of any intersected compact set. Thus infinitely many arbitrarily small incidental contacts cannot evade the angle argument.

At a point in the relative interior of a tile side, that tile contributes 180 degrees. A corner of another tile contributes 120 degrees, leaving 60 degrees, which cannot be filled by any further side interior or corner. At a genuine tiling vertex, all contributions are consequently 120 degrees and there are exactly three. A proper overlap of collinear native sides has an endpoint interior to at least one side, so is excluded. This establishes edge-to-edge contacts, including under reflections.

The cellular dual really is a triangulation of a topological plane: primal vertices have degree three and primal faces have six sides. Convexity excludes two distinct tiles sharing separated native edges and excludes self-incidence. The dual unit equilateral metric has six triangles per vertex, with no cone singularities. Its completeness does require the uniform unit-triangle geometry, which the report explicitly supplies; bounded degree alone for arbitrary triangle metrics would not suffice. Here bounded graph balls are finite and the uniform triangulation compares intrinsic distance to graph distance. Thus the stated completeness argument is sound. A complete simply connected flat plane develops isometrically onto the Euclidean plane, forcing the ordinary triangular tessellation and abstract honeycomb dual. No periodicity of the original metric embedding follows.

## Common directions with reflections

A strictly convex 120-degree hexagon turns by 60 degrees on each successive boundary edge. Its three unoriented directions are therefore fixed by any one edge direction. A neighboring reflected copy still has precisely that same set of three directions, since reversing the cyclic order changes the sign of the turn but not this set. Connectivity propagates the direction set globally. The outgoing 120-degree stars and alternating vertex classes follow. This does not imply complete straight edge lines or arithmetic spacing of their supporting lines.

## Exact weighted-lattice construction

For lattice displacement `2*u_k`, expanding the power comparison gives exactly

    y dot u_k <= 1 + (w_c-w_neighbor)/4.

The six residue increments of `i-j` are alternately +1 and -1 modulo three. Thus a residue-zero (weight-one) site has six bounds 5/4. A weight-zero site has alternating bounds 3/4 and 1; the other zero-weight residue reverses the alternation and is a 60-degree rotation. Translation of the site itself has no effect on congruence.

I independently solved the six pairs of consecutive support equations in SymPy and checked all 36 support incidences for each representative. For A, with even-index support 3/4, the successive vertices are

    (3/4, 5*sqrt(3)/12), (1/4, 7*sqrt(3)/12),
    (-1, sqrt(3)/6), (-1, -sqrt(3)/6),
    (1/4, -7*sqrt(3)/12), (3/4, -5*sqrt(3)/12).

The side lengths are alternately `5*sqrt(3)/6` and `sqrt(3)/3`, exactly the displayed L and S. B has all six side lengths `5*sqrt(3)/6`. All are strictly positive, so all six support constraints are active and every angle is 120 degrees. Opposite A sides have unequal lengths, excluding central symmetry.

The non-neighbor exclusion is valid for every lattice site, not merely a checked finite subset. The next possible lattice distance is `2*sqrt(3)`. The function `(D^2-1)/(2*D)` is increasing for positive D, so its lower bound is `11/(4*sqrt(3))`. Every six-constraint candidate lies inside the regular support hexagon of inradius 5/4 and hence inside radius `5/(2*sqrt(3))`. The strict clearance is `sqrt(3)/12`. Consequently no further power inequality clips a candidate. Bounded weights and lattice discreteness ensure the power minimum exists everywhere, so these full cells cover the plane with disjoint interiors.

There are exactly two congruence classes: the two A residue classes are rotated copies, and B is regular whereas A has unequal side lengths. The active neighbors of any site are its six triangular-lattice neighbors. Consecutive such neighbors and the original site form an elementary lattice triangle with all three residues; hence every cell vertex has an AAB star, with no hidden fourth incident cell.

The index shifts `(1,1)` and `(3,0)` preserve the residue and give the asserted physical periods `(3,sqrt(3))` and `(6,0)`. Their determinant has nonzero absolute value `6*sqrt(3)` and their index sublattice has index three, so a fundamental quotient contains one B and two A cells. The construction is genuinely mixed and has rank-two translation symmetry.

## Scope and remaining obligation

The example refutes only the assertion that each occurring hexagon must be centrally symmetric. It contains a regular B that alone tiles the plane, which is an allowed omission escape. It is neither a pair of two noncentral hexagons nor evidence against periodic escape. Conversely, abstract honeycomb connectivity and common directions do not establish periodic escape for an arbitrary mixed pair. The report preserves these distinctions and leaves the required global metric theorem open.

Verification used an independent exact SymPy calculation under the prescribed environment wrapper. No source report, Git state, or logs were edited.
