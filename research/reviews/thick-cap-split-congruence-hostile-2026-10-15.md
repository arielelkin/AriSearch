# Independent hostile review: thick-cap split congruence gate

Date: 2026-10-15. Reviewer did not develop the cap geometry or the author
checker. Verdict: **VALID** for the stated admissible mark-local,
normal-foot, equal-radius construction component. This is a restricted
construction obstruction, not a universal impossibility theorem.

## Exact claim reviewed

The author artifact is
[thick-cap-split-congruence-gate-2026-10-15.md](../searches/thick-cap-split-congruence-gate-2026-10-15.md),
with its author checker. I independently read its precursor
[three-sector construction](../searches/three-sector-fractional-construction-2026-10-15.md),
the actual source arrows in the
[split-edge artifact](../searches/ammann-split-edge-two-recipient-gate-2026-10-14.md),
and the changed-incidence proposal in
[the 09:00 Astra record](../searches/astra-direction-2026-10-15-0900.md).
No author module is imported by the new reviewer checker.

The claimed exclusion covers all admissible parameters in this component:
mark-local a_X,a_Y in (0,1) and positive h_X,h_Y; source-edge split M
which is the normal foot of its external donor apex t; donor nodes inside
their source rhombs; equal-distance cuts along all incident rays at each
node; thin caps left whole; thick caps split between interior points of
opposite cap edges into two strict pentagons. Precursor sectors must form
a valid embedded partition and all stipulated final corners must be genuine.
The fixed legal Ammann source contains a thin rhomb, hence at least one
whole thin hexagonal cap. The proof needs only that occurrence, not every
source-type/parity combination actually occurring in one source tiling.

The conclusion is that the resulting polygon outputs cannot occupy just
two Euclidean congruence classes, with reflections permitted. No intrinsic
source decoder, marked matching rule on final tiles, or uniqueness of a
cap's native labeling is assumed or inferred.

## Native incidence attack

For each of the four source-type/donor-parity cases I independently built
all receiving precursor words from source indices. At receiving edge i,
U=i,V=i+1, the internal nodes are p=d_(i-1), q=d_(i+1), and the external
apex is e_i. The words are (U,e_i,M_i,p), (M_i,e_i,V,q), (M_i,q,p).
Replacing each of their two donor-node vertices by its two ray-cut points
produces exactly the author's H_L,H_R,P_C words. They have respectively
6,6,5 native slots under the strict admissibility assumptions.

At each of the eight donor nodes across the four cases I collected the
four own-source incident sectors from these words and the two transferred
donor half-triangle sectors. Their ray-pair incidence is exactly the
six-cycle

    T, M_donor, H, M_H, opposite donor node, M_T.

Using the actual source arrows reverses this cycle when appropriate; it
does not reorder its middle rays incorrectly. Thus the cap indexing and
six-sector topology are compatible with both parities and both arrow
orientations. Opposite-edge split boundary incidence also checks: the two
five-vertex words cover the eight refined cap boundary edges once and
their common chord twice.

This does not independently prove source-sector embedding for all metric
parameters. That is an explicit admissibility hypothesis of the theorem,
and an inadmissible parameter is not a counterexample. The reviewed
obstruction is conditional on that full partition and strict convexity.

## Cyclic-angle attack and complete local proof

A strict convex hexagon whose vertices lie on a circle has equal alternate
interior-angle sums, both 2pi. This holds even if the circle center lies
outside the polygon. If its six consecutive positive central gaps are
(delta_0,...,delta_5), then angle_i=pi-(delta_(i-1)+delta_i)/2.
Each central gap occurs once in either alternating sum, so that sum is
3pi-(sum delta_i)/2=2pi. This is used only as a necessary condition,
not as a sufficient test for cyclicity.

For a strict original quad with angle alpha at a clipped corner, two cut
points at the SAME radial distance produce an isosceles removed triangle.
Its two base angles are (pi-alpha)/2. Hence both new polygon angles are
(pi+alpha)/2. This identity is independent of the cut radius. It remains
valid if the two DIFFERENT clipped vertices use different radii.
Disjoint admissible cuts leave the other original corner angles unchanged.

For L=(U,t,M,p), the resulting native angle sequence is

    alpha_U, (pi+alpha_t)/2, (pi+alpha_t)/2,
    alpha_M, (pi+alpha_p)/2, (pi+alpha_p)/2.

Subtracting alternate sums leaves exactly alpha_U-alpha_M. Thus cyclicity
of this receiving hexagon forces alpha_U=alpha_M, with no preferred mapping
to any cap vertex. The R quad gives the corresponding equality between
its original V and M angles.

