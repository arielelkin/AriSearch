# Balanced octagon AA purification and exact return audit

Date: 2026-10-19. One analytic cycle; no patch growth or torus enumeration. Conditional throughout on a tiling by a fixed strictly convex metric Q and the unit regular pentagon P. Angle labels are A=144°, B=α, C=252°−α, with 108°<α<126°. Reflections are allowed. This report uses the reviewed complementary-angle necessary theorem and audits the transfer from the resonant heptagon carrier argument. It has not received an independent hostile review.

## 1. Simultaneous purification

For each of the seven balanced octagon words, Q has (a,b,c)=(4,2,2) and exactly two AA sides. Uniform translated-window incidence estimates give p_R=2q_R+O(R+1). Every AA side faces a distinct P; a P receives at most one AA side. Therefore, writing a(P)∈{0,1} for receipt, the nonnegative integer deficit d(P)=1−a(P) has total O(R+1) in every translated square.

At α=120°, a BBB corner would have two incident QQ sides. Each non-A run in these words has length two. Its endpoint B or C has an incident side leading to A, and that side must face P at its A endpoint. Thus no corner in such a run can be BBB: t(Q)=0 pointwise. There is no sparse resonant exception to remove. The QQ edge in each non-A run is its unique matching edge; every other Q edge faces P. In particular all six PQ edges have length one.

For any fixed L, disks of radius L+2D about defective P anchors in a large square cover area O((R+1)(L+2D)^2), whereas the square interior has area Ω(R²). Taking R sufficiently large gives a radius-L neighborhood containing no defect. Translate its center to the origin and let L→∞. Fixed-polygon placement compactness, including the two reflection parities, gives a whole-plane tiling. Bounded tile diameter and positive area give local finite bounds; diagonal extraction preserves coverage and disjoint interiors. Indexed side incidences persist, or equivalently one reapplies the full-edge/star theorem in the limit and extracts the finite incidence neighborhoods. Every limiting P has a(P)=1. This changes the tiling; it does not prove that defects were absent in the source tiling.

## 2. Exact PP graph and its two return mechanisms

Every P now has the species side word PP,PQ,PP,PQ,PQ, with the AA-facing PQ side between the two PP sides. Consecutive PP sides are impossible since their common vertex would have three P corners. Thus the PP graph has degree two, and the center path turns by ±36° at each P. The two PP neighbors are distinct in a plane tiling.

Across a PP edge, each P selects the endpoint adjacent to its distinguished AA side. Same-endpoint selection occurs if and only if the Q at that endpoint has both incident sides AA. Thus it occurs precisely at the middle A of an AAA run. Opposite-endpoint selection reverses consecutive turn signs; same-endpoint selection preserves them. This is the exact physical endpoint rule, independent of reflection parity.

For the three words with disjoint AA sides, same-endpoint selection is impossible. Turn signs alternate, the center steps have length 2r with r=1/(2tan36°), and there is a two-step translation v of length 4r cos18°. The distinguished AA side returns with the pentagon. Its direction is parallel to v.

For each of the four AAA words, a Q's two AA-facing pentagons are PP neighbors. The corresponding PP edges form a perfect matching because each P has exactly one AA anchor. Marked and unmarked edges alternate on every component. Therefore the turn automaton is forced: signs repeat (s,s,−s,−s), up to shift and reversal. Step directions can be chosen 0°,36°,72°,36°, repeating. The four-step translation w has length 4r(1+cos36°)>0 and direction 36° in this convention. It preserves the distinguished sides and the marked-edge matching. There is no free symbolic sequence of PP turns.

Both center-path types are proper embedded graphs over their return axis: all steps have positive projection onto that axis. Their finite periodic deviations are bounded. A finite PP component is impossible because its nonzero return contradicts closure. Distinct center paths are disjoint, lying in disjoint pentagon interiors except at their own shared side midpoints. Nonparallel proper graph axes would force intersection. Hence all component axes are parallel. Within either word family their return lengths are equal, so the P union and its distinguished AA-side data share a common return v or w, with sign irrelevant.

## 3. The three disjoint-AA words

For AABBAACC, the oriented directions of its two AA edges differ by 72°+2(180°−α)=432°−2α. This lies strictly between 180° and216°. Both AA edges would have to be parallel to their anchored PP axes, which have just been shown parallel globally. This is impossible. Thus this word is untileable throughout the stated open interval, including α=120°.

For AABCAABC, write β=180°−α and γ=α−72°, so β+γ=108°. Starting its first AA edge in direction zero, the eight side directions are

    0, 36, 36+β, 144, 180, 216, 216+β, 324 degrees.

