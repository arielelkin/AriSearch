# Pentagon 120/105 and equiangular dodecagon: complete periodic-escape family

Date: 2026-10-13. Adversarially reviewed VALID for arbitrary metrics in the stated palette.
Fresh full audit: `research/reviews/contact-pentagon-120-105-dodecagon-hostile-review.md`.
Independent native-direction reconstruction: `research/reviews/contact-pentagon-120-105-dodecagon-independent.py`.

Let P be a genuine convex pentagon with one 120-degree corner and four 105-degree corners, and Q a genuine convex dodecagon with twelve 150-degree corners. Any unrestricted tiling by the original two congruence classes forces the metric conditions below. Conversely every metric pair satisfying them admits an explicit periodic tiling. Thus this angle palette cannot realize the main aperiodicity target. Reflections, arbitrary native length coincidences, omission and partial contacts are initially allowed.

## Unrestricted native reduction

All native angles exceed90. A side-interior event would require native corner angles summing180, impossible because each is at least105. Contacts therefore match whole native sides of both tiles, without an imposed edge-to-edge rule. In units15degrees, the full-star equation is 8A+7B+10C=24. Its only nonnegative solutions are (3,0,0) and (0,2,1): PPP with three P120 corners, or PPQ with two P105 and one Q150. Neither polygon can tile alone: P105 always needs Q, and Q150 always needs P.

Index P0 at120 and P1,...,P4 at105. Write lengths of sides0,...,4 as (x,u,w,v,y). Around each P105 corner the two neighboring species are P and Q, while at P120 both are P. Following the four consecutive 105 corners forces the native neighbor word (P,Q,P,Q,P). In particular Q contacts only the two indexed P edges of lengths u,v. Q cannot have a Q neighbor because no star contains two Q150 corners.

Every P120 lies in a PPP120 star. Its two incident native bevels have lengths x,y. Every neighboring PP edge at that star must also be incident to a P120 corner on its other tile: only P120 sectors occur there. Thus equal side lengths elsewhere on P cannot provide unintended native mates. If x!=y, whole matching around the three-tile star would alternate the two bevel values on an odd cycle. Each tile contributes one x and one y leg, so the three shared edges cannot be consistently two-coloured. Hence x=y. This argument includes all other length aliases and both handednesses.

Choose edge directions -60,15,90,165,240 degrees for indexed edges0,...,4. Horizontal closure gives (u-v)cos15=0 and therefore u=v. Vertical closure gives

    w=sqrt3*x-2u*sin15.

Every Q native side is a whole contact with u or v, hence all twelve have length u. Equiangular Q is consequently the regular dodecagon. Up to common similarity the entire necessary family is u=v=1 and w>0, with x=y=(w+2sin15)/sqrt3. The explicit carrier below verifies genuine convexity throughout this family, not just at a sampled metric.

## Exact 6P/1Q periodic carrier for every w>0

Put R=1/(2sin15)=sqrt(2+sqrt3), d=2R+w. Center Q at the origin with vertices

    qi=R*(cos(i*pi/6),sin(i*pi/6)), i=0,...,11.

Set lattice periods a=(d,0), b=(d/2,sqrt3*d/2), and triangular interstice point V=(d/2,d/(2sqrt3)). One pentagon representative is

    P*=(V,q1,q0,a+q6,a+q5).

Its indexed native angles are (120,105,105,105,105), and its edge lengths are (x,1,w,1,x). The bevel identity x=d/sqrt3-R equals (w+2sin15)/sqrt3 because (2-sqrt3)R=2sin15. Use Q and the six rotations of P* through k*pi/3, k=0,...,5, at every integral lattice shift. The exact producer proves strict supporting-line convexity and signed angle cosines for every w>0 by polynomial coefficient signs in the exact field Q(R), where R satisfies R^4-4R^2+1=0 and sqrt3=R^2-2.

The native reversed-edge pairing pattern is uniform in w. The producer solves the integral lattice coordinates for every possible reversed native edge pair, without a bounded shift window, obtaining exactly one partner for each of the42 directed edges. It also proves identically

    area(Q)+6area(P*)=det(a,b)>0.

The complete boundary cancellation makes periodized indicator multiplicity distributionally constant. Its mean is one by the area identity, so there are no positive-area overlaps and coverage is complete by closed local finiteness. This proves an actual periodic plane tiling for every admissible metric in the necessary family. It does not say every original tiling is periodic, which is unnecessary to exclude a universal aperiodicity claim.

Producer: `research/searches/contact-pentagon-120-105-dodecagon-symbolic-carrier.py`. Certificate: `research/certificates/contact-pentagon-120-105-dodecagon-symbolic-carrier.json`. It imports no earlier palette or polygon helper. The exact polynomial parameter includes w=1, x=w, x=1 and every other positive length-alias specialization; no genericity assumption enters the native reduction or witness. The geometric reduction proves necessity for arbitrary metrics, rather than treating the constructed one-parameter family as an exhaustive assumption.
