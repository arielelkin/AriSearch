# Forced neighboring-Q obstruction for the exact P5/Q14 candidate

Date: 2026-10-14. Status: **Proved, certified and independently hostile-reviewed VALID**
([fresh review and independent native-cycle reconstruction](../reviews/mixed-partial-parent-2026-10-14-p5q14-review.md)).
This excludes the exact candidate family below; it does
not resolve the unrestricted two-convex-tile problem.

## Statement and exact polygons

Let z=exp(iπ/14), i=z⁷, and work in Q(z) with the specified complex
embedding. Its defining polynomial is

    z¹²-z¹⁰+z⁸-z⁶+z⁴-z²+1=0.

Put s=(z-z⁻¹)/(2i), y=2s+4s², and v=1+2s(1-y). The pentagon P starts
at0 and has successive edge vectors

    (z⁻⁵, z, z⁷, v z¹³, y z¹⁹).

The Q14 polygon Q starts at0 and has successive edge vectors Lⱼz²ʲ,
j=0,…,13, where its native side-length word is (v,v,1,v,v,1,1)².
Both are strictly convex, close exactly, and satisfy 0<y<1<v.

**Theorem.** There is no plane tiling by isometric copies of P and Q,
even when reflections and unrestricted contacts are allowed.

**Corollary within the audited angle family.** The same fixed P cannot
tile together with any convex equiangular14-gon of angle6π/7. The earlier
necessary native-contact/count classification restricts such a partner
to35 closed binary words, and its mandatory native-palette audit reduces
all surviving shapes to Q above up to congruence.

## Audited prerequisites and their necessity

The complete reductions and their independent audits are preserved in
[the original experiment](../searches/contact-pentagon-5pi7-q14-exact.md),
[native-ring review](../reviews/contact-pentagon-5pi7-q14-independent-hostile-review.md),
and [palette review](../reviews/contact-pentagon-5pi7-q14-exact-palette-review.md).
The present proof uses precisely these established statements:

1. P has native corner0 of angleα=5π/7 and corners1–4 of angleβ=4π/7;
   Q corners have γ=6π/7. All angles lie strictly betweenπ/2 andπ.
   Therefore every admitted contact is whole native edge-to-edge and
   every vertex is trivalent. A T-contact is impossible: a flat host
   occupiesπ, while the complementaryπ needs at least two native
   corners, each greater thanπ/2. The complete full-star equation
   5A+4B+6C=14 gives only PPP=(2α,β) and PPQ=(2β,γ).
2. Every P's native y side4 is an α–α edge. Its unique neighboring
   P is reflection in that whole side, fixing native endpoints0 and4.
   Every native v side3 necessarily meets Q. Q can meet a P only along
   native u side1 or v side3; numerical aliases x=u=w=1 do not change
   these native identities. These deductions already include both P
   hands and every unit-side alias.
3. P alone cannot tile. Its only full star has twoα and oneβ, incompatible
   with oneα and fourβ per tile. In a square of sideR, native counting
   gives p=2N+O(R), 4p=N+O(R), hence7p=O(R), contradicting p=Ω(R²).
   Boundary terms are linear because the fixed compact convex polygons
   have positive area and bounded diameter. Thus a hypothetical P/Q
   tiling contains a Q.
4. Each Q's14 edge guests and all their forced α–α reflection mates
   necessarily occur in the hypothetical tiling. The exact exhaustive
   native-ring/dimer/palette audit leaves28 indexed patches, four for
   each of the seven cyclic rotations of period vvuvvuu. A surviving
   patch has Q plus20 distinct P faces. No other local native state
   can be rescued by tiles outside the patch: the rejected cases
   already contain an overlap, forbidden T-contact, or inconsistent
   native-corner multiset.

For the corollary, no QQ edge is possible by the full-star palette.
Consequently every Q side is native1 or v. Counting PPP/PPQ stars gives
p=8q+O(R); counting the unique obligatory v-Q contact per P gives
p=kq+O(R), where k is the fixed number of v sides of Q. Since
q=Ω(R²), k=8. Exact closure exhausts all C(14,8)=3003 binary masks,
leaving35 words; the earlier complete audit leaves the seven congruent
split-v-run words above. These are necessary reductions, not imposed
matching rules or periodicity assumptions.

## Normalization of all possible central states

Apply a global isometry taking a chosen Q to the displayed exact Q.
P copies retain both allowed hands. The four normalized states have
these author-native guest-choice cycles (slot indices0,…,13):

    10010101001010
    10010101011010
    10110101001010
    10110101011010

Each cycle chooses one of the two allowed native placements at every
Q edge; their ordering is that of the frozen original producer. The
compact certificate contains an explicit exact rotation zᵏ and
translation for each of all28 indexed positive patches, and a bijection
of its21 actual faces to one of these four states. The independent
verifier checks the full maps and equality of the five ordered native
P vertices, beyond merely equality of unordered face sets. A rotated
seven-bit period supplies no extra state or missing native incidence.
If the global isometry reflects, both hands are still present in the
native placement enumeration. This accounts for arbitrary central
rotation, translation and reflection.

Label faces as follows: face0 is Q, faces1–14 are its ordered native
edge guests, and faces15–20 are the previously absent mandatory mates
added in slot order. In all four states these three actual P tiles agree
exactly, including native indexing:

- F=face6, the guest on unit Q slot5;
- G=face7, the guest on unit Q slot6;
- M=face16, the mandatory α–α reflection mate of F.

The proof needs only these three P tiles and the central Q's shape.
The six possible unit-guest obligations were investigated, but one
obligation already yields the complete contradiction.

## Complete finite domain for the obligatory neighboring Q

