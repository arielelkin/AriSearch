# Independent hostile review: mixed offset parent and all-metric contact obstruction

Date: 2026-10-14. Reviewer developed the separate Ammann fan-transfer
experiment and did not develop this mixed-parent construction or theorem.

**Verdict: VALID for the repaired no-positive-P/Q-contact theorem, its
fixed exact local parent obstruction, and the stated limits.** Q-only
plane tilability is not classified. This is not an unrestricted two-shape
impossibility theorem.

Reviewed record:
[mixed-partial-parent-2026-10-14.md](../searches/mixed-partial-parent-2026-10-14.md),
its producer, frozen certificate, and independent exact-algebraic-real
verifier. The certificate verifier was run successfully. I also wrote and
ran a separate [endpoint-order checker](ammann-fractional-resection-2026-10-14-mixed-parent-review.py)
that imports neither producer nor verifier.

## Claim and exact hypotheses

Let P,Q be strictly convex polygons, with positive native side lengths,
whose cyclic angles are respectively

    P=(90,120,120,90,120),
    Q=(90,135,135,90,135,135).

The claim is that no plane tiling by these two shapes can contain a
positive-length P/Q contact. All rotations, reflections and partial-side
contacts are admitted. The fixed parent is an actual finite nonconvex union
of one P and one Q with a strict partial seam; it is not asserted to extend
to a full-plane tiling.

## Attacks checked

1. **Hidden whole-edge assumption.** The proof compares guest and host arm
   lengths in all three orders. If a guest side ends before the host side,
   the guest far native corner meets a flat host sector; if it continues
   beyond the host endpoint, the host corner meets a flat guest sector.
   Native far angles120 and135 leave60 and45, respectively, after the
   flat180 sector. Thus both unequal orders are impossible by the full
   local angle palette. A new tile or a host switch after that point
   cannot supply the forbidden remainder.

2. **Non-native guest or more than one guest at the exterior wedge.** The
   remaining wedge angle is90. Every nonflat native angle is at least90,
   and an edge-interior sector is180. Exactly one native90 guest corner
   must fill the wedge. This is forced locally without edge-to-edge
   assumptions elsewhere.

3. **A usable guest in a mixed120/135 wedge.** Every native90 of P has far
   neighbors120/120, and every native90 of Q has far neighbors135/135.
   Reflection only interchanges these arms. Once both endpoints are
   forced to coincide with the host endpoints, one host/guest pair is
   necessarily120+135, leaving105. There is no way to fill105 with the
   palette90,120,135,180. The other equal-endpoint sum may be legal; the
   one forbidden endpoint is sufficient.

4. **Endpoint orderings and the aligned containment countercase.** A P120
   endpoint cannot lie inside Q's side (remainder60), or coincide with
   Q90/Q135 (remainders150/105). For a P120-120 side, any positive overlap
   consequently puts Q inside P; some Q135 endpoint then lies in a P flat
   side and leaves45. Thus only a P90-120 side is possible. Normalize it
   to `[0,L]` with P90 at0. The Q right endpoint is strictly in `(0,L)`
   and must be90. Q's left endpoint is135 and may be **less than or equal
   to0**. Equality gives the aligned containment configuration: P90+Q135
   leaves135 at that endpoint, so it cannot be discarded. In both the
   strict and equality cases, the internal Q90 point has an exterior90
   wedge whose host arms end at P120 and Q135. Attack3 kills both.

The initial informal proof omitted the equality case. Root supplied that
countercase before this reviewer received the frozen repaired record.
The reviewed proof explicitly retains it, and the independent checker
requires an aligned representative to survive the first endpoint gate.
No further repair was needed during this review.

## Independent finite proof audit

The independent checker exhausts the ordered P and Q native side angle
pairs and all weak orderings of the four endpoints. It represents each
interval category by two values below the P interval, its left endpoint,
two values strictly inside, its right endpoint, and two values above.
Two representatives per open category suffice because there are only two
Q endpoints. These are order representatives, not sampled metric values.

There are198 positive-overlap representative cases. Seven survive the
first local endpoint angle gate. Reversing the common line when needed,
every survivor has P endpoint angles90/120, Q endpoint angles135/90 and
`q_left<=0<q_right<L`. Thus the complete surviving domain is precisely
staggered host switch or aligned Q containment. The checker separately
verifies the mixed-wedge failure for both arm orders of all four native90
corners. It passed with assertions enabled:

    PASS: 198 positive-overlap endpoint order/side-word cases; 7 interval representatives survive first gate; all normalize to staggered or aligned Q containment and die at mixed120/135 wedge

The universal theorem relies on the written interval and wedge proof,
not on extending a finite geometric patch. The independent certificate
verifier also passed the exact atom convexity/angles, partial seam,
eleven-corner parent area, two reflex turns and all eight oriented native90
corner keys. Its certificate checks the fixed geometry and local palette;
it does not replace the all-metric interval proof.

## Corollaries and limits

For a fixed finite compact protoset, bounded diameters and positive minimum
area imply local finiteness. A compact path between tile interiors can be
perturbed to avoid the finitely many native vertices; crossing an edge at
a nonvertex yields a positive-length contact. Hence positive-contact
adjacency is connected. The no-mixed-contact theorem therefore implies
that a plane tiling by this pair uses one species throughout.

For the displayed fixed P, cyclically rotate its side list so the edge of
length1 has direction0. Its Cairo side directions become0,90,150,240,300
and lengths `(1,7/sqrt3,1/sqrt3,3,2)`. The four right-corner arms are
pairwise distinct, so the reviewed
[Cairo monohedral theorem](../lemmas/partial-contact-cairo-monohedral-classification.md)
applies and excludes P-only tilings. This dependency was checked for
applicability, not re-proved. Q-only existence remains open here. A bounded
failure of a selected Q lattice search is not used as a theorem.

The proposed `b>3` metric repair retains the same angle word and therefore
the same mixed-wedge obstruction. No quotient growth, additional child
search or further side-length tuning can repair this **particular**
angle-word mechanism. Changed neighboring angles at a native90 corner,
or a changed flat-angle palette, are outside the exclusion.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-fractional-resection-2026-10-14-mixed-parent-review.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/mixed-partial-parent-2026-10-14-verify.py
