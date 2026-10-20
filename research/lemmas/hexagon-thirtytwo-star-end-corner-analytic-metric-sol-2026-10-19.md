# Last B orbit: corrected end-corner analytic metric branch

Date: 2026-10-19. Status: independently hostile-reviewed valid for its metric and monohedral claims; see [review](../reviews/hexagon-thirtytwo-star-end-corner-analytic-metric-hostile-sol-2026-10-19.md). This replaces the original metric argument whose closure used a different corner convention from its support. The two certificates describe different analytic branches.

## Statement and indexing

Take A=(0,1,2,0,3,4), B=(0,1,2,0,3,1). The angle alpha(f,i) is at the **end of side i**, between sides i and i+1. There exist strictly convex closed hexagons with these words, five positive pairwise distinct length parameters across the pair (A uses all five; B uses four), and the four angle identities

    a0+a1+b2=2pi; a2+b1+b5=2pi;
    a3+b0+b4=2pi; a4+a5+b3=2pi.

No geometric corona or plane extension is claimed.

## Proof

Let C have rows for both six-angle totals and these four star sums, in native end-corner indexing. Its rank is five. Let N be its exact nullspace basis in the certificate; write alpha=(2pi/3)1+Nx. Every required sum and both polygon totals then hold identically.

The direction of side j is phi(f,j)=sum(k=0..j-1)(pi-alpha(f,k)). This is the decisive corrected convention: corner0 turns side0 into side1. Define F(x,l) to be the two real closure components for each face, summing l[word(f,j)] exp(i phi(f,j)). At x=0, l=(2,1,1,1,1), both closures vanish: opposite length-two sides cancel and the remaining four unit sides cancel. Both base hexagons are strictly convex.

The first four columns of dF/dx at this base are

    [-sqrt(3)/2, sqrt(3)/2, 0, -sqrt(3)]
    [1/2, 1/2, -2, -2]
    [0, 0, -sqrt(3)/2, -sqrt(3)]
    [0, 0, 1/2, 0].

Their determinant is -3/4. Put l(t)=(2,1+t,1+2t,1+3t,1+4t), x4=t, x5=x6=0. The analytic implicit function theorem gives unique analytic x0(t),...,x3(t), all zero at t=0, solving both polygon closures for sufficiently small |t|. For sufficiently small positive t<1/4 the lengths are positive and distinct. Convexity and simplicity persist by continuity from the strict base configuration. This proves the statement without any numerical approximation.

The end-corner derivatives of this branch are

    A: (-2sqrt(3)-1, 4+3sqrt(3), -4-sqrt(3), 2, -sqrt(3), -1+sqrt(3));
    B: (-2, 4+sqrt(3), -3-sqrt(3), 1, 0, 0).

Their four star sums and two polygon totals vanish exactly. Both opposite-repeat H1 angle-sum derivatives are -1 (their complements +1). For the existing end-side H2 template, B's two admissible sums have derivatives +1,-1; A has no H2 length pattern and neither face has H3 adjacent-pair lengths. The script checks all dihedral labels. This audit uses end-side template angles: forward side j carries alpha(j), reversed side j carries alpha(j-1). The independent review checked this against the cited external H1/H2/H3 classification.

## Evidence and limitations

Producer: `research/searches/hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.py`.
Certificate: `research/certificates/hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.json`.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-star-end-corner-analytic-metric-sol-2026-10-19.py

Exact finite calculations use SymPy symbolic rational and quadratic arithmetic, no solver or floating point. They compute rank, derivative matrix, determinant, tangent vector, and twelve dihedral labels per polygon. The IFT and openness supply the analytic existence proof beyond these calculations.

Protocol section5: unrestricted periodic escape and global extension remain blocked without a new global construction/invariant. Four-face failure does not exclude larger carriers, and a feasible local metric supplies no finite-model property. No larger torus search or angle-support enumeration was performed in this correction.
