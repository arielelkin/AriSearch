# Fixed generic A001122 fixture forces a periodic escape

Date: 2026-10-13. Author/reviewer: sol, independently reconstructing terra's
producer and retained exact certificate. Status: independently checked and
reviewed finite gate; proof internally complete. This is a FIXED-FIXTURE
theorem, not an all-angle or all-metric001122 classification.

## Theorem

Let A be the exact strictly convex hexagon defined in
[the reviewed AAA counterexample](../counterexamples/terra-generic-aaa-does-not-force-monohedral.md),
with native angles(113,113,121,121,126,126) and its specified determinant-kernel
side word(a,a,b,b,c,c), with three pairwise distinct positive classes. Let B
be any actual strictly convex hexagon with two angles each134,118,108, in any
native order and with arbitrary actual side lengths. If {A,B} tiles the plane
under unrestricted contacts and reflected placements, it admits an admitted
periodic tiling using B alone. No mixed infinite extension is asserted.

Dependencies: the previously reviewed defect-free hexagon limit and
unrestricted monohedral hexagon theorem; the generic ternary star language
and B-B propagation; and the freshly reviewed fact that this A cannot tile
monohedrally. The exact positive A coordinates and full-copy AAA patch are
retained in the linked counterexample. These dependencies are not re-audited.

## Necessary local B metrics

Every admitted source tiling supplies a connected defect-free trivalent
edge-to-edge limit. If pure A, it contradicts the reviewed monohedral exclusion.
If pure B, the monohedral theorem already supplies a periodic escape. In a
genuinely mixed field the generic no-ABB language eliminates every B-B edge,
so every B side meets an A side and every B vertex is same-colour AAB.
At each endpoint of an AB side, B colour agrees with the incident A colour.
Consequently its length is determined by its unordered endpoint-colour pair:

    00,01 -> a; 11,12 -> b; 22,02 -> c.

These six pairs exhaust all B edges, including equal-colour edges. There is
no additional scale freedom: actual whole-side equality forces the displayed
length from the fixed A polygon. Reflection does not change an unordered pair.

The same-colour AAB arm tests permit precisely these ordered B arm pairs:

    colour0: (a,a),(a,c),(c,a),(c,c);
    colour1: (a,a),(a,b),(b,a),(b,b);
    colour2: (b,b),(b,c),(c,b),(c,c).

These follow by choosing either native same-colour A corner, reversing either
arm order, matching the common AA arm, then recording the other two arms.
They are necessary local conditions; satisfying them need not extend.

## Complete exact fixed-angle closure gate

There are eleven dihedral bracelets of two copies of each of three labelled
colours. All are tested, with no permutation of angle names. Every bracelet
has its unique side-class word from the six-pair palette, and passes the
necessary fan tests. Set the first B edge direction0 and successively add
180 minus its next native angle. Exact closure is then the sum of those six
forced lengths times their direction units. The retained certificate and an
independent Q(zeta720) checker reconstruct all eleven sums; precisely
native012012 closes. Every other exact residue is nonzero at this FIXED
angle/metric fixture. No all-angle nonzero assertion is inferred.

The surviving B length word is(a,b,c,a,b,c). Its opposite angles and opposite
lengths agree; its opposite edge vectors are negatives, so it is centrally
symmetric. Exact strict support inequalities confirm that candidate B is an
actual positive strictly convex polygon. The standard convex central-hexagon
translation theorem supplies its plane periodic tiling, with A omitted.
This is a monohedral escape, not an extension of the mixed neighbourhood.
The preceding pure/mixed cases prove the theorem.

## Evidence and scope

[Producer](../searches/terra-001122-b-neighbourhood.py),
[retained certificate](../certificates/terra-001122-b-neighbourhood.json),
[independent no-author-import checker](../reviews/verify_terra_001122_b_neighbourhood_independent.py).
The checker uses a different cyclotomic field from the producer, independently
reconstructs the reflected fans and palette, verifies eleven closure outcomes
and the survivor's24 strict supports. Domain: one exact A polygon and eleven
forced B word/metric assignments; no solver, random seed, timeout, numerical
acceptance or bounded-to-infinite inference. Omitted non-forced B metrics
are excluded by necessary whole-side endpoint matching, not an enumeration cap.

Nondestructive replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001122_b_neighbourhood_independent.py

Outcome: PASS. The broad generic001122aabbcc mechanism remains unclassified;
an all-angle closure proof would be a distinct obligation. Other A metrics,
other native A words, extra-star angle strata and the original research target
remain unresolved. Increasing sample metric bounds would not prove that
all-angle claim; symbolic closure is the justified next question.
