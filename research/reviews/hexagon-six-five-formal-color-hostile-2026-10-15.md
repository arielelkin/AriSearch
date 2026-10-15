# Independent hostile review: formal-color periodic escape

Date: 2026-10-15. Verdict: **VALID** for the precise full-side trivalent
colored-source theorem and its actual-contact-component corollary.
The reviewer did not author the formal-color transfer or its indexed-state
argument. No discovery log, registry or Git state was modified.

## Exact claim and dependency boundary

Reviewed artifact:
[hexagon-six-five-formal-color-periodic-escape-2026-10-15.md](../lemmas/hexagon-six-five-formal-color-periodic-escape-2026-10-15.md).

A and B are indexed genuine convex hexagons. A has six native side COLORS;
B has five or six. Equal colors have equal positive physical lengths,
but different colors may have identical lengths. A colored, full-native-edge,
everywhere-trivalent indexed source tiling exists and every seam matches
colors. The conclusion is a doubly periodic tiling by the underlying
unmarked shapes. Reflections are allowed. The source-color rule is auxiliary
data, not an added restriction in the final unmarked problem.

The source theorem does not claim that a partial-contact colored tiling
has a color-preserving defect-free limit. The corollary first takes an
UNCOLORED defect-free limit and then colors its actual native contacts.
This order is necessary and correctly stated.

## Attack 1: noninjective physical length map

The reused enumerations take only integer equality labels, cyclic side
words, native indices, finite sets/multisets and endpoint incidence. Inspection
of their four independent verifiers found no inequality between different
physical lengths or hidden requirement that distinct labels have distinct
real lengths. Their labels may therefore be interpreted as colors literally.

At a source vertex a full seam has one color because its two sides match.
If the two colors adjacent at every incident native corner differ, then
all three ray colors differ: two equal ray colors would bound a corner
with equal adjacent colors. This inference concerns color identity and
remains true even if all three physical lengths are equal. In the adjacent
repeated-color branch the source explicitly allows ray-color multisets
and tests simultaneous native-arm flips. No omitted unequal-color/equal-length
configuration can arise in T: a physically possible seam between different
colors is excluded by the SOURCE hypothesis, not claimed geometrically
impossible in the final unmarked tiling.

Conversely every same-color pairing used in the proof matches equal actual
lengths. Extra accidental metric equalities merely permit additional
unmarked tilings; they cannot invalidate the constructed periodic witness.
This is the correct direction for a periodic-escape argument.

## Attack 2: finite domains and actual endpoint tests

I independently reran the four existing finite verifiers. All returned PASS:

- distinct six/six words: 420 normalized words, 30 survivors, 54 four-face
  torus gluings and 95 angle-support cases;
- separation two: 3,780 words, eight classes, sixteen endpoint covers,
  fourteen direct tori and two deterministic partitions;
- adjacent repeat: 3,780 words, twelve classes, eleven closed supports,
  every support with a direct torus;
- opposite repeat: 1,890 words, eight classes, twelve mixed covers,
  ten direct tori and two deterministic partitions; the pure-B torus also checks.

The separation-two and opposite-repeat endpoint tests follow actual native
side slots to their far corners. When adjacent colors differ, the ray color
selects one native arm even if both arms happen to have equal physical
lengths. The same-side propagation is therefore unchanged.

For adjacent repeated B colors, two arms can have the same COLOR. The
microstate enumeration keeps their different native slots, chooses all
left/right flips and requires one simultaneous assignment to support all
three far-end pairs. Repeated actual corner indices are retained with
multiplicity. The proof correctly uses that exact finite lemma and does
not replace it with three independent ray choices. Its surviving supports
all use the ring branch, so no unresolved same-color-arm ambiguity enters
the deterministic proof.

The graph-private-color reductions also transfer: an A-private color has
no B incidence, regardless of whether an unrelated B color has the same
physical length. Those extra metric coincidences create no new colored
edges in the source graph.

## Attack 3: formal splitting and flat tori

The formal four-slot ring first selects four A/B matches with identical
SOURCE colors, then refines the other slots with private symbols. The
private sides are paired only with the same native slot of the other copy
of their own type. Thus all pairings are valid physical equal-length
matches, even when private symbols denote equal lengths or arise from
splitting one original source color.

The alternating-copy pairing proof needs only the four common cyclic
symbols and the four legal actual-corner angle equations. Reversing B's
reference by a reflection is allowed. Its eight circular three-sector
links, twelve edges and four faces give a connected orientable flat torus.
Noninjectivity of ell does not change these links or the original corner
angles. The complete flat universal cover supplies an actual Euclidean
plane tiling, avoiding any unsupported extension of a locally legal patch.

