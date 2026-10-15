# Same five lengths, same doubled length, separation two: a complete hexagon-family escape

Date: 2026-10-15. Status: independently hostile-reviewed VALID; [review](../reviews/hexagon-shared-repeat-separation-two-hostile-2026-10-15.md). This classifies the stated restricted family, not arbitrary two hexagons.

## Theorem

Let A,B be genuine convex hexagons. Suppose each has exactly five distinct physical side lengths, both have the SAME set of five lengths, the same length r is doubled in both, and the two occurrences of r have cyclic separation two in each hexagon (one intervening side on the shorter arc). If the unmarked pair tiles the plane with arbitrary rotations, reflections and partial contacts allowed, it admits a full-side tiling with two independent translations.

Stronger source variant: assign five DISTINCT FORMAL COLORS r,x,y,z,t to native sides, with each polygon using all five and doubling r at cyclic separation two. Same-colored sides have a common positive physical length; different colors may have equal physical lengths. If an indexed, color-matching, full-side everywhere-trivalent plane tiling exists, the underlying unmarked shapes admit a full-side doubly periodic tiling.

Up to a common renaming of the five colors and independent cyclic rotation or reflection of the two native words, the only cyclic-word orbit that can admit such a source is

    A=(r,x,r,y,z,t), B=(r,z,r,y,x,t).

This last assertion is necessary, not sufficient for arbitrary metrics in that orbit. The reviewed theorem for that orbit supplies a periodic escape whenever its source exists.

## 1. Canonical domain, including the full symmetry reduction

Normalize A=(r,x,r,y,z,t). Every separation-two B word can independently be rotated and reflected to

    B=(r,m,r,a,b,c),

where (m,a,b,c) is a permutation of (x,y,z,t). A fixed middle symbol m has six choices for (a,b,c); reflecting B exchanges a and c and fixes m,b. Thus the complete24-permutation domain reduces to12 tuples by the convention a<c in the label order x<y<z<t.

There is one further nontrivial relabeling preserving the normalized A up to its own reflection: sigma exchanges y and t and fixes r,x,z. Indeed reflection of A, followed by a suitable cyclic rotation, gives (r,x,r,t,z,y); applying sigma returns A. This symmetry acts on B by applying sigma to each symbol and then normalizing its independent reflection again.

There are no missing stabilizers: r is the only doubled symbol; x is the unique singleton on the short r-to-r arc; the long arc is the ordered path y,z,t. An automorphism of this cyclic word must fix r and x, and can only preserve or reverse that long path. It therefore fixes z and either fixes both y,t or exchanges them. The certificate also exhausts all24 singleton-label permutations against all12 dihedral images of A and recovers precisely these two stabilizers.

The resulting domain has SEVEN orbits, not six. The middle-x pendant cases contribute two orbits, and there are five remaining orbits. The complete table follows; each tuple is (m,a,b,c), without the two displayed r entries.

| Representative tuple | Other normalized tuple in its orbit | Result |
|---|---|---|
| (x,y,z,t) | none | pendant-x obstruction |
| (x,y,t,z) | (x,z,y,t) | pendant-x obstruction |
| (y,x,z,t) | (t,x,z,y) | new empty star atlas |
| (y,x,t,z) | (t,x,y,z) | new pruning8 to0 |
| (y,z,x,t) | (t,y,x,z) | previously proved pruning12 to1 to0 |
| (z,x,y,t) | (z,x,t,y) | new pruning12 to1 to0 |
| (z,y,x,t) | none | reviewed periodic escape |

The two seemingly different proposals B=(r,z,r,x,y,t) and B=(r,z,r,x,t,y) are the SAME orbit. No exchange of the prototype types is needed for exhaustiveness; such an exchange could only identify cases further.

## 2. Native-star and full-side propagation mechanism

Use the formal source variant throughout. Native corner i lies after side i, between sides i and i+1, with indices0,...,5 for A and6,...,11 for B. Neither word has equal adjacent colors. At a trivalent source vertex, its three ray colors must consequently be distinct. Its three native corner arm pairs are the three edges of a triangle in the union color graph.

The complete star atlas is therefore obtained by choosing three different native corners whose three distinct unordered arm pairs form such a triangle. Repeating a native corner cannot give a three-distinct-ray triangle, so no repeated-corner case is omitted. This argument uses distinct formal symbols, not distinct physical lengths.

