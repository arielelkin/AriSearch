# Oppositely ordered noncentral mixed homogeneous arcs cannot tile

Status: **VALID after fresh independent whole-proof hostile review.** This combines independently reviewed exact phase/count and off-curve obstruction with actual-star elimination of both exceptional curves; see [the fresh complete audit](../reviews/two-homogeneous-opposite-mixed-arcs-full-obstruction-review.md). No finite failed search or local-cover sufficiency is used.

## Exact theorem

Fix0<delta<30, distinct positive p,q and the strictly convex threefold A(delta) with native lengths(p,q,p,q,p,q), corners H120+delta,L120-delta alternating. Let B be strictly convex closed, native lengths(p,p,p,q,q,q), angles

    (u,alpha,beta,v,chi,eta),
    2alpha+beta=360, chi+2eta=360,
    alpha!=120,eta!=120.

Then the pair admits no plane tiling, including reflections, unrestricted contacts and omission of a species. This is precisely the relative opposite ordering of two noncentral mixed homogeneous arcs; center arcs and pure3-copy homogeneous arcs are outside its scope.

The exact geometry has90<alpha,eta<180,beta360-2alpha,chi360-2eta and

    u=rho(alpha)+rho(eta), v=alpha+eta-u,
    rho(x)=arg(1+2i sin x),
    p/q=sqrt(1+4sin²eta)/sqrt(1+4sin²alpha).

The exact phase/count manuscript `two-homogeneous-opposite-mixed-arcs-phase.md` proves this, both exceptional-curve parametrizations and pole handling, and AA exclusion. Its companion `two-homogeneous-opposite-mixed-arcs-off-curve-obstruction.md` proves all pairs off ualpha or ueta untileable, by actual ETE native-corner counts. They are explicit independently VALID dependencies: [phase review](../reviews/two-homogeneous-opposite-mixed-arcs-phase-review.md) and [off-curve review](../reviews/two-homogeneous-opposite-mixed-arcs-off-curve-obstruction-review.md).

## Reduction to one curve with one A present

Suppose a tiling exists. Use the reviewed fixed-hexagon defect-free limit to obtain an actual trivalent ETE tiling. No B-only tiling is possible: the reviewed complete monohexagonal classification excludes every cyclic/reflected distinct binary side wordpppqqq (`branching-hexagon-two-run-resonance-inventory.md`). Thus at least one A appears in this actual limit. Both AA seam lengths are excluded by the noncentral mixed homogeneous arcs, so at each A corner the other sectors are one B mixed and one B homogeneous corner. In particular both H and L must have such covers.

The off-curve theorem reduces the geometry to ualpha or ueta. The native operation reflecting B and displaying old corners(0,5,4,3,2,1), old sides(5,4,3,2,1,0), gives side word(q,q,q,p,p,p) and angles(u,eta,chi,v,beta,alpha). Exchanging length names thus swaps alpha,eta while preserving the opposite relative ordering and u,v. For A the exact reviewed length-swap reflection displays old sides(1,0,5,4,3,2), restoring the same delta and H-even indexing after rotation. Therefore assume ualpha. This is a genuine admissible prototile congruence/normalization, not a new shape or an inferred native symmetry.

Here rho(eta)=alpha-rho(alpha)=f(alpha), and f strictly increases with f(120)=rho(120)=60. Thus alpha and eta lie on opposite sides of120. A centered slot would force both centered, already excluded. Write their positive deviations as x,y; then y>x as follows. If alpha120-x,0<x<30, the phase value at eta120+x is120-epsilon with0<epsilon<x/2 by the strict-concavity chord argument in the off-curve proof. It exceeds the desired alpha120-x. Since rho decreases, actual eta exceeds120+x. If alpha120+x, then alpha=u<2atan(2)<150, so0<x<30. At eta120-x the phase is120-epsilon<120<alpha; to increase it toalpha requires eta below120-x. Thus in either case the eta deviation y is greater than x.

## All H/L cover equations on the curve

For each homogeneous B corner g, the only A cover angles are360-u-g and360-v-g. With ualpha,veta, the eight values, ordered by g=alpha,beta,chi,eta and mixed slotu/v, are

    360-2alpha, 360-alpha-eta;
    alpha, 2alpha-eta;
    2eta-alpha, eta;
    360-alpha-eta, 360-2eta.

For alpha120-x,eta120+y,y>x>0, their offsets from120 are

    (2x,x-y), (-x,-2x-y), (x+2y,y), (x-y,-2y).

