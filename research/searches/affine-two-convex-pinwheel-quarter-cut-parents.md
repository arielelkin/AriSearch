# Quarter-corner pinwheel resection: two specified parent compilers fail

Date: 2026-10-13. Exact finite construction gate completed. The entire proposed straight-edge resection family is now separately excluded by an explicit periodic Q-only escape: [direct proof](../lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md). The compiler itself is a restricted finite calculation, not a substitution.

The concrete change to the whole-four-triangle P/H omission domain moves the common corner of one P/H pair to the point one quarter along P's next native side. The two modified convex polygons have exact areas 15/4 and 17/4; their unchanged union still has area 8. The producer prints their exact rational coordinates. Both have the required genuine five and six sides, and their interiors are disjoint. The intended two-parent ordinary similarity is M²=((3,4),(-4,3)), with area expansion25. Positive mixed child counts chosen from the area equations are (8 P,15 Q) for P and (17 P,10 Q) for Q. These are 23 and 27 children, respectively, rather than the old uniform25 whole-face children.

A specified compiler applies the exact ordinary pinwheel triangle subdivision twice to the eight source triangles of that P/H union, giving 200 unit-area source cells. It enumerates all full-native-side-connected four-cell unions in that fixed source patch, retains convex area-four occurrences congruent to the OLD P or H boundary, transports the same quarter-corner edit by every ordinary isometry, and keeps each edited face wholly inside the proposed modified parent. It checks candidate intersections exactly with rational separating-axis predicates. No arbitrary increasing cluster or patch bound is involved.

Replay gives 212 connected four-cell subsets, of which only TWO are old-face occurrences. The P parent has four distinct contained edited P candidates and ZERO Q candidates, against the required (8,15). The Q parent has ZERO candidates of either species, against (17,10). The packing models are therefore INFEASIBLE directly from the species count inequalities, regardless of overlap constraints or the solver's time limit. No solver UNKNOWN status is promoted to an exclusion. The retained JSON contains exact coordinates, counts and statuses.

The result excludes only this specified source-address compiler. It does not exclude child occurrences connected only by partial source-cell contacts, edited faces spanning other source addresses, independently positioned congruent children, different corner resection choices, or any unrestricted tiling of the original modified polygons. In particular, hierarchy recognition was never reached. The new complementary seam corners do not automatically force their reunion: their angles remain in the original pinwheel angle field, and unrestricted angle stars allow other arrangements. There is no mandatory-recombination claim here.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/affine-two-convex-pinwheel-quarter-cut-parents.py

Certificate: `research/certificates/affine-two-convex-pinwheel-quarter-cut-parents.json`.
