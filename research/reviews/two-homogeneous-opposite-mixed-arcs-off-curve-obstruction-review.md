# Fresh analytic review: opposite mixed arcs off their singleton curves

**Verdict: VALID for the exact off-curve domain.**

Fresh reviewer: branching_hexagons. Independently checked the actual [off-curve theorem](../lemmas/two-homogeneous-opposite-mixed-arcs-off-curve-obstruction.md) and reconstructed its local angle inventories and count eliminations. The [phase review](two-homogeneous-opposite-mixed-arcs-phase-review.md) establishes its nonlinear geometry, exceptional curves, actual AA exclusions, O(R) counts and opposite-sign singleton cover premise. No solver or author-computation answer is assumed.

## Sum240 locus

The count and phase formulas are symmetric under permuting the two repeated homogeneous roles and their singleton inventories; this is an algebraic relabeling, not an assertion of native polygon congruence. Distinct lengths give alpha!=eta. Thus write the larger repeated angle120+x and the smaller120-x,0<x<30. Strict concavity yields epsilon120-rho(120+x)-rho(120-x)>0. Its second derivative is positive, so strict convexity and epsilon0=0 bound it above its endpoint chord. At x30, epsilon75-atan2<15 because atan2>60, so0<epsilon<x/2.

The Bmixed values are120-epsilon,120+epsilon. Independent substitution gives repeated larger-slot residuals from360 x-2epsilon,x,x+2epsilon, all positive, and smaller-slot residuals-x-2epsilon,-x,-x+2epsilon, all negative. Every repeated-slot A cover needs delta x±epsilon, while singleton opposite-sign covers require delta2x±epsilon. These sets are disjoint because x+epsilon<2x-epsilon. Thus neither repeated slot has any nonpure star. Native inventories force both pure counts N_B/2+O(R), then N_A=O(R), contrary to the off-curve lower bound and total quadratic coverage. The locus cannot meet a singleton exceptional curve since u lies strictly between the two repeated angles.

## The120 mixed-angle loci

At u120, rho monotonicity makes the repeated angles lie on opposite sides of120. At v120, f monotonicity does the same. None of these actual loci intersects another cover locus in the distinct noncentral domain: intersection would force alpha+eta240 and u=v120, contradicting strict rho concavity. Therefore the selected cover pair gives delta=|alpha-eta|. Write larger120+x,smaller120-y with x,y>0. Then delta=x+y<30 ensures the comparison angles120±x remain in(90,180). Strict concavity at u120, or strict f convexity at v120, forces y>x.

Fresh substitution, permitting interchange of the two Bmixed slots, gives singleton cover deviations larger(2x,x+y),smaller(-2y,-x-y). Only the second entry in each qualifies for ±delta because x!=y; hence larger singleton uses H and smaller singleton uses L. The larger repeated slot has A-cover deviations-x,y-2x, neither qualifying. The smaller repeated slot has y,2y-x, qualifying only at y2x and then only H. Its B-only residuals-y,x-2y,2x-3y are all strictly negative. Every orientation/mixed native-slot repetition is included in these inventories.

For y!=2x, the smaller repeated slot has no nonpure occurrence, forcing its pure count N_B/2+O(R). Since no repeated slot has an A cover, all H and L corners use their respective singleton counts. Equality of A's H/L inventories gives equality of the two pure counts up to O(R), hence both N_B/2+O(R) and N_A=O(R), contradiction. B-only larger repeated stars, even where locally allowed, do not evade these identities.

At y2x, all L corners still use the smaller singleton; H corners use the larger singleton or smaller repeated slot. The independent equations are N_B-Yq=3N_A+O(R),2N_B-Yp-2Yq=3N_A+O(R), and N_A=N_B-Yp-Yq+O(R). Eliminating N_A yields2Yp+Yq=N_B+O(R),3Yp+2Yq=2N_B+O(R); their exact solution is Yp=O(R),Yq=N_B+O(R), contradicting Yq<=N_B/2+O(R) and quadratic N_B. This treats the nongeneric A-cover intersection explicitly. Interchanging the original pp/qq roles simply permutes the inventory names; no geometry symmetry is assumed.

All three necessary cover loci are excluded. The proof consequently establishes untileability outside ualpha and ueta in the precise singly reversed mixed-homogeneous family, with unrestricted contacts via the actual ETE limit and possible species omission handled by the off-curve count bounds. Native mirror order does not create a missing angle multiset. Neither curve is excluded or claimed tileable by this proof. No bounded absence, local-to-global extension, limiting frequency or monohedral classification is used. No unresolved defect remains; the explicit no-locus-intersection explanation above clarifies a compressed transition in the manuscript.
