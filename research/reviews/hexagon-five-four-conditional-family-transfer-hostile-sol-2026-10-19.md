# Independent hostile review: conditional four-face family transfer

Date: 2026-10-19. Final verdict: **valid**, conditional on the stated side words, shared positive side lengths, strict convexity, four support angle equations, and a2=b3. The original research problem remains unresolved. No unrestricted first-support transfer is established.

## Claim and audited evidence

Read AGENTS.md, research-problem.md, research-protocol.md, the conditional-family lemma and producer/certificate, and the prior independent second-periodic carrier review. Independently reconstructed the fixed gluing and all selected metrics without importing the producer. Retained independent checker: `research/reviews/verify_hexagon_five_four_family_transfer_sol.py`.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_family_transfer_sol.py

Result: PASS. This replay checks the retained domain only and launches no search.

## Combinatorics, orientation, and indexing

The twelve side pairs in the prior fixture review cover all twenty-four directed sides once. The new independent checker verifies their exact endpoint offsets in the original lattice, their reversed edge vectors, and their native color matches. The two A boundaries use native vertex i and the two reflected B boundaries use native vertex 5-i modulo 6. Hence a stored B side i corresponds to native side 4-i, and its starting corner is b_(4-i). For A the starting corner is a_(i-1). These are exactly the maps used in the angle rows; confusing starting vertices with side-END angles would change the claimed condition.

Independently forming endpoint links gives eight disjoint three-sector cycles, with precisely the corner sets listed in the lemma. Every corner has two link neighbors. Thus these are actual circular links rather than merely equivalence classes of vertices. Each abstract face is a polygon disc, each edge is paired with one other edge reversing the chosen boundary orientations, and every vertex neighborhood is a disc. The face incidence graph is connected. The quotient is consequently a connected closed orientable surface, with F=4, E=12, V=8 and Euler characteristic zero, hence a torus. Reflected physical copies do not make the surface nonorientable: their stored boundaries are counterclockwise, and side identifications reverse these boundary directions.

## Linear obstruction

The independent corner reconstruction gives, in link order, the four rows

    a4+a5+b5=2pi,
    a0+b0+b1=2pi,
    a1+a2+b2=2pi,
    a3+b3+b4=2pi,

with multiplicities 2 each and the ordering in the lemma. Rational augmented ranks are exactly 5 for the six support rows, 4 for the carrier rows, and 6 for their union. The support span enlarged by a2-b3=0 equals the combined span. Explicitly the third displayed row differs from support row a1+b3+b2=2pi by a2-b3; the fourth differs from a2+a3+b4=2pi by b3-a2. The other two already belong to the support. This establishes necessity and sufficiency of the single extra relation for this carrier at the linear angle level. Failure of the broad rational implication is not a counterexample metric: nonlinear polygon closure might impose additional conditions, and the lemma correctly makes no claim that it does or does not.

## Global geometric attacks

Equal matched lengths alone would not guarantee a plane tiling. Here the proof supplies the missing global argument. Glue the actual strictly convex polygon discs by their endpoint reversing boundary isometries. This finite quotient is compact; it is a surface by the circular-link check, independently of its metric. Interior charts and unfolded edge charts are Euclidean. At each vertex the positive sectors appear in the circular order of its link and their angles sum exactly 2pi. Radial unfolding therefore provides a Euclidean disc chart, without a cone singularity or a branched multiple sheet. Charts can all be oriented consistently.

The resulting intrinsic metric is a compact length metric locally equal to Euclidean distance, and is therefore complete. Its universal cover has the complete lifted metric. One can make the development argument precise as follows: a developing local isometry from the simply connected flat cover to R2 exists by continuation of compatible Euclidean charts and homotopy invariance. A complete connected local isometry into R2 is a covering: lift any finite straight segment from a chosen starting point; if its maximal lift stopped at finite time, its finite remaining length would make the lift Cauchy, and completeness plus a local isometry chart would extend it. The same continuation on small balls gives evenly covered neighborhoods. Since R2 is simply connected, this covering is a global isometry. Thus no unsupported injectivity or extension claim is hidden in the development step.

Deck transformations preserve orientation and have no fixed points. An orientation preserving plane isometry with nontrivial rotational part has a fixed point, so every nonidentity deck transformation is a translation. Proper discontinuity makes the translation subgroup discrete. It is isomorphic to Z2, and compactness of its quotient forces its real span to be all R2: a proper span would leave an unbounded transverse coordinate on the quotient. Hence it is a full rank lattice. Neither a rank-one period degeneration nor irrational dense translations are possible. Its covolume equals the positive area 2 area(A)+2 area(B).

Finally each original closed polygon disc lifts injectively to the cover: the polygon disc is simply connected and its inclusion in the quotient has no internal identifications. The isometry to R2 preserves the complete lifted cell decomposition. Face interiors are disjoint and all cells cover the plane. The resulting Euclidean image of each face is congruent to its original polygon, since its connected interior develops by one rigid motion. This proves genuine tiling, and excludes hidden overlaps, rather than relying on the original fixture coordinates or preserving its original period vectors.

## Exact finite metric audit

The independent checker reads all 39 retained grid representatives and selects exactly indices

    0,1,3,4,5,7,9,13,14,20,22,24,28,29,32,34,35,37.

For each of these 18 it reconstructs both polygons from the exact Q(sqrt(3)) lengths and exact degree angles, verifies positive distinct lengths, strict interior angles, closure, total turn 360 degrees, and every nonincident strict supporting halfplane. It checks every support and carrier angle row. These checks certify admissible metrics for the conditional theorem and do not rely on approximate trigonometry.

Exactly 13 selected entries have an empty retained H1_species list. This confirms the stated overlap with the earlier classification labels; it does not independently reprove the imported monohedral classification. That dependency is explicitly disclosed in the lemma, and it is not needed for any of the 18 periodicity conclusions.

## Defects, repairs, and uncertainty

No mathematical defect found; no repair to the lemma was required. The development argument is short but valid under its supplied completeness and nonsingular vertex hypotheses; the details above make the covering and injectivity steps explicit. The producer's topology comments assume the known counterclockwise orientation of the original representatives, which the earlier independent fixture review verifies; the abstract construction itself can choose all polygon boundaries counterclockwise directly.

Remaining limits are scope limits, not gaps in the conditional theorem: no extension to metrics failing a2=b3, no nonlinear independence claim for that equation, no fresh monohedral theorem, no new enumeration, and no conclusion about arbitrary convex tile pairs.
