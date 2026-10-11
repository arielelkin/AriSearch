# Equal private sides in the two-angle pentagon--heptagon family

**Status:** adversarially reviewed VALID in the [fresh independent audit](../reviews/two-angle-5-7-equal-private-scaffold-review.md); exact restricted classification and universal periodic escape. This changes the private
scaffold mechanism from unique side matching to same-slot half-turns and
cross-slot glide reflections. It is not a solution of the unrestricted
aperiodic-pair problem.

## Family and result

Let alpha=4pi/7, beta=5pi/7. Let H be a genuine beta-equiangular heptagon
with counterclockwise lengths

    (L,a,L,b,c,d,e),

where L,a,b,c,d,e are positive and pairwise distinct except for the two
displayed L slots. Let P have one beta and four alpha corners, with five
distinct side lengths exactly a,b,c,d,e. The private value L does not occur
on P. Contacts, rotations and reflections are unrestricted.

**Theorem.** If this pair tiles, then up to an allowed reflection of the
whole metric data, P's clockwise length cycle is(e,a,b,d,c), its beta
corner is between b and d, and all lengths are given by

    b = (-t^2+t+4)*L/2 + (t-2)*a,
    c = (-3t^2+2t+7)*L/2 + (2t^2-t-4)*a,
    d = (-2t^2+t+5)*L + (2t^2-6)*a,
    e = (-3t^2+3t+7)*L/2 + (2t^2-2t-3)*a,             (1)

where t=2cos(pi/7), t^3-t^2-2t+1=0, 18/10<t<181/100.
The complete positive cone is

    L>0, 0<a<(t^2+3t/2+1/2)*L.                        (2)

The distinct-length hypotheses remove exactly ten interior ratios a/L,
listed with all equality pairs in the retained certificate. Every metric
in this cone, including its permitted generic subset, admits a doubly
periodic four-orbit tiling. Consequently NO pair in this equal-private
family is aperiodic. A second apparent cone with beta between d and c
forces b=e and c=d and is outside the five-distinct-side P hypothesis.

No assertion is made that every original tiling has a period. Mixed
half-turn/glide private chains have genuine orientation choices; finding
one period in every such tiling is unnecessary for the periodic escape.

## Complete local matching constraints

All native angles are strictly obtuse, so the reviewed all-obtuse theorem
makes every admitted contact a full native side. The only vertex star is
alpha+beta+beta. Alpha sectors occur only in P.

First, every P has exactly one P-P side neighbor. Any P-P side matches
the same native index because P has five distinct lengths. An alpha--alpha
side cannot match P, and reflection across a beta--alpha side creates an
alpha--alpha endpoint. Thus a P-P seam is a half-turn along a beta--alpha
side. At the unique P beta corner the third sectors cannot be two H beta
corners, and two P beta corners would require the forbidden reflected
P-P alignment. Its star is P_beta+P_alpha+H_beta. Exactly one of its two
sides is P-P and the other P-H; the remaining three alpha--alpha sides
are also P-H. This argument also excludes a P-only tiling.

An L seam can join H's side0 to side0, side2 to side2, or cross0/2.
For a same-slot match, reflection across the side produces equal external
lengths at a seam endpoint, impossible for a P alpha corner. The remaining
match is its midpoint half-turn. It prescribes a P alpha side pair(e,a)
for side0 or(a,b) for side2.

For a cross-slot match, reversed endpoint order would prescribe(a,a) at
one endpoint, so is impossible. Preserved native endpoint order is an
orientation-reversing placement; its endpoint pairs are(e,a) and(a,b).
Thus both forced unordered pairs occur at P alpha corners regardless
of all seam choices. They form a path e-a-b in P's length cycle. Up to
reversing the cycle the only possibilities are

    A=(e,a,b,c,d), B=(e,a,b,d,c).

The beta corner cannot be at e/a or a/b. Three beta positions remain
for each cycle, giving exactly six local cases.

Across a P-P side of value k, the residual H beta corner has the two
lengths preceding and following k in P's cycle. It must be an actual H
native adjacent pair. H's pairs are

    (L,a), (a,L), (L,b), (b,c), (c,d), (d,e), (e,L).

For cycle A none of the beta-incident side choices satisfies this test,
so it is untileable. For cycle B only P sides c and d can be P-P:
side c leaves(d,e), side d leaves(b,c). The cases are therefore

| P beta corner | Permitted P-P side |
|---|---|
| b/d | d only |
| d/c | c or d |
| c/e | c only |

The b/d and c/e cases are exchanged by reflecting/renumbering H through
j -> 2-j; this swaps b,e and c,d and fixes L,a. It suffices to analyze b/d.
In this case H side d cannot have a P neighbor: at P's beta endpoint the
residual P alpha corner would require(b,c) or(b,e), neither an adjacent
P pair. Thus H side5 of length d is always a same-index H-H half-turn.
The symmetric statement forces H side c in the c/e case.

## The private-chain state mechanism

Put z=exp(2pi*i/7). H's private midpoints are

    M0=L/2,
    M2=L+a*z+L*z^2/2,
    D=M2-M0=z*(L*cos(2pi/7)+a)!=0.                    (3)

Their chord therefore has direction z regardless of b,c,d,e. The
same-slot half-turns continue it straight. A cross placement mapping
native side2 to native side0 with preserved endpoint order is

    g_02(x)=z^2*conjugate(x)-L*z^2-a*z.                (4)

