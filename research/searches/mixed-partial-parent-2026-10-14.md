# Offset mixed partial-contact parent: exact obstruction

Date: 2026-10-14. Status: **fresh independent hostile review VALID** for the
repaired no-positive-P/Q-contact theorem and its stated limits;
see [review](../reviews/ammann-fractional-resection-2026-10-14-mixed-parent-review.md).
No aperiodic pair or plane extension is claimed. This tests one two-child
mixed parent with a genuine partial contact, then excludes its entire offset
interval and the one proposed metric repair. It does not enlarge any child bound.

## Contact equations before atomic coordinates

Place a P side of length3 on [0,3] of the x-axis, with P above it and its90
endpoint at0. Place a half-turn Q side of length b on [t-b,t], with Q below
it and its90 endpoint at t. The interface equations are

    0 < t < min(3,b), overlap=[0,t].

The P90 endpoint lies inside Q's native side and Q90 lies inside P's native
side. Each seam endpoint has inside sector180+90=270, leaving an exterior90
wedge. This is the intended flat-boundary mechanism: a native90 guest would
supply a legal180=90+90 boundary subdivision. The other seam-native endpoints
are outside the seam; the old full-edge120+90 and120+135 endpoint failures do
not apply there.

Fix b=3,t=1 for one exact constructive parent. Let r=sqrt3,s=sqrt2 positive.
The counterclockwise atoms are

    P=((0,0),(3,0),(4,r),(7/2,3r/2),(0,1/r)),
    Q=((0,0),(3,0),(3+1/(sr),1/(sr)),
       (3+1/(sr),7/r+1/(sr)),(s,7/r+1/(sr)),
       (0,7/r+1/(sr)-s)).

Native angle words are P=(90,120,120,90,120) and
Q=(90,135,135,90,135,135). Both atoms are strictly convex; they have different
side counts. With Qhat=(1,0)-Q, their interiors are disjoint by the x-axis
separation and their intersection is exactly the strict partial seam[0,1].
Writing vertices with subscripts, the simple parent boundary is

    (Qhat0,P1,P2,P3,P4,P0,Qhat1,Qhat2,Qhat3,Qhat4,Qhat5).

It has11 genuine corners and exactly two reflex270 corners. Its area is
area(P)+area(Q), with area(P)=10/r. The producer and certificate preserve
this exact finite mixed parent. It is a valid local geometric union that fails
the mandatory external completion test.

Arithmetic uses K=Q(g), g=sqrt2+sqrt3, minimal polynomial g^4-10g^2+1.
Recover s=(g-1/g)/2,r=(g+1/g)/2, with the positive real embedding. Certificate
coefficients use the basis(1,g,g^2,g^3). No numerical geometry is used.

## Angle-only mixed-wedge obstruction

Allowed native angles are90,120,135, and a side-interior incidence contributes
180. None of45,60,105,150 is a nonnegative sum of this palette. Any exterior90
wedge therefore has exactly one native90 guest corner. Each native90 corner
of P has two neighboring120 corners; each native90 corner of Q has two
neighboring135 corners. Reflections exchange its arms without changing this
homogeneous pair of far-corner angles.

Suppose the two boundary rays of an exterior90 wedge follow native host sides
until far endpoints of angles120 and135, respectively. Any guest arm has a
far endpoint of120 or135. If the guest arm is shorter than its host ray, its
far corner lies in a flat host sector; the remaining angle is60 or45, impossible.
If it is longer, the host far corner lies in a flat guest sector; again the
remaining angle is60 or45, impossible. This expressly retains attempted host
switches past the host endpoint rather than assuming they never occur.
Consequently both guest arms must end exactly at the host far endpoints.
At coincident endpoints, a120/135 pair leaves105, impossible. A P90 guest
can thus match only a120/120 host pair; a Q90 guest only a135/135 host pair.
Neither can match the mixed120/135 wedge. This exhausts four native90 corners,
both arm assignments, and all three length orders on each ray.

At Qhat0=(t,0) in the proposed parent, the exterior90 wedge borders the P
side remaining to P1 (far angle120) and Q's other incident side (far angle135).
The mixed-wedge obstruction kills it for every0<t<min(3,b), independent of
all lengths. The two exterior wedges cannot both be completed; in fact this
one alone is impossible. There is no subsequent atomic-cover search.

## Complete positive-contact theorem for these words

**Theorem.** For any strictly convex positive-metric P,Q with the displayed
native angle words, no admitted plane tiling contains a positive-length P/Q
contact. Partial contacts, arbitrary rotations, and reflections are included.

**Proof.** Consider two native sides sharing a positive interval. Their tiles
are on opposite sides of the shared line. A P120 endpoint cannot lie strictly
inside Q's side: its120 sector plus Q's flat180 sector leaves60. It cannot
coincide with a Q90 orQ135 endpoint either: the remaining angle is150 or105.
Thus every P120 endpoint of the P side lies strictly outside the Q interval.

