# Homogeneous pp slices with the reversed qq order

Status: **VALID after fresh independent finite/native-geometry, actual-phase and positive-transfer audits, with [whole-theorem synthesis](../reviews/branching-hexagon-two-run-reverse-qq-homogeneous-slices-synthesis-review.md).** These are two specified whole metric slices. Reversing B's qq order keeps A(delta) fixed and changes the actual B mixed angles. No result is obtained by silently identifying the forward and reversed formulas.

## Both exact domains

A has lengths(p,1,p,1,p,1), directions(0,60+delta,120,180+delta,240,300+delta), with0<delta<30. B has lengths(p,p,p,1,1,1), but now its qq corner order is

    chi=120+2delta, psi=120-2delta.

The common q directions are

    (rho+120+delta,rho+180-delta,rho+240+delta).

Their unit vector sum is still -2cos(delta)exp(i rho). The first p-chain determines rho and p by cancellation. Always require p unequal to1.

**Single-120 reversed slice.** Set alpha120 and0<beta<180,

    P_beta=1+exp(i60)+exp(i(240-beta)),
    rho=arg(P_beta), p=2cos(delta)/|P_beta|.

B's directions are(0,60,240-beta) followed by the displayed q directions. Its native angles are

    (60+rho+delta,120,beta,300-rho-delta-beta,
     120+2delta,120-2delta).

P_beta has real part at least1/2 and imaginary part positive on0<beta<180, so it is nonzero and0<rho<90. The actual strict convex domain is precisely rho+beta>120-delta. All other B angles are strictly in(0,180); for B3 positivity use beta+rho<270 and delta<30. A closes by symmetry, and B closes by the displayed p/q cancellation. Ordered positive side directions with all turns in(0,180) give the same strict-support proof as in the forward-slice lemma.

**Single-120 theorem. This pair tiles the plane if and only if beta is60 or120. Both branches admit doubly periodic tilings for the entire0<delta<30 interval.**

**Mixed homogeneous reversed slice.** Set90<alpha<180, beta=360-2alpha,

    P_alpha=1+2i sin(alpha), rho=arg(P_alpha),
    p=2cos(delta)/|P_alpha|.

B directions are(0,180-alpha,alpha) followed by the q directions. Its native angles are

    (60+rho+delta,alpha,beta,60+alpha-rho-delta,
     120+2delta,120-2delta).

P_alpha has real part1, is never zero and0<rho<atan(2)<90. The strict actual domain is precisely alpha-rho-delta<120. B0 is positive and less180 because rho<90 and delta<30; B3 is positive since alpha>90,rho<90,delta<30, and its upper bound is exactly the displayed inequality. Other angles and closure are as in the preceding proof.

**Mixed theorem. This pair tiles the plane if and only if alpha120. That branch admits a doubly periodic tiling.**

## Complete exceptional arrangements and retained certificates

For the single-120 slice use exact coefficient order(constant,delta,beta,rho), named angle rows

    AH (120,1,0,0); AL (120,-1,0,0);
    B0 (60,1,0,1); B3 (300,-1,-1,-1);
    alpha (120,0,0,0); beta (0,0,1,0);
    chi (120,2,0,0); psi (120,-2,0,0).

The complete48 named length-legal types have five identities: three alpha; twoAH+psi; twoAL+chi; AH+AL+alpha; B0+B3+beta. The43 remaining raw equations give15 proper classes including delta0. The14 interior classes are

    beta=120,120±2delta;
    rho=60+k delta, k=-4,-2,-1,0,2;
    rho+beta=180+k delta, k=-4,-2,-1,0,2;
    2rho+beta=240-2delta.

All470 subsets of size at most3 are retained. Their canonical rational affine row spaces give52 consistent flats; four force delta0 and miss the strict envelope. The48 positive-envelope strata use0<delta<30,0<beta<180,0<rho<90,rho+beta>120-delta. Complete indexed native-star and signed-seam systems yield **34 retained rational strong duals,14 retained rational mixed primals,0 UNKNOWN**.

For the mixed slice use coefficient order(constant,delta,alpha,rho). Its named rows change B3 to(60,-1,1,-1), alpha to(0,0,1,0) and beta to(360,0,-2,0), with the other rows above. The48 types have three identities: twoalpha+beta; twoAH+psi; twoAL+chi. The45 raw remaining equations give22 proper classes including delta0. The21 interior classes are

    alpha=120+k delta, k=-2,-1,0,1,2;
    rho+alpha=180+k delta, k=-2,0;
    rho-2alpha=-180+k delta, k=-2,0;
    2rho+alpha=240-2delta;
    2rho-3alpha=-240-2delta;
    rho-alpha=-60+k delta, k=-4,-2,-1,0,2;
    rho=60+k delta, k=-4,-2,-1,0,2.

All1562 subsets of size at most3 give99 consistent flats; six force delta0 and miss the envelope. The93 positive-envelope strata use0<delta<30,90<alpha<180,0<rho<90,alpha-rho-delta<120. Their full indexed native systems yield **71 retained rational strong duals,22 retained rational mixed primals,0 UNKNOWN**.

Each stratum is its flat minus every nonactive exceptional hyperplane. Its complete active set is all equation rows in its row space. All generators are saved, so every actual point belongs to a stratum represented by at most3 basis equations; extra intersections never silently acquire unrecorded stars. Rational samples prove only linear feasibility and are not asserted to be generic or metric points.

