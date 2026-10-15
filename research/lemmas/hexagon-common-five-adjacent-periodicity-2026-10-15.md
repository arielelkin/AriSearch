# Common five numerical side lengths: all adjacent-repeat cases

Date:2026-10-15. Status: independently hostile-reviewed VALID with exact certificates;
[final whole-proof audit](../reviews/hexagon-common-five-adjacent-hostile-2026-10-15.md). Restricted periodic escape only.

## Theorem and complete source domain

Let A,B be genuine convex hexagons with the SAME set of five distinct
numerical side lengths, one length doubled in each. Suppose at least one
doubled pair is adjacent. If these shapes admit any plane tiling, including
reflections and partial contacts, they admit a doubly periodic tiling.
The doubled values need not agree. Combining the independently reviewed
[nonadjacent-repeat results](hexagon-both-opposite-repeat-periodicity-2026-10-15.md)
therefore excludes ALL common-five numerical hexagon pairs from aperiodicity.
This is not a theorem about arbitrary two convex polygons.

Pass to a full-side, everywhere-trivalent indexed source using the reviewed
[defect-free limit theorem](hexagon-limit-and-periodicity.md). Normalize
A=(0,0,1,2,3,4), reading corner i between native sides i and i+1. For B let
its repeated positions be0,bp with bp=1,2,3. Choose its doubled color from
0..4 and permute the four other colors into the remaining slots. There
are120raw words per bp,360 total, without any symmetry quotient.

A source using A alone is impossible: its length-pair graph is a five-cycle
plus the loop at0. The only possible pure stars use the loop corner0 and
two copies of corner1 or5, or three corner0 copies; native corners2,3,4
cannot occur. The same applies to adjacent-repeat B. Separation-two B has
no pure star because its corner graph is triangle-free. If opposite-repeat
B alone tiles, a pure star gives its explicit two-face monohedral torus,
described below. Apart from this escape, both types occur and all twelve
native corners occur. Reflected source placements retain their native indices.

## Native states retain simultaneous arms and opposite endpoints

Repeated ray lengths and repeated native corner indices are allowed.
Choose three ordered native corner OCCURRENCES and independently choose
which native side is each corner's left/right arm. Retain cyclic choices
whose consecutive ray lengths match. All physical vertex states occur in
this list; a multiset reading plus every arm flip is equivalent because
three sectors have one cyclic order up to reversal, and global reflection
preserves the unordered native seam data. Repeated indices still represent
different tile occurrences.

A state records all THREE native full-side seams simultaneously. Each ray
retains the unordered pair of native SIDE slots, the multiset of near-end
corners and the multiset of their actual opposite-end corners. Prune if
any seam has no remaining opposite-end state with the SAME native slots
and required opposite-end corner multiset. Iterate to a fixed atlas.
Every actual state survives inductively; forgetting further geometry can
only enlarge this necessary atlas. No local-extension sufficiency is used.

The [independently reconstructed native certificate](../certificates/hexagon-five-adjacent-microstate-gate-2026-10-15.json)
and [no-import checker](../reviews/hexagon-five-adjacent-microstate-independent-2026-10-15.py)
check all360words and every initial/fixed state. Counts(no twelve-corner
cover, six-color escape, residual) are(88,24,8),(96,24,0),(92,24,4) for bp1,2,3.
For the component escape connect native slots meeting across ANY fixed
state seam. The actual seam graph is a subgraph, so its component partition
refines this upper graph. Disconnection of either shape's doubled slots
provides six actual component-colors for it, with at least five for its
partner. The reviewed [six/five formal-color theorem](hexagon-six-five-formal-color-periodic-escape-2026-10-15.md)
gives a doubly periodic unmarked escape for the original metrics. This also
proves the narrower [adjacent/separation-two result](hexagon-common-five-adjacent-separation-two-periodicity-2026-10-15.md).

The12residual raw words have explicit color bijections and independent
native dihedral readings to four representatives:

    B1=(0,0,1,3,2,4), B2=(0,0,2,4,1,3),
    B3=(2,2,1,3,0,4), B4=(0,1,3,0,4,2).

Their raw orbit sizes are2,2,4,4. The [complete support/witness certificate](../certificates/hexagon-common-five-adjacent-periodic-gate-2026-10-15.json)
retains each pointwise word map. For each representative enumerate every
subset S of its fixed star atlas, restrict the possible microstates to
stars in S, and repeat the simultaneous endpoint-state pruning. Keep S
exactly when every native corner is covered and the pruned states still
realize EVERY selected star. Actual occurring-star sets EQUAL one of these
supports:9,12,6,14 respectively, total41. Containment of a minimal support
would be insufficient for the case arguments below.

