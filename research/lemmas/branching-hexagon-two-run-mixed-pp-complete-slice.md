# Complete mixed-homogeneous pp / qq-low-high metric slice

Status: **VALID after fresh independent inventory, arrangement/native-seam and actual-phase reviews, with [whole-theorem synthesis](../reviews/branching-hexagon-two-run-mixed-pp-complete-slice-synthesis-review.md).** This classifies the complete specified resonance slice, with all exceptional star intersections retained. It does not classify every homogeneous resonance or resolve the unrestricted target. No exclusion is inferred from a timeout, a bounded tiling search, or positive angle coverage.

## Actual domain and theorem

Fix angles in degrees with

    0<delta<30, 90<alpha<180, beta=360-2alpha,
    P_alpha=1+2i sin(alpha), rho=arg(P_alpha),
    q=1, p=2cos(delta)/|P_alpha|.

Require p unequal to1 and alpha-rho+delta<120. A has side lengths(p,q,p,q,p,q) and edge directions

    (0,60+delta,120,180+delta,240,300+delta).

B has lengths(p,p,p,q,q,q) and edge directions

    (0,180-alpha,alpha,rho+120-delta,
     rho+180+delta,rho+240-delta).

Its native angles, before each indexed side, are

    (60+rho-delta, alpha, beta, 60+alpha-rho+delta,
     120-2delta,120+2delta).

**Theorem. The pair tiles the plane if and only if alpha120. At alpha120 it has a doubly periodic tiling. Every other actual-domain alpha is untileable, with unrestricted contacts permitted.**

The scalar p is positive. A closes by its threefold symmetry. B's first three unit p vectors sum

    1+exp(i(180-alpha))+exp(i alpha)=1+2i sin(alpha)=P_alpha.

Its three unit q vectors sum -2cos(delta) exp(i rho): the middle direction is rho+180+delta and the other two directions are rho+120-delta and rho+240-delta. Thus pP_alpha cancels the q chain exactly. P_alpha has real part1 and positive imaginary part, so it never vanishes and its principal phase is uniquely in(0,atan(2)), in particular(0,90).

Both displayed angle lists have every angle strictly between0 and180 precisely under the domain restrictions: beta is in(0,180); the two qq angles are in(60,180); B0 is positive and less150; B3 is positive, and B3<180 is exactly alpha-rho+delta<120. Successive edge directions therefore turn strictly by angles in(0,180) and make exactly one full turn. Together with closure and positive lengths this gives a strictly convex polygon. One direct support argument is to project all successive edges on the left normal of a chosen side: positive edge projections occur before negative ones because the ordered directions run once around the circle; their partial sums are strictly positive away from that side's endpoints and return to0 at closure. Every other vertex is strictly on its interior side. Thus strict convexity is obtained on the full domain, not by continuation from a sample.

At alpha120, beta120, P_alpha=1+i sqrt3=2 exp(i60), rho60 and p=cos(delta). The pair is exactly the independently reviewed first periodic curve, hence gives the positive implication throughout0<delta<30. This has p unequal to1 automatically.

## Complete 48-type inventory and 21 exceptional equations

A corners are A_H=120+delta and A_L=120-delta. B homogeneous corners are alpha,beta on pp and chi=120-2delta,psi=120+2delta on qq; its two mixed corners are B0 and B3 above. Because p unequal toq, a cyclic trivalent star has either zero or two mixed pq corners. The zero-mixed stars are the four three-corner multisets from each of the two homogeneous arcs. The two-mixed stars are the10 unordered pairs chosen with repetition from(A_H,A_L,B0,B3), each followed by one of the four homogeneous corners. This is the complete48 named length-legal domain, before indexed occurrences and orientations are expanded.

Use coefficient order(constant,delta,alpha,rho). The exact named angle rows are

    AH (120,1,0,0); AL (120,-1,0,0);
    B0 (60,-1,0,1); B3 (60,1,1,-1);
    alpha (0,0,1,0); beta (360,0,-2,0);
    chi (120,-2,0,0); psi (120,2,0,0).

