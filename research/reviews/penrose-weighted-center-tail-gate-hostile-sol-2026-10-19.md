# Independent hostile review: weighted Penrose-center tails

Date: 2026-10-19. Verdict: **PASS for the two stated closed parameter half-lines and combined open gap**, subject to the previously disclosed standard infinite Robinson/Penrose base-pairing dependency. This does not classify the remaining gap or resolve the main research problem.

Reviewed `research/searches/penrose-weighted-center-tail-gate-sol-2026-10-19.{md,py,json}`, the reviewed unweighted source Markdown and review, and the weighted central first-gate Markdown and hostile review. No producer artifact, git file, or research log was changed. No site search in the remaining gap or patch enlargement was performed.

## Independent arithmetic and replay

The retained checker is [verify_penrose_weighted_center_tail_sol_independent.py](verify_penrose_weighted_center_tail_sol_independent.py). It imports neither producer. Its source reconstruction reuses the separate real-coordinate method of the central hostile checker: Q(sqrt(5)), with points (x,y) and metric x²+((3-phi)/4)y². It reconstructs all ordered substitution triangles, pairing, centers, nesting and exposed edges. Its cell calculation directly intersects consecutive claimed support lines rather than reproducing the producer clipping algorithm. Both producer `--check` and this independent checker completed with exit zero and assertions enabled:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-weighted-center-tail-gate-sol-2026-10-19.py --check
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_penrose_weighted_center_tail_sol_independent.py
```

## Geometry, indices and finite completeness

The checker independently recovers 890 triangles and 430 distinct centers. All triangle apex edges have squared length one. Base squared lengths are 2-phi for color zero and 1+phi for color one, confirming thin and thick geometric types respectively. Ordered same-color base pairs have opposite apex sides and four unit rhomb edges. Every unmatched base lies on an actual outer-decagon segment. The exact labelled level-1 inclusion in level 5 passes. Thus the retained rhombs and their center ordering are those of the reviewed nested source, with no omitted interior base pair.

Sorting each type by exact squared distance to the origin and then by index independently selects thick index 25 and thin index 26 as the very first candidates; there are no rejected preceding candidates. Both exported cyclotomic center vectors agree with independently reconstructed real-coordinate centers. Support orders are exactly [24,70,328,413] and [29,72,116,374]. Every directly reconstructed cyclic vertex equals its exported Q(phi) coordinates. All four turns are strictly positive, all four vertices are distinct, every side lies on its claimed same-type bisector, and every vertex satisfies every retained same-type halfplane. A convex quadrilateral's four supporting halfplanes intersect in that quadrilateral; therefore feasibility plus these four genuine facets proves equality with the complete finite same-type cell. It does not merely exhibit an inscribed polygon, and no artificial bounding side is needed in this independent calculation.

The exact maxima of 2(q-c)·v-|q-c|² over all vertices and all retained opposite-type centers are 1/4+phi/3 for index 25 and 21/44+9phi/22 for index 26. The checker recovers every limiting pair: [(1,26),(3,374)] for thick and [(0,24),(0,413),(2,69),(2,115)] for thin. Expanding power distance gives

    2(q-c)·v <= |q-c|² + weight(c)-weight(q).

Thus the correct directions are delta >= 1/4+phi/3 for thick and delta <= -21/44-9phi/22 for thin. Every retained site inequality is independently satisfied at the respective endpoint. The fixed same-type polygons retain four positive turns there; opposite-type equalities touch vertices and do not remove any positive-length side. Both endpoints are included. Feasibility at the endpoint persists in the favorable direction because only opposite-type constraints change, and each becomes weaker.

## Infinite completeness and the unbounded weight issue

Independent exposed-edge distance minima are M=93/4+149phi/4 for thick and M=41/2+129phi/4 for thin. Independent maximum vertex squared radii are R²=11(1+phi)/36 and R²=1/2+3phi/4. In both cases M>4R² exactly. The center lies inside its retained nondegenerate rhomb. Hence the disk of radius sqrt(M) about it lies in the retained rhomb union. Any omitted genuine source center lies inside its own rhomb, whose interior is disjoint from retained interiors; its distance D is at least sqrt(M). Unpaired outer triangles do not create a hidden nearby site: their future rhomb centers are likewise omitted-rhomb interior points, covered by this same argument. No subtraction of a rhomb circumradius is required.

For any point v of the fixed polygon, |v|<=R by convexity, and therefore the geometric slack satisfies

    D²-2(q-c)·v >= D(D-2R) > 0.

This handles all omitted same-type centers. For omitted opposite-type centers the added weight slack is +delta for the selected thick cell and -delta for the selected thin cell. On the certified half-lines these quantities are positive and grow in the favorable unbounded direction. Consequently there is no hidden large-|delta| failure in the omitted-site estimate. A proof using a fixed bound on |delta| would not suffice here; the stated sign argument does suffice uniformly on both full half-lines. This establishes actual infinite-source power cells, conditional on the named source's standard infinite pairing property inherited from the previous review.

## Combined coverage and scope

The previously reviewed central interval is [-1/4,1/4+phi/3). The new thick certificate includes its excluded upper endpoint, giving [-1/4,infinity). The thin certificate gives (-infinity,-21/44-9phi/22]. The remaining uncertified set is exactly

    (-21/44-9phi/22, -1/4),

whose positive length is 5/22+9phi/22. Both gap endpoints already have strict quadrilateral witnesses. “Remaining gap” denotes a gap in these certificates, without asserting absence of other witnesses there.

Each certified strict convex quadrilateral admits the usual periodic tiling by half-turn copies. Accordingly any proposed two-shape protoset containing every output class of this fixed rule fails unrestricted aperiodicity on the covered parameters, where omission of a species is allowed. This review establishes neither a two-class census nor failure throughout the gap, nor exclusion of other weighted or context-dependent dual rules. No substantive defect was found in the stated tail gate.