## Positive four-face torus comparison covers25 supports

For B1,B3,B4 form two indexed A and two indexed B faces, all8 relative
boundary orientations modulo global reversal, and all within-color perfect
matchings of their24sides. Reverse boundary endpoints on each pair. The
finite domains have68040,48600,68040pairings respectively. Retain actual
connected orientable trivalent torus gluings, with complete circular vertex
links and Euler characteristic zero. The witnesses have4,1,2different native
angle patterns respectively. No larger quotient completeness is asserted.

For each actual source support impose the source equations: each hexagon's
angle total is4pi and each occurring star has total2pi. The certificate
supplies exact Fraction combinations of these augmented rows giving the
vertex equations of a retained ACTUAL torus. Coverage is9/9forB1,4/6forB3,
12/14forB4. All25positive implications retain their coefficients and gluings.

The positive geometry bridge is independent of search bounds. Paired sides
have equal original physical lengths. Circular links and the target angle
sums make the quotient a nonsingular compact oriented flat torus; its
complete universal cover develops isometrically onto the Euclidean plane.
The lifted original polygons tile with disjoint interiors and a rank-two
deck translation lattice. No source patch resembling the quotient is needed.
The16remaining exact supports are settled by the following arguments.

## B2: eight supports force impossible numerical length coincidences

There are12B2supports: two of size6, two of size7, and eight of sizes12–14.
For EVERY one of the eight large supports, the augmented source row basis
forces ALL twelve angles to120degrees. The certificate retains96 exact
weighted row identities, one per angle per support. This is not a numerical
angle inference. Orient each equiangular reference hexagon counterclockwise;
its successive side directions are0,60,120,180,240,300degrees up to rotation.
Writing the common lengths as(r,x,y,z,t), the words are

    A=(r,r,x,y,z,t), B2=(r,r,y,t,x,z).

Their two vector-closure equations each, multiplying the horizontal equation by2 and the vertical equation
by2/sqrt3, give the four rows

    (3,-1,-2,-1,1), (1,1,0,-1,-1),
    (3,-1,-1,1,-2), (1,-1,1,-1,0).

This matrix has rank4 and its kernel is precisely the span of(1,1,1,1,1).
The certificate supplies four exact row combinations giving each coordinate
minus the first. Thus r=x=y=z=t, contradicting five DISTINCT numerical
lengths. These eight actual supports cannot occur. If auxiliary colors were
allowed to coincide physically, this branch would instead give a regular
hexagon and an immediate monohedral periodic escape; no such extension is
needed for the numerical theorem.

## B2: small supports, parity and AB frame propagation

One small6support is

    S={(0,0,6),(1,2,7),(1,5,9),(2,3,10),(3,4,8),(4,5,11)}.

Every star is AAB and each native B corner occurs once. The other small6
support interchanges the roles, with every vertex ABB. Equal arms at the
native loop corner preclude a single-endpoint uniqueness shortcut. Instead
check BOTH endpoints of every possible AB side: the guest native side and
its two ordered native endpoints are unique whenever that side meets the
other species. The independent native checker retains these maps.

At every A corner exactly one incident side meets B, so its B-neighbor
sides alternate. Carry their even/odd parity as an additional finite state;
an incoming B neighbor fixes it. A B frame fixes every adjacent A frame
and parity through the two-endpoint map. An A frame with parity fixes its
three B neighbors. The AB-only graph is connected: every AA edge can be
bypassed at an endpoint via the third B, and no BB edge occurs. Consequently
maps between indexed B occurrences propagate through the entire source,
preserving all frames and parity. The discrete symmetry group has finitely
many tile orbits and acts cocompactly, hence contains a rank-two translation
lattice, as in the reviewed [AB parity argument](hexagon-both-opposite-repeat-periodicity-2026-10-15.md).
The ABB case is identical after interchanging species.

Each small7support adds ONE pure star to a small6support: in the AAB case
it is(0,0,0). On any A tile write b_i=1if side i meets B and0otherwise.
At the other FIVE native corners the AAB condition says b_i+b_(i+1)=1.
On an even six-cycle these five equations force the sixth as well. Thus
at corner0 exactly one adjacent side meets B; it cannot be an AAA vertex,
which requires both to meet A. The purported occurring pure star therefore
cannot occur, contradicting exact support equality. The swapped case adds
(6,6,6) and has the same contradiction. This closes all12B2supports.

## Necessary full-corona states and deterministic propagation

