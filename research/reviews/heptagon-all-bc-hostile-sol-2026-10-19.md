# Hostile review: universal all-BC heptagon carrier

Reviewed 2026-10-19. Verdict: **valid with the stated four unit public sides**. Reviewed the search note, Python verifier and JSON certificate independently of their author. No Git or discovery-log edits.

## Quantifiers and metric scope

The theorem covers every actual closed strictly convex Q with the specified angle word and lengths of sides 0,2,4,6 equal to one. The other three lengths are arbitrary positive solutions of closure. It does not fix their equality or a special member of the one-dimensional closure family. Without the four unit conditions, the asserted construction fails: a PQ seam must match a unit P edge. Scaling a valid Q alone illustrates this omitted restriction. The final note explicitly supplies the restriction and states the tiling consequence conditionally on the separately derived full-edge PPA/PBC gate. This review does not independently prove that gate for every exceptional angle.

For Q side0 at heading zero, the turn across each ordered BC or CB pair is 360-(B+C)=108 degrees. Thus the four public headings are exactly 0,108,216,324. The intermediate headings are 180-a1,288-a3,396-a5. The difference of the first two is 108+a1-a3, strictly between 72 and 144 degrees; its sine is positive. Therefore the displayed two-by-two closure solution has rank two throughout the interval. Its three strict affine inequalities describe all and only positive solutions. Positive turns with total 360 and closure imply a simple strictly convex polygon; this is also a hypothesis of the main theorem. No positivity assertion for an untested parameter is needed.

## Word, endpoint and reflection audit

There are eight choices of three ordered complementary pairs. Rooted reversal sends (x,y,z) to (opposite(z),opposite(y),opposite(x)); it has no fixed point because the middle pair changes. Its four representatives are exactly ABCBCBC, ABCBCCB, ABCCBBC, ACBBCBC. Among all balanced words rooted at the unique A there are twenty arrangements and ten reversal classes; six classes remain outside this result.

Every dart occurs in exactly one listed seam. Boundary orientation is reversed on each seam, so a dart u beginning at vertex u is joined to the endpoint of its mate v, and next-after-mate gives the stated vertex cycles. Two cycles contain the A corners and two P corners; the other six contain P and complementary members of one of the three ordered pairs. In particular the labels remain complementary when a pair is CB. PP and PQ lengths are unit. The three QQ seams join local sides 1 to 1, 3 to 3 and 5 to 5 of congruent Q copies, so their lengths match independently, with no permutation or equality of the three QQ lengths.

The symbolic heading equations agree with P0 rotation 0, P1 rotation 108, Q0 rotation 180 and Q1 rotation 0. For every listed seam the developed directed sides are opposite; endpoint reversal is consistent with these phases. Arbitrary Q need not have reflection symmetry. This creates no defect: the witness uses two direct copies, and reflecting the entire witness realizes the reversed word and reflected metric. The theorem is a positive construction and does not require enumerating all independently reflected face arrangements.

## Global geometric audit

The quotient of the four closed polygon disks under these full-edge isometries is connected, compact, oriented and without boundary. Every open edge has a disk neighborhood. Each vertex equivalence class has exactly the single circular link given by its three-cycle, with total angle 360 degrees. Consequently each vertex has a flat disk neighborhood as well. This produces an actual nonsingular flat surface, rather than an overlapping picture of prescribed coordinates. Its Euler characteristic is 8-12+4=0.

The induced length metric is complete by compactness. The simply connected complete flat universal cover is the Euclidean plane. The lifted polygon cell decomposition covers that plane exactly once: open faces are embedded and disjoint, and their closures cover. A convex face disk lifts injectively, so this statement concerns ordinary congruent polygon tiles. Deck transformations preserve orientation and act freely. An orientation-preserving Euclidean isometry that is not a translation has a fixed point, hence every nonidentity deck transformation is a translation. Discreteness and compact quotient give a rank-two lattice.

This establishes nonoverlap, coverage and nonzero periods for every permitted metric without an explicit seam determinant or a bounded translate test. In particular the lattice cannot collapse or become rank one at an interior positive parameter: that would contradict the compact nonsingular flat quotient just constructed. The area of the quotient is the positive sum of the four face areas; universal development has degree one. No hidden metric parameter is fixed.

## Replay and certificate limits

Replay completed successfully:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/heptagon-all-bc-qdimer-sol-2026-10-19.py

The Python verifier checks exact affine angle sums and heading compatibility for all eight pair choices modulo rooted reversal, and regenerates the stated JSON. Its arithmetic has no sampled alpha values. It does not itself prove the metric positivity formulas, flat-surface classification or universal-cover theorem; those are the analytic arguments audited above. Its unused Fraction import is harmless. The positive carrier theorem and its conditional tiling consequence are valid within the explicit scope. No claim about the six other balanced reversal classes follows.