The two QQ sides are positions 2 and6 (zero-based) and are opposite. All other sides have length one and cancel in opposite pairs. Closure forces the two QQ lengths equal. The actual metric polygon, not only its angle word, is therefore centrally symmetric. Each AA anchor has flanking non-A labels B,C. Given an AA side and its exterior half-plane, a forward B/C label determines Q uniquely, since choosing its other native AA edge gives the same placement by the actual half-turn symmetry. At the PBC vertex of P_n, the forward label at P_(n−1) is complementary to the backward label at P_(n+1); the two labels at an individual anchor are complementary. Hence forward labels have period two. The whole Q union returns under v, and the purified tiling has period v.

For AABCAACB, the side directions are

    0, 36, 36+β, 144, 180, 216, 216+γ, 324 degrees.

Only sides 2 and6 have unknown lengths x,y. Their directions sum to360°, while the vertical components of the other six unit sides cancel. Vertical closure gives (x−y)sin(36°+β)=0. Here 36°+β lies strictly between90° and108°, so x=y. Reflection across the vertical line through the first AA midpoint exchanges the relevant sides and vertices, and the equalities just proved make this an actual metric symmetry. The first AA anchor has B,B flanks and the other C,C. Its rooted placement is unique once this anchor type is specified: the reflection fixes the whole tile. PBC requires the anchor labels at n−1 and n+1 to be complementary, so anchor type flips every two P and returns every four. Thus the whole purified tiling has period 2v. Neither conclusion assumes the shape tiles for every allowed metric.

## 4. The four adjacent-AA words

Write their cyclic form as AAA X Y A Z W. The anchored pair has external flanking labels X,W. Its two AA edges fix its middle AAA vertex and its occupied sector. There are at most two rooted placements of Q on these edges, exchanged by reflection in the bisector of that sector.

| Word | External flanks X,W | Return status |
|---|---|---|
| AAABBACC | B,C | P backbone has w; reflected Q choice unresolved |
| AAABCABC | B,C | P backbone has w; reflected Q choice unresolved |
| AAABCACB | B,B | Actual reflection symmetry; whole tiling has w |
| AAACBABC | C,C | Actual reflection symmetry; whole tiling has w |

Here is the metric symmetry check for the last two entries. For AAABCACB the side directions are

    0, 36, 72, 72+β, 180, 216, 216+γ, 324 degrees.

The reflection axis at the middle AAA vertex has direction108°. Reflection reversing the cyclic traversal pairs the two QQ sides (positions3 and6); their directions are 252°−α and144°+α. The six known unit sides are paired by that reflection. Their QQ directions have opposite axial projections, so the axial component of closure is proportional to (x−y)cos(144°−α). This cosine is nonzero on the whole open interval. Hence x=y, and the reflection is an actual symmetry of Q. For AAACBABC, interchange β andγ; the coefficient is cos(α−108°), again nonzero. The rooted placement is therefore unique. Translation w preserves each marked PP edge and its two distinguished AA sides, hence every Q placed on that marked edge. All tiles return under the common w.

For AAABBACC and AAABCABC, swapping the two AA anchors interchanges external labels B and C. Since B≠C everywhere in the open interval, the two rooted placements are genuinely distinguishable. The marked PP edge fixes the geometry of the pair of AA anchors but does not fix this reflection choice. Unlike the one-AA heptagon, the Q across a pentagon's other PQ side need not be indexed by the immediately preceding or following AA anchor on the same carrier: each Q also has its isolated A and its two incident PQ edges. The PBC condition therefore couples an external flank of a rooted Q to a flank at another Q's isolated A, potentially on another PP component. The old recurrence F_(n−1)=F_(n+1) is not justified here.

## 5. Stop: exact surviving return gap

The analytic cycle proves purification for all seven words, a common periodic PP backbone for all of them, untileability of AABBAACC, and a whole-tiling nonzero translation for AABCAABC, AABCAACB, AAABCACB, AAACBABC. The periods are respectively v,2v,w,w.

For AAABBACC and AAABCABC the missing invariant is a proof that the reflected rooted-Q choice on every marked PP edge returns after one common nonzero multiple of w, accounting for the actual isolated-A contacts and both QQ contacts. A finite set of placement choices on a periodic P scaffold is not itself a periodicity proof. No global return invariant for these two words has been established in this cycle; no aperiodic realization or plane extension has been established either. The exact residual problem is a geometric binary decoration constrained across the carriers, rather than freedom in the PP turn language. Stop here; no patch growth, larger torus, or blocked seam-atlas reopening is warranted by this calculation.
