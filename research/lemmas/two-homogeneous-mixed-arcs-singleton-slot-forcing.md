# Both mixed homogeneous arcs force singleton slots onto A

Status: **VALID after fresh independent analytic hostile review.** This is a new exact contact/capacity restriction on one both-homogeneous native-angle branch, not a periodicity theorem or an existence claim.

## Exact domain and conclusion

Fix0<delta<30, distinct positive p,q, the displayed threefold alternating A(delta) with H=120+delta,L=120-delta, and a strictly convex binary two-run B with native angles(B0,alpha,beta,B3,chi,psi). Assume

    2alpha+beta=360, 2chi+psi=360,
    alpha!=120, chi!=120.

Thus90<alpha,chi<180 and both arcs are homogeneous but noncentral. Native repetitions, reflections and unrestricted contacts are allowed. No claim is made about the other relative ordering of the two mixed homogeneous arc multisets.

**Conditional lemma. In every actual trivalent edge-to-edge tiling of the two shapes, no B-only nonhomogeneous star contains B's beta or psi native corner. Every such corner outside its pure homogeneous star therefore belongs to a star with one A mixed corner, one B mixed corner and that B homogeneous corner. If N_A,N_B are square-window tile counts, and M_beta,M_psi count the corresponding nonhomogeneous stars, then**

    M_beta>=N_B/2-O(R), M_psi>=N_B/2-O(R),
    N_B/5-O(R)<=N_A<=N_B/3+O(R).

**Consequently any admitted unrestricted tiling, through the reviewed defect-free limit, requires an actual trivalent ETE tiling with both species at quadratic count and at least one legal indexed A/Bmixed/beta star and one legal indexed A/Bmixed/psi star.** This gives the simultaneous necessary angle equations below. A B-only trivalent ETE tiling is impossible in this domain. No periodic escape or tilability is inferred from these necessary conditions.

## Exact native phase geometry

Common-scale q1 and rotate B's side0 to direction0. Its first three p unit vectors have directions0,180-alpha,alpha because beta360-2alpha. Their sum is

    P_alpha=1+2i sin(alpha).

The unit q arc has the same form P_chi. Write rho(x)=arg(1+2i sin x), using its unique principal value in(0,90). Whole closure gives

    p/q=|P_chi|/|P_alpha|,
    direction(q3)=180+rho(alpha)-rho(chi).

There is no direction-lift ambiguity: both rho values lie between0 andatan2, and the actual ordered side3 direction lies between0 and360. The final q direction is direction(q3)+chi. Put t=rho(alpha)-rho(chi). The actual mixed native angles are

    u=B0=chi+t, v=B3=alpha-t,
    u+v=alpha+chi.

The actual strict convexity of B supplies0<u,v<180. On90<x<180, rho strictly decreases: in radians rho'(x)=2cos x/(1+4sin²x)<0. Hence f(x)=x-rho(x) strictly increases. Since sin x strictly decreases on this interval, distinct p,q imply alpha!=chi by the positive arc norm formula|P_x|²=1+4sin²x.

## No B-only mixed beta or psi star

Distinct binary ray labels make every trivalent star either homogeneous or have exactly two mixed corners and one homogeneous corner. A has only mixed corners. A B-only nonhomogeneous star containing beta must have its other two corners selected with repetition from u,v. Its angle equation is one of

    2u+beta=360, u+v+beta=360, 2v+beta=360.

Since beta360-2alpha, the first gives ualpha, equivalently f(chi)=f(alpha); the second gives chialpha; the third gives valpha, equivalently rho(alpha)=rho(chi). Each forces alpha=chi, impossible. Likewise a B-only nonhomogeneous star containing psi would require2u+psi360,u+v+psi360 or2v+psi360. These force respectively rho equality, alphachi, or f equality, and are impossible. This argument deliberately retains all repeated native mixed-slot possibilities and arbitrary mirror states.

