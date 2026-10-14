# Fresh review: unrestricted topology transfer of the two-size determinant theorem

Date:2026-10-13. Reviewer source_recovery, independently assigned to synthesis.
Claim: the new unrestricted-topology consequence in
research/lemmas/two-size-pentagon-six-child-wheel-obstruction.md.
Verdict: VALID. No enlarged computation was needed or executed.

## Exact hypotheses preserved

P is a genuine compact convex pentagon of positive area, with FIVE PAIRWISE
DISTINCT native angles and positive native side lengths. Integers b>0,d>=0
satisfy b+d=6. The real mu>1 obeys mu^2=dmu+b; lambda=sqrt(mu).
The parent is mu*P (mu is its LINEAR scale relative to P), and children are
b copies at scale1 and d copies at linear scale lambda. Parent area is
mu^2 area(P), while total child area is(b+d*lambda^2)area(P); hence the
stated quadratic is exactly the correct area equation. No confusion of linear
and area factors occurs. Both child types are convex genuine pentagons, under
reflections as well as direct isometries.

There are exactly six children, each with>=5 sides. The independently reviewed
universal six-child topology theorem applies with unrestricted contacts. It
forces every wheel property required by the old boundary theorem: one central
pentagon, five unsplit original corners, two COMPLETE native rays per corner
child, and each parent side covered by its two endpoint child sides. All
partial-contact / subdivided-corner possibilities are removed by the universal
topology proof, not silently excluded as input assumptions.

## The old determinant/row obligations match the forced boundary

A parent native angle at index i equals its child corner angle; distinctness
forces native index i. A reflection can exchange the two neighboring side
lengths, exactly as the existing reflection bit records. Central-tile orientation
has no effect on necessary outer boundary equations. The central type does
matter for how many large corner children remain and is explicitly represented
in the existing cases.

With parent scale mu and child scales t_i in{1,lambda}, the original boundary
matrix equation is still mu*l=C*l. Row sums<=2lambda give mu<=4. The six count
splits d0..5,b=6-d are unchanged; b>0 forbids an unintended d6 branch. The
four analytic exclusions d0,d1,d4,d5 do not assume any inner geometry. The
d1 maximum1+lambda includes the central-large possibility because then all
corners are small and the actual bound2 is stronger.

For d2 the two central-type cases give320+160=480 corner-type / reflection
patterns; for d3 they give320+320=640. All32 corner reflection patterns remain
necessary and sufficient for enumerating boundary placements. Their polynomials
lambda^4-2lambda^2-4 and lambda^4-3lambda^2-3 derive directly from the same
quadratic area equation. The injective positive field embedding converts the
retained nonzero determinants into nonzero real matrices. No additional scale,
side-closure or interior seam condition is introduced by the topology transfer.

The existing independent certificate audits remain dependencies:
research/reviews/resumed-two-size-wheel-complete-counts-review.md and
research/reviews/resumed-two-size-wheel-review.md. This review did not rerun
the already reviewed1120 domain or expand it. The new step is the analytic
composition of two reviewed theorems, not a new computer-assisted search.

## Attacks and exclusions checked

- Repeated angles remain outside the determinant theorem; the universal
  topology theorem does NOT remove that restriction.
- An arbitrary two-scale relation remains outside: mu^2=dmu+b and
  lambda=sqrt(mu) are retained.
- Reflected children are represented in both the topology theorem and old
  reflection-bit domain.
- A tiling using only one species is not under review; this is a finite
  dissection theorem, not a claimed plane-tiling impossibility.
- Different total child counts do not inherit the reduction.
- A sixth all-large-child branch is absent because b>0 is explicit.

No mathematical gap or quantifier weakening was found in the synthesis.

## Editorial scope clarification

At inspection time the opening original theorem description said it made no
assertion that every six-child partition is a wheel, and the final limits
paragraph listed other topologies as outside. Those sentences describe the
original fixed-topology theorem and should be qualified accordingly; they do
not describe the NEW unrestricted-topology consequence. The root was notified.
The new consequence itself has precise correct hypotheses and remains VALID.
Repeated-angle and different-count limitations must remain in either wording.
