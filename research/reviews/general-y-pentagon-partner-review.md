# Fresh hostile review of the full Y-pentagon periodic-partner construction

**Verdict: VALID.** Root independently reviewed
[the author's construction](../lemmas/general-y-pentagon-periodic-partner.md)
on2026-10-10, after its author derived the coordinates and proof. This review
covers the entire positive closure cone, the chosen distinct partner, and
the sufficient criterion for an independently specified pair. It does not
classify all Y/Y tilings.

The fresh [formal checker](verify_general_y_partner_formal_independent.py)
imports no author code. It derives P from independent closure coordinates
L0=hL2+2khL3-kL1, L4=hL1+kL2-dL3, scales all coordinates by h>0, and
computes in a rational polynomial ring modulo h^2+k^2=1. It constructs Q
from its native edge walk, without assuming the author's placed vertices.
The asserted common endpoints and reflected side order follow exactly.

The partner parameters are strictly positive. For lambda=S+kL0/d, the two
numerators are k*(lambda-L1)+L0 and L1+d*S. Since d,h,k and every actual
P length are positive, both deltas are positive and lambda exceeds every
P side. This excludes congruence using the actual maximum length, without
angle-word indexing assumptions. For an already prescribed Q, the two
stated shared-edge equalities and Q closure instead derive those same
deltas from its actual lambda; positivity suffices for the carrier even
without the large-lambda choice.

P and Q have the claimed cyclic directions, with every turn strictly
between0 andpi, and close. Their support-height proof is valid: relative
to an edge, the remaining transverse increments have a positive initial
block and a negative final block, with total0. Each nonincident partial
sum is strictly positive. Thus the loops are globally convex and simple;
positive local turns alone are not substituted for that argument. Q's
native angles are(R,theta,R,gamma,theta), and reflection starting at q2
gives the native Y lengths(delta2,delta4,L0,lambda,L1). The case theta=120
degrees only reduces the number of different angle values, as explicitly
acknowledged; it does not invalidate the construction.

The independent checker cancels actual opposite directed edges as a
multiset. Five pairs disappear and the remaining ten native edges form
one successor cycle. Removing its straight subdivision vertices yields
exactly(v3,v4,q1,v3*,v4*,q1*). The remaining sides are precisely
x,y,z,-x,-y,-z with positive magnitudes, in strictly cyclic order.
Consequently the oriented boundary identity is genuine for every metric.
Positive convex winding numbers force dissection of the convex carrier,
including containment and absence of unintended overlap. The finite
closed union covers all boundary points as well as its interior.

All three forward cross products det(x,y),det(x,z),det(y,z) are positive:
their direction differences are2theta-pi,theta,pi-theta, all in(0,pi).
The checker verifies the symbolic carrier area and motif area equal
cross(x+y,y+z), and all three actual reversed opposite-side translations.
The two circular quotient links each contain(theta,theta,gamma), giving
one flat disk. The connected complete flat-torus cover, or equivalently
the displayed map to the lattice torus of equal area, proves degree-one
whole-plane coverage. Irrational theta introduces no rotational holonomy:
all displayed side pairings are translations and generate the stated rank2
period lattice. Right-corner partial contacts on carrier seams are allowed.

Replay passed:

    conda run --no-capture-output -n arisearch python research/reviews/verify_general_y_partner_formal_independent.py

The author's separate algebraic coordinate/overlap replay also passed both
out-of-old-family fixtures: k=2/5 and1/3, with38 complete lattice comparisons
each, strict supports, noncongruence and exact density1. These fixture
checks validate the concrete metrics; the entire cone is justified by
the formal chain identity and analytic convexity/positivity proof.

No mathematical repair or missing extension obligation was found. The
scope attacks about arbitrary preassigned partners and universal forcing
are explicitly excluded by the theorem. This is a useful periodic escape
mechanism and supplies no aperiodic pair or literature-priority claim.
