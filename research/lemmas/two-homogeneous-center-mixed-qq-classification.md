# Complete center-pp / mixed-homogeneous-qq periodic escape

Status: **VALID after fresh independent analytic hostile review.** This class has two homogeneous arcs and was excluded from the earlier center-pp/no-homogeneous-qq theorem. Necessity here comes from native singleton-slot forcing rather than that theorem's unavailable middle-q exclusion.

## Exact theorem

Fix0<delta<30, distinct positive p,q, the native threefold A(delta) lengths(p,q,p,q,p,q) and directions(0,60+delta,120,180+delta,240,300+delta), and a strictly convex B with native length word(p,p,p,q,q,q). Its two pp native angles are120. Suppose its qq angles chi,psi have a mixed homogeneous multiset and are noncentral:

    2chi+psi=360 or chi+2psi=360,
    (chi,psi)!=(120,120).

**Theorem. The pair is tileable if and only if, after optionally reflecting and reindexing B, it belongs to the independently VALID same-slot or cross-slot pp-center periodic family. In particular every tileable pair under these hypotheses has a doubly periodic tiling.** Common normalize q1. The imported positive families are `branching-hexagon-two-run-pp-center-periodic-family.md` and `branching-hexagon-two-run-pp-center-cross-periodic-family.md`, each with a fresh independent whole-domain flat-cover review.

These positive families allow qq homogeneous stars and provide actual periodic tilings; their hypotheses never imposed no-qq-homogeneity. The present necessity does not assume any pure pp or qq star actually occurs in a tiling.

## Exact one-parameter metric and reflection normalization

A reflection/reindexing of B exchanges its pp native angles, its mixed angles and its qq angles; the pp120/120 pair is unchanged. Thus normalize the mixed qq multiset to

    c=chi in(90,180), psi=360-2c, c!=120.

Take B's p directions0,60,120. Their unit sum is2exp(i60). The unit q chain has angles c,360-2c and, relative to its first side, directions0,180-c,c. Its sum is

    P_c=1+2i sin c.

Put rho=arg(P_c) in(0,90). Actual B closure gives

    p/q=sqrt(1+4sin²c)/2,
    first q direction=240-rho,
    u=B0=c+60-rho, v=B3=60+rho.

The native direction lift is unique:240-rho lies in(150,240), while actual B side3 occurs between0 and360. The last q direction is240-rho+c; strict convexity supplies c-rho<120. Conversely c in(90,180),c-rho<120 gives all strict native turns and exact closed positive B. Distinct lengths are equivalent to c!=120 in this interval. In particular no extra phase convention is assumed.

The function rho(c)=arg(1+2i sin c) strictly decreases on(90,180), since rho'(c)=2cos c/(1+4sin²c)<0. The function f(c)=c-rho(c) strictly increases. At c120, rho60 and f60; these are unique on this interval.

## Whole-AA exclusion and no B-only singleton star

The qq arc has no native120 corner outside its center. It is not the unordered pair120±2delta: that pair sums240, while chi+psi360-c would force c120, giving two120 angles rather than the stipulated paired set. The two-ended whole-A p seam test therefore rules out AAp seams, including reflected matches. AAq may occur and is explicitly permitted.

A trivalent binary star has zero or two mixed corners. A B-only nonhomogeneous star containing the native singleton qq slot psi must use two B mixed corners, each from u,v with repetition allowed. Its three angle equations are

    2u+psi=360, u+v+psi=360, 2v+psi=360.

Their residuals from360 are respectively

    2(60-rho),120-c,2(60+rho-c).

The first forces rho60, the second c120, and the third f(c)60. Strict monotonicity forces c120 in all three, excluded. Thus no such B-only singleton star is legal. This argument retains all native mixed-slot repetitions and mirror states; it does not assume a selected partner or generic angle values.

A nonhomogeneous psi star cannot contain two A corners either: they would share an actual A p radial seam, already forbidden. It therefore consists of exactly one A mixed corner, one B mixed corner and the native B psi corner.

## Actual singleton occurrence from boundary counts

