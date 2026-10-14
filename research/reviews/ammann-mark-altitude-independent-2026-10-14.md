# Independent hostile review: marked-altitude fractional tree

Date: 2026-10-14. Verdict: **VALID within the stated height-only scheme**.
Reviewed [the second-cycle manuscript](../searches/ammann-mark-altitude-gate-2026-10-14.md) and [producer](../searches/ammann-mark-altitude-gate-2026-10-14.py). The reviewer developed the common-triangle precursor, but did not develop this marked-height variant. This check imports neither the producer nor its certificate.

The source's actual counterclockwise mark cycles are thin XXYY and thick XYYX. Both opposite-edge choices select exactly one X and one Y triangle. Across a source edge, equal marks and opposite source orientations give congruent unit-base isosceles triangles of the same marked height, on the needed side. The bipartite role rule places precisely one quad and one triangle on each edge. Consequently the marked-height variant has the same exact global gluing compatibility as its precursor, provided its four sectors geometrically partition each source rhomb. A source arrow is unnecessary for this particular symmetric triangle interface; the manuscript says so explicitly.

I independently derived the areas from polygon vertices, rather than dropping the unequal-height shear term. For triangle apices p=(1/2,hX), q=(1/2+c,s-hY), the BC quadrilateral's area is

    s/2+(2c-1)*hX/4-(2c+1)*hY/4.

Adding the receiving edge's triangle gives thin areas `s36/2 ± (1+2c36)*(hX-hY)/4` and thick areas `s72/2 ± (2c72-1)*(hX-hY)/4`. The independent symbolic checker derives these expressions directly for **both choices of triangle edges**, using the actual cyclic marks. It retains hX and hY as polynomial variables throughout this derivation. Thus the all-parameter area gate is not inferred merely from the numerical fixture.

Each coefficient is nonzero, so when delta=hX-hY is nonzero, every thin rhomb produces two distinct areas and every thick rhomb produces two distinct areas. If their union had only two values, the two unordered pairs would coincide. Their means would then coincide, but sin(36)/2 differs from sin(72)/2. Therefore at least three congruence classes occur whenever this rule is admissible and unequal in height. The argument requires both source species, which the stated infinite Ammann source supplies; it requires neither frequencies nor a contact catalogue.

For the explicit hX=sin(36)/10, hY=sin(36)/20 fixture, the reviewer checks all eight output polygons with exact algebraic support inequalities against every nonincident vertex. This includes both far endpoints of the removed common source edge. All outputs have exactly five strict corners. All four sectors in each of the four source/role cases pass the same strict support checks, have the prescribed triangle areas, and sum to the source area. Their tree topology and interior nodes make a partition: the two interior nodes and their joining segment lie inside the convex source, and the four leaf branches cut its cyclic boundary into the four stated sectors. The author's additional separating-axis checks are consistent with this argument. Arbitrary positive heights are not asserted to produce convex outputs; the area obstruction applies conditionally on admissibility.

At equal height the source mark disappears from the interface, and the homogeneous-rhomb periodic omission construction applies exactly. The construction does not need the homogeneous carrier to obey Ammann arrows because the output polygons are unmarked. This closes the full admissible height-only mechanism: unequal heights fail the two-shape gate; equal heights fail periodic omission. No universal decoder is claimed for the unequal-height outputs.

The independent checker passed using exact Q(phi) symbolic areas and exact algebraic signs. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-mark-altitude-independent-2026-10-14.py

No defect found. The next restart must change the midpoint-based isosceles triangle interface or simultaneously change the receiving quad boundary. Height variation alone cannot repair the two-shape count, and a larger source search has no bearing on this obstruction.