Their positive magnitudes are2x,x+2y,y and negative magnitudes arey-x,x,2x+y,2y. Exhaustively equating one from each list, with x>0,y>x, leaves onlyy=3x,delta=2x. For alpha120+x,eta120-y, the offsets are

    (-2x,y-x), (x,2x+y), (-x-2y,-y), (y-x,2y),

and the same exhaustive comparison again leaves onlyy=3x,delta=2x. This retains every native homogeneous slot, repeated mixed slot, either A sign and arbitrary mirrors. It uses existence of a single A tile with both signs, not an assumed positive A frequency.

The second case cannot satisfy the metric phase. Define

    g(x)=rho(120+x)+rho(120-3x)-120-x.

Here0<x<10 since eta>90. Correct differentiation givesrho''<0 everywhere in this interval. Thus g is strictly concave, g(0)=0,g'(0)=-1/2, and g(x)<0 for everyx>0. It cannot be the curve equationg0.

Every remaining possible geometry therefore has

    alpha=u=120-x, eta=v=120+3x,
    beta=120+2x, chi=120-6x, delta=2x, 0<x<15,
    rho(120-x)+rho(120+3x)=120-x.

The nonlinear phase equality is still mandatory. It is not relaxed to infer existence. The following native-corner contradiction holds at every nonzero x on the whole displayed angle line, so neither solving the phase root nor computing algebraic polygon coordinates is needed for untileability.

## Complete actual native-star inventory and contradiction

All six B and all A angles now have the form120+kx. A trivalent angle sum is360+Kx. Sincex>0, it equals360 if and only ifK=0; there are no rational-angle or isolated-resonance exceptions. Rebuilding binary cyclic ray labels and both native reflections gives exactly the following seven angle/type multisets:

    pure pp: (alpha,alpha,beta);
    pure qq: (chi,eta,eta);
    B-only mixed: (u,u,beta), (v,v,chi);
    with A_H: (H,u,alpha);
    with A_L: (L,v,alpha), (L,u,eta).

Here u,alpha are distinct native slots even though their angles coincide, as arev,eta. The lists do not conflate their incidences. Native corner repetitions are allowed across tile occurrences. All other triples fail either the actual angle coefficient equation or the cyclic binary length condition. AA impossibility also follows directly from this exact list.

Let h,t,l denote counts of(H,u,alpha),(L,v,alpha),(L,u,eta), respectively. Let Zbeta count(u,u,beta), and Yp the pure pp stars. Square-window inventories have uniformO(R) errors. A_H and A_L counts, native ppalpha, native ppbeta and the distinct native Bmixedu counts give

    h=3N_A+O(R), t+l=3N_A+O(R),
    2Yp+h+t=N_B+O(R),
    Yp+Zbeta=N_B+O(R),
    h+l+2Zbeta=N_B+O(R).

Substituteh3N_A,l3N_A-t,ZbetaN_B-Yp. The ppalpha equation givest=N_B-2Yp-3N_A+O(R); the Bmixedu equation givest=N_B-2Yp+6N_A+O(R). Subtraction yields

    9N_A=O(R).

This is a global contradiction, rather than merely zero allowed asymptotic frequency. The imported convex monohex classification says B alone has no admitted tiling. The reviewed uniform-occurrence lemma `two-type-uniform-density.md`, applied with S={B}, therefore givesN_A>=cR² for every admitted pair tiling, with c>0 depending only on the two fixed shapes. It applies to this actual ETE limit and allows all isometries and arbitrary contacts. Equivalently one could extract an A-free admitted limit fromN_A=O(R), which would tile by B alone. No limiting frequency or ergodic hypothesis is used.

## Dependencies, computation and limits

Exact author ledger: `research/searches/two-homogeneous-opposite-mixed-arcs-full-obstruction.py`; retained report under the corresponding certificate name. The ledger reconstructs all oriented native stars from raw corners and binary radial labels, checks both cover-offset lists and every potential positive/negative equality, native length-swap indexing, the strict-concavity derivative/sign at zero, the complete seven-type inventory, and9N_A elimination. It has no solver and cannot turn a local angle cover into a tiling. Normal replay is read-only; explicit--output retains a report.

The candidate count cancellation was proposed by root and independently reconstructed here; consequently root's own algebra check is not by itself a fresh review of this full theorem. The [fresh independent whole-proof review](../reviews/two-homogeneous-opposite-mixed-arcs-full-obstruction-review.md) checks the two prior dependencies, curve cover reductions, actual species occurrence/positive-density use, mirrored native-slot inventory and all boundary errors. Its no-author-import checker is `research/reviews/verify_two_homogeneous_opposite_full_independent.py`.

This completes one both-homogeneous relative-order branch only. The unrestricted two-prototile target, central homogeneous arcs and other both-homogeneous resonance categories remain unresolved.
