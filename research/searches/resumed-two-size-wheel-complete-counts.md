# Exact decision: all negative-conjugate six-child wheel counts

Date:2026-10-13. **Status: complete640-case nonsingularity certificate; independent review [VALID](../reviews/resumed-two-size-wheel-complete-counts-review.md). The finite-domain decision below was written before execution.** No generic point,
metric or topology enumeration is authorized or implied by this test.

## Mathematical question and new invariant

Retain precisely the distinct-native-angle, unsubdivided-one-center/five-corner
wheel hypotheses in [the original wheel record](resumed-two-size-six-wheel.md).
Let parent mu P be tiled by b copies of P and d copies of lambda P, where
lambda²=mu, b+d=6, b>0, d>=0 and mu²=dmu+b. The six integer counts are
(b,d)=(6,0),(5,1),(4,2),(3,3),(2,4),(1,5). No claim is made that arbitrary
six-pentagon partitions have this wheel topology.

Necessary boundary matrix C is nonnegative and has row sums

    sum_j C_ij=t_i+t_(i+1)<=2lambda,

where t_i=1 orlambda is the corner-child scale. A positive native length
vector l with C l=mu l would give mu<=max row sum: choose an index at which
l_i is maximal and compare C_ij l_j<=C_ij l_i. Thus mu<=2lambda, equivalently
mu<=4. This new invariant prunes counts before determinant computation:

* d=4,b=2: mu=2+sqrt6>4, excluded.
* d=5,b=1: mu=(5+sqrt29)/2>5>4, excluded.
* d=0,b=6: every corner is small, so all row sums2<sqrt6=mu, excluded.
* d=1,b=5: at mostone corner is large, so all row sums<=1+lambda<mu.
  Here mu=(1+sqrt21)/2<3 and mu²=mu+5; consequently
  (mu-1)²-mu=6-2mu>0 and mu-1>0, giving mu>1+sqrt(mu).
* d=2,b=4: all480 matrices were exactly certified nonsingular in the
  [prior record](resumed-two-size-six-wheel.md), with independent review.

Only d=3,b=3 remains. It uses mu=(3+sqrt21)/2<4 andlambda=sqrt(mu),
whose minimal polynomial is f(t)=t⁴-3t²-3. Negative quadratic conjugacy
proves f irreducible as in the reviewed d=2 field argument.

## Exact new finite domain, written before execution

One central child and five corner children; exactly three of the six are
large. If the center is small, exactly3 corners arelarge, giving
C(5,3)*2^5=320 scale/reflection patterns. If the center islarge, exactly2
corners arelarge, giving C(5,2)*2^5=320 patterns. Total640, with no symmetry
reduction. Reflections swap incoming/outgoing native lengths at matching
corner indices. No angle or metric positions are enumerated.

For every case, construct M=lambda² I-C(lambda) over Q[t]/(f), using the
same explicitly documented corner equations as the prior wheel. Retain
central size, large corner indices, five reflectionbits, and four exact
integer determinant coefficients in basis1,t,t²,t³. If any determinant
vanishes, retain its kernel and separately test positive-length feasibility;
do not label singularity a geometric candidate. If all determinants are
nonzero, combine with the four analytic prunings and prior d=2 certificate
to exclude this precise wheel for every negative-conjugate six-child count.

Software:SageMath exact rational number-field arithmetic. Deterministic,
no solver, floating-point tolerance, random seed, resource timeout or metric
sweep. Root independently commissioned a hostile reviewer using a different
polynomial determinant algorithm. Pre-execution status was NOT YET RUN. The stated finite domain is now complete.

## Completed result and exact combined exclusion

All640 determinants are nonzero in Q[t]/(t⁴-3t²-3). Therefore no case has a
nonzero real native-length solution; there are no singular kernels or
positive-feasibility cases to retain. This completes d=3 independently of
coordinate closure and inner contact realizability.

**Combined theorem (specified wheel only).** No genuine convex pentagon with
five distinct native angles supports the unsubdivided-one-center/five-corner
six-piece two-size wheel at any count b+d=6, b>0, d>=0, mu²=dmu+b, lambda²=mu.
The d0,d1,d4,d5 cases fail the positive eigenvector row bound; d2 andd3 fail
their respective complete480/640 exact determinant domains. All six counts
are covered. Arbitrary real side lengths are permitted, and every corner
reflection is included. This does not prove every6-piece partition has the
stated scheme, exclude repeated-angle assignments/corner subdivisions, or
establish any unrestricted impossibility result.

Producer:[resumed_intrinsic_wheel_d3.py](resumed_intrinsic_wheel_d3.py).
Certificate:[resumed_intrinsic_wheel_d3.json](../certificates/resumed_intrinsic_wheel_d3.json).
Each of640 records gives the complete case label and four exact determinant
coefficients. No floating-point decisions or missing intermediate witnesses.

Read-only replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed_intrinsic_wheel_d3.py --check research/certificates/resumed_intrinsic_wheel_d3.json

This command passed. The earlier480-domain independently reviewed result is
linked above. The fresh reviewer has been given the complete640 certificate
for separate native-matrix reconstruction and polynomial Leibniz verification.

**Restart:** exact repeated-angle corner assignment, corner subdivision or a
different explicit dissection topology could change the obstruction. No
additional adjacent count/metric enumeration follows from this complete
wheel exclusion.

The stable combined theorem is extracted to [the lemma](../lemmas/two-size-pentagon-six-child-wheel-obstruction.md), with [fresh independent review](../reviews/resumed-two-size-wheel-complete-counts-review.md).
