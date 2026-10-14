# Bounded nonconvex-parent construction and pentagon repair

Date: 2026-10-14. Completed bounded construction/adversary cycle; [independent hostile review VALID](../reviews/nonconvex-parent-construction-2026-10-14-review.md) within the stated finite domains. The original all-hexagon grid is empty, and the single pentagon-containing repair has exact nonconvex parents that cannot extend to a plane tiling. A bounded partial-contact test retains explicit local P-only patches, including host switches. No aperiodic pair or hierarchy is claimed.

Atomic A has native side lengths (p,1,p,1,p,1), edge directions
(0,60+delta,120,180+delta,240,300+delta), delta in {10,20} degrees.
Atomic B has native side lengths (p,p,p,1,1,1) and native angles
(u,120,beta,v,120,eta). Each of beta,eta is in {10,20,...,170} minus {120};
u,v are in {10,20,...,170}; u+v+beta+eta=480. Vertices0 are at the origin and
side0 points east. B closure fixes p>0, p!=1; both atomic polygons must be
strictly convex and distinct congruence classes. This is the OPEN P/P
binary-arc category, with a pure homogeneous120 corner on each of its two
homogeneous arcs. It does not reuse the closed center or noncentral mixed
homogeneous categories.

Macroparents are unions of one A and one B, with one full matching native
side, either endpoint pairing and determinant sign, and disjoint interiors.
Only simple NONCONVEX union boundaries qualify. For each, fixed scalar
inflation2 and exact atomic dissections with8 atomic children are permitted.
The area equation is checked before placement enumeration and fixes4A+4B
unless exact equal atomic areas create an additional count solution. Multiple
macroparent types are permitted, but no finite dissection is interpreted as a
closed substitution or shape-only forced hierarchy.

Before expansion: reject invalid closure, atomic omission/explicit periodic
carriers, missing native corner stars, and impossible flat boundary subdivision.
All-obtuse atoms cannot subdivide a straight macro boundary side; every mixed
full-edge two-child parent exposes both lengths, so scalar2 doubles its longest
native side beyond any atomic side. Acute/right B signatures remain explicitly
inside this changed domain, with legal180-degree boundary stars tested before
expansion. Reflections are always allowed. Whole-edge parent assembly and the
fixed atomic placement atlas are search hypotheses; arbitrary partial contacts
are not claimed exhausted.

Arithmetic is exact in Q(zeta36), zeta36=exp(i*pi/18). The intended artifacts
are a deterministic producer, frozen exact certificate, this self-contained
finite-domain note, and an independent hostile audit. No randomness, source
hierarchy, unbounded enumeration, or bound increase is authorized.

## Completed first gate and justified repair

The [initial producer](nonconvex-parent-construction-2026-10-14.py) exhausted1430
angle signatures satisfying the stated grid and angle sum. NONE gives a positive,
real, distinct p!=1 closed B. The [initial frozen certificate](../certificates/nonconvex-parent-construction-2026-10-14.json)
contains no atomic pair. Hence none of the producer's later native-star or flat-star
filters was exercised or used as mathematical evidence. In particular, a
three-native-corner census would not exhaust all high-valence/T stars for the
acute signatures in this grid; no such stronger conclusion is asserted.

Independently of the empty grid, the root and adversary identified a stronger
all-hexagon hierarchy gate. For any simple polygonal parent with p genuine corners,
a dissection into fixed convex atoms of at least6 sides has at most p-6 additional
boundary vertices. Thus its perimeter is at most (2p-6)L, where L is the longest
atomic side. This excludes arbitrarily inflated iterates of any fixed finite
polygonal parent, including nonconvex parents. Its corrected sector-count proof
counts flat child incidences at reflex parent corners; the convex-parent native
corner identity cannot simply be reused at those corners. The [separate proof](../lemmas/nonconvex-parent-hexagon-perimeter-bound.md)
and [fresh review](../reviews/nonconvex-parent-hexagon-perimeter-bound-review.md)
retain the corrected argument. This justified the one change to a
pentagon-containing pair, rather than a larger all-hexagon search.

## Fixed source-free pentagon/hexagon repair

Let s=sqrt(2), r=sqrt(3), both positive. The exact counterclockwise atoms are

    P=((0,0),(3,0),(4,r),(7/2,3r/2),(0,1/r)),
    Q=((0,0),(3,0),(3+1/(sr),1/(sr)),
       (3+1/(sr),7/r+1/(sr)),(s,7/r+1/(sr)),
       (0,7/r+1/(sr)-s)).

P has angles (90,120,120,90,120) and native lengths (3,2,1,7/r,1/r).
Q has angles (90,135,135,90,135,135) and native lengths
(3,1/r,7/r,3+(1/r-2)/s,2,7/r+(1/r-2)/s). The producer checks strict convexity
using every supporting edge against every other vertex. Their different side
counts imply different congruence classes. P has area10/r; their areas are
unequal. Scalar2 gives four times the mixed-parent area. With exactly8 atomic
children, the area equation therefore forces4P+4Q.

Arithmetic is exact in K=Q(g), g=sqrt(2)+sqrt(3), minimal polynomial
x^4-10x^2+1 and the displayed positive real embedding. Recover
s=(g-1/g)/2, r=(g+1/g)/2. Certificate scalars are rational coefficient strings
in basis(1,g,g^2,g^3); each vertex is two such coefficient lists. No floating
point geometry, random seed, timeout or solver assumption enters the result.