If both P endpoints are120, positive intersection would require Q to lie
strictly between them; Q has at least one135 endpoint, which would then lie
inside P's side and leave45. This is impossible. Hence the P side is90-120.
Normalize its interval to[0,L], P90 at0, P120 at L. Because L must be strictly
outside the Q interval, positive intersection forces Q's right endpoint
q_right into(0,L), while its left endpoint q_left is less than q_right.
Q's right endpoint must be90, since a135 corner inside P's flat side leaves45.
The other endpoint of that Q side is135, and cannot be strictly inside[0,L].
It follows that q_left<=0. Exactly two cases remain:

1. q_left<0: staggered host switch, with P90 and Q90 inside the other's side;
2. q_left=0: Q is contained in P with its135 endpoint coincident with P90.

The aligned case must be retained: the coincident90+135 endpoint leaves a
legal135 remainder. An initial interval argument omitted this case; root
review supplied it before this record was frozen. The repaired proof includes
it explicitly. In both cases, the Q90 point q_right lies inside P's side.
The exterior90 wedge there follows P's remaining ray toward P120 at L and
Q's other incident side toward a Q135 corner. The mixed-wedge obstruction
excludes it. This proves the theorem. The certificate enumerates the local
angle/corner alternatives; the universal interval argument is this proof,
not an inference from sampled offsets. QED.

With a finite set of compact convex prototiles, any plane tiling is locally
finite: tiles meeting a compact set lie in a fixed enlarged compact set and
their disjoint positive areas bound their number. The graph joining tiles
across positive-length contacts is connected, since a compact path between
two tile interiors can be perturbed to avoid the finitely many native vertices
and can then cross only relative interiors of shared side segments. Therefore
this theorem also implies that any plane tiling by this pair uses only one
species. The primary retained result is the no-mixed-contact theorem.

## Cheap gates and the one repair

Closure, supporting-line strict convexity, exact angles, the partial seam,
nonoverlap, simple boundary, parent area and both reflex corners are checked
before any extension enumeration. The exact guest census has8 oriented right
corners and zero completions. No child-cover, quotient growth, radius growth,
SAT timeout or numerical acceptance criterion is used.

The fixed P has Cairo arm indexing(a,b,c,d,e)=(1,7/r,1/r,3,2). Its four90
arms are pairwise distinct. The independently reviewed
[monohedral Cairo theorem](../lemmas/partial-contact-cairo-monohedral-classification.md)
therefore excludes unrestricted P-only tilings. The previous exact
[two-copy half-turn lattice audit](construction-adversary-2026-10-14.md)
retains no Q-only witness in its60-generator domain; that is only a bounded
NO_WITNESS result and is not used as a Q-only obstruction here. Q-only
existence is explicitly unclassified by this work.

The only contemplated repair increases Q's base b>3 while preserving its
angle word, with remaining native lengths

    (b,u,7/r,b+(u-2)/s,2,7/r+(u-2)/s), u=1/r.

Closure holds; all lengths remain positive for b>3 and the polygon stays
strictly convex. The first forced P90-guest metric equation suggests b-t=3,
i.e. t=b-3 and3<b<6. However its other ray still has a120/135 endpoint
mismatch. The angle-only theorem excludes every such metric, as well as the
larger strictly convex positive-metric domain of these words. No numerical
search of b or second repair is warranted.

The flat boundary mechanism is real locally(90+90=180), but its far endpoints
cannot transmit an interface across the two species. Parent repeatability
thus fails before an inflation count or perimeter resource check is useful.
There is no extension/recognition obligation left for this killed scheme.
A viable future construction must change the native neighbor-angle correlation
around90 corners, providing at least one mixed far-angle right corner, or
change the flat-star palette. Merely changing these side lengths or increasing
children cannot repair this obstruction.

## Replay artifacts and proof scope

[Producer](mixed-partial-parent-2026-10-14.py),
[frozen certificate](../certificates/mixed-partial-parent-2026-10-14.json), and
[independent checker](mixed-partial-parent-2026-10-14-verify.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/mixed-partial-parent-2026-10-14.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/mixed-partial-parent-2026-10-14-verify.py

Default producer output is deterministic JSON and does not rewrite evidence.
The independent checker reads the frozen certificate, reconstructs its scalar
embedding with exact algebraic reals, and separately checks geometry, complete
right-corner keys, local angle alternatives and the fixed P omission premise.
It cannot replace the written interval proof. The fresh
[independent hostile review](../reviews/ammann-fractional-resection-2026-10-14-mixed-parent-review.md)
also retains all198 positive-overlap weak endpoint-order/native-side-word
cases in a separate exact proof checker and finds the repaired theorem VALID.
No literature novelty claim is made, and the unrestricted objective
remains unresolved. Discovery-log and registry integration belongs to root.