Exactly three named types sum360 identically:

    alpha+alpha+beta; AH+AH+chi; AL+AL+psi.

The45 other raw equations, after division by integer gcd and consistent sign, give22 distinct proper affine equation classes. One is delta0, outside the domain. The remaining21 classes are exactly

    alpha=120+k delta, k=-2,-1,0,1,2;                  (5)
    rho+alpha=180+k delta, k=0,2;                     (2)
    rho-2alpha=-180+k delta, k=0,2;                   (2)
    2rho+alpha=240+2delta;                            (1)
    2rho-3alpha=-240+2delta;                          (1)
    rho-alpha=-60+k delta, k=-2,0,1,2,4;              (5)
    rho=60+k delta, k=-2,0,1,2,4.                     (5)

All21 equations pass through(delta0,alpha120,rho60). Outside their union the only three identity star types contain no B mixed corner, already preventing a complete trivalent tiling using B. The argument below retains every intersection instead of making a generic-only conclusion. The certificate stores all48 raw named triples, their coefficient rows and the exact raw-index partition into all22 classes.

## Complete finite arrangement, distinct from nonlinear metric geometry

The strict linear angle envelope is

    0<delta<30, 90<alpha<180, 0<rho<90,
    alpha-rho+delta<120.

Every actual polygon above belongs to this envelope. It deliberately does not impose rho=arg(P_alpha) or p unequal to1, and can include unrealized geometry. SAT for this envelope is only a necessary balance outcome.

Represent each exceptional equation as a row in Q^4. Retain every subset of size0,1,2,3 of the21 rows: exactly1+21+210+1330=1562 raw generators. Discard only affine-inconsistent subsets, characterized by augmented rank greater than variable-coefficient rank. Canonical rational row spaces yield99 distinct consistent flats, each with all its generating subsets retained. Six do not meet the strict envelope; all six bases contain the delta0 equation. The remaining93 flats each have a nonempty relatively open envelope intersection.

The complete active set of a flat is every one of the21 rows in its row space. A stratum is that flat minus all nonactive exceptional hyperplanes, intersected with the envelope. Finitely many proper hyperplanes cannot remove its relatively open envelope intersection. Retained rational samples prove linear feasibility only; they need not avoid every nonactive hyperplane and are never claimed to be metric points.

Every actual metric point has one full-active stratum. Indeed its vanishing exceptional rows have consistent affine rank at most3, so a basis is among the1562 generators. Closing that basis under row-space membership recovers exactly all exceptional equations that vanish at the point. Consequently no extra star on an intersection is omitted.

## Every indexed native star and signed seam, with free species frequencies

For each of the93 strata, retain all12 indexed native corners, including all three repeated A_H and all three repeated A_L slots. Enumerate every indexed three-corner multiset whose angle-sum-minus360 row lies in that flat's row space. Expand every permutation and every choice of reflected occurrence; retain precisely the cyclic binary side-label matches and identify only cyclic rotations of the whole star. This includes all legal ppp and qqq stars. Additional angle equalities occur only in their separately retained smaller strata.

At each whole seam use the reviewed typed native-slot/xor-parity feature. The sign is positive at flag0 of the smaller typed slot and negative at flag1; both flags reverse at the opposite endpoint and cancel. When the two typed slots coincide and their parity is1, the feature is zero because no occurrence is distinguished. All other features have an unambiguous sign. Retain every star's12 corner counts C_t and full signed seam vector S_t.

The exact necessary system on each stratum is

    sum_t C_t X_t = F_A M_A+F_B M_B,
    sum_t S_t X_t = 0,
    X_t>=0, F_A>=0, F_B>=0, F_A+F_B=1.

No equality of A and B frequencies is imposed; omission is allowed. All93 primary systems and subsequent certificate extractions finish: **71 UNSAT with retained rational strong duals;22 SAT with retained rational primals;0 UNKNOWN.** A secondary mixed-species solve produces F_A=F_B=1/2 for each22 SAT record, as an outcome. Solver limits are10 seconds per solve; any timeout would remain UNKNOWN, but none occurs.

