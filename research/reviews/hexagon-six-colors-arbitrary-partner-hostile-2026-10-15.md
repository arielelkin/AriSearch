# Independent hostile review: six colors versus an arbitrary hexagon partner

Date: 2026-10-15. Verdict: **VALID** for the exact indexed full-side trivalent
source theorem and actual-seam necessity corollary. This is not a complete
two-polygon result. The reviewer did not author the general transfer.

Reviewed artifact:
[hexagon-six-colors-arbitrary-partner-2026-10-15.md](../lemmas/hexagon-six-colors-arbitrary-partner-2026-10-15.md).
I read its three-sharing, narrow double-pair, general periodic-chain and
uniform-unavoidability dependencies. The previously reviewed B-five/six
formal-color bridge was checked again at its relevant hypothesis boundary.
No discovery log, registry or Git state was modified.

## 1. Exact source and target; monohedral branch

The source is a geometrically valid, everywhere-trivalent full-native-side
plane tiling with a fixed reference indexing on every occurrence. A has
six different side COLORS; B's color word is unrestricted. Equal colors
prescribe equal physical lengths, but differently colored slots may have
the same physical length, and either physical polygon may be symmetric.
Seams in this given source match colors. The desired witness is UNMARKED
and requires just one nonzero translational period.

The first monohedral escape is correctly about unmarked shapes. A B-only
UNMARKED tiling need not be compatible with B's source color word; its
reviewed monohedral periodic escape nevertheless answers the target.
The proof can therefore assume both unmarked types individually untileable.
This is exactly the physical hypothesis needed by uniform unavoidability
later. Excluding only colored monohedral tilability would not suffice,
but that erroneous exclusion is not made.

The reduction is exhaustive: after the reviewed B-five/six-color branch,
B has at most four colors. If at most three are shared, Section 1 applies.
Otherwise B has exactly four colors and all four are shared, with the
only possible six-slot multiplicities (2,2,1,1) or (3,1,1,1).

## 2. Private COLOR is sufficient for the source AA rules

I specifically attempted to replace private colors by physically shared
lengths, including the extreme assignment ell(c)=1 for EVERY color.
No inference fails. A private color u is absent from B's native word;
therefore the source neighbor across u is A. A has only one u slot, so
the ACTUAL indexed neighbor uses that same slot, even if B or other A
slots have physically equal sides. Extra uncolored placements are irrelevant
to this source step.

For that same-slot AA match there are precisely two opposite-interior
indexed maps. With the reference side on a horizontal segment, endpoint
preservation leaves identity and reflection in the side line; only the
reflection sends the neighbor interior to the opposite side. Endpoint
exchange leaves the midpoint half-turn and reflection in the perpendicular
bisector; only the half-turn sends the interior to the opposite side.
These statements do not require physical asymmetry or unequal lengths.

At a reflected private seam, both endpoint-adjacent A rays have the same
color x at one end and the same color y at the other, with x!=y as COLORS.
The third corner at either end cannot be A, because A has no equal adjacent
colors. It must be a B corner with arms xx or yy respectively. Even if
ell(x)=ell(y), these are TWO different required color loops in the source.
A B word with multiplicities (3,1,1,1) can have loops at only its tripled
color. Hence both designated private seams are forced half-turns. Physical
coincidence does not turn two color loops into one.

Reference symmetries also cannot alter this conclusion: the source supplies
one actual indexed isometry per occurrence, and the ordered side endpoints
and the interior half-plane determine the complete relative isometry.
Choosing different native slot indices because their lengths coincide
would violate the given color matching and is not an allowed inference.

## 3. Three shared colors and framed A-carrier propagation

The isolated-private-color argument is valid. At a corner with two private
A colors, both neighbors would be A; an AAA vertex has three distinct ray
colors and would give a triangle in A's six-cycle, impossible. At most three
shared colors therefore means exactly three, alternating with three private
colors. Every A corner is AAB, all shared A sides meet B, and following
full sides around any B touching A makes all six of its sides AB. Full-side
adjacency connectivity propagates this to all B tiles. Thus there are no
B-private colors and every vertex is AAB.

