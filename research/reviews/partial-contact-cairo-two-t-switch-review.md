# Fresh independent review: two-T switches and changed Cairo pair

Date2026-10-10. Reviewer: root, independent of the author.
[Submitted lemma](../lemmas/partial-contact-cairo-two-t-switch.md).

## Exact claims and hypotheses

For Cairo-angle polygons, an unequal arm/arm ray match from a120 star
forces two native90 T vertices. Their right-corner events have banks
{m,n},{M,q} with m+n=M+q and0<m<M<m+n. A beta-to-beta e side hosting
a T equals an event's bank sum. These are necessary relations for actual
unrestricted contacts, not extension or sufficiency rules. The particular
Q(sqrt3) pair in the submitted file has no admitted plane tiling.

## Hostile checks

The angle equations allow only90^4,120^3 and90^2+180 at native vertices.
At a T, both perpendicular native arms end120; their unequal lengths would
put120 inside a native side, so the event seam is whole. This applies
without private arms and with reflections. A shorter collinear arm ends90
inside the longer arm, creating the first T. The forward bank ends120 at
m+n. The host's90 endpoint must precede it and be strictly past m,
creating the second T. The second forward bank's120 endpoint must coincide
with the first forward bank endpoint; either strict ordering creates an
illegal120 inside a side. Intermediate vertices cannot occur on the
shared open subsegments because two tiles cover both half-neighborhoods.
Thus neither switch inequality nor sum identity assumes full host matching.

For e with no T, its opposing side cannot be an arm: unequal lengths
produce an interior120 or an interior90 T, while equal lengths identify
90 with120. Hence e must be wholly matched to e. With a T its two120
endpoints align the two bank120 endpoints, giving the event sum. Every
native side has at most one T: at a T each adjacent shared interval has
one fixed bank arm ending120; a second subdivision before that endpoint
would introduce a corner into two occupied half-neighborhoods. Reaching
a120 in the host interior is impossible. This remains valid when an arm
host ends90 before the forward bank; that is the second T on the other
bank's native side, not another T on the original host.

The explicit pair has eight oriented90 slots and12 equal-perpendicular
events. Its six distinct sums permit only unequal arm compatibility
{a,d} or{b,c}; e,f are absent from every sum and private among all
lengths. A P e seam therefore exists whole and with a second P. At each
endpoint, both other rays have a/d lengths. The third120 tile has to use
two arms in that same component; an e/f alternative is impossible by the
endpoint angles and sum exclusion. Neither native isolated120 corner has
both arms in{a,d}. This rules out every P occurrence. A Q-only tiling is
also excluded by the independently reviewed private-arm theorem, applied
to its four distinct arms alone. The target permits species omission and
the proof explicitly covers it.

## Independent computation and outcome

Added [no-author-import exact checker](verify_partial_contact_cairo_two_t_independent.py).
It independently accumulates the native side vectors, checks closure,
every side norm and supporting determinant, and reconstructs all8 slots,
12 events,6 sums, e/f exclusions and the complete finite compatibility
relation. Both author and independent checker pass:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-two-t-switch.py
    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_two_t_independent.py

No defect or repair found. The event list is a necessary contact filter;
its passage to unrestricted untileability uses the explicit local e-seam
contradiction, not an assumption that all local events extend. The theorem
does not classify other metrics or produce a tileable aperiodic pair. No
novelty claim.

**Verdict: VALID** for the switch invariant and the exact pair's
unrestricted untileability.
