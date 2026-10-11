# Every corner can fit an angle star, yet neither hexagon pair can tile

**Status:** proved and independently adversarially reviewed VALID;
[hostile review](../reviews/angle-frequency-cover-review.md) and
[no-solver exact verifier](../reviews/verify_angle_frequency_cover_independent.py)
completed2026-10-10. This is
a counterexample to a proposed local sufficiency test, not an aperiodic pair
or a complete impossibility theorem. No novelty claim.

## Claim refuted and theorem

Claim refuted: if every corner angle of two convex hexagons participates in
some available three-corner star of total angle360 degrees, then their
angle marginals admit nonnegative whole-tile frequency balance.

Let A have successive native corner angles

    (100,100,100,140,140,140) degrees,

and let B have successive native corner angles

    (100,100,110,130,140,140) degrees.

**Theorem.** No pair of convex hexagons with these angle multisets can tile
the plane, for any positive exact side lengths giving genuine polygons,
including reflected copies and unrestricted contacts. Every angle in the
combined list belongs to an available three-corner360-degree angle star.
Local eligibility here concerns angles alone; it does not assert that
length-matched whole-tile patches exist for all the stars.

## Exact concrete shapes

Take z as the root of z^12-z^6+1=0 with

    98/100 < Re(z) < 99/100, 17/100 < Im(z) < 18/100.

This selects exp(2pi i/36), uniquely among the polynomial's roots. Put
i=z^9. For a multiple t of10 degrees, define the real unit normal

    n(t)=((z^(t/10)+z^(-t/10))/2,
          (z^(t/10)-z^(-t/10))/(2i)).

For either ordered angle list alpha=(alpha0,...,alpha5) above set theta0=0
and thetaj=sum_(k=1..j)(180-alphak), j=1..5. Define the polygon by

    n(thetaj) dot x <= 1, j=0,...,5.

Its vertex j is the intersection of the two lines with normals
n(theta_(j-1)) and n(thetaj), with indices modulo6. Equivalently its finite
exact coordinates are

    vertexj = matrix([n(theta_(j-1)), n(thetaj)])^(-1) (1,1).

All successive exterior turns are40,50,70 or80 degrees, strictly between0
and180, and sum360. The normals surround the unit disk. Each consecutive
tangent-line intersection satisfies every nonincident halfplane strictly,
so every line is a genuine supporting side; exact verification of all36
incidences per polygon is retained. Each interior angle is180 minus the
corresponding normal gap, giving exactly the prescribed lists. The shapes
are compact strictly convex polygons with nonempty interiors. They are
noncongruent because their corner-angle multisets differ.

The certificate retains every coordinate as rational coefficients in the
basis 1,z,...,z^11; the line-intersection definition also suffices without
that expansion. Numerical approximations make no proof decisions.

## Complete unrestricted untileability proof

Every tile corner exceeds90 degrees. At a vertex containing a straight
180-degree tile sector, the remaining180 degrees cannot contain two tile
corners, each larger than90, or a single corner, each smaller than180.
Two straight sectors leave no room for a corner. Thus a native corner
cannot lie inside another native side. All contacts in any putative tiling
are edge-to-edge. At any vertex four corners would exceed360 and two would
fall short, so there are exactly three corners. This argument starts with
unrestricted contacts and permits every reflection.

The combined available angles are100,110,130,140. Exhausting the20
three-element multisets shows that the only stars summing to360 are

    (100,130,130), (110,110,140).

Every available angle appears in one of these stars. Assign corner weights

    w100=2, w110=-1, w130=-1, w140=2.

Every legal star has total weight zero. Each A tile has total weight12,
and each B tile has total weight6, both strictly positive.

For completeness, this yields a contradiction in the infinite plane
without assuming frequencies or periods. Select all tiles whose interiors
meet the interior of Q_R=[-R,R]^2. Their number N is at least4R^2/M,
where M bounds tile areas, because they cover Q_R. Their total corner
weight is at least6N. Every vertex all of whose incident tiles are selected
contributes zero. All nonzero remainder contributions are on the boundary
of the selected patch. A boundary tile meets partial Q_R and lies in its
fixed-diameter neighborhood; the strip area is O(R) and disjoint interiors
of positive minimum area imply O(R) such tiles. With six corners per tile
and weights of absolute value at most2, the boundary contribution is O(R).
Consequently6N<=O(R), contradicting N>=4R^2/M for large R.

Equivalently, the nonnegative angle-frequency equations force
6 fA+3 fB=0, contrary to positive covered area. This alternate formulation
is not needed for the direct boundary proof and does not require both types
to have positive density. Tiling by only one of the shapes is also excluded.

## Exact computation and replay

[Search record](../searches/angle-frequency-cover-counterexample.md),
[producer](../searches/angle-frequency-cover-counterexample.py), and
[certificate](../certificates/angle-frequency-cover-counterexample.json).
The complete finite search compared1081 unordered pairs of sorted angle
multisets;692 passed corner-angle coverage, but11 had inconsistent
nonnegative frequency balance. All681 feasible systems retain rational
solutions; all11 rejections retain rational separating functionals. These
are certificates for the finite linear systems, not tiling certificates.

This concrete pair falsifies the local angle-sufficiency claim. It does
not furnish two tileable shapes and cannot satisfy the main existence gate.
