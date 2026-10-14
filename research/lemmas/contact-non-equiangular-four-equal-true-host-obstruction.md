# Four-equal pentagon and genuinely extendible Q-host cap: a sparse-defect obstruction

Date:2026-10-13. Status: exact fixture/cap replay passed; repaired analytic proof [independently reviewed VALID](../reviews/contact-non-equiangular-four-equal-repaired-hostile-review.md). One changed candidate, not an all-metric theorem.

## Exact pair and locally genuine host bypass

Put r=sqrt2,c=cos(pi/8),t=sin(pi/8). Integrate P edge directions
-22.5,45,135,202.5,270 with lengths(1,1,1,1,w), w=r-2t in(0,1).
P has native angles112.5,112.5,90,112.5,112.5. Integrate Q edge directions
22.5,45,90,135,202.5,225,270,315 with lengths(2,1,1,1,2,1,1,1).
Q is centrally symmetric with angles112.5,157.5,135,135 repeated twice.
Both are genuine convex positive polygons. Its two length2 slots are private
relative to P, but may be Q-hosted twoP90 caps, so QQforcing cannot be
imported from the old equiangular palette.

The producer research/searches/contact-non-equiangular-four-equal-true-host.py
checks closure, strict support inequalities, all native angle/length identities,
and the complete full/flat angle census. It constructs a disjoint Q/twoP
cap along a private2 side, with two along-host unit legs and a shared
perpendicular unit edge. Its far twoP112.5 endpoint admits FOUR actual
Q135 whole-angle placements, each giving a disjoint Q/twoP/Q patch.
Thus the earlier missing(y,y) shortcut is escaped geometrically, not merely
by a length coincidence. No plane existence follows from this positive patch.

The complete full stars are

    Q112+Q112+Q135, P112+Q112+Q135, 2P112+Q135,
    P90+2Q135, P90+Q112+Q157, P90+P112+Q157, 4P90.

The only flat star is host180+2P90. Here112 denotes112.5,157 denotes157.5.

## Partial-contact geometry derived for this fixture

No native corner other than P90 can lie inside another side: after adding
180 the remainders67.5,45,22.5 are below the minimum native angle90.
At any flat cap both acute legs are unit length, so both perpendicular
and along-host guest legs are unit. A host with two nonright native
endpoints must have length2, since neither host endpoint nor guestP112
far endpoint may lie in a side interior. A Pacute side of length1 cannot
host: its nativeP112 endpoint would have to coincide with the guest's
farP112 at distance1 from the internal flat point, exceeding the remaining
portion of that length-one host. Therefore P hosts are all impossible;
its both-obtuse sides have lengths1,1,w, none2. Qpublic unit hosts are
likewise impossible. Only native Qlength2 sides may host a cap, necessarily
covering the complete side with its one flat midpoint. Every other contact
involving Q is whole on both native sides. The length2 side is either a
Q-Q whole contact or this twoP cap, never a longer partition.

## Endpoint geometry forbids all QQ135/135 acute stars

Use native Qword(2,U,M,V,2,U,M,V), all public lengths1, where U runs
from157 to135, M from135 to135, V from135 to112. A length2 QQcontact
uses one of the two opposite equal private slots; central symmetry
identifies their geometry. A supporting-line reflected mate places two157
corners together, impossible. The midpoint halfturn gives112+157+P90.
If instead that side hosts a cap, at its157 endpoint the cap'sP112 leaves
exactlyP90. Thus EVERY nativeQ157 is incident to exactly one P90,
and its Uside has a whole Pacute neighbor starting at that157 endpoint.
That same P has P112 at the Uside's135 endpoint.

