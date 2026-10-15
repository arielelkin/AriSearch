# Independent hostile review: six/five-length hexagon periodicity

Date: 2026-10-15. Reviewer: fresh independent agent, not the author of the
hexagon theorem or producer searches. Status: **VALID for the theorem and
finite certificate described below**, using the separately reviewed
geometric dependencies. This is a restricted impossibility result for an
aperiodic pair, not the main arbitrary-convex-polygon solution. No novelty
claim is reviewed here.

## Exact claim

Let A,B be genuine compact convex hexagons. A has six pairwise distinct
native side lengths. B has exactly five distinct native side lengths, with
its sole repeated length occupying side slots at cyclic separation two.
If the pair admits any plane tiling by isometric copies, with reflections
and unrestricted contacts allowed, then it admits a doubly periodic plane
tiling. The periodic witness may differ from the initial tiling.

Reviewed objects: root's finite certificate
`research/certificates/hexagon-six-five-ring-support-2026-10-15.json`, its
producer `research/searches/hexagon-six-five-ring-selection-2026-10-15.py`,
the complete author proof
`research/lemmas/hexagon-six-five-separation-two-periodicity-2026-10-15.md`,
and the named reviewed dependencies. The full author artifact was read
after completing the independent reconstruction; Sections 1--6 agree with
the complete audited bridge below. No missing-draft qualification remains.

## Independent finite reconstruction

The retained verifier imports only the Python standard library and no
producer code. It constructs words rather than trusting the eight input
representatives. Normalize A=(0,1,2,3,4,5). For each k=0,...,5 choose the
k shared A symbols, adjoin 5-k private B symbols, assign these five symbols
to roles p,q,r,s,t, and use B=(p,q,p,r,s,t) with r<t. All assignments are
visited. There are 60*sum(k=0,...,5) binomial(6,k)=3780 words. Some have
redundant private-label descriptions; redundancy cannot omit a case.

Rather than enumerating length-graph triangles and lifting their edges,
the verifier directly enumerates the 220 triples of actual corner indices.
A triple is admitted precisely when its three distinct unordered side pairs
are the three edges on three numerical length symbols. Actual corner
coverage retains exactly 30 words for k=4 and 60 for k=5, none for smaller
k. An independently implemented full dihedral canonicalization produces
three and five orbits respectively, matching all eight certificate rows.

For each representative, every subset of its actual stars is tested for
coverage and for closure across the other endpoint of every full native
side. The reconstructed support counts are exactly

    1,3,1,1,0,3,0,7  (total 16).

Every actual support is tested, including subsets that might fail unknown
metric realizability conditions; this is a safe overapproximation. No
angle feasibility solver or rational-span argument is needed.

For each support, the verifier independently enumerates perfect matchings
of actual equal-length side occurrences on four faces A0,A1,B0,B1. It
tries both uniform chiralities of the B faces. This is a distinct encoding
from the producer's formal-ring selection. It directly reverses boundary
endpoints in every gluing, checks all 24 corner identifications, checks
that the result has eight vertices each containing three corners from the
selected actual support, and checks face connectivity. Fourteen supports
admit such connected orientable four-face torus witnesses. Exactly two
residual supports remain, both disjoint four-star partitions. For these,
the verifier checks a unique neighbor actual corner across each incident
ray and consistency of the two actual endpoint maps on every side.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-independent-2026-10-15.py

Observed result: PASS, 3780 words, 90 survivors, 8 orbits, 16 supports,
14 direct four-face tori, 2 deterministic residuals. This is finite
combinatorics using exact integers, with no random seed, solver, numerical
geometry, search depth, or producer imports. A temporary first execution
encountered a certificate-schema rename while the producer was being
updated; the retained independent verifier uses the current support-list
schema and passed after that synchronization.

## Audit of the unrestricted-to-finite bridge

The reviewed defect-free limit theorem supplies an everywhere-trivalent,
edge-to-edge tiling by the original hexagons from any unrestricted tiling.
The conclusion sought is existence of some periodic tiling, so replacing
the initial tiling by this limit does not change the theorem quantifier.
A single A has a triangle-free six-cycle corner graph; a single B has a
triangle-free four-cycle with pendant edge, the pendant occurring twice.
Thus neither can tile the defect-free limit alone. Both types occur, and
all twelve actual corners must occur.

B has no pair of adjacent sides of equal length, despite the separated
repeat. Consequently at a trivalent full-side vertex the three ray lengths
are distinct: two equal ray lengths would be the two adjacent native sides
of one incident tile. Its actual corners are therefore one of the enumerated
triples. The finite support contains every actual corner. Across a shared
full side the same two actual tile copies appear at its far endpoint,
which gives precisely the imposed closure relation. In particular two
identical far corner indices cannot occupy one star, since the distinct
ray-length argument forbids a repeated corner pair in a triangle. Reflected
placements change cyclic orientation but do not alter these unordered
corner-pair or endpoint statements. The side-slot formula in the independent
checker was reconstructed directly by listing both slots incident to a
corner, rather than importing the producer's far-end function.

## Flat-torus branch

For each of the fourteen supports, the independently found side pairing
matches equal numerical lengths and reverses the chosen boundary orders.
Every face interior is a copy of the original whole polygon. Pairing the
sides of oriented polygon disks gives a closed orientable surface; the
vertex identifications checked above have connected circular links because
each corner link is an interval and endpoint gluing connects exactly the
same corner classes. There are V=8,E=12,F=4, hence Euler characteristic
zero. Face connectivity makes this a torus. The support was the set of
actually occurring stars, so every quotient vertex has angle 2pi.
The induced metric is therefore a complete flat torus. The established
flat-torus development argument lifts its faces to a Euclidean plane
tiling with two independent translational periods. A local legal patch
alone is never used as an extension proof.

## Deterministic branch, including reflections

Each residual support partitions the twelve actual corner indices into
four triples. Thus each host actual corner specifies its unique occurring
star. For each native ray incident to that corner, exactly one of the
other two corners contains that numerical ray length, because the three
ray lengths are distinct. This fixes the neighboring prototile and actual
corner index. The neighboring side slot is then unique: its two incident
side lengths differ. The full side determines the far endpoint of that
same neighbor. The independent checker verifies that the far host corner's
unique star selects exactly that far neighbor corner.

There is a unique COMPLETE relative isometry, not merely a symbolic rule:
match the selected neighbor side and the specified starting endpoint to
the host side and endpoint. There are two plane isometries of a segment
with those endpoint images, differing by reflection in its supporting
line. Exactly one places the polygon interiors on opposite sides.
Hence reflections introduce no second allowed neighbor placement. The
finite intrinsic state can be the indexed reference prototile itself;
the deterministic rules are intrinsic to the fixed actual-support branch,
not additional restrictions imposed on the shapes. The edge-to-edge tile
adjacency graph is connected. All hypotheses of the reviewed intrinsic
geometric determinism lemma are met, and that defect-free tiling itself
has a rank-two translation lattice. Finitely many absolute orientations
are not assumed.

## Defects and remaining uncertainty

No substantive mathematical defect found in the scoped theorem, finite
support reduction, torus branch, or determinism branch. No author proof
was edited and no mathematical repair was required. The independent
checker does not re-prove the defect-free limit or intrinsic determinism
lemmas; those are explicitly imported reviewed dependencies. It does
independently check all new finite data and both-endpoint determinism.

The theorem does not cover a separation-one or separation-three repeat,
fewer distinct side lengths, arbitrary side counts, or arbitrary convex
pairs. Neither its restricted scope nor its proof supplies the required
main-problem resolution or a novelty audit.
