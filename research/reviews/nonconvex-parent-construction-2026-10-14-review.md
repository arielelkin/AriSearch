# Independent hostile review of the bounded nonconvex-parent construction cycle

Date: 2026-10-14. **Verdict: VALID within the recorded finite domains.**
The reviewer did not develop or repair either producer, the retained atoms,
the parent attachments, or the T-completion search. No producer or
certificate was changed by this review. The independent
[checker](verify_nonconvex_parent_construction_2026_10_14_independent.py)
imports no author code and uses Q(ζ24) complex coordinates for the repair
geometry, rather than its real Q(√2+√3) matrix encoding.

Submitted [note](../searches/nonconvex-parent-construction-2026-10-14.md),
[initial producer](../searches/nonconvex-parent-construction-2026-10-14.py),
[repair producer](../searches/nonconvex-parent-construction-2026-10-14-pentagon-repair.py),
and their frozen certificates were inspected. This review covers the
1430-signature initial closure census, the fixed repaired atom pair and
eight native parents, and the one-stage 216-placement T-capable test.
No eight-child cover enumeration, infinite extension or forced hierarchy
is claimed or independently inferred.

## Original all-hexagon domain

The B edge directions are correctly derived from the native angle word
(u,120,β,v,120,η): (0,60,240−β,u+η−60,u+η,u+180), using
u+v+β+η=480. The three p directions and three unit directions give one
exact complex linear closure equation. The independent checker exhausts
the prescribed 10-degree angle grid afresh and finds exactly1430 angle
signatures and zero real positive p≠1 closed B polygons, agreeing with
the certificate. Therefore no atomic pair reaches any later parent gate.

The initial producer's `native_stars` helper examines only three native
corners and would not be a complete all-contact filter for acute B
signatures admitting higher-valence or T stars. This was raised during
review. It is unexercised because the earlier closure domain is empty;
the final note explicitly records this limit. Thus no result relies on
that incomplete helper and no repair to the retained closure conclusion
is needed. The separate fixed-atomic perimeter theorem has its own
[fresh review](nonconvex-parent-hexagon-perimeter-bound-review.md).

## Fixed pentagon/hexagon repair and parent obstruction

The checker independently reconstructs the displayed P,Q coordinates,
every strict support, their native isometric placement data, area(P)=10/√3
and unequal areas. Their side counts distinguish the congruence classes.
For a two-atom parent, scalar2 multiplies area by4; with eight children,
unequal areas force exactly4P+4Q. This is an area necessity, not proof of
a dissection.

There are exactly four equal native P/Q side pairs. Both endpoint
assignments and orthogonal determinant signs give eight opposite-interior
attachments. The independent checker verifies all eight actual placed
polygons, separation, boundary area conservation and the pointed native
endpoint obstruction. The producer's reversed boundary traversal and
flat-vertex suppression were inspected; these produce simple nonconvex
unions of the two convex polygons sharing a full side. Counts refer to
indexed attachments, not distinct congruence classes.

Every P side has a120 endpoint. At a full P/Q seam it meets Q90 or Q135,
leaving150 or105 degrees. Neither gap is filled by any nonnegative
combination of native90,120,135 or a flat180 sector. The two placed atoms
already occupy sectors totaling more than180, so no alternative flat
host can evade this gap. Hence none of the eight parents occurs in an
admitted full-plane atom tiling. This kills this whole-native parent
mechanism before a child-cover search; it does not reject arbitrary
partial P/Q contacts.

The P-only omission filter is also applied correctly. Starting at native
vertex2 and rotating −120 gives Cairo directions(0,90,150,240,300) and
lengths(a,b,c,d,e)=(1,7/√3,1/√3,3,2). The checker verifies that actual
coordinate transformation and both closure identities. The four90 arms
a,b,c,d are pairwise distinct, so the necessity part of the separately
reviewed [unrestricted Cairo monohedral theorem](../lemmas/partial-contact-cairo-monohedral-classification.md)
excludes P-only tilings. This imports a proved restricted angle-family
theorem, not completeness of a general pentagon list. The adversary's
bounded two-copy halfturn failure is correctly recorded only as a scoped
NO_WITNESS result; no Q-only conclusion is inferred from it here.

## T-completion completeness and host switches

At a native P120 vertex, a flat host would leave60 degrees, which the
palette cannot fill. Four native corners exceed360. The only full star
containing120 is therefore PPP120³. Normalize the three rays to0,120,240.
Three native120 choices and two arm assignments independently in each
sector give exactly6³=216 oriented stars, including reflections. The
checker verifies the complete unique placement-key domain and all central
native congruences. No edge-to-edge convention was imported.

At an unequal ray, its shorter edge ends in the other tile's side. A
short120 endpoint is impossible because180+120 leaves60. A short90
endpoint leaves precisely a90 wedge, forcing one native90 corner of P or
Q. Both such corners of each shape and both arm assignments are
enumerated. The orthogonal matrix construction places exactly those
copies, without a length-alias or reflection reduction.

The two new contacts are tested symmetrically. If one side is shorter,
its endpoint must be90: native120 or135 would need a missing60 or45
complement to the flat host sector. A side extending beyond an existing
90 host endpoint is retained, allowing the host to switch there. Equal
endpoints require only that their remaining angle be a native/flat
palette sum. In particular a180 gap may be a flat sector or two90
corners; the producer includes both in its generous necessary test.
This avoids imposing the false equality that every guest terminates at
the first host endpoint.

Guests are checked against all three central atoms. Choices for multiple
initial T points are then combined, identifying equal polygon sets as
one tile before overlap testing. That identification matters: one actual
tile may fill two T points. Every actual patch vertex also counts flat
incidences when it lies strictly inside another placed tile's side.
The remaining-angle test is conservative and local; it does not prove
those gaps can be filled consistently.

The final216 branches are116 NO_90_GUEST_COMPLETION,80
SHORT_RAY_END_IS_120, and20 LOCAL_COMPLETION_SURVIVOR. Each surviving
record has one joint completion. The independent checker proves native
congruence, genuine convexity, pairwise disjoint interiors and all
remaining-angle checks for every retained joint patch using oriented
supporting lines, rather than the author's projection interval helper.
Six contain native P4 and two P0 guests; each has five distinct P tiles
and two actual host switches. Those explicit positive controls defeat
an endpoint-splitting-only model. The other14 have no host switch.

The checker independently regenerates the1430 closure census and the
eight parent endpoint gates, but its T-domain computation checks all216
placement keys and the20 retained positive witnesses. It does not
independently reclassify the196 negative T branches. Their counts rely on
the frozen exhaustive producer, whose finite placement enumeration and
necessary rejection logic were independently audited above. This is the
explicit boundary between independent witness verification and reviewed
search evidence.

## Defects, repairs and limits

During this review the author was completing the already planned
equal-ray endpoint and joint-guest checks. The frozen version includes
them. The reviewer specifically challenged the flat180 gap, duplicate
guest handling and incomplete initial three-corner helper; the final
implementation/note address all three without dropping legal host
switches. No unresolved defect remains within the stated finite scope.

The check does not exhaust second-generation T completions, all partial
parents, larger quotients, different metrics or other substitutions.
The P-only patches remain compatible locally despite the separately
proved global P-only obstruction. No infinite tiling is inferred from
the finite positives, and no unrestricted impossibility or aperiodicity
is inferred from the killed parent mechanism.

Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_nonconvex_parent_construction_2026_10_14_independent.py
```

The independent check passes. Its remaining trusted dependency is Sage
exact number-field/real-algebraic arithmetic; this is not a proof-assistant
formalization. The broader two-convex-tile problem remains unresolved.