U cannot be QQ because its157 endpoint already has the forced Psector.
M cannot be QQ, including a mate using a DIFFERENT native unit slot.
A mate U is impossible because U cannot QQ at its157 endpoint. A mate M
puts two Q135 corners at the endpoint next to the fixed UguestP112,
which would requireP90 instead. A mate V could put Q112 at that endpoint,
and Q135+Q112+P112 is an allowed angle star. But the Uguest's exposed
native PPbevel is unit length with112.5 at BOTH endpoints, while the
mateQ112's outgoing side is its native privateH of length2. Their shared
interface therefore ends at guestP112 inside that QH side, forbidden by
the flat-star census. The Q-hosted90/90 alternative cannot repair a guest
112.5 endpoint. Thus the mixed M/V mate is excluded by actual lengths,
not just angle counting. Whole Ucontact fixes the starting P112 guest
and its exposed unit bevel. Hence the only possible public QQsides are V. A Vside is QQ exactly when its112 endpoint's private
side hosts a cap: Q112+capP112 leavesQ135 alongV; with a privateQQside it
instead leavesP90 alongV, makingV a Pcontact. A QQ Vmate must also use
V because U/MQQ were excluded. Reflection aligns112+112, which requires
Q135, but the actual capP112 is already present there; impossible. The
halfturn instead aligns112+135 withP112. Thus no actual QQedge joins two
Q135 native corners. In particular the potential P90+2Q135 full star never
occurs, even though it belongs to the abstract angle census.

## Uniform corner ledger makes caps and quads sparse

In any translated square count centroid-anchored p,q tiles, h complete
Qlength2-host incidences, and z fourP90 vertices. All counting errors are
uniform O(R): fixed positive areas/diameters bound tiles in a boundary
collar. Every Q has two157 corners, each with one P90; no star contains
two157, so these contribute2q DISTINCT P90 occurrences. Host midpoints
contribute2h more, and quads4z. These exhaust P90 because QQ135/135 was
excluded. Therefore

    p=2q+2h+4z+O(R).

Assign native weights P90=4,P112=1,Q112=1,Q135=-2,Q157=-5.
All abstract full stars have score0 except quads with16; the sole flat
star has8. Complete tile totals are P8,Q-16. Since all flats are precisely
Qhost caps, unrestricted native occurrence counting gives

    8p-16q=8h+16z+O(R), hence p=2q+h+2z+O(R).

Subtracting forces h+2z=O(R), uniformly in square position. Both are
nonnegative, so arbitrarily large separated-grid disks are free of host
midpoints and quads. This is not a pointwise zero-defect assertion and
makes no species-frequency or vertex-separation assumption.

## Clean placement limit gives a missing native middle side

Translate growing clean disks and extract indexed fixed-polygon placement
limits; positive areas bound local tile counts, translations are bounded
locally and orthogonal placements are compact. Coverage/interior nonoverlap
persist. At each limiting native vertex, isolate its finite multiset of
converging native corner occurrences in a small disk. Each approximating
geometric star in the disk is clean and score0. Additivity preserves total
score0 even if several stars merge. Thus the limiting star has score0.
Flat caps and quads have positive scores8/16 and cannot appear in the limit.
This is the reviewed native corner-cluster argument, not an assumed FLC
or unchanged incidence language. All native contacts in the clean plane
are consequently whole and the tiling is trivalent.

Every private length2 Qside must now QQmatch, with the midpoint halfturn
geometry proved above. Therefore each Q112 andQ157 is already in the
QQ/P90 star. No P112 can meet either of those native Qcorner types.
All P112 stars are consequently PPQ135; all P90 stars are PQQ (quad and
flat removed, P90+P112+Q157 excluded by the privateQQ star). At each of the
four obtuse Pcorners there is one Pneighbor and one Qneighbor; both acute
legs have Qneighbors. Native alternation around P therefore forces the
indexed Rword Q-P-Q-P-Q: its middle native sidew must contact Q.
But Q's native alphabet is{1,2}, while0<w<1. A whole wcontact is impossible.
No admitted clean plane exists, contradicting compactness from the assumed
original plane. The fixed pair is UNTILEABLE despite its genuine cap and
four positive farQ extensions. Species omission is retained: P alone fails
at112.5, and Q alone fails at157.5 (its only full stars needP90).

No assertion concerns other metrics, four-equal palettes in general or
all non-equiangular partners. This is a changed mechanism with an analytic
sparse-host obstruction, not a periodicity claim or resolution of the main
unrestricted problem.