For the opposite-repeat pure-B branch, the two possible pure stars are
B-local corner triples {0,1,2} and {3,4,5}. Either actual occurrence supplies
one angle sum 2pi; B's angle sum 4pi supplies the other. Native sides 0 and 3
have the SAME color, so they can be glued within either B face. The other
four same-index sides pair across the two faces. The independently checked
four circular three-corner links give V=4,E=6,F=2 and a flat torus. No
assumption of unequal other lengths or physical asymmetry is needed.

Minor notation observation, not a mathematical defect: Section 7's displayed
pure-B triples use B-local indices 0..5, whereas most other displayed
supports use global A0..5/B6..11 indices. The source opposite-repeat lemma
makes this local convention explicit, and the proof and replay agree.

## Attack 4: physical symmetries and indexed deterministic propagation

This was the main new proof obligation. The argument succeeds because the
source supplies actual indexed maps g_U, rather than trying to recover
unmarked native indices from a physically symmetric polygon.

In a partition support every actual native corner belongs to one triple.
Its three ray COLORS are distinct. At a fixed indexed host side, one endpoint
corner and its side color select the unique other corner incident to that
ray. At that neighboring corner the color selects a unique native side.
The other endpoint is then fixed by that full side. Thus neighbor type,
native side and ordered endpoint images are fixed by the indexed host
state; the finite checks confirm consistency at BOTH endpoints.

For arbitrary genuine convex reference metrics, the ordered segment mapping
has exactly two plane-isometry extensions. One sends the neighboring reference
interior to each side of the line, so precisely one puts it opposite the
host reference interior. This fixes a complete relative map h. If the host
is reflected, composing h with its reflected placement gives the corresponding
reflected configuration; no absolute orientation set is assumed.

Physical polygon symmetries cause no remaining ambiguity. An isometry fixing
the images of two distinct native endpoints is either identity or reflection
in their line. The latter interchanges the interior half-planes and cannot
preserve the required placed interior. Equivalently, every possible geometric
reference symmetry acts dihedrally on the native side slots, and six distinct
A colors or four singly occurring B colors allow only the identity among
color-preserving such permutations. A physical symmetry permuting colors
is not a symmetry of this indexed source state.

Consequently the ACTUAL indexed neighbor map satisfies

    g_V = g_U composed with h_(host type, native side).

This is stronger than saying the unindexed polygon images coincide. Transport
between two same-state indexed tiles propagates through the connected full-side
adjacency graph and preserves the entire framed tiling. Image tiles cover
the plane, so no separate surjectivity assumption is missing. The resulting
framed symmetry group has finitely many tile orbits, is discrete and acts
cocompactly. The reproduced elementary planar group argument then gives a
rank-two translation lattice. Forgetting colors and frames preserves those
translations, yielding the required unmarked periodic witness.

No assertion that EVERY unmarked tiling has unique neighbors is made or
needed. The specified indexed source alone obeys the derived deterministic
rules. This avoids the invalid move of trying to derive framing solely
from unequal physical lengths.

## Attack 5: actual-contact-component corollary

In the chosen uncolored defect-free tiling, fix any reference indexing of
each occurrence. A graph edge joins the two native side slots used by an
ACTUAL full seam. Its transitive closure E joins only equal physical lengths.
Assigning the E-component as a native side color therefore gives a valid
fixed color on each reference slot and makes every source seam color-matched.
The resulting function from component colors to physical lengths need not
be injective, precisely as allowed by the theorem.

For an A-five/B-five pair, if the repeated A slots were in different
E-components then A would have six component colors: no other two A slots
can join because their physical lengths differ. B has at least five component
colors because unequal physical lengths cannot join. The source theorem
would yield an admitted periodic escape. The same applies with A/B exchanged.
Hence an aperiodic pair would require BOTH repeated pairs to be E-connected
for every admitted defect-free source and every chosen occurrence indexing.
An allowed but nonoccurring seam cannot establish this connectivity. The
claimed quantifiers, including arbitrary indexing choices and reflections,
are therefore justified.

## New reviewer checker and replay

The small new standard-library-only checker is
[hexagon-six-five-formal-color-independent-2026-10-15.py](hexagon-six-five-formal-color-independent-2026-10-15.py).
It imports no author artifact. It checks color-preserving dihedral symmetry
ambiguity for all three repeat separations and reconstructs all forty-eight
complete native-side endpoint maps in the four partition supports. It
deliberately gives EVERY formal color the same physical length 1, so no
hidden metric inequality can select a neighbor. Result: PASS. This is a
finite index check; the universal geometric isometry argument is proved
above, not inferred from that special metric assignment.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-formal-color-independent-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-holonomy-verify.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-independent-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-adjacent-independent-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-separation-three-independent-2026-10-15.py

All five commands completed with exit status 0. No new word domain or metric
search was needed. No mathematical defect requiring repair was found.

**Final verdict: VALID.** The new formal-color theorem and actual-component
corollary follow from the existing finite lemmas with the explicit indexed
geometric bridge supplied. The main unrestricted two-polygon problem,
including the case where both repeated pairs are actually seam-connected,
remains unresolved.
