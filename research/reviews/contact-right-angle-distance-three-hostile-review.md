# Fresh hostile review: exact distance-three native pair exclusions

Date: 2026-10-13. Independent reviewer: contact_structure.
Artifact: [native analysis and universal-period argument](../searches/contact-right-angle-distance-three-native-analysis.md),
[distinct-private ring producer](../searches/contact-right-angle-distance-three-local-ring.py),
[equal-private ring producer](../searches/contact-right-angle-equal-private-distance-three-ring.py).
Verdict: VALID for the two exact stated metric pairs. The first is untileable;
every admitted tiling of the second has a nonzero translation symmetry.
No infinite tiling of the second is asserted or proved.

## Exact scope and complete neighbor domain

The P metric is the already independently verified fully asymmetric carrier
pentagon. Its five lengths are distinct and its three possible both-obtuse
flat-host side lengths avoid 2u and 2v. The reviewed unrestricted native
reduction therefore makes every admitted tiling edge-to-edge. Because Q has
no side of P bevel lengths x,y, the P-Q-P-Q-P species word is impossible;
every P has exactly three whole Q neighbors, with native lengths u,v,w.
The two private Q slots are0,3. They fix the whole QQ mask, since the local
native-word theorem permits at most two QQ slots.

The first metric has distinct private lengths, so each QQ attachment uses
its own native slot. The second has equal private lengths, so both native
slots0,3 are explicitly tried and geometrically identical vertex sets are
quotiented. Every isometry mapping a candidate native side to a fixed Q side
is one of the two endpoint correspondences times the two orthogonal frame
choices; inward placements are rejected by positive-area overlap with Q.
This is complete, including reflections. Public u/v attachments are filtered
by their unique acute endpoint, which necessarily meets the neighboring QQ
slot; w attachments keep both choices. The resulting choice counts
[2,1,1,2,1,2,2,1] give all16full rings for each exact pair. No template, arbitrary
orientation restriction or periodic quotient is imposed.

## Independent exact ring and rigid-map checks

A new [independent checker](contact-right-angle-distance-three-ring-check.py)
reconstructs P,Q in Sage AA radicals, checks every strict support halfplane,
enumerates endpoint/frame maps and replaces the producers separating-axis
predicates by exact convex-polygon clipping. It also independently checks
native vertices in the relative interiors of other native sides. It passed:

    mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/contact-right-angle-distance-three-ring-check.py

The mixed short-gap metric has zero valid rings out of16. The equal short-gap
metric has exactly one, and its private neighbor SHAPES equal the explicit
S(Q) and T(Q) in the record. The checker independently verifies M squared
identity, determinant -1, ST(Q)=Q as an exact vertex set, and the explicit
nonzero translation vector of S squared. These checks do not rely on the
producers number field or option ordering. The equal-private producer was
also replayed successfully, matching its stated choices and rigid maps.
Retained certificates are [mixed](../certificates/contact-right-angle-distance-three-local-ring.json)
and [equal](../certificates/contact-right-angle-equal-private-distance-three-ring.json).
They record exactly these finite16-ring domains, not infinite tilability.

The mixed short-gap analytic obstruction agrees with the computation:
the two P neighbors forced at that central Q vertex have incompatible whole
PP-side lengths x and y. Both far endpoints are P112.5 and cannot lie inside
a side, so partial matching cannot evade the inequality. This pair is
untileable under the original unrestricted convention.

## Unique-ring propagation and universal period

For the equal-private pair, uniqueness concerns the geometric neighbor ring,
not indexed representatives. Any Q symmetry sends a legal ring to another
legal ring and therefore fixes this unique geometric ring. Transporting it
by any actual placement is thus well defined. If a plane tiling exists,
S transports the reference Q and its ENTIRE neighbor ring onto its Q neighbor
and that neighbors actual unique ring. ST(Q)=Q implies T(Q)=S inverse(Q),
so the whole QQ component is S to the integer power applied to Q.

S squared is translation by nonzero d. All iterates of Q are distinct:
a repetition would imply compact Q invariant under a nonzero multiple of d,
either immediately for an even repetition or after squaring an odd one.
Each component and all its P neighbor tiles are consequently invariant under
d. This uses actual ring uniqueness; no locally legal ring is assumed to
extend globally.

The centroid/shared-side-midpoint path is a proper simple line inside its
Q chain. Same-chain tiles meet only along their graph-adjacent whole sides;
nonneighbor Q point contact would itself give a QQ side by the complete star
language. Periodicity gives a finite two-tile motif at bounded distance from
a line parallel to d and two opposite infinite ends. Disjoint chain cores
cannot have nonparallel asymptotic lines: proper-arc Jordan separation puts
the far halfplanes on opposite sides, so a nonparallel second core would
connect those components and have to cross the first. Its path cannot cross
another Q-chain interior or internal QQ seam. Thus all chain vectors are
parallel. They are isometric images of the same d and have equal nonzero
length, so the common vector up to sign is a period of each chain together
with its P neighbors. Every P has three Q neighbors, hence these decorated
chains exhaust every tile in the actual tiling. Their common vector is a
period of the ENTIRE tiling; no finite-state P completion step is needed.

## Limits

The first finite census is an emptiness proof because every admitted tiling
would supply one of the enumerated rings. The second finite census plus
reviewed propagation/barrier argument proves a universal symmetry conclusion,
not existence. An empty tiling space is not presented as an aperiodic pair.
No arbitrary distance-three metric classification, general two-private-family
theorem or novelty assertion is imported. No unresolved objection remains.

Both retained certificate replay commands with --check completed exit0 after
certificate metadata/output support was added: mixed valid count0, equal
valid count1, sixteen rings each. The independent AA/clipping checker remains
separate from those producer recomputations.

A later checker audit found that reflected neighbor vertex lists can be
clockwise. The independent clipping helper now normalizes the clip polygon
to counterclockwise order before using left halfplanes. Its corrected replay
passed both complete16-ring domains with the same0/1 results and rigid maps.
The orientation-independent producer predicates and analytic proofs were
unaffected. The current independent verifier includes this repair.
