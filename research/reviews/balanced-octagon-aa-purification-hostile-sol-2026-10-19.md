# Independent hostile Sol review: balanced octagon AA purification

Date: 2026-10-19. Reviewed the producer report `research/searches/balanced-octagon-aa-purification-sol-2026-10-19.md` and its complementary-angle necessary-theorem dependency. This review uses independent analytic reconstruction, not finite patch evidence. The domain is a fixed strictly convex metric Q, a unit regular pentagon P, arbitrary isometries including reflections, unrestricted initial contacts, and every real 108°<α<126°, including α=120°.

**Verdict: PASS after the incorporated local algebra correction in §4.** The initial sine/transverse closure calculation was incorrect. The producer has incorporated the correct axial cosine calculation independently reconstructed below; it proves the same metric symmetry and the same periods. The two residual reflection decorations remain unresolved. All positive periodicity conclusions concern a purified limit tiling; they do not establish periodicity of every source tiling.

## Contact reduction and purification

The full-edge reduction applies before any matching hypothesis: all native angles are at least 108°, strictly below 180°, so an open-side contact would require one straight native angle or at least two native corners totaling 180°. Neither can occur. Every vertex is trivalent. The only stars are PPA and PBC, with BBB additionally possible exactly at α=120°.

In all seven words the non-A runs have length two. At either endpoint of such a run, the edge toward the neighboring A must face P because every star containing A is PPA. Consequently the endpoint cannot participate in BBB, which would require both its Q edges to face Q. Every B is such an endpoint; therefore BBB is absent pointwise, including at resonance. Each two-letter run has its unique QQ edge. The other six edges face unit pentagons and have length one.

The uniform incidence identities are x=4q+O(R+1), y=2q+O(R+1), and 5p=2x+y+O(R+1), hence p=2q+O(R+1), for translated square windows. The constants are uniform in the window translation for a fixed metric. Each Q has two AA edges; each is adjacent to a different physical P, since one P cannot receive two AA edges. Indeed an AA receipt forces the two neighboring P sides to be PP; PP sides form a matching of the pentagon cycle, with maximum size two and a unique side adjacent to both. Thus the integer nonnegative deficit 1−a(P) has sum O(R+1), after the bounded boundary correction for anchor/receipt counting.

For fixed L, defective anchors within distance L plus a tile diameter of a large square exclude only O(R+1) disks of bounded radius. They cannot cover its quadratic area. A center in the remaining interior gives a clean L-neighborhood. Choose L tending to infinity and translate those centers to the origin. Fixed positive tile area and bounded diameter bound the number of tiles meeting each compact set. A diagonal subsequence of their placements, allowing both parity classes, yields disjoint interiors and coverage of the plane. For any limiting P, select its AA neighbor along a subsequence; bounded local multiplicity and the finite native side choices ensure a fixed incident pair can be selected, and the full side coincidence survives the limit. Every limiting P therefore receives an AA side. There is no inference from subquadratic deficit to pointwise saturation in the original tiling.

## PP carriers, reflections, and common return

An AA receipt forces exactly two nonconsecutive PP sides, so the PP graph has degree two. Across each PP side the regular pentagon neighbor is uniquely placed. Different PP sides cannot lead to the same physical neighbor: two convex polygons with disjoint interiors cannot share two noncollinear boundary segments. The center steps have length 2r, r=1/(2tan36°), and turns ±36°.

At each PP edge, mark the endpoint adjoining each pentagon's distinguished AA side. If the marks select the same endpoint, the two AA sides belong to the same Q at that endpoint; its intervening A has an AA edge on both sides, hence is the middle of AAA. Conversely that middle A forces this configuration. Opposite endpoint choices reverse turn sign, equal endpoint choices preserve it. These statements use physical sides and endpoints, so reflecting any Q does not add a hidden choice to the PP dynamics.

For disjoint-AA words all choices are opposite: the turn sequence alternates, the two-step translation has length 4r cos18°, and the AA sides are parallel to its axis. For AAA words the same-endpoint PP edges are exactly the edges joining each Q's two AA-facing pentagons. Each P belongs to exactly one such pair, giving a perfect matching. Along a carrier, marked and unmarked edges alternate, forcing turns ++-- up to reversal and shift. A step direction sequence is 0°,36°,72°,36°; its four-step sum has length 4r(1+cos36°), axis 36°, and restores the regular pentagon and its distinguished side, as well as the matching.