For two corners c,d of a star, their unique common ray color identifies the seam and the particular native side at each corner. Because the source is full-side, at that seam's other endpoint the corresponding two far native corners must belong together to an actual star. Let K0 be the complete atlas and let K_(j+1) remove from K_j every star having a seam with no such far-end completion in K_j. Inductively every actual source star belongs to every K_j: its actual far-end star survives whenever all actual stars survive. If any K_j is empty, no source tiling exists. No local survivor is ever asserted to extend globally.

## 3. The six excluded orbits

For the two m=x orbits, color x is adjacent only to r in BOTH native corner graphs. Thus no graph triangle contains the rx edge, although the native rx corners occur on every copy of either prototype. No full-side trivalent source exists. This also rules out a source using only one prototype.

For the three new nonpendant representatives, the complete certificates give:

| B word | Complete initial atlas size | Successive sizes |
|---|---:|---|
| (r,y,r,x,z,t) |0|0|
| (r,y,r,x,t,z) |8|8,0|
| (r,z,r,x,y,t) |12|12,1,0|

For every deleted star, the retained certificate names the two seam corners, common ray color and their far native corners, and the current atlas in which no completion exists. The first word has no native star at all. The last word's sole first-round survivor is (4,6,11); across its color-z seam between corners4 and6, the far pair is (3,7), absent from that singleton atlas. Thus the last deletion is explicit as well.

The [new exact producer](../searches/hexagon-shared-repeat-separation-two-remaining-2026-10-15.py) exhausts all original subsets too:1,256,4096 masks respectively, retaining corner coverage and all seam continuations. None survive. This supplemental check is not required by the stronger empty-atlas propagation proof.

The remaining excluded nonpendant orbit is B=(r,y,r,z,x,t). Its complete twelve-star atlas and12-to1-to0 propagation were already established in [the earlier single-family obstruction](../searches/hexagon-shared-repeat-single-family-2026-10-15.py), with [independent native reconstruction](../reviews/hexagon-shared-repeat-single-family-independent-2026-10-15.py). The proof only uses native color equality, different adjacent colors and full-side continuation. It therefore applies unchanged to formal colors even when their physical length map is noninjective. No numerical inequality is used in this excluded branch.

This excludes six of the seven canonical orbits under precisely the stated formal source hypotheses.

## 4. The sole surviving orbit and unrestricted transfer

For B=(r,z,r,y,x,t), apply the independently reviewed [changed-family theorem](hexagon-shared-repeat-changed-family-periodicity-2026-10-15.md), including its explicit stronger formal-color source version. Its exhaustive171-support source domain yields169 literal flat-torus witnesses and two exact deterministic source supports. Both routes produce two independent translations for the underlying unmarked shapes. The source theorem explicitly permits a noninjective color-to-length map and physical polygon symmetries, carrying the given source indexing in the deterministic branch.

This proves the formal source statement. For the numerical unrestricted theorem, start with any admitted tiling of the two genuine convex hexagons. The reviewed [defect-free limit theorem](hexagon-limit-and-periodicity.md) supplies a full-side everywhere-trivalent tiling of those same shapes. Assign each native side its physical-length color; the five numerical lengths are distinct and shared, so every full-side seam matches its color. This is exactly a source of the kind just classified. Its unmarked pair therefore has the asserted periodic escape. QED.

## Reproducibility, review and scope

[Complete new certificate](../certificates/hexagon-shared-repeat-separation-two-remaining-2026-10-15.json).

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-shared-repeat-separation-two-remaining-2026-10-15.py

Default stdout is the full deterministic JSON certificate. Passing --output PATH additionally writes the identical text to that path. Computation uses only finite tuples, sets and exact integer indices. There is no solver, numerical metric search, angle sampling, or enlarged periodic quotient. The finite domains are24 B permutations,12 canonical reflected tuples,24 A relabelings checked against12 dihedral images,7 final orbits, and the three explicitly listed new native atlases.

Independent review must audit canonical exhaustiveness, the exact seven-orbit action, reflected native endpoint continuation, transfer of the old killed-word proof to formal colors, the already-reviewed surviving source theorem, and the unrestricted defect-free limit dependency. The root owns that review and any final status promotion.

Pairs with different sets of five numerical lengths, different doubled numerical values, adjacent or opposite repeat separation, more repeated lengths, or a pentagon remain outside this theorem. The original unrestricted objective remains unresolved.
