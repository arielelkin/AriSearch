# Hostile whole-witness review: minimal pentagon/heptagon torus

Verdict: **valid** for the explicit h=0 periodic witness. Reviewed independently on 2026-10-19 against research-problem.md and research-protocol.md §§8,11,19, after reading the reviewed 144/126 first gate. This excludes aperiodicity of this exact pair and makes no claim about other parameters or the overall problem.

## Exact geometry and independent verification

The companion review checker reconstructs w with QQbar.zeta(20), constructs P and Q from their edge sums, and directly constructs P, 1-P, 1-w^6 Q, w^6 Q. It imports neither search code nor certificate. Real coordinates use ordered exact AA arithmetic. Every vertex other than an edge's endpoints lies strictly to its left, separately for every edge of every face. Thus all four specified cyclic polygons are simple strictly convex polygons with positive area. The pentagon is regular by its unit edges with successive direction ratio w^4. The heptagon is exactly the reviewed h=0 metric by its alternating prescribed lengths and directions.

The checker independently uses the stated lattice vectors. Its determinant is positive (approximately 17.06601673017679), and is exactly the sum of the four signed polygon areas. This equality is an algebraic decision, not a comparison of the displayed decimals.

For each ordered face pair, inverse lattice coordinates give exact bounding intervals. Any intersecting translate must have each integer shift between ceil(minimum of first minus maximum of second) and floor(maximum of first minus minimum of second). All 26 nonidentity ordered translate candidates are checked with Sage Polyhedron intersection, a different intersection implementation from the search separating-axis test. Every intersection has dimension below two. Identical face and zero shift are the only omissions, as required. This also checks possible overlaps with other translates of the same representative. The finite bound does not assume a numerical tolerance or a preselected lattice radius.

Without consulting stored pairings, the checker compares every ordered pair of representative edges. Each of the 24 darts has exactly one opposite edge vector with endpoint difference in the integral lattice; mate involution and opposite shift are checked. Hence every full edge has exactly one matching full edge. The three QQ shifts recovered are (0,-1), (1,-1), (1,0), as claimed. All unit edge and long edge gluings are exact. No extra gluing hypothesis is needed for coverage.

## From finite witness to the whole plane

The lattice has rank two and each representative is compact, so the family of translates is locally finite and its union is closed. Disjoint interiors give a torus union of area equal to the sum of face areas, exactly the area of the torus. If the plane union omitted a point, closedness would give an omitted open ball. Its projection contains a positive-area open subset of the torus, contradicting that area equality. Thus there are no holes, including boundary holes. Translation by either nonzero lattice vector preserves the full family. This establishes an actual periodic plane tiling with both congruence classes, rather than a locally compatible torus drawing.

## Reflections and enumeration scope

The checker separately verifies the exact symmetry set identity {w^8 conjugate(q): q in Q}=Q. This is an orientation reversing isometry fixing the origin. P has its usual regular-polygon reflections. Therefore allowing physical reflections introduces no further congruence classes or missing native face placements; a reflected tile can be rewritten as a direct placement using its reflection symmetry and the corresponding boundary relabeling. This is sufficient for the positive witness independently of enumeration completeness.

The enumeration's claimed scope is also sound: the first-gate reduction forces trivalent APP and PBB stars and full edges. In a 2P+2Q torus the two A incidences give two PPQ vertices; their PP half edges yield one PP edge. A pentagon cannot have two PP edges: consecutive ones create a forbidden PPP corner; two disjoint ones force four A endpoints and therefore an extra AA edge on the pentagon five-cycle, requiring another PP edge and forcing consecutiveness. Thus the unique PP edge joins distinct P faces. Independent cyclic relabeling by regular-pentagon rotations puts it at edge0 on each. The remaining AB/BA endpoint matching choices are 2! each, BB matching choices 4!, and QQ perfect matchings 15. Their product is 1,440. No lattice displacement bound is part of this combinatorial enumeration. The dart permutation next-after-mate correctly cycles around an oriented vertex, and testing exactly three-cycle APP/PBB label multisets imposes the intended stars. Developing face rotations then checking every paired vector is a necessary translation holonomy test. The source replay agrees exactly with the retained JSON; its two surviving maps differ by Q face exchange. This review audits that small enumeration directly but does not supply a second enumeration engine. Its completeness is unnecessary to the independently certified positive witness.

## Defects, repairs, uncertainty

No defect found and no mathematical repair proposed. Attacks checked included self-overlap, incorrect embedding, reflection omission, omitted far lattice translates, same-face translate overlap, accidental area equality with holes, edge multiplicity, and finite-to-infinite coverage. The original search does not explicitly test strict convexity; the independent checker supplies that check and the first gate already proves the family convex. There is no unresolved qualification for the explicit h=0 witness. The general two-polygon research target remains unresolved.

Replay from repository root:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/regular-pentagon-heptagon-minimal-torus-hostile-sol-2026-10-19.sage

Output: VALID independent QQbar/AA Polyhedron witness; translate pairs 26. SageMath exact algebraic arithmetic; no solver, seed, timeout, or numerical branch. No Git or discovery-log edits.