The disk-boundary incidence estimates use physical areas, diameter bounds
and inradius packing, all valid with coincident side lengths. They force
B's three shared colors to occur twice each. No limiting frequency or
injective color-length map is assumed.

The corona rule is intrinsic to native COLORS. At either end of a B side,
its A neighbor's unique corresponding color slot has different adjacent
private slots. The two endpoint private choices must therefore differ.
The direct classification leaves xyzxyz and xxy zzy. An independent checker
below also enumerates all ninety double-each three-color words and their
permitted corner-private assignments, giving exactly these two classes.

For xyzxyz, opposite colors give equal physical lengths, and same private
AA seam formulas give opposite equal angles. Three consecutive exterior
turns sum to pi, so opposite directed edge vectors are negatives; B is
centrally symmetric and has its unmarked lattice escape.

For xxy zzy, missing COLOR loops force two private half-turn maps and one
private side reflection. These are complete maps between indexed A frames.
The private-AA graph is connected: the A neighbors surrounding each B form
an AA cycle, and there are no BB contacts. Any full adjacency path through
B can be replaced by that cycle. This is a statement about actual source
tiles and their full sides, not a connected graph of merely allowed seams.

For two indexed A copies U,W, transport g_W g_U^(-1) commutes with all three
private neighbor operations. Its image on the A graph contains W and is
closed under every graph edge. Connectedness makes the image all A tiles,
with their frames. No uniqueness of a physical A frame inferred from its
shape is used. Since every B edge is AB and every vertex AAB, the complement
of the closed A union is precisely the disjoint union of B interiors.
Transport permutes its connected components and hence unmarked B closures.
B frames need not be preserved or recovered. The resulting group is discrete
and cocompact, with finitely many B orbits; finite physical symmetry groups
are sufficient for discreteness. The reviewed planar-group argument gives
a rank-two translation lattice. Thus this carrier argument survives physical
A symmetries and coincident side lengths.

## 4. Double-pair finite lemma interpreted as colors

The narrow producer's 2,160-word domain, 192 cyclic words, actual-corner
multisets, all native-arm flip assignments, endpoint pruning and formal
rings use only label equality and native indices. Its canonical integer
ordering selects representatives; it is not an ordering of physical lengths.
Normalizing A's private positions by a dihedral reindexing likewise does
not presume that reindexing is a physical symmetry of A. Actual angles
and native slots are carried with the reindexing.

The source support is consequently among the same ninety-three retained
closed covers. Seventy-one provide direct ring inclusions. The other
twenty-two provide four exact rational row combinations each, of occurring
star equations and the two hexagon angle sums. Those equations hold for
the actual physical angles regardless of the color-to-length map.
Every target ring match has equal colors, or pairs the same private native
slot between copies of its own type. Its physical side lengths agree.
The flat four-face torus and complete plane cover are unchanged.

I reran the small independent row-certificate checker. It returned PASS
for all twenty-four feasible words, seventy-one direct supports and all
eighty-eight target row identities in the twenty-two remaining supports.
No solver, metric inequality or new finite-domain interpretation is hidden
in this transfer. Its complete enumeration remains the already independently
reviewed finite lemma, rather than a numerical extrapolation here.

## 5. Audit of the geometric-chain and strip dependency

The original periodic-chain theorem's statement uses private numerical
lengths and six distinct physical lengths. Invoking that statement alone
outside its hypotheses would be invalid. The new artifact instead supplies
the missing SOURCE-specific indexed half-turn derivation and audits the
rest of the original proof. I checked each remaining use directly.

After the two forced indexed half-turns are known, Sections 2–5 of the chain
proof need only:

1. Two distinct designated native side slots, with those same-slot half-turn
   neighbors at every A occurrence.
2. Fixed compact convex shapes with positive inradii and bounded diameters.
3. The original full-side source, and physical non-tilability of B alone.