For the remaining B3/B4supports use the independently audited
[narrow corona certificate](../certificates/hexagon-adjacent-corona-states-2026-10-15.json)
and [checker](../reviews/hexagon-adjacent-corona-independent-2026-10-15.py).
At each native host corner retain all simultaneous compatible port options
from actual-star arm assignments: each of the host's two incident sides
names its guest native side and guest corner at that endpoint. Choose one
option at each of a tile's six native corners. Require the TWO endpoint
records of each host side to specify the SAME guest side and its TWO distinct
native endpoints. Such a tile state specifies complete indexed relative
isometries for all six neighbors: ordered endpoints fix the segment map,
and the opposite interior half-plane selects the whole plane isometry.
All actual tile states survive these necessary tests.

Prune any tile state lacking a reciprocal guest state on some side. Every
actual source state again survives. A transition is called certain when
the guest state is unique; retained propagation edges are certain both ways.
If these edges form a connected graph on the actual source tiles, an
isometry between ANY two occurrences of the same indexed tile state
propagates its relative maps AND next states through that connected graph.
It is a symmetry of the entire framed tiling. There are finitely many states,
so the symmetry group is discrete and cocompact, and the reviewed planar
crystallographic argument supplies two independent translations. Finite
state counts ALONE are not sufficient; connectivity and transition uniqueness
are proved in each case below.

## B3: delete only uncertain edges, then bypass them

The two uncovered supports are

    T1={(0,1,1),(0,5,10),(2,2,6),(3,4,11),(3,7,8),(4,5,9)},
    T2={(0,10,10),(1,8,9),(2,6,7),(3,7,8),(4,5,9),(6,11,11)}.

For T1 the complete necessary coronas give2A states and1B state. ALL
neighbor transitions are certain except the A-side2 to A-side2 adjacency.
Delete those uncertain AAedges. Each has at its native A2 endpoint the
star(2,2,6), whose third tile is B. This supplies a two-AB-edge bypass via
the two A-side3 incidences, both certain. The original full-side graph is
connected, so after these replacements the certain-edge graph is connected.

For T2 there is1A state and2B states. The ONLY uncertainty is B-side5 to
B-side5. At its native B4 endpoint the star is(0,10,10), with third tile A.
The two B-side4 incidences provide certain BAedges bypassing the deleted
BBedge. The same connected deterministic propagation argument applies.
This establishes periodicity for both exact supports, including their
repeated native corner indices and original reflected placements.

## B4: unique transitions or monohedral opposite-repeat escape

The two uncovered supports are

    U={(0,1,6),(0,5,9),(1,2,11),(2,3,7),(3,4,10),(4,5,8)},
    Uplus=U union {(6,7,8),(9,10,11)}.

For exact U there are2A states and1B state, with EVERY neighbor transition
certain. The full-side graph itself is connected, so the intrinsic-state
argument applies directly. For exact Uplus an actual pure-B star occurs.
Its native triple is{0,1,2}or{3,4,5}; either angle sum2pi forces the other.
Within each of two equally oriented B faces pair native side0to3, and pair
each other native side to itself in the other face, reversing endpoints.
This gives four circular triple links, two of each native angle triple,
and V4,E6,F2. It is a compact flat torus by those equations. The universal
cover supplies the required periodic unmarked tiling. This is precisely the
reviewed opposite-repeat monohedral escape, also valid if the source omitted A.

All41remaining actual supports now give a contradiction or an admitted
doubly periodic escape. The theorem follows. QED.

## Exact artifacts, replay and limits

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-common-five-adjacent-periodic-gate-2026-10-15.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-adjacent-corona-states-2026-10-15.py

These producers print complete deterministic JSON; --output PATH explicitly
retains it. The complete native gate and corona proofs have independent
reviews, linked above. The [independent complete checker](../reviews/hexagon-common-five-adjacent-independent-2026-10-15.py)
confirmed all360native gates,12word maps,41supports,25positive comparisons
with100weighted rows,96angle identities,4length identities and every residual
branch. The fresh whole-proof synthesis audit is VALID. A bounded torus miss is never a negative result.
No angles or coordinates are sampled. All finite domains are explicit.

The later [unequal-palette adjacent theorem](hexagon-five-unequal-adjacent-periodicity-2026-10-15.md) closes the remaining unequal-five cases. Together these results cover every hexagon pair in which each member has at least five distinct numerical side lengths. See the [unified statement and proof map](hexagon-six-distinct-unrestricted-periodic-escape-2026-10-15.md#unified-statement-and-proof-map) for the distinct one-period and doubly periodic conclusions. Pairs with a member having at most four distinct lengths are outside this common-five classification; pentagon-containing pairs and the unrestricted main objective remain unresolved.
