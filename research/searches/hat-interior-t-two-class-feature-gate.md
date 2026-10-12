# Genuine interior T contact in a changed hat partition

Date: 2026-10-12. Status: [independently reviewed VALID scoped exclusion](../reviews/hat-interior-t-two-class-review.md).
This covers the specified cut and parameter domain, not arbitrary hat partitions.

Keep all four strictly reflex source vertices h0,h4,h8,h11 as cut
junctions. Choose `V=(u,v)` and a point `W=h4+s(V−h4)`, `0<s<1`.
Use these four cyclic words:

* `P0=[h0,h1,h2,h3,h4,W]`, a hexagon;
* `P1=[h4,h5,h6,h7,h8,V]`, a hexagon;
* `P2=[V,h8,h9,h10,h11]`, a pentagon;
* `P3=[h0,W,V,h11,h12]`, a pentagon.

W is strictly inside the full h4–V side of P1. At W, P0 and P3
contribute two native corners summing180 degrees and P1 contributes
a flat side-interior contact. This is a genuine partial contact and
changes the old fixed P6 pentagon into a hexagon. It avoids the previously
reviewed trivalent whole-side fusion mechanism. It is an intended source
feature, not yet a theorem forcing such contacts in unrestricted tilings.

The strict convex partition cone is nonempty. Take

    b=1, V=(9/5,0), s=1/2,
    W=(12/5−sqrt3/4,−1/4).

Every nonincident vertex lies strictly in its piece's supporting
halfplanes. All six pairwise intersection areas vanish and exact internal
edge cancellation gives the source outline. The strict geometry persists
under small changes of b,u,v,s. The certificate retains the sample words
and exact coordinates. This is the local realization test required before
any congruence gate.

## A multiset cancellation forces the T point to be the midpoint

For two unmarked congruence classes, P0 must be congruent to P1 and P2
to P3, since their strict native corner counts are6 and5. Write actual
positive lengths

    L=|h4−V|, F=|h0−W|, G=|h8−V|, J=|h11−V|.

The hexagon side multisets are

    P0: {b,1,2,1,sL,F},
    P1: {b,b,1,1,G,L}.

Cancel one b and two occurrences of1 to obtain
`{2,sL,F}={b,G,L}`. The pentagon side multisets are

    P2: {G,b,b,1,J},
    P3: {F,(1−s)L,J,1,b}.

Their cancellation gives `{b,G}={(1−s)L,F}`. Substituting this into
the hexagon identity and cancelling F yields

    {2,sL}={(1−s)L,L}.

Since `0<s<1` implies `sL<L`, the right-hand L cannot equal the
left-hand sL. Therefore L=2; the remaining equality forces s=1/2.
The pentagon identity reduces to `{b,G}={1,F}`. Thus the entire
two-class metric family satisfies one of exactly two branches:

* A: `b=1, L=2, F=G`;
* B: `L=2, G=1, F=b`.

Multiset cancellation remains valid at every repeated-length coincidence;
no assumption of distinct native lengths, chirality or endpoint order
enters this reduction. It is a necessary metric test, preceding any
full polygon congruence enumeration.

## The two small exact branches fail strict convexity

Set W=(h4+V)/2. In squared lengths, the three equations of each branch
are polynomial over Q(sqrt3):

    A: b−1=0, |h4−V|²−4=0, |W|²−|h8−V|²=0;
    B: |h4−V|²−4=0, |h8−V|²−1=0, |W|²−b²=0.

Both ideals have dimension0. Solving over the exact algebraic real field
gives two real points per branch. All four have b>0, and all four violate
at least one strict supporting inequality. Signed determinants and their
minimal polynomials are retained in the certificate. The first B point
is exactly `(b,u,v)=(4sqrt3/3,3,−2sqrt3/3)`; the other is algebraic
of higher degree. Full cyclic/reflected congruences are additionally
checked but are unnecessary for exclusion: no point even satisfies the
strict geometry together with the necessary common side inventories.

Consequently this exact genuine-T compiler has no two-class convex
realization. There is no surviving fixed pair on which a monohedral or
mixed-periodic attack is needed. This excludes these words and this
straight-side T topology, not other source subdivisions or arbitrary
unmarked pairs. No unrestricted recognition, full-plane existence or
aperiodicity theorem has been obtained.

Artifacts:

* [Exact feature and small metric gate](hat-interior-t-two-class-feature-gate.py).
* [Exact certificate](../certificates/hat-interior-t-two-class-feature-gate.json).

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/searches/hat-interior-t-two-class-feature-gate.py --output /tmp/hat-interior-t-replay.json