No remaining use requires the designated colors to be private PHYSICAL
lengths. The two edge midpoints are distinct because edge interiors of
a genuine convex polygon are disjoint. Their half-turn product therefore
has nonzero translation vector 2(m_v-m_u), even if u and v have equal physical
lengths. Every component of the SELECTED private-color AA graph has two
indexed placements per period. Additional A-A contacts through other colors
or metric coincidences do not change these selected components.

The anchor-to-midpoint separator curves lie in A interiors or the interiors
of their selected full AA seams. Different components cannot meet there,
regardless of extra physical equalities. Proper noncrossing periodic curves
force parallel axes and a common period vector up to sign. All A tiles
belong to selected components, so their union has that common period.
This does not itself assert that its arbitrary B filling is periodic.

The reviewed uniform-occurrence theorem applies to the UNMARKED shapes
because B-alone tilability was excluded first. Consequently consecutive
bands have uniformly bounded width. In a band, a bounded adjacency path
to a chosen lower-chain A yields a finite set of exact B placements modulo
the common period. With physical symmetries and equal lengths there are
more possible native side and endpoint correspondences, but still finitely
many: each reference has only six actual sides and two endpoint orders.
Their opposite-half-plane extensions fix complete relative maps. Products
of uniformly bounded path length remain finite. The boundary A chain has
two SOURCE-indexed placements modulo its period because its forced maps
were derived at the indexed level. No asymmetric physical-A anchor choice
or finite absolute orientation assumption is needed.

The band no-overlap and coverage constraints then form the same finite-window
one-dimensional SFT as in the reviewed chain proof. They concern physical
polygon placements only. The original B filling is admitted, so a finite
graph cycle provides a periodic replacement. Uniform candidate and memory
bounds synchronize periods across all bands. The final B placement choices
may violate the auxiliary color rule, which is allowed by the UNMARKED
target. Ignoring colors at this final stage cannot invalidate geometric
coverage or disjointness. Thus the full geometric/SFT bridge genuinely
transfers; it is not an unsupported periodic-skeleton assertion.

## 6. Actual-seam necessity and exact limits

For any chosen indexing of an admitted full-side trivalent unmarked tiling,
let E be generated by its ACTUAL full-seam native slot pairs. Transitivity
preserves physical length equality. Coloring native slots by E classes
makes every source seam color-matched. If no E class contains two A slots,
A has six colors, and the new arbitrary-partner theorem applies regardless
of B's color count. It yields an admitted unmarked periodic escape.
Exchanging species gives the symmetric condition.

Therefore an aperiodic two-hexagon pair would have to join two different
native slots of BOTH species through occurring seam types, in every indexed
defect-free tiling. It is not enough that compatible but unused seams could
connect them. Connected slots necessarily have equal physical lengths.
This proves the stated necessity and makes no sufficiency or existence claim.
The unrestricted limit is used before defining E, so no unsupported
color-preserving limit is assumed. Pentagon-containing pairs and the residual
connected cases remain outside the theorem.

## Replay, defects and verdict

The new reviewer checker is
[hexagon-six-colors-arbitrary-partner-independent-2026-10-15.py](hexagon-six-colors-arbitrary-partner-independent-2026-10-15.py).
It imports no author producer. It checks all ninety three-color double-each
words and corona assignments, the forced modes for the double-block word,
and all 960 raw four-color words of multiplicities (3,1,1,1) across the two
private-side normalizations. All 1,920 tested private-seam flank pairs fail
the two-loop requirement, even with ell(c)=1 for every color. This is a
finite incidence check, not an inference of global geometry from abstract
angle data.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-colors-arbitrary-partner-independent-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-four-row-certificate-check-2026-10-15.py

Both commands completed with exit status 0. The universal framed carrier
and strip implications are proved and audited above; they are not certified
by a metric sample or merely by failure to find a counterexample.

No mathematical defect requiring author repair was found. **Final verdict:
VALID**, under the exact full-side colored-source assumptions and reviewed
dependencies stated in the artifact. The conclusion is existence of one
unmarked nonzero-translational escape; no aperiodic pair, full two-hexagon
classification or universal impossibility theorem is claimed.