The [repair producer](nonconvex-parent-construction-2026-10-14-pentagon-repair.py)
and [frozen certificate](../certificates/nonconvex-parent-construction-2026-10-14-pentagon-repair.json)
exhaust every full-native mixed attachment: four matching native side pairs,
both endpoint assignments, both determinant signs, retaining opposite-side
placements. There are8 indexed attachments. Exact separating axes prove their
atomic interiors disjoint. Cancel the shared edge, simplify straight vertices,
and obtain8 nonconvex parent boundaries, with exact areas P+Q. These are oriented
attachment records, not8 distinct congruence classes.

All8 parents fail the extension gate even with unrestricted external contacts.
Every P side has at least one120 endpoint. At a whole P/Q seam endpoint that
P120 meets a Q90 or Q135, leaving150 or105 degrees. No combination of the
native palette90,120,135 or a flat180 sector fills either gap. Thus a whole
native P/Q seam cannot occur in any admitted plane tiling of this pair. This
kills this full-edge parent mechanism BEFORE an8-child cover search, which
was consequently not run. It does not prohibit every partial P/Q contact.

## Omission and periodic counterexample filters

The separately retained [construction adversary](construction-adversary-2026-10-14.py)
independently confirms convexity, all8 full-native seam endpoint failures, and
controls for winding, length aliases, reflections and known periodic witnesses.
Its two-copy native-halfturn lattice domain exhausts30 P and60 Q generator
pairs without a witness. That result is NO_WITNESS_IN_DOMAIN, not an omission
proof or aperiodicity evidence; its certificate is
[construction-adversary-2026-10-14.json](../certificates/construction-adversary-2026-10-14.json).

A stronger reviewed P-only filter does apply. Cyclically start our P at native
side2 and rotate by -120 degrees. Its directions become(0,90,150,240,300), and
its lengths become the Cairo indexing

    (a,b,c,d,e)=(1,7/r,1/r,3,2).

Closure gives b-c=r(d-a) and e=r*c+d-2a exactly. The four90 arms
(1,7/r,1/r,3) are pairwise distinct. The reviewed
[Cairo monohedral theorem](../lemmas/partial-contact-cairo-monohedral-classification.md),
via its private-arm necessity, therefore excludes P-only tilings with arbitrary
contacts and reflections. The surviving finite P patches below demonstrate
local legality, not a contradiction to that global result. No new Q-only
classification is claimed here.

## One bounded T-capable completion test

The palette makes every native P120 plane vertex a PPP120^3 vertex. A120 corner
cannot lie inside another tile side because the remaining60 degrees cannot be
filled. Normalize its three rays to0,120,240 degrees. Independently choose P
native corner1,2 or4 in each sector and either arm assignment: exactly216 oriented
placements. Every preserving/reversing native isometry is considered; no native
corner equality is treated as a polygon symmetry.

At an unequal shared ray the shorter native edge ends inside the longer host.
A shorter120 endpoint is impossible because flat180+120 leaves60. If the shorter
endpoint is90, the remaining90 wedge needs one P/Q native90 corner. Enumerate
both P90 corners and both Q90 corners, with both arm assignments, in this forced
wedge. Check disjointness against all three central polygons and necessary
endpoint conditions along both new contacts. The only flat angle completion is
90+90. A shorter120/135 endpoint is therefore forbidden, while an edge extending
PAST a90 host endpoint remains allowed. Equal ray endpoints must also admit a
completion of their remaining angle by native or flat sectors.

For multiple initial T points, jointly enumerate the finitely many guest choices.
An actual tile may fill two such points, so identical geometric polygons are
counted once before overlap and angle checks. Exact separating axes test every
pair of actual tiles. At every genuine vertex of the resulting patch, sum native
angles and any flat180 incidences from the other placed tiles and require the
remaining angle to admit a palette completion. This is a necessary local test,
not a claim that the remaining sectors extend consistently.

The216 oriented branches divide into116 with no eligible90 guest,80 with a
short120 ray endpoint, and20 surviving joint completions. Each surviving branch
has exactly one retained joint completion. Six include native Pcorner4 and two
Pcorner0 guests, yielding five actual P copies. In those six, both guests extend
past a90 host endpoint: genuine host switches. The other14 branches have no
host switch. No quotient by congruence has been applied to these counts.

These exact host-switch patches are regression controls against the false
assumption that every host edge must simply split into a+b with both guest edges
ending at its endpoints. Their newly created T vertices need further completion;
no second completion stage, radius growth, infinite P tiling, mixed plane tiling,
substitution closure, macroparse, or universal forcing is inferred. This bounded
cycle stops with a killed full-edge parent mechanism and retained local partial-
contact patches requiring a materially different future parent incidence.

## Replay and scope

Both producers print deterministic JSON by default and leave retained certificates
unchanged. Optional --output explicitly writes the selected report. Each completed
run took well under a minute in the locked arisearch environment; no resource cap
or interrupted enumeration contributed to the result. Replay commands:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/nonconvex-parent-construction-2026-10-14.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/nonconvex-parent-construction-2026-10-14-pentagon-repair.py

Both producers and the independent checker are registered for replay. The
[completed independent audit](../reviews/nonconvex-parent-construction-2026-10-14-review.md)
validates the stated finite-domain claims. Its checker independently verifies
the 20 retained partial-contact patches and coverage of the 216 branch keys;
the classification of all 196 negative branches additionally relies on the
frozen exhaustive producer and source audit.
No literature priority or novelty claim is made. The unrestricted two-convex-tile
problem remains unresolved.
