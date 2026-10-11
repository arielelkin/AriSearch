# Forward noncentral mixed-homogeneous arcs cannot tile

Status: **VALID after fresh independent hostile review.** This is a complete negative theorem for the simultaneous forward mixed-homogeneous native ordering, including its nongeneric phase intersections. It does not cover the relative opposite ordering or an arc with two120 angles.

## Exact theorem and imported native forcing

Fix0<delta<30, distinct positive lengths p,q, the native A(delta) lengths(p,q,p,q,p,q) and directions(0,60+delta,120,180+delta,240,300+delta), and a strictly convex closed B with lengths(p,p,p,q,q,q). Write its native corners(B0,alpha,beta,B3,chi,psi). Assume

    2alpha+beta=360, 2chi+psi=360,
    alpha!=120, chi!=120.

**Theorem. The pair admits no plane tiling, even with unrestricted contacts and possible species omission.** Reflections are permitted.

Use the independently reviewed [singleton-slot forcing lemma](two-homogeneous-mixed-arcs-singleton-slot-forcing.md), its exact1/5 strengthening accepted separately by root, and the reviewed unrestricted-hexagon trivalent ETE limit. Common normalize q1. In any alleged actual ETE tiling, both AA lengths are forbidden. Every nonhomogeneous star has at most one A; it either has A+Bmixed+Bhomogeneous or two Bmixed+Bhomogeneous. Let N_A,N_B,Y_p,Y_q be square-window tile and pure pp/qq counts. Let M_alpha,M_beta,M_chi,M_psi count the respective homogeneous native slots at nonhomogeneous stars. All equations have uniform O(R) boundary discrepancies, and N_A+N_B=Omega(R²). The reviewed conclusions are

    N_B/5-O(R)<=N_A<=N_B/3+O(R),
    N_A=N_B-Y_p-Y_q+O(R),
    N_B=2Y_p+M_alpha=Y_p+M_beta+O(R),
    N_B=2Y_q+M_chi=Y_q+M_psi+O(R).

No B-only nonhomogeneous star contains beta or psi; all such M_beta/M_psi stars contain one A. In particular

    M_beta+M_psi=N_B+N_A+O(R).

Both singleton types occur at quadratic count. Moreover an actual beta-star and an actual psi-star with opposite A_H/A_L signs must exist. If no such pair existed, their two nonempty sign sets would both be the same singleton sign. All M_beta+M_psi=N_B+N_A+O(R) stars would then consume only one of the two A sign inventories, giving N_B+N_A<=3N_A+O(R), or N_A>=N_B/2-O(R), contradicting N_A<=N_B/3+O(R) and quadratic count. Choose such an opposite-sign pair. Each requires an actual A/Bmixed/singleton angle equation. If M_alpha=M_chi=O(R), the repeated-slot inventories give Y_p=Y_q=N_B/2+O(R), hence N_A=O(R), contradicting the1/5 lower bound and quadratic total. We use this as the zero-repeated-slot criterion. Every count remains valid if one species were initially omitted; the inequalities themselves rule that out.

## Exact normalization and complete four-choice reduction

Both alpha and chi lie in(90,180). The native arc norm is|1+2i sin x|²=1+4sin²x, strictly decreasing on that interval, so distinct lengths imply alpha!=chi. Apply the exact reviewed common-scale length swap and A reflection if needed: beginning B at oldside3 swaps(alpha,beta) with(chi,psi), preserving these forward equations and their noncentrality. Thus assume

    x=alpha>y=chi,
    h=rho(y)-rho(x)>0, rho(a)=arg(1+2i sin a),
    beta=360-2x, psi=360-2y,
    u=B0=y-h, v=B3=x+h.

The actual native phase and mixed angles are derived in the singleton lemma. They are not independent angle variables. Let d=x-y>0. Because beta/psi stars need A, at least one beta filler and one psi filler equation from these choices hold:

    F1=2x-y+h or F2=x-h belongs to{120-delta,120+delta};
    G1=y+h or G2=2y-x-h belongs to{120-delta,120+delta}.

There are exactly four pair choices F1/G1,F2/G2,F1/G2,F2/G1, and the selected F and G values have opposite signs relative to120. Additional simultaneous choices are permitted; the actual opposite-sign pair is sufficient for the exhaustive contradiction below. An A_H filler corresponds to F or G value120+delta, since its Bmixed+homogeneous sum is240-delta. An A_L filler corresponds to120-delta.

To test nonhomogeneous repeated slots x,y, enumerate all possibilities. Their A-star sums are u+x,v+x,u+y,v+y and must equal240±delta. Their B-only sums are2u+x,u+v+x,2v+x,2u+y,u+v+y,2v+y and must equal360. The checker retains all these repeated native mixed-slot possibilities, including mirrors. Excluding these equations excludes all M_alpha or M_chi stars; no hypothetical local configuration is promoted to existence.