At M use isometric coordinates with the receiver in y<0 and the source
edge on y=0. The normal-foot rule gives M=(m,0), t=(m,h), h>0.
An internal donor node has p=(x,y), y<0. Therefore

    (t-M) dot (p-M) = h*y < 0.

The strict convex quad's interior M angle is the smaller angle between
these rays, so it is strictly greater than pi/2. Thus the original U
angle is strictly obtuse. Applying this at both ends of both receiving
edges of any thin source rhomb makes all four source-vertex endpoint
angles of its four receiving quads strictly obtuse.

Every thin cap has six vertices on one circle. If there were only two
congruence classes, strict pentagons and strict hexagons must occupy
different classes, since isometries preserve the number of genuine corners.
All hexagons would therefore be congruent to that whole cyclic thin cap,
and every receiving H_L,H_R would be cyclic. This proves all four obtuse
requirements. Neither thick-child congruence nor a hidden source labeling
was invoked.

## Actual-arrow cancellation attack

I did not accept the source mark count as a substitute for endpoint
geometry. Let Gamma_v be the original rhomb interior angle at source
vertex v. Its one owned receiving quad has angle

    Gamma_v - b_own_donor(v) + b_incoming_donor(v).

Indeed the valid sector partition removes the internal donor triangle's
base sector from the source angle, and attaching the external half-triangle
adds its base sector along the same physical source edge. Splitting that
base edge at M does not change the triangle's angle at the original endpoint.
There is one receiving quad at each of the four source vertices.

The actual arrow tail of mark Z has base angle atan(h_Z/a_Z); its head has
atan(h_Z/(1-a_Z)). Reversing an edge's direction in source boundary order
exchanges which endpoint gets which angle but does not alter the physical
arrow. In each thin/thick and parity case I calculated all four endpoint
angle rows on the independent formal basis

    Gamma_0,...,Gamma_3, X_tail,X_head,Y_tail,Y_head.

Their sum is exactly Gamma_0+...+Gamma_3: ALL FOUR tail/head coefficients
cancel separately. Thus their sum is 2pi. This verifies actual arrow and
endpoint compatibility, not merely equal counts of X and Y. Four strictly
obtuse angles would sum to more than 2pi, giving the required contradiction.
The mark-local hypothesis is essential here: unrelated source-context
base-angle values could not be canceled on this basis.

## Other attacks, defects and repairs

- **Corner aliases and reflections:** cyclicity and alternate-angle sums
  are intrinsic isometry invariants. Relabeling, reversing or reflecting
  any cap or receiver cannot bypass the argument. No D5 or D6 matching
  enumeration is needed.
- **Arbitrary admissible cut radii:** the isosceles-triangle formula has no
  radius parameter. It needs equal distances along the two rays of EACH
  cut corner, not equal radii at different donor nodes. A non-small cut
  is covered if it still satisfies disjointness and strict convexity.
- **Thick-cap chord aliases:** arbitrary lambda,mu in (0,1) change only the
  cap children. They do not alter any receiving hexagon or whole thin cap.
  The contradiction precedes every pentagonal child congruence equation.
- **Area gate:** the count vectors (2P+6H) and (6P+4H) and their stated
  exact area inversion are consistent. Passing that necessary area gate
  supplies no exception to the later angle obstruction.
- **Scope outside normal-foot or equal-radius rules:** the proof does not
  cover them. For instance (t-M)=(-2,1), (p-M)=(-1,-1) gives positive dot
  product despite p being in the lower half-plane; this shows why the
  normal-foot rule cannot be silently dropped. This is a counterexample
  to an overextended local sign argument, not an admitted construction.

No mathematical defect requiring author repair was found. The necessary
existence of a whole thin cap is explicit in this review and supplied by
the fixed two-species legal source. If the source were replaced by an
arbitrary all-thick dissection, that hypothesis would need separate analysis.

## Independent replay and final verdict

The reviewer-owned checker is
[thick-cap-split-congruence-independent-2026-10-15.py](thick-cap-split-congruence-independent-2026-10-15.py).
It imports only standard-library Counter and Fraction, independently
reconstructs the four actual-arrow endpoint cancellations and eight cap
ray cycles, audits all clipped native words and split incidence, and checks
the formal cyclic-angle identities and exact normal-foot dot polynomial.
It has no metric samples, numerical angle decisions, solver, or author import.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/thick-cap-split-congruence-independent-2026-10-15.py

Result: PASS. The universal strict inequalities and geometric implications
are justified in the proof above, rather than inferred from a sampled
fixture or absence of a counterexample.

**Final verdict: VALID.** The entire stated admissible construction component
is closed. No two-class output realization exists within it. No claim is
made about unequal-radius caps, off-foot split points, source-context-dependent
triangle rules, or the original unrestricted two-polygon target.
