# A skew-angle flat forces equal lengths in the changed shared-repeat pair

Date: 2026-10-15. Status: standalone implication independently hostile-reviewed VALID; [review](../reviews/hexagon-changed-word-skew-flat-metric-hostile-2026-10-15.md). The named affine-flat provenance is separate and unused in the current periodicity theorems.

## Exact statement

Let A,B be strictly convex hexagons with common positive lengths named r,x,y,z,t and cyclic words

    A=(r,x,r,y,z,t), B=(r,z,r,y,x,t).

No numerical distinctness is needed for the following implication. Write angles in radians, at corners immediately after the corresponding side. Suppose, for real p,q0,u0,v0, the angle words are

    A=(2pi-u0-v0, 2pi-p-q0, -q0+u0+v0, q0, u0, p+q0-u0),
    B=(2pi-p-q0, 2pi-u0-v0, p, q0, u0, v0).

Then x=z. In particular, this angle flat is impossible when all five physical lengths are distinct. These are exactly maximal affine flat7 in the connected-r support certificate. The proof applies at every rank-degenerate metric, not just generic closure matrices.

## Proof

Put delta=p+q0-u0-v0=a5-b5, Q=exp(i delta), and H=exp(i delta/2). Strict convexity gives a5,b5 in (0,pi), so |delta|<pi, H+H^{-1}=2cos(delta/2)>0, and 1+Q is nonzero.

Independently rotate the two reference polygons so each side0 has complex unit direction1. Let U be A's side1 direction. From the angle words, consecutive side directions turn by pi minus the intervening interior angle. Direct substitution gives:

* A side2 and B side2 both have direction Q U^2;
* B side1 has direction Q U;
* A side4 has direction -Q U, and B side4 has direction -U;
* the direction of A side3 is Q times that of B side3, and the same holds for side5.

These identities also hold when delta=0. For example, if alpha=a0=2pi-u0-v0, then U=-exp(-i alpha), a1=b0=alpha-delta, and b1=alpha. Thus side2 has direction exp(-i(2alpha-delta))=QU^2. The remaining statements follow by adding a2 or b2 and then the common a3=b3, a4=b4.

Write V3,V5 for the directions of B sides3,5. Polygon closure is

    r(1+QU^2) + xU - zQU + Q(yV3+tV5) = 0,
    r(1+QU^2) - xU + zQU +   yV3+tV5  = 0.

Subtract Q times the second equation from the first:

    r(1-Q)(1+QU^2) + (1+Q)U(x-Qz) = 0.

Divide by the nonzero complex number (1+Q)UH. The coefficient of r becomes

    ((1-Q)/(1+Q)) * (H^{-1}U^{-1}+HU).

The first factor is -i tan(delta/2), purely imaginary. The second is twice the real part of HU, hence real, because |HU|=1. Taking real parts leaves

    (x-z) cos(delta/2)=0.

The cosine is strictly positive, proving x=z.

## Scope and dependencies

This is a polygon-closure identity. It assumes no tiling, local extension, finite quotient, or closure-matrix rank. Its use as one branch of a tiling theorem requires the separate connected-r necessary support gate. It does not exclude the other six maximal flats or any arbitrary two-hexagon family.