In both models enumerate all12 indexed corners, every angle-legal native multiset, every permutation and reflection, and every cyclic binary length match. No homogeneous star is omitted. The seam features are the reviewed typed slot/xor-parity signs, with ambiguous equal-slot parity1 omitted as zero. The normalized model leaves F_A,F_B free nonnegative with sum1. Every saved dual is checked exactly against all stars and has native W-charge at most-1 for each species; every saved primal is checked against every corner and seam equation. Secondary mixed solves happen to return1/2 each, as outcomes. Solver timeouts would be UNKNOWN and no timeout occurs.

The negative implication uses the reviewed actual defect-free trivalent ETE limit plus square-boundary charge cancellation: all interior seam features cancel, complete stars have nonnegative augmented charge, boundary contributions are O(R), and selected tile charge is at most-N with N=Omega(R^2). A negative per-tile charge for each species handles omission automatically. Positive angle-envelope primals are never treated as tilings.

## Complete actual phase filters

For single-120, all14 SAT row spaces force beta120, rho60, or rho+beta180. The metric P_beta is unchanged from the forward slice. With u=tan60=sqrt3 and v=tan(beta/2)>0 finite, the exact imaginary-part numerators over positive denominator(1+u^2)(1+v^2) are

    sin120-sin(beta): 2(u-v)(1-uv);
    sin(beta)-sin(beta-120)-sin120: 4uv(u-v).

Thus beta120 directly and rho+beta180 each give beta120; rho60 gives beta120 **or beta60**. Both branches now lie in the strict domain. At beta60,P_beta=exp(i60),rho60,p=2cos(delta), and B3=180-delta<180. This is the important distinction from the forward qq order, where B3 was180+delta and excluded that root. There are no omitted denominator roots or chain-zero cases.

For beta120 the full active14-equation set is[3,6,11], stratum39. For beta60, exactly one interior exceptional breakpoint exists: delta15. Away from it the full active set is[3], stratum38; at delta15 it is[3,8], stratum43. The exact phase-filter enumerates every plane's affine restriction to beta60,rho60, retains all rational roots in0<delta<30, and verifies that15 is the only root. All other11 SAT strata fail the full actual active-set comparison.

For the mixed slice, every22 SAT flat forces alpha120, alpha+rho180, or rho=2alpha-180. With P_alpha=1+2i sin(alpha), the last two necessary imaginary parts are

    sin(alpha)(1+2cos(alpha));
    2sin(alpha)(2cos(alpha)+1)(cos(alpha)-1).

On90<alpha<180 the only allowed root is alpha120. With u=tan(alpha/2)>1 finite, exact rational numerators are2u(3-u^2) over(1+u^2)^2 and-8u^3(3-u^2) over(1+u^2)^3. The denominators are positive, u0 and cosalpha1 are excluded, and P_alpha's real part1 prevents a phase-chain zero. Thus rho60,p=cos(delta); its full active set is[4,5,12,16,17], uniquely stratum73. The other21 SAT strata cannot contain actual metric points.

## Exact positive transfers and native-order caution

Reflect B and then reindex its native sides in order(2,1,0,5,4,3). Its native vertices are reordered(3,2,1,0,5,4). Therefore the native corners transform as

    (B0,alpha,beta,B3,chi,psi)
      ->(B3,beta,alpha,B0,psi,chi).

A reflected B is an allowed copy of the same prototile; this transfer leaves the A prototile unchanged. In particular:

- Reversed beta120, or reversed mixed alpha120, becomes the forward pair alpha=beta120,qq(low,high). This is the reviewed periodic first curve p=cos(delta).
- Reversed single beta60 becomes the forward complementary-pp cone at alpha60,beta120,qq(low,high), with p=2cos(delta). Its domain60-delta<alpha<120-delta contains alpha60 for every0<delta<30. The mixed corner list after reflection is(180-delta,60,120,120+delta,120-2delta,120+2delta), exactly that reviewed cone.

These are exact congruence transfers from independently reviewed periodic quotients, not constructions inferred from the feasible balance vectors. They establish every surviving positive branch.

Reflection swaps both pp and qq orders. Consequently the forward single-alpha120 and mixed-twoalpha-plusbeta slices alone never covered every pp-homogeneous case at a fixed qq order. Together with these separately computed reversed slices, all four pp resonance planes with paired qq angles can now be addressed by explicit native reflection, after fresh review.

## Stable artifact scope

Under `research/searches` and `research/certificates`, each of the prefixes

    branching-hexagon-two-run-single-120-reverseqq-
    branching-hexagon-two-run-mixed-pp-reverseqq-

has `exceptional-stars`, `strata-slot-balance`, and `strata-metric-filter` producers and matching JSON certificates. Replay is read-only; writes require explicit`--output`. The separate saved domains preserve all470/1562 generators,52/99 flats,48/93 positive envelopes,34/71 duals,14/22 primals and every exact phase-filter branch. Independent verification must reconstruct native geometry/angle rows without producer imports, check complete arrangements and all vectors/certificates, inspect the actual strict domains and every factor root, and verify both positive reflection transfers. Full-slice status is independently VALID after those checks and whole-theorem synthesis.
