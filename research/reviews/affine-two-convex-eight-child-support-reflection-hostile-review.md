# Independent hostile review of the eight-child support-reflection gate

Date: 2026-10-14. Verdict: **VALID for the specified topology and open angle slice.**
Reviewed artifact: [support-reflection gate](../searches/affine-two-convex-eight-child-support-reflection-gate.md).
Independent replay: `mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_eight_child_support_reflection_independent.py`.

## Exact claim and assumptions

The claim excludes an eight-child partition of a parent similar to P, with seven
congruent P children and one Q6, **under the prescribed central pair and sector
incidence**. The two central P children share full native side0 and are support-line
reflections. Six spokes join the other central vertices to distinct parent-side
relative interiors. The z0 reflex sector is one P and contains no parent corner;
the z1 reflex sector is one Q and contains one parent corner. Each other sector
is one P and contains one parent corner. The angles of P, indexed counterclockwise,
are (120,120+epsilon,60,120-epsilon,120), with 0<epsilon<30 degrees.

The child and parent copies may have either determinant sign. The review imposes
no uniqueness of native edge length. Positivity of all five native lengths is
required; global closure is necessary. The prescribed incidence is a hypothesis
of the scheme, not something forced by the two unmarked shapes. No existence,
substitution, second parent, or plane-tiling assertion follows from this review.

## Independent derivation and attempted counterexamples

The union boundary order is z1,z2,z3,z4,z0,z4',z3',z2'. Its z0 angle is 240,
so the outer sector angle is 120. Its z1 angle is 240+2epsilon, so its outer
sector angle is 120-2epsilon. The only P native corners equal to 120 are 0 and4.
Both adjacent contacts in the z0 sector have length y (central side4). Therefore
native corner0 requires x=y and native corner4 requires v=y. Reversing the child
or swapping the two contacts yields the same two length equalities. A P corner
cannot lie in the interior of a straight contact edge here: the sector angle is
120, rather than180. Thus no third reflex mating case is omitted.

If a nonreflex P sector contacts native edgej, its endpoints are j,j+1. The
adjacent spoke edges lead to j-1 and j+2. The remaining boundary path has vertices
j+2,j+3,j+4=j-1, and its unique parent corner is j+3 modulo5. Reversing its traversal
keeps this middle vertex. Native sides1,2,3 consequently provide parent angles
120,120,120+epsilon respectively. The Q parent corner is cyclically between the
two side2 (length w) contact sectors, regardless of a global reflection or cyclic
reindexing of the parent. This indexing is the relevant topological assumption;
the four nonreflex P corners cannot be reordered arbitrarily.

From independently summing the directions 0,60-epsilon,180-epsilon,240,300,
closure is

    x+u*cos(60-epsilon)-w*cos(epsilon)-v/2+y/2 = 0,
    u*sin(60-epsilon)+w*sin(epsilon)-sqrt(3)*(v+y)/2 = 0.

For x=y=1 these give the stated w and v formulas. Since u>0 and
0<cos(30-epsilon)<=1, w>sqrt(3)>1. If w differs from v, its only possible native
matches are sides1 or2, allowing u=w. They both give parent120. The two neighbors
of Q are then120, whereas no position in the original angle word has both neighbors
120. This argument allows every native side as a match on either v sector, so
any additional v alias is harmless.

If w=v, none of sides0 or4 can match this common length. Each of the four outer
P parent corners is therefore120 or120+epsilon, including the alias u=w=v. Both
60 and120-epsilon are distinct and absent from these four corners. One Q corner
cannot provide both. The endpoints epsilon=0 and30, where some distinctions would
fail, are explicitly outside the claim.

For v=y=1 closure instead gives

    u=2*cos(epsilon)-2*x*sin(epsilon)/sqrt(3),
    w=2*x*sin(60-epsilon)/sqrt(3)+2*cos(60-epsilon).

Positive u gives 0<x<sqrt(3)*cot(epsilon). The affine function w-x is positive at
both endpoints of this interval: its values are 2*cos(60-epsilon) and
sqrt(3)*(1-cos(epsilon))/sin(epsilon). Hence w>x. Also
w>2*cos(60-epsilon)>1, so w cannot equal x,v,y. Sides1 and2 again exhaust its
possible native matches, including u=w. This is the same neighbor obstruction.
The overlap of the two reflex cases x=y=v is already covered by either argument.

## Exact executable verification

The independent checker imports no author code. It works in the exact field
Q(sqrt(3)), with positive sqrt(3) embedded in the real algebraic field, and an
exact multivariate rational-function field. It parametrizes

    tan(epsilon/2)=(2-sqrt(3))*T/(1+T), T>0,
    u=U>0 in case A,
    x=sqrt(3)*cot(epsilon)*R/(1+R), R>0 in case B.

These substitutions cover the entire relevant open domains. Strict inequalities
are checked by exact nonnegative numerator and denominator coefficients after
substitution; a nonzero such polynomial is strictly positive when all variables
are positive. The checker also verifies closure and both affine endpoint
identities. It permits a superset of geometric native-edge mates and exhausts
400 ordinary parent-angle words and324 w=v alias words against every cyclic shift
and reversal of the original angle word. There is no numeric sampling, solver,
random seed, timeout, or retained numerical certificate. This finite verification
supports the written continuum proof and does not claim that the topology is
forced by unrestricted tilings.

## Defect, repair, and remaining uncertainty

The original description called the orientation preserving full-edge mate a
midpoint halfturn even for a different matching native edge. That is only true
when source and host use the same directed native edge. A different native index
can require another rotation. The description now specifies both endpoint
assignments and determinant signs and retains all opposite-side placements.
The exclusion already allowed every native index compatible with length, so this
wording defect neither adds a mathematical hypothesis nor changes its proof.
The root independently checked this descriptive repair under protocol8.2;
see the [checkpoint audit](checkpoint-diff-audit-2026-10-14.md).

No unresolved defect was found in the analytic gate itself. The unknown broader
question is whether a different angle word or a different actual parent incidence
can provide a useful two-tile construction. That is outside the reviewed claim
and does not justify restarting a numerical search in this excluded slice.
