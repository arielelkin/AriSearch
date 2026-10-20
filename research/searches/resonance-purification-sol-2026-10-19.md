# Resonant purification and a periodic carrier for AABBBBC

Date: 2026-10-19. Status: analytic proof, [independent Sol hostile review PASS](../reviews/resonance-purification-hostile-sol-2026-10-19.md). No computation, enumeration, or literature novelty claim. This resolves only the exact resonant survivor specified here.

## Statement

Let P be a regular pentagon of side one, and Q a fixed strictly convex heptagon whose cyclic angles are A,A,B,B,B,B,C, where A=144°, B=120°, C=132°. Reflections and arbitrary contacts are allowed. If P,Q admit any plane tiling, they admit a plane tiling with a nonzero translation. More precisely, a translated compactness limit of any admitted tiling has every Q at saturation t=3 and every P facing exactly one Q AA side. Every such saturated tiling is periodic with translation length

    |v| = 4r cos(18°),   r = 1/(2 tan(36°)).

No absence of defects in the given tiling is asserted.

Dependency: the reviewed necessary theorem `research/lemmas/complementary-angle-flow-necessary-theorem-2026-10-19.md` and review `research/reviews/complementary-angle-flow-hostile-sol-2026-10-19.md`. Its consequences needed below are reproduced explicitly.

## 1. Nonnegative deficits and purification

The only stars are PPA, PBC, BBB; all contacts are full-edge and three corners meet. Write q_R,p_R for tile-anchor counts in a side-R square. Boundary strips contain O(R+1) tiles, uniformly over translated windows, because the two fixed shapes have positive areas and bounded diameters. Incidence counts give

    p_R=q_R+O(R+1),
    sum_Q t(Q)=3q_R+O(R+1).

For the word AABBBBC the locally possible t values are 1,3. An AA edge must face a P and its two endpoints force the neighboring sides of that P to be PP. A pentagon cannot have consecutive PP sides and can receive at most one AA side. Let a(P) be 1 if P receives such a side and 0 otherwise. Counting the unique AA edge on each Q gives

    sum_P a(P)=q_R+O(R+1).

Therefore the integer-valued nonnegative local defects

    d_Q=3−t(Q),   d_P=1−a(P)

have total O(R+1) in every side-R window. This statement permits infinitely many defects.

For each integer L choose a sufficiently large square of side R. The union of radius-(L+2D) disks about defective tile anchors in a fixed-D enlargement of that square has area O((R+1)(L+2D)^2), with constants independent of R. The available interior has area of order R². Taking R sufficiently large produces a center whose radius-L neighborhood meets no defective tile. Translate that center to the origin. With L tending to infinity, extract a subsequence converging to a tiling by these same fixed shapes.

For completeness, this geometric compactness uses bounded tile diameter D, a positive minimum tile area, and compactness of the placement group over bounded translation ranges (orthogonal transformations include both reflection parities). Only uniformly finitely many tiles meet each fixed disk. Diagonal extraction of their placements preserves disjoint interiors; coverage follows because each point remains covered by a tile meeting a slightly larger disk. Surviving side incidences can also be extracted diagonally. The full-edge and star theorem applies to the limit. Every tile in a fixed disk inherits a defect-free incidence neighborhood, so its defect is zero. This produces another whole-plane tiling with both saturations simultaneously. It does not delete individual tiles from, or claim defect absence in, the original tiling.

## 2. Exact saturated contact graph

Label the Q vertices cyclically A0,A1,B0,B1,B2,B3,C. Its three PQ sides are A0A1, A1B0, CA0; its four consecutive QQ sides are

    B0B1, B1B2, B2B3, B3C.

B1,B2,B3 are BBB corners. B0 and C are PBC corners. The two A corners are PPA.

Every P receives its unique AA side. Its boundary species word is PP,PQ,PP,PQ,PQ, with the middle PQ side facing AA. It has exactly two PP neighbors and three PQ contacts. Its four PP endpoints are PPA; its remaining corner is PBC. Pair each P with the unique Q across its middle side. This is a bijection between all P and all Q.

Consider a PP edge between P and P'. At either endpoint the third tile is a Q with an A corner. Each pentagon has its AA-facing side adjacent to this PP edge at exactly one endpoint. Those selected endpoints must be different: otherwise the single third Q at the selected endpoint would have both incident sides facing AA-receiving P tiles; both sides would have to be AA edges of that Q. Q has exactly one AA edge. This is impossible. The argument is in physical endpoint terms and is independent of reflection parity.

Thus PP components are chains. Index one by P_n and write Q_n for its paired Q. At a PP junction, the Q paired to one pentagon also faces the other pentagon along the Q side adjacent to AA. Full-edge contact makes this the entire side. Consequently the full PQ neighborhood is exactly

    P_n adjacent to Q_(n−1), Q_n, Q_(n+1),
    Q_n adjacent to P_(n−1), P_n, P_(n+1).

The unique PBC corner of P_n consists of P_n,Q_(n−1),Q_(n+1). In particular the latter two Q tiles have a QQ edge there. Each Q has two such outer QQ contacts with Q_(n−2) and Q_(n+2), using its first and last QQ sides. The remaining two consecutive QQ sides B1B2 and B2B3 meet other Q tiles; their endpoints are all BBB. These latter contacts need not be classified to establish periodicity. Their other incident tiles can belong to the same or another PP carrier; no unsupported transverse pairing is imposed.

