# Complementary-angle necessary theorem

Let P be a unit regular pentagon. Let Q be a fixed strictly convex polygon whose native angles belong to A=144°, B=α, C=252°−α, with 108°<α<126°. Suppose copies of P and Q tile the plane under arbitrary isometries and contacts; either species may be omitted. This theorem gives necessary conditions only. It does not assert that any listed Q tiles.

**Theorem.** Every contact is full-edge and every vertex has three corners. When α≠120°, the stars are PPA and PBC, Q has equal numbers b=c of B and C corners, and its angle word up to rotation and reversal belongs to one of these lists:

* Seven sides: `ABBBCCC`, `ABBCBCC`, `ABBCCBC`, `ABBCCCB`, `ABCBBCC`, `ABCBCBC`, `ABCBCCB`, `ABCCBBC`, `ACBBBCC`, `ACBBCBC`.
* Eight sides: `AAABBACC`, `AAABCABC`, `AAABCACB`, `AAACBABC`, `AABBAACC`, `AABCAABC`, `AABCAACB`.

At α=120°, the same balanced words survive the stated necessary conditions. Additionally, `AABBBBC` is the only surviving word with counts (a,b,c)=(2,4,1), and `BBBBBB` is the only surviving word with counts (0,6,0). In the latter case any tiling is Q-only. All nine- and ten-sided inventories, and the resonant (5,3,0) inventory, are excluded. Here B and C are distinct labels even at the resonance: their angles are 120° and 132°.

**Proof.** Every angle is strictly above 108° and below 180°. Two native corners cannot fill a vertex, four exceed 360°, and a vertex in another tile's open side would require one corner of 180° or at least two corners totaling 180°; both are impossible. Thus contacts are edge-to-edge with three corners. Exhausting triples gives PPA and PBC identically, plus BBB exactly at α=120°.

Let p_R,q_R count tile reference points in a square of side R, and x_R,y_R,z_R count PPA,PBC,BBB vertices there. Fixed positive tile area and diameter bound all boundary errors by O(R+1). If Q has counts a,b,c, incidence counting yields

`x_R=a q_R+O(R)`, `y_R=c q_R+O(R)`, `b q_R=y_R+3z_R+O(R)`, and `5p_R=2x_R+y_R+O(R)`.

Coverage, the last identity, and positive tile areas force `q_R=Ω(R²)`; hence there is no hidden zero-frequency Q exception. Off resonance z_R=0, so b=c. The Q angle sum then gives a+3b=10 and the four possible inventories (a,b,c)=(10,0,0),(7,1,1),(4,2,2),(1,3,3). At resonance z_R≥0 gives b≥c; the angle sum gives `3a+5b+4c=30`, whose nonnegative solutions satisfying b≥c are (0,6,0),(1,3,3),(2,4,1),(4,2,2),(5,3,0),(7,1,1),(10,0,0).

At a non-A corner away from resonance exactly one incident Q side faces Q. The QQ sides form the unique perfect matching on each cyclic non-A run; each such run has even length. A physical QQ endpoint joins B to C, even with reflected copies. At resonance B corners assigned BBB instead have two QQ sides and join B to B at those endpoints; C still has exactly one QQ side. Let t(T) count such B corners on one Q. Counting BBB incidences gives `Σt(T)=(b−c)q_R+O(R)`.

An AA side of Q requires a distinct adjacent P with a PQ side flanked by two PP sides. The five-cycle of P permits at most one such side per P, so if m is the number of AA sides of Q then `m≤(2a+c)/5`. This excludes the nine- and ten-sided inventories, and words with an excessively long A run. For resonant (5,3,0), a non-A run must contain all three B corners and yields m=4>2. For (2,4,1), a word with separated A corners has non-A runs of lengths 2 and 3 and t≤1; with adjacent A corners, t=3 is possible only if the run's three interior positions are B and its C lies at an endpoint. That is `AABBBBC` up to reversal. The exact finite dihedral enumeration of remaining balanced words gives the two displayed lists. It enumerates all labeled words and cyclic QQ subsets; it imposes only necessary local degrees, AA capacity, and the global t budget. Its independent Sol review reproduced the counts and survivors.

The square-window estimate, endpoint rules, full word table, exact replay, and discussion of sparse resonant defects are in [the complete gate](../searches/complementary-angle-flow-sol-2026-10-19.md). The [independent hostile review](../reviews/complementary-angle-flow-hostile-sol-2026-10-19.md) passed the necessary theorem, with one wording correction incorporated in that report. Neither document supplies a metric realization, plane extension, or periodicity/aperiodicity proof for the survivors.
