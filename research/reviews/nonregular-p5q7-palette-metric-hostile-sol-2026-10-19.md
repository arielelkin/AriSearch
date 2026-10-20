# Independent hostile review: fixed nonregular P5/Q7 metric

Verdict: **PASS for the exact metric/native-corner gate; FAIL as written for the literal reflected-mate claim.** No plane tiling or aperiodicity conclusion is established. Reviewed the .md, .py and .json named `research/searches/nonregular-p5q7-palette-metric-sol-2026-10-19` against AGENTS.md, research-protocol.md and research-problem.md. Discovery log and Git untouched.

## Exact replay and geometry

Ran `mise exec -- conda run --no-capture-output -n arisearch python research/searches/nonregular-p5q7-palette-metric-sol-2026-10-19.py`: all assertions passed. A separate runpy/captured-output comparison verified parsed JSON equals the retained certificate. Independently recomputed both vector sums in Q(zeta72), obtaining zero, and checked exact AA inequalities `0<L<a<1<b` (positivity also asserted by replay). Thus all four lengths are distinct; a and L having the same minimal polynomial is harmless because their embedded values differ.

The direction increments, including cyclic wraparound, are exactly 180 minus the declared interior angles. Every nonincident vertex is strictly left of every directed edge under exact AA cross-product comparisons. Together with exact closure this certifies genuine strictly convex polygons, not merely a positive-turn chain. The Q linear system uses directions10 and31, whose determinant is sin105 degrees, nonzero.

## Reconstructed forcing and stars

The complete species-aware trivalent resonance list has five entries, including P110/P115/Q135. At a P tile, its two115 corners must be PPQ; its100 corners cannot be PPQ. Every PP edge contributes two PPQ endpoints and each PPQ corner exactly one PP edge. Thus the number of PPQ corners is even and the unique110 cannot be PPQ. Exactly one PP edge joins the adjacent115 corners. This excludes that fourth resonance pointwise, without a frequency argument.

Private Q length a forces side1 QQ. Vertices1 and2 (both130) are PQQ. The number of PPQ vertices on a Q is odd: the remaining Q vertices are paired as endpoints of QQ edges. Only vertices0,1,2 could be PPQ, so vertex0 is its unique PPQ. Consequently sides0 and6 are PQ. Private length b forces side3 QQ, so its125 endpoints3 and4 are PQQ and sides2 and4 are PQ. Vertex5 is125 and vertex6 is135; both are PQQ. At each, one incident side (4 or6) is PQ, forcing the remaining **side5, length1, to be QQ**. This is pointwise and does not misuse average-one to discard sparse defects.

The four seam triangles genuinely support all native corners: (P0,P1,Q0) with (L,1,1); (P2,Q1,Q2) with (1,a,1); (P3,Q3,Q4) with (1,b,1); (P4,Q5,Q6) with (1,1,1). Each corner can be placed in its prescribed angular sector by an allowed isometry; convexity keeps its entire tile in that sector. The sectors partition360 degrees, hence tile interiors are disjoint and the equal seam segments coincide. None of this requires that any particular pair have opposite chirality. The four PQ edge correspondences1↔0,2↔2,3↔4,4↔6 have compatible endpoint star types when either endpoint order is allowed.

## Defect found: reflection versus endpoint reversal

The sentence “QQ edges have reflected mates” and corresponding Python comment are inaccurate literally. Consider Q native side5, running from vertex5 (125) to vertex6 (135). A reflection in its supporting line keeps these endpoint positions fixed, giving angle pairs125+125=250 and135+135=270; neither is a possible QQ star. A copy placed across the edge with endpoints swapped instead gives125+135=260 at both ends, leaving the required P100 angle. The explicit map is the half-turn `x ↦ v5+v6-x`, which is orientation preserving and supplies a **same-chirality** mate. An orientation-reversing isometry swapping those endpoints reflects in the perpendicular bisector and leaves the tile on the original side of the supporting line, so it cannot repair this by opposite chirality.

Correction: say “Each QQ side admits an endpoint-compatible congruent mate; side5 must reverse its125/135 endpoints and can be paired by a half-turn.” Reflections remain permitted globally. The checker only tests the sum of the two native endpoint angles for each QQ edge; it does not test, and cannot justify, the stronger reflected-mate sentence. No other claimed native star relies on opposite chirality, and the correction leaves the substantive local gate intact. No source files were repaired by this review; the author must amend that wording.

## Limits

Full-edge trivalence is used from the cited obtuse-edge-forcing lemma; this review independently checks its consequences here, not that separate lemma. The geometry and local constructions are valid under the explicitly allowed reflections and unrestricted isometries. No corona, continuation rule, infinite tiling, periodic escape, or shape-only aperiodicity argument follows. Final verdict in protocol vocabulary: **valid for the stated metric/native-corner result, invalid for the literal reflected-mate subclaim, global extension unresolved**.