Let a=F₃ and b=F₄. The segmentab is F's native v side; it is not any
edge of the central Q. By prerequisite2 it must meet a different Q.
Every permissible isometric copy of Q sharing this whole segment can
be written

    T(p)=r p+d, or T(p)=r conjugate(p)+d,

with |r|=1. An isometry maps native polygon corners to corners; because
1≠v, the matched Q edge must be one of the eight native v indices

    J={0,1,3,4,7,8,10,11}.

For each hand h=+1 or−1 and each j∈J there is exactly one endpoint
order putting the Q interior opposite F acrossab. If ε is F's native
winding sign, use start,end=(b,a) when ε=h, and (a,b) otherwise.
With Bⱼ=Qⱼ for h=+1 and conjugate(Qⱼ) for h=−1, the forced map is

    r=(end-start)/(Bⱼ₊₁-Bⱼ),  d=start-r Bⱼ.

Thus there are exactly16 indexed attachments, not an arbitrary
orientation or translation grid. All16 are retained for each central
state. Only afterwards are unordered Q face identities compared,
yielding four physical Q placements per state. Symmetric native
representations do not remove any tested incidence obligation.

## Pointed exact obstruction

For each of all64 cases (four central states ×eight native v sides
×both hands), a native corner p of T(Q) lies strictly inside the
native v side of G or M. The compact certificate gives p, the host
native endpointsc,d, and the native corner and face indices. Its exact
predicate is

    cross(d-c,p-c)=0,
    (p-c)·(p-d)<0.

Equivalently p=c+t(d-c), where the only parameters occurring are

    t=3-z⁴-2z⁶+2z⁸+z¹⁰=1/v,  or 1-t=(v-1)/v,

and v>1 immediately gives0<t<1. Each parameter occurs
32 times. The independent verifier checks collinearity, strict
interiority, and the exact coordinates of every pointed incidence.

For an explicit exhaustive index table, these are the state0 cases;
the same F,G,M coordinates and indices apply to every other state.
The host side is native3 in every row. Q corners are indexed in the
original native order, including for reflected copies.

| Q hand | Q matched native side | rotation exponent k | host face | Q corner |
|---|---:|---:|---:|---:|
| +1 |0|26|7|13|
| +1 |1|24|16|3|
| +1 |3|20|7|2|
| +1 |4|18|16|6|
| +1 |7|12|7|6|
| +1 |8|10|16|10|
| +1 |10|6|7|9|
| +1 |11|4|16|13|
| −1 |0|12|16|13|
| −1 |1|14|7|3|
| −1 |3|18|16|2|
| −1 |4|20|7|6|
| −1 |7|26|16|6|
| −1 |8|0|7|10|
| −1 |10|4|16|9|
| −1 |11|6|7|13|

These actual T-contacts contradict prerequisite1. No neighboring-Q
native-ring completion or global hypothesis is needed for this step.
The necessity chain is now complete: Q presence is forced; its central
neighborhood belongs to one of four states; that neighborhood contains
F,G,M; F's native v edge forces a neighboring Q; every geometric
placement of that Q has a forbidden T-contact. Therefore no admitted
plane tiling exists. In particular, the candidate cannot be aperiodic.

## Orientation transitions, simultaneous compatibility and holonomy

The larger fixed contact-derived investigation was fully executed
before extraction of the simpler witness. For every central state,
each of its six unit guests supplies an obligatory v-Q contact. For
each contact we tried16 indexed Q attachments and four possible
normalized neighboring mandatory rings, giving1536 indexed cases:

| Outcome | Count |
|---|---:|
| Actual required P absent from the neighboring ring |768|
| Positive-area overlap with the central mandatory patch |128|
| Forbidden native T-contact |576|
| Native-corner multiset incompatible with PPP/PPQ |64|
| Compatible completion |0|

These are stronger necessary geometric tests, not a proof of global
existence from a graph. Every mandatory central obligation has zero
compatible transitions. Accordingly there is no simultaneously
compatible assignment of neighboring Q tiles and no surviving closed
transition chain on which holonomy could be nontrivial. A periodic
lattice/quotient search would be unnecessary: the obstruction occurs
at one mandatory native contact. The compact64-case proof above
avoids relying on the ring-missing/overlap/star classification of
this larger computation.

## Arithmetic, certificates, replay and scope

No solver, random seed, numerical tolerance, timeout-based negative
inference, patch-size escalation or quotient-size escalation is used.
All equalities lie in Q(z); all proof-critical inequalities use exact
real algebraic signs in Sage. The producer uses CyclotomicField(28);
the small verifier independently uses the displayed degree12
NumberField presentation. Software versions are frozen in both
certificates. The finite domains complete without a resource cutoff.

Artifacts:

- [Producer](../searches/p5q14-orientation-transition-2026-10-14.py).
- [Compact64-case pointed certificate and28 normalization maps](../certificates/p5q14-orientation-transition-2026-10-14-compact.json).
- [Small independent verifier](../reviews/p5q14-orientation-transition-2026-10-14-verifier.py).
- [Full1536-case transition certificate](../certificates/p5q14-orientation-transition-2026-10-14.json).

Replay from the repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/p5q14-orientation-transition-2026-10-14.py --compact-check research/certificates/p5q14-orientation-transition-2026-10-14-compact.json
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/p5q14-orientation-transition-2026-10-14-verifier.py
mise exec -- conda run --no-capture-output -n arisearch python research/searches/p5q14-orientation-transition-2026-10-14.py --check research/certificates/p5q14-orientation-transition-2026-10-14.json
```

The first two are sufficient to replay this theorem's new finite
component; the earlier audited native-ring and palette classifications
remain explicit dependencies. The last preserves the full exploratory
transition domain. This is a candidate-family untileability result.
It does not establish that arbitrary pairs of convex polygons admit
periodic tilings or cannot force aperiodicity.
