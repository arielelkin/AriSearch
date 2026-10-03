# Hostile review: obtuse-angle edge-to-edge forcing

**Artifact reviewed:** [obtuse-edge-forcing.md](../lemmas/obtuse-edge-forcing.md).

**Date:** 2026-10-02
**Verdict:** **Valid.**

The review separately checked a tile vertex in another side interior,
subdivision endpoints, one side extending beyond another, collinear boundary
overlaps, point contacts, and reflected copies.  Local finiteness follows
from the finite positive-area protoset.  The strict inequalities are
essential: an angle equal to \(\pi/2\) permits two corners to fill a
half-plane, while redundant \(\pi\)-angles destroy the genuine-corner count.

After T-junctions are excluded, every contact subdivision disappears and
all vertex sectors are genuine corners.  The bounds
\(\pi/2<\alpha<\pi\) then force valence exactly three.

The stated side-count consequences were checked against the exact curvature
identity.  They do not exclude an obtuse pentagon paired with a polygon of
seven or more sides, where negative side curvature can balance pentagons.

The later frequency corollary for side counts $(5,n)$, $n\ge7$, was also
checked.  Edge-to-edge trivalence sets both nonnegative defect terms in the
curvature identity to zero, leaving
$N_5-(n-6)N_n=O(R)$.  Combining this with the uniform quadratic total tile
count gives quadratic lower bounds for each type and the stated Følner ratio.
The argument gives density, not syndeticity, for the $n$-gons.
