# Resumed source compiler: exact golden-triangle fan and periodic inheritance

Date: 2026-10-13. Status: independently adversarially reviewed VALID exclusions; These exclude specified compilers, not arbitrary convex pairs. No closed enumeration was resumed.

## Concrete compiler proposal

Use unit-side Penrose rhombs as an intermediate source. Let φ=(1+√5)/2. The thick rhomb, angles72°,108°, splits along its long diagonal into two isosceles triangles O with sides1,1,φ and distinguished apex108°. The thin rhomb, angles36°,144°, splits along its short diagonal into two isosceles triangles C with sides1,1,φ−1 and distinguished apex36°. These are exact geometry statements, with no unmarked aperiodicity asserted for triangles or rhombs.

A new two-class compiler proposal groups three such triangles around a common distinguished apex, gluing unit radial sides consecutively; the desired final atoms are strict convex pentagons. Every radial endpoint lies at distance1 from the apex. Words of length3 over{C,O}, in all orders, form the finite initial proposal domain. Reflections are allowed.

## Stable mathematical extraction

The complete exact fan exclusion, explicit periodic carrier and general periodic-inheritance theorem are extracted without duplicate proofs at research/counterexamples/resumed-golden-triangle-fan-periodic-escape.md. The same eight-word domain is analytically exhausted; this record retains the proposal and replay pointer.

## Assumption ledger and restart

Problem assumptions used: all isometries and unrestricted contacts are allowed; target omission allowed. Derived: exact golden triangle shapes, convexity fan gate, periodic carrier. Temporary proposal: same distinguished apex, unit radial sides, exactly three triangles per final atom. No universal Penrose decoder exists for this proposal; it is already falsified without needing one.

No proof-relevant numerical equality or finite-search UNSAT occurs. An exact Sage check of the coordinates, hexagon symmetry, strict convexity, positive lattice determinant and area equality is retained at research/searches/resumed-source-fan-check.py. Replay: mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed-source-fan-check.py. This is one exact witness, not an enumeration or a certificate of universal tiling classification.

Next viable change must have an explicit cross-boundary branching reassembly with final corners of at least5, no member periodic alone, and an intrinsic decoder enforcing source markings. Neither more triangle-fan words nor source-by-source rhomb cuts address the two proved failures.
