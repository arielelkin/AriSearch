# Independent repaired true-host obstruction audit

Date: 2026-10-13. Reviewer: root, separately from source author and contact's
repair proposal. Verdict: VALID for the single exact four-equal fixture.

Reviewed [repaired complete proof](../lemmas/contact-non-equiangular-four-equal-true-host-obstruction.md)
and [exact producer](../searches/contact-non-equiangular-four-equal-true-host.py).
All reflections, partial contacts and species omission remain allowed.
No local cap or far-Q extension is promoted to plane existence.

The new [independent checker](contact-non-equiangular-four-equal-independent.py)
imports no author code and uses a quartic field plus orientation-independent
separating-axis projections instead of clipping. It reconstructs both closed
strictly convex prototypes, their unique physical hosted cap, and all eight
native two-edge Q135 isometries modulo actual geometric equality. Precisely
four far-Q polygon placements remain, and every four-tile patch has disjoint
interiors. It independently enumerates the complete seven full and one flat
native stars and verifies every weight, including per-tile totals. It passed.
Thus the corrected CCW clipping repair did not change the claimed positive
patch counts, and those counts now have an independent geometric control.

The original M-QQ exclusion omitted an angle-compatible V mate. The repaired
proof treats all endpoint types: a U mate supplies an impossible157 sector;
a M mate supplies135 where the fixed Uguest already has112.5; a V mate
supplies112.5, which fits the angles but places its private length-two H
edge against the Uguest's length-one P bevel. That bevel has112.5 at both
ends, so its far endpoint cannot lie inside H. Nor can the Q endpoint lie
inside the P side. This eliminates the missing case. The actual Uguest is
forced by the already-classified private H contact: H is either its
midpoint half-turn QQ mate, or a two-unit-leg hosted cap, in both cases
putting P90 against U at its157 endpoint. Its far endpoint is therefore
P112.5, as used. No circular assumption about U being Pcontact is made.

Consequently no QQ135/135 acute star occurs. Every Q157 contributes exactly
one distinct P90 occurrence. Counting those, two per cap and four per quad
gives p=2q+2h+4z+O(R). Independently, the full/flat weights give
p=2q+h+2z+O(R). Boundary errors are uniform from positive areas and bounded
diameters. Nonnegative h+2z therefore has a uniform linear bound; clean
growing disks exist.

The indexed placement limit preserves coverage and interior nonoverlap.
Isolating finite native-corner clusters preserves zero total star score
through mergers, so positive-score caps and quads do not arise in the limit.
Every private H side must then QQmatch, uniquely by half-turn because a
reflected mate makes157+157 impossible. Its native112/157 corners are
already in P90 stars. Hence all remaining P112 stars are PPQ135 and all
P90 stars are PQQ. Indexed alternation forces the R middle side w to have
Qcontact, but Q has only native lengths1 and2 while0<w<1. This is an exact
whole-side contradiction, establishing untileability of the original field
via the clean-limit implication. No ETE rule or FLC is assumed beforehand.

P-only and Q-only omission are excluded directly by their native corner
angles. The proof makes no all-metric claim. Its remaining uncertainty
concerns other pairs, not this exact fixture.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/contact-non-equiangular-four-equal-independent.py
