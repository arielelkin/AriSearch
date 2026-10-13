# Adjacent-pair A002112: periodic binary lift when AAA is unused

Date:2026-10-13. [Fresh independent hostile review VALID](../reviews/five-one-adjacent-pair-no-aaa-binary-row-fresh-hostile-review.md), with two independent native checkers. Conditional actual-field theorem, not full A002112 coverage.

## Statement and dependencies

Use the reviewed B5+1 family x in(112.5,126),x!=120,y=720-5x,z=4x-360,r=360-2x,s=360-2y. Actual strictly convex A has native angle word002112 in x,y,z; actual B has native(s,r,r,r,r,r). Suppose an actual defect-free trivalent field is mixed, every B has two B neighbours, and AAA vertices are UNUSED. Then the actual pair admits a periodic tiling, with every metric equality specialization allowed.

Dependencies: reviewed saturation palette, honeycomb indexing and actual metric development, and [periodic binary equality fibre lifting](periodic-binary-equality-fibre-lifting.md). No geometric row periodicity is assumed. Partial-contact original tilings enter only if the separately reviewed saturation extraction and the unusedAAA hypothesis supply this field.

## Opposite private seams force alternating rows

A endpoint palettes include00,02,12,11,12,02, so only B middle maskBB{1,4} is possible. Its four AB palettes are02/12. Thus A native sides0(00) and3(11) are AA. With noAAA, every A0/A1 corner has exactly one AA arm and every A2 has none, so these are precisely its two AA sides. They are opposite.

Each A component in the triangular cell lattice is a full straight primitive lattice line. Different direction lines intersect at an integer cell (determinants absolute1), incompatible with exact A degree2; all A lines therefore are parallel. Choose their directionD0=(1,0). Entire rows are A or B. Adjacent A rows violate A degree2; adjacent B rows violate saturated B degree2. Rows alternate.

## Native phases form a fixed periodic base

Let phase0 of an A cell mean its rightD0 AA side is native0, phase1 mean native3. Across each AA seam both endpoints have the same A colour; an00 side cannot match an11 side in the exact AAB language. Hence phases alternate along every A row. At each phase exactly two A placements remain:

    phase0:(1,+),(0,-); phase1:(4,+),(3,-).

Within each pair all six native ANGLE profiles coincide, while side lengths may differ. Thus chirality is the sole binary variable per A cell.

B has four middle-mask row states. Define its phase0 when its special s corner is global slot1 (upper AAB vertex), and phase1 when it is slot4 (lower):

    phase0:(1,-),(5,+); phase1:(4,-),(2,+).

Both states at each phase have the same six angles. The upper two A cells sit at D1,D2 and their AA seam uses the opposite phase to that of the upper A cell at columni; the lower cells at D4,D5 use the lower row's phase at columni. The upper AAB vertex must be y/y exactly when the lower is x/x, or conversely, because B has one s and one remaining AABr corner. This forces the adjacent A rows to have the SAME phase at every common column. B's phase is that common phase. This does not depend on chirality or metric equalities.

Consequently the whole species/phase base has periods2D0 and2D1. A global column shift normalizes the one initial phase. The [independent native checker](../reviews/verify_five_one_adjacent_pair_binary_rows.py) verifies all1024 phase/chirality wheel assignments directly from corner indexing, including the exclusion of unequal adjacent row phases.

## Every remaining seam is a binary equality fibre

Put one binary chirality variable at every A/B cell of this fixed periodic base. All angle constraints hold identically for every binary choice; AA side indices also agree irrespective of chirality. Each other seam requires equality of two lengths, each of which is a function of ONE binary variable with two fixed possible values from the actual polygon.

Equality of two binary-valued functions gives only: no restriction, contradiction, a pin on one variable, pins on both, equality, or inequality between the two variables. To prove this, if both functions take distinct values the allowed relation is a matching with at most two pairs; if one is constant it is a row/column relation; if both are constant it is all or empty. The independent checker also enumerates all256 four-value assignments, which include every Bell4 equality type. This preserves all degenerate length merges; no generic distinct-side assumption enters.

The complete metric constraint system is therefore a periodic network of signed binary equalities and pins. It has a solution, supplied by the assumed actual field. The reviewed binary-fibre theorem provides a finite periodic cover carrying a solution. Its full native labels give a periodic honeycomb field, and the reviewed actual metric development supplies a Euclidean plane tiling with nonzero translational symmetry (possibly after squaring a glide).

This re-develops the periodic field; it does not claim selected polygons can be reinserted at the old geometric coordinates. No finite patch was promoted to global existence: existence is an input, and the fibre theorem supplies the periodic extension.

## Replay and remaining obligation

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_adjacent_pair_binary_rows.py

Finite domain: four A/four B row states,1024 wheel phase/chirality assignments and256 scalar equality patterns. No solver, search bound, time cap or floating arithmetic. An actual field USING AAA remains outside coverage. Its possible metric strata require exact positive closure and compatible saturated B neighbourhoods; minimal equality patterns alone do not classify their coarsenings. This lemma does not settle that obligation or the eight-word changed-multiplicity programme.