## 3. Alternating turns give an exact return

Let c_n be the centers of P_n and r the pentagon apothem. Across a full PP side, centers have distance 2r along its normal. The two PP sides of a pentagon have outward normals differing by 144°; therefore traversing a PP chain turns the center path by +36° or −36°. The physical opposite-endpoint condition just proved forces successive signs to be opposite. This can be checked without choosing a tile chirality: if the shared outward normal of the first pentagon is angle 0 and its AA normal is +72°, the next pentagon has shared normal 180° and, because its selected endpoint is opposite, AA normal 252°. Its other PP normal is 324°. Reversing the initial choice reverses all signs.

Hence the successive displacement vectors alternate between fixed vectors u,w of length 2r and mutual angle 36°. They satisfy

    c_(n+2)=c_n+v,   v=u+w,
    |v|=4r cos(18°)>0.

Translation by v sends P_n exactly to P_(n+2), including its AA-facing side. In particular there can be no finite PP component: the same propagation around a putative cycle would contradict this nonzero two-step displacement. Every component is a doubly infinite zigzag, a graph over its v-axis and a bounded distance from a straight line.

## 4. The Q decoration has the same return

There are at most two placements of fixed Q on a prescribed AA edge and its prescribed side. Both A angles are equal, so the two adjacent sides CA0 and A1B0 have the same rays for these two placements. Both have length one, since they face P. These two placements interchange which of their far endpoints has label B0 and which has label C. The labels are distinct (120° versus132°), so the placements are distinguished by this choice.

For each Q_n record the label at the end of its flanking PQ edge toward P_(n+1). At the PBC corner of P_n, Q_(n−1) contributes its forward label and Q_(n+1) its backward label. The backward label of each Q is the complement B↔C of its forward label. Since a PBC star requires opposite labels, the forward labels for Q_(n−1) and Q_(n+1) agree. Thus this binary choice has period two.

Here is the complete recurrence table. Define F_j to be the non-A endpoint on Q_j's flanking PQ side shared with P_(j+1), and H_j the endpoint on its flanking PQ side shared with P_(j−1). They are B0,C in some order. Let s_j be the angle label of F_j. Then label(H_j)=complement(s_j). At the sole PBC corner of P_n the Q labels are exactly label(F_(n−1)) and label(H_(n+1)).

| s_(n−1) | s_(n+1) | actual pair at P_n | allowed? |
|---|---|---|---|
| B | B | B,C | yes |
| B | C | B,B | no |
| C | B | C,C | no |
| C | C | C,B | yes |

Both reflection cases are included explicitly as follows. For the base pentagon with shared PP outward normal 0, the AA outward normal can be +72° or −72°. In the +72° case use the first row of the following table; mirror reflection produces its second row. In either row, the two possible reflected Q placements on a prescribed AA edge are indexed by s_j=B and s_j=C, respectively.

| PP/AA normal choice | placement with s_j=B: (F_j,H_j) | placement with s_j=C: (F_j,H_j) | PBC test |
|---|---|---|---|
| 0,+72° | (B0,C) | (C,B0) | preceding table |
| 0,−72° (mirror) | (B0,C) | (C,B0) | preceding table |

This is a physical-incidence table, not a native counterclockwise convention: F always means toward increasing chain index, so reflecting the entire configuration preserves the table. The two AA-edge placements are distinguished by this label even when reflections of Q are allowed. The P geometry after two steps repeats by translation, so F_(j+2) is the translated forward side of F_j; there is no implicit reversal on the two-step return.

The geometric AA edge and half-plane already repeat after translation by v; the period-two label choice now fixes the entire Q placement. Therefore

    Q_(n+2)=Q_n+v.

Each decorated carrier, consisting of all P_n and Q_n in one component, is invariant under translation by v. No assumption about the four-side QQ continuation or an extension of a finite patch has entered this conclusion.

## 5. All carriers have a common period

For each PP component draw its center path, joining consecutive pentagon centers through the midpoint of their common PP edge. This path lies in P interiors except at these shared midpoints. Paths of distinct components are disjoint: two components have disjoint P interiors, and coincidence at a shared PP midpoint would make them the same component.

Each path is a proper embedded zigzag, is a graph over its axis, and has bounded distance from that straight axis. Two such paths with nonparallel axes must intersect. Indeed the first separates the plane into its two graph sides, and the two tails of a path with a nonparallel axis eventually lie in opposite sides, forcing intersection. Therefore all PP component axes are parallel.

Every two-step return has the same length 4r cos(18°). With parallel axes their vectors are consequently v or −v. Every decorated carrier is invariant under the same translation v. The AA pairing partitions every tile of the saturated tiling among these carriers. Their union, the whole tiling, is therefore invariant under v.

## Scope, audit targets, and restart state

This supplies a new exact return mechanism rather than a bounded enumeration: simultaneous nonnegative saturation permits purification; the AA endpoint rule forces alternating PP turns; PBC forces period-two Q placement; disjoint proper PP paths align all carrier axes. The independent hostile review passed these steps. This exact metric-word branch cannot furnish an aperiodic pair.

The most consequential audit targets are the physical endpoint argument in section2, the orientation-independent forward/backward label propagation in section4, and the proper-path separation in section5. No claim is made that every metric Q with this word tiles, nor that an arbitrary original tiling has zero defects or is periodic. The implication is precisely: any tiling implies existence of a periodic tiling. No additional search or torus enumeration is needed for this implication.
