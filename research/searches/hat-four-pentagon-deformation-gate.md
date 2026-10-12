# The fixed four-pentagon cut has no surviving two-class hat deformation

Date: 2026-10-12. Status: [independently reviewed VALID scoped exclusion](../reviews/hat-four-pentagon-deformation-review.md).
This covers the specified cut and parameter domain, not arbitrary hat partitions.

## Source, parameters and proposed mechanism

Use the direction-preserving Tile(a,b) outline from Section6 of Smith,
Myers, Kaplan and Goodman-Strauss,
[An aperiodic monotile](https://arxiv.org/html/2303.10798v3).
Normalize a=1 and write its thirteen cyclic outline vertices h_0,...,h_12.
Starting from the repository's exact Tile(1,sqrt3) coordinates, scale every
edge of squared length3 by b/sqrt3 and leave edges of squared length1 or4
unchanged. The length4 case is the merged pair of unit sides. The two edge
classes each close independently, so the deformed outline closes exactly.

Let O=h_0, X=h_4, M=h_8 and Y=h_11. Introduce one interior cut vertex

    V=(u, y(h_7)).

The source segment h_7 M is horizontal of unit length, so M lies on the
side h_7 V when u<x(M). Draw OX and the three spokes VX,VY,VM. The four
prescribed counter-clockwise polygons are

    P6   =[h0,h1,h2,h3,h4],
    P9   =[h0,h4,V,h11,h12],
    P48  =[h4,h5,h6,h7,V],
    P192 =[V,h8,h9,h10,h11].

The names agree with whole-kite masks at b=sqrt3,u=2, but the general
members are not asserted to be unions of eight congruent standard kites.
There are precisely two real free parameters (b,u), with b>0. Reflections
are identified as usual. A valid compiler needs the cuts to partition the
source outline and the resulting shapes to have at most two classes.

This template changes an actual hypothesis of the earlier fixed-kite gate:
it varies the source ratio and permits a nonstandard internal cut vertex.
It retains a higher-valence source scaffold and a prescribed T-junction at M.
If a two-class convex point had survived, matching its side/angle signatures
would have been a concrete route to recovering these cuts and grouping
pieces into hats. The present result stops that obligation before any
unrestricted recognition is asserted: the class-economy gate already fails.

## Exact necessary class-collapse test

If four polygons have at most two congruence classes, any selected three
of them contain a congruent pair. Consequently it is necessary that at
least one of

    P6~P48, P6~P192, P48~P192

holds. P9 does not need to be used in the congruence equations. This avoids
an incomplete choice of two-block partitions: the three-polygon pigeonhole
condition is necessary for every such partition.

For each pair, each of five cyclic shifts and both cyclic directions,
equate all ten squared vertex distances. The coordinate entries are affine
polynomials in b,u over Q(sqrt3); squared distances are exact quadratic
polynomials. On strictly convex pentagons every isometry induces one of
these ten cyclic correspondences. No numerical rotation factor or drawing
decides congruence.

All **30 ideals** are empty or zero-dimensional. Every real root is found
exactly. The filter requires b>0, u<x(M), nonzero polygon sides and global
convexity of each of the four polygons. Supporting-line tests reject a
multiply-wound polygon even if its local turns were positive. The retained
filter uses a superset of genuine source partitions; no omitted cut
membership inequality can introduce additional valid compiler points.

## Result and periodic kill

The only point passing the strict-convex filter is

    b=sqrt3, u=2.

Six congruence correspondences reproduce this same exact point. Its defining
data are b^2=3 with b>0 and u=2. It is the original hat point: all four
pieces are congruent two-kite pentagons. They form the already reviewed
fixed decomposition, and each pentagon tiles periodically by the regular
hexagon's three-piece dissection. See the
[reviewed obstruction](../lemmas/hat-eight-kite-convex-cluster-obstruction.md).

Thus no strictly convex two-class specialization of this prescribed
four-pentagon compiler survives. Boundary degenerations that reduce a piece
to four or fewer intrinsic corners have a triangle/quadrilateral monohedral
escape; the computation does not purport to classify every such degeneration.
The stated compiler family has at most five corners per piece and the
source parameters are positive, so these degenerations cannot supply an
aperiodic exception.

## Trust, limitations and replay

Producer: `research/searches/hat-four-pentagon-deformation-gate.py`.
Certificate: `research/certificates/hat-four-pentagon-deformation-gate.json`.
The certificate includes exact polygon entries, every correspondence ideal,
its Groebner basis and every real-point record. No resource timeout or
random sample was involved. The [fresh independent review](../reviews/hat-four-pentagon-deformation-review.md)
is VALID: all thirty ideals were independently reconstructed, and the sole
point was checked for exact assembly and congruence. Shared Sage/Singular
arithmetic remains computational trust.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/hat-four-pentagon-deformation-gate.py TEMP_CERTIFICATE.json

The command passed on2026-10-12. It does not prove a source partition for
arbitrary parameter values, a recognition theorem for final shapes, or an
exclusion of different cut graphs, additional internal vertices or cross-hat
clusters. The compulsory-pair classification makes those missing positive
obligations unnecessary for this failed template; it does not solve the
original two-convex-polygon problem.
