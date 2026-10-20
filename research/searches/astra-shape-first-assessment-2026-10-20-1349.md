# Independent shape-first assessment, 2026-10-20 13:49 UTC

**Unresolved.** No current pair has proved plane existence and unrestricted aperiodicity. This assessment reads the governing documents, discovery-log opening, deduplication audit, 12:59 assessment, six-template P5/Q8 report, branching local obstruction, P5/Q7 self-cap report, asymmetric P5/P5 report, and second-round hostile review. It makes no literature novelty claim. No discovery-log edit or subagent work was performed.

## What changed

The previous assessment's two proposals have now reached their prescribed gates. This is useful falsification, not progress toward a surviving tiling.

* Four exact P5/Q8 representatives are independently reviewed **plane-nontilable**, by compulsory twelve-P components and incompatible Q caps. The two branching representatives now have a stronger author proof: every neighborhood of one P fails because the mandatory Q caps at P vertices 1 and 3 overlap. Their independent-review status remains pending in the materials read. All six fixed metrics should be closed to constructive patch growth; review the last proof rather than enlarge the patches.
* The asymmetric P5/P5 metric realizes its unequal split and simultaneous endpoint completions, but both whole-host P/P alternatives also have simultaneous endpoint completions. The key forcing test failed. Neither the angle words nor the whole continuous metric family have been excluded.
* The P5/Q7 self-cap pair survives some immediate attachments after the corrected orientation audit. The exact four-face torus exclusion is substantive within its domain, but supplies neither an infinite tiling nor a constraint on larger or partial-contact periods. Stop this metric until a genuinely new extension or contact invariant is available.

The search has repeatedly selected metrics by fitting one seam, then discovered that the other compulsory seams are incompatible. The next assembly should therefore begin with a complete junction having several exits, or with a mixed-species contact whose side-interior continuation is itself explicitly closed. A longer strip or a higher denominator in the old ring is not such a change.

## Proof audit priorities

For the branching P5/Q8 obstruction, independently reconstruct both algebraic metrics and verify the complete side-length inventory, all 16 neighbor choices, all third-corner species, and both reflected Q placements. A residual sector might contain P rather than Q unless its angle and incident lengths exclude that possibility. Equal image polygons must be identified before treating overlap as a contradiction. Check that the two P neighbors are distinct and that excluding overlapping P neighbors only removes impossible branches. The author's vertex-1/vertex-3 universal conflict is sufficient; no torus search or larger neighborhood is needed.

The old review's statement that two branching metrics remain unresolved is chronologically superseded by the new author claim, not yet by a reviewed theorem. Keep those statuses distinct. The 2P+Q UNSAT computations have no separately checkable UNSAT certificates; they are not needed for the four reviewed nonexistence proofs. Likewise the pentagon classification filter is not needed for P5/Q8 omission: a P100 corner cannot meet two P corners totaling 260, and a Q150 corner cannot meet two Q corners totaling 210.

For P5/Q7, unrestricted partial contacts remain a material gap. Its all-obtuse partner alone does not prohibit a mixed T junction, because P60 can meet Q120 or P120 if present; here Q120 is available. The reviewed four-face quotient exclusion must retain its full-edge qualifier.

## General diagnostic: deterministic seam orbits

Suppose a polygon placement has a compulsory successor obtained by a fixed relative isometry g, and the same state and successor rule recur. Starting from placement f, successors are f g^n. If g is orientation preserving with nonzero rotational part, every orbit lies in a bounded region about its rotation center. A bounded region contains only finitely many disjoint congruent positive-area polygons. Therefore an infinite sequence of distinct successor tiles is impossible. A rational rotation can return exactly and form a finite component; an irrational rotation must force an overlap before any return. If g is a reflection it has order two; if it is a glide reflection, its square is a translation. A pure translation is the other unbounded possibility.

This is an elementary diagnostic, not a new impossibility theorem for two tiles. In particular, varying the old P seam angle away from 30 degrees does not manufacture an aperiodic chain: it either changes a finite ring or creates bounded-orbit incompatibility. A productive successor system needs genuinely changing states or a nontrivial branching rule. Even then an unbounded chain proves neither plane coverage nor aperiodicity.

## New route A: a three-arm P5/Q9 hub

This changes the side-count balance and junction topology. It is an exact proposed pair, with closure and positivity checked, but its hub has not yet been tested for overlap.

Write u(t)=(cos(t degrees),sin(t degrees)). Define positive algebraic b,c by

    b (u(144)+u(276)) + c (u(72)+u(216)) = -u(0).

The coefficient matrix is nonsingular. Exact Sage AA evaluation gives b=0.790943073464693... and c=0.8855793519707398..., both positive. Starting at the origin, integrate the following directed edges:

* P angles (96,108,108,108,120), directions (0,72,144,216,276), lengths (1,c,b,c,b).
* Q angles (156,144,120,156,144,120,156,144,120), directions (0,36,96,120,156,216,240,276,336), lengths (1,b,c,1,b,c,1,b,c).

