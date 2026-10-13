# Hostile review: straight collapse and shared-edge exterior-budget obstruction

Date: 2026-10-13. Reviewer: terra, independent of author luna.
Claim reviewed: research/lemmas/penrose-dual-straight-collapse-shared-edge-obstruction.md.
Verdict: VALID on the explicit fixed-fixture degree2/3/4 domain, including the
existential open-parameter consequence. Replay completion recorded below.

## Assumptions and model checked

The35 retained source points and their original incident rays are fixed at
tau=1/100. Degree2 is admitted only for an exactly opposite pair; degree0/1,
new nodes/cuts/rays and source changes are excluded. Actual final faces are
convex polygons in two congruence classes. Straight contraction is interpreted
as concatenating two retained collinear original segments, so each original
edge still has a well-defined retained bit at both endpoints. Source fixture
occurrence is an explicit premise, not a theorem about every Penrose source.

## Attacks on exact local domains and trace

1. Approximate collinearity could spuriously add collapse: the independent
   checker normalizes exact algebraic ray quotients and accepts only phase-1.
   All ten listed points and all opposite-pair options are reconstructed.
2. Degree2 angles might be counted as native corners: both sectors arepi and
   their angle-ID set is empty. Contraction consumes no exterior deficit.
3. Independent-choice reduction might miss helpful repeated signatures: any
   actual selection restricts to one point per signature; extra selected
   points only enlarge the required union. Thus2025 products are a sound
   relaxation. The minimum605 lower bound indeed permits an actual union
   deficit<616<720 using the certified strict floor+1 upper bounds.
4. Shared-edge constraints could be too restrictive after contraction: an
   actual retained segment, even as part of a contracted longer side, remains
   at both endpoints of its original source edge. Omitted edges are omitted
   at both. Added fractional segments or chords would change the hypothesis.
5. Arc removals could trust a solver or omit a currently available support:
   each of the40 steps is rechecked against the ENTIRE current neighbour
   domain, and its removed IDs equal all unsupported source choices. The
   neighbour-domain snapshot is verified before deletion. Every removal is
   a sound necessary consequence for all globally consistent assignments.
6. Unconstrained outside neighbours could invalidate deletion: only constrained
   neighbours among the35 points enter support pruning. This relaxes the
   global source; it cannot remove a genuine compiler solution.
7. Forced-angle union could rely on one arbitrary survivor: it uses intersection
   over every remaining choice at each point, followed by union over points.
   The checker reproduces final domains and every intersection. All11 forced
   phases are distinct positive native angles, and exact floor cost750>720.

## Continuity attack

A finite common interval preserves strict point interior, crossings, ray order
and every formerly reflex rejection. Nonopposite old pairs remain nonopposite;
old opposite pairs may cease to be allowed, which only removes options. Old
pi-gap choices already occur in the degree3/4 list: opening one to a positive
angle adds nonnegative deficit, while becoming reflex deletes that option.
Hence every nearby actual option maps to an old option and must survive the
same40 retention-bit removals.

The forced positive old angle labels persist in nearby actual options. There
are finitely many sector functions and26 distinct old phase values, so one
common interval makes different old labels occupy disjoint angle intervals.
Splitting one old label into several nearby values cannot merge different
required labels or reduce their selected budget. Each selected deficit is
strictly greater than its old integer floor minus1. The11 representatives
therefore cost>750-11=739>720. This is a valid existential interval proof;
no uncomputed numerical epsilon or whole-parameter-family coverage is claimed.

## Defects, repairs and limits

No consequential defect or repair found. No matching-deletion, pairwise fusion,
old degree3/4 curvature identity or bound on partner side count is used.
Degree0 point removal, added cuts/rays/nodes, source change or distant parameters
are outside the result. The independent relaxed605 pass is not an infinite
construction; the40-step750 contradiction excludes precisely the changed
fixed-source compiler. The CP-SAT1286 exploratory value is not load-bearing.

## Nondestructive exact replay

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_collapse_shared_edge.py

PASS: reconstructed geometry and26 floor bounds; ten straight-collapse points;
2025 independent products with605 minimum;40 sound deletions and11 forced
angles with750 sum. No new source, budget search or solver invocation was run.
