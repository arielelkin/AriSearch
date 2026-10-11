# Oppositely ordered mixed homogeneous arcs: off-curve obstruction

Status: **VALID after fresh independent analytic hostile review.** This manuscript uses the exact phase/count lemma in `two-homogeneous-opposite-mixed-arcs-phase.md`, itself freshly independently VALID. No exceptional-curve tilability classification is claimed.

## Statement and actual-tiling reduction

Take exactly that lemma's domain:0<delta<30, distinct positive p,q, alternating threefold A(delta), strictly convex two-run B with angles(u,alpha,360-2alpha,v,360-2eta,eta),90<alpha,eta<180 and neither repeated angle120. Set u=rho(alpha)+rho(eta),v=alpha+eta-u. If

    u!=alpha and u!=eta,

then the two polygons cannot tile the plane, including unrestricted contacts, reflections or omission of a species. Consequently any tileable pair in this singly reversed mixed-homogeneous branch must lie on one of the two explicitly parametrized exceptional curves of the phase lemma. This is not a positive result on those curves.

Suppose an unrestricted tiling exists. The reviewed limit supplies an actual trivalent ETE tiling. In it AA seams are impossible, the singleton beta and chi slots must occur in A/Bmixed/homogeneous stars, both species have quadratic counts, and

    N_B/5-O(R)<=N_A<=N_B/3+O(R).

The opposite-sign singleton cover argument forces u120, v120 or alpha+eta240. We eliminate every point of those three loci by actual native-corner incidence, retaining repeated slots and mirror states. Put H120+delta,L120-delta, beta360-2alpha,chi360-2eta. For any homogeneous corner g, its B-only nonpure residuals are2u+g-360,u+v+g-360,2v+g-360. Its A covers require one of360-u-g,360-v-g to equal H or L.

## Locus alpha+eta=240

The equations and counts are symmetric in the two repeated homogeneous slots, so assume alpha=120+x,eta=120-x,0<x<30. Put

    epsilon=120-rho(120+x)-rho(120-x),
    u=120-epsilon, v=120+epsilon.

Strict concavity of rho gives epsilon>0. The function epsilon(x) is strictly convex, epsilon(0)=0, and

    epsilon(30)=120-rho(150)-rho(90)=75-atan(2)<15,

because rho(150)=45 and atan(2)>60. Hence the chord bound gives0<epsilon<x/2 for0<x<30. This also shows u is strictly between eta and alpha, so this locus does not intersect either exceptional curve.

The B-only nonpure residuals for repeated alpha are(x-2epsilon,x,x+2epsilon); for repeated eta they are(-x-2epsilon,-x,-x+2epsilon). None is zero. The possible A-cover differences from120 for repeated alpha/eta have absolute values

    x-epsilon or x+epsilon.

The beta/chi singleton covers instead require

    delta=2x-epsilon or2x+epsilon.

These sets are disjoint since x+epsilon<2x-epsilon. Thus neither repeated native slot can occur at any nonpure star: it cannot have B-only sectors and cannot have an A sector. Their inventories force Yp=N_B/2+O(R),Yq=N_B/2+O(R), then N_A=O(R), contrary to the quadratic lower bound. All points on this locus are excluded.

## Loci u=120 and v=120

First determine the order of the repeated angles using the actual nonlinear phase, rather than assuming a linear envelope. For u120, strict decrease of rho forces alpha,eta to lie on opposite sides of120, since alpha!=eta and rho(120)=60. For v120 the same follows from strict increase of f=x-rho(x), with f(120)=60. Rename the repeated slot with the larger angle as alpha for the following symmetric inventory; write

    alpha=120+x, eta=120-y, x>0,y>0.

This is a permutation of the algebraic corner-count ledger, not an assertion that the two native shapes are congruent under a relabeling. The already established opposite-sign singleton covers force delta=x+y<30, so0<x,y<30 and both120+x,120-x lie in the derivative interval(90,180). On u120, strict concavity gives rho(120+x)+rho(120-x)<120, so equality rho(alpha)+rho(eta)=120 forces y>x. On v120, strict convexity gives f(120+x)+f(120-x)>120, so equality f(alpha)+f(eta)=120 likewise forces y>x.

The beta slot belonging to larger repeated alpha has only an H cover; the chi slot belonging to smaller repeated eta has only an L cover. Indeed their form-minus120 lists, up to interchange of mixed slots u,v, are

    beta: (2x, x+y), chi:(-2y,-x-y).

Since0<x<y, only±(x+y) qualify. The repeated alpha A-cover form-minus120 values are(-x,y-2x), neither equal±(x+y), so it has no A cover. Repeated eta's values are(y,2y-x), which qualify only when y=2x, and then its cover is H. Its B-only residuals, up to interchange, are

    -y, x-2y, 2x-3y,

all strictly negative because y>x. Thus repeated eta cannot occur in a B-only nonpure star at any point of either locus.

If y!=2x, repeated eta has no nonpure star at all, so Yq=N_B/2+O(R). All A H corners then occur at beta singleton stars and all A L corners at chi singleton stars: repeated alpha has no A cover, repeated eta has none, and every A star has one B homogeneous slot. Therefore

    N_B-Yp=3N_A+O(R), N_B-Yq=3N_A+O(R),

which gives Yp=Yq+O(R). Both pure counts are N_B/2+O(R), so N_A=O(R), contradicting the quadratic lower bound. (No assumption that the pure counts or frequencies converge is used.)

If y=2x, every A L corner still belongs to chi and every A H corner belongs to beta or repeated eta. These exact native incidences give

    N_B-Yq=3N_A+O(R),
    (N_B-Yp)+(N_B-2Yq)=3N_A+O(R),
    N_A=N_B-Yp-Yq+O(R).

Eliminating N_A yields2Yp+Yq=N_B+O(R),3Yp+2Yq=2N_B+O(R), hence Yp=O(R),Yq=N_B+O(R). This violates Yq<=N_B/2+O(R) and quadratic N_B. Both loci are excluded, including their possible overlap and all isolated metric resonances.

## Scope and evidence

The proof does not claim a fixed quotient carrier is necessary, does not infer a pointwise tiling property from a frequency equality, and does not use a bounded failed search. It uses actual trivalent ETE stars after the reviewed unrestricted-contact limit and boundary O(R) inventories. Mirror orientations change ray order but preserve every exhaustive homogeneous/mixed angle combination used above.

The separate phase lemma contains all exact curve branches, denominator cases and convexity bounds. Those two curves remain genuine unresolved two-species possibilities: their local B-only singleton patterns invalidate this proof's forced-singleton premise. Neither existence nor global exclusion there follows from the present result.

An exact author ledger checks the derivatives, twelve nonpure residuals, all A-cover formulas, both locus tables, homogeneous resonance intersections, binary cyclic label patterns and count eliminations: `research/searches/two-homogeneous-opposite-mixed-arcs-phase.py`. It is not an independent review.

Fresh independent whole-proof analytic [review](../reviews/two-homogeneous-opposite-mixed-arcs-off-curve-obstruction-review.md) is VALID.
