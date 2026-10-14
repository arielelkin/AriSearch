# Fresh hostile review: fully asymmetric right-pentagon periodic carrier

Date: 2026-10-13. Independent reviewer: contact_structure.
Artifact: [metric and plane proof](../searches/contact-right-angle-nonsymmetric-carrier.md),
[producer](../searches/contact-right-angle-nonsymmetric-carrier.py).
Verdict: VALID for the single stated exact metric and lattice tiling.

The algebraic isolating interval picks c=cos(pi/8), and r=4c squared minus2
is positive sqrt(2). The other positive root is outside the stated interval.
The pentagon closes exactly and its edge directions turn one full circle
with four67.5turns and one90turn. The octagon edges alternate axial/diagonal
and turn45, giving a genuine135-equiangular octagon. Five distinct P side
lengths exclude any nonidentity symmetry. Q side lengths are v,h,u,w repeated;
the private h slots are opposite and have EQUAL length. This example is
therefore outside the distinct-private-slot Q-core theorem, as it should be.

The exhaustive lattice overlap bound uses exact vertex ranges in the lattice
basis. Any intersecting pair must overlap those ranges coordinatewise, so
every possible integer translation is inside the ceil/floor intervals. The
22 nonidentity ordered candidates include every potential self-orbit overlap.
Separating-axis tests are valid for the convex polygons; no empirical radius
cutoff is used. Area equals positive covolume exactly.

A new [independent checker](contact-right-angle-nonsymmetric-carrier-check.py)
reconstructs the geometry using Sage AA radicals without importing the
producer or its number field and replaces separating axes by exact polygon
clipping. It checks all strict supporting halfplanes, five distinct P lengths,
private slots, no permitted doubled flat host, the covolume identity and all
22 exhaustive translation candidates. It passed:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/contact-right-angle-nonsymmetric-carrier-check.py

The resulting infinite packing is locally finite and closed. On the
fundamental torus its area equals the torus area, with no overlaps of positive
area. An uncovered point would belong to its open complement and hence leave
positive missing area. This proves entire-plane coverage, not just a finite
module. Nonzero lattice vectors are periods and both species occur. The
metric checks with the reviewed native reduction really exclude every flat
star for this pair, but the example does not claim all admitted tilings are
periodic. One periodic witness already falsifies aperiodicity.

Only this specified metric is certified; no parameter-family packing,
arbitrary-metric classification, intrinsic forcing or novelty is asserted.
No unresolved objection remains.