These are exact coordinates in the real/imaginary parts of the 30th roots of unity. P closes by definition; the three Q edge blocks are rotations through 120 degrees and sum to zero. Positive lengths and the ordered turns give strictly convex polygons. Q has threefold rotational symmetry. All corners exceed 90, so every tiling would be trivalent and edge-to-edge, including the unrestricted problem's contacts. Neither species can tile alone: P96 belongs to no all-P star, and Q156 belongs to no all-Q star.

**First finite gate.** Attach P side 0 to Q sides 0,3,6, placing P96 against Q156 and P108 against Q144. Enumerate actual reflection choices and check the three P arms against one another and Q. At each Q156 endpoint the residual angle is 108, with outgoing lengths c and b: P corner 2 has precisely those incident lengths. At each Q144 endpoint the residual angle is 108, with outgoing lengths b and c: P corner 3 supplies them. Enumerate every P108 corner with matching exact lengths, all reflections and radial orders, rather than only these named choices. Develop all six endpoint completions, identify coincident tile images, and test pairwise exact nonoverlap. This is one complete prescribed hub gate, not an expanding patch search. Stop this metric immediately if the hub is impossible.

If a hub survives, record its exposed sides and the exact alternatives for connecting its three arms. It earns a second gate only if the surviving geometry supplies a changed-state continuation between hubs. Attack that observed continuation with a 3P+Q carrier first. The angular triples are (96,108,156), (96,120,144), (108,108,144), (120,120,120). For 3P+Q their counts are uniquely (3,0,3,2), checked by exact linear algebra. That is bookkeeping, not a glued torus. In an arbitrary infinite tiling a zero density conclusion would not by itself exclude isolated defects; do not turn the zero count into an unrestricted local prohibition.

This pair is not a reparameterization of the six P5/Q8 templates, the stored P5/Q7 metrics, or a private-edge two-exit dimer. Its intended mechanism is a multi-exit junction. No plane extension or forced hierarchy is claimed.

## New route B: a mixed-species midpoint with an explicit outgoing offset

The prior split placed two copies of Q against a P host. This experiment makes the midpoint intrinsically mixed: a P120 corner and Q60 corner meet along a Q host. It does not yet force that split, and should be stopped at the first failed continuation.

Use P angles (72,96,120,132,120), directions (0,84,144,192,252), and lengths (p0,1/5,1,1/5,p4), with

    p0 u(0) + p4 u(252) = -u(144) - (u(84)+u(192))/5.

Use Q angles (60,84,144,108,144), directions (0,96,132,204,240), and lengths (2,q1,q2,1/5,3), with

    q1 u(96) + q2 u(132) = -2u(0)-3u(240)-u(204)/5.

Exact AA checks give p0=1.225840857236482..., p4=0.7834521718069352..., q1=2.649081777939740..., q2=0.06035661912531940..., all positive. Both polygons close and have ordered strictly convex turns. The definitions are algebraic in 60th roots of unity. Neither angle word has adjacent supplementary corners, but the complete monohedral-type filter is still required; absence of that easy carrier is not a full omission proof.

**First finite gate.** On Q host side 4 of length 3, put P side 2 of length 1 and Q side 0 of length 2, meeting at P corner 2 (120) and Q corner 0 (60). Enumerate both segment orders and all reflection choices. The residual midpoint rays must coincide. Their lengths are P1=1/5 and Q4=3, so the short ray ends at a named additional side-interior vertex after distance 1/5. Require an explicit compatible completion there, not just at the two host endpoints. Thus this experiment tests the previously deferred outgoing offset as part of its first gate.

In the order with P at the host's Q144 endpoint, the endpoint gaps are 84 (Q144+P132) and 216 (Q60+Q84). The 84 gap has Q's native 84 corner; 216 can use two Q108 corners or P96+P120, among other sequences to be enumerated. The minimum corner is 60, so there are at most six full corners in a 360-degree star; include flat sectors wherever allowed. Develop simultaneous exact completions, including the named short-ray endpoint, and compare all Q/Q whole-host alternatives. If the local patch fails, either species has an omission carrier, or whole-host seams remain interchangeable without an explicit successor distinction, stop the metric. No larger patch of the earlier asymmetric pair is proposed.

This second route is lower priority than the Q9 hub because partial contacts create additional offset obligations. Its advantage is a precise new obligation to falsify: the short outgoing seam ends on a known long side, so the next contact can be audited immediately instead of postponing it to global forcing.

## Recommended allocation and reproducibility

First complete independent review of the two branching P5/Q8 obstructions. In parallel only if an available worker is already authorized, attempt the Q9 hub gate. Use the mixed-species midpoint as the independent fallback. Do not run a new angle grid, enlarge any stopped fixed metric, or infer progress from another bounded torus exclusion.

The small checks in this assessment used the prescribed arisearch environment, Sage AA for both two-by-two closure systems and positivity, and exact SymPy linear algebra for Q9 star counts. Exploratory SciPy feasibility checks were used while selecting the second proposal, but no floating-point result is part of its stated positivity claim. The proposed assemblies have not been developed or independently reviewed. Their next action is exactly the finite geometry gate stated above, not a claim that either tiles.