It is reflection in the midpoint-chord line followed by translation -D.
Its linear part S(x)=z^2*conjugate(x) fixes D, and

    g_02^2(x)=x-2D.

Thus cross seams also continue the chord straight, although (4) is a
glide reflection rather than an involution. Relative chain linear states
are I,-I,S,-S: a same-slot seam flips the along-chord sign; a cross seam
preserves it and flips the normal sign. Arbitrary mixed choices do not by
themselves prove a periodic tile chain. The local constraints above and
full metric closure, rather than a claimed finite-state pumping theorem,
resolve the aperiodic-pair avenue by supplying a periodic assembly.

## Exact closure and the whole positive cone

Write eta=exp(pi*i/7). For H the directions are eta^(2j).
For P clockwise from its beta corner, successive edge directions, after
one arbitrary rotation, are

    1, eta^-3, eta^-6, eta^-9, eta^-12.

The b/d case has P lengths(d,c,e,a,b). The two real H closure equations
and two real P closure equations have rank4 on the six real length
variables(L,a,b,c,d,e). Solving them with free L,a gives precisely (1).
These equations use real lengths without any rationality assumption.
In the d/c case P lengths(c,e,a,b,d) instead give b=e and c=d throughout
the closure kernel; this contradicts the stipulated distinct P values.
The c/e case gives the reflected version of (1).

The b coefficient is positive in L and negative in a. Its zero occurs at
r=a/L=t^2+3t/2+1/2. At the two cone rays(L,a)=(1,0) and(1,r), the remaining
lengths c,d,e are strictly positive, and L is positive. Since every
length in (1) is linear, c,d,e remain positive throughout the wedge.
Consequently all six lengths are positive exactly on (2). Positive
closed walks in these cyclic convex directions are globally strictly
convex, so no hidden area/intersection condition narrows this cone.

Coincidence ratios are the roots of the fifteen pairwise differences of
L,a,b,c,d,e. Exactly ten distinct roots lie strictly between0 and r.
The certificate lists all corresponding equality pairs, including multiple
coincidences at a single ratio. Thus its generic subset is also explicit.
For example L=1,a=11/10 gives six positive distinct values

    L=1, a=11/10,
    b=-t^2/2+8t/5-1/5,
    c=7t^2/10-t/10-9/10,
    d=t^2/5+t-8/5,
    e=7t^2/10-7t/10+1/5.

## Universal periodic escape, not a bounded experiment

Reflect and renumber H by j_new=2-j_old. Its new length order is

    H'=(L,a,L,e,d,c,b).

The reflected clockwise P, starting at beta, has lengths

    (b,a,e,c,d).

This is EXACTLY the four-orbit shared-order family in
[two-angle-5-7-metric-continuum](two-angle-5-7-metric-continuum.md), with
its four parameters(a_old,b_old,c_old,d_old)=(a,L,d,b) and its closing
P side p=d. Substituting (1) into that lemma's formulas gives the exact
identities

    H'_0=L, H'_3=e, H'_5=c, Pprivate=d.

All eight positive cone inequalities transfer from (2). The continuum's
symbolic twelve-seam/eight-link flat-torus proof therefore produces a
whole-plane four-orbit tiling for EVERY such metric. Its existence proof
allows coincident lengths; the distinct-length assumption was needed
only for that lemma's stronger every-tiling rigidity assertion. No such
rigidity is imported here.

In original labels this construction uses same-slot half-turn H-H seams
at sides0,2,5, and a P-P seam at length d. It has two independent periods.
It is a valid escape even if another assembly could use cross-slot glide
choices or encode a nonperiodic private chain. All admitted tilings must
be nonperiodic for an aperiodic pair, so this explicit periodic one kills
the whole positive metric cone.

## Reproduction, review and remaining scope

Producer: `research/searches/two-angle-5-7-equal-private-scaffold.py`.
Certificate: `research/certificates/two-angle-5-7-equal-private-scaffold.json`.
The computation has precisely six local order/beta cases, three exact
four-row closure kernels, fifteen collision comparisons, and one formal
four-parameter torus embedding. It uses exact Q(t) arithmetic, no solver,
no torus-bound increase, no random seed and no timeout extrapolation.

```text
conda run --no-capture-output -n arisearch python research/searches/two-angle-5-7-equal-private-scaffold.py
```

Default replay is nondestructive. The separate small same-author checker
`research/searches/verify_two_angle_5_7_equal_private_certificate.py`
imports no producer; it derives the six cases from permutations, constructs
closure rows directly from cyclotomic trigonometric values, and rechecks
the full kernels, all fifteen coincidence comparisons, positivity rays,
glide geometry and periodic-cone embedding. It passed its complete replay:

```text
conda run --no-capture-output -n arisearch python research/searches/verify_two_angle_5_7_equal_private_certificate.py
```

This mechanical replay is not a fresh hostile review. The independent reviewer must audit the
six-case completeness, all real closure equations, the cross-slot glide
branch, and the exact use of the continuum existence theorem with repeated
lengths. No claim about every mixed-branch tiling's periods is made.

Other repeated-side positions, more repeated private values, repeated P
lengths, a private value occurring three times, or a different angular
family remain outside this theorem. The unrestricted objective remains
unresolved. Reopening this exact family as an aperiodic route would require
invalidating the explicit universal periodic escape, not exploring longer
private-chain words.
