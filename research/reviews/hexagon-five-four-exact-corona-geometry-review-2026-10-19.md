# Exact seven-corona geometry audit

Date: 2026-10-19. Verdict: **valid within the stated finite domain**.

Claim reviewed: whether any of the seven formal boundary coronas for
A=(0,1,2,0,3,4), B=(0,1,1,0,2,3) is an actual finite gap-free,
nonoverlapping local ring at the exact metric lengths (1,2,3,sqrt(3),4)
and end-of-side interiors A=(90,120,150,120,90,150),
B=(150,120,90,150,90,120).

All seven pass. Each patch has exactly ten distinct tiles: two central A
tiles and eight external tiles. Thus ten is the smallest retained patch
among these seven coronas. This does not assert minimality among other
possible patches.

## Independent reconstruction and checks

The script constructs both polygons independently from exact side vectors
in Q(r), r^2=3, r>0, taking side0 along the positive x axis and turning
left by 180 minus the end-of-side interior after each side. It asserts
exact closure and strict convexity by checking every nonincident vertex
strictly to the left of every directed edge. Coordinates are retained in
the certificate.

The second central A is the halfturn of the first through the midpoint of
side5. Its ten-edge union boundary is A sides0..4 followed by their
halfturned counterparts. For each retained state cycle, the state in
position k+1 places the external tile along boundary edge k. Handedness
+1 reverses the shared-edge direction and handedness -1 preserves it
while reflecting the polygon. Each map is checked orthogonal exactly.

To attack inconsistent identity, the external placements at the two edges
incident to either central seam endpoint are compared as exact unordered
vertex sets. Both pairs agree for every corona. All geometrically identical
tiles are identified globally before further checks. No distinct pair in
any resulting patch has overlapping interior, by the exact separating-axis
criterion for convex polygons. At each of the ten central boundary
vertices, exact native angles of the incident patch tiles sum to 360.
Disjoint convex sectors with this sum cover a full neighborhood of the
vertex. Shared central edges are covered on their opposite side, so the
central dimer has a gap-free finite ring.

No defects or repairs were required. This verifier does import the seven
formal state cycles from the atlas; it does not certify completeness of
that combinatorial enumeration. It independently decides geometry of
exactly those seven cycles. No additional corona or extension search was
performed. It establishes neither plane extension nor periodicity nor
aperiodicity. Parent research separately reports that A alone has a
periodic escape, which this finite audit does not revisit.

## Evidence and replay

Script: `research/reviews/hexagon-five-four-exact-corona-geometry-2026-10-19.py`.
Certificate: `research/certificates/hexagon-five-four-exact-corona-geometry-2026-10-19.json`.
The certificate contains every exact patch, overlap list, identity check,
and vertex-angle sum. No randomness or timeout; domain completed.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-five-four-exact-corona-geometry-2026-10-19.py

Arithmetic: SageMath QuadraticField(3), exact ordered real quadratic field.