Each retained negative decision uses an exact checked rational functional, not solver status alone:

    W dot C_t+Y dot S_t>=0 for every retained star;
    W dot M_A<=-1, W dot M_B<=-1.

All inequalities and every positive primal corner/seam equation are checked with Fraction arithmetic before saving. The unrestricted exclusion is the reviewed defect-free ETE/trivalent limit followed by signed-seam boundary cancellation. A square's selected tiles carry total W-charge at most-N. Complete stars have nonnegative augmented charge; interior seam endpoint features cancel; only O(R) boundary stars/seams remain, whereas N=Omega(R^2). This is impossible. No actual frequency limit, positive frequency for both species, or periodicity hypothesis is needed.

## Complete nonlinear phase filter of all 22 SAT strata

Exact row-space membership proves that each of the22 SAT flat bases forces at least one of

    alpha120; alpha+rho180; rho=2alpha-180.

On the actual metric domain each implies alpha120:

1. alpha120 gives P_alpha=2exp(i60), rho60 directly.
2. alpha+rho180 implies exp(i alpha)P_alpha is negative real. Its imaginary part is sin(alpha)(1+2cos(alpha)). Since90<alpha<180 gives sin(alpha)>0, the sole zero is cos(alpha)=-1/2, hence alpha120.
3. rho=2alpha-180 implies exp(-2i alpha)P_alpha is negative real. Its imaginary part is

       2sin(alpha)(cos(2alpha)-cos(alpha))
       =2sin(alpha)(2cos(alpha)+1)(cos(alpha)-1).

   The roots sin(alpha)=0 and cos(alpha)=1 are outside the stated alpha interval. The only permitted root is again cos(alpha)=-1/2, so alpha120.

These are necessary imaginary-part tests, not asserted converses on an arbitrary ray; direct evaluation at alpha120 supplies the required principal phase and signs. No tangent denominator has been discarded. More explicitly let u=tan(alpha/2)>1, finite. Exact rational identities are

    Im(exp(i alpha)P_alpha)=2u(3-u^2)/(1+u^2)^2;
    Im(exp(-2i alpha)P_alpha)=-8u^3(3-u^2)/(1+u^2)^3.

Their denominators are strictly positive. The u0 root is excluded and the only allowed positive root u=sqrt3 gives alpha120. P_alpha has real part1 everywhere, so no chain-zero or phase-denominator root exists. The filter retains these factor branches explicitly.

At alpha120,rho60, all21 exceptional rows reduce to their delta coefficient timesdelta. Exactly indices[4,5,12,16,17] vanish fordelta>0 in the saved ordering: rho-alpha=-60, rho60, alpha120, rho-2alpha=-180, rho+alpha180. Only stratum73 has this complete active set. The other21 SAT strata either impose an extra equation that would force delta0 or omit a phase-forced active equation. They are not further actual geometric survivors, even if their underlying flat intersects the actual curve. The certificate checks complete active sets, not merely flat membership.

This leaves exactly the known periodic first curve. Together with the71 strong duals and the positive quotient theorem, it proves both directions of the whole-slice result after fresh independent review.

## Retained artifacts and review scope

All files share prefix `branching-hexagon-two-run-mixed-pp-`:

- `research/searches/...exceptional-stars.py` and matching certificate: full48 named types,3 identities,22 classes and21 interior equations;
- `research/searches/...strata-slot-balance.py` and matching certificate: all1562 generators,99 flats,6 rejected envelope flats,93 native models,71 duals and22 primals;
- `research/searches/...strata-metric-filter.py` and matching certificate: exact rational phase identities, all22 SAT filters, complete active set and unique stratum73.

Every producer is read-only by default and requires explicit `--output` to write. The slot producer imports its authoring inventory for angle rows; independent verification must reconstruct all rows without producer imports. The metric filter has no solver import and verifies saved exact data. Fresh review must independently check the complete arrangement and all indexed native stars/seams/duals/primals, the full actual strict domain, phase factor roots, active-set comparison, boundary argument and periodic-construction transfer. The independently reviewed theorem is a whole open two-parameter slice with its proper exceptional subloci classified, not only an isolated fixture.