## Case1: F1/G1

F1-G1=2d>0 forces F1=120+delta,G1=120-delta, hence d=delta,v120,x120-h,y120-h-delta. Both x,y are below120; u120-2h-delta<120. Thus every B-only sum with repeated slot x or y is below360. The A sums are

    u+x=240-3h-delta, v+x=240-h,
    u+y=240-3h-2delta, v+y=240-h-delta.

The only possible A repeated-slot equation would be v+x=240-delta, requiring h=delta. On90<y<x<120, -rho'(a)=(-2cos a)/(1+4sin²a)<1/4 (radian derivative; degree conversion cancels), so0<h<d/4=delta/4. Therefore no equation is possible. Both repeated-slot counts vanish, and the zero-repeated-slot criterion gives contradiction.

## Case2: F2/G2

F2-G2=2d>0 forces d=delta,u120,y120+h,x120+h+delta,v120+2h+delta. Both repeated slots exceed120, and u,v>=120; every B-only repeated-slot sum exceeds360. The A sums are

    u+x=240+h+delta, v+x=240+3h+2delta,
    u+y=240+h, v+y=240+3h+delta.

The x slot has no A star. The y slot can have an A star only if h=delta, then only A_L. If h!=delta, both repeated slots have no nonhomogeneous star, giving the usual contradiction.

If h=delta, M_alpha0, so Y_p=N_B/2+O(R) and M_beta=N_B/2+O(R). Here F1=120+4delta and F2=120+delta, so beta stars can only use A_H. G1=120+2delta and G2=120-delta, so psi stars use only A_L. The y stars also use only A_L. Therefore every A_H occurrence belongs to an M_beta star, giving3N_A=M_beta+O(R)=N_B/2+O(R), or N_A=N_B/6+O(R). This contradicts the independently reviewed N_A>=N_B/5-O(R). No positive density is assumed separately.

## Case3: F1/G2

F1-G2=3d+2h>0 forces opposite signs F1high,G2low. Their sum is x+y, so x+y240. Put z=d/2>0; then

    x120+z, y120-z, delta3z+h,
    u120-z-h, v120+z+h.

The A sums for repeated slots are240-h,240+2z+h,240-2z-h,240+h. None equals240±delta because delta3z+h. The six B-only repeated-slot residuals from360 are

    -z-2h, z, 3z+2h, -3z-2h, -z, z+2h,

all nonzero. Thus both repeated slots have no nonhomogeneous star, contradiction.

## Case4: F2/G1

Opposite signs imply x+y240, so x120+z,y120-z with0<z<30 because y>90. Exact phase subtraction gives

    tan h=sin z/(2cos²z),
    z/2<h<z.

Indeed tan h/tan z=1/(2cos z)<1, and tan h/tan(z/2)=(1+cos z)/(2cos²z)>1 because(2cos z+1)(cos z-1)<0. Both h,z are in(0,90), so tangent comparison preserves order. Therefore F2-G1=2(z-h)>0 and the targets are F2high,G1low, with delta=z-h.

The same six B-only repeated-slot residuals as case3 are nonzero. The repeated-slot A sums are again240-h,240+2z+h,240-2z-h,240+h. Only a possible h=delta equality could survive, which would require h=z/2, excluded strictly. Hence both repeated-slot counts vanish, contradiction.

## Conclusion and exact scope

All possible actual singleton beta/psi cover choices lead to a boundary contradiction or an impossible native phase. Thus an alleged unrestricted tiling cannot have its reviewed actual trivalent ETE limit, proving untileability. The simultaneous B reflection is also covered by native congruence, as are p/q exchange and omission. The relative opposite mixed ordering2alpha+beta360,chi+2psi360 has a different q-chain phase and is explicitly outside this theorem. Central arcs and pure120/noncentral combinations are likewise separate. This theorem does not resolve all both-homogeneous binary pairs or the unrestricted two-convex-tile target.

The exact arithmetic/local checker is `research/searches/two-homogeneous-forward-mixed-arcs-obstruction.py`. Fresh review must check the length swap, all four cover choices and their signs, opposite-sign selection, phase tangent comparisons and the exceptional h=delta capacity branch, H/L corner capacities, every O(R) identity, and absence of species-density assumptions. No numerical reconnaissance or solver output is a dependency.

Fresh independent complete [review](../reviews/two-homogeneous-forward-mixed-arcs-obstruction-review.md) is VALID; its no-author-import checker independently audits all four cases, exact native stars and boundary count contradictions.
