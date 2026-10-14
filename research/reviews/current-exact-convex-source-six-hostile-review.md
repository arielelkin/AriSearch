# Fresh hostile review: reconstructed six-source fixture and thin periodic escape

Date: 2026-10-13. Independent reviewer: contact_structure.
Verdict: VALID for the exact internally selected fixture and its monohedral
thin-P periodic escape. Original six-source parameter compatibility, Penrose
arrow consistency and universal intrinsic decoding remain UNPROVED.

Reviewed artifacts: [literature record](../literature/current-exact-convex-source-six-reconstruction.md),
[producer](../searches/current-exact-convex-source-six-profile.py),
[explicit four-P plane proof](../searches/current-exact-convex-source-thin-four-motif.md).

## Exact fixture and finite checks

The producer was replayed after the four-P additions and passed. It uses exact
Sage AA, a single eps=1/100 midpoint profile, and six stated incidence cycles.
Its supporting-halfplane convexity tests, pairwise clipping intersections and
area identities cover exactly that finite domain. Distance signatures allow
both cyclic orientations, so reflection identifications are retained. The
three thick classes and one thin class yield four classes, not two.
This is an invented exact realization of recovered diagram incidence; no
claim that it reconstructs original generic arrow-compatible parameters is
licensed. The warning and remaining source obligations are explicit.

## Independent Type2 and labeling check

I opened the primary Sugimoto paper and inspected its
[Figure1 image](https://arxiv.org/html/2501.07090v2/CPM15TF-Fig01re.png)
on 2026-10-13. Type2 is A+B+D=360 and a=d; the extra c=e in Section2
gives the edge-to-edge specialization. The repaired literature record now
states these conditions correctly. The figure uses a=EA,b=AB,c=BC,d=CD,e=DE.
Under new consecutive vertices (oldD,oldE,oldA,oldB,oldC), a is oldC-oldD,
d is oldA-oldB, c is oldE-oldA, e is oldB-oldC, and b is the seam oldD-oldE.
The four profile sides are exactly equal, proving both a=d and c=e. OldA and
oldC are supplementary, so the other three angles give the required 360 sum.
The old corner angles remain 36 and 144 individually: both incident rays at
each old vertex rotate by the same signed profile tilt. No pixel measurement
or approximate equality enters the argument. The article confirms periodic
translation units, but the new direct motif makes this imported result
unnecessary for the exact escape.

## Full-plane four-P carrier audit

Reflection S swaps a and b and reverses the old boundary indexing, so the
reflected side kink is S(L_(3-i)). The four translated coincidence identities
are correct. Checkerboard parity switches on every primitive rhomb-grid
adjacency and is preserved by a+b and a-b. The proposed four pieces are
isometric copies of P: identity, halfturn, reflection, reflected halfturn.

The parent-grid fan homotopy supplies an actual global covering proof.
Only a midpoint moves in each fan triangle; signed determinants are affine
in the homotopy parameter. Positive values at parameter zero and one ensure
strict positivity throughout. The stated epsilon bound is sufficient and
satisfied exactly. At any mesh vertex the cyclic incident image rays remain
nonzero with each consecutive determinant positive. Their winding number
cannot change from one during the homotopy, and their positive angular
increments therefore cover exactly one turn; the local fan is embedded.
Edge and triangle interiors likewise have embedded neighborhoods. Thus the
maps are local homeomorphisms, not merely collections of nonflipped triangles.
Bounded displacement by epsilon makes each map proper. A proper local
homeomorphism has open and closed image and is a covering of the plane;
connectedness of the domain and simple connectedness of the plane make it
a homeomorphism. This justifies all-plane coverage and absence of overlap.

The modified parent is split into P and its halfturn along the shared seam;
the exact support and clipping checks plus matching boundary arcs verify this
local partition. Area/covolume equality is expressly supplementary, so no
finite-patch or area-only gap remains. The four-P motif therefore gives a
periodic monohedral escape with nonzero lattice vectors, killing every
proposed protoset that includes this exact P.

## Independent checker and scope

A small independent [checker](current-exact-convex-source-six-hostile-check.py)
reconstructs the thin coordinates without importing the producer and verifies
P strict convexity, supplementary algebraic data, checkerboard side identities,
both endpoints of every homotopy determinant and the four-P covolume. It passed:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/current-exact-convex-source-six-hostile-check.py

This checker plus the analytic plane argument verify the escape. They do not
verify the original book source, any Penrose matching arrow system, generic
asymmetric profiles, or a universal decoder for six convex source shapes.
The conditional macro-content vector argument is algebraically valid under
its expressly assumed six-distinct-face decoder and thick/thin ratio; it is
not applied to the four-class fixture. No unresolved objection to these
scoped claims remains.
