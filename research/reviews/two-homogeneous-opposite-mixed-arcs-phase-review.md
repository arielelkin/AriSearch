# Fresh analytic review: opposite mixed homogeneous arcs

**Verdict: VALID for the exact native phase, exceptional-curve parametrization and necessary off-curve incidence statements.**

Fresh reviewer: branching_hexagons. Independently reconstructed the actual [phase lemma](../lemmas/two-homogeneous-opposite-mixed-arcs-phase.md), rather than importing the forward-order phase or trusting the producer. The author ledger is retained evidence only; this analytic review does not depend on executing it. The separate off-curve obstruction receives its own review.

## Raw native geometry

With pp repeated slot alpha and qq repeated slot eta, the p directions are0,180-alpha,alpha and sum P_alpha=1+2i sin alpha. The q directions relative to first side phi are0,2eta-180,eta. Their sum is exp(i(phi+eta))(1-2i sin eta), exactly exp(i(phi+eta))*conjugate(P_eta), not the forward mixed arc sum. Thus positive closure forces p/q=|P_eta|/|P_alpha| and phi=180+rho(alpha)+rho(eta)-eta. Actual Bmixed angles are u=rho(alpha)+rho(eta),v=alpha+eta-u.

Both rho values are strictly between0 andatan2. Hence0<u<2atan2<180; phi>0 and phi+eta180+u<360. The mixed angle v is positive because alpha+eta>180>u, and its sole additional strict condition is v<180. The other four angles and turns are strict on90<alpha,eta<180. Closure with one ordered strict revolution gives all strict supporting lines by the positive-then-negative normal projection argument. Conversely every closed strictly convex native geometry on these exact resonance equations must have this unique lift: adding360 to phi would violate its actual side direction range. No linear-angle-envelope phase is imported.

Differentiating rho=atan(2sin x) independently gives rho'=2cos x/(1+4sin²x) and rho''=-2sin x*(5+4cos²x)/(1+4sin²x)². Both signs are strict on(90,180). Thus rho decreases and is strictly concave, while f=x-rho increases and is strictly convex. The positive norm|P_x|²=1+4sin²x is strictly decreasing there, so distinct lengths are equivalent to alpha!=eta.

## Complete singleton exceptional curves

A B-only nonhomogeneous star has two Bmixed corners and one homogeneous corner. Retaining all repetitions from u,v gives beta residuals2(u-alpha),eta-alpha,2(eta-u), and chi residuals2(u-eta),alpha-eta,2(alpha-u). With distinct alpha,eta these vanish only at ualpha or ueta. Each equality permits the stated pair of binary angle patterns; this is local compatibility only, not global existence.

For ualpha, the independently expanded imaginary part of exp(-i alpha)*P_alpha*P_eta is sin(alpha)(2cos(alpha)-1)+(2cos(alpha)+4sin²alpha)*sin eta. With t=tan(alpha/2)>1, its solution is sin eta=N/D, N=t(3t²-1), D1+8t²-t⁴. At D0 the second coefficient vanishes while the first is strictly negative, so no solution is lost. N>0;0<sin eta<1 is exactly D>N, equivalent to F=t⁴+3t³-8t²-t-1<0.

F''=12t²+18t-16>0 on t>1; F'(1)-4 and F(1)-6 show one minimum followed by strict increase to infinity. Consequently exactly one root t0 lies above1. F(sqrt3)=8sqrt3-16<0,F(2)5 bound it strictly between sqrt3 and2. Thus1<t<t0 is exactly the complete allowed branch; D>N>0 throughout, and eta180-arcsin(N/D) is the unique angle in(90,180). Both u and alpha lie in(0,180), so vanishing imaginary part cannot select an antipodal ray. On the curve veta automatically gives strict convexity. Equality alphaeta would imply2rho(alpha)=alpha and hence t²3, giving only the excluded120 center. An individually centered arc likewise forces this point using strict rho/f monotonicity. The symmetric ueta curve is complete after swapping the repeated variables. Pole, positive-unit phase, inverse-sine branch, curve crossing and endpoint exclusions are all accounted for.

## Actual star counts and opposite-sign cover reduction

Noncentral mixed homogeneous arcs have neither native120 nor paired120±2delta angles. The exact two-ended AA test therefore excludes both AA lengths. Any star with A has exactly one A, one Bmixed and one Bhomogeneous. The binary three-ray ledger gives zero or two mixed corners, so6N_A<=2N_B+O(R). Each pure arc has only its stated mixed multiset; the other homogeneous planes intersect it only at its excluded center. Native inventories give Yp,Yq<=N_B/2+O(R) and N_A=N_B-Yp-Yq+O(R).

Off both exceptional curves, singleton beta/chi nonpure stars contain A. Their sum is N_B+N_A+O(R), yielding N_A>=N_B/5-O(R). Together with the upper bound and total quadratic coverage, both species and both singleton inventories are quadratic. If their actual A-sign sets admitted no opposite-sign pair, both would be the same single H or L sign, requiring N_B+N_A<=3N_A+O(R), incompatible with the upper bound. Thus an actual opposite-sign pair exists, not merely hypothetical independent local choices.

The four pair sums of their cover forms are2v,alpha+eta,alpha+eta,2u; adding H+L240 therefore forces v120,alpha+eta240 oru120. On the sum240 locus the stated delta alternatives follow directly. On u/v120 one must exclude intersections before assigning delta|alpha-eta|: if two of these loci intersect, alpha+eta240 and u=v120. With alpha!=eta, write alpha120+x,eta120-x,0<|x|<30. Strict concavity gives u<120 and strict convexity gives v>120, a contradiction. Thus the actual noncentral metric domain has no such intersections, and the selected opposite-cover pair on each120 locus is necessarily its corresponding pair, giving delta|alpha-eta|. This explicit phase argument fills a compressed explanatory step without changing the theorem.

Uniform O(R) errors follow from a fixed-width boundary band, finite diameters and positive minimum tile area, with bounded native incidence per tile. Omission of a species is permitted in the imported actual trivalent ETE limit and handled by the inequalities, not hidden density assumptions. The exceptional curves are exempt from forced-singleton and lower-density claims exactly as stated.

No unresolved defect remains in the phase/curve/count result. The paragraph invoking an already reviewed monohexagonal side inventory is ancillary and is not needed in this review or in the off-curve proof; its validity retains its separately named imported review. Neither curve existence nor a global two-species obstruction on the curves follows here. The unrestricted target remains open.
