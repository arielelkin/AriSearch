# Interleaved/alternating hexagons: private native seams and complete AB length alphabet

Date: 2026-10-12. Status: [independently reviewed VALID](../reviews/two-hexagon-interleaved-alternating-private-seams-review.md).

Use the exact rank-nine same-colour AAB family in
[two-hexagon colour transport](two-hexagon-rank-nine-colour-transport.md).
Fix native A word I=(p,p,q,p,q,q) and B word ALT=(r,s,r,s,r,s), with
p+q=240, r=360-2p, s=2p-120, 90<p<150 and p!=120. A side j joins
native corners j and j+1. Reflections and repeated lengths are permitted.
The conclusions below concern the reviewed defect-free trivalent limit of
any original tiling; the original tiling need not have whole-side contacts.

## Whole-side species and native-index forcing

Every B side has endpoints of opposite corner colours. Thus native A sides
0 (p,p) and4 (q,q) cannot meet B. In the one-B species phase, every A has
three A neighbours and three B neighbours, alternating around its six sides.
Any native placement preserves side-index parity as a partition, even under
reflection. Since sides0 and4 meet A, precisely the even native sides0,2,4
meet A; the odd sides1,3,5 all meet B.

Across an AA seam, the two A corner colours at either endpoint must agree.
Among the three even sides, side0 alone has endpoint pair(p,p), side4
alone has(q,q), and side2 alone has(q,p). Consequently ALL AA seams match
the same native side index: 0-to-0,2-to-2 or4-to-4. At side2 the unequal
endpoint colours force native corner2 to meet corner2 and corner3 to meet
corner3. The neighboring congruent A copy across the seam is therefore its
reflection across the supporting line, not a half-turn. At homogeneous
sides0,4 both endpoint correspondences remain locally allowed; reflection
and half-turn joins must both be retained until a further obstruction is
proved. Coincidence of lengths does not change any of these angular facts.

## Complete finite metric alphabet on AB seams

Put x=A1,y=A3,z=A5 for the three positive odd-native A side lengths. Every
B native side length lies in {x,y,z}, since all its seams meet odd A sides.
Partition the three native indices1,3,5 into blocks of equal actual length.
For each block U, exactly 2*|U| of the six native B sides have that length.

To prove the multiplicity statement without a frequency assumption on an
individual tiling, average translates of a legal full-state lattice field
to obtain an invariant probability measure. The one-B species phase gives
A density2/3 and B density1/3. Each A copy contributes |U| AB sides of the
chosen length, and each B copy contributes n_U such sides. Counting the
same seams from either end gives (2/3)*|U|=(1/3)*n_U, so n_U=2*|U|.

There are only five partitions of the three native odd indices. With three
distinct lengths the B native word has two occurrences of each of x,y,z,
so there are 6!/(2!^3)=90 labeled words before native dihedral quotient.
With two length blocks the multiplicities are4 and2; with one block all
six B sides are equal. These cases form a complete necessary metric word
domain. Further coincidences with even A lengths introduce no additional
AA choices: native-index forcing already restricts those seams. They may
therefore be treated as additional equalities after the AB word census.

This is a transport and metric-domain restriction, not an extension or
periodicity theorem. A surviving local ring or permitted B length word
has not been proved geometrically realizable or globally extendible.
Periodic witnesses still must match the actual fixed polygons, and failure
of a bounded periodic search supplies no impossibility conclusion.
