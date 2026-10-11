# Fresh hostile review of the equal-private (5,7) scaffold

**Verdict: VALID.** Root reviewed the full
[equal-private theorem](../lemmas/two-angle-5-7-equal-private-scaffold.md)
on2026-10-10 and did not derive its local cases, closure formulas or periodic
embedding. This review concerns periodic-witness existence throughout the
stated family, not periodicity of every mixed-glide tiling.

The all-obtuse dependency applies to all angles. The only native sector
sum is alpha+beta+beta. Internally distinct P values fix each P-P native
side index; same-index reflections repeat alpha at the other endpoint,
so every possible P-P side is a beta--alpha midpoint half-turn. At the
unique P beta corner another P supplies alpha, while a second P beta
would require the excluded reflected seam. Thus every P has exactly one
P-P neighbor and four H neighbors. This is pointwise and does not invoke
an average-frequency rule.

I checked both endpoint assignments for H's two L slots. Same-slot
reflection leaves equal external rays and would force an equal-sided
P alpha corner. Cross-slot orientation-preserving endpoint reversal does
the same at one endpoint via the two a rays. The remaining cross-slot
reflection prescribes exactly(e,a) and(a,b). Hence the common forced
P length path e-a-b is correct, including arbitrary mixed native choices.
With the other two distinct P symbols c,d there are precisely two cyclic
orders up to reversal and three beta positions per order. Comparing each
beta-incident side's other two P symbols with the actual H adjacent pairs
leaves no P-P option in order A and the stated d/c options in order B.
The six-case reduction is exhaustive for its exact declared hypotheses.

The clockwise P directions starting at beta are successive powers
eta^0,eta^-3,eta^-6,eta^-9,eta^-12; the last exterior turn is2pi/7,
so no omitted rotation or angle indexing assumption enters closure.
The four real closure rows have rank4. In the middle beta position the
full kernel forces b=e and c=d; this excludes the case by internal
P distinctness, without treating an empty search as a theorem. The other
two kernels are exchanged by the actual reflection/renumbering. The
surviving formulas are linear in L,a; evaluation on both boundary rays
shows c,d,e positive, while the b zero gives exactly the stated upper
bound. Thus the complete strict positive cone, and not only an interior
fixture, has been established. Strict cyclic direction order with positive
closure makes both polygons globally convex. Fifteen value comparisons
yield the declared ten interior coincidence ratios.

The periodic embedding is exact: new H indices j_new=2-j_old give
(L,a,L,e,d,c,b), and reflected clockwise P from beta is(b,a,e,c,d).
Substitution into the separately twice-reviewed four-dimensional continuum
with parameters(a,L,d,b) gives the declared native walks and closing P
side d. That continuum's existence proof explicitly allows coincident
numerical values. Its distinct-length hypotheses belong to its stronger
every-tiling assertion and are not imported here. All its positivity
inequalities hold for every metric in the new cone, so its twelve actual
seams, eight circular links and degree-one flat-torus proof give an
infinite periodic tiling using the actual shapes for the entire cone.
No finite-state pumping or general mixed-chain period is assumed.

I separately checked the glide map: with z=exp(2pi*i/7),
g(x)=z^2 conjugate(x)-L z^2-a z has square translation
-L(1+z^2)-2a z=-2(M2-M0), and its linear reflection fixes the
midpoint chord. This establishes the local holonomy statement. It does
not prove a period for arbitrary mixed chains, which the theorem carefully
does not claim.

The no-producer-import exact certificate checker was inspected and replayed:

    conda run --no-capture-output -n arisearch python research/searches/verify_two_angle_5_7_equal_private_certificate.py

It passed all six local cases, three full closure kernels, full cone and
all ten collision ratios, glide geometry and periodic embedding. Its
author is the theorem author; its mechanical independence is not counted
as a second human/agent review. The present hostile review independently
checks the argument and its use of the previously reviewed continuum.

No defect or unresolved obligation remains in this restricted result.
Other repeat positions, repeated P lengths or three occurrences of L
are outside it. No arbitrary-pair or universal-aperiodicity result follows.