Both paths have positive projection on their return axis and bounded transverse excursion. They are proper lines, with no finite components. Distinct center paths cannot cross: their segments run through tile interiors and the midpoint of their own PP sides. Two proper lines with nonparallel axes and bounded transverse excursion would have interlacing ends outside a large disk and must intersect. Thus all axes are parallel. The respective return lengths are fixed, giving the same vector v or w on all components, with either traversal orientation. The P union and all distinguished-side data have that return, even if carrier phases differ.

## The three disjoint-AA words

For AABBAACC the difference of oriented AA directions is 72°+2(180°−α)=432°−2α, strictly between 180° and 216°. It is never a multiple of 180°. Both AA sides would need the common axis direction. This is an exact obstruction over the full open interval, including resonance.

For AABCAABC, set β=180°−α. The unit-side direction pairs are (0°,180°), (36°,216°), and (144°,324°); the QQ directions are 36°+β and 216°+β. Closure therefore forces equal QQ lengths. Every opposite side vector is the negative of its mate, proving actual central symmetry of the metric Q. A rooted AA side with an exterior half-plane has two distinguishable placements, determined by its forward B/C flank; using the other native AA side gives the same placement by that central symmetry. To audit the recurrence, trace the two non-AA PQ sides of P_n through its two PP neighbors: their Q tiles are anchored at P_(n−1) and P_(n+1). The third PQ/PQ vertex of P_n requires complementary B,C labels. Each individual anchor itself has complementary flanks. Hence the forward flank repeats every two P steps. The full metric Q placement, including reflected copies, returns under v.

For AABCAACB the QQ directions are d=36°+β and 360°−d. The other six unit sides have total vertical component zero. Closure gives (x−y)sin d=0; d is strictly between 90° and108°, so x=y. Reflection in the perpendicular bisector of the first AA side pairs the ordered edge vectors with reversed traversal and fixes the actual polygon. There are two anchor types, with B,B and C,C flanks, and each type has a unique rooted placement. The same physical tracing at P_n requires the types at n−1 and n+1 to be opposite. Thus types return after four P steps and all Q placements return under 2v. This argument supplies a finite common return, not a mere finite alphabet on a periodic scaffold.

## The four AAA words and the algebra correction

For AAABCACB, put the first side at direction zero. The middle-AAA bisector has direction 108°. The two QQ directions are d3=252°−α and d6=144°+α, summing to396°=2·108°+180°. Their projections **along** that axis are respectively cos(144°−α) and −cos(144°−α). The six unit-side vectors pair by reflection with reversed traversal and have zero axial sum. Consequently closure gives

    (x−y) cos(144°−α)=0.

For AAACBABC the analogous equation is

    (x−y) cos(α−108°)=0.

Both cosine factors are strictly positive throughout 108°<α<126°. The initially submitted transverse sine equations were not the actual closure components: the transverse components of the two QQ vectors agree, while their axial components oppose. This is a repair to the proof, not a counterexample to its conclusion. Equal QQ lengths make the indicated reflection an actual metric symmetry, because it pairs every side vector and native vertex of the closed polygon.

The two consecutive AA sides fix the middle AAA vertex and occupied sector. Their rooted Q has at most the two placements exchanged by that reflection. In these two symmetric words those placements coincide. Every Q is anchored on exactly one marked PP edge, and w preserves that edge's two AA anchors with their actual geometry. Thus every Q returns under the common w; both full tilings have a nonzero translation.

For AAABBACC and AAABCABC the exterior flanks are B,C and the two rooted placements remain distinct because α and252°−α never coincide in the open interval. The third PQ side incidence at the isolated A can link decorations on different carriers. The simple same-carrier recurrence used for disjoint-AA words does not follow. Neither periodic P positions, finite local choices, compactness, nor a finite repeated patch implies a common return of the binary Q decoration. No claim closing this gap is certified here.

## Exact scope

| Word | Result certified by this review |
|---|---|
| AABBAACC | No plane tiling in the stated domain |
| AABCAABC | Any assumed tiling yields a purified tiling with period v |
| AABCAACB | Any assumed tiling yields a purified tiling with period 2v |
| AAABCACB | Any assumed tiling yields a purified tiling with period w, using corrected closure calculation |
| AAACBABC | Any assumed tiling yields a purified tiling with period w, using corrected closure calculation |
| AAABBACC | Purification and periodic P scaffold; full Q decoration unresolved |
| AAABCABC | Purification and periodic P scaffold; full Q decoration unresolved |

The four implications do not assert that every metric in those families tiles, or that the source tiling itself is periodic. No finite enumeration was used to fill the reflection gap. No discovery-log or Git edits were made.

The two residual words are assigned to a separate pending chirality review. This PASS certifies only the purification/backbone conclusions and the one exclusion/four conditional periodicity conclusions tabulated above; it does not prejudge that separate review.
