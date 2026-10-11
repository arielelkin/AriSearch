# Fresh written-artifact review: direct common period with distinct native lengths

**Verdict: VALID without repair.** The reviewer did not develop the root's
[direct theorem](../lemmas/distinct-length-obtuse-direct-common-period.md).
This audit checks the extracted written proof, following an earlier fresh
check of the proposed argument. No computation is used or required.

The exact claim is that every admitted original tiling by an all-obtuse
pentagon P and all-obtuse n-gon Q, n>=7, each with internally pairwise distinct
native lengths, has at least one nonzero translation period. Numerical
lengths may be shared across species. Reflections and unrestricted original
contacts are allowed. The separately reviewed n>=8 untileability and n=7
rank-two witness classification are dependencies only for the comparison
with the older result, not for this new analytic period proof.

At a trivalent vertex all three ray lengths are distinct: every pair is the
adjacent native pair of one tile. A monochromatic star would require a
triangle of adjacent lengths in its simple C5 or Cn native cycle, impossible.
Thus neither PPP nor QQQ occurs, including omission of one species.

A Q-Q full seam matches the same unique native Q side. The four segment-
preserving isometries are correctly exhausted. Identity and perpendicular-
bisector reflection preserve the interior half-plane and overlap; the two
support-opposite alternatives are side-line reflection and midpoint
half-turn. For side-line reflection, the outer rays at each fixed endpoint
are equal copies of one native adjacent Q side. Its third tile must be P,
which would need equal adjacent sides. This violates P's internal
uniqueness. The half-turn conclusion therefore applies to every Q-Q seam,
not only to a selected private subset and not only in a good limit.

At most five Q values appear on P, so two fixed distinct native Q-private
slots exist. Their two mates always have type Q. Selecting just these slots
makes a degree2 graph on every Q occurrence, even in the presence of other
Q contacts. Its two neighbors are different because sharing two genuine
noncollinear whole sides would cause positive-area convex overlap. The
midpoint chords lie in Q interiors and half-turn continuation forms entire
straight axes, with no finite cycle or unexamined Q component. All axes
are disjoint: open chord intersection causes interior overlap, and at an
endpoint a full-side midpoint has only its two actual side mates. Hence
axes are parallel. All chain period vectors have the same length, so one
nonzero u and its negative preserve the entire actual Q tile set.

PPP exclusion gives every P at least three Q side slots, hence two
consecutive ones and a PQQ corner. Translation by u takes its prescribed
Q pair and two whole P segments to actual copies. If the translated third
tile were Q, its translate by -u would be an actual Q occupying an open
sector inside the original P. This is impossible. The third tile is P;
two distinct native P lengths select unique native sides and their unique
common corner. Their noncollinear endpoints fix one placement, including
reflections. Thus it is exactly P+u. Repeating for -u proves equality of
both species' tile sets under the translation.

No circular use of a periodic torus, good-limit saturation, rational angles,
finite-state assumption or area-frequency argument was found. The proof
does not infer that every original tiling has two independent periods;
one nonzero common period is the complete assertion. It does not cover
repeated native lengths or nonobtuse angles, and is consistent with the
older no-tiling theorem for n>=8. No novelty claim was audited.