Pass any alleged unrestricted tiling to the reviewed actual trivalent ETE limit. Species omission is allowed. Because AAp is impossible, all3N_A A p sides meet B p sides. Each B supplies three such sides, so N_A<=N_B+O(R). Total count is Omega(R²) by coverage and positive fixed areas; hence N_B has quadratic count.

The only legal pure qqq multiset is2c+psi360: the other three resonance equations intersect it only at c120. Let Y_q count those pure stars, M_c count nonhomogeneous c corners and M_psi nonhomogeneous psi corners. Native ledgers give

    N_B=2Y_q+M_c+O(R),
    N_B=Y_q+M_psi+O(R).

Consequently Y_q<=N_B/2+O(R), and M_psi>=N_B/2-O(R). Thus an actual nonhomogeneous psi star exists, indeed at quadratic count. This reasoning works even if no pure qqq star occurs; its frequency is not presumed. A-only omission is impossible by the same p-side count and total coverage, while B-only omission is impossible because M_psi must contain A. All discrepancies are uniform O(R): changing tile/native-vertex/side-midpoint square selection affects only a fixed-width boundary band, with O(R) tiles by bounded diameter and minimum positive area. No limiting frequency or extra sparse-defect saturation is used.

## Singleton corner derives one of the exact positive families

At an actual psi star the A angle is H=120+delta or L=120-delta. Therefore either

    u+psi=240±delta,
    or v+psi=240±delta.

For the first alternative, total B angle sum u+v+c+psi480 gives v+c=240∓delta. Write v+c240-sigma delta,u+psi240+sigma delta. If sigma+, the native angles are exactly

    (240+delta-psi,120,120,240-delta-c,c,psi),

the same-slot center family. Strict mixed-angle bounds give c>60-delta,psi>60+delta. Native direction subtraction and actual closure give its defining complex phase exp(i delta)(exp(i c)-1+exp(-i psi))=-2p.

For the second alternative, write v+psi240-sigma delta,u+c240+sigma delta. If sigma+, the angles are exactly

    (240+delta-c,120,120,240-delta-psi,c,psi),

the cross-slot center family. Strict convexity gives c>60+delta,psi>60-delta, and native closure gives exp(i delta)(exp(i psi)-exp(i(psi-c))+exp(-i c))=-2p.

If sigma-, reflect/reindex B with native side map(2,1,0,5,4,3) and vertex map(3,2,1,0,5,4). This exchanges u/v and c/psi, preserves pp120/120, and converts the corresponding same or cross condition to sigma+. No reflection of A or change of delta is required. Both known positive families provide actual full-plane periodic tilings after this normalization. Common scaling and prototype congruence transfer those independent periods back. This proves necessity and sufficiency.

Equivalently the original normalized forward native geometry is parameterized by c in(90,180),c!=120,c-rho(c)<120, with p=sqrt(1+4sin²c)/2. It is tileable exactly when

    delta=|180-c-rho(c)| or delta=|2c-180-rho(c)|,
    0<delta<30.

These are respectively the same and cross alternatives above, with optional B reflection taking care of the signs. This scalar restatement is derived from actual mixed-angle sums, not numerical roots. For example c150,psi60,rho45,p1/sqrt2,delta15 belongs to the same family after B reflection.

## Scope and review obligations

This completes center pp with noncentral mixed-homogeneous qq, including either native qq order and all nongeneric intersections. It does not cover a pure120 qq slot with its other slot different from120, two noncentral pure arcs, or arbitrary B. Two central arcs force p=q by their equal unit-chain norm2 and are outside the distinct-binary scope. The unrestricted two-prototile target remains unresolved.

The exact local/algebra ledger is retained at `research/searches/two-homogeneous-center-mixed-qq-classification.py`. Dependencies are the reviewed unrestricted-hexagon ETE limit, fixed-shape boundary estimates, exact whole-AA endpoint test and independently VALID full positive same/cross center families. Fresh independent review must check native phase lifts, monotonic singleton exclusion,2c+psi native counts, species omission, whole-AA exclusion, reflection conversion and full positive theorem scope. No bounded search, positive seam primal or fixture-continuity argument is used.

The [fresh independent analytic whole-proof review](../reviews/two-homogeneous-center-mixed-qq-classification-review.md) accepts necessity and exact periodic sufficiency.