## Whole-AA exclusion and native capacities

Neither mixed homogeneous arc has a120 angle outside its excluded center. Neither can be paired{120-2delta,120+2delta}, since its mixed homogeneous equation would then force delta0. The actual two-ended AA seam test therefore excludes both AAp and AAq: its two fillers would require a120 homogeneous slot or the unordered paired arc. Every pair of sectors at a trivalent star are neighbors along a radial seam, so each star contains at most one A. Every A corner has one other mixed corner and one homogeneous corner, both B. Injection into B's two mixed native slots gives6N_A<=2N_B+O(R).

The only pure pp multiset is2alpha+beta, and the only pure qq multiset is2chi+psi: two of the four resonance planes intersect only at the central point. Let Y_p,Y_q count these pure stars and M_alpha,M_chi the other nonhomogeneous native-slot counts. Direct native-corner inventories give

    N_B=2Y_p+M_alpha+O(R), N_B=Y_p+M_beta+O(R),
    N_B=2Y_q+M_chi+O(R), N_B=Y_q+M_psi+O(R).

Thus Y_p,Y_q<=N_B/2+O(R), and M_beta,M_psi>=N_B/2-O(R). The preceding no-B-only result means every M_beta or M_psi star has exactly one A corner. They are disjoint because a nonhomogeneous star has one homogeneous slot. The binary corner ledger2V_m=6N_A+2N_B+O(R),4N_B=V_m+3(Y_p+Y_q)+O(R) also gives N_A=N_B-Y_p-Y_q+O(R). Hence M_beta+M_psi=2N_B-Y_p-Y_q+O(R)=N_B+N_A+O(R). A supplies only6N_A corner occurrences, so N_B+N_A<=6N_A+O(R), proving the stronger stated lower bound N_A>=N_B/5-O(R). Root independently accepted this explicit arithmetic strengthening after the original fresh review. No frequency is presumed to exist.

Boundary discrepancies are uniform O(R) for fixed shapes: any mismatch between vertex, side-midpoint and tile-window selection is supported in a fixed-width boundary band, containing only O(R) tiles by bounded diameter and positive minimum area. Total selected tile count is Omega(R²). Therefore N_A<=N_B/3+O(R) forces N_B quadratic, and the lower bound forces N_A quadratic as well, including after a limit that initially permits omission.

## Explicit simultaneous angle restriction

The beta and psi nonhomogeneous stars each contain A_H or A_L, one B mixed native angle u or v, and the indicated homogeneous slot. Therefore at least one equation in each of the following two four-element lists must hold:

    u+beta=240-delta or240+delta,
    v+beta=240-delta or240+delta;

    u+psi=240-delta or240+delta,
    v+psi=240-delta or240+delta.

Equivalently, using the exact phase t,

    2alpha-chi-t=120±delta or alpha+t=120±delta,
    chi-t=120±delta or 2chi-alpha+t=120±delta.

These are necessary for actual positive native-slot counts, not just hypothetical angle-legal pure stars. They do not guarantee all A H/L corners can be covered, side seam balance, planar development or existence. They apply to this precise simultaneous forward mixed-homogeneous ordering; simultaneous B reflection transfers them to its doubly reversed ordering, while a singly reversed arc needs a separate phase derivation.

The independent local/algebra ledger is retained at `research/searches/two-homogeneous-mixed-arcs-singleton-slot-forcing.py`. The separate numeric reconnaissance is explicitly non-proof work and is not a dependency.

Dependencies: reviewed unrestricted hexagon-to-trivalent-ETE limit; fixed-shape uniform boundary estimates; the directly derived two-ended AA contact test. The unrestricted two-prototile target and other both-homogeneous branches remain unresolved.

The [fresh independent analytic review](../reviews/two-homogeneous-mixed-arcs-singleton-slot-forcing-review.md) accepts the scoped contact, phase and boundary-count proof.
