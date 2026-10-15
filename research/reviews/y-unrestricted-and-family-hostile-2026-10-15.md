# Fresh hostile audit: fixed Y pair and parameterized obstruction

Date: 2026-10-15. Reviewer: independent fresh agent; no authorship of the
reviewed proofs or their producer checkers.

## Exact claims and verdicts

1. `research/lemmas/pentagon-y-unrestricted-2026-10-15.md`: **VALID** for
   nonexistence of an unrestricted plane tiling by the two displayed fixed
   pentagons, conditional only on its cited, already independently reviewed
   full-BB-mate theorem (which was read in this audit).
2. The abstract obstruction in
   `research/lemmas/y-pentagon-parameter-family-2026-10-15.md`: **VALID**
   under precisely its stated angle, side-cycle, irrationality, and strict
   metric hypotheses. Its BB argument is self-contained and does not need
   the fixed-pair BB theorem.
3. The rational-coordinate parameter family in that file: **VALID** for
   every rational t in its stated open interval. Its reduction to the abstract
   hypotheses is correct.

These are candidate-family exclusions. None establishes the main two-convex-
tiles construction or universal impossibility problem. This review does not
establish novelty; that remains a separate literature obligation.

## Assumptions independently reconstructed

I rebuilt the six angle vectors in the basis (pi/4,theta), enumerated all
multisets of one through five corners for total 2pi and one through two for
total pi, and obtained exactly the stated seven full stars and two flat
stars. These size bounds follow from c>3pi/8, so a sixth native corner or
third corner beside a flat is impossible. The vectors are independent
because theta/pi is irrational. In the rational family, the root-of-unity
argument is valid: a rational algebraic integer 2cos(2theta) is an integer
in [-2,2], and its five possibilities give no rational t in the interval.

The independent checker reconstructs both coordinate polygons, all ten edge
lengths, each corner cotangent, and strict convexity by testing every other
vertex against every directed supporting edge. It proves signs on the
whole exact algebraic interval by exact root exclusion and evaluation at
t=2; it does not substitute numerical sampling for an interval proof. The
three printed quadratic identities and 4L^2-9S^2=2(t-1)^2 all hold. Thus
0<S<R<L<2S, 2L!=3S, and (for rational t) 2R!=3S are justified. The t=2
coordinates give the fixed pair up to the displayed translation of Q.

## Hostile contact-case audit

**Local finiteness and unrestricted contacts.** The contained-disk argument
is valid for these two fixed compact shapes, with a positive common disk
radius and a bounded diameter. Hence the contact subdivision of a native
side is finite. At an interior change of the positive-length guest contact,
either adjacent guest has a flat sector, since a flat sector occupies all
of the available half-plane. Both contacts therefore end at native vertices.
Any intermediate complete guest side is at least S. This validates both
the GG interval argument and the at-most-one BB transition bound. A tile
with only a point contact does not evade the argument: at a transition the
flat palette permits exactly two native corners, while inside a positive
contact interval the opposite guest is flat and fills its half-plane.

**GG cases.** The no-flat property at G excludes a containing native side
and any endpoint overhang. Two complete guest sides cannot fit because
2S>R. Thus a full length-R mate is forced. A GG/GG mate gives the unique
RGG endpoint star and places GC against RA. Its C at distance S<R forces
B against a flat; the B arm reaches past the host A because R-S<S. This
contradicts no-flat at A. The argument uses native arms and works after
reflection, without assuming a common orientation.

**BB transition cases in the generalized proof.** An overhung host B
forces C, and its arm on host BA must be CD: a CG arm would put forbidden
G inside that longer BA. Its other arm is consequently the actual guard
CG on the BB continuation. For an outward forbidden endpoint A,D,G,
both strict orders relative to guard G are impossible, so equality is
necessary. An rr transition therefore forces 2R=3S. At a bc transition,
C cannot use GC horizontally because its G is inside the guard; B then
cannot use BB horizontally because the internal G would be inside BA.
Both horizontal arms have length L and the guards force 2L=3S. Both
orders and both reflected arm arrangements are covered.

**Containing BB side.** If a longer side overhangs both ends, its at least
one forbidden endpoint must equal its guard G, requiring length at least
2S, contrary to R,L<2S. In the one-flush case the far endpoint lies
strictly inside its guard and cannot be A,D,G. The surviving directed
profiles are exactly RA flush at A, AB flush at A, and CD flush at D.
For D+B the positive residual is smaller than 2c and has theta coefficient
-3, so no native completion exists. For A+B the completion is uniquely G.
RA flush at A puts G's GG endpoint inside one of two length-L arms.
AB flush at A forces GG onto the length-R ray and GC onto host BA; its
C then forces B, whose length-at-least-S arm passes through the original
host A because L-S<S. This exhausts longer containing sides.

**Actual corner propagation.** The proof correctly stays on one particular
P tile. One Q forces a full GG/RA mate; at that P's R the second G cannot
use GC and therefore supplies the other complete GG/RA mate. Thus both of
that actual P's A corners are in ABG stars. Across either AB, the B cannot
use BB because the proved full-BB-mate rule forbids the longer AB as mate;
it must use BA, whose equal length makes this a full match. At each actual
far B the native star is ABG, putting G across the original BB ray. The
original BB's full mate would thus need G at both endpoints, but the
length-S side inventory is only BB and CG. This is the required contradiction;
there is no illicit replacement of an actual endpoint by an abstract label.
A P-only tiling is excluded by either A star; Q-only is excluded by GG/RA.

## Defects, repairs, and uncertainty

No substantive defect found; no repair was needed or made to author proofs.
The arguments use neither edge-to-edge hypotheses nor a bounded-search to
infinite-tiling inference. Their unbounded component is the written local
geometric contradiction, not the finite computation. The checker below
independently verifies the finite symbolic and metric inputs; it does not
purport to formalize every geometric inference in a proof assistant.

Independent verifier (no producer imports):

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/y-family-independent-hostile-check-2026-10-15.py

Observed result: PASS. The verifier's finite domains and exact-arithmetic
method are stated in its module docstring. No random seed, solver, timeout,
or bounded placement depth is used. No new global tiling claim or priority
claim should be inferred from this audit.
