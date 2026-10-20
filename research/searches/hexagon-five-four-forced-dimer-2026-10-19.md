# Forced AA dimers: five/four numerical-color gate

Date: 2026-10-19. Status: exact finite necessary upper atlas; no periodicity theorem.

Domain: strict convex hexagons, A side word (0,1,2,0,3,4),
B any of the180 distinct permutations of (0,0,1,1,2,3), five distinct
positive numerical lengths. This audit concerns an edge-to-edge trivalent
source, available as an admitted limit for a tileable two-hexagon pair.
It does not assert that all original tilings are edge-to-edge.

## Forced dimer lemma

A side5 has color4, absent from B and from all other A sides. Each A must
therefore have exactly one A mate across side5. In particular these contacts
partition A tiles into pairs. Reflected coincidence across the shared
side fixes both endpoints. At its color3 endpoint the two A corners have
incident colors (3,4), so the third sector must have colors (3,3).
Each prototile contains color3 just once, so such a native corner does not
exist, with either orientation. Reflection is impossible. The mate must
instead be the image under the midpoint halfturn. This claim uses the
trivalent source hypothesis. It gives a forced dimer, not a periodic tiling.

## Exact finite definitions

Corner c=6f+i lies between native sides i and i+1. A signed corner port
(c,h), h in {-1,1}, has incoming/outgoing sides (i,i+1) for h=1,
and (i+1,i) for h=-1. Signs describe the same polygon handedness
at every vertex. Enumerate all24^3 ordered triples, permitting repeated
corners, retain consecutive color matches, and quotient cyclic rotation.
A seam between consecutive ports p,q propagates to the other endpoint
as the consecutive ordered pair (far(q),far(p)), with handedness preserved.
Delete any star lacking one of these three endpoint continuations until
the greatest fixed point. All actual trivalent stars lie in this upper atlas.

A simultaneous seam microstate consists of one surviving star, a specified
seam, and one surviving opposite star with those two propagated ports.
A dimer boundary corona is a cycle of ten vertex factors: two AA seam
junctions and eight ordinary A corners. The neighboring native side and
handedness agree at both endpoints of each boundary edge. Evidence retains
all such cycles, with A handedness normalized to +1; reflection supplies -1.
External tile identifications, coincident third tiles, Euclidean overlap,
angle sums and polygon closure are not tested. These are combinatorial
necessary conditions, never actual realized coronas.

## Results and stopping reason

Of180 words,96 lack full twelve-corner cover and84 retain it.
Fixed-star count histogram is4:96,10:12,12:36,16:12,22:12,32:12.
The simultaneous AA-seam endpoint microcorona count is2 for144 words
and8 for36. Among84 full-cover words the ten-vertex boundary-corona counts
are1 for36 words,2 for12,4 for12,7 for12 and100 for12.

Explicit fixture B=(0,1,1,0,2,3) has22 signed stars and7 boundary coronas.
Its only certain neighbor transitions in the entire retained upper atlas
are the two handed readings of the forced AA seam. Thus this atlas supplies
no connected certain-transition mechanism for that fixture. This refutes
only the proposed inference from this upper atlas and the dimer lemma to
universal certain-neighbor propagation. It is not a geometrically realizable
counterexample, and it does not establish that actual source supports lack
such a mechanism.

No larger torus or patch search was launched. The missing step is an
angle/metric-aware necessity mechanism restricting actual supports enough
to force connected deterministic propagation, or a positive periodic
carrier whose angle rows follow from every actual support. The seven and
hundred-corona cases have no such mechanism here. Stop this branch at that
gap rather than expanding bounded torus searches.

## Replay and review status

Producer: research/searches/hexagon-five-four-forced-dimer-2026-10-19.py.
Evidence: research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json.
Independent incidence checker:
research/searches/hexagon-five-four-forced-dimer-check-2026-10-19.py.
The checker independently constructs side endpoint sets and verifies every
retained seam continuation, the reflection obstruction, boundary edge colors,
and the explicit fixture. It does not independently reconstruct the complete
star enumeration or certify geometry; fresh hostile review remains needed.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-forced-dimer-2026-10-19.py --output research/certificates/hexagon-five-four-forced-dimer-2026-10-19.json
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-forced-dimer-check-2026-10-19.py

Explicit fixture corona (closed edge-state cycle, slot IDs A0..5/B6..11):

    (11,-1),(6,-1),(8,-1),(10,-1),(3,+1),
    (11,-1),(6,-1),(8,-1),(10,-1),(3,+1),(11,-1)

These are the third-tile native side/handedness states; the repeated final
state closes the ten-edge cycle. The certificate contains all seven choices.
Route status: **Paused** at the missing angle/metric and global
certain-transition mechanism. No full theorem is claimed.
