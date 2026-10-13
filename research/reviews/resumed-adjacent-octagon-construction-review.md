# Independent hostile review: adjacent-alpha six-face covering

Date:2026-10-13. Verdict: **VALID** for the exact singleton construction.
Reviewer developed the necessary metric equality obstruction, not this
positive covering or its producer. The witness was independently verified
by a different overlap method.

Reviewed [construction](../searches/resumed-adjacent-octagon-construction.md)
and [producer](../searches/resumed-adjacent-octagon-check.py).
Independent verifier:
[resumed_higher_adjacent_octagon_verify.py](resumed_higher_adjacent_octagon_verify.py).

## Claims, hypotheses and attempted failures

The two shapes have respectively five108 corners and an eight-corner
108,108,144,144,144,144,144,144 word. The six-face motif uses precisely
4 isometric P and2 isometric Q copies, including the stated reflections
and half-turns. Nonzero independent vectors S,T repeat it over the entire
plane. The AA side equals a BB side exactly; repeated lengths outside the
original private-side gate are intentional. No symbolic source rule is used.

I checked boundary orientation under reflections, exact algebraic rotation
and closure, genuine convexity, Q-chain translation, motif congruence,
complete relative-translation ranges, area-to-coverage and monohedral
omissions. No unaddressed defect found.

## Independent geometric verification

The independent Sage checker never imports or executes the producer. It
constructs the direction vectors recursively by exact complex-coordinate
multiplication rather than matrix powers, then reconstructs the six motif
polygons from the exact formulas. Every consecutive turn is strictly
positive, actual cosine values agree with the stated words, and AA/BB
lengths are both1. It checks sum of six positive areas equals S_x*T_y>0.

For each ordered pair it derives all integer bbox-eligible relative
translations, without symmetry reduction. Outside these closed ranges
one coordinate interval is disjoint, so interior overlap is impossible.
All44 remaining pairs are checked by a separating-axis criterion using
all supporting edge lines of both convex polygons. An exact weak separating
line exists for each pair, proving their interiors disjoint. This is
independent of the producer's Sutherland-Hodgman clipping algorithm and
avoids trusting its computed intersection area. Repeated boundary vertices
or segment-only contacts do not cause trouble for the separating-axis test.

The all-translates check reduces correctly to comparing unshifted motif
polygon A with B+mS+nT; applying a common lattice translation handles any
two copies in the infinite family. The sole skipped case is a tile against
itself, not two different occurrences. Strictly positive tile areas and
this check also rule out coincident motif copies.

The coverage proof is valid. This finite lattice family is locally finite,
so its union is closed. The sum of tile areas per quotient rectangle is its
covered area because intersections have zero area; periodic multiplicity
integration accounts for polygons crossing the rectangle boundary. Since
the sum equals rectangle area, no open hole can remain. An absent point
would lie in a positive-area open hole, contradicting the integral. This
argument proves full-plane coverage, not merely area density or finite
patch extension. Both lattice vectors preserve the actual tile occurrence
set, decisively rejecting aperiodicity.

## Singleton omission and scope

All-obtuse forcing covers reflections and arbitrary partial contacts and
forces trivalent full-side stars. Their only angle sum is108+108+144.
For P alone no beta angle exists, so every native star is impossible.
For Q alone finite-window corner counts would require2N_Q=12N_Q+O(R),
hence N_Q=O(R), contradicting plane coverage. No monohedral classification
or prior periodicity theorem is needed.

Thus both shapes individually fail to tile while their pair tiles doubly
periodically. This establishes exactly the claimed positive escape from
the necessary equality obstruction. It does not classify arbitrary metrics
on the equality locus or establish any universal periodicity theorem.

## Replay and verdict

Both commands completed exit0:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resumed-adjacent-octagon-check.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed_higher_adjacent_octagon_verify.py

Producer reports44 complete bbox overlap checks. Independent verifier
reports44 exact separating-axis tests, complete translate domain, two
classes and AA/BB equality. No parameter search, numerical tolerance or
solver result occurs. No repair was made and no novelty claim is reviewed.
